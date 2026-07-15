#!/usr/bin/env python3
"""Wrapper de download do componente: Database Addon for Contact Form 7 &#8211; CFDB7."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Database Addon for Contact Form 7 &#8211; CFDB7', 'slug': 'contact-form-cfdb7', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
