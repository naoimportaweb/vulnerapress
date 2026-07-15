#!/usr/bin/env python3
"""Wrapper de download do componente: Post SMTP – Complete Email Deliverability and SMTP Solution with Email Logs, Alerts, Backup SMTP &amp; Mobile App."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Post SMTP – Complete Email Deliverability and SMTP Solution with Email Logs, Alerts, Backup SMTP &amp; Mobile App', 'slug': 'post-smtp', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
