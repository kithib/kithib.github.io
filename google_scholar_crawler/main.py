import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


SCHOLAR_ID = os.environ["GOOGLE_SCHOLAR_ID"].strip()
EXPECTED_NAME = os.environ.get("GOOGLE_SCHOLAR_NAME", "Chenxing Wei").strip()
SCHOLAR_URL = "https://scholar.google.com/citations?" + urllib.parse.urlencode(
    {"user": SCHOLAR_ID, "hl": "en", "pagesize": "100"}
)


def parse_number(value):
    normalized = value.replace(",", "").strip()
    return int(normalized) if normalized.isdigit() else None


class ScholarProfileParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta_description = ""
        self.profile_name = ""
        self.metric_cells = []
        self.publications = []
        self._in_profile_name = False
        self._in_metric_cell = False
        self._in_publication_row = False
        self._in_publication_title = False
        self._in_publication_citations = False
        self._in_publication_year = False
        self._current_publication = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = set(attributes.get("class", "").split())

        if tag == "meta" and attributes.get("name") == "description":
            self.meta_description = attributes.get("content", "")

        if tag == "div" and attributes.get("id") == "gsc_prf_in":
            self._in_profile_name = True

        if tag == "td" and "gsc_rsb_std" in classes:
            self._in_metric_cell = True

        if tag == "tr" and "gsc_a_tr" in classes:
            self._in_publication_row = True
            self._current_publication = {
                "bib": {"title": "", "pub_year": ""},
                "num_citations": 0,
                "author_pub_id": "",
            }

        if self._in_publication_row and tag == "a" and "gsc_a_at" in classes:
            self._in_publication_title = True
            match = re.search(
                r"citation_for_view=([^&]+)", attributes.get("href", "")
            )
            if match:
                self._current_publication["author_pub_id"] = urllib.parse.unquote(
                    match.group(1)
                )

        if self._in_publication_row and tag == "a" and "gsc_a_ac" in classes:
            self._in_publication_citations = True

        if self._in_publication_row and tag == "span" and "gsc_a_h" in classes:
            self._in_publication_year = True

    def handle_endtag(self, tag):
        if tag == "div":
            self._in_profile_name = False
        if tag == "td":
            self._in_metric_cell = False
        if tag == "a":
            self._in_publication_title = False
            self._in_publication_citations = False
        if tag == "span":
            self._in_publication_year = False
        if tag == "tr" and self._in_publication_row:
            title = self._current_publication["bib"]["title"].strip()
            if title:
                self._current_publication["bib"]["title"] = title
                self.publications.append(self._current_publication)
            self._current_publication = None
            self._in_publication_row = False

    def handle_data(self, data):
        text = html.unescape(data).strip()
        if not text:
            return

        if self._in_profile_name:
            self.profile_name += text
        if self._in_metric_cell:
            self.metric_cells.append(text)
        if self._current_publication is not None and self._in_publication_title:
            self._current_publication["bib"]["title"] += text
        if self._current_publication is not None and self._in_publication_citations:
            citation_count = parse_number(text)
            if citation_count is not None:
                self._current_publication["num_citations"] = citation_count
        if self._current_publication is not None and self._in_publication_year:
            self._current_publication["bib"]["pub_year"] = text


def fetch_profile_html():
    request = urllib.request.Request(
        SCHOLAR_URL,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_metrics(parser):
    metrics = [
        number
        for cell in parser.metric_cells
        if (number := parse_number(cell)) is not None
    ]
    if len(metrics) < 6:
        fallback = re.search(r"Cited by\s+([0-9,]+)", parser.meta_description)
        if fallback:
            citedby = int(fallback.group(1).replace(",", ""))
            if not metrics or metrics[0] != citedby:
                metrics.insert(0, citedby)
    if len(metrics) < 6:
        raise RuntimeError("Could not parse all Google Scholar metrics.")
    return {
        "citedby": metrics[0],
        "citedby5y": metrics[1],
        "hindex": metrics[2],
        "hindex5y": metrics[3],
        "i10index": metrics[4],
        "i10index5y": metrics[5],
    }


def main():
    parser = ScholarProfileParser()
    parser.feed(fetch_profile_html())

    profile_name = parser.profile_name.strip()
    if EXPECTED_NAME and profile_name.casefold() != EXPECTED_NAME.casefold():
        raise RuntimeError(
            f"Scholar profile mismatch: expected {EXPECTED_NAME!r}, got {profile_name!r}."
        )
    if not parser.publications:
        raise RuntimeError("No Google Scholar publications were found.")

    author = {
        "scholar_id": SCHOLAR_ID,
        "name": profile_name,
        "source": SCHOLAR_URL,
        "updated": datetime.now(timezone.utc).isoformat(),
        "publications": {
            publication["author_pub_id"]: publication
            for publication in parser.publications
            if publication["author_pub_id"]
        },
        **parse_metrics(parser),
    }

    results_dir = Path(os.environ.get("RESULTS_DIR", "results"))
    results_dir.mkdir(parents=True, exist_ok=True)
    (results_dir / "gs_data.json").write_text(
        json.dumps(author, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (results_dir / "gs_data_shieldsio.json").write_text(
        json.dumps(
            {
                "schemaVersion": 1,
                "label": "citations",
                "message": str(author["citedby"]),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "scholar_id": author["scholar_id"],
                "name": author["name"],
                "citedby": author["citedby"],
                "updated": author["updated"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Google Scholar crawler failed: {error}", file=sys.stderr)
        raise
