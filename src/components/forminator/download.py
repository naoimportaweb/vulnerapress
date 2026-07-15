#!/usr/bin/env python3
"""Wrapper de download do componente: Forminator Forms – Contact Form, Payment Form &amp; Custom Form Builder."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Forminator Forms – Contact Form, Payment Form &amp; Custom Form Builder', 'slug': 'forminator', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
