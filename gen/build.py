# -*- coding: utf-8 -*-
import os
import sys
import re
import html as htmlmod

sys.path.insert(0, os.path.dirname(__file__))
from templates import (
    page, rating_badge, breadcrumbs, faq_block, stat_pill, RATING_STYLE, ICONS, DOMAIN, SITE,
    DATE_PUBLISHED, LAST_REVIEWED, LAST_REVIEWED_DISPLAY, ORG_SCHEMA,
)
from data_countries import COUNTRIES, BY_SLUG as COUNTRY_BY_SLUG
from data_us_cities import US_CITIES, BY_SLUG as US_BY_SLUG
from data_intl_cities import INTL_CITIES, BY_SLUG as INTL_BY_SLUG
from data_guides import GUIDES

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

ALL_PAGES = []  # (path, priority, changefreq) for sitemap


def write_page(rel_path, html):
    """rel_path like '/country/japan/' -> writes country/japan/index.html"""
    assert rel_path.startswith("/") and rel_path.endswith("/")
    fs_path = os.path.join(ROOT, rel_path.lstrip("/"), "index.html")
    os.makedirs(os.path.dirname(fs_path), exist_ok=True)
    with open(fs_path, "w", encoding="utf-8") as f:
        f.write(html)


def register(path, priority="0.7", changefreq="monthly"):
    ALL_PAGES.append((path, priority, changefreq))


# Build city lookup by country
CITIES_BY_COUNTRY = {}
for c in INTL_CITIES:
    CITIES_BY_COUNTRY.setdefault(c["country_slug"], []).append(c)


def info_card(icon_svg, label, value):
    return f"""<div class="bg-white rounded-lg border border-gray-200 p-4">
      <div class="flex items-center gap-2 text-gray-400 mb-1">{icon_svg}<span class="text-xs font-medium uppercase tracking-wide">{label}</span></div>
      <div class="text-gray-900 font-semibold">{value}</div>
    </div>"""


ICON_SOURCE = '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>'
ICON_DROP = '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>'
ICON_PEOPLE = '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a4 4 0 00-3-3.87M9 20H4v-2a4 4 0 013-3.87m6-8a4 4 0 110 8 4 4 0 010-8zm6 3a4 4 0 11-8 0"/></svg>'
ICON_MAP = '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/></svg>'


def section_card(title, body_html, id_=None):
    idattr = f' id="{id_}"' if id_ else ""
    return f"""<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6"{idattr}>
      <h2 class="text-xl font-bold text-gray-900 mb-3">{title}</h2>
      <div class="text-gray-600 leading-relaxed space-y-3">{body_html}</div>
    </div>"""


def bullet_list(items):
    lis = "".join(f'<li class="flex items-start gap-2"><span class="text-sky-500 mt-1.5">&bull;</span><span>{i}</span></li>' for i in items)
    return f'<ul class="space-y-2">{lis}</ul>'


HARDNESS_LABELS = ["Soft", "Moderate", "Hard", "Very Hard"]


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


def hardness_gauge(text):
    """Visual 4-segment hardness scale. Empty string when level can't be determined."""
    level = hardness_level(text)
    if level is None:
        return ""
    segs = ""
    labels = ""
    seg_colors = ["bg-sky-300", "bg-sky-400", "bg-sky-600", "bg-sky-800"]
    for i, label in enumerate(HARDNESS_LABELS):
        active = (i + 1) == level
        color = seg_colors[i] if active else "bg-gray-200"
        segs += f'<div class="h-2 flex-1 rounded-full {color}"></div>'
        lbl_cls = "text-gray-900 font-semibold" if active else "text-gray-400"
        labels += f'<div class="flex-1 text-center text-xs {lbl_cls}">{label}</div>'
    return f"""<div class="mt-4" aria-label="Water hardness scale: {HARDNESS_LABELS[level-1]}">
      <div class="flex gap-1.5">{segs}</div>
      <div class="flex gap-1.5 mt-1.5">{labels}</div>
    </div>"""


def reviewed_badge():
    return (f'<span class="text-sm text-gray-400">Last reviewed: '
            f'<time datetime="{LAST_REVIEWED}">{LAST_REVIEWED_DISPLAY}</time></span>')


def _source_link(href, label):
    return (f'<a href="{href}" target="_blank" rel="noopener" '
            f'class="text-sky-700 hover:underline">{label}</a>')


def sources_card(kind):
    """Per-page sources & references section. kind: 'country' | 'us' | 'intl'"""
    common = [
        _source_link("https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/water-safety-and-quality/drinking-water-quality-guidelines",
                     "WHO Guidelines for Drinking-water Quality"),
    ]
    if kind == "country":
        items = common + [
            _source_link("https://wwwnc.cdc.gov/travel/destinations/list", "CDC Travelers' Health destination pages"),
            _source_link("https://washdata.org/", "WHO/UNICEF Joint Monitoring Programme (JMP)"),
            "National and municipal water utility public quality reports",
        ]
    elif kind == "us":
        items = [
            _source_link("https://www.epa.gov/sdwa", "US EPA Safe Drinking Water Act regulations"),
            _source_link("https://www.ewg.org/tapwater/", "EWG Tap Water Database"),
            "The utility's most recent Consumer Confidence Report (CCR)",
        ] + common
    else:  # intl city
        items = common + [
            _source_link("https://wwwnc.cdc.gov/travel/destinations/list", "CDC Travelers' Health destination pages"),
            "The municipal water utility's published quality data",
        ]
    lis = "".join(f'<li class="flex items-start gap-2"><span class="text-sky-500 mt-1.5">&bull;</span><span>{i}</span></li>' for i in items)
    return f"""<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6" id="page-sources">
      <h2 class="text-xl font-bold text-gray-900 mb-3">Sources &amp; References</h2>
      <p class="text-sm text-gray-500 mb-3">The safety rating and guidance on this page draw on the following sources. See our <a href="/about/#sources" class="text-sky-700 hover:underline">full methodology</a>.</p>
      <ul class="space-y-2 text-sm">{lis}</ul>
    </div>"""


def article_schema(headline, description, url):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": description,
        "url": url,
        "datePublished": DATE_PUBLISHED,
        "dateModified": LAST_REVIEWED,
        "author": {"@type": "Organization", "name": f"{SITE} Editorial Team", "url": f"{DOMAIN}/about/"},
        "publisher": {"@type": "Organization", "name": SITE, "url": DOMAIN},
    }


# ---------------------------------------------------------------------------
# COUNTRY PAGES
# ---------------------------------------------------------------------------

def build_country_page(c):
    slug = c["slug"]
    rs = RATING_STYLE[c["rating"]]
    cities = CITIES_BY_COUNTRY.get(slug, [])

    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Countries", "/country/"), (c["name"], None)])

    cities_html = ""
    if cities:
        cards = "".join(
            f'''<a href="/city/{ci["slug"]}/" class="block bg-white rounded-lg border border-gray-200 p-4 hover:border-sky-300 hover:shadow-md transition-all">
              <div class="flex items-center justify-between">
                <span class="font-semibold text-gray-900">{ci["name"]}</span>
                {rating_badge(ci["rating"])}
              </div>
            </a>''' for ci in cities
        )
        cities_html = f"""<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h2 class="text-xl font-bold text-gray-900 mb-4">Cities in {c['name']}</h2>
          <div class="grid sm:grid-cols-2 gap-3">{cards}</div>
        </div>"""

    precautions_html = bullet_list(c["precautions"]) if len(c["precautions"]) > 1 else f'<p>{c["precautions"][0]}</p>'
    tips_html = bullet_list(c["tips"])

    faq_html, faq_ld = faq_block(c["faqs"])

    other_countries = [x for x in COUNTRIES if x["region"] == c["region"] and x["slug"] != slug][:6]
    other_html = ""
    if other_countries:
        links = "".join(f'<a href="/country/{o["slug"]}/" class="text-sky-700 hover:underline">{o["name"]}</a>' for o in other_countries)
        other_html = f"""<div class="bg-sky-50 rounded-xl border border-sky-100 p-6">
          <h2 class="text-lg font-bold text-gray-900 mb-3">Other Countries in {c['region']}</h2>
          <div class="flex flex-wrap gap-x-4 gap-y-2 text-sm">{links}</div>
        </div>"""

    body = f"""
<section class="bg-gradient-to-b {rs['hero']} to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">
    {bc_html}
  </div>
</section>

<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <div class="flex flex-wrap items-center gap-3 mb-4">
      {rating_badge(c['rating'], size='large')}
      <span class="text-sm text-gray-400">{c['region']}</span>
      <span class="text-gray-300">&middot;</span>
      {reviewed_badge()}
    </div>
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Is Tap Water Safe to Drink in {c['name']}?</h1>
    <p class="text-lg text-gray-700 leading-relaxed mb-6">{c['quick_answer']}</p>

    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-8">
      {info_card(ICON_DROP, 'Hardness', c['hardness'].split(',')[0])}
      {info_card(ICON_PEOPLE, 'Locals Drink It?', 'Yes' if c['locals_drink'].strip().lower().startswith('yes') else ('No' if c['locals_drink'].strip().lower().startswith('no') else 'Mixed'))}
      {info_card(ICON_MAP, 'Region', c['region'])}
      {info_card(ICON_SOURCE, 'Cities Covered', str(len(cities)) if cities else '&mdash;')}
    </div>

    <div class="space-y-6">
      {section_card('Water Source', f"<p>{c['water_source']}</p>")}
      {section_card('Contaminants &amp; Concerns', f"<p>{c['contaminants']}</p>")}
      {section_card('Regional Variations', f"<p>{c['regional']}</p>")}
      {section_card('Water Hardness', f"<p>{c['hardness']}.</p>" + hardness_gauge(c['hardness']))}
      {section_card('Do Locals Drink Tap Water?', f"<p>{c['locals_drink']}</p>")}
      {section_card('Tips for Travelers', tips_html)}
      {section_card('Recommended Precautions', precautions_html)}
      {cities_html}
      {faq_html}
      {sources_card('country')}
      {other_html}
    </div>

    <div class="mt-8 flex flex-wrap gap-3">
      <a href="/rankings/best-tap-water/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">See countries with the best tap water &rarr;</a>
      <a href="/rankings/worst-tap-water/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">See countries to use caution in &rarr;</a>
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    if faq_ld:
        schemas.append(faq_ld)
    schemas.append(article_schema(f"Is Tap Water Safe to Drink in {c['name']}?", c["meta_description"], f"{DOMAIN}/country/{slug}/"))

    title = f"Is Tap Water Safe in {c['name']}? Drinking Water Guide | TapWaterGuide"
    html = page(title, c["meta_description"], f"/country/{slug}/", body, schemas=schemas, active_nav="countries")
    write_page(f"/country/{slug}/", html)
    register(f"/country/{slug}/", "0.8", "monthly")


# ---------------------------------------------------------------------------
# US CITY PAGES
# ---------------------------------------------------------------------------

def build_us_city_page(ci):
    slug = ci["slug"]
    rs = RATING_STYLE[ci["rating"]]
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("US Cities", "/rankings/best-tap-water-us/"), (ci["name"], None)])

    contam_html = bullet_list(ci["contaminants"])
    tips_html = bullet_list(ci["tips"])
    faq_html, faq_ld = faq_block(ci["faqs"])

    other_us = [x for x in US_CITIES if x["slug"] != slug][:8]
    import random as _r
    other_links = "".join(f'<a href="/city/{o["slug"]}/" class="text-sky-700 hover:underline">{o["name"]}</a>' for o in other_us[:6])

    body = f"""
