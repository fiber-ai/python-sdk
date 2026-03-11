from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_current_profiles_in_saved_search_body import GetCurrentProfilesInSavedSearchBody
from ...models.get_current_profiles_in_saved_search_response_200 import GetCurrentProfilesInSavedSearchResponse200
from ...models.get_current_profiles_in_saved_search_response_400 import GetCurrentProfilesInSavedSearchResponse400
from ...models.get_current_profiles_in_saved_search_response_401 import GetCurrentProfilesInSavedSearchResponse401
from ...models.get_current_profiles_in_saved_search_response_402 import GetCurrentProfilesInSavedSearchResponse402
from ...models.get_current_profiles_in_saved_search_response_403 import GetCurrentProfilesInSavedSearchResponse403
from ...models.get_current_profiles_in_saved_search_response_404 import GetCurrentProfilesInSavedSearchResponse404
from ...models.get_current_profiles_in_saved_search_response_429 import GetCurrentProfilesInSavedSearchResponse429
from ...models.get_current_profiles_in_saved_search_response_500 import GetCurrentProfilesInSavedSearchResponse500
from ...models.get_current_profiles_in_saved_search_response_503 import GetCurrentProfilesInSavedSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetCurrentProfilesInSavedSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/current/profiles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCurrentProfilesInSavedSearchResponse200
    | GetCurrentProfilesInSavedSearchResponse400
    | GetCurrentProfilesInSavedSearchResponse401
    | GetCurrentProfilesInSavedSearchResponse402
    | GetCurrentProfilesInSavedSearchResponse403
    | GetCurrentProfilesInSavedSearchResponse404
    | GetCurrentProfilesInSavedSearchResponse429
    | GetCurrentProfilesInSavedSearchResponse500
    | GetCurrentProfilesInSavedSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetCurrentProfilesInSavedSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCurrentProfilesInSavedSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetCurrentProfilesInSavedSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetCurrentProfilesInSavedSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetCurrentProfilesInSavedSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCurrentProfilesInSavedSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetCurrentProfilesInSavedSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetCurrentProfilesInSavedSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetCurrentProfilesInSavedSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCurrentProfilesInSavedSearchResponse200
    | GetCurrentProfilesInSavedSearchResponse400
    | GetCurrentProfilesInSavedSearchResponse401
    | GetCurrentProfilesInSavedSearchResponse402
    | GetCurrentProfilesInSavedSearchResponse403
    | GetCurrentProfilesInSavedSearchResponse404
    | GetCurrentProfilesInSavedSearchResponse429
    | GetCurrentProfilesInSavedSearchResponse500
    | GetCurrentProfilesInSavedSearchResponse503
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
    body: GetCurrentProfilesInSavedSearchBody,
) -> Response[
    GetCurrentProfilesInSavedSearchResponse200
    | GetCurrentProfilesInSavedSearchResponse400
    | GetCurrentProfilesInSavedSearchResponse401
    | GetCurrentProfilesInSavedSearchResponse402
    | GetCurrentProfilesInSavedSearchResponse403
    | GetCurrentProfilesInSavedSearchResponse404
    | GetCurrentProfilesInSavedSearchResponse429
    | GetCurrentProfilesInSavedSearchResponse500
    | GetCurrentProfilesInSavedSearchResponse503
]:
    r"""Get current profiles in saved search

     Get current profiles found for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCurrentProfilesInSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCurrentProfilesInSavedSearchResponse200 | GetCurrentProfilesInSavedSearchResponse400 | GetCurrentProfilesInSavedSearchResponse401 | GetCurrentProfilesInSavedSearchResponse402 | GetCurrentProfilesInSavedSearchResponse403 | GetCurrentProfilesInSavedSearchResponse404 | GetCurrentProfilesInSavedSearchResponse429 | GetCurrentProfilesInSavedSearchResponse500 | GetCurrentProfilesInSavedSearchResponse503]
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
    body: GetCurrentProfilesInSavedSearchBody,
) -> (
    GetCurrentProfilesInSavedSearchResponse200
    | GetCurrentProfilesInSavedSearchResponse400
    | GetCurrentProfilesInSavedSearchResponse401
    | GetCurrentProfilesInSavedSearchResponse402
    | GetCurrentProfilesInSavedSearchResponse403
    | GetCurrentProfilesInSavedSearchResponse404
    | GetCurrentProfilesInSavedSearchResponse429
    | GetCurrentProfilesInSavedSearchResponse500
    | GetCurrentProfilesInSavedSearchResponse503
    | None
):
    r"""Get current profiles in saved search

     Get current profiles found for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCurrentProfilesInSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCurrentProfilesInSavedSearchResponse200 | GetCurrentProfilesInSavedSearchResponse400 | GetCurrentProfilesInSavedSearchResponse401 | GetCurrentProfilesInSavedSearchResponse402 | GetCurrentProfilesInSavedSearchResponse403 | GetCurrentProfilesInSavedSearchResponse404 | GetCurrentProfilesInSavedSearchResponse429 | GetCurrentProfilesInSavedSearchResponse500 | GetCurrentProfilesInSavedSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetCurrentProfilesInSavedSearchBody,
) -> Response[
    GetCurrentProfilesInSavedSearchResponse200
    | GetCurrentProfilesInSavedSearchResponse400
    | GetCurrentProfilesInSavedSearchResponse401
    | GetCurrentProfilesInSavedSearchResponse402
    | GetCurrentProfilesInSavedSearchResponse403
    | GetCurrentProfilesInSavedSearchResponse404
    | GetCurrentProfilesInSavedSearchResponse429
    | GetCurrentProfilesInSavedSearchResponse500
    | GetCurrentProfilesInSavedSearchResponse503
]:
    r"""Get current profiles in saved search

     Get current profiles found for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCurrentProfilesInSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCurrentProfilesInSavedSearchResponse200 | GetCurrentProfilesInSavedSearchResponse400 | GetCurrentProfilesInSavedSearchResponse401 | GetCurrentProfilesInSavedSearchResponse402 | GetCurrentProfilesInSavedSearchResponse403 | GetCurrentProfilesInSavedSearchResponse404 | GetCurrentProfilesInSavedSearchResponse429 | GetCurrentProfilesInSavedSearchResponse500 | GetCurrentProfilesInSavedSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetCurrentProfilesInSavedSearchBody,
) -> (
    GetCurrentProfilesInSavedSearchResponse200
    | GetCurrentProfilesInSavedSearchResponse400
    | GetCurrentProfilesInSavedSearchResponse401
    | GetCurrentProfilesInSavedSearchResponse402
    | GetCurrentProfilesInSavedSearchResponse403
    | GetCurrentProfilesInSavedSearchResponse404
    | GetCurrentProfilesInSavedSearchResponse429
    | GetCurrentProfilesInSavedSearchResponse500
    | GetCurrentProfilesInSavedSearchResponse503
    | None
):
    r"""Get current profiles in saved search

     Get current profiles found for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCurrentProfilesInSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCurrentProfilesInSavedSearchResponse200 | GetCurrentProfilesInSavedSearchResponse400 | GetCurrentProfilesInSavedSearchResponse401 | GetCurrentProfilesInSavedSearchResponse402 | GetCurrentProfilesInSavedSearchResponse403 | GetCurrentProfilesInSavedSearchResponse404 | GetCurrentProfilesInSavedSearchResponse429 | GetCurrentProfilesInSavedSearchResponse500 | GetCurrentProfilesInSavedSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
