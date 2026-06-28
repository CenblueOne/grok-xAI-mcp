# Yahoo Finance MCP untuk Grok Web

Integrasi data saham, crypto, dan keuangan dari Yahoo Finance ke Grok.

## Fitur yang Didukung

- Ambil data harga real-time & historis
- Data fundamental perusahaan (PE, EPS, Market Cap, dll)
- Data crypto & forex
- Analisis teknikal sederhana
- Download data ke CSV/Excel
- Multi ticker support

## Cara Setup

### Opsi 1: Menggunakan Python Script (Paling Mudah)

1. Install library:
   ```bash
   pip install yfinance pandas
   ```

2. Gunakan script `yahoo_finance_tools.py` yang disediakan.

3. Jalankan script sebagai MCP-like tool atau gunakan bersama Python client.

### Opsi 2: Custom MCP Server

Kamu bisa membuat MCP Server sederhana menggunakan FastAPI + yfinance, lalu expose via HTTP untuk digunakan dengan MCP SuperAssistant.

## Contoh Prompt di Grok

- "Berapa harga saham BBCA.JK saat ini?"
- "Tampilkan data historis saham TLKM 1 bulan terakhir"
- "Bandingkan performa saham BBRI dan BMRI"
- "Ambil data fundamental dari saham AAPL"
- "Download data harga saham selama 1 tahun ke file CSV"

## File yang Disertakan

- `README.md`
- `yahoo_finance_tools.py` — Script Python siap pakai
- `yahoo-finance-config.json` — Template konfigurasi (untuk custom MCP)

## Catatan

Yahoo Finance tidak menyediakan official MCP Server. Script yang disediakan bisa dijadikan dasar untuk membuat custom MCP Server sendiri.
