# -*- coding: utf-8 -*-
"""Shared HTML building blocks for TapWaterGuide.org"""
import json

SITE = "TapWaterGuide"
DOMAIN = "https://tapwaterguide.org"
GA_MEASUREMENT_ID = "G-FS0BXPE79Z"

# Content dates for E-E-A-T signals. Bump LAST_REVIEWED whenever content data is updated.
DATE_PUBLISHED = "2026-08-28"
LAST_REVIEWED = "2026-08-31"
LAST_REVIEWED_DISPLAY = "August 31, 2026"

ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": SITE,
    "url": DOMAIN,
    "logo": f"{DOMAIN}/assets/android-chrome-512x512.png",
    "email": "info@tapwaterguide.org",
    "description": "The worldwide reference for tap water safety, built on WHO, EPA, EWG, and CDC guidance.",
}

RATING_STYLE = {
    "Safe": {
        "badge": "bg-emerald-50 text-emerald-700 border-emerald-200",
        "bar": "bg-emerald-500",
        "text": "text-emerald-700",
        "solid": "bg-emerald-600",
        "hero": "from-emerald-50",
        "icon": "check",
    },
    "Generally Safe": {
        "badge": "bg-sky-50 text-sky-700 border-sky-200",
        "bar": "bg-sky-500",
        "text": "text-sky-700",
        "solid": "bg-sky-600",
        "hero": "from-sky-50",
        "icon": "check",
    },
    "Caution": {
        "badge": "bg-amber-50 text-amber-700 border-amber-200",
        "bar": "bg-amber-500",
        "text": "text-amber-700",
        "solid": "bg-amber-600",
        "hero": "from-amber-50",
        "icon": "alert",
    },
    "Not Safe": {
        "badge": "bg-red-50 text-red-700 border-red-200",
        "bar": "bg-red-500",
        "text": "text-red-700",
        "solid": "bg-red-600",
        "hero": "from-red-50",
        "icon": "x",
    },
}

ICONS = {
    "check": '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>',
    "alert": '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v3.75m0 3.75h.008v.008H12v-.008zM10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L14.71 3.86a2 2 0 00-3.42 0z"/></svg>',
    "x": '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"/></svg>',
    "droplet": '<svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>',
    "search": '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M17 10a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>',
    "chevron": '<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>',
    "pin": '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a2 2 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>',
}


def rating_badge(rating, size="normal"):
    s = RATING_STYLE[rating]
    pad = "px-3 py-1 text-sm" if size == "normal" else "px-5 py-2 text-lg shadow-sm"
    return (
        f'<span class="inline-flex items-center gap-1.5 rounded-full border {pad} font-semibold {s["badge"]}">'
        f'{ICONS[s["icon"]]}{rating}</span>'
    )


def nav(active=""):
    items = [
        ("Home", "/", "home"),
        ("Map", "/map/", "map"),
        ("Countries", "/country/", "countries"),
        ("US Cities", "/rankings/best-tap-water-us/", "us"),
        ("US Water", "/us-water-quality/", "uswater"),
        ("World Cities", "/city/", "world"),
        ("Rankings", "/rankings/", "rankings"),
        ("Hardness", "/water-hardness/", "hardness"),
        ("Guides", "/guides/", "guides"),
    ]

    def cls(key):
        base = "text-gray-600 hover:text-sky-700"
        return f"text-sky-700 font-semibold" if key == active else base

    desktop = "\n".join(
        f'<a href="{href}" class="{cls(key)}">{label}</a>' for label, href, key in items
    )
    mobile = "\n".join(
        f'<a href="{href}" class="block py-2 text-gray-700 font-medium">{label}</a>'
        for label, href, key in items
    )
    return f"""<header class="bg-white border-b border-gray-200 sticky top-0 z-50">
  <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
    <a href="/" class="flex items-center gap-2">
      <div class="w-10 h-10 bg-sky-600 rounded-xl flex items-center justify-center">
        {ICONS['droplet']}
      </div>
      <div>
        <div class="font-bold text-gray-900 leading-tight">TapWaterGuide</div>
        <div class="text-xs text-gray-500 leading-tight">Worldwide water safety reference</div>
      </div>
    </a>
    <nav class="hidden md:flex items-center gap-6 text-sm">
      {desktop}
      <div class="relative">
        <input id="navSearch" type="text" placeholder="Search&hellip;" autocomplete="off"
          class="w-40 lg:w-56 bg-gray-50 border border-gray-200 rounded-full px-4 py-1.5 text-sm outline-none focus:border-sky-400 focus:bg-white transition-colors">
        <div id="navSearchResults" class="hidden absolute right-0 top-full mt-2 w-72 bg-white rounded-xl shadow-xl border border-gray-200 overflow-hidden z-50 text-left"></div>
      </div>
    </nav>
    <button onclick="document.getElementById('mobileMenu').classList.toggle('hidden')" class="md:hidden p-2" aria-label="Menu">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
    </button>
  </div>
  <div id="mobileMenu" class="hidden md:hidden border-t border-gray-200 bg-white">
    <div class="px-4 py-3 space-y-1">
      <div class="relative pb-2">
        <input id="navSearchMobile" type="text" placeholder="Search a country or city&hellip;" autocomplete="off"
          class="w-full bg-gray-50 border border-gray-200 rounded-full px-4 py-2 text-sm outline-none focus:border-sky-400">
        <div id="navSearchMobileResults" class="hidden bg-white rounded-xl border border-gray-200 overflow-hidden mt-2"></div>
      </div>
      {mobile}
    </div>
  </div>
</header>"""


