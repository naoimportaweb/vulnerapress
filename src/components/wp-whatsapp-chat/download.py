#!/usr/bin/env python3
"""Wrapper de download do componente: Social Chat &#8211; Click To Chat App Button."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Social Chat &#8211; Click To Chat App Button', 'slug': 'wp-whatsapp-chat', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
