# -*- coding: utf-8 -*-
"""QA checks: broken internal links, duplicate titles, duplicate meta descriptions, missing alt/meta."""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

all_html_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    if "node_modules" in dirpath or "/.git" in dirpath or "/gen/" in dirpath or dirpath.endswith("/gen"):
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

    # Ignore hrefs inside inline scripts (JS-built markup templates, not real links)
    html_no_scripts = re.sub(r"<script.*?</script>", "", html, flags=re.S)
    for href in link_re.findall(html_no_scripts):
        href = href.split("?")[0]
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

# --- Checks added in the September 2026 audit -------------------------------
import html as _html
import json as _json

extra = []
sitemap = set(re.findall(r"<loc>https://tapwaterguide\.org(.*?)</loc>", open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()))
indexable = set()
for f in all_html_files:
    rel = os.path.relpath(f, ROOT)
    html = open(f, encoding="utf-8").read()
    noindex = re.search(r'<meta name="robots" content="[^"]*noindex', html) is not None
    if rel != "404.html" and not noindex:
        d = os.path.dirname(rel)
        indexable.add("/" + d + "/" if d else "/")
    if noindex:
        continue
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    if t and len(_html.unescape(t.group(1))) > 65:
        extra.append((rel, f"title is {len(_html.unescape(t.group(1)))} chars (max 65)"))
    d = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
    if not d:
        extra.append((rel, "missing meta description"))
    elif len(_html.unescape(d.group(1))) > 160:
        extra.append((rel, "meta description over 160 chars"))
    if len(re.findall(r"<h1[ >]", html)) != 1:
        extra.append((rel, "page must have exactly one h1"))
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            _json.loads(blk)
        except ValueError:
            extra.append((rel, "invalid JSON-LD"))
            continue
        if re.search(r"&[a-z]+;|&#\d+;|<[a-z/]", blk):
            extra.append((rel, "HTML or entities inside JSON-LD"))
    main = re.search(r"<main.*?>(.*)</main>", html, re.S)
    text = re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style|svg).*?</\1>", "", main.group(1) if main else "", flags=re.S))
    if re.search(r"[^.]\.\.(?!\.)", text):
        extra.append((rel, "double period in body text"))
    for img in re.findall(r"<img[^>]*>", html):
        if "alt=" not in img:
            extra.append((rel, "img without alt"))
for u in sorted(sitemap - indexable):
    extra.append(("sitemap.xml", f"{u} is listed but is missing or noindex"))
for u in sorted(indexable - sitemap):
    extra.append(("sitemap.xml", f"{u} is indexable but not listed"))

print("\n=== ADDITIONAL CHECKS ===")
for rel, msg in extra:
    print(f"  {rel}: {msg}")
print(f"Total additional issues: {len(extra)}")

print(f"\nTotal pages: {len(all_html_files)}")
print(f"Total unique titles: {len(titles)}")
print(f"Total unique descriptions: {len(descs)}")

sys.exit(1 if (dupe_titles or dupe_descs or broken_links or extra) else 0)