<section class="bg-gradient-to-b {rs['hero']} to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>

<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <div class="flex flex-wrap items-center gap-3 mb-4">
      {rating_badge(ci['rating'], size='large')}
      <span class="text-sm text-gray-400">{ci['state']}, United States</span>
      <span class="text-gray-300">&middot;</span>
      {reviewed_badge()}
    </div>
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Is Tap Water Safe to Drink in {ci['name']}?</h1>
    <p class="text-lg text-gray-700 leading-relaxed mb-6">{ci['quick_answer']}</p>

    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
      {info_card(ICON_DROP, 'Hardness', ci['hardness'].split(',')[0])}
      {info_card(ICON_SOURCE, 'pH', ci['ph'])}
      {info_card(ICON_MAP, 'TDS', ci['tds'])}
      {info_card(ICON_PEOPLE, 'EPA Status', 'Compliant')}
    </div>
    <div class="mb-8">{hardness_gauge(ci['hardness'])}</div>

    <div class="space-y-6">
      {section_card('Water Source', f"<p>{ci['water_source']}</p>")}
      {section_card('EPA Compliance Status', f"<p>{ci['epa_status']}</p>")}
      {section_card('Notable Contaminants &amp; Context', contam_html)}
      {section_card('How It Compares', f"<p>{ci['comparison']}</p>")}
      {section_card('Tips', tips_html)}
      {faq_html}
      {sources_card('us')}
      <div class="bg-sky-50 rounded-xl border border-sky-100 p-6">
        <h2 class="text-lg font-bold text-gray-900 mb-3">More US Cities</h2>
        <div class="flex flex-wrap gap-x-4 gap-y-2 text-sm">{other_links}</div>
      </div>
    </div>

    <div class="mt-8 flex flex-wrap gap-3">
      <a href="/rankings/best-tap-water-us/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">See all US city rankings &rarr;</a>
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    if faq_ld:
        schemas.append(faq_ld)
    schemas.append(article_schema(f"Is Tap Water Safe to Drink in {ci['name']}?", ci["meta_description"], f"{DOMAIN}/city/{slug}/"))
    title = f"Is Tap Water Safe in {ci['name']}, {ci['state']}? | TapWaterGuide"
    html = page(title, ci["meta_description"], f"/city/{slug}/", body, schemas=schemas, active_nav="us")
    write_page(f"/city/{slug}/", html)
    register(f"/city/{slug}/", "0.8", "monthly")


# ---------------------------------------------------------------------------
# INTERNATIONAL CITY PAGES
# ---------------------------------------------------------------------------

def build_intl_city_page(ci):
    slug = ci["slug"]
    rs = RATING_STYLE[ci["rating"]]
    country = COUNTRY_BY_SLUG[ci["country_slug"]]
    bc_html, bc_ld = breadcrumbs([
        ("Home", "/"), ("Countries", "/country/"),
        (country["name"], f"/country/{country['slug']}/"), (ci["name"], None),
    ])

    tips_html = bullet_list(ci["tips"])
    faq_html, faq_ld = faq_block(ci["faqs"])

    siblings = [x for x in CITIES_BY_COUNTRY.get(country["slug"], []) if x["slug"] != slug]
    sib_html = ""
    if siblings:
        links = "".join(f'<a href="/city/{o["slug"]}/" class="text-sky-700 hover:underline">{o["name"]}</a>' for o in siblings)
        sib_html = f"""<div class="bg-sky-50 rounded-xl border border-sky-100 p-6">
          <h2 class="text-lg font-bold text-gray-900 mb-3">Other Cities in {country['name']}</h2>
          <div class="flex flex-wrap gap-x-4 gap-y-2 text-sm">{links}</div>
        </div>"""

    body = f"""
<section class="bg-gradient-to-b {rs['hero']} to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>

<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <div class="flex flex-wrap items-center gap-3 mb-4">
      {rating_badge(ci['rating'], size='large')}
      <span class="text-sm text-gray-400">{country['name']}</span>
      <span class="text-gray-300">&middot;</span>
      {reviewed_badge()}
    </div>
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Is Tap Water Safe to Drink in {ci['name']}?</h1>
    <p class="text-lg text-gray-700 leading-relaxed mb-6">{ci['quick_answer']}</p>

    <div class="grid grid-cols-2 md:grid-cols-3 gap-3 mb-4">
      {info_card(ICON_DROP, 'Hardness', ci['hardness'].split(',')[0])}
      {info_card(ICON_MAP, 'Country', country['name'])}
      {info_card(ICON_PEOPLE, 'Rating', ci['rating'])}
    </div>
    <div class="mb-8">{hardness_gauge(ci['hardness'])}</div>

    <div class="space-y-6">
      {section_card('Water Source', f"<p>{ci['water_source']}</p>")}
      {section_card('Contaminants &amp; Concerns', f"<p>{ci['contaminants']}</p>")}
      {section_card('Tips', tips_html)}
      {faq_html}
      {sources_card('intl')}
      {sib_html}
    </div>

    <div class="mt-8 flex flex-wrap gap-3">
      <a href="/country/{country['slug']}/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">&larr; Full {country['name']} country guide</a>
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    if faq_ld:
        schemas.append(faq_ld)
    schemas.append(article_schema(f"Is Tap Water Safe to Drink in {ci['name']}?", ci["meta_description"], f"{DOMAIN}/city/{slug}/"))
    title = f"Is Tap Water Safe in {ci['name']}, {country['name']}? | TapWaterGuide"
    html = page(title, ci["meta_description"], f"/city/{slug}/", body, schemas=schemas, active_nav="world")
    write_page(f"/city/{slug}/", html)
    register(f"/city/{slug}/", "0.8", "monthly")


for c in COUNTRIES:
    build_country_page(c)
for ci in US_CITIES:
    build_us_city_page(ci)
for ci in INTL_CITIES:
    build_intl_city_page(ci)

print(f"Built {len(COUNTRIES)} country pages, {len(US_CITIES)} US city pages, {len(INTL_CITIES)} intl city pages")

# ---------------------------------------------------------------------------
# HOMEPAGE
# ---------------------------------------------------------------------------

import json as _json

ALL_ENTITIES = (
    [dict(name=c["name"], slug=c["slug"], type="country", rating=c["rating"], href=f"/country/{c['slug']}/") for c in COUNTRIES]
    + [dict(name=f"{c['name']}, {c['state']}", slug=c["slug"], type="us-city", rating=c["rating"], href=f"/city/{c['slug']}/") for c in US_CITIES]
    + [dict(name=re.sub('<[^<]+?>', '', c["name"]), slug=c["slug"], type="world-city", rating=c["rating"], href=f"/city/{c['slug']}/") for c in INTL_CITIES]
)

N_COUNTRIES = len(COUNTRIES)
N_CITIES = len(US_CITIES) + len(INTL_CITIES)

# Shared search index consumed by the header search on every page
with open(os.path.join(ROOT, "search-index.json"), "w", encoding="utf-8") as f:
    _json.dump(ALL_ENTITIES, f, ensure_ascii=False)
print(f"Built search-index.json with {len(ALL_ENTITIES)} entries")

FEATURED_COUNTRIES = ["japan", "mexico", "italy", "thailand", "india", "spain", "france", "costa-rica", "greece", "vietnam", "morocco", "chile"]
FEATURED_US = ["new-york-city", "chicago", "los-angeles", "san-francisco", "houston", "miami", "seattle", "las-vegas"]
FEATURED_WORLD = ["paris", "london", "rome", "tokyo", "bangkok", "bali", "dubai", "cancun",
                  "mexico-city", "madrid", "copenhagen", "milan"]


def build_homepage():
    country_chips = "".join(
        f'<a href="/country/{s}/" class="px-4 py-2 bg-white border border-gray-200 rounded-full text-sm font-medium text-gray-700 hover:border-sky-400 hover:text-sky-700 transition-colors">{COUNTRY_BY_SLUG[s]["name"]}</a>'
        for s in FEATURED_COUNTRIES
    )
    us_cards = "".join(
        f'''<a href="/city/{s}/" class="block bg-white rounded-lg border border-gray-200 p-4 hover:border-sky-300 hover:shadow-md transition-all">
          <div class="flex items-center justify-between mb-1">
            <span class="font-semibold text-gray-900">{US_BY_SLUG[s]["name"]}</span>
            {rating_badge(US_BY_SLUG[s]["rating"])}
          </div>
          <div class="text-xs text-gray-400">{US_BY_SLUG[s]["state"]}</div>
        </a>''' for s in FEATURED_US
    )
    world_cards = "".join(
        f'''<a href="/city/{s}/" class="block bg-white rounded-lg border border-gray-200 p-4 hover:border-sky-300 hover:shadow-md transition-all">
          <div class="flex items-center justify-between mb-1">
            <span class="font-semibold text-gray-900">{INTL_BY_SLUG[s]["name"]}</span>
            {rating_badge(INTL_BY_SLUG[s]["rating"])}
          </div>
          <div class="text-xs text-gray-400">{INTL_BY_SLUG[s]["country_name"]}</div>
        </a>''' for s in FEATURED_WORLD
    )

    search_data = _json.dumps(ALL_ENTITIES, ensure_ascii=False)

    body = f"""
