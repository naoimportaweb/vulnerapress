#!/usr/bin/env python3
"""Wrapper de download do componente: Cart Abandonment Recovery for WooCommerce – Recover Lost Sales with Automated Emails."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Cart Abandonment Recovery for WooCommerce – Recover Lost Sales with Automated Emails', 'slug': 'woo-cart-abandonment-recovery', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
