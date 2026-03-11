from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_excluded_prospects_for_exclusion_list_body import GetExcludedProspectsForExclusionListBody
from ...models.get_excluded_prospects_for_exclusion_list_response_200 import (
    GetExcludedProspectsForExclusionListResponse200,
)
from ...models.get_excluded_prospects_for_exclusion_list_response_400 import (
    GetExcludedProspectsForExclusionListResponse400,
)
from ...models.get_excluded_prospects_for_exclusion_list_response_401 import (
    GetExcludedProspectsForExclusionListResponse401,
)
from ...models.get_excluded_prospects_for_exclusion_list_response_402 import (
    GetExcludedProspectsForExclusionListResponse402,
)
from ...models.get_excluded_prospects_for_exclusion_list_response_403 import (
    GetExcludedProspectsForExclusionListResponse403,
)
from ...models.get_excluded_prospects_for_exclusion_list_response_404 import (
    GetExcludedProspectsForExclusionListResponse404,
)
from ...models.get_excluded_prospects_for_exclusion_list_response_429 import (
    GetExcludedProspectsForExclusionListResponse429,
)
from ...models.get_excluded_prospects_for_exclusion_list_response_500 import (
    GetExcludedProspectsForExclusionListResponse500,
)
from ...models.get_excluded_prospects_for_exclusion_list_response_503 import (
    GetExcludedProspectsForExclusionListResponse503,
)
from ...types import Response