<section class="bg-gradient-to-b from-sky-50 via-sky-50 to-white px-4 py-14 md:py-20">
  <div class="max-w-3xl mx-auto text-center">
    <div class="inline-flex items-center justify-center w-16 h-16 bg-sky-600 rounded-2xl mb-6">
      {ICONS['droplet']}
    </div>
    <h1 class="text-3xl md:text-5xl font-bold text-gray-900 mb-4 leading-tight">Is tap water safe to drink?<br class="hidden md:block"> Check any country or city.</h1>
    <p class="text-lg text-gray-600 mb-8 max-w-xl mx-auto">The worldwide reference for tap water safety, built on WHO, EPA, EWG, and CDC guidance &mdash; for travelers and for checking your own city.</p>

    <div class="relative max-w-xl mx-auto">
      <div class="flex items-center bg-white rounded-full shadow-lg border border-gray-200 px-5 py-3.5">
        <span class="text-gray-400">{ICONS['search']}</span>
        <input id="siteSearch" type="text" placeholder="Search a country or city&hellip; e.g. Mexico, Chicago, Bali" autocomplete="off" class="flex-1 ml-3 outline-none text-gray-900 placeholder-gray-400 bg-transparent">
      </div>
      <div id="searchResults" class="hidden absolute z-40 top-full mt-2 w-full bg-white rounded-xl shadow-xl border border-gray-200 overflow-hidden text-left"></div>
    </div>

    <div class="flex flex-wrap items-center justify-center gap-6 mt-10">
      {stat_pill('Countries Covered', N_COUNTRIES)}
      {stat_pill('Cities Covered', N_CITIES)}
      {stat_pill('Data Sources', 'WHO &middot; EPA &middot; EWG &middot; CDC')}
    </div>
  </div>
</section>

<section class="px-4 py-8">
  <div class="max-w-6xl mx-auto">
    <a href="/map/" class="block bg-gradient-to-br from-sky-50 to-white rounded-xl border border-sky-100 p-6 hover:shadow-md transition-shadow">
      <div class="flex items-center justify-between gap-4 flex-wrap">
        <div>
          <h2 class="text-xl font-bold text-gray-900 mb-1">Explore the World Safety Map</h2>
          <p class="text-sm text-gray-600">Every country colored by tap water safety rating &mdash; click any country for its full guide.</p>
        </div>
        <span class="inline-flex items-center gap-1.5 px-5 py-2.5 bg-sky-600 text-white rounded-lg font-medium hover:bg-sky-700">Open the map &rarr;</span>
      </div>
    </a>
  </div>
</section>

<section class="px-4 py-12">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-2xl font-bold text-gray-900 mb-5">Popular Countries</h2>
    <div class="flex flex-wrap gap-3 mb-4">{country_chips}</div>
    <a href="/country/" class="text-sm text-sky-700 hover:underline font-medium">Browse all {N_COUNTRIES} countries &rarr;</a>
  </div>
</section>

<section class="px-4 py-8 bg-white border-y border-gray-100">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-2xl font-bold text-gray-900 mb-5">Popular US Cities</h2>
    <div class="grid sm:grid-cols-2 md:grid-cols-4 gap-3 mb-4">{us_cards}</div>
    <a href="/rankings/best-tap-water-us/" class="text-sm text-sky-700 hover:underline font-medium">See all US city rankings &rarr;</a>
  </div>
</section>

<section class="px-4 py-12">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-2xl font-bold text-gray-900 mb-5">Popular World Cities</h2>
    <div class="grid sm:grid-cols-2 md:grid-cols-4 gap-3 mb-4">{world_cards}</div>
    <a href="/city/" class="text-sm text-sky-700 hover:underline font-medium">Browse all world cities &rarr;</a>
  </div>
</section>

<section class="px-4 py-12 bg-white border-t border-gray-100">
  <div class="max-w-6xl mx-auto grid md:grid-cols-3 gap-6">
    <a href="/rankings/best-tap-water/" class="block bg-gradient-to-br from-emerald-50 to-white rounded-xl border border-emerald-100 p-6 hover:shadow-md transition-shadow">
      <h3 class="font-bold text-gray-900 mb-2">Best Tap Water Worldwide</h3>
      <p class="text-sm text-gray-600">Countries where tap water is safest and best-tasting, from Iceland to Singapore.</p>
    </a>
    <a href="/rankings/worst-tap-water/" class="block bg-gradient-to-br from-red-50 to-white rounded-xl border border-red-100 p-6 hover:shadow-md transition-shadow">
      <h3 class="font-bold text-gray-900 mb-2">Countries to Avoid Tap Water</h3>
      <p class="text-sm text-gray-600">Where to stick to bottled or filtered water, and why.</p>
    </a>
    <a href="/rankings/best-tap-water-us/" class="block bg-gradient-to-br from-sky-50 to-white rounded-xl border border-sky-100 p-6 hover:shadow-md transition-shadow">
      <h3 class="font-bold text-gray-900 mb-2">Best US City Water</h3>
      <p class="text-sm text-gray-600">Which American cities have the cleanest municipal tap water, and why.</p>
    </a>
  </div>
</section>

