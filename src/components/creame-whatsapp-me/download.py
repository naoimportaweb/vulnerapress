#!/usr/bin/env python3
"""Wrapper de download do componente: Joinchat &#8211; Enhanced &quot;click to chat&quot;."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Joinchat &#8211; Enhanced &quot;click to chat&quot;', 'slug': 'creame-whatsapp-me', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
