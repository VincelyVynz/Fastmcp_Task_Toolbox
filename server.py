from fastmcp import FastMCP
from tools.math_tools import calculate_percentage
from tools.text_tools import count_words
from tools.time_tools import current_time

mcp = FastMCP("Task Toolbox")

@mcp.tool()
def get_percentage(part: float, whole: float)-> str:
    """Calculates what percentage 'part' is of 'whole'."""
    return calculate_percentage(part, whole)

@mcp.tool()
def word_count(text: str)-> int:
    """Calculate the total number of words in the input string"""
    return count_words(text)

@mcp.tool()
def time_now()-> str:
    """Return current time in iso format."""
    return current_time()

if __name__ == "__main__":
    mcp.run()