<script>
var SEARCH_DATA = {search_data};
var input = document.getElementById('siteSearch');
var results = document.getElementById('searchResults');
var typeLabel = {{country: 'Country', 'us-city': 'US City', 'world-city': 'World City'}};
input.addEventListener('input', function() {{
  var q = input.value.trim().toLowerCase();
  if (!q) {{ results.classList.add('hidden'); results.innerHTML = ''; return; }}
  var matches = SEARCH_DATA.filter(function(e) {{ return e.name.toLowerCase().indexOf(q) !== -1; }}).slice(0, 8);
  if (!matches.length) {{
    results.innerHTML = '<div class="px-5 py-4 text-sm text-gray-500">No matches. Try a country or major city name.</div>';
  }} else {{
    results.innerHTML = matches.map(function(e) {{
      return '<a href="' + e.href + '" class="flex items-center justify-between px-5 py-3 hover:bg-sky-50 border-b border-gray-100 last:border-0">' +
        '<span class="text-gray-900">' + e.name + '</span>' +
        '<span class="text-xs text-gray-400">' + typeLabel[e.type] + '</span></a>';
    }}).join('');
  }}
  results.classList.remove('hidden');
}});
document.addEventListener('click', function(ev) {{
  if (!ev.target.closest('#siteSearch') && !ev.target.closest('#searchResults')) {{ results.classList.add('hidden'); }}
}});
</script>
"""
    schemas = [{
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE,
        "url": DOMAIN + "/",
        "potentialAction": {
            "@type": "SearchAction",
            "target": f"{DOMAIN}/?q={{search_term_string}}",
            "query-input": "required name=search_term_string",
        },
    }, ORG_SCHEMA]
    title = "TapWaterGuide.org &mdash; Is Tap Water Safe to Drink? Check Any Country or City"
    desc = f"Check tap water safety for {N_COUNTRIES} countries and {N_CITIES} cities worldwide, built on WHO, EPA, EWG, and CDC data. Free, answer-first drinking water guide."
    html = page(title, desc, "/", body, schemas=schemas, active_nav="home")
    write_page("/", html)
    register("/", "1.0", "weekly")


build_homepage()
print("Built homepage")

# ---------------------------------------------------------------------------
# COUNTRY INDEX (/country/)
# ---------------------------------------------------------------------------

def build_country_index():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Countries", None)])
    by_region = {}
    for c in COUNTRIES:
        by_region.setdefault(c["region"], []).append(c)
    region_order = ["Europe", "Asia", "North America", "South America", "Africa", "Oceania", "Middle East"]
    sections = ""
    for region in region_order:
        items = sorted(by_region.get(region, []), key=lambda x: x["name"])
        if not items:
            continue
        rows = "".join(
            f'''<a href="/country/{c['slug']}/" class="flex items-center justify-between px-4 py-3 hover:bg-sky-50 border-b border-gray-100 last:border-0">
              <span class="text-gray-900 font-medium">{c['name']}</span>
              {rating_badge(c['rating'])}
            </a>''' for c in items
        )
        region_slug_map = {"Europe": "europe", "Asia": "asia", "North America": "north-america",
                           "South America": "south-america", "Africa": "africa", "Oceania": "oceania",
                           "Middle East": "middle-east"}
        rlink = f'<a href="/region/{region_slug_map[region]}/" class="text-sm text-sky-700 hover:underline font-normal">Region guide &rarr;</a>'
        sections += f"""<div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
          <div class="px-4 py-3 bg-gray-50 border-b border-gray-200 flex items-center justify-between"><h2 class="font-bold text-gray-900">{region}</h2>{rlink}</div>
          {rows}
        </div>"""

    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-3">Tap Water Safety by Country</h1>
    <p class="text-gray-600 mb-8">Drinking water safety ratings for {len(COUNTRIES)} countries worldwide, organized by region. Select a country for a full guide including water source, hardness, and traveler tips.</p>
    {sections}
  </div>
</section>
"""
    schemas = [bc_ld]
    title = "All Countries &mdash; Tap Water Safety by Country | TapWaterGuide"
    desc = f"Browse tap water safety ratings for all {len(COUNTRIES)} countries covered by TapWaterGuide, organized by region from Europe to Oceania."
    html = page(title, desc, "/country/", body, schemas=schemas, active_nav="countries")
    write_page("/country/", html)
    register("/country/", "0.9", "weekly")


build_country_index()
print("Built country index")

# ---------------------------------------------------------------------------
# CITY INDEX (/city/)
# ---------------------------------------------------------------------------

def build_city_index():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Cities", None)])

    us_sorted = sorted(US_CITIES, key=lambda x: x["name"])
    us_rows = "".join(
        f'''<a href="/city/{c['slug']}/" class="flex items-center justify-between px-4 py-3 hover:bg-sky-50 border-b border-gray-100 last:border-0">
          <span class="text-gray-900 font-medium">{c['name']}, {c['state']}</span>
          {rating_badge(c['rating'])}
        </a>''' for c in us_sorted
    )
    intl_sorted = sorted(INTL_CITIES, key=lambda x: re.sub('<[^<]+?>', '', x["name"]))
    intl_rows = "".join(
        f'''<a href="/city/{c['slug']}/" class="flex items-center justify-between px-4 py-3 hover:bg-sky-50 border-b border-gray-100 last:border-0">
          <span class="text-gray-900 font-medium">{c['name']}, {c['country_name']}</span>
          {rating_badge(c['rating'])}
        </a>''' for c in intl_sorted
    )

    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-3">Tap Water Safety by City</h1>
    <p class="text-gray-600 mb-8">Drinking water safety ratings for {len(US_CITIES)} US cities and {len(INTL_CITIES)} world cities. Select a city for water source, quality data, and practical tips.</p>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">US Cities ({len(US_CITIES)})</h2></div>
      {us_rows}
    </div>
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">World Cities ({len(INTL_CITIES)})</h2></div>
      {intl_rows}
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    title = "All Cities &mdash; Tap Water Safety by City | TapWaterGuide"
    desc = f"Browse tap water safety ratings for {len(US_CITIES)} US cities and {len(INTL_CITIES)} world cities covered by TapWaterGuide."
    html = page(title, desc, "/city/", body, schemas=schemas, active_nav="world")
    write_page("/city/", html)
    register("/city/", "0.9", "weekly")


build_city_index()
print("Built city index")

# ---------------------------------------------------------------------------
# RANKINGS PAGES
# ---------------------------------------------------------------------------

def ranking_row(name, href, rating, note=""):
    note_html = f'<div class="text-xs text-gray-400 mt-0.5">{note}</div>' if note else ""
    return f'''<a href="{href}" class="flex items-center justify-between px-4 py-3 hover:bg-sky-50 border-b border-gray-100 last:border-0">
      <div><span class="text-gray-900 font-medium">{name}</span>{note_html}</div>
      {rating_badge(rating)}
    </a>'''


BEST_ORDER = ["iceland", "finland", "switzerland", "denmark", "austria", "norway", "singapore",
              "sweden", "netherlands", "germany"]


def build_best_tap_water():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Rankings", "/rankings/"), ("Best Tap Water Worldwide", None)])
    safe = [COUNTRY_BY_SLUG[s] for s in BEST_ORDER]
    rest = sorted([c for c in COUNTRIES if c["rating"] == "Safe" and c["slug"] not in BEST_ORDER], key=lambda x: x["name"])
    gensafe = sorted([c for c in COUNTRIES if c["rating"] == "Generally Safe"], key=lambda x: x["name"])

    top_rows = "".join(ranking_row(f"{i+1}. {c['name']}", f"/country/{c['slug']}/", c["rating"]) for i, c in enumerate(safe))
    rest_rows = "".join(ranking_row(c["name"], f"/country/{c['slug']}/", c["rating"]) for c in rest)
    gensafe_rows = "".join(ranking_row(c["name"], f"/country/{c['slug']}/", c["rating"]) for c in gensafe)

    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-3">Countries with the Best Tap Water</h1>
    <p class="text-gray-600 mb-8">Ranked by overall water quality, treatment infrastructure, and international reputation. These are countries where tap water is safe to drink everywhere, with minimal treatment needed and consistently excellent taste.</p>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">Top 10</h2></div>
      {top_rows}
    </div>
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">Also Rated Safe</h2></div>
      {rest_rows}
    </div>
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">Generally Safe (minor regional exceptions)</h2></div>
      {gensafe_rows}
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    title = "Best Tap Water in the World: Countries Ranked | TapWaterGuide"
    desc = "Iceland, Finland, and Switzerland top the list of countries with the safest, best-tasting tap water. See the full worldwide ranking."
    html = page(title, desc, "/rankings/best-tap-water/", body, schemas=schemas, active_nav="rankings")
    write_page("/rankings/best-tap-water/", html)
    register("/rankings/best-tap-water/", "0.9", "monthly")


