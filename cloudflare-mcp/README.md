# Cloudflare MCP untuk Grok Web

Integrasi Cloudflare (DNS, Workers, R2, Pages, dll) dengan Grok.

## Fitur yang Didukung (Contoh)
- Manage DNS records
- Deploy & manage Cloudflare Workers
- Upload file ke R2 Storage
- Manage Pages projects
- Security & WAF settings

## Cara Setup

1. Dapatkan **Cloudflare API Token** dengan permission yang dibutuhkan.
2. Edit `cloudflare-config.json` dan masukkan token kamu.
3. Jalankan proxy:

```bash
npx @srbhptl39/mcp-superassistant-proxy@latest --config cloudflare-config.json
```

4. Buka Grok Web → Tools Cloudflare akan muncul.

## Contoh Prompt
- "Tambahkan DNS record A untuk subdomain api ke IP 1.2.3.4"
- "Deploy Worker baru bernama 'grok-api'"
- "Upload file ke R2 bucket 'backups'"

## Peringatan
Jangan share API Token. Gunakan token dengan scope terbatas.
