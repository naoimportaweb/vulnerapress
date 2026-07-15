#!/usr/bin/env python3
"""Wrapper de download do componente: Template Kit &#8211; Import."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Template Kit &#8211; Import', 'slug': 'template-kit-import', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