NAV_SEARCH_SCRIPT = """<script>
(function(){
  var idx = null, loading = false;
  function ensureIndex(cb){
    if (idx) { cb(); return; }
    if (loading) return;
    loading = true;
    fetch('/search-index.json').then(function(r){ return r.json(); }).then(function(d){ idx = d; cb(); }).catch(function(){ loading = false; });
  }
  var typeLabel = {country:'Country','us-city':'US City','world-city':'World City','us-state':'US State'};
  function wire(inputId, resultsId){
    var input = document.getElementById(inputId);
    var results = document.getElementById(resultsId);
    if (!input || !results) return;
    function render(){
      var q = input.value.trim().toLowerCase();
      if (!q) { results.classList.add('hidden'); results.innerHTML=''; return; }
      if (!idx) { ensureIndex(render); return; }
      var m = idx.filter(function(e){ return e.name.toLowerCase().indexOf(q) !== -1; }).slice(0, 8);
      results.innerHTML = m.length ? m.map(function(e){
        var meta = typeLabel[e.type] + (e.hardness ? ' &middot; ' + e.hardness + ' water' : '');
        return '<a href="'+e.href+'" class="flex items-center justify-between px-4 py-2.5 hover:bg-sky-50 border-b border-gray-100 last:border-0 text-sm">'+
          '<span class="text-gray-900">'+e.name+'</span>'+
          '<span class="text-xs text-gray-400">'+meta+'</span></a>';
      }).join('') : '<div class="px-4 py-3 text-sm text-gray-500">No matches</div>';
      results.classList.remove('hidden');
    }
    input.addEventListener('focus', function(){ ensureIndex(function(){}); });
    input.addEventListener('input', render);
  }
  wire('navSearch','navSearchResults');
  wire('navSearchMobile','navSearchMobileResults');
  document.addEventListener('click', function(ev){
    ['navSearchResults','navSearchMobileResults'].forEach(function(id){
      var el = document.getElementById(id);
      if (el && !ev.target.closest('#'+id) && !ev.target.closest('input')) el.classList.add('hidden');
    });
  });
})();
</script>"""


def footer():
    return f"""<footer class="bg-gray-900 text-gray-400 px-4 py-10 mt-16">
  <div class="max-w-7xl mx-auto">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-8 mb-8">
      <div>
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 bg-sky-600 rounded-lg flex items-center justify-center">
            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>
          </div>
          <span class="text-white font-bold">TapWaterGuide</span>
        </div>
        <p class="text-sm">The worldwide reference for tap water safety, quality, and drinkability &mdash; built on WHO, EPA, EWG and CDC data.</p>
      </div>
      <div>
        <h4 class="text-white font-medium mb-3">Explore</h4>
        <div class="space-y-1 text-sm">
          <a href="/map/" class="block hover:text-white">World Safety Map</a>
          <a href="/us-water-quality/" class="block hover:text-white">US Water Quality by ZIP</a>
          <a href="/country/" class="block hover:text-white">All Countries</a>
          <a href="/city/" class="block hover:text-white">All Cities</a>
          <a href="/water-hardness/by-city/" class="block hover:text-white">Water Hardness by City</a>
          <a href="/guides/" class="block hover:text-white">Guides</a>
          <a href="/rankings/best-tap-water/" class="block hover:text-white">Best Tap Water Worldwide</a>
          <a href="/rankings/worst-tap-water/" class="block hover:text-white">Countries to Avoid</a>
          <a href="/rankings/best-tap-water-us/" class="block hover:text-white">Best US City Water</a>
          <a href="/rankings/best-tap-water-cities/" class="block hover:text-white">Best Tap Water Cities</a>
        </div>
      </div>
      <div>
        <h4 class="text-white font-medium mb-3">Popular Countries</h4>
        <div class="space-y-1 text-sm">
          <a href="/country/japan/" class="block hover:text-white">Japan</a>
          <a href="/country/mexico/" class="block hover:text-white">Mexico</a>
          <a href="/country/italy/" class="block hover:text-white">Italy</a>
          <a href="/country/thailand/" class="block hover:text-white">Thailand</a>
          <a href="/country/india/" class="block hover:text-white">India</a>
        </div>
      </div>
      <div>
        <h4 class="text-white font-medium mb-3">Site</h4>
        <div class="space-y-1 text-sm">
          <a href="/about/" class="block hover:text-white">About &amp; Data Sources</a>
          <a href="/about/#sources" class="block hover:text-white">Methodology</a>
          <a href="/privacy/" class="block hover:text-white">Privacy Policy</a>
          <a href="/sitemap.xml" class="block hover:text-white">Sitemap</a>
        </div>
      </div>
    </div>
    <div class="border-t border-gray-800 pt-6 text-sm text-center">
      <p>&copy; 2026 TapWaterGuide.org &mdash; Worldwide Tap Water Safety Reference</p>
      <p class="mt-1 text-gray-500">Informational reference only, not medical advice. Water quality changes over time &mdash; always check current local advisories before travel.</p>
    </div>
  </div>
</footer>"""


