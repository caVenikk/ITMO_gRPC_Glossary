from datetime import datetime
import grpc
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import GlossaryTerm
from proto import glossary_pb2, glossary_pb2_grpc


class GlossaryServicer(glossary_pb2_grpc.GlossaryServiceServicer):
    def __init__(self, session: AsyncSession):
        self.session = session

    def _term_to_proto(self, term: GlossaryTerm) -> glossary_pb2.GlossaryTerm:
        return glossary_pb2.GlossaryTerm(
            id=term.id,
            term=term.term,
            definition=term.definition,
            created_at=term.created_at.isoformat(),
            updated_at=term.updated_at.isoformat(),
        )

    async def GetAllTerms(
        self, request: glossary_pb2.Empty, context: grpc.aio.ServicerContext
    ) -> glossary_pb2.GlossaryTermList:
        async with self.session as session:
            result = await session.execute(select(GlossaryTerm))
            terms = result.scalars().all()
            return glossary_pb2.GlossaryTermList(terms=[self._term_to_proto(term) for term in terms])

    async def GetTermById(
        self, request: glossary_pb2.TermId, context: grpc.aio.ServicerContext
    ) -> glossary_pb2.GlossaryTerm:
        async with self.session as session:
            result = await session.get(GlossaryTerm, request.id)
            if not result:
                context.abort(grpc.StatusCode.NOT_FOUND, "Term not found")
            return self._term_to_proto(result)

    async def SearchTerms(
        self, request: glossary_pb2.SearchRequest, context: grpc.aio.ServicerContext
    ) -> glossary_pb2.GlossaryTermList:
        async with self.session as session:
            query = select(GlossaryTerm).where(
                or_(GlossaryTerm.term.ilike(f"%{request.query}%"), GlossaryTerm.definition.ilike(f"%{request.query}%"))
            )
            result = await session.execute(query)
            terms = result.scalars().all()
            return glossary_pb2.GlossaryTermList(terms=[self._term_to_proto(term) for term in terms])

    async def CreateTerm(
        self, request: glossary_pb2.CreateTermRequest, context: grpc.aio.ServicerContext
    ) -> glossary_pb2.GlossaryTerm:
        async with self.session as session:
            term = GlossaryTerm(term=request.term, definition=request.definition)
            session.add(term)
            await session.commit()
            await session.refresh(term)
            return self._term_to_proto(term)

    async def UpdateTerm(
        self, request: glossary_pb2.UpdateTermRequest, context: grpc.aio.ServicerContext
    ) -> glossary_pb2.GlossaryTerm:
        async with self.session as session:
            term = await session.get(GlossaryTerm, request.id)
            if not term:
                context.abort(grpc.StatusCode.NOT_FOUND, "Term not found")

            term.term = request.term
            term.definition = request.definition
            term.updated_at = datetime.utcnow()

            await session.commit()
            await session.refresh(term)
            return self._term_to_proto(term)

    async def DeleteTerm(
        self, request: glossary_pb2.TermId, context: grpc.aio.ServicerContext
    ) -> glossary_pb2.DeleteResponse:
        async with self.session as session:
            term = await session.get(GlossaryTerm, request.id)
            if not term:
                context.abort(grpc.StatusCode.NOT_FOUND, "Term not found")

            await session.delete(term)
            await session.commit()

            return glossary_pb2.DeleteResponse(success=True, message=f"Term {request.id} successfully deleted")
