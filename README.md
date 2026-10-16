# Fiber AI Python SDK

Official Python SDK for the [Fiber AI API](https://fiber.ai). Auto-generated from the [OpenAPI specification](https://api.fiber.ai/openapi.json).

[![PyPI version](https://badge.fury.io/py/fiberai.svg)](https://pypi.org/project/fiberai/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## For AI agents (Cursor / Claude / Codex / ChatGPT / Copilot)

Do NOT guess operation names — read the canonical agent-facing docs first:

- **Routing index + critical rules:** https://api.fiber.ai/llms.txt
- **Per-operation markdown:** `https://api.fiber.ai/ai-docs/<operationId>.md`
  (e.g. [`companySearch`](https://api.fiber.ai/ai-docs/companySearch.md),
  [`syncQuickContactReveal`](https://api.fiber.ai/ai-docs/syncQuickContactReveal.md),
  [`triggerExhaustiveContactEnrichment`](https://api.fiber.ai/ai-docs/triggerExhaustiveContactEnrichment.md))
- **Operation index:** https://api.fiber.ai/ai-docs/index.md
- **Full corpus (single file):** https://api.fiber.ai/llms-full.txt
- **OpenAPI spec:** `https://api.fiber.ai/openapi.json`
  (send `Accept: text/markdown` for the agent-friendly variant)
- **MCP server:** `https://mcp.fiber.ai/mcp/v2` (also see [fiber-ai/mcp](https://github.com/fiber-ai/mcp))

See also [`llms.txt`](./llms.txt) in this repo for the SDK-specific quickstart.

## Table of contents

- [Installation](#installation)
- [Quick start](#quick-start)
- [Authentication](#authentication)
- [Async usage](#async-usage)
- [Detailed responses](#detailed-responses)
- [Error handling](#error-handling)
- [Pagination](#pagination)
- [Credit tracking](#credit-tracking)
- [Available API modules](#available-api-modules)
- [Configuration](#configuration)
- [Choosing the right operation](#choosing-the-right-operation)
- [Links](#links)

## Installation

```bash
pip install fiberai
```

Requires Python 3.11 or newer. Runtime dependencies: `httpx`, `attrs`, `python-dateutil`.

## Quick start

```python
import os
from fiberai import Client
from fiberai.api.search import company_search
from fiberai.models import CompanySearchBody
from fiberai.models.company_search_response_200 import CompanySearchResponse200

client: Client = Client(base_url="https://api.fiber.ai")

body: CompanySearchBody = CompanySearchBody.from_dict({
    "apiKey": os.environ["FIBER_API_KEY"],
    "searchParams": {
        "industriesV2": {"anyOf": ["Software"]},
        "employeeCountV2": {
            "lowerBoundExclusive": 50,
            "upperBoundInclusive": 500,
        },
    },
    "pageSize": 10,
})

result = company_search.sync(client=client, body=body)

if isinstance(result, CompanySearchResponse200):
    for company in result.output.data:
        print(company.to_dict())
else:
    # 4xx / 5xx — `result` is one of CompanySearchResponse{400,401,402,403,404,429,500}
    print("error:", result.to_dict() if result else "no body")
```

> **Field names matter.** The body keys are camelCase JSON (`apiKey`, `searchParams`, `industriesV2`, `employeeCountV2`) — not the snake-case Python attributes. `from_dict` accepts the same shape the HTTP API accepts. See [`https://api.fiber.ai/ai-docs/companySearch.md`](https://api.fiber.ai/ai-docs/companySearch.md) for the full filter list.

## Authentication

Every generated operation takes your key as a required `apiKey` field (in the request body, or as the `api_key` argument for GET operations), so the plain `Client` is all you need:

```python
from fiberai import Client

client: Client = Client(base_url="https://api.fiber.ai")
```

`AuthenticatedClient` is also exported. It sends the key as an `Authorization: Bearer` header, which the API accepts too, but the generated models still require `apiKey`, so it adds nothing over `Client`.

Get an API key at https://fiber.ai/app/api. Production keys start with `sk_live_`, sandbox keys with `sk_test_`. Treat them like passwords — never commit them; load from `os.environ` or a secrets manager.

## Async usage

Every operation ships sync and async variants. The signature, body model, and return type are identical; only the function name changes (`sync` → `asyncio`, `sync_detailed` → `asyncio_detailed`):

```python
import asyncio
import os
from fiberai import Client
from fiberai.api.search import company_search
from fiberai.models import CompanySearchBody
from fiberai.models.company_search_response_200 import CompanySearchResponse200


async def main() -> None:
    client: Client = Client(base_url="https://api.fiber.ai")

    body: CompanySearchBody = CompanySearchBody.from_dict({
        "apiKey": os.environ["FIBER_API_KEY"],
        "searchParams": {"industriesV2": {"anyOf": ["Software"]}},
        "pageSize": 10,
    })

    result = await company_search.asyncio(client=client, body=body)
    if isinstance(result, CompanySearchResponse200):
        print(f"got {len(result.output.data)} companies")


asyncio.run(main())
```

For long-running scripts, reuse a single `Client` (or use it as an `async with` context manager) so the underlying `httpx.AsyncClient` connection pool is shared across calls.

## Detailed responses

Use `sync_detailed` / `asyncio_detailed` when you need the HTTP status code, headers, or raw body alongside the parsed object:

```python
from fiberai.api.search import company_search
from fiberai.types import Response

response: Response = company_search.sync_detailed(client=client, body=body)
print(response.status_code)   # http.HTTPStatus
print(response.headers)       # MutableMapping[str, str]
print(response.content)       # raw bytes
print(response.parsed)        # the same object sync() returns (or None)
```

`response.headers` is where you read `Retry-After` for 429s, `X-Request-Id` for support tickets, etc.

## Error handling

The non-detailed call returns a discriminated union covering every documented status. Type-narrow with `isinstance` to dispatch:

```python
from fiberai.api.search import company_search
from fiberai.models.company_search_response_200 import CompanySearchResponse200
from fiberai.models.company_search_response_401 import CompanySearchResponse401
from fiberai.models.company_search_response_402 import CompanySearchResponse402
from fiberai.models.company_search_response_429 import CompanySearchResponse429

result = company_search.sync(client=client, body=body)

if isinstance(result, CompanySearchResponse200):
    companies = result.output.data
elif isinstance(result, CompanySearchResponse401):
    raise RuntimeError("invalid API key")
elif isinstance(result, CompanySearchResponse402):
    raise RuntimeError("out of credits — top up at https://fiber.ai/app/billing")
elif isinstance(result, CompanySearchResponse429):
    # Rate limited — sync_detailed exposes the Retry-After header
    raise RuntimeError("rate limited; back off and retry")
else:
    raise RuntimeError(f"unexpected error: {result}")
```

For undocumented status codes (e.g. transient 502/503 from upstream), the SDK returns `None` by default. Set `raise_on_unexpected_status=True` to surface them as exceptions instead:

```python
from fiberai import Client
from fiberai import errors

client: Client = Client(
    base_url="https://api.fiber.ai",
    raise_on_unexpected_status=True,
)

try:
    result = company_search.sync(client=client, body=body)
except errors.UnexpectedStatus as exc:
    print(exc.status_code, exc.content[:200])
```

`httpx.TimeoutException` (request exceeded `timeout`) and `httpx.ConnectError` (network) propagate untouched.

## Pagination

Search responses include `output.next_cursor`. Pass it back as the next request's `cursor` to walk the full result set:

```python
import os
from typing import Optional
from fiberai.api.search import company_search
from fiberai.models import CompanySearchBody
from fiberai.models.company_search_response_200 import CompanySearchResponse200

cursor: Optional[str] = None
all_companies: list[dict] = []

while True:
    body: CompanySearchBody = CompanySearchBody.from_dict({
        "apiKey": os.environ["FIBER_API_KEY"],
        "searchParams": {"industriesV2": {"anyOf": ["Software"]}},
        "pageSize": 100,
        **({"cursor": cursor} if cursor else {}),
    })

    result = company_search.sync(client=client, body=body)
    if not isinstance(result, CompanySearchResponse200):
        raise RuntimeError(f"search failed: {result}")

    all_companies.extend(c.to_dict() for c in result.output.data)

    cursor = result.output.next_cursor or None
    if not cursor:
        break
```

The same pattern applies to `people_search`, `investor_search`, `investment_search`, and `job_posting_search`.

## Credit tracking

Every successful response carries a `charge_info` object documenting exactly how many credits were consumed and why. Persist it for billing reconciliation rather than deriving cost from result counts:

```python
result = company_search.sync(client=client, body=body)
if isinstance(result, CompanySearchResponse200):
    print(result.charge_info.to_dict())
    # { "method": "...", "creditsCharged": 7.0 }
```

To check your balance before kicking off a large batch:

```python
import os
from fiberai.api.account import get_org_credits
from fiberai.models.get_org_credits_response_200 import GetOrgCreditsResponse200

credits = get_org_credits.sync(client=client, api_key=os.environ["FIBER_API_KEY"])
if isinstance(credits, GetOrgCreditsResponse200):
    print(credits.to_dict())
```

> `get_org_credits` is a `GET` request that takes the API key as a query-string kwarg rather than a body. A handful of read-only utility operations follow this convention; the per-operation docs at https://api.fiber.ai/ai-docs/index.md note which.

## Available API modules

The SDK is organized by API domain. The endpoint path corresponding to each operation lives in the module's `_get_kwargs` helper if you need to grep for it.

| Module | What's in it |
|--------|--------------|
| `fiberai.api.search` | `company_search`, `people_search`, `investor_search`, `investment_search`, `job_posting_search` (+ `_count` variants), and the combined-search trio (`combined_search`, `sync_combined_search`, `poll_combined_search`) |
| `fiberai.api.live_fetch` | Real-time LinkedIn fetches: `profile_live_enrich`, `company_live_enrich`, plus posts/comments/reactions for both profiles and companies |
| `fiberai.api.contact_details` | Email + phone reveal: `sync_contact_enrichment` (sync), `trigger_contact_enrichment` + `poll_contact_enrichment_result` (async waterfall), `start_batch_contact_enrichment` + `poll_batch_contact_enrichment` (batch) |
| `fiberai.api.kitchen_sink` | Bulk company/profile lookup by identifier: `kitchen_sink_company`, `kitchen_sink_profile`, `kitchen_sink_bulk_company`, `kitchen_sink_bulk_profile` |
| `fiberai.api.google_maps` | Google Maps business search: `google_maps_search`, `poll_google_maps_results`, `check_google_maps_results` |
| `fiberai.api.ai_research` | AI-powered domain lookup: `domain_lookup_trigger`, `domain_lookup_polling` |
| `fiberai.api.agentic_search` | LLM-powered text-to-search: `text_to_company_search`, `text_to_profile_search`, `text_to_combined_search` |
| `fiberai.api.exclusions` | Manage company and prospect exclusion lists (create / add / remove / list / delete) |
| `fiberai.api.saved_search` | Saved search lifecycle: create, list, run, fetch run results |
| `fiberai.api.email_lookup` | `reverse_email_lookup` (email → LinkedIn profile) |
| `fiberai.api.validation` | `email_bounce_detection` |
| `fiberai.api.account` | `get_org_credits` |
| `fiberai.api.enums` | Enum value lookups: industries, accelerators, NAICS codes, regions, languages, tags, time zones |
| `fiberai.api.typeaheads` | `company_typeahead`, `location_typeahead` |
| `fiberai.api.company_info` | `bulk_company_logos` |
| `fiberai.api.coming_soon` | Beta endpoints: `start_local_business_search`, `poll_local_business_search` |
| `fiberai.api.utility` | `health_check`, `get_open_api` (no API key required) |

> If you want LinkedIn-URL → company details, use `live_fetch.company_live_enrich` (not `company_info`). The `company_info` module currently only exposes bulk logo fetching.

The Python SDK lags slightly behind the API in a few places — notably the new `syncQuickContactReveal` / `syncTurboContactEnrichment` / `triggerExhaustiveContactEnrichment` operation names, which still ship under their older `sync_contact_enrichment` / `trigger_contact_enrichment` module names here. See [`llms.txt`](./llms.txt) for the workaround (direct `httpx` call) until the next regeneration.

## Configuration

`Client` accepts the same kwargs as `httpx.Client` plus a few of its own:

```python
import httpx
import ssl
from fiberai import Client

client: Client = Client(
    base_url="https://api.fiber.ai",
    timeout=httpx.Timeout(60.0, connect=10.0),
    headers={"X-Custom-Header": "value"},
    cookies={"session": "..."},
    verify_ssl=True,                       # bool | str | ssl.SSLContext
    follow_redirects=False,
    raise_on_unexpected_status=False,      # see "Error handling"
    httpx_args={"http2": True},            # forwarded to httpx.Client(...)
)
```

Useful helpers (each returns a *new* `Client` rather than mutating in place):

```python
client_with_auth: Client = client.with_headers({"X-Trace-Id": "abc123"})
client_with_timeout: Client = client.with_timeout(httpx.Timeout(120.0))
```

For long-running services, use the client as a context manager so connection pools are torn down cleanly:

```python
with Client(base_url="https://api.fiber.ai") as client:
    result = company_search.sync(client=client, body=body)

# or, async:
async with Client(base_url="https://api.fiber.ai") as client:
    result = await company_search.asyncio(client=client, body=body)
```

## Choosing the right operation

Several Fiber operations cover overlapping use cases (e.g. three different ways to reveal contact info, two ways to search). The trade-offs (cost, latency, coverage, quality) live in the per-operation docs, not in this README:

| Use case | Read this |
|----------|-----------|
| Sync vs turbo vs exhaustive contact reveal | https://api.fiber.ai/llms.txt and the relevant `ai-docs/<operationId>.md` |
| When to use audiences vs ad-hoc search | https://api.fiber.ai/ai-docs/index.md |
| Rate limits and credit cost per operation | Stamped at the top of each `ai-docs/<operationId>.md` page |

When in doubt, prefer reading these over guessing — the routing rules change faster than this SDK regenerates.

## Links

- [Fiber AI](https://fiber.ai) — main website
- [API documentation](https://docs.fiber.ai) — full API docs
- [Per-operation reference](https://api.fiber.ai/ai-docs/index.md) — every operation, its schema, its cost
- [TypeScript SDK](https://github.com/fiber-ai/typescript-sdk) — TypeScript/JavaScript SDK
- [MCP server](https://github.com/fiber-ai/mcp) — expose Fiber operations as MCP tools to your agent
- [Get an API key](https://fiber.ai/app/api)
- [Issues](https://github.com/fiber-ai/python-sdk/issues) — bug reports and feature requests

## License

MIT — see [LICENSE](./LICENSE) for details.
