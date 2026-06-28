# Windows-MCP Full Setup Guide (Awal sampai Akhir)
**Untuk Grok + Desktop Automation di Windows**

## 1. Persiapan Awal (Prerequisites)
- Windows 10/11 (English language lebih baik)
- Python 3.13 atau lebih baru
- PowerShell (admin recommended)
- UV package manager (recommended):
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

## 2. Install & Jalankan Windows-MCP Server
```powershell
# Jalankan server (HTTP mode + auth)
uvx windows-mcp serve --transport streamable-http --auth-key ganti-dengan-kunci-kuat-123 --config "%USERPROFILE%\.windows-mcp\config.toml"
```

**Buat folder config dulu:**
```powershell
mkdir "$env:USERPROFILE\.windows-mcp"
```

## 3. Buat Config File (mcp-config.toml)
Simpan sebagai: `C:\Users\Administrator\.windows-mcp\config.toml`

Isi contoh (ganti auth_key):
```toml
[server]
transport = "streamable-http"
host = "0.0.0.0"
port = 8000
auth_key = "ganti-dengan-kunci-kuat-123"

[security]
ip_allowlist = ["127.0.0.1", "192.168.1.0/24"]

[tools]
# exclude = ["PowerShell", "Registry"]   # opsional untuk keamanan
```

## 4. Buat .bat untuk Mudah Jalankan Server
Gunakan file `start-windows-mcp.bat` yang sudah dibuat sebelumnya (double click).

## 5. Setup untuk Grok Web (Paling Mudah)
1. Buka Chrome → install extension **MCP SuperAssistant**  
   Link langsung: https://chromewebstore.google.com/detail/mcp-superassistant/kngiafgkdnlkgmefdafaibkibegkcaef

2. Buat file `mcp-superassistant-config.json` di folder Downloads atau mana saja:
```json
{
  "mcpServers": {
    "windows-mcp": {
      "url": "http://localhost:8000/mcp",
      "headers": {
        "Authorization": "Bearer ganti-dengan-kunci-kuat-123"
      }
    }
  }
}
```

3. Jalankan proxy (biarkan tetap running):
```powershell
npx @srbhptl39/mcp-superassistant-proxy@latest --config mcp-superassistant-config.json
```

## 6. Cara Pakai di Grok Web (Setelah Extension Muncul)
Setelah extension terinstall dan proxy running:

1. Buka Grok chat di browser.
2. Di toolbar atau **sidebar kanan** akan muncul label **"MCP"** + pengaturan MCP baru.
3. Klik ikon/sidebar MCP → pastikan server **windows-mcp** muncul dan status **Connected** (hijau).
4. Sekarang Grok bisa langsung menggunakan tools Windows-MCP (mouse, keyboard, app, file, screenshot, PowerShell, dll).

**Contoh prompt yang bisa dipakai:**
- "Buka Notepad, ketik 'Halo dari Grok via MCP', simpan sebagai test.txt di Desktop"
- "Screenshot layar penuh dan deskripsikan isi layar"
- "Buka File Explorer, buat folder 'Grok-Project' di Documents, lalu pindahkan 2 file .txt ke dalamnya"
- "Buka Chrome dan buka website x.ai"

**Tips:**
- Tools yang tersedia tergantung config (bisa whitelist/exclude di mcp-config.toml)
- Jika tools tidak muncul, cek proxy log dan pastikan auth_key cocok di config.json

## 7. Opsional: Pakai Ngrok (Remote Access)
```powershell
ngrok config add-authtoken TOKEN_ANDA
ngrok http 8000
```
Copy URL https://xxxx.ngrok.io → ganti di config.json jika butuh akses remote.

## Peringatan Keamanan Penting
- Jangan expose ke public tanpa auth_key kuat + ip_allowlist
- Windows-MCP punya akses penuh ke desktop kamu (klik, ketik, hapus file, PowerShell)
- Matikan server saat tidak dipakai
- Review SECURITY.md di repo asli

## File yang Sudah Dibuat (Download dari Chat)
- `start-windows-mcp.bat` — double-click untuk jalankan server
- `mcp-config.toml` — config utama Windows-MCP
- `mcp-superassistant-config.json` — config proxy + Grok extension
- `windows_mcp_client.py` — contoh Python client (opsional)

## 8. Python Client (Opsional)
Jika ingin kontrol dari Python:

```bash
python windows_mcp_client.py
```

Edit `auth_key` di file tersebut sesuai yang ada di `mcp-config.toml`.

Selesai. Semua file siap di-upload ke GitHub.
```

Now, the file is created. For the response, keep it very brief.