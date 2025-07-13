from fastmcp import Client
import asyncio

async def main():
    async with Client("python ../server/weather_server.py") as mcp_client:
        tools = await mcp_client.list_tools()
        print("=== Available Tools ===")
        print(tools)
        
        print("\n=== Testing get_weather ===")
        print("Berlin:", await mcp_client.call_tool("get_weather", {"city": "Berlin"}))
        print("Random city:", await mcp_client.call_tool("get_weather", {"city": "Paris"}))

if __name__ == "__main__":
    asyncio.run(main())