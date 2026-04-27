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

1. Ensure the user has installed `fiberai`: `pip install fiberai`.
2. Every request needs an `apiKey`.
3. Use the `Client` or `AuthenticatedClient` for requests.
4. Methods are organized by sub-modules: `fiberai.api.search`, `fiberai.api.contact_details`, etc.

## Examples

### 1. Simple Search
```python
from fiberai import Client
from fiberai.api.search import company_search
from fiberai.models import CompanySearchBody, CompanySearchBodySearchParams

client = Client(base_url="https://api.fiber.ai")
body = CompanySearchBody(
    api_key="sk_live_...",
    search_params=CompanySearchBodySearchParams.from_dict({
        "standardIndustries": {"anyOf": [{"slug": "software"}]}
    })
)

response = company_search.sync(client=client, body=body)
```

### 2. Async Usage
```python
import asyncio
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
