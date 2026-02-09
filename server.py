from fastmcp import FastMCP
from tools.math_tools import calculate_percentage

mcp = FastMCP("Task Toolbox")

@mcp.tool()
def get_percentage(part: float, whole: float)-> str:
    """Calculates what percentage 'part' is of 'whole'."""
    return calculate_percentage(part, whole)

if __name__ == "__main__":
    mcp.run()