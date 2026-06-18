from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_auto_topup_settings_response_200 import GetAutoTopupSettingsResponse200
from ...models.get_auto_topup_settings_response_400 import GetAutoTopupSettingsResponse400
from ...models.get_auto_topup_settings_response_401 import GetAutoTopupSettingsResponse401
from ...models.get_auto_topup_settings_response_402 import GetAutoTopupSettingsResponse402
from ...models.get_auto_topup_settings_response_403 import GetAutoTopupSettingsResponse403
from ...models.get_auto_topup_settings_response_404 import GetAutoTopupSettingsResponse404
from ...models.get_auto_topup_settings_response_422 import GetAutoTopupSettingsResponse422
from ...models.get_auto_topup_settings_response_429 import GetAutoTopupSettingsResponse429
from ...models.get_auto_topup_settings_response_500 import GetAutoTopupSettingsResponse500
from ...models.get_auto_topup_settings_response_503 import GetAutoTopupSettingsResponse503
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
        "url": "/v1/auto-topup/settings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAutoTopupSettingsResponse200
    | GetAutoTopupSettingsResponse400
    | GetAutoTopupSettingsResponse401
    | GetAutoTopupSettingsResponse402
    | GetAutoTopupSettingsResponse403
    | GetAutoTopupSettingsResponse404
    | GetAutoTopupSettingsResponse422
    | GetAutoTopupSettingsResponse429
    | GetAutoTopupSettingsResponse500
    | GetAutoTopupSettingsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetAutoTopupSettingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAutoTopupSettingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAutoTopupSettingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetAutoTopupSettingsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetAutoTopupSettingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAutoTopupSettingsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetAutoTopupSettingsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetAutoTopupSettingsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAutoTopupSettingsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAutoTopupSettingsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAutoTopupSettingsResponse200
    | GetAutoTopupSettingsResponse400
    | GetAutoTopupSettingsResponse401
    | GetAutoTopupSettingsResponse402
    | GetAutoTopupSettingsResponse403
    | GetAutoTopupSettingsResponse404
    | GetAutoTopupSettingsResponse422
    | GetAutoTopupSettingsResponse429
    | GetAutoTopupSettingsResponse500
    | GetAutoTopupSettingsResponse503
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
    GetAutoTopupSettingsResponse200
    | GetAutoTopupSettingsResponse400
    | GetAutoTopupSettingsResponse401
    | GetAutoTopupSettingsResponse402
    | GetAutoTopupSettingsResponse403
    | GetAutoTopupSettingsResponse404
    | GetAutoTopupSettingsResponse422
    | GetAutoTopupSettingsResponse429
    | GetAutoTopupSettingsResponse500
    | GetAutoTopupSettingsResponse503
]:
    r"""Get auto top-up settings

     Get the organization's auto top-up configuration. When configured is false, no auto top-up settings
    exist yet.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAutoTopupSettingsResponse200 | GetAutoTopupSettingsResponse400 | GetAutoTopupSettingsResponse401 | GetAutoTopupSettingsResponse402 | GetAutoTopupSettingsResponse403 | GetAutoTopupSettingsResponse404 | GetAutoTopupSettingsResponse422 | GetAutoTopupSettingsResponse429 | GetAutoTopupSettingsResponse500 | GetAutoTopupSettingsResponse503]
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
    GetAutoTopupSettingsResponse200
    | GetAutoTopupSettingsResponse400
    | GetAutoTopupSettingsResponse401
    | GetAutoTopupSettingsResponse402
    | GetAutoTopupSettingsResponse403
    | GetAutoTopupSettingsResponse404
    | GetAutoTopupSettingsResponse422
    | GetAutoTopupSettingsResponse429
    | GetAutoTopupSettingsResponse500
    | GetAutoTopupSettingsResponse503
    | None
):
    r"""Get auto top-up settings

     Get the organization's auto top-up configuration. When configured is false, no auto top-up settings
    exist yet.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAutoTopupSettingsResponse200 | GetAutoTopupSettingsResponse400 | GetAutoTopupSettingsResponse401 | GetAutoTopupSettingsResponse402 | GetAutoTopupSettingsResponse403 | GetAutoTopupSettingsResponse404 | GetAutoTopupSettingsResponse422 | GetAutoTopupSettingsResponse429 | GetAutoTopupSettingsResponse500 | GetAutoTopupSettingsResponse503
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
    GetAutoTopupSettingsResponse200
    | GetAutoTopupSettingsResponse400
    | GetAutoTopupSettingsResponse401
    | GetAutoTopupSettingsResponse402
    | GetAutoTopupSettingsResponse403
    | GetAutoTopupSettingsResponse404
    | GetAutoTopupSettingsResponse422
    | GetAutoTopupSettingsResponse429
    | GetAutoTopupSettingsResponse500
    | GetAutoTopupSettingsResponse503
]:
    r"""Get auto top-up settings

     Get the organization's auto top-up configuration. When configured is false, no auto top-up settings
    exist yet.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAutoTopupSettingsResponse200 | GetAutoTopupSettingsResponse400 | GetAutoTopupSettingsResponse401 | GetAutoTopupSettingsResponse402 | GetAutoTopupSettingsResponse403 | GetAutoTopupSettingsResponse404 | GetAutoTopupSettingsResponse422 | GetAutoTopupSettingsResponse429 | GetAutoTopupSettingsResponse500 | GetAutoTopupSettingsResponse503]
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
    GetAutoTopupSettingsResponse200
    | GetAutoTopupSettingsResponse400
    | GetAutoTopupSettingsResponse401
    | GetAutoTopupSettingsResponse402
    | GetAutoTopupSettingsResponse403
    | GetAutoTopupSettingsResponse404
    | GetAutoTopupSettingsResponse422
    | GetAutoTopupSettingsResponse429
    | GetAutoTopupSettingsResponse500
    | GetAutoTopupSettingsResponse503
    | None
):
    r"""Get auto top-up settings

     Get the organization's auto top-up configuration. When configured is false, no auto top-up settings
    exist yet.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAutoTopupSettingsResponse200 | GetAutoTopupSettingsResponse400 | GetAutoTopupSettingsResponse401 | GetAutoTopupSettingsResponse402 | GetAutoTopupSettingsResponse403 | GetAutoTopupSettingsResponse404 | GetAutoTopupSettingsResponse422 | GetAutoTopupSettingsResponse429 | GetAutoTopupSettingsResponse500 | GetAutoTopupSettingsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
