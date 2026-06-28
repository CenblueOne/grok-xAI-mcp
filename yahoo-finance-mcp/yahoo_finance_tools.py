#!/usr/bin/env python3
"""
Yahoo Finance Tools untuk Grok
Script ini bisa digunakan sebagai dasar untuk membuat Yahoo Finance MCP Server
atau dipanggil langsung dari Python.

Install:
    pip install yfinance pandas
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Optional

def get_stock_price(ticker: str):
    """Ambil harga saham terkini"""
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "ticker": ticker,
        "price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "currency": info.get("currency"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
    }

def get_historical_data(ticker: str, period: str = "1mo"):
    """Ambil data historis"""
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df.tail(10).to_dict("records")

def get_fundamentals(ticker: str):
    """Ambil data fundamental"""
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "ticker": ticker,
        "longName": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "marketCap": info.get("marketCap"),
        "trailingPE": info.get("trailingPE"),
        "forwardPE": info.get("forwardPE"),
        "dividendYield": info.get("dividendYield"),
        "beta": info.get("beta"),
    }

def compare_stocks(tickers: List[str]):
    """Bandingkan beberapa saham"""
    results = []
    for t in tickers:
        try:
            results.append(get_stock_price(t))
        except Exception as e:
            results.append({"ticker": t, "error": str(e)})
    return results

if __name__ == "__main__":
    print("=== Contoh Penggunaan Yahoo Finance Tools ===\n")

    print("1. Harga saham BBCA.JK:")
    print(get_stock_price("BBCA.JK"))

    print("\n2. Data Fundamental AAPL:")
    print(get_fundamentals("AAPL"))

    print("\n3. Bandingkan saham:")
    print(compare_stocks(["BBCA.JK", "TLKM.JK", "BMRI.JK"]))
