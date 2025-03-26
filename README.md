# etsy-mcp-server

Note: this is a work in progress.
MCP server to integrate with Etsy API

# Set up the Etsy API key
1. Go to https://www.etsy.com/developers and click "Create an app"
2. The app will go through a review process that can take days to weeks. To expedite the process, send an email to developers@etsy.com to request API key approval. An example email is in etsy-email-template.txt
3. Once approved, copy the API key will be in "Manage your apps" page

# Set up the MCP server in Claude Desktop

Add the following in `claude_desktop_config.json`. It can be found at `~/Library/Application\ Support/Claude/claude_desktop_config.json`

```
 "etsy-mcp-server": {
    "command": "/Users/{user}/.local/bin/uv",
    "args": [
        "--directory",
        {PATH_TO_REPO},
        "run",
        "etsy-mcp-server.py"
    ],
    "env": {
        "ETSY_API_KEY": {YOUR_ETSY_API_KEY}
    }
}
```
where `{user}` is your username, `{PATH_TO_REPO}` is the path to the repo, and `{YOUR_ETSY_API_KEY}` is your Etsy API key.

# Incoming tools:
- create a listing
- listing stats analysis 

# License
MIT