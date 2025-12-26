from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀", log_level="DEBUG")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http")