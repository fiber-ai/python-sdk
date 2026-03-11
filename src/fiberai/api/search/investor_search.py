from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.investor_search_body import InvestorSearchBody
from ...models.investor_search_response_200 import InvestorSearchResponse200
from ...models.investor_search_response_400 import InvestorSearchResponse400
from ...models.investor_search_response_401 import InvestorSearchResponse401
from ...models.investor_search_response_402 import InvestorSearchResponse402
from ...models.investor_search_response_403 import InvestorSearchResponse403
from ...models.investor_search_response_404 import InvestorSearchResponse404
from ...models.investor_search_response_429 import InvestorSearchResponse429
from ...models.investor_search_response_500 import InvestorSearchResponse500
from ...models.investor_search_response_503 import InvestorSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: InvestorSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/investor-search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InvestorSearchResponse200
    | InvestorSearchResponse400
    | InvestorSearchResponse401
    | InvestorSearchResponse402
    | InvestorSearchResponse403
    | InvestorSearchResponse404
    | InvestorSearchResponse429
    | InvestorSearchResponse500
    | InvestorSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = InvestorSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InvestorSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InvestorSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = InvestorSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InvestorSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InvestorSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = InvestorSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InvestorSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = InvestorSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InvestorSearchResponse200
    | InvestorSearchResponse400
    | InvestorSearchResponse401
    | InvestorSearchResponse402
    | InvestorSearchResponse403
    | InvestorSearchResponse404
    | InvestorSearchResponse429
    | InvestorSearchResponse500
    | InvestorSearchResponse503
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
    body: InvestorSearchBody,
) -> Response[
    InvestorSearchResponse200
    | InvestorSearchResponse400
    | InvestorSearchResponse401
    | InvestorSearchResponse402
    | InvestorSearchResponse403
    | InvestorSearchResponse404
    | InvestorSearchResponse429
    | InvestorSearchResponse500
    | InvestorSearchResponse503
]:
    r"""Investor search

     Search for investors with flexible filtering capabilities

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per investor found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InvestorSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvestorSearchResponse200 | InvestorSearchResponse400 | InvestorSearchResponse401 | InvestorSearchResponse402 | InvestorSearchResponse403 | InvestorSearchResponse404 | InvestorSearchResponse429 | InvestorSearchResponse500 | InvestorSearchResponse503]
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
    body: InvestorSearchBody,
) -> (
    InvestorSearchResponse200
    | InvestorSearchResponse400
    | InvestorSearchResponse401
    | InvestorSearchResponse402
    | InvestorSearchResponse403
    | InvestorSearchResponse404
    | InvestorSearchResponse429
    | InvestorSearchResponse500
    | InvestorSearchResponse503
    | None
):
    r"""Investor search

     Search for investors with flexible filtering capabilities

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per investor found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InvestorSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvestorSearchResponse200 | InvestorSearchResponse400 | InvestorSearchResponse401 | InvestorSearchResponse402 | InvestorSearchResponse403 | InvestorSearchResponse404 | InvestorSearchResponse429 | InvestorSearchResponse500 | InvestorSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InvestorSearchBody,
) -> Response[
    InvestorSearchResponse200
    | InvestorSearchResponse400
    | InvestorSearchResponse401
    | InvestorSearchResponse402
    | InvestorSearchResponse403
    | InvestorSearchResponse404
    | InvestorSearchResponse429
    | InvestorSearchResponse500
    | InvestorSearchResponse503
]:
    r"""Investor search

     Search for investors with flexible filtering capabilities

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per investor found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InvestorSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvestorSearchResponse200 | InvestorSearchResponse400 | InvestorSearchResponse401 | InvestorSearchResponse402 | InvestorSearchResponse403 | InvestorSearchResponse404 | InvestorSearchResponse429 | InvestorSearchResponse500 | InvestorSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InvestorSearchBody,
) -> (
    InvestorSearchResponse200
    | InvestorSearchResponse400
    | InvestorSearchResponse401
    | InvestorSearchResponse402
    | InvestorSearchResponse403
    | InvestorSearchResponse404
    | InvestorSearchResponse429
    | InvestorSearchResponse500
    | InvestorSearchResponse503
    | None
):
    r"""Investor search

     Search for investors with flexible filtering capabilities

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per investor found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (InvestorSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvestorSearchResponse200 | InvestorSearchResponse400 | InvestorSearchResponse401 | InvestorSearchResponse402 | InvestorSearchResponse403 | InvestorSearchResponse404 | InvestorSearchResponse429 | InvestorSearchResponse500 | InvestorSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
