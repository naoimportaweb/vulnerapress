#!/usr/bin/env python3
"""Wrapper de download do componente: PDF Invoices &amp; Packing Slips for WooCommerce."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'PDF Invoices &amp; Packing Slips for WooCommerce', 'slug': 'woocommerce-pdf-invoices-packing-slips', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
