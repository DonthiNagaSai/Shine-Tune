#!/usr/bin/env python3
"""Build index.html.

Concatenates src/shell.html (markup + CSS) and src/body.html (game logic),
inlines the Baloo 2 font subsets as base64 so the game works offline, and
wraps the result in a standalone HTML document.

The font package is not committed. Fetch it once with:

    mkdir -p src/font && cd src/font
    npm pack @fontsource-variable/baloo-2@5.3.0 && tar xzf *.tgz
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
FONT = SRC / "font" / "package"
SUBSETS = ("latin", "latin-ext", "devanagari")


def font_faces() -> str:
    """Return @font-face rules with each woff2 subset inlined as a data URI."""
    css = (FONT / "wght.css").read_text()
    pattern = r"/\*\s*baloo-2-([a-z-]+)-wght-normal\s*\*/\s*(@font-face\s*\{.*?\})"
    rules = []
    for name, block in re.findall(pattern, css, re.S):
        if name not in SUBSETS:
            continue
        data = (FONT / "files" / f"baloo-2-{name}-wght-normal.woff2").read_bytes()
        b64 = base64.b64encode(data).decode()
        rng = re.search(r"unicode-range:\s*([^;]+);", block).group(1)
        rules.append(
            "@font-face{font-family:'Baloo 2';font-style:normal;font-display:swap;"
            "font-weight:400 800;"
            f"src:url(data:font/woff2;base64,{b64}) format('woff2');"
            f"unicode-range:{rng}}}"
        )
    if len(rules) != len(SUBSETS):
        raise SystemExit(f"expected {len(SUBSETS)} font subsets, found {len(rules)}")
    return "\n".join(rules)


HEAD_EXTRA = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,user-scalable=no">
<meta name="theme-color" content="#b7dba0">
<meta name="description" content="One washer. One empty lot. Build the busiest plaza in town.">
<style>
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:light}
html,body{margin:0;height:100%}
img{max-width:100%}
[hidden]{display:none!important}
</style>"""


def main() -> None:
    shell = (SRC / "shell.html").read_text()
    body = (SRC / "body.html").read_text()

    cut = shell.index("</style>") + len("</style>")
    head, markup = shell[:cut], shell[cut:]
    head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">', "")

    page = markup + body
    if "/*FONTFACE*/" in head:
        head = head.replace("/*FONTFACE*/", font_faces())
    elif "/*FONTFACE*/" in page:
        page = page.replace("/*FONTFACE*/", font_faces())

    doc = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        f"{HEAD_EXTRA}\n{head.strip()}\n"
        "</head>\n<body>\n"
        f"{page.strip()}\n"
        "</body>\n</html>\n"
    )
    out = ROOT / "index.html"
    out.write_text(doc)
    print(f"wrote {out.relative_to(ROOT)} ({len(doc) // 1024} KB)")


if __name__ == "__main__":
    main()
