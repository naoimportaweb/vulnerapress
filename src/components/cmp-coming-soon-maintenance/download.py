#!/usr/bin/env python3
"""Wrapper de download do componente: CMP &#8211; Coming Soon &amp; Maintenance Plugin by NiteoThemes."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'CMP &#8211; Coming Soon &amp; Maintenance Plugin by NiteoThemes', 'slug': 'cmp-coming-soon-maintenance', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
