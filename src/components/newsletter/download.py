#!/usr/bin/env python3
"""Wrapper de download do componente: Newsletter &#8211; Send awesome emails from WordPress."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Newsletter &#8211; Send awesome emails from WordPress', 'slug': 'newsletter', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