def build_worst_tap_water():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Rankings", "/rankings/"), ("Countries to Avoid Tap Water", None)])
    notsafe = sorted([c for c in COUNTRIES if c["rating"] == "Not Safe"], key=lambda x: x["name"])
    caution = sorted([c for c in COUNTRIES if c["rating"] == "Caution"], key=lambda x: x["name"])

    notsafe_rows = "".join(ranking_row(c["name"], f"/country/{c['slug']}/", c["rating"]) for c in notsafe)
    caution_rows = "".join(ranking_row(c["name"], f"/country/{c['slug']}/", c["rating"]) for c in caution)

    body = f"""
<section class="bg-gradient-to-b from-red-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-3">Countries Where You Should Avoid Tap Water</h1>
    <p class="text-gray-600 mb-8">In these destinations, stick to bottled, boiled, or properly filtered water. This isn't necessarily about poor infrastructure everywhere &mdash; it often reflects aging distribution pipes that recontaminate water after it leaves the treatment plant, or a lack of centralized treatment altogether.</p>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">Not Safe &mdash; Avoid Tap Water</h2></div>
      {notsafe_rows}
    </div>
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">Caution &mdash; Bottled Water Recommended</h2></div>
      {caution_rows}
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    title = "Worst Tap Water: Countries to Avoid Drinking From the Tap | TapWaterGuide"
    desc = "See which countries have unsafe tap water for travelers, from India to Egypt, and why bottled or filtered water is recommended in each."
    html = page(title, desc, "/rankings/worst-tap-water/", body, schemas=schemas, active_nav="rankings")
    write_page("/rankings/worst-tap-water/", html)
    register("/rankings/worst-tap-water/", "0.9", "monthly")


US_BEST_ORDER = ["new-york-city", "san-francisco", "seattle", "portland", "boston", "memphis",
                  "denver", "salt-lake-city"]


def build_best_tap_water_us():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Rankings", "/rankings/"), ("Best US City Water", None)])
    top = [US_BY_SLUG[s] for s in US_BEST_ORDER]
    rest = sorted([c for c in US_CITIES if c["slug"] not in US_BEST_ORDER], key=lambda x: x["name"])

    top_rows = "".join(ranking_row(f"{i+1}. {c['name']}, {c['state']}", f"/city/{c['slug']}/", c["rating"]) for i, c in enumerate(top))
    rest_rows = "".join(ranking_row(f"{c['name']}, {c['state']}", f"/city/{c['slug']}/", c["rating"]) for c in rest)

    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-3">Best Tap Water in US Cities</h1>
    <p class="text-gray-600 mb-8">All {len(US_CITIES)} cities on TapWaterGuide meet EPA Safe Drinking Water Act standards. This ranking highlights cities whose water is exceptional by source quality &mdash; several draw from protected watersheds so clean they're exempt from full filtration requirements, a distinction held by only a handful of U.S. systems.</p>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">Top Tier &mdash; Exceptional Source Water</h2></div>
      {top_rows}
    </div>
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">All Other Cities (All EPA-Compliant)</h2></div>
      {rest_rows}
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    title = "Best Tap Water in US Cities: Rankings | TapWaterGuide"
    desc = "New York, San Francisco, and Seattle lead U.S. cities for tap water quality, drawing from protected watersheds. See the full city-by-city ranking."
    html = page(title, desc, "/rankings/best-tap-water-us/", body, schemas=schemas, active_nav="us")
    write_page("/rankings/best-tap-water-us/", html)
    register("/rankings/best-tap-water-us/", "0.9", "monthly")


def build_rankings_index():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Rankings", None)])
    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-6">Tap Water Rankings</h1>
    <div class="grid md:grid-cols-3 gap-6">
      <a href="/rankings/best-tap-water/" class="block bg-gradient-to-br from-emerald-50 to-white rounded-xl border border-emerald-100 p-6 hover:shadow-md transition-shadow">
        <h2 class="font-bold text-gray-900 mb-2">Best Tap Water Worldwide</h2>
        <p class="text-sm text-gray-600">Countries where tap water is safest and best-tasting.</p>
      </a>
      <a href="/rankings/worst-tap-water/" class="block bg-gradient-to-br from-red-50 to-white rounded-xl border border-red-100 p-6 hover:shadow-md transition-shadow">
        <h2 class="font-bold text-gray-900 mb-2">Countries to Avoid Tap Water</h2>
        <p class="text-sm text-gray-600">Where to stick to bottled or filtered water.</p>
      </a>
      <a href="/rankings/best-tap-water-us/" class="block bg-gradient-to-br from-sky-50 to-white rounded-xl border border-sky-100 p-6 hover:shadow-md transition-shadow">
        <h2 class="font-bold text-gray-900 mb-2">Best US City Water</h2>
        <p class="text-sm text-gray-600">Which American cities have the cleanest tap water.</p>
      </a>
      <a href="/rankings/best-tap-water-cities/" class="block bg-gradient-to-br from-emerald-50 to-white rounded-xl border border-emerald-100 p-6 hover:shadow-md transition-shadow">
        <h2 class="font-bold text-gray-900 mb-2">Best Tap Water Cities Worldwide</h2>
        <p class="text-sm text-gray-600">World cities with the purest, best-tasting tap water.</p>
      </a>
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    title = "Tap Water Rankings &mdash; Best &amp; Worst Worldwide | TapWaterGuide"
    desc = "Compare tap water quality rankings worldwide and across US cities, from the safest, best-tasting water to destinations where you should avoid the tap."
    html = page(title, desc, "/rankings/", body, schemas=schemas, active_nav="rankings")
    write_page("/rankings/", html)
    register("/rankings/", "0.8", "monthly")


CITY_BEST_ORDER = ["reykjavik", "zurich", "vienna", "oslo", "copenhagen", "munich",
                   "singapore-city", "tokyo", "sydney", "auckland"]


def build_best_tap_water_cities():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Rankings", "/rankings/"), ("Best Tap Water Cities", None)])
    top = [INTL_BY_SLUG[s] for s in CITY_BEST_ORDER]
    top_slugs = set(CITY_BEST_ORDER)
    rest_safe = sorted([c for c in INTL_CITIES if c["rating"] == "Safe" and c["slug"] not in top_slugs],
                       key=lambda x: re.sub('<[^<]+?>', '', x["name"]))

    top_rows = "".join(ranking_row(f"{i+1}. {c['name']}", f"/city/{c['slug']}/", c["rating"], note=c["country_name"]) for i, c in enumerate(top))
    rest_rows = "".join(ranking_row(c["name"], f"/city/{c['slug']}/", c["rating"], note=c["country_name"]) for c in rest_safe)

    body = f"""
<section class="bg-gradient-to-b from-emerald-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-3">Cities with the Best Tap Water in the World</h1>
    <p class="text-gray-600 mb-8">Ranked by source purity, treatment quality, and taste. The top of this list is dominated by cities drawing on protected springs, alpine catchments, and glacial or volcanic sources &mdash; several need little or no chemical treatment at all.</p>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">Top 10</h2></div>
      {top_rows}
    </div>
    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
      <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">Also Rated Safe</h2></div>
      {rest_rows}
    </div>

    <div class="mt-8 flex flex-wrap gap-3">
      <a href="/rankings/best-tap-water/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">Best tap water by country &rarr;</a>
      <a href="/city/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">Browse all cities &rarr;</a>
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    title = "Best Tap Water Cities in the World: Rankings | TapWaterGuide"
    desc = "Reykjavik, Zurich, and Vienna top the list of world cities with the best tap water, drawing on springs and alpine sources. See the full ranking."
    html = page(title, desc, "/rankings/best-tap-water-cities/", body, schemas=schemas, active_nav="rankings")
    write_page("/rankings/best-tap-water-cities/", html)
    register("/rankings/best-tap-water-cities/", "0.9", "monthly")


build_best_tap_water()
build_worst_tap_water()
build_best_tap_water_us()
build_best_tap_water_cities()
build_rankings_index()
print("Built rankings pages")

# ---------------------------------------------------------------------------
# REGION HUB PAGES (/region/<slug>/)
# ---------------------------------------------------------------------------

REGION_META = {
    "Europe": {
        "slug": "europe",
        "intro": "Europe has the most consistently safe tap water of any continent, anchored by the EU Drinking Water Directive &mdash; one of the strictest water quality frameworks in the world. Nearly all of Western, Northern, and Central Europe is safe to drink from the tap. The picture is more mixed in parts of the Balkans and Eastern Europe, where aging Soviet-era infrastructure can compromise well-treated water on its way to the tap.",
        "desc": "Tap water is safe in most of Europe under strict EU standards. See safety ratings for every European country and city, from Iceland to Albania.",
    },
    "Asia": {
        "slug": "asia",
        "intro": "Asia spans the full spectrum of tap water safety. Japan, South Korea, Singapore, and Hong Kong treat water to among the highest standards on Earth, while in most of South and Southeast Asia &mdash; India, Thailand, Vietnam, Indonesia &mdash; even locals rely on boiled, filtered, or bottled water due to distribution infrastructure that recontaminates treated water before it reaches the tap.",
        "desc": "Asia's tap water ranges from world-class (Japan, Singapore) to unsafe (India, Thailand, Vietnam). See ratings for every Asian country and city.",
    },
    "North America": {
        "slug": "north-america",
        "intro": "North America splits sharply at the Rio Grande. The United States and Canada maintain EPA- and Health Canada-regulated systems that are safe nationwide. Mexico and most of Central America are a different story &mdash; municipal treatment exists, but aging pipes and intermittent pressure make bottled water the norm. The Caribbean varies island by island, with desalination-dependent nations often faring better than expected.",
        "desc": "US and Canadian tap water is safe; Mexico and most of Central America is not. See ratings for every North American country and city.",
    },
    "South America": {
        "slug": "south-america",
        "intro": "South America's tap water quality tracks closely with infrastructure investment. Chile and Uruguay lead the continent with reliably safe urban water, and Argentina's major cities are largely safe. Elsewhere &mdash; Peru, Ecuador, and much of Colombia and Brazil &mdash; treatment at the plant is often undone by distribution problems, making bottled or filtered water the sensible default for travelers.",
        "desc": "Chile and Uruguay have South America's safest tap water; Peru and Ecuador require bottled water. See every country and city rating.",
    },
    "Africa": {
        "slug": "africa",
        "intro": "Africa has the world's largest gap between water treatment capability and reliable delivery. South Africa's major cities have historically maintained good municipal water, and Morocco's urban systems are chemically treated, but for most of the continent &mdash; including tourist destinations in Kenya, Tanzania, and Egypt &mdash; bottled or purified water is essential for visitors.",
        "desc": "Most of Africa requires bottled water for travelers, with partial exceptions in South Africa's cities. See every African country and city rating.",
    },
    "Oceania": {
        "slug": "oceania",
        "intro": "Australia and New Zealand maintain some of the world's most reliable tap water, with strict national standards and well-funded utilities. Tap water is safe to drink in every major city and town in both countries. The smaller Pacific island nations vary widely and often depend on rainwater collection and limited treatment infrastructure.",
        "desc": "Yes, tap water is safe throughout Australia and New Zealand. See ratings for Oceania's countries and major cities.",
    },
    "Middle East": {
        "slug": "middle-east",
        "intro": "The Middle East runs almost entirely on desalinated seawater, and the engineering is world-class &mdash; Israel, the UAE, and Qatar produce water that meets WHO standards at the plant. The catch is the last mile: rooftop storage tanks and building plumbing mean many residents still prefer bottled water, and travelers will find bottled water is the cultural default nearly everywhere.",
        "desc": "Middle East tap water is desalinated to WHO standards in Israel, UAE, and Qatar, though bottled remains the local norm. See all ratings.",
    },
}

RATING_ORDER = ["Safe", "Generally Safe", "Caution", "Not Safe"]


