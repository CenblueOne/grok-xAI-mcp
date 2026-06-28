@echo off
title Windows-MCP Server
echo ============================================
echo   Starting Windows-MCP Server (HTTP mode)
echo   Config: %USERPROFILE%\.windows-mcp\config.toml
echo ============================================
echo.
echo Make sure config.toml has correct auth_key and ip_allowlist!
echo.

uvx windows-mcp serve --transport streamable-http --config "%USERPROFILE%\.windows-mcp\config.toml"

echo.
echo Server stopped. Press any key to exit...
pause >nul
