import asyncio
import grpc

from proto import glossary_pb2, glossary_pb2_grpc


async def test_all_operations() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = glossary_pb2_grpc.GlossaryServiceStub(channel)

        # Get all terms
        print("\nGetting all terms")
        response = await stub.GetAllTerms(glossary_pb2.Empty())
        print(f"Found {len(response.terms)} terms")

        # Create a new term
        print("\nCreating new term")
        new_term = await stub.CreateTerm(
            glossary_pb2.CreateTermRequest(term="gRPC", definition="A high-performance RPC framework")
        )
        print(f"Created term: {new_term.term}")

        # Get term by ID
        print("\nGetting term by ID")
        term = await stub.GetTermById(glossary_pb2.TermId(id=new_term.id))
        print(f"Retrieved term: {term.term} - {term.definition}")

        # Update term
        print("\nUpdating term")
        updated_term = await stub.UpdateTerm(
            glossary_pb2.UpdateTermRequest(
                id=new_term.id,
                term="gRPC (Google Remote Procedure Call)",
                definition="A modern, open source RPC framework by Google",
            )
        )
        print(f"Updated term: {updated_term.term} - {updated_term.definition}")

        # Search terms
        print("\nSearching terms")
        search_results = await stub.SearchTerms(glossary_pb2.SearchRequest(query="RPC"))
        print(f"Found {len(search_results.terms)} matching terms")
        for term in search_results.terms:
            print(f"- {term.term}: {term.definition}")

        # Delete term
        print("\nDeleting term")
        delete_response = await stub.DeleteTerm(glossary_pb2.TermId(id=new_term.id))
        print(f"Delete result: {delete_response.message}")


if __name__ == "__main__":
    asyncio.run(test_all_operations())
