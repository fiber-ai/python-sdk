from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhook_endpoints_response_200 import ListWebhookEndpointsResponse200
from ...models.list_webhook_endpoints_response_400 import ListWebhookEndpointsResponse400
from ...models.list_webhook_endpoints_response_401 import ListWebhookEndpointsResponse401
from ...models.list_webhook_endpoints_response_402 import ListWebhookEndpointsResponse402
from ...models.list_webhook_endpoints_response_403 import ListWebhookEndpointsResponse403
from ...models.list_webhook_endpoints_response_404 import ListWebhookEndpointsResponse404
from ...models.list_webhook_endpoints_response_422 import ListWebhookEndpointsResponse422
from ...models.list_webhook_endpoints_response_429 import ListWebhookEndpointsResponse429
from ...models.list_webhook_endpoints_response_500 import ListWebhookEndpointsResponse500
from ...models.list_webhook_endpoints_response_503 import ListWebhookEndpointsResponse503
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
        "url": "/v1/webhooks/endpoints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListWebhookEndpointsResponse200
    | ListWebhookEndpointsResponse400
    | ListWebhookEndpointsResponse401
    | ListWebhookEndpointsResponse402
    | ListWebhookEndpointsResponse403
    | ListWebhookEndpointsResponse404
    | ListWebhookEndpointsResponse422
    | ListWebhookEndpointsResponse429
    | ListWebhookEndpointsResponse500
    | ListWebhookEndpointsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListWebhookEndpointsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListWebhookEndpointsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListWebhookEndpointsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListWebhookEndpointsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListWebhookEndpointsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListWebhookEndpointsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ListWebhookEndpointsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ListWebhookEndpointsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListWebhookEndpointsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListWebhookEndpointsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListWebhookEndpointsResponse200
    | ListWebhookEndpointsResponse400
    | ListWebhookEndpointsResponse401
    | ListWebhookEndpointsResponse402
    | ListWebhookEndpointsResponse403
    | ListWebhookEndpointsResponse404
    | ListWebhookEndpointsResponse422
    | ListWebhookEndpointsResponse429
    | ListWebhookEndpointsResponse500
    | ListWebhookEndpointsResponse503
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
    ListWebhookEndpointsResponse200
    | ListWebhookEndpointsResponse400
    | ListWebhookEndpointsResponse401
    | ListWebhookEndpointsResponse402
    | ListWebhookEndpointsResponse403
    | ListWebhookEndpointsResponse404
    | ListWebhookEndpointsResponse422
    | ListWebhookEndpointsResponse429
    | ListWebhookEndpointsResponse500
    | ListWebhookEndpointsResponse503
]:
    r"""List webhook endpoints

     List every webhook endpoint configured for your organization, including each endpoint's delivery
    URL, subscribed event types, and paused state. Reading webhook endpoints is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookEndpointsResponse200 | ListWebhookEndpointsResponse400 | ListWebhookEndpointsResponse401 | ListWebhookEndpointsResponse402 | ListWebhookEndpointsResponse403 | ListWebhookEndpointsResponse404 | ListWebhookEndpointsResponse422 | ListWebhookEndpointsResponse429 | ListWebhookEndpointsResponse500 | ListWebhookEndpointsResponse503]
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
    ListWebhookEndpointsResponse200
    | ListWebhookEndpointsResponse400
    | ListWebhookEndpointsResponse401
    | ListWebhookEndpointsResponse402
    | ListWebhookEndpointsResponse403
    | ListWebhookEndpointsResponse404
    | ListWebhookEndpointsResponse422
    | ListWebhookEndpointsResponse429
    | ListWebhookEndpointsResponse500
    | ListWebhookEndpointsResponse503
    | None
):
    r"""List webhook endpoints

     List every webhook endpoint configured for your organization, including each endpoint's delivery
    URL, subscribed event types, and paused state. Reading webhook endpoints is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookEndpointsResponse200 | ListWebhookEndpointsResponse400 | ListWebhookEndpointsResponse401 | ListWebhookEndpointsResponse402 | ListWebhookEndpointsResponse403 | ListWebhookEndpointsResponse404 | ListWebhookEndpointsResponse422 | ListWebhookEndpointsResponse429 | ListWebhookEndpointsResponse500 | ListWebhookEndpointsResponse503
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
    ListWebhookEndpointsResponse200
    | ListWebhookEndpointsResponse400
    | ListWebhookEndpointsResponse401
    | ListWebhookEndpointsResponse402
    | ListWebhookEndpointsResponse403
    | ListWebhookEndpointsResponse404
    | ListWebhookEndpointsResponse422
    | ListWebhookEndpointsResponse429
    | ListWebhookEndpointsResponse500
    | ListWebhookEndpointsResponse503
]:
    r"""List webhook endpoints

     List every webhook endpoint configured for your organization, including each endpoint's delivery
    URL, subscribed event types, and paused state. Reading webhook endpoints is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookEndpointsResponse200 | ListWebhookEndpointsResponse400 | ListWebhookEndpointsResponse401 | ListWebhookEndpointsResponse402 | ListWebhookEndpointsResponse403 | ListWebhookEndpointsResponse404 | ListWebhookEndpointsResponse422 | ListWebhookEndpointsResponse429 | ListWebhookEndpointsResponse500 | ListWebhookEndpointsResponse503]
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
    ListWebhookEndpointsResponse200
    | ListWebhookEndpointsResponse400
    | ListWebhookEndpointsResponse401
    | ListWebhookEndpointsResponse402
    | ListWebhookEndpointsResponse403
    | ListWebhookEndpointsResponse404
    | ListWebhookEndpointsResponse422
    | ListWebhookEndpointsResponse429
    | ListWebhookEndpointsResponse500
    | ListWebhookEndpointsResponse503
    | None
):
    r"""List webhook endpoints

     List every webhook endpoint configured for your organization, including each endpoint's delivery
    URL, subscribed event types, and paused state. Reading webhook endpoints is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookEndpointsResponse200 | ListWebhookEndpointsResponse400 | ListWebhookEndpointsResponse401 | ListWebhookEndpointsResponse402 | ListWebhookEndpointsResponse403 | ListWebhookEndpointsResponse404 | ListWebhookEndpointsResponse422 | ListWebhookEndpointsResponse429 | ListWebhookEndpointsResponse500 | ListWebhookEndpointsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
