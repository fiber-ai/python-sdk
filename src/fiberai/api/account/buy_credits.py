from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.buy_credits_body import BuyCreditsBody
from ...models.buy_credits_response_200 import BuyCreditsResponse200
from ...models.buy_credits_response_400 import BuyCreditsResponse400
from ...models.buy_credits_response_401 import BuyCreditsResponse401
from ...models.buy_credits_response_402 import BuyCreditsResponse402
from ...models.buy_credits_response_403 import BuyCreditsResponse403
from ...models.buy_credits_response_404 import BuyCreditsResponse404
from ...models.buy_credits_response_422 import BuyCreditsResponse422
from ...models.buy_credits_response_429 import BuyCreditsResponse429
from ...models.buy_credits_response_500 import BuyCreditsResponse500
from ...models.buy_credits_response_503 import BuyCreditsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: BuyCreditsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/buy-credits",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BuyCreditsResponse200
    | BuyCreditsResponse400
    | BuyCreditsResponse401
    | BuyCreditsResponse402
    | BuyCreditsResponse403
    | BuyCreditsResponse404
    | BuyCreditsResponse422
    | BuyCreditsResponse429
    | BuyCreditsResponse500
    | BuyCreditsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = BuyCreditsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BuyCreditsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BuyCreditsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = BuyCreditsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = BuyCreditsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = BuyCreditsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = BuyCreditsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = BuyCreditsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = BuyCreditsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = BuyCreditsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BuyCreditsResponse200
    | BuyCreditsResponse400
    | BuyCreditsResponse401
    | BuyCreditsResponse402
    | BuyCreditsResponse403
    | BuyCreditsResponse404
    | BuyCreditsResponse422
    | BuyCreditsResponse429
    | BuyCreditsResponse500
    | BuyCreditsResponse503
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
    body: BuyCreditsBody,
) -> Response[
    BuyCreditsResponse200
    | BuyCreditsResponse400
    | BuyCreditsResponse401
    | BuyCreditsResponse402
    | BuyCreditsResponse403
    | BuyCreditsResponse404
    | BuyCreditsResponse422
    | BuyCreditsResponse429
    | BuyCreditsResponse500
    | BuyCreditsResponse503
]:
    """Buy credits

     Purchase additional credits for your organization at $20.00 per 1,000 credits. This endpoint
    immediately charges real money to your organization's saved payment method via Stripe. AI agents are
    strongly recommended to confirm with their human operator before calling this endpoint.

    <span>⚡ <strong>Rate limit:</strong> 2 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BuyCreditsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuyCreditsResponse200 | BuyCreditsResponse400 | BuyCreditsResponse401 | BuyCreditsResponse402 | BuyCreditsResponse403 | BuyCreditsResponse404 | BuyCreditsResponse422 | BuyCreditsResponse429 | BuyCreditsResponse500 | BuyCreditsResponse503]
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
    body: BuyCreditsBody,
) -> (
    BuyCreditsResponse200
    | BuyCreditsResponse400
    | BuyCreditsResponse401
    | BuyCreditsResponse402
    | BuyCreditsResponse403
    | BuyCreditsResponse404
    | BuyCreditsResponse422
    | BuyCreditsResponse429
    | BuyCreditsResponse500
    | BuyCreditsResponse503
    | None
):
    """Buy credits

     Purchase additional credits for your organization at $20.00 per 1,000 credits. This endpoint
    immediately charges real money to your organization's saved payment method via Stripe. AI agents are
    strongly recommended to confirm with their human operator before calling this endpoint.

    <span>⚡ <strong>Rate limit:</strong> 2 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BuyCreditsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuyCreditsResponse200 | BuyCreditsResponse400 | BuyCreditsResponse401 | BuyCreditsResponse402 | BuyCreditsResponse403 | BuyCreditsResponse404 | BuyCreditsResponse422 | BuyCreditsResponse429 | BuyCreditsResponse500 | BuyCreditsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BuyCreditsBody,
) -> Response[
    BuyCreditsResponse200
    | BuyCreditsResponse400
    | BuyCreditsResponse401
    | BuyCreditsResponse402
    | BuyCreditsResponse403
    | BuyCreditsResponse404
    | BuyCreditsResponse422
    | BuyCreditsResponse429
    | BuyCreditsResponse500
    | BuyCreditsResponse503
]:
    """Buy credits

     Purchase additional credits for your organization at $20.00 per 1,000 credits. This endpoint
    immediately charges real money to your organization's saved payment method via Stripe. AI agents are
    strongly recommended to confirm with their human operator before calling this endpoint.

    <span>⚡ <strong>Rate limit:</strong> 2 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BuyCreditsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuyCreditsResponse200 | BuyCreditsResponse400 | BuyCreditsResponse401 | BuyCreditsResponse402 | BuyCreditsResponse403 | BuyCreditsResponse404 | BuyCreditsResponse422 | BuyCreditsResponse429 | BuyCreditsResponse500 | BuyCreditsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BuyCreditsBody,
) -> (
    BuyCreditsResponse200
    | BuyCreditsResponse400
    | BuyCreditsResponse401
    | BuyCreditsResponse402
    | BuyCreditsResponse403
    | BuyCreditsResponse404
    | BuyCreditsResponse422
    | BuyCreditsResponse429
    | BuyCreditsResponse500
    | BuyCreditsResponse503
    | None
):
    """Buy credits

     Purchase additional credits for your organization at $20.00 per 1,000 credits. This endpoint
    immediately charges real money to your organization's saved payment method via Stripe. AI agents are
    strongly recommended to confirm with their human operator before calling this endpoint.

    <span>⚡ <strong>Rate limit:</strong> 2 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BuyCreditsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuyCreditsResponse200 | BuyCreditsResponse400 | BuyCreditsResponse401 | BuyCreditsResponse402 | BuyCreditsResponse403 | BuyCreditsResponse404 | BuyCreditsResponse422 | BuyCreditsResponse429 | BuyCreditsResponse500 | BuyCreditsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
