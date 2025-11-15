#!/usr/bin/env python3
"""Generate a consolidated publications markdown file from _publications front matter.

Parses each Markdown file in _publications, extracts common keys, and outputs a
sorted (newest first) publications_compiled.md file.

No external dependencies; naive YAML front matter parsing sufficient for simple key: value pairs.
"""
import os
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB_DIR = ROOT / "_publications"
OUT_FILE = ROOT / "publications_compiled.md"

FRONT_MATTER_BOUNDARY = re.compile(r'^---\s*$')
KEY_VALUE_RE = re.compile(r'^(?P<key>[A-Za-z0-9_]+):\s*(?P<val>.*)$')
MULTILINE_KEYS = {"abstract"}

class Publication:
    def __init__(self, meta, body):
        self.meta = meta
        self.body = body
        # Normalize keys
        self.title = meta.get("title", "Untitled").strip().strip('"')
        self.authors = meta.get("authors", "").strip('"')
        self.venue = meta.get("venue", "").strip('"')
        self.date_raw = meta.get("date", "1900-01-01").strip()
        self.paperurl = meta.get("paperurl")
        self.arxiv = meta.get("arxiv")
        self.pdfurl = meta.get("pdfurl")
        self.selected = str(meta.get("selected", "false")).lower() == "true"
        self.abstract = meta.get("abstract", "").strip()
        self.year = self._extract_year(self.date_raw)
        self.date = self._parse_date(self.date_raw)

    def _extract_year(self, date_str):
        m = re.match(r'^(\d{4})', date_str)
        return m.group(1) if m else "????"

    def _parse_date(self, date_str):
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except Exception:
            return datetime.datetime(1900,1,1)

    def primary_link(self):
        return self.paperurl or self.arxiv or self.pdfurl

    def link_label(self):
        if self.paperurl and "proceedings" in self.paperurl:
            # attempt short label
            if "mlr.press" in self.paperurl:
                return "proceedings"
        if self.arxiv:
            return "arxiv"
        if self.pdfurl:
            return "pdf"
        return "link"

    def to_markdown_block(self):
        lines = []
        title_line = f"**{self.title}**"
        if self.primary_link():
            title_line = f"**[{self.title}]({self.primary_link()})**"
        # Selected marker
        if self.selected:
            title_line += "  _(selected)_"
        lines.append(title_line)
        if self.authors:
            lines.append(f"*Authors:* {self.authors}")
        if self.venue:
            lines.append(f"*Venue:* {self.venue}")
        lines.append(f"*Year:* {self.year}")
        if self.paperurl and self.arxiv and self.paperurl != self.arxiv:
            lines.append(f"*Links:* [proceedings]({self.paperurl}) · [arxiv]({self.arxiv})")
        elif self.arxiv and not self.paperurl:
            lines.append(f"*Link:* [arxiv]({self.arxiv})")
        elif self.paperurl and not self.arxiv:
            lines.append(f"*Link:* [proceedings]({self.paperurl})")
        elif self.pdfurl and not (self.paperurl or self.arxiv):
            lines.append(f"*Link:* [pdf]({self.pdfurl})")
        if self.abstract:
            # Collapse abstract into single paragraph (remove internal newlines)
            abstract_clean = re.sub(r'\s*\n\s*', ' ', self.abstract).strip()
            lines.append(f"<details><summary>Abstract</summary><div>{abstract_clean}</div></details>")
        return '\n'.join(lines)


def parse_publication(path: Path) -> Publication:
    with path.open('r', encoding='utf-8') as f:
        lines = f.readlines()
    # Extract front matter
    meta = {}
    body_lines = []
    in_front = False
    front_done = False
    current_multiline_key = None
    multiline_buffer = []
    for line in lines:
        if not in_front and FRONT_MATTER_BOUNDARY.match(line):
            in_front = True
            continue
        if in_front and FRONT_MATTER_BOUNDARY.match(line):
            # end front matter
            in_front = False
            front_done = True
            if current_multiline_key:
                meta[current_multiline_key] = '\n'.join(multiline_buffer)
                current_multiline_key = None
                multiline_buffer = []
            continue
        if in_front:
            # multiline abstract support
            if current_multiline_key:
                if line.startswith(' ') or line.startswith('\t'):
                    multiline_buffer.append(line.rstrip())
                    continue
                else:
                    # end multiline block
                    meta[current_multiline_key] = '\n'.join(multiline_buffer)
                    current_multiline_key = None
                    multiline_buffer = []
            m = KEY_VALUE_RE.match(line.rstrip())
            if m:
                key = m.group('key').strip()
                val = m.group('val').strip()
                if key in MULTILINE_KEYS and val == '|':
                    current_multiline_key = key
                    multiline_buffer = []
                else:
                    meta[key] = val
            continue
        if front_done:
            body_lines.append(line.rstrip())
    return Publication(meta, '\n'.join(body_lines))


def main():
    publications = []
    for md in sorted(PUB_DIR.glob('*.md')):
        try:
            pub = parse_publication(md)
            publications.append(pub)
        except Exception as e:
            print(f"Warning: failed parsing {md}: {e}")
    # Sort newest first by date
    publications.sort(key=lambda p: p.date, reverse=True)
    # Build markdown
    out_lines = ["# Publications", "", f"Generated on {datetime.datetime.utcnow().isoformat()} UTC", ""]
    for pub in publications:
        out_lines.append(pub.to_markdown_block())
        out_lines.append("")
        out_lines.append("---")
        out_lines.append("")
    OUT_FILE.write_text('\n'.join(out_lines), encoding='utf-8')
    print(f"Wrote {OUT_FILE} with {len(publications)} entries.")

if __name__ == '__main__':
    main()
