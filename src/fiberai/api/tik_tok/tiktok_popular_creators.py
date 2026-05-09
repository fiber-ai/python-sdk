from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tiktok_popular_creators_body import TiktokPopularCreatorsBody
from ...models.tiktok_popular_creators_response_200 import TiktokPopularCreatorsResponse200
from ...models.tiktok_popular_creators_response_400 import TiktokPopularCreatorsResponse400
from ...models.tiktok_popular_creators_response_401 import TiktokPopularCreatorsResponse401
from ...models.tiktok_popular_creators_response_402 import TiktokPopularCreatorsResponse402
from ...models.tiktok_popular_creators_response_403 import TiktokPopularCreatorsResponse403
from ...models.tiktok_popular_creators_response_404 import TiktokPopularCreatorsResponse404
from ...models.tiktok_popular_creators_response_429 import TiktokPopularCreatorsResponse429
from ...models.tiktok_popular_creators_response_500 import TiktokPopularCreatorsResponse500
from ...models.tiktok_popular_creators_response_503 import TiktokPopularCreatorsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TiktokPopularCreatorsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tiktok/popular-creators",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TiktokPopularCreatorsResponse200
    | TiktokPopularCreatorsResponse400
    | TiktokPopularCreatorsResponse401
    | TiktokPopularCreatorsResponse402
    | TiktokPopularCreatorsResponse403
    | TiktokPopularCreatorsResponse404
    | TiktokPopularCreatorsResponse429
    | TiktokPopularCreatorsResponse500
    | TiktokPopularCreatorsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TiktokPopularCreatorsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TiktokPopularCreatorsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TiktokPopularCreatorsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TiktokPopularCreatorsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TiktokPopularCreatorsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TiktokPopularCreatorsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TiktokPopularCreatorsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TiktokPopularCreatorsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TiktokPopularCreatorsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TiktokPopularCreatorsResponse200
    | TiktokPopularCreatorsResponse400
    | TiktokPopularCreatorsResponse401
    | TiktokPopularCreatorsResponse402
    | TiktokPopularCreatorsResponse403
    | TiktokPopularCreatorsResponse404
    | TiktokPopularCreatorsResponse429
    | TiktokPopularCreatorsResponse500
    | TiktokPopularCreatorsResponse503
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
    body: TiktokPopularCreatorsBody,
) -> Response[
    TiktokPopularCreatorsResponse200
    | TiktokPopularCreatorsResponse400
    | TiktokPopularCreatorsResponse401
    | TiktokPopularCreatorsResponse402
    | TiktokPopularCreatorsResponse403
    | TiktokPopularCreatorsResponse404
    | TiktokPopularCreatorsResponse429
    | TiktokPopularCreatorsResponse500
    | TiktokPopularCreatorsResponse503
]:
    r"""Fetch popular TikTok creators

     Fetches a list of popular TikTok creators. Optionally filter by country and sort order.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokPopularCreatorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokPopularCreatorsResponse200 | TiktokPopularCreatorsResponse400 | TiktokPopularCreatorsResponse401 | TiktokPopularCreatorsResponse402 | TiktokPopularCreatorsResponse403 | TiktokPopularCreatorsResponse404 | TiktokPopularCreatorsResponse429 | TiktokPopularCreatorsResponse500 | TiktokPopularCreatorsResponse503]
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
    body: TiktokPopularCreatorsBody,
) -> (
    TiktokPopularCreatorsResponse200
    | TiktokPopularCreatorsResponse400
    | TiktokPopularCreatorsResponse401
    | TiktokPopularCreatorsResponse402
    | TiktokPopularCreatorsResponse403
    | TiktokPopularCreatorsResponse404
    | TiktokPopularCreatorsResponse429
    | TiktokPopularCreatorsResponse500
    | TiktokPopularCreatorsResponse503
    | None
):
    r"""Fetch popular TikTok creators

     Fetches a list of popular TikTok creators. Optionally filter by country and sort order.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokPopularCreatorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokPopularCreatorsResponse200 | TiktokPopularCreatorsResponse400 | TiktokPopularCreatorsResponse401 | TiktokPopularCreatorsResponse402 | TiktokPopularCreatorsResponse403 | TiktokPopularCreatorsResponse404 | TiktokPopularCreatorsResponse429 | TiktokPopularCreatorsResponse500 | TiktokPopularCreatorsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokPopularCreatorsBody,
) -> Response[
    TiktokPopularCreatorsResponse200
    | TiktokPopularCreatorsResponse400
    | TiktokPopularCreatorsResponse401
    | TiktokPopularCreatorsResponse402
    | TiktokPopularCreatorsResponse403
    | TiktokPopularCreatorsResponse404
    | TiktokPopularCreatorsResponse429
    | TiktokPopularCreatorsResponse500
    | TiktokPopularCreatorsResponse503
]:
    r"""Fetch popular TikTok creators

     Fetches a list of popular TikTok creators. Optionally filter by country and sort order.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokPopularCreatorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TiktokPopularCreatorsResponse200 | TiktokPopularCreatorsResponse400 | TiktokPopularCreatorsResponse401 | TiktokPopularCreatorsResponse402 | TiktokPopularCreatorsResponse403 | TiktokPopularCreatorsResponse404 | TiktokPopularCreatorsResponse429 | TiktokPopularCreatorsResponse500 | TiktokPopularCreatorsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TiktokPopularCreatorsBody,
) -> (
    TiktokPopularCreatorsResponse200
    | TiktokPopularCreatorsResponse400
    | TiktokPopularCreatorsResponse401
    | TiktokPopularCreatorsResponse402
    | TiktokPopularCreatorsResponse403
    | TiktokPopularCreatorsResponse404
    | TiktokPopularCreatorsResponse429
    | TiktokPopularCreatorsResponse500
    | TiktokPopularCreatorsResponse503
    | None
):
    r"""Fetch popular TikTok creators

     Fetches a list of popular TikTok creators. Optionally filter by country and sort order.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TiktokPopularCreatorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TiktokPopularCreatorsResponse200 | TiktokPopularCreatorsResponse400 | TiktokPopularCreatorsResponse401 | TiktokPopularCreatorsResponse402 | TiktokPopularCreatorsResponse403 | TiktokPopularCreatorsResponse404 | TiktokPopularCreatorsResponse429 | TiktokPopularCreatorsResponse500 | TiktokPopularCreatorsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
