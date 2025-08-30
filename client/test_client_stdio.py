import asyncio
from fastmcp import Client, FastMCP


client = Client("server.py")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        print(tools)

        # Execute operations
        result = await client.call_tool("search_company", {"siret": "44302124100072"})
        print(result)

asyncio.run(main())