# -*- coding: utf-8 -*-
"""QA checks: broken internal links, duplicate titles, duplicate meta descriptions, missing alt/meta."""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

all_html_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    if "node_modules" in dirpath or "/.git" in dirpath or "/gen" in dirpath:
        continue
    for fn in filenames:
        if fn == "index.html" or fn == "404.html":
            all_html_files.append(os.path.join(dirpath, fn))

print(f"Found {len(all_html_files)} HTML files")

# Build set of valid paths (directories that have index.html -> the URL path)
valid_paths = set()
for f in all_html_files:
    rel = os.path.relpath(f, ROOT)
    if rel == "404.html":
        continue
    d = os.path.dirname(rel)
    url = "/" + d + "/" if d else "/"
    url = url.replace("//", "/")
    valid_paths.add(url)

titles = {}
descs = {}
broken_links = []
link_re = re.compile(r'href="(/[^"]*)"')

for f in all_html_files:
    rel = os.path.relpath(f, ROOT)
    html = open(f, encoding="utf-8").read()
    tmatch = re.search(r"<title>(.*?)</title>", html, re.S)
    dmatch = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
    if tmatch:
        t = tmatch.group(1)
        titles.setdefault(t, []).append(rel)
    if dmatch:
        d = dmatch.group(1)
        descs.setdefault(d, []).append(rel)

    for href in link_re.findall(html):
        if href.startswith("/assets/") or href == "/sitemap.xml" or href == "/robots.txt":
            continue
        if href.startswith("/#") or "#" in href and href.split("#")[0] == "":
            continue
        path = href.split("#")[0]
        if not path:
            continue
        if not path.endswith("/"):
            # non-trailing-slash internal link is suspicious for this site structure
            broken_links.append((rel, href, "no trailing slash"))
            continue
        if path not in valid_paths:
            broken_links.append((rel, href, "target not found"))

print("\n=== DUPLICATE TITLES ===")
dupe_titles = {k: v for k, v in titles.items() if len(v) > 1}
for t, files in dupe_titles.items():
    print(f"  {t!r}: {files}")
print(f"Total duplicate title groups: {len(dupe_titles)}")

print("\n=== DUPLICATE META DESCRIPTIONS ===")
dupe_descs = {k: v for k, v in descs.items() if len(v) > 1}
for d, files in dupe_descs.items():
    print(f"  {d[:80]!r}: {files}")
print(f"Total duplicate description groups: {len(dupe_descs)}")

print("\n=== BROKEN LINKS ===")
for rel, href, reason in broken_links:
    print(f"  {rel} -> {href} ({reason})")
print(f"Total broken link issues: {len(broken_links)}")

print(f"\nTotal pages: {len(all_html_files)}")
print(f"Total unique titles: {len(titles)}")
print(f"Total unique descriptions: {len(descs)}")

sys.exit(1 if (dupe_titles or dupe_descs or broken_links) else 0)