def build_region_page(region_name):
    meta = REGION_META[region_name]
    rslug = meta["slug"]
    countries = sorted([c for c in COUNTRIES if c["region"] == region_name], key=lambda x: x["name"])
    if not countries:
        return
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Countries", "/country/"), (region_name, None)])

    groups_html = ""
    for rating in RATING_ORDER:
        group = [c for c in countries if c["rating"] == rating]
        if not group:
            continue
        rows = "".join(
            f'''<a href="/country/{c['slug']}/" class="flex items-center justify-between px-4 py-3 hover:bg-sky-50 border-b border-gray-100 last:border-0">
              <span class="text-gray-900 font-medium">{c['name']}</span>
              {rating_badge(c['rating'])}
            </a>''' for c in group
        )
        groups_html += f"""<div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
          <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">{rating} ({len(group)})</h2></div>
          {rows}
        </div>"""

    region_cities = sorted(
        [ci for ci in INTL_CITIES if COUNTRY_BY_SLUG[ci["country_slug"]]["region"] == region_name],
        key=lambda x: re.sub('<[^<]+?>', '', x["name"]))
    cities_html = ""
    if region_cities:
        cards = "".join(
            f'''<a href="/city/{ci["slug"]}/" class="block bg-white rounded-lg border border-gray-200 p-4 hover:border-sky-300 hover:shadow-md transition-all">
              <div class="flex items-center justify-between">
                <span class="font-semibold text-gray-900">{ci["name"]}</span>
                {rating_badge(ci["rating"])}
              </div>
              <div class="text-xs text-gray-400 mt-1">{ci["country_name"]}</div>
            </a>''' for ci in region_cities
        )
        cities_html = f"""<h2 class="text-2xl font-bold text-gray-900 mb-4 mt-10">City Guides in {region_name}</h2>
        <div class="grid sm:grid-cols-2 md:grid-cols-3 gap-3">{cards}</div>"""

    other_regions = "".join(
        f'<a href="/region/{REGION_META[r]["slug"]}/" class="text-sky-700 hover:underline">{r}</a>'
        for r in REGION_META if r != region_name
    )

    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-3">Tap Water Safety in {region_name}</h1>
    <p class="text-gray-600 leading-relaxed mb-8">{meta['intro']}</p>
    {groups_html}
    {cities_html}
    <div class="bg-sky-50 rounded-xl border border-sky-100 p-6 mt-10">
      <h2 class="text-lg font-bold text-gray-900 mb-3">Other Regions</h2>
      <div class="flex flex-wrap gap-x-4 gap-y-2 text-sm">{other_regions}</div>
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    title = f"Tap Water Safety in {region_name}: Every Country Rated | TapWaterGuide"
    html = page(title, meta["desc"], f"/region/{rslug}/", body, schemas=schemas, active_nav="countries")
    write_page(f"/region/{rslug}/", html)
    register(f"/region/{rslug}/", "0.8", "monthly")


for _region in REGION_META:
    build_region_page(_region)
print(f"Built {len(REGION_META)} region hub pages")

# ---------------------------------------------------------------------------
# INTERACTIVE WORLD MAP (/map/)
# ---------------------------------------------------------------------------

ISO2SLUG = {
    "JP": "japan", "IT": "italy", "CR": "costa-rica", "MX": "mexico", "ES": "spain",
    "PT": "portugal", "IS": "iceland", "FR": "france", "DE": "germany", "HR": "croatia",
    "GR": "greece", "TR": "turkey", "TH": "thailand", "MA": "morocco", "IN": "india",
    "VN": "vietnam", "KR": "south-korea", "AR": "argentina", "PE": "peru", "CO": "colombia",
    "EG": "egypt", "PH": "philippines", "CU": "cuba", "BR": "brazil", "DO": "dominican-republic",
    "SG": "singapore", "GB": "united-kingdom", "IE": "ireland", "AU": "australia",
    "NZ": "new-zealand", "CA": "canada", "NL": "netherlands", "AT": "austria",
    "CH": "switzerland", "CZ": "czech-republic", "HU": "hungary", "PL": "poland",
    "NO": "norway", "SE": "sweden", "DK": "denmark", "FI": "finland", "ZA": "south-africa",
    "KE": "kenya", "TZ": "tanzania", "ID": "indonesia", "MY": "malaysia", "KH": "cambodia",
    "LA": "laos", "MM": "myanmar", "NP": "nepal", "AE": "united-arab-emirates",
    "HK": "hong-kong", "LT": "lithuania", "LV": "latvia", "CY": "cyprus", "BG": "bulgaria",
    "UY": "uruguay", "NI": "nicaragua", "KY": "cayman-islands", "SV": "el-salvador",
    "LK": "sri-lanka", "QA": "qatar", "CL": "chile", "GE": "georgia", "ME": "montenegro",
    "RU": "russia", "BS": "bahamas", "EE": "estonia", "AL": "albania", "RO": "romania",
    "BM": "bermuda", "IL": "israel", "UA": "ukraine", "BE": "belgium", "MT": "malta",
    "EC": "ecuador", "PA": "panama", "CN": "china", "TW": "taiwan",
}

MAP_FILL = {
    "Safe": "#34d399",
    "Generally Safe": "#38bdf8",
    "Caution": "#fbbf24",
    "Not Safe": "#f87171",
}
MAP_FILL_NONE = "#e5e7eb"

# Small territories absent from the 110m map, drawn as circle markers: slug -> (lon, lat)
SMALL_TERRITORIES = {
    "singapore": (103.8, 1.35),
    "hong-kong": (114.15, 22.3),
    "malta": (14.4, 35.9),
    "bermuda": (-64.75, 32.3),
    "cayman-islands": (-81.2, 19.3),
}


def _map_project(lon, lat, w, h):
    x = (lon + 180.0) / 360.0 * w
    y = (85.0 - lat) / 145.0 * h
    return round(x, 1), round(y, 1)


def build_map_page():
    with open(os.path.join(os.path.dirname(__file__), "world_map_data.json"), "r", encoding="utf-8") as f:
        mapdata = _json.load(f)
    w, h = mapdata["width"], mapdata["height"]

    paths = []
    for cdata in mapdata["countries"]:
        iso = cdata["iso"]
        slug = ISO2SLUG.get(iso)
        if slug and slug in COUNTRY_BY_SLUG:
            c = COUNTRY_BY_SLUG[slug]
            fill = MAP_FILL[c["rating"]]
            p = (f'<a href="/country/{slug}/"><path d="{cdata["path"]}" fill="{fill}" '
                 f'fill-rule="evenodd" stroke="#fff" stroke-width="0.5" class="mc" '
                 f'data-name="{c["name"]}" data-rating="{c["rating"]}"/></a>')
        elif iso == "US":
            p = (f'<a href="/rankings/best-tap-water-us/"><path d="{cdata["path"]}" fill="{MAP_FILL["Safe"]}" '
                 f'fill-rule="evenodd" stroke="#fff" stroke-width="0.5" class="mc" '
                 f'data-name="United States" data-rating="Safe &#8212; see city guides"/></a>')
        else:
            p = (f'<path d="{cdata["path"]}" fill="{MAP_FILL_NONE}" fill-rule="evenodd" '
                 f'stroke="#fff" stroke-width="0.5" class="mc" data-name="{cdata["name"]}" '
                 f'data-rating="Not yet covered"/>')
        paths.append(p)

    for slug, (lon, lat) in SMALL_TERRITORIES.items():
        if slug not in COUNTRY_BY_SLUG:
            continue
        c = COUNTRY_BY_SLUG[slug]
        x, y = _map_project(lon, lat, w, h)
        fill = MAP_FILL[c["rating"]]
        paths.append(
            f'<a href="/country/{slug}/"><circle cx="{x}" cy="{y}" r="4" fill="{fill}" '
            f'stroke="#fff" stroke-width="1" class="mc" data-name="{c["name"]}" '
            f'data-rating="{c["rating"]}"/></a>')

    legend_items = "".join(
        f'''<span class="inline-flex items-center gap-2 text-sm text-gray-600">
          <span class="inline-block w-4 h-4 rounded" style="background:{color}"></span>{label}</span>'''
        for label, color in [("Safe", MAP_FILL["Safe"]), ("Generally Safe", MAP_FILL["Generally Safe"]),
                             ("Caution", MAP_FILL["Caution"]), ("Not Safe", MAP_FILL["Not Safe"]),
                             ("Not yet covered", MAP_FILL_NONE)]
    )

    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("World Map", None)])

    n_safe = sum(1 for c in COUNTRIES if c["rating"] == "Safe")
    n_gen = sum(1 for c in COUNTRIES if c["rating"] == "Generally Safe")
    n_caution = sum(1 for c in COUNTRIES if c["rating"] == "Caution")
    n_notsafe = sum(1 for c in COUNTRIES if c["rating"] == "Not Safe")

    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-6xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-6xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-3">World Tap Water Safety Map</h1>
    <p class="text-gray-600 mb-6">Every country TapWaterGuide covers, colored by drinking water safety rating. Click any colored country for its full guide. Hover (or tap) for a quick verdict.</p>

    <div class="flex flex-wrap gap-4 mb-4">{legend_items}</div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-2 md:p-4 relative">
      <svg viewBox="0 0 {w} {h}" width="{int(w)}" height="{int(h)}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="World map of tap water safety ratings" style="width:100%;height:auto">
        {''.join(paths)}
      </svg>
      <div id="mapTip" class="hidden absolute z-10 bg-gray-900 text-white text-sm rounded-lg px-3 py-1.5 pointer-events-none shadow-lg" style="max-width:220px"></div>
    </div>

    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mt-6">
      {stat_pill('Safe', n_safe)}
      {stat_pill('Generally Safe', n_gen)}
      {stat_pill('Caution', n_caution)}
      {stat_pill('Not Safe', n_notsafe)}
    </div>

    <div class="mt-8 flex flex-wrap gap-3">
      <a href="/country/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">Browse all countries as a list &rarr;</a>
      <a href="/rankings/best-tap-water/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">Best tap water rankings &rarr;</a>
    </div>
  </div>
