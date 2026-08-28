# -*- coding: utf-8 -*-
"""Convert Natural Earth 110m GeoJSON into compact SVG path data for the
interactive world map. Run once (or when the source data changes):

    python3 gen/make_map_svg.py /path/to/ne_110m_admin_0_countries.geojson

Writes gen/world_map_data.json: list of {iso, name, path}.
Projection: equirectangular, cropped to lat [-60, 85] (drops Antarctica).
"""
import json
import math
import os
import sys

W = 1000.0
LAT_TOP = 85.0
LAT_BOTTOM = -60.0
H = round(W * (LAT_TOP - LAT_BOTTOM) / 360.0, 1)  # ~402.8
MIN_DIST = 0.8  # px; drop points closer than this to the previous kept point


def project(lon, lat):
    x = (lon + 180.0) / 360.0 * W
    y = (LAT_TOP - lat) / (LAT_TOP - LAT_BOTTOM) * H
    return x, y


def ring_to_path(ring):
    pts = []
    last = None
    for lon, lat in ring:
        if lat < LAT_BOTTOM:
            lat = LAT_BOTTOM
        x, y = project(lon, lat)
        if last is not None:
            dx, dy = x - last[0], y - last[1]
            if dx * dx + dy * dy < MIN_DIST * MIN_DIST:
                continue
        pts.append((round(x, 1), round(y, 1)))
        last = (x, y)
    if len(pts) < 3:
        return ""
    d = f"M{pts[0][0]},{pts[0][1]}"
    for x, y in pts[1:]:
        d += f"L{x},{y}"
    return d + "Z"


def main(src):
    with open(src, "r", encoding="utf-8") as f:
        gj = json.load(f)

    out = []
    for feat in gj["features"]:
        props = feat["properties"]
        iso = props.get("ISO_A2_EH") or props.get("ISO_A2") or ""
        name = props.get("NAME_EN") or props.get("ADMIN") or props.get("NAME") or ""
        if iso in ("-99", ""):
            iso = ""
        if name == "Antarctica":
            continue
        geom = feat["geometry"]
        polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        d = ""
        for poly in polys:
            for ring in poly:  # outer ring + holes; fill-rule evenodd handles holes
                d += ring_to_path(ring)
        if not d:
            continue
        out.append({"iso": iso, "name": name, "path": d})

    dst = os.path.join(os.path.dirname(__file__), "world_map_data.json")
    with open(dst, "w", encoding="utf-8") as f:
        json.dump({"width": W, "height": H, "countries": out}, f, ensure_ascii=False)
    total = sum(len(c["path"]) for c in out)
    print(f"Wrote {len(out)} countries, {total/1024:.0f} KB of path data, canvas {W}x{H}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "/tmp/world.geojson")
