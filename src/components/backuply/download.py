#!/usr/bin/env python3
"""Wrapper de download do componente: Backuply &#8211; Backup, Restore, Migrate and Clone."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Backuply &#8211; Backup, Restore, Migrate and Clone', 'slug': 'backuply', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
