#!/usr/bin/env python3
"""Wrapper de download do componente: Checkout Field Editor (Checkout Manager) for WooCommerce."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Checkout Field Editor (Checkout Manager) for WooCommerce', 'slug': 'woo-checkout-field-editor-pro', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