def breadcrumbs(items):
    """items: list of (label, href_or_None)"""
    parts = []
    ld_items = []
    for i, (label, href) in enumerate(items):
        pos = i + 1
        if href:
            parts.append(f'<a href="{href}" class="hover:text-sky-700">{label}</a>')
        else:
            parts.append(f'<span class="text-gray-500" aria-current="page">{label}</span>')
        ld_items.append({
            "@type": "ListItem",
            "position": pos,
            "name": label,
            "item": (DOMAIN + href) if href else None,
        })
    for it in ld_items:
        if it["item"] is None:
            it.pop("item")
    sep = '<svg class="w-3 h-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>'
    html = f'<nav class="flex items-center gap-2 text-sm flex-wrap" aria-label="Breadcrumb">' + f' {sep} '.join(parts) + '</nav>'
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld_items}
    return html, ld


def faq_block(faqs, heading="Frequently Asked Questions"):
    if not faqs:
        return "", None
    items = []
    ld_entities = []
    for i, (q, a) in enumerate(faqs):
        oid = f"faq-{i}"
        items.append(f"""<div class="border-b border-gray-100 last:border-0">
          <button type="button" class="faq-toggle w-full flex items-center justify-between gap-4 text-left py-4" aria-expanded="false" aria-controls="{oid}">
            <span class="font-semibold text-gray-900">{q}</span>
            <svg class="w-5 h-5 text-sky-600 flex-shrink-0 faq-chevron transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div id="{oid}" class="faq-panel hidden pb-4 text-gray-600 leading-relaxed">{a}</div>
        </div>""")
        ld_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        })
    html = f"""<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 class="text-xl font-bold text-gray-900 mb-2">{heading}</h2>
      <div>{''.join(items)}</div>
    </div>"""
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ld_entities}
    return html, ld


FAQ_SCRIPT = """<script>
document.querySelectorAll('.faq-toggle').forEach(function(btn){
  btn.addEventListener('click', function(){
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', open ? 'false' : 'true');
    panel.classList.toggle('hidden');
    var chevron = btn.querySelector('.faq-chevron');
    if (chevron) chevron.classList.toggle('rotate-180');
  });
});
</script>"""


def stat_pill(label, value):
    return f"""<div class="bg-white rounded-lg border border-gray-200 px-4 py-3 text-center">
      <div class="text-lg font-bold text-sky-700">{value}</div>
      <div class="text-xs text-gray-500">{label}</div>
    </div>"""


def page(title, description, path, body, extra_head="", schemas=None, active_nav="", og_type="website"):
    """path like '/country/japan/' (must start and end with /, or '' for home)"""
    canonical = DOMAIN + path
    schemas = schemas or []
    schema_scripts = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA_MEASUREMENT_ID}');</script>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/assets/site.webmanifest">
<meta name="theme-color" content="#0284c7">
<link rel="stylesheet" href="/assets/style.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>*{{font-family:'Inter',sans-serif}}body{{background:#f8fafc}}</style>
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="TapWaterGuide">
<meta property="og:image" content="{DOMAIN}/assets/og-default.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{DOMAIN}/assets/og-default.png">
{extra_head}
{schema_scripts}
</head>
<body class="text-gray-700 min-h-screen flex flex-col">
{nav(active_nav)}
<main class="flex-1">
{body}
</main>
{footer()}
{FAQ_SCRIPT}
{NAV_SEARCH_SCRIPT}
</body>
</html>"""
