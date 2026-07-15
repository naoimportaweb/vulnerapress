#!/usr/bin/env python3
"""Wrapper de download do componente: Disable Comments &#8211; Remove Comments &amp; Stop Spam [Multi-Site Support]."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Disable Comments &#8211; Remove Comments &amp; Stop Spam [Multi-Site Support]', 'slug': 'disable-comments', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
