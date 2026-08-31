from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_auto_topup_settings_body import UpdateAutoTopupSettingsBody
from ...models.update_auto_topup_settings_response_200 import UpdateAutoTopupSettingsResponse200
from ...models.update_auto_topup_settings_response_400 import UpdateAutoTopupSettingsResponse400
from ...models.update_auto_topup_settings_response_401 import UpdateAutoTopupSettingsResponse401
from ...models.update_auto_topup_settings_response_402 import UpdateAutoTopupSettingsResponse402
from ...models.update_auto_topup_settings_response_403 import UpdateAutoTopupSettingsResponse403
from ...models.update_auto_topup_settings_response_404 import UpdateAutoTopupSettingsResponse404
from ...models.update_auto_topup_settings_response_422 import UpdateAutoTopupSettingsResponse422
from ...models.update_auto_topup_settings_response_429 import UpdateAutoTopupSettingsResponse429
from ...models.update_auto_topup_settings_response_500 import UpdateAutoTopupSettingsResponse500
from ...models.update_auto_topup_settings_response_503 import UpdateAutoTopupSettingsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateAutoTopupSettingsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auto-topup/configure",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateAutoTopupSettingsResponse200
    | UpdateAutoTopupSettingsResponse400
    | UpdateAutoTopupSettingsResponse401
    | UpdateAutoTopupSettingsResponse402
    | UpdateAutoTopupSettingsResponse403
    | UpdateAutoTopupSettingsResponse404
    | UpdateAutoTopupSettingsResponse422
    | UpdateAutoTopupSettingsResponse429
    | UpdateAutoTopupSettingsResponse500
    | UpdateAutoTopupSettingsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = UpdateAutoTopupSettingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateAutoTopupSettingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateAutoTopupSettingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = UpdateAutoTopupSettingsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = UpdateAutoTopupSettingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateAutoTopupSettingsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = UpdateAutoTopupSettingsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = UpdateAutoTopupSettingsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateAutoTopupSettingsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateAutoTopupSettingsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateAutoTopupSettingsResponse200
    | UpdateAutoTopupSettingsResponse400
    | UpdateAutoTopupSettingsResponse401
    | UpdateAutoTopupSettingsResponse402
    | UpdateAutoTopupSettingsResponse403
    | UpdateAutoTopupSettingsResponse404
    | UpdateAutoTopupSettingsResponse422
    | UpdateAutoTopupSettingsResponse429
    | UpdateAutoTopupSettingsResponse500
    | UpdateAutoTopupSettingsResponse503
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
    body: UpdateAutoTopupSettingsBody,
) -> Response[
    UpdateAutoTopupSettingsResponse200
    | UpdateAutoTopupSettingsResponse400
    | UpdateAutoTopupSettingsResponse401
    | UpdateAutoTopupSettingsResponse402
    | UpdateAutoTopupSettingsResponse403
    | UpdateAutoTopupSettingsResponse404
    | UpdateAutoTopupSettingsResponse422
    | UpdateAutoTopupSettingsResponse429
    | UpdateAutoTopupSettingsResponse500
    | UpdateAutoTopupSettingsResponse503
]:
    """Update auto top-up settings

     Update the organization's auto top-up configuration. Enabling auto top-up will automatically charge
    your organization's saved payment method via Stripe when your credit balance falls below the
    configured threshold. AI agents should confirm with a human operator before enabling this feature.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateAutoTopupSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAutoTopupSettingsResponse200 | UpdateAutoTopupSettingsResponse400 | UpdateAutoTopupSettingsResponse401 | UpdateAutoTopupSettingsResponse402 | UpdateAutoTopupSettingsResponse403 | UpdateAutoTopupSettingsResponse404 | UpdateAutoTopupSettingsResponse422 | UpdateAutoTopupSettingsResponse429 | UpdateAutoTopupSettingsResponse500 | UpdateAutoTopupSettingsResponse503]
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
    body: UpdateAutoTopupSettingsBody,
) -> (
    UpdateAutoTopupSettingsResponse200
    | UpdateAutoTopupSettingsResponse400
    | UpdateAutoTopupSettingsResponse401
    | UpdateAutoTopupSettingsResponse402
    | UpdateAutoTopupSettingsResponse403
    | UpdateAutoTopupSettingsResponse404
    | UpdateAutoTopupSettingsResponse422
    | UpdateAutoTopupSettingsResponse429
    | UpdateAutoTopupSettingsResponse500
    | UpdateAutoTopupSettingsResponse503
    | None
):
    """Update auto top-up settings

     Update the organization's auto top-up configuration. Enabling auto top-up will automatically charge
    your organization's saved payment method via Stripe when your credit balance falls below the
    configured threshold. AI agents should confirm with a human operator before enabling this feature.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateAutoTopupSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAutoTopupSettingsResponse200 | UpdateAutoTopupSettingsResponse400 | UpdateAutoTopupSettingsResponse401 | UpdateAutoTopupSettingsResponse402 | UpdateAutoTopupSettingsResponse403 | UpdateAutoTopupSettingsResponse404 | UpdateAutoTopupSettingsResponse422 | UpdateAutoTopupSettingsResponse429 | UpdateAutoTopupSettingsResponse500 | UpdateAutoTopupSettingsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAutoTopupSettingsBody,
) -> Response[
    UpdateAutoTopupSettingsResponse200
    | UpdateAutoTopupSettingsResponse400
    | UpdateAutoTopupSettingsResponse401
    | UpdateAutoTopupSettingsResponse402
    | UpdateAutoTopupSettingsResponse403
    | UpdateAutoTopupSettingsResponse404
    | UpdateAutoTopupSettingsResponse422
    | UpdateAutoTopupSettingsResponse429
    | UpdateAutoTopupSettingsResponse500
    | UpdateAutoTopupSettingsResponse503
]:
    """Update auto top-up settings

     Update the organization's auto top-up configuration. Enabling auto top-up will automatically charge
    your organization's saved payment method via Stripe when your credit balance falls below the
    configured threshold. AI agents should confirm with a human operator before enabling this feature.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateAutoTopupSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAutoTopupSettingsResponse200 | UpdateAutoTopupSettingsResponse400 | UpdateAutoTopupSettingsResponse401 | UpdateAutoTopupSettingsResponse402 | UpdateAutoTopupSettingsResponse403 | UpdateAutoTopupSettingsResponse404 | UpdateAutoTopupSettingsResponse422 | UpdateAutoTopupSettingsResponse429 | UpdateAutoTopupSettingsResponse500 | UpdateAutoTopupSettingsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAutoTopupSettingsBody,
) -> (
    UpdateAutoTopupSettingsResponse200
    | UpdateAutoTopupSettingsResponse400
    | UpdateAutoTopupSettingsResponse401
    | UpdateAutoTopupSettingsResponse402
    | UpdateAutoTopupSettingsResponse403
    | UpdateAutoTopupSettingsResponse404
    | UpdateAutoTopupSettingsResponse422
    | UpdateAutoTopupSettingsResponse429
    | UpdateAutoTopupSettingsResponse500
    | UpdateAutoTopupSettingsResponse503
    | None
):
    """Update auto top-up settings

     Update the organization's auto top-up configuration. Enabling auto top-up will automatically charge
    your organization's saved payment method via Stripe when your credit balance falls below the
    configured threshold. AI agents should confirm with a human operator before enabling this feature.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateAutoTopupSettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAutoTopupSettingsResponse200 | UpdateAutoTopupSettingsResponse400 | UpdateAutoTopupSettingsResponse401 | UpdateAutoTopupSettingsResponse402 | UpdateAutoTopupSettingsResponse403 | UpdateAutoTopupSettingsResponse404 | UpdateAutoTopupSettingsResponse422 | UpdateAutoTopupSettingsResponse429 | UpdateAutoTopupSettingsResponse500 | UpdateAutoTopupSettingsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
