# Windows-MCP Setup untuk Grok

Kumpulan file konfigurasi, script, dan panduan lengkap untuk menjalankan **Windows-MCP** di Windows dan mengintegrasikannya dengan **Grok** (baik via web maupun script Python).

## Apa itu Windows-MCP?

Windows-MCP adalah MCP Server yang memungkinkan AI (seperti Grok) mengontrol desktop Windows secara langsung:
- Klik mouse & keyboard
- Buka/tutup aplikasi
- Manage file & folder
- Screenshot
- Jalankan PowerShell
- dll.

## File yang Tersedia

| File | Keterangan |
|------|------------|
| `Windows-MCP-Full-Setup-Guide.md` | Panduan lengkap dari awal sampai akhir (recommended) |
| `start-windows-mcp.bat` | Script batch untuk menjalankan server dengan mudah |
| `mcp-config.toml` | Konfigurasi utama Windows-MCP (auth, security, tools) |
| `mcp-superassistant-config.json` | Konfigurasi untuk MCP SuperAssistant Proxy + Grok Web |
| `windows_mcp_client.py` | Contoh Python client untuk mengontrol Windows-MCP dari script |

## Cara Cepat Mulai

1. Baca dulu **Windows-MCP-Full-Setup-Guide.md**
2. Jalankan `start-windows-mcp.bat`
3. Install extension **MCP SuperAssistant** di Chrome
4. Jalankan proxy menggunakan `mcp-superassistant-config.json`
5. Buka Grok → MCP sidebar akan muncul

## Keamanan

- **Jangan** expose server ke internet tanpa auth_key yang kuat
- Windows-MCP memiliki akses penuh ke komputer kamu
- Selalu gunakan `ip_allowlist` dan matikan server saat tidak digunakan

## Repo Asli Windows-MCP

- GitHub: https://github.com/CursorTouch/Windows-MCP
- PyPI: `windows-mcp`

## Lisensi

Bebas digunakan untuk keperluan pribadi. Sesuaikan config sesuai kebutuhan.

---

Dibuat untuk kemudahan setup Windows-MCP + Grok integration.
