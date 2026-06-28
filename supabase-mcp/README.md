# Supabase MCP untuk Grok Web

Integrasi Supabase dengan Grok menggunakan MCP SuperAssistant.

## Fitur yang Didukung

- Query & manage database (Postgres)
- Authentication & user management
- Storage (upload/download file)
- Edge Functions
- Realtime subscriptions (terbatas)

## Cara Setup

### 1. Dapatkan Supabase Access Token

1. Buka https://supabase.com/dashboard/account/tokens
2. Buat Personal Access Token baru.

### 2. Jalankan Supabase MCP

Supabase punya official MCP server. Cara termudah:

```bash
npx -y @supabase/mcp-server-supabase --access-token YOUR_SUPABASE_TOKEN
```

Atau gunakan Remote MCP (jika tersedia):
```
https://mcp.supabase.com/mcp
```

### 3. Konfigurasi untuk Grok Web

Edit file `supabase-config.json` dan masukkan token kamu.

### 4. Jalankan Proxy

```bash
npx @srbhptl39/mcp-superassistant-proxy@latest --config supabase-config.json
```

Setelah itu, buka Grok Web. Tools Supabase akan muncul di sidebar MCP.

## Contoh Prompt di Grok

- "Tampilkan semua user dari tabel profiles"
- "Buat user baru di Supabase Auth"
- "Upload file ke bucket 'avatars'"
- "Jalankan Edge Function 'send-welcome-email'"

## File yang Disertakan

- `supabase-config.json` — Template konfigurasi untuk proxy
- `README.md` — Panduan ini

## Peringatan Keamanan

Jangan share access token kamu. Gunakan token dengan permission terbatas jika memungkinkan.
