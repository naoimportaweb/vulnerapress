#!/usr/bin/env python3
"""Wrapper de download do componente: SureForms &#8211; Drag &amp; Drop Contact Form &amp; Form Builder, Payment Form, Survey, Quiz &amp; Calculator."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'SureForms &#8211; Drag &amp; Drop Contact Form &amp; Form Builder, Payment Form, Survey, Quiz &amp; Calculator', 'slug': 'sureforms', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
