#!/usr/bin/env python3
"""Wrapper de download do componente: Complianz &#8211; Terms and Conditions."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Complianz &#8211; Terms and Conditions', 'slug': 'complianz-terms-conditions', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
