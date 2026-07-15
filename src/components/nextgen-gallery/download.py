#!/usr/bin/env python3
"""Wrapper de download do componente: Photo Gallery, Sliders, Proofing and Themes &#8211; NextGEN Gallery."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from downloader import sync_component

COMPONENT = {'name': 'Photo Gallery, Sliders, Proofing and Themes &#8211; NextGEN Gallery', 'slug': 'nextgen-gallery', 'type': 'plugin'}

if __name__ == "__main__":
    raise SystemExit(sync_component(**COMPONENT))
