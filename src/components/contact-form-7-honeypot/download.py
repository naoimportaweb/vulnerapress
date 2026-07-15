#!/usr/bin/env python3
"""Wrapper de download do componente: CF7 Apps – Honeypot, Database, Redirection, Webhook, and Addons for Contact Form 7."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'CF7 Apps – Honeypot, Database, Redirection, Webhook, and Addons for Contact Form 7', 'slug': 'contact-form-7-honeypot', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
