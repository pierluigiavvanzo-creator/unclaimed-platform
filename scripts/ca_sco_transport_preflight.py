#!/usr/bin/env python3
"""Execute one bounded metadata-only transport preflight.

The script discovers a named download link from an official source page, then issues
HEAD requests only to HTTPS endpoints whose hosts are explicitly allowlisted. It
never reads, persists, or parses a download response body.
"""

from __future__ import annotations

import argparse
import http.client
import json
import ssl
import sys
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

USER_AGENT = "unclaimed-platform-transport-preflight/1.0 metadata-only body-zero"
SAFE_RESPONSE_HEADERS = {
    "accept-ranges",
    "cache-control",
    "content-length",
    "content-type",
    "etag",
    "last-modified",
    "location",
}


class _AnchorCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._href: str | None = None
        self._text_parts: list[str] = []
        self.anchors: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attributes = dict(attrs)
        href = attributes.get("href")
        if href:
            self._href = href
            self._text_parts = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href is not None:
            text = " ".join("".join(self._text_parts).split())
            self.anchors.append((text, self._href))
            self._href = None
            self._text_parts = []


def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def _validate_https_allowlisted(url: str, allowlisted_hosts: set[str]) -> tuple[str, str]:
    parsed = urlparse(url)
    if parsed.scheme.lower() != "https":
        raise ValueError(f"non-HTTPS endpoint blocked: {url}")
    host = (parsed.hostname or "").lower()
    if host not in allowlisted_hosts:
        raise ValueError(f"host not allowlisted: {host or '<missing>'}")
    path = parsed.path or "/"
    if parsed.query:
        path += f"?{parsed.query}"
    return host, path


def discover_endpoint(
    official_source_page: str,
    link_label: str,
    timeout_seconds: int,
    allowlisted_hosts: set[str],
) -> tuple[str, str]:
    request = Request(official_source_page, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout_seconds) as response:  # noqa: S310 - fixed HTTPS source
        html = response.read().decode("utf-8", errors="replace")

    parser = _AnchorCollector()
    parser.feed(html)
    matches = [href for text, href in parser.anchors if text.strip() == link_label]
    if len(matches) != 1:
        raise RuntimeError(
            f"expected exactly one anchor labelled {link_label!r}; found {len(matches)}"
        )

    endpoint = urljoin(official_source_page, matches[0])
    host, _ = _validate_https_allowlisted(endpoint, allowlisted_hosts)
    return endpoint, host


def _head_once(
    url: str,
    timeout_seconds: int,
    allowlisted_hosts: set[str],
) -> tuple[int, dict[str, str]]:
    host, path = _validate_https_allowlisted(url, allowlisted_hosts)
    context = ssl.create_default_context()
    connection = http.client.HTTPSConnection(host, timeout=timeout_seconds, context=context)
    try:
        connection.request(
            "HEAD",
            path,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "*/*",
                "Connection": "close",
            },
        )
        response = connection.getresponse()
        headers = {
            key.lower(): value
            for key, value in response.getheaders()
            if key.lower() in SAFE_RESPONSE_HEADERS
        }
        # Deliberately do not call response.read(). The preflight consumes zero body bytes.
        return response.status, headers
    finally:
        connection.close()


def _base_result(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "execution_id": "ca.sco.unclaimed_property.bulk.transport_preflight.execution.2026-09-14",
        "source_id": "ca.sco.unclaimed_property.bulk",
        "jurisdiction": "CA",
        "execution_approval_ref": args.approval_ref,
        "official_source_page": args.official_source_page,
        "target_link_label": args.link_label,
        "controls": {
            "https_only": True,
            "request_method": "HEAD",
            "timeout_seconds": args.timeout_seconds,
            "max_redirects": args.max_redirects,
            "allowlisted_hosts": sorted(args.allow_host),
            "response_body_bytes_allowed": 0,
            "persist_response_body": False,
            "parse_response_body": False,
            "persist_dataset_artifact": False,
            "pii_processing_allowed": False,
            "beneficiary_matching_allowed": False,
            "outreach_allowed": False,
        },
        "endpoint_discovery": {
            "source_page_request_performed": False,
            "extraction_method": "OFFICIAL_SOURCE_PAGE_HTML_ANCHOR",
            "extracted_endpoint": None,
            "extracted_host": None,
        },
        "transport": {
            "download_endpoint_request_performed": False,
            "observed_at": None,
            "redirect_hops": [],
            "final_endpoint": None,
            "final_host": None,
            "http_status": None,
            "response_headers": {},
            "content_type": None,
            "content_length": None,
            "tls_scheme": None,
            "response_body_bytes_read": 0,
        },
        "safety_state": {
            "acquisition_performed": False,
            "source_approved": False,
            "source_enabled": False,
            "persist_response_body": False,
            "parse_response_body": False,
            "persist_dataset_artifact": False,
            "real_pii_processed": False,
            "beneficiary_matching_performed": False,
            "outreach_performed": False,
        },
        "result_status": "FAILED_ENDPOINT_DISCOVERY",
        "result_reason": "execution not started",
    }


