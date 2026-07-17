#!/usr/bin/env python3
"""Wrapper de download do componente: OMGF | GDPR/DSGVO Compliant, Faster Google Fonts. Easy.."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'OMGF | GDPR/DSGVO Compliant, Faster Google Fonts. Easy.', 'slug': 'host-webfonts-local', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
