# MCP untuk Grok Web

Repository ini berisi **kumpulan konfigurasi, script, dan panduan** untuk menggunakan **Model Context Protocol (MCP)** di **Grok Web**.

Tujuan utama:
- Memudahkan integrasi MCP Server ke Grok melalui **MCP SuperAssistant** Chrome Extension
- Memberikan kontrol tambahan ke Grok (desktop automation, file management, dll)

## Yang Sudah Tersedia

### Windows-MCP
Kontrol desktop Windows secara langsung dari Grok.

Fitur yang didukung:
- Mouse & Keyboard control
- Buka/tutup aplikasi
- Manage file & folder
- Screenshot + visual understanding
- Jalankan PowerShell & system command
- Clipboard, notification, dll.

**File utama:**
- `Windows-MCP-Full-Setup-Guide.md` → Panduan lengkap setup dari awal sampai akhir
- `start-windows-mcp.bat` → Script untuk menjalankan server
- `mcp-config.toml` → Konfigurasi server (auth, security, tools)
- `mcp-superassistant-config.json` → Konfigurasi untuk proxy + Grok extension
- `windows_mcp_client.py` → Contoh Python client

## Cara Penggunaan Singkat

1. Baca **Windows-MCP-Full-Setup-Guide.md**
2. Jalankan Windows-MCP server
3. Install **MCP SuperAssistant** extension di Chrome
4. Jalankan proxy menggunakan config yang disediakan
5. Buka Grok Web → MCP sidebar akan muncul otomatis

Setelah terhubung, Grok bisa langsung menggunakan tools Windows-MCP melalui chat.

## Struktur Folder

```
.
├── README.md
├── Windows-MCP-Full-Setup-Guide.md
├── start-windows-mcp.bat
├── mcp-config.toml
├── mcp-superassistant-config.json
└── windows_mcp_client.py
```

## Catatan Keamanan

- Windows-MCP memiliki akses penuh ke komputer kamu (mouse, keyboard, file, command).
- Gunakan `auth_key` yang kuat dan `ip_allowlist`.
- Jangan expose ke public tanpa perlindungan yang baik.
- Matikan server ketika tidak digunakan.

## Repo Terkait

- Windows-MCP: https://github.com/CursorTouch/Windows-MCP
- MCP SuperAssistant: https://mcpsuperassistant.ai/

---

**Repo ini akan terus ditambahkan** dengan MCP lain untuk Grok Web di masa depan.
