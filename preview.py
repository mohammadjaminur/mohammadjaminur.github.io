#!/usr/bin/env python3
"""Lightweight local preview for this Jekyll site (no Ruby required)."""

from __future__ import annotations

import http.server
import os
import re
import shutil
import socketserver
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / ".preview"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4000


def load_config(path: Path) -> dict[str, str]:
    cfg: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = line.split(":", 1)
        cfg[key.strip()] = val.strip().strip('"').strip("'")
    return cfg


def strip_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, parts[2].lstrip("\n")


def render_liquid(template: str, site: dict[str, str], page: dict[str, str], content: str = "") -> str:
    base = site.get("baseurl", "")

    def relative_url(path: str) -> str:
        path = path.strip().strip("'\"")
        if not path.startswith("/"):
            path = "/" + path
        return f"{base}{path}".replace("//", "/") if base else path

    out = template

    # {{ content }}
    out = out.replace("{{ content }}", content)

    # {{ '/path/' | relative_url }}
    out = re.sub(
        r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}",
        lambda m: relative_url(m.group(1)),
        out,
    )
    out = re.sub(
        r'\{\{\s*"([^"]+)"\s*\|\s*relative_url\s*\}\}',
        lambda m: relative_url(m.group(1)),
        out,
    )

    # {{ site.key }}
    out = re.sub(
        r"\{\{\s*site\.([a-zA-Z0-9_]+)\s*\}\}",
        lambda m: site.get(m.group(1), ""),
        out,
    )

    # {{ page.key }}
    out = re.sub(
        r"\{\{\s*page\.([a-zA-Z0-9_]+)\s*\}\}",
        lambda m: page.get(m.group(1), ""),
        out,
    )

    # Simple conditionals used in the layout
    # {% if page.title and page.title != "Home" %}...{% endif %}
    def title_block(match: re.Match[str]) -> str:
        title = page.get("title", "")
        return match.group(1) if title and title != "Home" else ""

    out = re.sub(
        r'\{%\s*if page\.title and page\.title != "Home"\s*%\}(.*?)\{%\s*endif\s*%\}',
        title_block,
        out,
        flags=re.S,
    )

    # {% if page.layout_class %}{{ page.layout_class }}{% endif %}
    out = re.sub(
        r"\{%\s*if page\.layout_class\s*%\}(.*?)\{%\s*endif\s*%\}",
        lambda m: render_liquid(m.group(1), site, page, content) if page.get("layout_class") else "",
        out,
        flags=re.S,
    )

    # aria-current conditionals: {% if page.url == '/' %}...{% endif %}
    page_url = page.get("url", "")
    out = re.sub(
        r"\{%\s*if page\.url == '/' \s*%\}(.*?)\{%\s*endif\s*%\}",
        lambda m: m.group(1) if page_url == "/" else "",
        out,
        flags=re.S,
    )
    out = re.sub(
        r"\{%\s*if page\.url contains '([^']+)'\s*%\}(.*?)\{%\s*endif\s*%\}",
        lambda m: m.group(2) if m.group(1) in page_url else "",
        out,
        flags=re.S,
    )

    # {{ page.description | default: site.description }}
    out = re.sub(
        r"\{\{\s*page\.description\s*\|\s*default:\s*site\.description\s*\}\}",
        page.get("description") or site.get("description", ""),
        out,
    )

    # Drop any leftover tags
    out = re.sub(r"\{%.*?%\}", "", out, flags=re.S)
    out = re.sub(r"\{\{.*?\}\}", "", out, flags=re.S)
    return out


def build() -> None:
    site = load_config(ROOT / "_config.yml")
    layout = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
    base = site.get("baseurl", "").rstrip("/")

    if OUT.exists():
        shutil.rmtree(OUT)
    out_root = OUT / base.lstrip("/") if base else OUT
    out_root.mkdir(parents=True, exist_ok=True)

    # Copy CSS
    shutil.copy2(ROOT / "style.css", out_root / "style.css")
    if (ROOT / "profile.jpg").exists():
        shutil.copy2(ROOT / "profile.jpg", out_root / "profile.jpg")

    pages = [
        ("index.md", "/", "index.html"),
        ("about.md", "/about/", "about/index.html"),
        ("research.md", "/research/", "research/index.html"),
        ("publications.md", "/publications/", "publications/index.html"),
        ("news.md", "/news/", "news/index.html"),
        ("teaching.md", "/teaching/", "teaching/index.html"),
    ]

    for src_name, url, dest_rel in pages:
        meta, body = strip_front_matter((ROOT / src_name).read_text(encoding="utf-8"))
        page = {
            "title": meta.get("title", ""),
            "description": meta.get("description", ""),
            "layout_class": meta.get("layout_class", ""),
            "url": url,
        }
        # Content itself may include liquid
        content = render_liquid(body, site, page)
        html = render_liquid(layout, site, page, content=content)
        dest = out_root / dest_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")

    # Convenience redirect at preview root when baseurl is set
    if base:
        (OUT / "index.html").write_text(
            f'<!DOCTYPE html><meta http-equiv="refresh" content="0; url={base}/">',
            encoding="utf-8",
        )


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(OUT), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        sys.stdout.write("%s - %s\n" % (self.address_string(), fmt % args))


def main() -> None:
    os.chdir(ROOT)
    build()
    base = load_config(ROOT / "_config.yml").get("baseurl", "")
    url = f"http://127.0.0.1:{PORT}{base}/"
    print(f"Preview built in {OUT}")
    print(f"Open: {url}")
    print("Press Ctrl+C to stop.")
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
