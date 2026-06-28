#!/usr/bin/env python3
"""
Simple Windows-MCP Client (Python)
Gunakan ini jika ingin kontrol Windows-MCP dari script Python / automation.

Pastikan:
- Windows-MCP server running (streamable-http di port 8000)
- auth_key cocok dengan yang di config.toml
"""

import requests
from typing import Any, Dict, Optional

class WindowsMCPClient:
    def __init__(self, base_url: str = "http://localhost:8000/mcp", auth_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        if auth_key:
            self.session.headers.update({"Authorization": f"Bearer {auth_key}"})

    def call(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Panggil method MCP (sesuai protokol streamable-http)."""
        payload = {"jsonrpc": "2.0", "id": 1, "method": method}
        if params:
            payload["params"] = params
        resp = self.session.post(self.base_url, json=payload)
        resp.raise_for_status()
        return resp.json()

    def list_tools(self):
        return self.call("tools/list")

    def call_tool(self, name: str, arguments: Dict[str, Any]):
        return self.call("tools/call", {"name": name, "arguments": arguments})

    # Contoh helper
    def screenshot(self):
        return self.call_tool("screenshot", {})

    def click(self, x: int, y: int):
        return self.call_tool("click", {"x": x, "y": y})

    def type_text(self, text: str):
        return self.call_tool("type", {"text": text})


if __name__ == "__main__":
    client = WindowsMCPClient(
        base_url="http://localhost:8000/mcp",
        auth_key="ganti-dengan-auth_key-mu"   # ← GANTI INI
    )

    print("Tools available:")
    print(client.list_tools())

    # Contoh: ambil screenshot
    # result = client.screenshot()
    # print(result)
```

This is a basic starting point (MCP protocol can be more involved; for full features use the official proxy/extension).

Now, update the guide to include this file in the "Files created" section and add a small note in section 6 or a new section.