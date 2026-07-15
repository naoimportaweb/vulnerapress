#!/usr/bin/env python3
"""Wrapper de download do componente: Ninja Forms &#8211; The Contact Form Builder That Grows With You."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Ninja Forms &#8211; The Contact Form Builder That Grows With You', 'slug': 'ninja-forms', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
