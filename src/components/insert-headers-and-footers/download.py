#!/usr/bin/env python3
"""Wrapper de download do componente: WPCode &#8211; Insert Headers and Footers + Custom Code Snippets &#8211; WordPress Code Manager."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'WPCode &#8211; Insert Headers and Footers + Custom Code Snippets &#8211; WordPress Code Manager', 'slug': 'insert-headers-and-footers', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
