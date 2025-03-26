from typing import Any
import httpx
import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("etsy-mcp-server")
USER_AGENT = "etsy-mcp-server/1.0"

# Get API key from environment variable
ETSY_API_KEY = os.environ.get("ETSY_API_KEY", "")

@mcp.tool()
async def get_etsy_listings(tag: str) -> str:
    """Get Etsy listings for a given tag.

    Args:
        tag: Etsy tag (e.g. "artsy", "vintage")
    """
    # Define your user agent
    headers = {
        "User-Agent": USER_AGENT,
        "x-api-key": ETSY_API_KEY
    }
    
    if not ETSY_API_KEY:
        return "Error: ETSY_API_KEY environment variable not set"
    
    # Make the request to Etsy API
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://openapi.etsy.com/v3/application/listings/active",
            params={"tags": tag},
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            return f"Found {len(data['results'])} listings for tag: {tag}"
        else:
            return f"Error fetching Etsy listings: {response.status_code} - {response.text}"


if __name__ == "__main__":
    mcp.run(transport='stdio')
