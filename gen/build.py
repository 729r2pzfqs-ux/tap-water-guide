# -*- coding: utf-8 -*-
import os
import sys
import re
import html as htmlmod

sys.path.insert(0, os.path.dirname(__file__))
from templates import (
    page, rating_badge, breadcrumbs, faq_block, stat_pill, RATING_STYLE, ICONS, DOMAIN, SITE,
)
from data_countries import COUNTRIES, BY_SLUG as COUNTRY_BY_SLUG
from data_us_cities import US_CITIES, BY_SLUG as US_BY_SLUG
from data_intl_cities import INTL_CITIES, BY_SLUG as INTL_BY_SLUG

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
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">
    {bc_html}
  </div>
</section>

<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <div class="flex flex-wrap items-center gap-3 mb-4">
      {rating_badge(c['rating'], size='large')}
      <span class="text-sm text-gray-400">{c['region']}</span>
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
      {section_card('Water Hardness', f"<p>{c['hardness']}.</p>")}
      {section_card('Do Locals Drink Tap Water?', f"<p>{c['locals_drink']}</p>")}
      {section_card('Tips for Travelers', tips_html)}
      {section_card('Recommended Precautions', precautions_html)}
      {cities_html}
      {faq_html}
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
    schemas.append({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": f"Is Tap Water Safe to Drink in {c['name']}?",
        "description": c["meta_description"],
        "url": f"{DOMAIN}/country/{slug}/",
        "publisher": {"@type": "Organization", "name": SITE, "url": DOMAIN},
    })

    title = f"Is Tap Water Safe in {c['name']}? Drinking Water Guide | TapWaterGuide"
    html = page(title, c["meta_description"], f"/country/{slug}/", body, schemas=schemas, active_nav="countries")
    write_page(f"/country/{slug}/", html)
    register(f"/country/{slug}/", "0.8", "monthly")


# ---------------------------------------------------------------------------
# US CITY PAGES
# ---------------------------------------------------------------------------

def build_us_city_page(ci):
    slug = ci["slug"]
    bc_html, bc_ld = breadcrumbs([("Home", "/"), ("US Cities", "/rankings/best-tap-water-us/"), (ci["name"], None)])

    contam_html = bullet_list(ci["contaminants"])
    tips_html = bullet_list(ci["tips"])
    faq_html, faq_ld = faq_block(ci["faqs"])

    other_us = [x for x in US_CITIES if x["slug"] != slug][:8]
    import random as _r
    other_links = "".join(f'<a href="/city/{o["slug"]}/" class="text-sky-700 hover:underline">{o["name"]}</a>' for o in other_us[:6])

    body = f"""
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>

<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <div class="flex flex-wrap items-center gap-3 mb-4">
      {rating_badge(ci['rating'], size='large')}
      <span class="text-sm text-gray-400">{ci['state']}, United States</span>
    </div>
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Is Tap Water Safe to Drink in {ci['name']}?</h1>
    <p class="text-lg text-gray-700 leading-relaxed mb-6">{ci['quick_answer']}</p>

    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-8">
      {info_card(ICON_DROP, 'Hardness', ci['hardness'].split(',')[0])}
      {info_card(ICON_SOURCE, 'pH', ci['ph'])}
      {info_card(ICON_MAP, 'TDS', ci['tds'])}
      {info_card(ICON_PEOPLE, 'EPA Status', 'Compliant')}
    </div>

    <div class="space-y-6">
      {section_card('Water Source', f"<p>{ci['water_source']}</p>")}
      {section_card('EPA Compliance Status', f"<p>{ci['epa_status']}</p>")}
      {section_card('Notable Contaminants &amp; Context', contam_html)}
      {section_card('How It Compares', f"<p>{ci['comparison']}</p>")}
      {section_card('Tips', tips_html)}
      {faq_html}
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
    schemas.append({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": f"Is Tap Water Safe to Drink in {ci['name']}?",
        "description": ci["meta_description"],
        "url": f"{DOMAIN}/city/{slug}/",
        "publisher": {"@type": "Organization", "name": SITE, "url": DOMAIN},
    })
    title = f"Is Tap Water Safe in {ci['name']}, {ci['state']}? | TapWaterGuide"
    html = page(title, ci["meta_description"], f"/city/{slug}/", body, schemas=schemas, active_nav="us")
    write_page(f"/city/{slug}/", html)
    register(f"/city/{slug}/", "0.8", "monthly")


# ---------------------------------------------------------------------------
# INTERNATIONAL CITY PAGES
# ---------------------------------------------------------------------------

def build_intl_city_page(ci):
    slug = ci["slug"]
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
<section class="bg-gradient-to-b from-sky-50 to-white px-4 py-6 border-b border-gray-100">
  <div class="max-w-4xl mx-auto">{bc_html}</div>
</section>

<section class="px-4 py-8">
  <div class="max-w-4xl mx-auto">
    <div class="flex flex-wrap items-center gap-3 mb-4">
      {rating_badge(ci['rating'], size='large')}
      <span class="text-sm text-gray-400">{country['name']}</span>
    </div>
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Is Tap Water Safe to Drink in {ci['name']}?</h1>
    <p class="text-lg text-gray-700 leading-relaxed mb-6">{ci['quick_answer']}</p>

    <div class="grid grid-cols-2 md:grid-cols-3 gap-3 mb-8">
      {info_card(ICON_DROP, 'Hardness', ci['hardness'].split(',')[0])}
      {info_card(ICON_MAP, 'Country', country['name'])}
      {info_card(ICON_PEOPLE, 'Rating', ci['rating'])}
    </div>

    <div class="space-y-6">
      {section_card('Water Source', f"<p>{ci['water_source']}</p>")}
      {section_card('Contaminants &amp; Concerns', f"<p>{ci['contaminants']}</p>")}
      {section_card('Tips', tips_html)}
      {faq_html}
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
    schemas.append({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": f"Is Tap Water Safe to Drink in {ci['name']}?",
        "description": ci["meta_description"],
        "url": f"{DOMAIN}/city/{slug}/",
        "publisher": {"@type": "Organization", "name": SITE, "url": DOMAIN},
    })
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

FEATURED_COUNTRIES = ["japan", "mexico", "italy", "thailand", "india", "spain", "france", "costa-rica", "greece", "vietnam", "morocco", "singapore"]
FEATURED_US = ["new-york-city", "chicago", "los-angeles", "san-francisco", "houston", "miami", "seattle", "las-vegas"]
FEATURED_WORLD = ["paris", "london", "rome", "tokyo", "bangkok", "bali", "dubai", "cancun"]


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
    }]
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
        sections += f"""<div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden mb-6">
          <div class="px-4 py-3 bg-gray-50 border-b border-gray-200"><h2 class="font-bold text-gray-900">{region}</h2></div>
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


build_best_tap_water()
build_worst_tap_water()
build_best_tap_water_us()
build_rankings_index()
print("Built rankings pages")

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
# SITEMAP & ROBOTS & MANIFEST
# ---------------------------------------------------------------------------

def build_sitemap():
    entries = []
    for path, priority, changefreq in ALL_PAGES:
        entries.append(f"""  <url>
    <loc>{DOMAIN}{path}</loc>
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
