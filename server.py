# server.py
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import subprocess
import asyncio
import os
# from openai import OpenAI
# load_dotenv()
# client = OpenAI()



# Create an MCP server
mcp = FastMCP("Demo")


# # Add an addition tool
# @mcp.tool()
# # make async
# async def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b

async def fetch_url(url: str) -> dict:
    """Fetch the content of a URL."""
    # Simulate a URL fetch with a python scraper
    proc = await asyncio.create_subprocess_exec(
        "python",
        "scraper_doc.py",
        url,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        raise Exception(f"Error: {stderr.decode().strip()}")
    return {"organic_results": stdout.decode().strip()}

@mcp.tool()
async def search_web_tool(query: str) -> dict:
    """
    Search the web for a given query.
    Args:
        query: The search query.
    Returns:
        The search results.
    """
    return await fetch_url(query)
    

# async def generate_story(query: str) -> str:
#     """Generate a story based on a given query."""
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {
#                 "role": "user",
#                 "content": query
#             }
#         ]
#     )

#     # print(completion.choices[0].message.content)
#     return completion.choices[0].message.content

# @mcp.tool()
# async def query_web(query: str) -> str:
#     """
#     Query the web for a given query.
#     Args:
#         query: The query to search the web for.
#     Returns:
#         The story generated based on the query.
#     """
#     return await generate_story(query)

if __name__ == "__main__":
    mcp.run(transport="stdio")
