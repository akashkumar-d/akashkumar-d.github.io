#!/usr/bin/env python3
"""Minimal PDF generator for publications list.

Creates a very simple text PDF (Helvetica) listing all publications in newest-first order.
No external dependencies; emits raw PDF objects.
"""
import re, datetime, pathlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB_DIR = ROOT / "_publications"
OUT_PDF = ROOT / "publications.pdf"

FRONT_BOUND = re.compile(r'^---\s*$')
KEY_RE = re.compile(r'^(?P<k>[A-Za-z0-9_]+):\s*(?P<v>.*)$')
MULTILINE_KEYS = {"abstract"}

def parse(pub_path: Path):
    lines = pub_path.read_text(encoding='utf-8').splitlines()
    meta = {}
    in_front = False
    current_key = None
    buf = []
    for line in lines:
        if not in_front and FRONT_BOUND.match(line):
            in_front = True
            continue
        if in_front and FRONT_BOUND.match(line):
            in_front = False
            if current_key:
                meta[current_key] = '\n'.join(buf)
                current_key = None
                buf = []
            break
        if in_front:
            if current_key:
                if line.startswith(' ') or line.startswith('\t'):
                    buf.append(line.strip())
                    continue
                else:
                    meta[current_key] = '\n'.join(buf)
                    current_key = None
                    buf = []
            m = KEY_RE.match(line)
            if m:
                k,v = m.group('k'), m.group('v').strip()
                if k in MULTILINE_KEYS and v == '|':
                    current_key = k
                    buf = []
                else:
                    meta[k] = v
    # basic fields
    title = meta.get('title','Untitled').strip('"')
    authors = meta.get('authors','').strip('"')
    venue = meta.get('venue','').strip('"')
    date = meta.get('date','1900-01-01')
    abstract = meta.get('abstract','').strip()
    paperurl = meta.get('paperurl')
    arxiv = meta.get('arxiv')
    selected = str(meta.get('selected','false')).lower()=='true'
    return {
        'title': title,
        'authors': authors,
        'venue': venue,
        'date': date,
        'abstract': abstract,
        'paperurl': paperurl,
        'arxiv': arxiv,
        'selected': selected,
    }

def escape_pdf_text(s: str) -> str:
    return s.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')

def build_lines(pub):
    lines = []
    title = pub['title'] + (' [selected]' if pub['selected'] else '')
    lines.append(title)
    if pub['authors']:
        lines.append(f"Authors: {pub['authors']}")
    if pub['venue']:
        lines.append(f"Venue: {pub['venue']}")
    lines.append(f"Date: {pub['date']}")
    if pub['paperurl'] or pub['arxiv']:
        link_parts = []
        if pub['paperurl']:
            link_parts.append(f"proceedings: {pub['paperurl']}")
        if pub['arxiv']:
            link_parts.append(f"arxiv: {pub['arxiv']}")
        lines.append("Links: " + ' | '.join(link_parts))
    if pub['abstract']:
        # compress whitespace for PDF brevity
        abstract = re.sub(r'\s+',' ', pub['abstract']).strip()
        lines.append("Abstract: " + abstract[:600])  # truncate long abstracts
    return lines

def paginate(lines, max_lines_per_page=55):
    pages = []
    page = []
    for line in lines:
        if len(page) >= max_lines_per_page:
            pages.append(page)
            page = []
        page.append(line)
    if page:
        pages.append(page)
    return pages

def generate_pdf(pages):
    objects = []
    # Font object id 5
    # Build page content streams
    content_ids = []
    y_start = 760
    line_height = 12
    for p_i, page in enumerate(pages):
        text_ops = ["BT /F1 11 Tf"]
        y = y_start
        for line in page:
            esc = escape_pdf_text(line)
            text_ops.append(f"1 0 0 1 50 {y} Tm ({esc}) Tj")
            y -= line_height
            if y < 40:
                break
        text_ops.append("ET")
        stream = '\n'.join(text_ops).encode('utf-8')
        obj_id = 10 + p_i
        objects.append((obj_id, f"<< /Length {len(stream)} >>", stream))
        content_ids.append(obj_id)
    # Page objects
    page_ids = []
    for idx, cid in enumerate(content_ids):
        pid = cid + 50
        page_ids.append(pid)
        objects.append((pid, f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 5 0 R >> >> /Contents {cid} 0 R >>", b""))
    # Catalog, Pages, Font
    objects.insert(0, (1, "<< /Type /Catalog /Pages 2 0 R >>", b""))
    kids = ' '.join(f"{pid} 0 R" for pid in page_ids)
    objects.insert(1, (2, f"<< /Type /Pages /Kids [ {kids} ] /Count {len(page_ids)} >>", b""))
    objects.insert(2, (5, "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>", b""))
    # Build xref
    pdf_parts = [b"%PDF-1.4\n"]
    offsets = []
    for obj_id, header, stream in objects:
        offsets.append(sum(len(part) for part in pdf_parts))
        pdf_parts.append(f"{obj_id} 0 obj\n{header}\n".encode('utf-8'))
        if stream:
            pdf_parts.append(b"stream\n")
            pdf_parts.append(stream)
            pdf_parts.append(b"\nendstream\n")
        pdf_parts.append(b"endobj\n")
    xref_start = sum(len(p) for p in pdf_parts)
    pdf_parts.append(f"xref\n0 {max(obj[0] for obj in objects)+1}\n".encode('utf-8'))
    # object 0 placeholder
    pdf_parts.append(b"0000000000 65535 f \n")
    for i, obj in enumerate(objects, start=1):
        off = offsets[i-1]
        pdf_parts.append(f"{off:010d} 00000 n \n".encode('utf-8'))
    pdf_parts.append(b"trailer\n")
    size = max(obj[0] for obj in objects)+1
    pdf_parts.append(f"<< /Size {size} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF".encode('utf-8'))
    OUT_PDF.write_bytes(b''.join(pdf_parts))


def main():
    pubs = [parse(p) for p in PUB_DIR.glob('*.md')]
    # sort newest first by date
    def parse_date(d):
        try:
            return datetime.datetime.strptime(d, '%Y-%m-%d')
        except Exception:
            return datetime.datetime(1900,1,1)
    pubs.sort(key=lambda x: parse_date(x['date']), reverse=True)
    all_lines = ["Publications (Generated: " + datetime.datetime.utcnow().isoformat() + ' UTC)']
    for pub in pubs:
        all_lines.append("")
        all_lines.extend(build_lines(pub))
    pages = paginate(all_lines)
    generate_pdf(pages)
    print(f"Created {OUT_PDF} with {len(pages)} page(s).")

if __name__ == '__main__':
    main()
