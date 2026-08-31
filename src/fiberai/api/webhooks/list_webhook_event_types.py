from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhook_event_types_response_200 import ListWebhookEventTypesResponse200
from ...models.list_webhook_event_types_response_400 import ListWebhookEventTypesResponse400
from ...models.list_webhook_event_types_response_401 import ListWebhookEventTypesResponse401
from ...models.list_webhook_event_types_response_402 import ListWebhookEventTypesResponse402
from ...models.list_webhook_event_types_response_403 import ListWebhookEventTypesResponse403
from ...models.list_webhook_event_types_response_404 import ListWebhookEventTypesResponse404
from ...models.list_webhook_event_types_response_422 import ListWebhookEventTypesResponse422
from ...models.list_webhook_event_types_response_429 import ListWebhookEventTypesResponse429
from ...models.list_webhook_event_types_response_500 import ListWebhookEventTypesResponse500
from ...models.list_webhook_event_types_response_503 import ListWebhookEventTypesResponse503
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
        "url": "/v1/webhooks/event-types",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListWebhookEventTypesResponse200
    | ListWebhookEventTypesResponse400
    | ListWebhookEventTypesResponse401
    | ListWebhookEventTypesResponse402
    | ListWebhookEventTypesResponse403
    | ListWebhookEventTypesResponse404
    | ListWebhookEventTypesResponse422
    | ListWebhookEventTypesResponse429
    | ListWebhookEventTypesResponse500
    | ListWebhookEventTypesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListWebhookEventTypesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListWebhookEventTypesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListWebhookEventTypesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListWebhookEventTypesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListWebhookEventTypesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListWebhookEventTypesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ListWebhookEventTypesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ListWebhookEventTypesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListWebhookEventTypesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListWebhookEventTypesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListWebhookEventTypesResponse200
    | ListWebhookEventTypesResponse400
    | ListWebhookEventTypesResponse401
    | ListWebhookEventTypesResponse402
    | ListWebhookEventTypesResponse403
    | ListWebhookEventTypesResponse404
    | ListWebhookEventTypesResponse422
    | ListWebhookEventTypesResponse429
    | ListWebhookEventTypesResponse500
    | ListWebhookEventTypesResponse503
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
    ListWebhookEventTypesResponse200
    | ListWebhookEventTypesResponse400
    | ListWebhookEventTypesResponse401
    | ListWebhookEventTypesResponse402
    | ListWebhookEventTypesResponse403
    | ListWebhookEventTypesResponse404
    | ListWebhookEventTypesResponse422
    | ListWebhookEventTypesResponse429
    | ListWebhookEventTypesResponse500
    | ListWebhookEventTypesResponse503
]:
    """List webhook event types

     List every event type you can subscribe a webhook endpoint to. Each entry includes a description of
    when the event fires and an example payload so you can build and test your receiver before creating
    an endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookEventTypesResponse200 | ListWebhookEventTypesResponse400 | ListWebhookEventTypesResponse401 | ListWebhookEventTypesResponse402 | ListWebhookEventTypesResponse403 | ListWebhookEventTypesResponse404 | ListWebhookEventTypesResponse422 | ListWebhookEventTypesResponse429 | ListWebhookEventTypesResponse500 | ListWebhookEventTypesResponse503]
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
    ListWebhookEventTypesResponse200
    | ListWebhookEventTypesResponse400
    | ListWebhookEventTypesResponse401
    | ListWebhookEventTypesResponse402
    | ListWebhookEventTypesResponse403
    | ListWebhookEventTypesResponse404
    | ListWebhookEventTypesResponse422
    | ListWebhookEventTypesResponse429
    | ListWebhookEventTypesResponse500
    | ListWebhookEventTypesResponse503
    | None
):
    """List webhook event types

     List every event type you can subscribe a webhook endpoint to. Each entry includes a description of
    when the event fires and an example payload so you can build and test your receiver before creating
    an endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookEventTypesResponse200 | ListWebhookEventTypesResponse400 | ListWebhookEventTypesResponse401 | ListWebhookEventTypesResponse402 | ListWebhookEventTypesResponse403 | ListWebhookEventTypesResponse404 | ListWebhookEventTypesResponse422 | ListWebhookEventTypesResponse429 | ListWebhookEventTypesResponse500 | ListWebhookEventTypesResponse503
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
    ListWebhookEventTypesResponse200
    | ListWebhookEventTypesResponse400
    | ListWebhookEventTypesResponse401
    | ListWebhookEventTypesResponse402
    | ListWebhookEventTypesResponse403
    | ListWebhookEventTypesResponse404
    | ListWebhookEventTypesResponse422
    | ListWebhookEventTypesResponse429
    | ListWebhookEventTypesResponse500
    | ListWebhookEventTypesResponse503
]:
    """List webhook event types

     List every event type you can subscribe a webhook endpoint to. Each entry includes a description of
    when the event fires and an example payload so you can build and test your receiver before creating
    an endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookEventTypesResponse200 | ListWebhookEventTypesResponse400 | ListWebhookEventTypesResponse401 | ListWebhookEventTypesResponse402 | ListWebhookEventTypesResponse403 | ListWebhookEventTypesResponse404 | ListWebhookEventTypesResponse422 | ListWebhookEventTypesResponse429 | ListWebhookEventTypesResponse500 | ListWebhookEventTypesResponse503]
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
    ListWebhookEventTypesResponse200
    | ListWebhookEventTypesResponse400
    | ListWebhookEventTypesResponse401
    | ListWebhookEventTypesResponse402
    | ListWebhookEventTypesResponse403
    | ListWebhookEventTypesResponse404
    | ListWebhookEventTypesResponse422
    | ListWebhookEventTypesResponse429
    | ListWebhookEventTypesResponse500
    | ListWebhookEventTypesResponse503
    | None
):
    """List webhook event types

     List every event type you can subscribe a webhook endpoint to. Each entry includes a description of
    when the event fires and an example payload so you can build and test your receiver before creating
    an endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookEventTypesResponse200 | ListWebhookEventTypesResponse400 | ListWebhookEventTypesResponse401 | ListWebhookEventTypesResponse402 | ListWebhookEventTypesResponse403 | ListWebhookEventTypesResponse404 | ListWebhookEventTypesResponse422 | ListWebhookEventTypesResponse429 | ListWebhookEventTypesResponse500 | ListWebhookEventTypesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
