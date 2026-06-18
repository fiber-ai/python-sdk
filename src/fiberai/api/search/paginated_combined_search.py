from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_combined_search_body import PaginatedCombinedSearchBody
from ...models.paginated_combined_search_response_200 import PaginatedCombinedSearchResponse200
from ...models.paginated_combined_search_response_400 import PaginatedCombinedSearchResponse400
from ...models.paginated_combined_search_response_401 import PaginatedCombinedSearchResponse401
from ...models.paginated_combined_search_response_402 import PaginatedCombinedSearchResponse402
from ...models.paginated_combined_search_response_403 import PaginatedCombinedSearchResponse403
from ...models.paginated_combined_search_response_404 import PaginatedCombinedSearchResponse404
from ...models.paginated_combined_search_response_422 import PaginatedCombinedSearchResponse422
from ...models.paginated_combined_search_response_429 import PaginatedCombinedSearchResponse429
from ...models.paginated_combined_search_response_500 import PaginatedCombinedSearchResponse500
from ...models.paginated_combined_search_response_503 import PaginatedCombinedSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PaginatedCombinedSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/combined-search/paginated",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PaginatedCombinedSearchResponse200
    | PaginatedCombinedSearchResponse400
    | PaginatedCombinedSearchResponse401
    | PaginatedCombinedSearchResponse402
    | PaginatedCombinedSearchResponse403
    | PaginatedCombinedSearchResponse404
    | PaginatedCombinedSearchResponse422
    | PaginatedCombinedSearchResponse429
    | PaginatedCombinedSearchResponse500
    | PaginatedCombinedSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedCombinedSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PaginatedCombinedSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PaginatedCombinedSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PaginatedCombinedSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PaginatedCombinedSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PaginatedCombinedSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PaginatedCombinedSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PaginatedCombinedSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PaginatedCombinedSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PaginatedCombinedSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PaginatedCombinedSearchResponse200
    | PaginatedCombinedSearchResponse400
    | PaginatedCombinedSearchResponse401
    | PaginatedCombinedSearchResponse402
    | PaginatedCombinedSearchResponse403
    | PaginatedCombinedSearchResponse404
    | PaginatedCombinedSearchResponse422
    | PaginatedCombinedSearchResponse429
    | PaginatedCombinedSearchResponse500
    | PaginatedCombinedSearchResponse503
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
    body: PaginatedCombinedSearchBody,
) -> Response[
    PaginatedCombinedSearchResponse200
    | PaginatedCombinedSearchResponse400
    | PaginatedCombinedSearchResponse401
    | PaginatedCombinedSearchResponse402
    | PaginatedCombinedSearchResponse403
    | PaginatedCombinedSearchResponse404
    | PaginatedCombinedSearchResponse422
    | PaginatedCombinedSearchResponse429
    | PaginatedCombinedSearchResponse500
    | PaginatedCombinedSearchResponse503
]:
    r"""Combined people + company search

     Search for companies and profiles together. Returns results page by page using cursor-based
    pagination. Each entity type (companies, profiles) has its own cursor, so you can paginate them
    independently.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged per page based on results: 1 credits per company
    found and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Your total charge will vary based on the number of companies and profiles returned
    in your results.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PaginatedCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCombinedSearchResponse200 | PaginatedCombinedSearchResponse400 | PaginatedCombinedSearchResponse401 | PaginatedCombinedSearchResponse402 | PaginatedCombinedSearchResponse403 | PaginatedCombinedSearchResponse404 | PaginatedCombinedSearchResponse422 | PaginatedCombinedSearchResponse429 | PaginatedCombinedSearchResponse500 | PaginatedCombinedSearchResponse503]
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
    body: PaginatedCombinedSearchBody,
) -> (
    PaginatedCombinedSearchResponse200
    | PaginatedCombinedSearchResponse400
    | PaginatedCombinedSearchResponse401
    | PaginatedCombinedSearchResponse402
    | PaginatedCombinedSearchResponse403
    | PaginatedCombinedSearchResponse404
    | PaginatedCombinedSearchResponse422
    | PaginatedCombinedSearchResponse429
    | PaginatedCombinedSearchResponse500
    | PaginatedCombinedSearchResponse503
    | None
):
    r"""Combined people + company search

     Search for companies and profiles together. Returns results page by page using cursor-based
    pagination. Each entity type (companies, profiles) has its own cursor, so you can paginate them
    independently.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged per page based on results: 1 credits per company
    found and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Your total charge will vary based on the number of companies and profiles returned
    in your results.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PaginatedCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCombinedSearchResponse200 | PaginatedCombinedSearchResponse400 | PaginatedCombinedSearchResponse401 | PaginatedCombinedSearchResponse402 | PaginatedCombinedSearchResponse403 | PaginatedCombinedSearchResponse404 | PaginatedCombinedSearchResponse422 | PaginatedCombinedSearchResponse429 | PaginatedCombinedSearchResponse500 | PaginatedCombinedSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PaginatedCombinedSearchBody,
) -> Response[
    PaginatedCombinedSearchResponse200
    | PaginatedCombinedSearchResponse400
    | PaginatedCombinedSearchResponse401
    | PaginatedCombinedSearchResponse402
    | PaginatedCombinedSearchResponse403
    | PaginatedCombinedSearchResponse404
    | PaginatedCombinedSearchResponse422
    | PaginatedCombinedSearchResponse429
    | PaginatedCombinedSearchResponse500
    | PaginatedCombinedSearchResponse503
]:
    r"""Combined people + company search

     Search for companies and profiles together. Returns results page by page using cursor-based
    pagination. Each entity type (companies, profiles) has its own cursor, so you can paginate them
    independently.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged per page based on results: 1 credits per company
    found and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Your total charge will vary based on the number of companies and profiles returned
    in your results.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PaginatedCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCombinedSearchResponse200 | PaginatedCombinedSearchResponse400 | PaginatedCombinedSearchResponse401 | PaginatedCombinedSearchResponse402 | PaginatedCombinedSearchResponse403 | PaginatedCombinedSearchResponse404 | PaginatedCombinedSearchResponse422 | PaginatedCombinedSearchResponse429 | PaginatedCombinedSearchResponse500 | PaginatedCombinedSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PaginatedCombinedSearchBody,
) -> (
    PaginatedCombinedSearchResponse200
    | PaginatedCombinedSearchResponse400
    | PaginatedCombinedSearchResponse401
    | PaginatedCombinedSearchResponse402
    | PaginatedCombinedSearchResponse403
    | PaginatedCombinedSearchResponse404
    | PaginatedCombinedSearchResponse422
    | PaginatedCombinedSearchResponse429
    | PaginatedCombinedSearchResponse500
    | PaginatedCombinedSearchResponse503
    | None
):
    r"""Combined people + company search

     Search for companies and profiles together. Returns results page by page using cursor-based
    pagination. Each entity type (companies, profiles) has its own cursor, so you can paginate them
    independently.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged per page based on results: 1 credits per company
    found and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Your total charge will vary based on the number of companies and profiles returned
    in your results.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PaginatedCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCombinedSearchResponse200 | PaginatedCombinedSearchResponse400 | PaginatedCombinedSearchResponse401 | PaginatedCombinedSearchResponse402 | PaginatedCombinedSearchResponse403 | PaginatedCombinedSearchResponse404 | PaginatedCombinedSearchResponse422 | PaginatedCombinedSearchResponse429 | PaginatedCombinedSearchResponse500 | PaginatedCombinedSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