</section>

<style>
.mc {{ transition: opacity .15s; cursor: pointer; }}
a:hover .mc, .mc:hover {{ opacity: .75; }}
</style>
<script>
(function(){{
  var tip = document.getElementById('mapTip');
  var box = tip.parentElement;
  document.querySelectorAll('.mc').forEach(function(el){{
    el.addEventListener('mousemove', function(ev){{
      var r = box.getBoundingClientRect();
      tip.innerHTML = '<strong>' + el.getAttribute('data-name') + '</strong><br>' + el.getAttribute('data-rating');
      tip.style.left = Math.min(ev.clientX - r.left + 12, r.width - 230) + 'px';
      tip.style.top = (ev.clientY - r.top + 12) + 'px';
      tip.classList.remove('hidden');
    }});
    el.addEventListener('mouseleave', function(){{ tip.classList.add('hidden'); }});
  }});
}})();
</script>
"""
    schemas = [bc_ld]
    title = "World Tap Water Safety Map &mdash; Interactive | TapWaterGuide"
    desc = f"Interactive world map of tap water safety: {len(COUNTRIES)} countries rated Safe, Generally Safe, Caution, or Not Safe. Click any country for details."
    html = page(title, desc, "/map/", body, schemas=schemas, active_nav="map")
    write_page("/map/", html)
    register("/map/", "0.9", "monthly")


build_map_page()
print("Built world map page")

# ---------------------------------------------------------------------------
# GUIDES CONTENT HUB (/guides/ and /guides/<slug>/)
# ---------------------------------------------------------------------------

GUIDE_BY_SLUG = {g["slug"]: g for g in GUIDES}


def build_guide_page(g):
    slug = g["slug"]
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Guides", "/guides/"), (g["title"], None)])

    sections_html = "".join(section_card(heading, body) for heading, body in g["sections"])
    faq_html, faq_ld = faq_block(g["faqs"])

    related_links = "".join(
        f'<a href="/guides/{r}/" class="text-sky-700 hover:underline">{GUIDE_BY_SLUG[r]["title"]}</a>'
        for r in g["related"] if r in GUIDE_BY_SLUG
    )
    related_html = f"""<div class="bg-sky-50 rounded-xl border border-sky-100 p-6">
      <h2 class="text-lg font-bold text-gray-900 mb-3">Related Guides</h2>
      <div class="flex flex-wrap gap-x-4 gap-y-2 text-sm">{related_links}</div>
    </div>"""

    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>

<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <div class="flex flex-wrap items-center gap-3 mb-4">
      {reviewed_badge()}
    </div>
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{g['title']}</h1>
    <p class="text-lg text-gray-700 leading-relaxed mb-6">{g['intro']}</p>

    <div class="space-y-6">
      {sections_html}
      {faq_html}
      {related_html}
    </div>

    <div class="mt-8 flex flex-wrap gap-3">
      <a href="/guides/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">&larr; All guides</a>
      <a href="/map/" class="inline-flex items-center gap-1.5 text-sm text-sky-700 hover:underline">Check any destination on the world safety map &rarr;</a>
    </div>
  </div>
</section>
"""
    schemas = [bc_ld]
    if faq_ld:
        schemas.append(faq_ld)
    schemas.append(article_schema(g["title"], g["meta_description"], f"{DOMAIN}/guides/{slug}/"))

    title = f"{g['title']} | TapWaterGuide"
    html = page(title, g["meta_description"], f"/guides/{slug}/", body, schemas=schemas, active_nav="guides")
    write_page(f"/guides/{slug}/", html)
    register(f"/guides/{slug}/", "0.8", "monthly")


def build_guides_index():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Guides", None)])
    cards = "".join(
        f'''<a href="/guides/{g["slug"]}/" class="block bg-white rounded-xl border border-gray-200 p-6 hover:border-sky-300 hover:shadow-md transition-all">
          <h2 class="font-bold text-gray-900 mb-2">{g["title"]}</h2>
          <p class="text-sm text-gray-600">{g["meta_description"]}</p>
        </a>''' for g in GUIDES
    )

    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>
<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-900 mb-3">Tap Water Guides</h1>
    <p class="text-gray-600 mb-8">Practical, evergreen guides to drinking water safety &mdash; purification methods, travel precautions, water chemistry explained, and what to do when the tap can't be trusted. Each guide pairs with our <a href="/country/" class="text-sky-700 hover:underline">country</a> and <a href="/city/" class="text-sky-700 hover:underline">city</a> ratings.</p>
    <div class="grid md:grid-cols-2 gap-4">{cards}</div>
  </div>
</section>
"""
    schemas = [bc_ld]
    title = "Tap Water Guides: Purification, Travel Safety &amp; Water Quality | TapWaterGuide"
    desc = f"{len(GUIDES)} practical guides to tap water safety: purification methods, travel precautions, baby formula, hardness, TDS, and more."
    html = page(title, desc, "/guides/", body, schemas=schemas, active_nav="guides")
    write_page("/guides/", html)
    register("/guides/", "0.9", "weekly")


for _g in GUIDES:
    build_guide_page(_g)
build_guides_index()
print(f"Built {len(GUIDES)} guide pages and guides index")

# ---------------------------------------------------------------------------
# ABOUT PAGE
# ---------------------------------------------------------------------------

def build_about():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("About", None)])
    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-8">
  <div class="max-w-3xl mx-auto">
    {bc_html}
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mt-4 mb-3">About TapWaterGuide</h1>
    <p class="text-gray-600">A free, worldwide reference for tap water safety &mdash; built for travelers deciding whether to drink the tap, and for anyone checking the quality of their own city's water.</p>
  </div>
</section>

<section class="px-4 py-8">
  <div class="max-w-3xl mx-auto space-y-6">

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-3">What We Cover</h2>
      <p class="text-gray-600 leading-relaxed">TapWaterGuide currently covers {len(COUNTRIES)} countries and {len(US_CITIES) + len(INTL_CITIES)} cities ({len(US_CITIES)} US, {len(INTL_CITIES)} international), each with a safety rating, water source detail, known contaminant concerns, and practical guidance. We rate every destination on a simple four-tier scale: <strong class="text-gray-900">Safe</strong>, <strong class="text-gray-900">Generally Safe</strong>, <strong class="text-gray-900">Caution</strong>, and <strong class="text-gray-900">Not Safe</strong>.</p>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6" id="sources">
      <h2 class="text-xl font-bold text-gray-900 mb-4">Data Sources &amp; Methodology</h2>
      <div class="space-y-4">
        <div class="border-l-4 border-sky-500 pl-4">
          <p class="font-bold text-gray-900">World Health Organization (WHO)</p>
          <p class="text-sm text-gray-600">WHO Guidelines for Drinking-water Quality inform our understanding of international safety benchmarks and inform country-level ratings, particularly for travel health context.</p>
        </div>
        <div class="border-l-4 border-sky-500 pl-4">
          <p class="font-bold text-gray-900">US EPA (Environmental Protection Agency)</p>
          <p class="text-sm text-gray-600">The Safe Drinking Water Act and its National Primary Drinking Water Regulations set the legal compliance standard referenced on every US city page, including limits for lead, arsenic, disinfection byproducts, and PFAS.</p>
        </div>
        <div class="border-l-4 border-sky-500 pl-4">
          <p class="font-bold text-gray-900">Environmental Working Group (EWG)</p>
          <p class="text-sm text-gray-600">EWG's Tap Water Database and related research inform the contaminant context on US city pages, particularly around contaminants regulated below EPA's legal limits but above EWG's more precautionary health guidelines.</p>
        </div>
        <div class="border-l-4 border-sky-500 pl-4">
          <p class="font-bold text-gray-900">US CDC (Centers for Disease Control and Prevention)</p>
          <p class="text-sm text-gray-600">CDC Travelers' Health guidance informs our country-level traveler precautions and food-and-water safety recommendations for international destinations.</p>
        </div>
        <div class="border-l-4 border-sky-500 pl-4">
          <p class="font-bold text-gray-900">National &amp; municipal water utilities</p>
          <p class="text-sm text-gray-600">Individual water authority public reports (consumer confidence reports, annual water quality reports) inform source, treatment, and hardness detail for specific cities.</p>
        </div>
      </div>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-3">How We Rate</h2>
      <div class="space-y-3">
        <div class="flex items-start gap-3"><span class="mt-0.5">{rating_badge('Safe')}</span><p class="text-sm text-gray-600 flex-1">Tap water is safe to drink nationwide or citywide with no special precautions.</p></div>
        <div class="flex items-start gap-3"><span class="mt-0.5">{rating_badge('Generally Safe')}</span><p class="text-sm text-gray-600 flex-1">Safe in most areas, with documented regional or historical exceptions worth knowing about.</p></div>
        <div class="flex items-start gap-3"><span class="mt-0.5">{rating_badge('Caution')}</span><p class="text-sm text-gray-600 flex-1">Municipally treated but not generally recommended for direct drinking; bottled or boiled water advised.</p></div>
        <div class="flex items-start gap-3"><span class="mt-0.5">{rating_badge('Not Safe')}</span><p class="text-sm text-gray-600 flex-1">Not safe to drink from the tap; bottled, boiled, or properly filtered water is necessary.</p></div>
      </div>
    </div>

    <div class="bg-amber-50 border border-amber-200 rounded-xl p-6">
      <h2 class="text-xl font-bold text-amber-800 mb-3">Disclaimer</h2>
      <p class="text-amber-900 text-sm leading-relaxed">TapWaterGuide is an informational reference, not medical or travel advice. Water quality and infrastructure conditions change over time, including through drought, natural disasters, and infrastructure failures. Always check current local advisories, your accommodation, or your embassy's travel health guidance before making decisions about drinking water, especially for infants, pregnant travelers, or those who are immunocompromised.</p>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6" id="contact">
      <h2 class="text-xl font-bold text-gray-900 mb-3">Contact</h2>
      <p class="text-gray-600">Found an error or have a correction? We'd love to hear from you.</p>
      <p class="mt-3"><a href="mailto:info@tapwaterguide.org" class="text-sky-600 hover:text-sky-800 font-medium">info@tapwaterguide.org</a></p>
    </div>

  </div>
</section>
"""
    schemas = [bc_ld, {
        "@context": "https://schema.org", "@type": "AboutPage",
        "name": "About TapWaterGuide", "url": f"{DOMAIN}/about/",
        "mainEntity": {"@type": "Organization", "name": SITE, "url": DOMAIN, "email": "info@tapwaterguide.org"},
    }]
    title = "About TapWaterGuide &mdash; Data Sources &amp; Methodology"
    desc = "How TapWaterGuide rates tap water safety worldwide, using WHO, EPA, EWG, and CDC data. See our methodology, rating scale, and sources."
    html = page(title, desc, "/about/", body, schemas=schemas, active_nav="")
    write_page("/about/", html)
    register("/about/", "0.6", "yearly")


