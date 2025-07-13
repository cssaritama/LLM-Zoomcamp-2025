from fastmcp import FastMCP
from weather_tools import get_weather, set_weather

mcp = FastMCP("Weather Tools Server")

mcp.tool(get_weather)
mcp.tool(set_weather)

if __name__ == "__main__":
    mcp.run()