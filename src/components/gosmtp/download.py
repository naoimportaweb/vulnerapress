#!/usr/bin/env python3
"""Wrapper de download do componente: GoSMTP &#8211; SMTP for WordPress."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'GoSMTP &#8211; SMTP for WordPress', 'slug': 'gosmtp', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
