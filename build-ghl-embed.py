#!/usr/bin/env python3
"""
Bygger en embed-klar version af index.html til GHL's Custom HTML/Code-element.

Kør:  python3 build-ghl-embed.py
Ud:   ghl-embed.html  (indholdet indsættes i GHL's code-element)

Tre ting løses:
 1. Relative stier (assets/..., *.html) gøres absolutte, så de virker på GHL-domænet.
 2. Globale CSS-regler (*, body, html) scopes til #fx-site, så de ikke smitter
    af på GHL's egne elementer.
 3. Dokument-tags (<!DOCTYPE>, <html>, <head>, <body>) fjernes, da koden
    indsættes inde i en eksisterende side.
"""
import re

BASE = "https://majestic100.github.io/Farvexperten/"
SRC, OUT = "index.html", "ghl-embed.html"

html = open(SRC, encoding="utf-8").read()

style = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)

# --- 1. Absolutte stier ------------------------------------------------------
def absolutise(text):
    text = re.sub(r'((?:src|href)=")(assets/)', r"\1" + BASE + r"\2", text)
    text = re.sub(r"(url\(')(assets/)", r"\1" + BASE + r"\2", text)
    text = re.sub(r'(href=")((?:privatlivs|cookie)politik\.html)', r"\1" + BASE + r"\2", text)
    return text

style, body = absolutise(style), absolutise(body)

# --- 2. Scope globale regler -------------------------------------------------
# VIGTIGT: der scopes med :where(), som har NUL specificitet. Bruger man
# '#fx-site *', får resetten ID-specificitet og overtrumfer alle klasseregler
# (.wrap, .svc ...), så layoutet falder fra hinanden.
SCOPE = ":where(#fx-site)"
# '*{...}' -> ':where(#fx-site) *,:where(#fx-site){...}'
style = re.sub(r"(^|\})\s*\*\{", r"\1" + SCOPE + " *," + SCOPE + "{", style, count=1)
# 'body{...}' -> ':where(#fx-site){...}'
style = re.sub(r"(^|\})\s*body\{", r"\1" + SCOPE + "{", style)
# html-reglen kan ikke scopes; scroll-behavior beholdes globalt (harmløs)
style = re.sub(r"(^|\})\s*html\{[^}]*\}", r"\1", style, count=1)

wrapper_css = (
    SCOPE + "{font-family:'Roboto',system-ui,-apple-system,Segoe UI,Arial,sans-serif;"
    "font-weight:400;color:#25282B;background:#fff;line-height:1.65;"
    "-webkit-font-smoothing:antialiased;overflow-x:hidden}\n"
    "html{scroll-behavior:smooth;scroll-padding-top:88px}\n"
)

out = f"""<!-- Farve X-perten landingsside - genereret af build-ghl-embed.py -->
<!-- Indsaet ALT herunder i GHL's Custom HTML/Code-element. -->
<link href="{BASE}assets/fonts/fonts.css" rel="stylesheet">
<style>
{wrapper_css}{style}
</style>
<div id="fx-site">
{body}
</div>
"""

open(OUT, "w", encoding="utf-8").write(out)
print(f"Skrev {OUT} ({len(out)//1024} KB)")
