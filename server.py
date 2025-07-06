# server.py
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import asyncio
import os
from scraper_doc import scrape_website
from urllib.parse import urlparse
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

def ensure_url_format(url: str) -> str:
    """Ensure URL has proper protocol (http/https)"""
    if not url.startswith(('http://', 'https://')):
        # Default to https for better security
        return f"https://{url}"
    return url

async def fetch_url(url: str) -> dict:
    """Fetch the content of a URL using direct function call."""
    try:
        # Ensure proper URL format
        formatted_url = ensure_url_format(url)
        
        # Run the scraper function in a thread to avoid blocking
        loop = asyncio.get_event_loop()
        markdown_content = await loop.run_in_executor(
            None, 
            scrape_website, 
            formatted_url
        )
        
        if markdown_content:
            return {"organic_results": markdown_content}
        else:
            return {"organic_results": "Failed to scrape the website"}
            
    except Exception as e:
        return {"organic_results": f"Error scraping website: {str(e)}"}

@mcp.tool()
async def search_web_tool(query: str) -> dict:
    """
    Search the web for a given query.
    Args:
        query: The search query (URL).
    Returns:
        The search results as markdown content.
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
