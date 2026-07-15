#!/usr/bin/env python3
"""Wrapper de download do componente: Click to Chat &#8211; HoliThemes."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Click to Chat &#8211; HoliThemes', 'slug': 'click-to-chat-for-whatsapp', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
