# Azure MCP untuk Grok Web

Integrasi layanan Microsoft Azure dengan Grok menggunakan MCP.

## Fitur yang Didukung (Azure MCP Server)

- Azure Resource Management
- Azure SQL Database
- Blob Storage
- Azure Functions
- Cosmos DB
- Key Vault
- Monitor & Logs
- dan 40+ layanan Azure lainnya

## Cara Setup

### 1. Install Azure MCP Server

Microsoft menyediakan official Azure MCP Server.

Cara termudah (menggunakan npx / uvx jika tersedia):

```bash
npx -y @azure/mcp-server-azure
```

Atau ikuti petunjuk resmi:
https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/

### 2. Login ke Azure

Pastikan kamu sudah login dengan `az login` atau Application (Service Principal).

### 3. Konfigurasi untuk Grok Web

Gunakan file `azure-config.json` yang disediakan.

### 4. Jalankan Proxy

```bash
npx @srbhptl39/mcp-superassistant-proxy@latest --config azure-config.json
```

Buka Grok Web. Tools Azure akan tersedia di sidebar MCP.

## Contoh Prompt

- "List semua resource group di subscription saya"
- "Tampilkan isi container di Blob Storage"
- "Jalankan query di Azure SQL Database"
- "Deploy function app terbaru"

## File yang Disertakan

- `azure-config.json`
- `README.md`

## Catatan

Azure MCP Server cukup kompleks. Untuk penggunaan awal, disarankan menggunakan **Remote MCP** jika Microsoft sudah menyediakannya, atau jalankan secara lokal setelah login Azure CLI.