def _get_kwargs(
    *,
    body: GetExcludedProspectsForExclusionListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exclusions/prospects/read-from-list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetExcludedProspectsForExclusionListResponse200
    | GetExcludedProspectsForExclusionListResponse400
    | GetExcludedProspectsForExclusionListResponse401
    | GetExcludedProspectsForExclusionListResponse402
    | GetExcludedProspectsForExclusionListResponse403
    | GetExcludedProspectsForExclusionListResponse404
    | GetExcludedProspectsForExclusionListResponse429
    | GetExcludedProspectsForExclusionListResponse500
    | GetExcludedProspectsForExclusionListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetExcludedProspectsForExclusionListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetExcludedProspectsForExclusionListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetExcludedProspectsForExclusionListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetExcludedProspectsForExclusionListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetExcludedProspectsForExclusionListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetExcludedProspectsForExclusionListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetExcludedProspectsForExclusionListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetExcludedProspectsForExclusionListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetExcludedProspectsForExclusionListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetExcludedProspectsForExclusionListResponse200
    | GetExcludedProspectsForExclusionListResponse400
    | GetExcludedProspectsForExclusionListResponse401
    | GetExcludedProspectsForExclusionListResponse402
    | GetExcludedProspectsForExclusionListResponse403
    | GetExcludedProspectsForExclusionListResponse404
    | GetExcludedProspectsForExclusionListResponse429
    | GetExcludedProspectsForExclusionListResponse500
    | GetExcludedProspectsForExclusionListResponse503
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
    body: GetExcludedProspectsForExclusionListBody,
) -> Response[
    GetExcludedProspectsForExclusionListResponse200
    | GetExcludedProspectsForExclusionListResponse400
    | GetExcludedProspectsForExclusionListResponse401
    | GetExcludedProspectsForExclusionListResponse402
    | GetExcludedProspectsForExclusionListResponse403
    | GetExcludedProspectsForExclusionListResponse404
    | GetExcludedProspectsForExclusionListResponse429
    | GetExcludedProspectsForExclusionListResponse500
    | GetExcludedProspectsForExclusionListResponse503
]:
    r"""Get excluded prospects for exclusion list

     Get excluded prospects for a specific exclusion list with pagination

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetExcludedProspectsForExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExcludedProspectsForExclusionListResponse200 | GetExcludedProspectsForExclusionListResponse400 | GetExcludedProspectsForExclusionListResponse401 | GetExcludedProspectsForExclusionListResponse402 | GetExcludedProspectsForExclusionListResponse403 | GetExcludedProspectsForExclusionListResponse404 | GetExcludedProspectsForExclusionListResponse429 | GetExcludedProspectsForExclusionListResponse500 | GetExcludedProspectsForExclusionListResponse503]
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
    body: GetExcludedProspectsForExclusionListBody,
) -> (
    GetExcludedProspectsForExclusionListResponse200
    | GetExcludedProspectsForExclusionListResponse400
    | GetExcludedProspectsForExclusionListResponse401
    | GetExcludedProspectsForExclusionListResponse402
    | GetExcludedProspectsForExclusionListResponse403
    | GetExcludedProspectsForExclusionListResponse404
    | GetExcludedProspectsForExclusionListResponse429
    | GetExcludedProspectsForExclusionListResponse500
    | GetExcludedProspectsForExclusionListResponse503
    | None
):
    r"""Get excluded prospects for exclusion list

     Get excluded prospects for a specific exclusion list with pagination

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetExcludedProspectsForExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExcludedProspectsForExclusionListResponse200 | GetExcludedProspectsForExclusionListResponse400 | GetExcludedProspectsForExclusionListResponse401 | GetExcludedProspectsForExclusionListResponse402 | GetExcludedProspectsForExclusionListResponse403 | GetExcludedProspectsForExclusionListResponse404 | GetExcludedProspectsForExclusionListResponse429 | GetExcludedProspectsForExclusionListResponse500 | GetExcludedProspectsForExclusionListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetExcludedProspectsForExclusionListBody,
) -> Response[
    GetExcludedProspectsForExclusionListResponse200
    | GetExcludedProspectsForExclusionListResponse400
    | GetExcludedProspectsForExclusionListResponse401
    | GetExcludedProspectsForExclusionListResponse402
    | GetExcludedProspectsForExclusionListResponse403
    | GetExcludedProspectsForExclusionListResponse404
    | GetExcludedProspectsForExclusionListResponse429
    | GetExcludedProspectsForExclusionListResponse500
    | GetExcludedProspectsForExclusionListResponse503
]:
    r"""Get excluded prospects for exclusion list

     Get excluded prospects for a specific exclusion list with pagination

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetExcludedProspectsForExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExcludedProspectsForExclusionListResponse200 | GetExcludedProspectsForExclusionListResponse400 | GetExcludedProspectsForExclusionListResponse401 | GetExcludedProspectsForExclusionListResponse402 | GetExcludedProspectsForExclusionListResponse403 | GetExcludedProspectsForExclusionListResponse404 | GetExcludedProspectsForExclusionListResponse429 | GetExcludedProspectsForExclusionListResponse500 | GetExcludedProspectsForExclusionListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetExcludedProspectsForExclusionListBody,
) -> (
    GetExcludedProspectsForExclusionListResponse200
    | GetExcludedProspectsForExclusionListResponse400
    | GetExcludedProspectsForExclusionListResponse401
    | GetExcludedProspectsForExclusionListResponse402
    | GetExcludedProspectsForExclusionListResponse403
    | GetExcludedProspectsForExclusionListResponse404
    | GetExcludedProspectsForExclusionListResponse429
    | GetExcludedProspectsForExclusionListResponse500
    | GetExcludedProspectsForExclusionListResponse503
    | None
):
    r"""Get excluded prospects for exclusion list

     Get excluded prospects for a specific exclusion list with pagination

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetExcludedProspectsForExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExcludedProspectsForExclusionListResponse200 | GetExcludedProspectsForExclusionListResponse400 | GetExcludedProspectsForExclusionListResponse401 | GetExcludedProspectsForExclusionListResponse402 | GetExcludedProspectsForExclusionListResponse403 | GetExcludedProspectsForExclusionListResponse404 | GetExcludedProspectsForExclusionListResponse429 | GetExcludedProspectsForExclusionListResponse500 | GetExcludedProspectsForExclusionListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
