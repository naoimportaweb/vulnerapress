#!/usr/bin/env python3
"""Wrapper de download do componente: Floating Chat Widget: Contact Chat Icons, Telegram Chat, Line Messenger, WeChat, Email, SMS, Call Button – Chaty."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Floating Chat Widget: Contact Chat Icons, Telegram Chat, Line Messenger, WeChat, Email, SMS, Call Button – Chaty', 'slug': 'chaty', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
