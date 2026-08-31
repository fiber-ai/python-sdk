from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_test_webhook_event_body import SendTestWebhookEventBody
from ...models.send_test_webhook_event_response_200 import SendTestWebhookEventResponse200
from ...models.send_test_webhook_event_response_400 import SendTestWebhookEventResponse400
from ...models.send_test_webhook_event_response_401 import SendTestWebhookEventResponse401
from ...models.send_test_webhook_event_response_402 import SendTestWebhookEventResponse402
from ...models.send_test_webhook_event_response_403 import SendTestWebhookEventResponse403
from ...models.send_test_webhook_event_response_404 import SendTestWebhookEventResponse404
from ...models.send_test_webhook_event_response_422 import SendTestWebhookEventResponse422
from ...models.send_test_webhook_event_response_429 import SendTestWebhookEventResponse429
from ...models.send_test_webhook_event_response_500 import SendTestWebhookEventResponse500
from ...models.send_test_webhook_event_response_503 import SendTestWebhookEventResponse503
from ...types import Response


def _get_kwargs(
    endpoint_id: str,
    *,
    body: SendTestWebhookEventBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/endpoints/{endpoint_id}/test-event".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SendTestWebhookEventResponse200
    | SendTestWebhookEventResponse400
    | SendTestWebhookEventResponse401
    | SendTestWebhookEventResponse402
    | SendTestWebhookEventResponse403
    | SendTestWebhookEventResponse404
    | SendTestWebhookEventResponse422
    | SendTestWebhookEventResponse429
    | SendTestWebhookEventResponse500
    | SendTestWebhookEventResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SendTestWebhookEventResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SendTestWebhookEventResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SendTestWebhookEventResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SendTestWebhookEventResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SendTestWebhookEventResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SendTestWebhookEventResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = SendTestWebhookEventResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = SendTestWebhookEventResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SendTestWebhookEventResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SendTestWebhookEventResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SendTestWebhookEventResponse200
    | SendTestWebhookEventResponse400
    | SendTestWebhookEventResponse401
    | SendTestWebhookEventResponse402
    | SendTestWebhookEventResponse403
    | SendTestWebhookEventResponse404
    | SendTestWebhookEventResponse422
    | SendTestWebhookEventResponse429
    | SendTestWebhookEventResponse500
    | SendTestWebhookEventResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendTestWebhookEventBody,
) -> Response[
    SendTestWebhookEventResponse200
    | SendTestWebhookEventResponse400
    | SendTestWebhookEventResponse401
    | SendTestWebhookEventResponse402
    | SendTestWebhookEventResponse403
    | SendTestWebhookEventResponse404
    | SendTestWebhookEventResponse422
    | SendTestWebhookEventResponse429
    | SendTestWebhookEventResponse500
    | SendTestWebhookEventResponse503
]:
    """Send test webhook event

     Send an example payload of the given event type to a single webhook endpoint. Use this to verify
    your receiver accepts deliveries and parses payloads correctly before relying on real events.
    Sending test events is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (SendTestWebhookEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendTestWebhookEventResponse200 | SendTestWebhookEventResponse400 | SendTestWebhookEventResponse401 | SendTestWebhookEventResponse402 | SendTestWebhookEventResponse403 | SendTestWebhookEventResponse404 | SendTestWebhookEventResponse422 | SendTestWebhookEventResponse429 | SendTestWebhookEventResponse500 | SendTestWebhookEventResponse503]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendTestWebhookEventBody,
) -> (
    SendTestWebhookEventResponse200
    | SendTestWebhookEventResponse400
    | SendTestWebhookEventResponse401
    | SendTestWebhookEventResponse402
    | SendTestWebhookEventResponse403
    | SendTestWebhookEventResponse404
    | SendTestWebhookEventResponse422
    | SendTestWebhookEventResponse429
    | SendTestWebhookEventResponse500
    | SendTestWebhookEventResponse503
    | None
):
    """Send test webhook event

     Send an example payload of the given event type to a single webhook endpoint. Use this to verify
    your receiver accepts deliveries and parses payloads correctly before relying on real events.
    Sending test events is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (SendTestWebhookEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendTestWebhookEventResponse200 | SendTestWebhookEventResponse400 | SendTestWebhookEventResponse401 | SendTestWebhookEventResponse402 | SendTestWebhookEventResponse403 | SendTestWebhookEventResponse404 | SendTestWebhookEventResponse422 | SendTestWebhookEventResponse429 | SendTestWebhookEventResponse500 | SendTestWebhookEventResponse503
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendTestWebhookEventBody,
) -> Response[
    SendTestWebhookEventResponse200
    | SendTestWebhookEventResponse400
    | SendTestWebhookEventResponse401
    | SendTestWebhookEventResponse402
    | SendTestWebhookEventResponse403
    | SendTestWebhookEventResponse404
    | SendTestWebhookEventResponse422
    | SendTestWebhookEventResponse429
    | SendTestWebhookEventResponse500
    | SendTestWebhookEventResponse503
]:
    """Send test webhook event

     Send an example payload of the given event type to a single webhook endpoint. Use this to verify
    your receiver accepts deliveries and parses payloads correctly before relying on real events.
    Sending test events is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (SendTestWebhookEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendTestWebhookEventResponse200 | SendTestWebhookEventResponse400 | SendTestWebhookEventResponse401 | SendTestWebhookEventResponse402 | SendTestWebhookEventResponse403 | SendTestWebhookEventResponse404 | SendTestWebhookEventResponse422 | SendTestWebhookEventResponse429 | SendTestWebhookEventResponse500 | SendTestWebhookEventResponse503]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendTestWebhookEventBody,
) -> (
    SendTestWebhookEventResponse200
    | SendTestWebhookEventResponse400
    | SendTestWebhookEventResponse401
    | SendTestWebhookEventResponse402
    | SendTestWebhookEventResponse403
    | SendTestWebhookEventResponse404
    | SendTestWebhookEventResponse422
    | SendTestWebhookEventResponse429
    | SendTestWebhookEventResponse500
    | SendTestWebhookEventResponse503
    | None
):
    """Send test webhook event

     Send an example payload of the given event type to a single webhook endpoint. Use this to verify
    your receiver accepts deliveries and parses payloads correctly before relying on real events.
    Sending test events is free.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        endpoint_id (str):
        body (SendTestWebhookEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendTestWebhookEventResponse200 | SendTestWebhookEventResponse400 | SendTestWebhookEventResponse401 | SendTestWebhookEventResponse402 | SendTestWebhookEventResponse403 | SendTestWebhookEventResponse404 | SendTestWebhookEventResponse422 | SendTestWebhookEventResponse429 | SendTestWebhookEventResponse500 | SendTestWebhookEventResponse503
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            client=client,
            body=body,
        )
    ).parsed