build_about()
print("Built about page")

# ---------------------------------------------------------------------------
# PRIVACY POLICY PAGE
# ---------------------------------------------------------------------------

def build_privacy():
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("Privacy Policy", None)])
    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-8">
  <div class="max-w-3xl mx-auto">
    {bc_html}
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mt-4 mb-3">Privacy Policy</h1>
    <p class="text-gray-600">Effective date: <time datetime="{LAST_REVIEWED}">{LAST_REVIEWED_DISPLAY}</time></p>
  </div>
</section>

<section class="px-4 py-8">
  <div class="max-w-3xl mx-auto space-y-6">

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-3">Overview</h2>
      <p class="text-gray-600 leading-relaxed">TapWaterGuide.org is a free informational reference. We do not require accounts, do not collect names or email addresses through the site, and do not sell any data. This policy explains the limited data collected automatically when you visit.</p>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-3">Analytics</h2>
      <p class="text-gray-600 leading-relaxed mb-3">We use Google Analytics 4 to understand aggregate site usage &mdash; which pages are visited, from which countries, and on which device types. Google Analytics uses cookies and collects data such as your approximate location (city level), browser type, and pages viewed. IP addresses are not logged or stored by us.</p>
      <p class="text-gray-600 leading-relaxed">You can opt out of Google Analytics with the <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener" class="text-sky-700 hover:underline">Google Analytics Opt-out Browser Add-on</a>, or by using a content blocker or your browser's tracking protection.</p>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-3">Cookies</h2>
      <p class="text-gray-600 leading-relaxed">The only cookies set by this site are those used by Google Analytics for anonymous usage measurement. We set no advertising, personalization, or tracking cookies of our own.</p>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-3">Third-Party Services</h2>
      <p class="text-gray-600 leading-relaxed">Pages load fonts from Google Fonts and analytics scripts from Google. These services may receive standard technical request data (such as your IP address) as part of serving those files. See <a href="https://policies.google.com/privacy" target="_blank" rel="noopener" class="text-sky-700 hover:underline">Google's Privacy Policy</a> for how Google handles this data. External links to sources such as WHO, EPA, EWG, and CDC lead to sites with their own privacy policies.</p>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-3">Your Rights</h2>
      <p class="text-gray-600 leading-relaxed">Depending on your jurisdiction (including the EU/EEA under GDPR and California under CCPA), you may have rights to access, correct, or delete personal data. Because we collect no directly identifying information, such requests generally apply to Google Analytics data, which you can control through the opt-out tools above. For any privacy question or request, contact us and we will respond promptly.</p>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-3">Changes to This Policy</h2>
      <p class="text-gray-600 leading-relaxed">If our data practices change (for example, if advertising is introduced), this policy will be updated and the effective date revised before those changes take effect.</p>
    </div>

    <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-3">Contact</h2>
      <p class="text-gray-600">Questions about this policy or your data:</p>
      <p class="mt-3"><a href="mailto:info@tapwaterguide.org" class="text-sky-600 hover:text-sky-800 font-medium">info@tapwaterguide.org</a></p>
    </div>

  </div>
</section>
"""
    schemas = [bc_ld]
    title = "Privacy Policy | TapWaterGuide"
    desc = "TapWaterGuide's privacy policy: what limited data is collected via analytics, how cookies are used, and how to opt out."
    html = page(title, desc, "/privacy/", body, schemas=schemas, active_nav="")
    write_page("/privacy/", html)
    register("/privacy/", "0.3", "yearly")


build_privacy()
print("Built privacy page")

# ---------------------------------------------------------------------------
# 404 PAGE
# ---------------------------------------------------------------------------

def build_404():
    body = f"""
<section class="px-4 py-24">
  <div class="max-w-lg mx-auto text-center">
    <div class="inline-flex items-center justify-center w-16 h-16 bg-sky-100 rounded-2xl mb-6">
      <span class="text-sky-600">{ICONS['droplet']}</span>
    </div>
    <h1 class="text-3xl font-bold text-gray-900 mb-3">404 &mdash; Page Not Found</h1>
    <p class="text-gray-600 mb-8">The page you're looking for doesn't exist, may have moved, or the URL was mistyped.</p>
    <div class="flex flex-wrap items-center justify-center gap-3">
      <a href="/" class="px-5 py-2.5 bg-sky-600 text-white rounded-lg font-medium hover:bg-sky-700">Back to Home</a>
      <a href="/country/" class="px-5 py-2.5 bg-white border border-gray-200 text-gray-700 rounded-lg font-medium hover:border-sky-300">Browse Countries</a>
      <a href="/city/" class="px-5 py-2.5 bg-white border border-gray-200 text-gray-700 rounded-lg font-medium hover:border-sky-300">Browse Cities</a>
    </div>
  </div>
</section>
"""
    title = "404 &mdash; Page Not Found | TapWaterGuide"
    desc = "The page you're looking for doesn't exist. Browse our full list of countries and cities instead."
    html = page(title, desc, "/404/", body, active_nav="")
    fs_path = os.path.join(ROOT, "404.html")
    with open(fs_path, "w", encoding="utf-8") as f:
        f.write(html)


build_404()
print("Built 404 page")

# ---------------------------------------------------------------------------
# REDIRECT STUBS (for renamed URLs; not registered in sitemap)
# ---------------------------------------------------------------------------

REDIRECTS = {
    "/country/malta-country/": "/country/malta/",
}


def build_redirects():
    for old, new in REDIRECTS.items():
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Redirecting&hellip;</title>
<link rel="canonical" href="{DOMAIN}{new}">
<meta http-equiv="refresh" content="0; url={new}">
<meta name="robots" content="noindex">
</head>
<body><p>This page has moved to <a href="{new}">{DOMAIN}{new}</a>.</p></body>
</html>"""
        fs_path = os.path.join(ROOT, old.lstrip("/"), "index.html")
        os.makedirs(os.path.dirname(fs_path), exist_ok=True)
        with open(fs_path, "w", encoding="utf-8") as f:
            f.write(html)


build_redirects()
print(f"Built {len(REDIRECTS)} redirect stubs")

# ---------------------------------------------------------------------------
# SITEMAP & ROBOTS & MANIFEST
# ---------------------------------------------------------------------------

def build_sitemap():
    entries = []
    for path, priority, changefreq in ALL_PAGES:
        entries.append(f"""  <url>
    <loc>{DOMAIN}{path}</loc>
    <lastmod>{LAST_REVIEWED}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>
"""
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


def build_robots():
    txt = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(txt)


def build_manifest():
    manifest = {
        "name": "TapWaterGuide",
        "short_name": "TapWaterGuide",
        "icons": [
            {"src": "/assets/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png"},
        ],
        "theme_color": "#0284c7",
        "background_color": "#ffffff",
        "display": "standalone",
    }
    with open(os.path.join(ROOT, "assets", "site.webmanifest"), "w", encoding="utf-8") as f:
        _json.dump(manifest, f, indent=2)


build_sitemap()
build_robots()
build_manifest()
print(f"Built sitemap.xml with {len(ALL_PAGES)} URLs, robots.txt, and site.webmanifest")
