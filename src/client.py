import asyncio
import grpc

from proto import glossary_pb2, glossary_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = glossary_pb2_grpc.GlossaryServiceStub(channel)

        # Example: Get all terms
        response = await stub.GetAllTerms(glossary_pb2.Empty())
        print("All terms:", response.terms)

        # Example: Search terms
        search_response = await stub.SearchTerms(glossary_pb2.SearchRequest(query="Python"))
        print("Search results:", search_response.terms)


if __name__ == "__main__":
    asyncio.run(run())
