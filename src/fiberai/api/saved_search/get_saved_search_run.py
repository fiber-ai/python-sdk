from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_saved_search_run_body import GetSavedSearchRunBody
from ...models.get_saved_search_run_response_400 import GetSavedSearchRunResponse400
from ...models.get_saved_search_run_response_401 import GetSavedSearchRunResponse401
from ...models.get_saved_search_run_response_402 import GetSavedSearchRunResponse402
from ...models.get_saved_search_run_response_403 import GetSavedSearchRunResponse403
from ...models.get_saved_search_run_response_404 import GetSavedSearchRunResponse404
from ...models.get_saved_search_run_response_429 import GetSavedSearchRunResponse429
from ...models.get_saved_search_run_response_500 import GetSavedSearchRunResponse500
from ...models.get_saved_search_run_response_503 import GetSavedSearchRunResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetSavedSearchRunBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/run/get",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSavedSearchRunResponse400
    | GetSavedSearchRunResponse401
    | GetSavedSearchRunResponse402
    | GetSavedSearchRunResponse403
    | GetSavedSearchRunResponse404
    | GetSavedSearchRunResponse429
    | GetSavedSearchRunResponse500
    | GetSavedSearchRunResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSavedSearchRunResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSavedSearchRunResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetSavedSearchRunResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetSavedSearchRunResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSavedSearchRunResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetSavedSearchRunResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetSavedSearchRunResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSavedSearchRunResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSavedSearchRunResponse400
    | GetSavedSearchRunResponse401
    | GetSavedSearchRunResponse402
    | GetSavedSearchRunResponse403
    | GetSavedSearchRunResponse404
    | GetSavedSearchRunResponse429
    | GetSavedSearchRunResponse500
    | GetSavedSearchRunResponse503
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
    body: GetSavedSearchRunBody,
) -> Response[
    GetSavedSearchRunResponse400
    | GetSavedSearchRunResponse401
    | GetSavedSearchRunResponse402
    | GetSavedSearchRunResponse403
    | GetSavedSearchRunResponse404
    | GetSavedSearchRunResponse429
    | GetSavedSearchRunResponse500
    | GetSavedSearchRunResponse503
]:
    r"""Get saved search run

     Get all details for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavedSearchRunResponse400 | GetSavedSearchRunResponse401 | GetSavedSearchRunResponse402 | GetSavedSearchRunResponse403 | GetSavedSearchRunResponse404 | GetSavedSearchRunResponse429 | GetSavedSearchRunResponse500 | GetSavedSearchRunResponse503]
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
    body: GetSavedSearchRunBody,
) -> (
    GetSavedSearchRunResponse400
    | GetSavedSearchRunResponse401
    | GetSavedSearchRunResponse402
    | GetSavedSearchRunResponse403
    | GetSavedSearchRunResponse404
    | GetSavedSearchRunResponse429
    | GetSavedSearchRunResponse500
    | GetSavedSearchRunResponse503
    | None
):
    r"""Get saved search run

     Get all details for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavedSearchRunResponse400 | GetSavedSearchRunResponse401 | GetSavedSearchRunResponse402 | GetSavedSearchRunResponse403 | GetSavedSearchRunResponse404 | GetSavedSearchRunResponse429 | GetSavedSearchRunResponse500 | GetSavedSearchRunResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetSavedSearchRunBody,
) -> Response[
    GetSavedSearchRunResponse400
    | GetSavedSearchRunResponse401
    | GetSavedSearchRunResponse402
    | GetSavedSearchRunResponse403
    | GetSavedSearchRunResponse404
    | GetSavedSearchRunResponse429
    | GetSavedSearchRunResponse500
    | GetSavedSearchRunResponse503
]:
    r"""Get saved search run

     Get all details for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavedSearchRunResponse400 | GetSavedSearchRunResponse401 | GetSavedSearchRunResponse402 | GetSavedSearchRunResponse403 | GetSavedSearchRunResponse404 | GetSavedSearchRunResponse429 | GetSavedSearchRunResponse500 | GetSavedSearchRunResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetSavedSearchRunBody,
) -> (
    GetSavedSearchRunResponse400
    | GetSavedSearchRunResponse401
    | GetSavedSearchRunResponse402
    | GetSavedSearchRunResponse403
    | GetSavedSearchRunResponse404
    | GetSavedSearchRunResponse429
    | GetSavedSearchRunResponse500
    | GetSavedSearchRunResponse503
    | None
):
    r"""Get saved search run

     Get all details for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavedSearchRunResponse400 | GetSavedSearchRunResponse401 | GetSavedSearchRunResponse402 | GetSavedSearchRunResponse403 | GetSavedSearchRunResponse404 | GetSavedSearchRunResponse429 | GetSavedSearchRunResponse500 | GetSavedSearchRunResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
