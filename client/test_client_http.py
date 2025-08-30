from fastmcp import Client
import asyncio

async def test_client():
    client = Client("http://127.0.0.1:8000/mcp")
    
    async with client:
        tools = await client.list_tools()
        print(tools)

        company = await client.call_tool("search_company", {"siret": "44302124100072"})
        print(company)

if __name__ == "__main__":
    asyncio.run(test_client())

