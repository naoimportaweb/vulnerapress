#!/usr/bin/env python3
"""Wrapper de download do componente: Call Now Button &#8211; The #1 Click to Call Button for WordPress."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Call Now Button &#8211; The #1 Click to Call Button for WordPress', 'slug': 'call-now-button', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
