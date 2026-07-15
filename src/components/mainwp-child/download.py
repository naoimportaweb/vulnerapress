#!/usr/bin/env python3
"""Wrapper de download do componente: MainWP Child &#8211; Securely Connects to the MainWP Dashboard to Manage Multiple Sites."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'MainWP Child &#8211; Securely Connects to the MainWP Dashboard to Manage Multiple Sites', 'slug': 'mainwp-child', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
