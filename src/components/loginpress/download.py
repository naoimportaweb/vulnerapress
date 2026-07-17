#!/usr/bin/env python3
"""Wrapper de download do componente: LoginPress | wp-login Custom Login Page Customizer."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'LoginPress | wp-login Custom Login Page Customizer', 'slug': 'loginpress', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
