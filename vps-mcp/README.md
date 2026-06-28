# VPS MCP (SSH Control) untuk Grok Web

Kontrol VPS Linux (Ubuntu, Debian, CentOS, dll) dari Grok via SSH.

## Fitur
- Jalankan perintah shell
- Manage file & folder via SSH
- Install package, restart service
- Monitoring (disk, memory, CPU)
- Deploy aplikasi sederhana

## Cara Setup

1. Siapkan VPS dengan SSH key atau password.
2. Edit `vps-config.json` dengan detail koneksi VPS kamu.
3. Jalankan proxy.

## Keamanan Penting
- Gunakan SSH Key (bukan password) jika memungkinkan.
- Batasi command yang boleh dijalankan Grok.
- Jangan berikan akses root jika tidak perlu.
