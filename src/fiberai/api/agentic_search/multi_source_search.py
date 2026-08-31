from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.multi_source_search_body import MultiSourceSearchBody
from ...models.multi_source_search_response_200 import MultiSourceSearchResponse200
from ...models.multi_source_search_response_400 import MultiSourceSearchResponse400
from ...models.multi_source_search_response_401 import MultiSourceSearchResponse401
from ...models.multi_source_search_response_402 import MultiSourceSearchResponse402
from ...models.multi_source_search_response_403 import MultiSourceSearchResponse403
from ...models.multi_source_search_response_404 import MultiSourceSearchResponse404
from ...models.multi_source_search_response_422 import MultiSourceSearchResponse422
from ...models.multi_source_search_response_429 import MultiSourceSearchResponse429
from ...models.multi_source_search_response_500 import MultiSourceSearchResponse500
from ...models.multi_source_search_response_503 import MultiSourceSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: MultiSourceSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/multi-source/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    MultiSourceSearchResponse200
    | MultiSourceSearchResponse400
    | MultiSourceSearchResponse401
    | MultiSourceSearchResponse402
    | MultiSourceSearchResponse403
    | MultiSourceSearchResponse404
    | MultiSourceSearchResponse422
    | MultiSourceSearchResponse429
    | MultiSourceSearchResponse500
    | MultiSourceSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = MultiSourceSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = MultiSourceSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = MultiSourceSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = MultiSourceSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = MultiSourceSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = MultiSourceSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = MultiSourceSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = MultiSourceSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = MultiSourceSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = MultiSourceSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    MultiSourceSearchResponse200
    | MultiSourceSearchResponse400
    | MultiSourceSearchResponse401
    | MultiSourceSearchResponse402
    | MultiSourceSearchResponse403
    | MultiSourceSearchResponse404
    | MultiSourceSearchResponse422
    | MultiSourceSearchResponse429
    | MultiSourceSearchResponse500
    | MultiSourceSearchResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MultiSourceSearchBody,
) -> Response[
    MultiSourceSearchResponse200
    | MultiSourceSearchResponse400
    | MultiSourceSearchResponse401
    | MultiSourceSearchResponse402
    | MultiSourceSearchResponse403
    | MultiSourceSearchResponse404
    | MultiSourceSearchResponse422
    | MultiSourceSearchResponse429
    | MultiSourceSearchResponse500
    | MultiSourceSearchResponse503
]:
    """Multi-source AI search

     AI-powered natural language search across multiple sources (LinkedIn, Google Maps, web, and more).
    Ideal for local business search where companies/employees have spotty web or LinkedIn presence.

    **Pagination flow:**

    1. **First page** — send `{ search: { request: "initial", query: "...", pageSize: 10 } }`. The
    `pageSize` you choose here is locked for the entire session.
    2. **Subsequent pages** — send `{ search: { request: "subsequent", cursor: "<nextCursor>" } }`.
    3. When `nextCursor` is `null` in the response, there are no more results.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the search completes based on results: 2
    credits per company found and 2 credits per prospect found. Each query resolves to either companies
    or prospects, so only one rate applies per page.&nbsp;<span title="Pricing shown is default pricing.
    Actual pricing may vary. Your total charge depends on the number of results returned and which
    entity type the query resolves to.">ⓘ</span></span>

    Args:
        body (MultiSourceSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MultiSourceSearchResponse200 | MultiSourceSearchResponse400 | MultiSourceSearchResponse401 | MultiSourceSearchResponse402 | MultiSourceSearchResponse403 | MultiSourceSearchResponse404 | MultiSourceSearchResponse422 | MultiSourceSearchResponse429 | MultiSourceSearchResponse500 | MultiSourceSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: MultiSourceSearchBody,
) -> (
    MultiSourceSearchResponse200
    | MultiSourceSearchResponse400
    | MultiSourceSearchResponse401
    | MultiSourceSearchResponse402
    | MultiSourceSearchResponse403
    | MultiSourceSearchResponse404
    | MultiSourceSearchResponse422
    | MultiSourceSearchResponse429
    | MultiSourceSearchResponse500
    | MultiSourceSearchResponse503
    | None
):
    """Multi-source AI search

     AI-powered natural language search across multiple sources (LinkedIn, Google Maps, web, and more).
    Ideal for local business search where companies/employees have spotty web or LinkedIn presence.

    **Pagination flow:**

    1. **First page** — send `{ search: { request: "initial", query: "...", pageSize: 10 } }`. The
    `pageSize` you choose here is locked for the entire session.
    2. **Subsequent pages** — send `{ search: { request: "subsequent", cursor: "<nextCursor>" } }`.
    3. When `nextCursor` is `null` in the response, there are no more results.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the search completes based on results: 2
    credits per company found and 2 credits per prospect found. Each query resolves to either companies
    or prospects, so only one rate applies per page.&nbsp;<span title="Pricing shown is default pricing.
    Actual pricing may vary. Your total charge depends on the number of results returned and which
    entity type the query resolves to.">ⓘ</span></span>

    Args:
        body (MultiSourceSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MultiSourceSearchResponse200 | MultiSourceSearchResponse400 | MultiSourceSearchResponse401 | MultiSourceSearchResponse402 | MultiSourceSearchResponse403 | MultiSourceSearchResponse404 | MultiSourceSearchResponse422 | MultiSourceSearchResponse429 | MultiSourceSearchResponse500 | MultiSourceSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MultiSourceSearchBody,
) -> Response[
    MultiSourceSearchResponse200
    | MultiSourceSearchResponse400
    | MultiSourceSearchResponse401
    | MultiSourceSearchResponse402
    | MultiSourceSearchResponse403
    | MultiSourceSearchResponse404
    | MultiSourceSearchResponse422
    | MultiSourceSearchResponse429
    | MultiSourceSearchResponse500
    | MultiSourceSearchResponse503
]:
    """Multi-source AI search

     AI-powered natural language search across multiple sources (LinkedIn, Google Maps, web, and more).
    Ideal for local business search where companies/employees have spotty web or LinkedIn presence.

    **Pagination flow:**

    1. **First page** — send `{ search: { request: "initial", query: "...", pageSize: 10 } }`. The
    `pageSize` you choose here is locked for the entire session.
    2. **Subsequent pages** — send `{ search: { request: "subsequent", cursor: "<nextCursor>" } }`.
    3. When `nextCursor` is `null` in the response, there are no more results.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the search completes based on results: 2
    credits per company found and 2 credits per prospect found. Each query resolves to either companies
    or prospects, so only one rate applies per page.&nbsp;<span title="Pricing shown is default pricing.
    Actual pricing may vary. Your total charge depends on the number of results returned and which
    entity type the query resolves to.">ⓘ</span></span>

    Args:
        body (MultiSourceSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MultiSourceSearchResponse200 | MultiSourceSearchResponse400 | MultiSourceSearchResponse401 | MultiSourceSearchResponse402 | MultiSourceSearchResponse403 | MultiSourceSearchResponse404 | MultiSourceSearchResponse422 | MultiSourceSearchResponse429 | MultiSourceSearchResponse500 | MultiSourceSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MultiSourceSearchBody,
) -> (
    MultiSourceSearchResponse200
    | MultiSourceSearchResponse400
    | MultiSourceSearchResponse401
    | MultiSourceSearchResponse402
    | MultiSourceSearchResponse403
    | MultiSourceSearchResponse404
    | MultiSourceSearchResponse422
    | MultiSourceSearchResponse429
    | MultiSourceSearchResponse500
    | MultiSourceSearchResponse503
    | None
):
    """Multi-source AI search

     AI-powered natural language search across multiple sources (LinkedIn, Google Maps, web, and more).
    Ideal for local business search where companies/employees have spotty web or LinkedIn presence.

    **Pagination flow:**

    1. **First page** — send `{ search: { request: "initial", query: "...", pageSize: 10 } }`. The
    `pageSize` you choose here is locked for the entire session.
    2. **Subsequent pages** — send `{ search: { request: "subsequent", cursor: "<nextCursor>" } }`.
    3. When `nextCursor` is `null` in the response, there are no more results.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the search completes based on results: 2
    credits per company found and 2 credits per prospect found. Each query resolves to either companies
    or prospects, so only one rate applies per page.&nbsp;<span title="Pricing shown is default pricing.
    Actual pricing may vary. Your total charge depends on the number of results returned and which
    entity type the query resolves to.">ⓘ</span></span>

    Args:
        body (MultiSourceSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MultiSourceSearchResponse200 | MultiSourceSearchResponse400 | MultiSourceSearchResponse401 | MultiSourceSearchResponse402 | MultiSourceSearchResponse403 | MultiSourceSearchResponse404 | MultiSourceSearchResponse422 | MultiSourceSearchResponse429 | MultiSourceSearchResponse500 | MultiSourceSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
