# MCP Web Search Tool

A lightweight MCP server implementation for web search operations using FastMCP, designed to integrate with Smithery's development environment.

## Features
- **Async web search** through custom scraper integration
- **FastMCP** server foundation for rapid tool development
- **Smithery deployment** ready configuration
- **Simulated URL fetching** with error handling

## Prerequisites
- Python 3.9+
- [MCP CLI]([https://smithery.io/mcp-cli](https://github.com/modelcontextprotocol/python-sdk)) installed
- Smithery development environment access

## Installation
```
git clone https://github.com/rockerritesh/scraper-mcp-smithery.git
cd scraper-mcp-smithery
uv run server.py
mcp dev server.py
```

## Usage
**Run development server:**
```
mcp dev server.py
```

## Scraper Integration
The tool uses `scraper_doc.py` for:
- URL content extraction
- Error handling with status codes
- MD-formatted results parsing

## Development
```
# Test with debug mode
MCP_DEBUG=1 mcp dev server.py
```

## License
MIT License (see LICENSE file)
```

This README provides clear setup instructions while highlighting the tool's async capabilities and Smithery integration. The structure follows best practices for developer tools documentation.

---
