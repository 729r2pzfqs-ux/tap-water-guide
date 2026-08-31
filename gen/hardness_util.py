# -*- coding: utf-8 -*-
"""Shared water-hardness parsing helpers.

Free-text `hardness` fields ("Hard, roughly 250&ndash;300 mg/L") remain the
editorial source of truth; these helpers derive the classification level and
structured numeric mg/L values used for gauges, sorting, and ranking.
"""
import re

HARDNESS_LABELS = ["Soft", "Moderate", "Hard", "Very Hard"]

# Typical mg/L midpoint per USGS band, used when the text states a
# classification but no number (e.g. "Generally moderate, data limited").
LEVEL_TYPICAL_MGL = {1: 40, 2: 90, 3: 150, 4: 250}

_RANGE_RE = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:&ndash;|&#8211;|[–—-]|\s+to\s+)\s*(\d+(?:\.\d+)?)\+?\s*mg/L",
    re.I,
)
_SINGLE_RE = re.compile(r"(\d+(?:\.\d+)?)\s*\+?\s*mg/L", re.I)


def hardness_level(text):
    """Parse free-text hardness into level 1-4, using the first-mentioned descriptor.
    Returns None when hardness is unspecified or purely variable."""
    t = re.sub(r"<[^>]+>", "", text).lower()
    positions = []
    vh = t.find("very hard")
    if vh != -1:
        positions.append((vh, 4))
    t_masked = t.replace("very hard", "#########")
    h = t_masked.find("hard")
    if h != -1:
        positions.append((h, 3))
    m = t.find("moderate")
    if m != -1:
        positions.append((m, 2))
    s = t.find("soft")
    if s != -1:
        positions.append((s, 1))
    if not positions:
        return None
    return min(positions)[1]


def band_for_mgl(mgl):
    """USGS band (1-4) for a numeric mg/L CaCO3 value; None for None."""
    if mgl is None:
        return None
    if mgl <= 60:
        return 1
    if mgl <= 120:
        return 2
    if mgl <= 180:
        return 3
    return 4


def parse_hardness_mgl(text):
    """Extract (min, max, midpoint) mg/L from a free-text hardness description.

    Uses the first stated mg/L range or value; falls back to the typical
    midpoint of the described band ("soft"/"moderate"/...) when no number is
    published. Returns (None, None, None) when hardness is purely variable.
    """
    m = _RANGE_RE.search(text)
    if m:
        lo, hi = float(m.group(1)), float(m.group(2))
        if lo > hi:
            lo, hi = hi, lo
        return int(lo), int(hi), int(round((lo + hi) / 2))
    m = _SINGLE_RE.search(text)
    if m:
        v = int(round(float(m.group(1))))
        return v, v, v
    level = hardness_level(text)
    if level:
        mid = LEVEL_TYPICAL_MGL[level]
        return None, None, mid
    return None, None, None
