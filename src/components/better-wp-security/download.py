#!/usr/bin/env python3
"""Wrapper de download do componente: Kadence Security – Password, Two Factor Authentication, and Brute Force Protection."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Kadence Security – Password, Two Factor Authentication, and Brute Force Protection', 'slug': 'better-wp-security', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
