#!/usr/bin/env python3
"""Wrapper de download do componente: Sucuri Security &#8211; Auditing, Malware Scanner and Security Hardening."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Sucuri Security &#8211; Auditing, Malware Scanner and Security Hardening', 'slug': 'sucuri-scanner', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
