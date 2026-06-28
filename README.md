# Windows-MCP untuk Grok Web

**MCP Server untuk mengontrol Windows dari Grok**

Windows-MCP memungkinkan Grok mengontrol desktop Windows secara langsung melalui **MCP SuperAssistant** extension. Dengan setup ini, Grok bisa melakukan klik mouse, mengetik, membuka aplikasi, mengelola file, screenshot, dan menjalankan perintah sistem.

## Fitur Utama

- Kontrol UI Windows secara real-time (mouse, keyboard, aplikasi)
- Integrasi mudah dengan **Grok Web** via MCP SuperAssistant
- Dukungan transport HTTP (streamable-http) + autentikasi
- Bisa dijalankan secara lokal atau via ngrok
- Python client tersedia untuk automation
- Keamanan configurable (auth key, IP allowlist, tool whitelist)

## Persyaratan

- Windows 10 / 11
- Python 3.13 atau lebih baru
- UV Package Manager (direkomendasikan)
- Chrome + ekstensi **MCP SuperAssistant**

## Instalasi Cepat

### 1. Jalankan Windows-MCP Server

```powershell
# Buat folder config
mkdir "$env:USERPROFILE\.windows-mcp"

# Jalankan server
uvx windows-mcp serve --transport streamable-http --config "$env:USERPROFILE\.windows-mcp\config.toml"
```

### 2. Konfigurasi (mcp-config.toml)

Edit file `mcp-config.toml` dan isi `auth_key` dengan kunci yang kuat.

### 3. Setup untuk Grok Web

1. Install ekstensi **MCP SuperAssistant** dari Chrome Web Store.
2. Edit `mcp-superassistant-config.json` (isi `auth_key` yang sama).
3. Jalankan proxy:

```powershell
npx @srbhptl39/mcp-superassistant-proxy@latest --config mcp-superassistant-config.json
```

4. Buka Grok Web. Sidebar **MCP** akan muncul otomatis.

## Cara Penggunaan di Grok

Setelah terhubung, kamu bisa memberikan perintah seperti:

- "Buka Notepad dan tulis 'Halo dari Grok'"
- "Screenshot layar dan jelaskan isinya"
- "Buka File Explorer, buat folder baru di Documents"
- "Tutup semua aplikasi Chrome"

## File yang Disertakan

| File                              | Keterangan                              |
|-----------------------------------|-----------------------------------------|
| `Windows-MCP-Full-Setup-Guide.md` | Panduan lengkap step-by-step            |
| `start-windows-mcp.bat`           | Script batch untuk menjalankan server   |
| `mcp-config.toml`                 | Konfigurasi server                      |
| `mcp-superassistant-config.json`  | Konfigurasi proxy + Grok                |
| `windows_mcp_client.py`           | Contoh Python client                    |
| `README_Windows-MCP_Grok.md`      | README ini                              |

## Keamanan

> **Peringatan**: Windows-MCP memiliki akses penuh ke komputer kamu.

- Selalu gunakan `auth_key` yang kuat
- Batasi IP dengan `ip_allowlist`
- Jangan expose ke internet tanpa ngrok + perlindungan
- Matikan server saat tidak digunakan
- Hindari memberikan akses ke tool berbahaya (PowerShell, Registry) jika tidak perlu

## Repo Terkait

- Windows-MCP asli: https://github.com/CursorTouch/Windows-MCP
- MCP SuperAssistant: https://mcpsuperassistant.ai/

## Lisensi

Bebas digunakan untuk keperluan pribadi dan pengembangan.

---

Dibuat untuk memudahkan integrasi **Windows-MCP** dengan **Grok Web**.
