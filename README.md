# INSEE MCP Server

MCP (Model Context Protocol) server for accessing INSEE data via the SIRENE API, BDM, and official nomenclatures.

## One-line Installation

### With uv (recommended)
```bash
# Install and launch directly
API_KEY="your_insee_api_key" uv run --with insee-mcp insee-mcp
```
or if you prefer to use uvx
```bash
# Install and launch directly
API_KEY="your_insee_api_key" uvx insee-mcp insee-mcp
```

### Standard MCP Configuration
Add this to your MCP configuration (e.g., Claude Desktop, or Copilot):

```json
{
  "mcpServers": {
    "insee": {
      "command": "uvx",
      "args": ["insee-mcp", "insee-mcp"],
      "env": {
        "API_KEY": "your_insee_api_key"
      }
    }
  }
}
```

### With pipx
```bash
API_KEY="your_insee_api_key" pipx run --spec git+https://github.com/KerryanOPMace/mcp-insee.git insee-mcp
```

## Quick Installation

### Direct Installation (recommended)

```bash
# Install directly from GitHub
pip install git+https://github.com/KerryanOPMace/mcp-insee.git

# Set your INSEE API key
export API_KEY="your_insee_api_key"

# Start the server
insee-mcp
```

### Installation with pipx (isolated)

```bash
# Install with pipx (isolated environment)
pipx install git+https://github.com/KerryanOPMace/mcp-insee.git

# Set the API key
export API_KEY="your_insee_api_key"

# Start the server
insee-mcp
```

### Developer Installation

```bash
# Clone the repository
git clone https://github.com/KerryanOPMace/mcp-insee.git
cd mcp-insee

# Install in development mode
pip install -e .
```

If you wish to contribute to the project, please create issues and branches. You can merge request and then a supervisor will review it before merging

## Configuration

### INSEE API Key

You must obtain an API key from the [INSEE API portal](https://api.insee.fr/) and configure it:

**Linux/Mac:**
```bash
export API_KEY="your_insee_api_key"
```

**Windows (PowerShell):**
```powershell
$env:API_KEY="your_insee_api_key"
```

**Windows (CMD):**
```cmd
set API_KEY=your_insee_api_key
```

## Available Tools

- `search_company`: Search for companies in the SIRENE database
  - By SIREN, SIRET, or company name
  - Fuzzy search available


## STREAMABLE-HTTP TRANSPORT

## Server Access

Once started, the MCP server is accessible at:
- **URL**: `http://127.0.0.1:8000/mcp`
- **Transport**: Streamable HTTP

### Client Test

```python
from fastmcp import Client
import asyncio

async def test():
    client = Client("http://127.0.0.1:8000/mcp")
    async with client:
        # List tools
        tools = await client.list_tools()
        print(tools)
        
        # Search for a company
        result = await client.call_tool("search_company", {
            "siret": "44302124100072"
        })
        print(result)

asyncio.run(test())
```

### Requirements

- Python 3.8+
- Valid INSEE API key
- Internet access for API requests



## STDIO TRANSPORT

## Server Access

Once started, the MCP server runs locally according to the standard io protocol

### Client Test

```python
from fastmcp import Client
import asyncio

async def test():
    client = Client("http://127.0.0.1:8000/mcp")
    async with client:
        # List tools
        tools = await client.list_tools()
        print(tools)
        
        # Search for a company
        result = await client.call_tool("search_company", {
            "siret": "44302124100072"
        })
        print(result)

asyncio.run(test())
```

### Requirements

- Python 3.8+
- Valid INSEE API key
- Internet access for API requests

## License

MIT License

