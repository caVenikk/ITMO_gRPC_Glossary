import asyncio
import json
import logging
from pathlib import Path

from grpc.aio import server as grpc_aio_server
from sqlalchemy import text

from database.session import AsyncSessionLocal
from database.models import GlossaryTerm
from proto import glossary_pb2_grpc
from services.glossary_service import GlossaryServicer


async def init_db() -> None:
    """Initialize database with terms from glossary.json"""
    async with AsyncSessionLocal() as session:
        # Check if database is empty
        result = await session.execute(text("SELECT COUNT(*) FROM glossary_terms"))
        count = result.scalar()

        if count == 0:
            # Load terms from JSON file
            json_path = Path(__file__).parent / "glossary.json"
            with open(json_path, "r", encoding="utf-8") as f:
                terms = json.load(f)

            # Add terms to database
            for term_data in terms:
                term = GlossaryTerm(term=term_data["term"], definition=term_data["definition"])
                session.add(term)

            await session.commit()
            logging.info("Database initialized with glossary terms")


async def serve() -> None:
    # Initialize database
    await init_db()

    # Create gRPC server
    server = grpc_aio_server()

    # Add GlossaryService to server
    glossary_pb2_grpc.add_GlossaryServiceServicer_to_server(GlossaryServicer(AsyncSessionLocal()), server)

    # Start server
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
