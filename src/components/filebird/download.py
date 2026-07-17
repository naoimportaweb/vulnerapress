#!/usr/bin/env python3
"""Wrapper de download do componente: FileBird &#8211; WordPress Media Library Folders &amp; File Manager."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'FileBird &#8211; WordPress Media Library Folders &amp; File Manager', 'slug': 'filebird', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
