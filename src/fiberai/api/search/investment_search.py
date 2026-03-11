from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.investment_search_body import InvestmentSearchBody
from ...models.investment_search_response_200 import InvestmentSearchResponse200
from ...models.investment_search_response_400 import InvestmentSearchResponse400
from ...models.investment_search_response_401 import InvestmentSearchResponse401
from ...models.investment_search_response_402 import InvestmentSearchResponse402
from ...models.investment_search_response_403 import InvestmentSearchResponse403
from ...models.investment_search_response_404 import InvestmentSearchResponse404
from ...models.investment_search_response_429 import InvestmentSearchResponse429
from ...models.investment_search_response_500 import InvestmentSearchResponse500
from ...models.investment_search_response_503 import InvestmentSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: InvestmentSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/investment-search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InvestmentSearchResponse200
    | InvestmentSearchResponse400
    | InvestmentSearchResponse401
    | InvestmentSearchResponse402
    | InvestmentSearchResponse403
    | InvestmentSearchResponse404
    | InvestmentSearchResponse429
    | InvestmentSearchResponse500
    | InvestmentSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = InvestmentSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InvestmentSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InvestmentSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = InvestmentSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InvestmentSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InvestmentSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = InvestmentSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InvestmentSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = InvestmentSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InvestmentSearchResponse200
    | InvestmentSearchResponse400
    | InvestmentSearchResponse401
    | InvestmentSearchResponse402
    | InvestmentSearchResponse403
    | InvestmentSearchResponse404
    | InvestmentSearchResponse429
    | InvestmentSearchResponse500
    | InvestmentSearchResponse503
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
    body: InvestmentSearchBody,
) -> Response[
    InvestmentSearchResponse200
    | InvestmentSearchResponse400
    | InvestmentSearchResponse401
    | InvestmentSearchResponse402
    | InvestmentSearchResponse403
    | InvestmentSearchResponse404
    | InvestmentSearchResponse429
    | InvestmentSearchResponse500
    | InvestmentSearchResponse503
]:
    r"""Investment search

     Search for investments with flexible filtering capabilities. Supports filtering by investor,
    company, round type, location, and financial metrics.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per investment found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InvestmentSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvestmentSearchResponse200 | InvestmentSearchResponse400 | InvestmentSearchResponse401 | InvestmentSearchResponse402 | InvestmentSearchResponse403 | InvestmentSearchResponse404 | InvestmentSearchResponse429 | InvestmentSearchResponse500 | InvestmentSearchResponse503]
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
    body: InvestmentSearchBody,
) -> (
    InvestmentSearchResponse200
    | InvestmentSearchResponse400
    | InvestmentSearchResponse401
    | InvestmentSearchResponse402
    | InvestmentSearchResponse403
    | InvestmentSearchResponse404
    | InvestmentSearchResponse429
    | InvestmentSearchResponse500
    | InvestmentSearchResponse503
    | None
):
    r"""Investment search

     Search for investments with flexible filtering capabilities. Supports filtering by investor,
    company, round type, location, and financial metrics.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per investment found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InvestmentSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvestmentSearchResponse200 | InvestmentSearchResponse400 | InvestmentSearchResponse401 | InvestmentSearchResponse402 | InvestmentSearchResponse403 | InvestmentSearchResponse404 | InvestmentSearchResponse429 | InvestmentSearchResponse500 | InvestmentSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InvestmentSearchBody,
) -> Response[
    InvestmentSearchResponse200
    | InvestmentSearchResponse400
    | InvestmentSearchResponse401
    | InvestmentSearchResponse402
    | InvestmentSearchResponse403
    | InvestmentSearchResponse404
    | InvestmentSearchResponse429
    | InvestmentSearchResponse500
    | InvestmentSearchResponse503
]:
    r"""Investment search

     Search for investments with flexible filtering capabilities. Supports filtering by investor,
    company, round type, location, and financial metrics.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per investment found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InvestmentSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvestmentSearchResponse200 | InvestmentSearchResponse400 | InvestmentSearchResponse401 | InvestmentSearchResponse402 | InvestmentSearchResponse403 | InvestmentSearchResponse404 | InvestmentSearchResponse429 | InvestmentSearchResponse500 | InvestmentSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InvestmentSearchBody,
) -> (
    InvestmentSearchResponse200
    | InvestmentSearchResponse400
    | InvestmentSearchResponse401
    | InvestmentSearchResponse402
    | InvestmentSearchResponse403
    | InvestmentSearchResponse404
    | InvestmentSearchResponse429
    | InvestmentSearchResponse500
    | InvestmentSearchResponse503
    | None
):
    r"""Investment search

     Search for investments with flexible filtering capabilities. Supports filtering by investor,
    company, round type, location, and financial metrics.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per investment found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InvestmentSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvestmentSearchResponse200 | InvestmentSearchResponse400 | InvestmentSearchResponse401 | InvestmentSearchResponse402 | InvestmentSearchResponse403 | InvestmentSearchResponse404 | InvestmentSearchResponse429 | InvestmentSearchResponse500 | InvestmentSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
