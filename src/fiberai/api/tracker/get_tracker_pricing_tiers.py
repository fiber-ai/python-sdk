from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tracker_pricing_tiers_response_200 import GetTrackerPricingTiersResponse200
from ...models.get_tracker_pricing_tiers_response_400 import GetTrackerPricingTiersResponse400
from ...models.get_tracker_pricing_tiers_response_401 import GetTrackerPricingTiersResponse401
from ...models.get_tracker_pricing_tiers_response_402 import GetTrackerPricingTiersResponse402
from ...models.get_tracker_pricing_tiers_response_403 import GetTrackerPricingTiersResponse403
from ...models.get_tracker_pricing_tiers_response_404 import GetTrackerPricingTiersResponse404
from ...models.get_tracker_pricing_tiers_response_422 import GetTrackerPricingTiersResponse422
from ...models.get_tracker_pricing_tiers_response_429 import GetTrackerPricingTiersResponse429
from ...models.get_tracker_pricing_tiers_response_500 import GetTrackerPricingTiersResponse500
from ...models.get_tracker_pricing_tiers_response_503 import GetTrackerPricingTiersResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    api_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tracker/pricing-tiers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetTrackerPricingTiersResponse200
    | GetTrackerPricingTiersResponse400
    | GetTrackerPricingTiersResponse401
    | GetTrackerPricingTiersResponse402
    | GetTrackerPricingTiersResponse403
    | GetTrackerPricingTiersResponse404
    | GetTrackerPricingTiersResponse422
    | GetTrackerPricingTiersResponse429
    | GetTrackerPricingTiersResponse500
    | GetTrackerPricingTiersResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetTrackerPricingTiersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetTrackerPricingTiersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetTrackerPricingTiersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetTrackerPricingTiersResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetTrackerPricingTiersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTrackerPricingTiersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetTrackerPricingTiersResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetTrackerPricingTiersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetTrackerPricingTiersResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetTrackerPricingTiersResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetTrackerPricingTiersResponse200
    | GetTrackerPricingTiersResponse400
    | GetTrackerPricingTiersResponse401
    | GetTrackerPricingTiersResponse402
    | GetTrackerPricingTiersResponse403
    | GetTrackerPricingTiersResponse404
    | GetTrackerPricingTiersResponse422
    | GetTrackerPricingTiersResponse429
    | GetTrackerPricingTiersResponse500
    | GetTrackerPricingTiersResponse503
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
    api_key: str,
) -> Response[
    GetTrackerPricingTiersResponse200
    | GetTrackerPricingTiersResponse400
    | GetTrackerPricingTiersResponse401
    | GetTrackerPricingTiersResponse402
    | GetTrackerPricingTiersResponse403
    | GetTrackerPricingTiersResponse404
    | GetTrackerPricingTiersResponse422
    | GetTrackerPricingTiersResponse429
    | GetTrackerPricingTiersResponse500
    | GetTrackerPricingTiersResponse503
]:
    """Explain your tracker pricing tiers

     Returns the pricing tier each of your tracker lists will be billed at on its next scheduled refresh,
    with the per-entity cost, the two criteria that decided the tier, and the one change that would move
    each list to a cheaper tier. Tiers depend on how many companies and people your organization tracks
    in total and on each list's refresh cadence.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTrackerPricingTiersResponse200 | GetTrackerPricingTiersResponse400 | GetTrackerPricingTiersResponse401 | GetTrackerPricingTiersResponse402 | GetTrackerPricingTiersResponse403 | GetTrackerPricingTiersResponse404 | GetTrackerPricingTiersResponse422 | GetTrackerPricingTiersResponse429 | GetTrackerPricingTiersResponse500 | GetTrackerPricingTiersResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetTrackerPricingTiersResponse200
    | GetTrackerPricingTiersResponse400
    | GetTrackerPricingTiersResponse401
    | GetTrackerPricingTiersResponse402
    | GetTrackerPricingTiersResponse403
    | GetTrackerPricingTiersResponse404
    | GetTrackerPricingTiersResponse422
    | GetTrackerPricingTiersResponse429
    | GetTrackerPricingTiersResponse500
    | GetTrackerPricingTiersResponse503
    | None
):
    """Explain your tracker pricing tiers

     Returns the pricing tier each of your tracker lists will be billed at on its next scheduled refresh,
    with the per-entity cost, the two criteria that decided the tier, and the one change that would move
    each list to a cheaper tier. Tiers depend on how many companies and people your organization tracks
    in total and on each list's refresh cadence.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTrackerPricingTiersResponse200 | GetTrackerPricingTiersResponse400 | GetTrackerPricingTiersResponse401 | GetTrackerPricingTiersResponse402 | GetTrackerPricingTiersResponse403 | GetTrackerPricingTiersResponse404 | GetTrackerPricingTiersResponse422 | GetTrackerPricingTiersResponse429 | GetTrackerPricingTiersResponse500 | GetTrackerPricingTiersResponse503
    """

    return sync_detailed(
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    GetTrackerPricingTiersResponse200
    | GetTrackerPricingTiersResponse400
    | GetTrackerPricingTiersResponse401
    | GetTrackerPricingTiersResponse402
    | GetTrackerPricingTiersResponse403
    | GetTrackerPricingTiersResponse404
    | GetTrackerPricingTiersResponse422
    | GetTrackerPricingTiersResponse429
    | GetTrackerPricingTiersResponse500
    | GetTrackerPricingTiersResponse503
]:
    """Explain your tracker pricing tiers

     Returns the pricing tier each of your tracker lists will be billed at on its next scheduled refresh,
    with the per-entity cost, the two criteria that decided the tier, and the one change that would move
    each list to a cheaper tier. Tiers depend on how many companies and people your organization tracks
    in total and on each list's refresh cadence.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTrackerPricingTiersResponse200 | GetTrackerPricingTiersResponse400 | GetTrackerPricingTiersResponse401 | GetTrackerPricingTiersResponse402 | GetTrackerPricingTiersResponse403 | GetTrackerPricingTiersResponse404 | GetTrackerPricingTiersResponse422 | GetTrackerPricingTiersResponse429 | GetTrackerPricingTiersResponse500 | GetTrackerPricingTiersResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetTrackerPricingTiersResponse200
    | GetTrackerPricingTiersResponse400
    | GetTrackerPricingTiersResponse401
    | GetTrackerPricingTiersResponse402
    | GetTrackerPricingTiersResponse403
    | GetTrackerPricingTiersResponse404
    | GetTrackerPricingTiersResponse422
    | GetTrackerPricingTiersResponse429
    | GetTrackerPricingTiersResponse500
    | GetTrackerPricingTiersResponse503
    | None
):
    """Explain your tracker pricing tiers

     Returns the pricing tier each of your tracker lists will be billed at on its next scheduled refresh,
    with the per-entity cost, the two criteria that decided the tier, and the one change that would move
    each list to a cheaper tier. Tiers depend on how many companies and people your organization tracks
    in total and on each list's refresh cadence.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTrackerPricingTiersResponse200 | GetTrackerPricingTiersResponse400 | GetTrackerPricingTiersResponse401 | GetTrackerPricingTiersResponse402 | GetTrackerPricingTiersResponse403 | GetTrackerPricingTiersResponse404 | GetTrackerPricingTiersResponse422 | GetTrackerPricingTiersResponse429 | GetTrackerPricingTiersResponse500 | GetTrackerPricingTiersResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
