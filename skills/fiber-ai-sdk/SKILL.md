---
name: fiber-ai-sdk-python
description: Use the Fiber AI Python SDK to call Fiber AI APIs and answer questions about its methods and schemas.
---

# Fiber AI Python SDK Skill

Use the official `fiberai` package to call Fiber AI APIs from Python.

## When to activate

- User asks how to integrate Fiber AI in a Python project.
- User wants to know which Python method to use.
- User asks for code examples in Python.

## Instructions

1. Ensure the user has installed `fiberai` (Python 3.11+): `pip install fiberai`.
2. Every request needs an `apiKey` (request body, or `api_key` for GET operations).
3. Use the plain `Client` for requests.
4. Methods are organized by sub-modules: `fiberai.api.search`, `fiberai.api.contact_details`, etc.

## Examples

### 1. Simple Search
```python
from fiberai import Client
from fiberai.api.search import company_search
from fiberai.models import CompanySearchBody

client = Client(base_url="https://api.fiber.ai")
body = CompanySearchBody.from_dict({
    "apiKey": "sk_live_...",
    "searchParams": {"industriesV2": {"anyOf": ["Software"]}},
    "pageSize": 10,
})

response = company_search.sync(client=client, body=body)
```

### 2. Async Usage
```python
import asyncio
from fiberai import Client
from fiberai.api.search import company_search

async def search():
    client = Client(base_url="https://api.fiber.ai")
    response = await company_search.asyncio(client=client, body=body)
```

### 3. Error Handling
The SDK raises no errors by default unless `raise_on_unexpected_status=True` is set on the Client. Check `response.status_code` otherwise.
```python
from fiberai import errors
client = Client(base_url="...", raise_on_unexpected_status=True)
```