def execute(args: argparse.Namespace) -> dict[str, Any]:
    result = _base_result(args)
    allowlisted_hosts = {host.lower() for host in args.allow_host}

    try:
        result["endpoint_discovery"]["source_page_request_performed"] = True
        endpoint, host = discover_endpoint(
            args.official_source_page,
            args.link_label,
            args.timeout_seconds,
            allowlisted_hosts,
        )
        result["endpoint_discovery"]["extracted_endpoint"] = endpoint
        result["endpoint_discovery"]["extracted_host"] = host
    except Exception as exc:  # noqa: BLE001 - failure is recorded fail-closed
        result["result_status"] = "FAILED_ENDPOINT_DISCOVERY"
        result["result_reason"] = f"endpoint discovery failed: {type(exc).__name__}: {exc}"
        return result

    current = endpoint
    result["transport"]["observed_at"] = _utc_now()

    try:
        for redirect_index in range(args.max_redirects + 1):
            status, headers = _head_once(current, args.timeout_seconds, allowlisted_hosts)
            result["transport"]["download_endpoint_request_performed"] = True
            location = headers.get("location")
            result["transport"]["redirect_hops"].append(
                {
                    "requested_endpoint": current,
                    "http_status": status,
                    "location": location,
                }
            )

            if 300 <= status < 400 and location:
                if redirect_index >= args.max_redirects:
                    result["result_status"] = "BLOCKED_REDIRECT_LIMIT"
                    result["result_reason"] = (
                        "redirect limit reached before a terminal response"
                    )
                    return result
                next_endpoint = urljoin(current, location)
                next_host = (urlparse(next_endpoint).hostname or "").lower()
                next_scheme = urlparse(next_endpoint).scheme.lower()
                if next_scheme != "https" or next_host not in allowlisted_hosts:
                    result["result_status"] = "BLOCKED_REDIRECT_HOST"
                    result["result_reason"] = (
                        "redirect target blocked because it is not HTTPS on an "
                        f"allowlisted host: {next_endpoint}"
                    )
                    return result
                current = next_endpoint
                continue

            final_host = (urlparse(current).hostname or "").lower()
            content_length_raw = headers.get("content-length")
            content_length = None
            if content_length_raw and content_length_raw.isdigit():
                content_length = int(content_length_raw)

            result["transport"].update(
                {
                    "final_endpoint": current,
                    "final_host": final_host,
                    "http_status": status,
                    "response_headers": headers,
                    "content_type": headers.get("content-type"),
                    "content_length": content_length,
                    "tls_scheme": "https",
                    "response_body_bytes_read": 0,
                }
            )
            result["result_status"] = "SUCCEEDED"
            result["result_reason"] = (
                "metadata-only HEAD preflight completed without reading response body bytes"
            )
            return result

        result["result_status"] = "BLOCKED_REDIRECT_LIMIT"
        result["result_reason"] = "redirect limit exhausted"
        return result
    except Exception as exc:  # noqa: BLE001 - failure is recorded fail-closed
        result["result_status"] = "FAILED_TRANSPORT"
        result["result_reason"] = f"transport preflight failed: {type(exc).__name__}: {exc}"
        return result


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--approval-ref", required=True)
    parser.add_argument("--official-source-page", required=True)
    parser.add_argument("--link-label", required=True)
    parser.add_argument("--allow-host", action="append", required=True)
    parser.add_argument("--timeout-seconds", type=int, default=10)
    parser.add_argument("--max-redirects", type=int, default=3)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if not 1 <= args.timeout_seconds <= 30:
        parser.error("--timeout-seconds must be between 1 and 30")
    if not 0 <= args.max_redirects <= 5:
        parser.error("--max-redirects must be between 0 and 5")
    return args


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(sys.argv[1:] if argv is None else argv)
    result = execute(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    compact = json.dumps(result, sort_keys=True, separators=(",", ":"))
    print(f"PREFLIGHT_RESULT_JSON={compact}")
    acceptable_results = {
        "SUCCEEDED",
        "BLOCKED_REDIRECT_HOST",
        "BLOCKED_REDIRECT_LIMIT",
    }
    return 0 if result["result_status"] in acceptable_results else 1


if __name__ == "__main__":
    raise SystemExit(main())
