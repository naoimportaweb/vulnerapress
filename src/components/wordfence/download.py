#!/usr/bin/env python3
"""Wrapper de download do componente: Wordfence Security &#8211; Firewall, Malware Scan, and Login Security."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Wordfence Security &#8211; Firewall, Malware Scan, and Login Security', 'slug': 'wordfence', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
