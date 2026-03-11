from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.manually_spawn_saved_search_run_body import ManuallySpawnSavedSearchRunBody
from ...models.manually_spawn_saved_search_run_response_200 import ManuallySpawnSavedSearchRunResponse200
from ...models.manually_spawn_saved_search_run_response_400 import ManuallySpawnSavedSearchRunResponse400
from ...models.manually_spawn_saved_search_run_response_401 import ManuallySpawnSavedSearchRunResponse401
from ...models.manually_spawn_saved_search_run_response_402 import ManuallySpawnSavedSearchRunResponse402
from ...models.manually_spawn_saved_search_run_response_403 import ManuallySpawnSavedSearchRunResponse403
from ...models.manually_spawn_saved_search_run_response_404 import ManuallySpawnSavedSearchRunResponse404
from ...models.manually_spawn_saved_search_run_response_429 import ManuallySpawnSavedSearchRunResponse429
from ...models.manually_spawn_saved_search_run_response_500 import ManuallySpawnSavedSearchRunResponse500
from ...models.manually_spawn_saved_search_run_response_503 import ManuallySpawnSavedSearchRunResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ManuallySpawnSavedSearchRunBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/spawn",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ManuallySpawnSavedSearchRunResponse200
    | ManuallySpawnSavedSearchRunResponse400
    | ManuallySpawnSavedSearchRunResponse401
    | ManuallySpawnSavedSearchRunResponse402
    | ManuallySpawnSavedSearchRunResponse403
    | ManuallySpawnSavedSearchRunResponse404
    | ManuallySpawnSavedSearchRunResponse429
    | ManuallySpawnSavedSearchRunResponse500
    | ManuallySpawnSavedSearchRunResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ManuallySpawnSavedSearchRunResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ManuallySpawnSavedSearchRunResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ManuallySpawnSavedSearchRunResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ManuallySpawnSavedSearchRunResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ManuallySpawnSavedSearchRunResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ManuallySpawnSavedSearchRunResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ManuallySpawnSavedSearchRunResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ManuallySpawnSavedSearchRunResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ManuallySpawnSavedSearchRunResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ManuallySpawnSavedSearchRunResponse200
    | ManuallySpawnSavedSearchRunResponse400
    | ManuallySpawnSavedSearchRunResponse401
    | ManuallySpawnSavedSearchRunResponse402
    | ManuallySpawnSavedSearchRunResponse403
    | ManuallySpawnSavedSearchRunResponse404
    | ManuallySpawnSavedSearchRunResponse429
    | ManuallySpawnSavedSearchRunResponse500
    | ManuallySpawnSavedSearchRunResponse503
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
    body: ManuallySpawnSavedSearchRunBody,
) -> Response[
    ManuallySpawnSavedSearchRunResponse200
    | ManuallySpawnSavedSearchRunResponse400
    | ManuallySpawnSavedSearchRunResponse401
    | ManuallySpawnSavedSearchRunResponse402
    | ManuallySpawnSavedSearchRunResponse403
    | ManuallySpawnSavedSearchRunResponse404
    | ManuallySpawnSavedSearchRunResponse429
    | ManuallySpawnSavedSearchRunResponse500
    | ManuallySpawnSavedSearchRunResponse503
]:
    r"""Manually spawn saved search run

     Manually spawn a new saved search run

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per prospect/company found in search&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ManuallySpawnSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManuallySpawnSavedSearchRunResponse200 | ManuallySpawnSavedSearchRunResponse400 | ManuallySpawnSavedSearchRunResponse401 | ManuallySpawnSavedSearchRunResponse402 | ManuallySpawnSavedSearchRunResponse403 | ManuallySpawnSavedSearchRunResponse404 | ManuallySpawnSavedSearchRunResponse429 | ManuallySpawnSavedSearchRunResponse500 | ManuallySpawnSavedSearchRunResponse503]
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
    body: ManuallySpawnSavedSearchRunBody,
) -> (
    ManuallySpawnSavedSearchRunResponse200
    | ManuallySpawnSavedSearchRunResponse400
    | ManuallySpawnSavedSearchRunResponse401
    | ManuallySpawnSavedSearchRunResponse402
    | ManuallySpawnSavedSearchRunResponse403
    | ManuallySpawnSavedSearchRunResponse404
    | ManuallySpawnSavedSearchRunResponse429
    | ManuallySpawnSavedSearchRunResponse500
    | ManuallySpawnSavedSearchRunResponse503
    | None
):
    r"""Manually spawn saved search run

     Manually spawn a new saved search run

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per prospect/company found in search&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ManuallySpawnSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManuallySpawnSavedSearchRunResponse200 | ManuallySpawnSavedSearchRunResponse400 | ManuallySpawnSavedSearchRunResponse401 | ManuallySpawnSavedSearchRunResponse402 | ManuallySpawnSavedSearchRunResponse403 | ManuallySpawnSavedSearchRunResponse404 | ManuallySpawnSavedSearchRunResponse429 | ManuallySpawnSavedSearchRunResponse500 | ManuallySpawnSavedSearchRunResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ManuallySpawnSavedSearchRunBody,
) -> Response[
    ManuallySpawnSavedSearchRunResponse200
    | ManuallySpawnSavedSearchRunResponse400
    | ManuallySpawnSavedSearchRunResponse401
    | ManuallySpawnSavedSearchRunResponse402
    | ManuallySpawnSavedSearchRunResponse403
    | ManuallySpawnSavedSearchRunResponse404
    | ManuallySpawnSavedSearchRunResponse429
    | ManuallySpawnSavedSearchRunResponse500
    | ManuallySpawnSavedSearchRunResponse503
]:
    r"""Manually spawn saved search run

     Manually spawn a new saved search run

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per prospect/company found in search&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ManuallySpawnSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManuallySpawnSavedSearchRunResponse200 | ManuallySpawnSavedSearchRunResponse400 | ManuallySpawnSavedSearchRunResponse401 | ManuallySpawnSavedSearchRunResponse402 | ManuallySpawnSavedSearchRunResponse403 | ManuallySpawnSavedSearchRunResponse404 | ManuallySpawnSavedSearchRunResponse429 | ManuallySpawnSavedSearchRunResponse500 | ManuallySpawnSavedSearchRunResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ManuallySpawnSavedSearchRunBody,
) -> (
    ManuallySpawnSavedSearchRunResponse200
    | ManuallySpawnSavedSearchRunResponse400
    | ManuallySpawnSavedSearchRunResponse401
    | ManuallySpawnSavedSearchRunResponse402
    | ManuallySpawnSavedSearchRunResponse403
    | ManuallySpawnSavedSearchRunResponse404
    | ManuallySpawnSavedSearchRunResponse429
    | ManuallySpawnSavedSearchRunResponse500
    | ManuallySpawnSavedSearchRunResponse503
    | None
):
    r"""Manually spawn saved search run

     Manually spawn a new saved search run

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per prospect/company found in search&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ManuallySpawnSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManuallySpawnSavedSearchRunResponse200 | ManuallySpawnSavedSearchRunResponse400 | ManuallySpawnSavedSearchRunResponse401 | ManuallySpawnSavedSearchRunResponse402 | ManuallySpawnSavedSearchRunResponse403 | ManuallySpawnSavedSearchRunResponse404 | ManuallySpawnSavedSearchRunResponse429 | ManuallySpawnSavedSearchRunResponse500 | ManuallySpawnSavedSearchRunResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
