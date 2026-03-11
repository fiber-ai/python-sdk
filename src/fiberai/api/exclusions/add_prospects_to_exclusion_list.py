from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_prospects_to_exclusion_list_body import AddProspectsToExclusionListBody
from ...models.add_prospects_to_exclusion_list_response_200 import AddProspectsToExclusionListResponse200
from ...models.add_prospects_to_exclusion_list_response_400 import AddProspectsToExclusionListResponse400
from ...models.add_prospects_to_exclusion_list_response_401 import AddProspectsToExclusionListResponse401
from ...models.add_prospects_to_exclusion_list_response_402 import AddProspectsToExclusionListResponse402
from ...models.add_prospects_to_exclusion_list_response_403 import AddProspectsToExclusionListResponse403
from ...models.add_prospects_to_exclusion_list_response_404 import AddProspectsToExclusionListResponse404
from ...models.add_prospects_to_exclusion_list_response_429 import AddProspectsToExclusionListResponse429
from ...models.add_prospects_to_exclusion_list_response_500 import AddProspectsToExclusionListResponse500
from ...models.add_prospects_to_exclusion_list_response_503 import AddProspectsToExclusionListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: AddProspectsToExclusionListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exclusions/prospects/add-to-list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddProspectsToExclusionListResponse200
    | AddProspectsToExclusionListResponse400
    | AddProspectsToExclusionListResponse401
    | AddProspectsToExclusionListResponse402
    | AddProspectsToExclusionListResponse403
    | AddProspectsToExclusionListResponse404
    | AddProspectsToExclusionListResponse429
    | AddProspectsToExclusionListResponse500
    | AddProspectsToExclusionListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AddProspectsToExclusionListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddProspectsToExclusionListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddProspectsToExclusionListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = AddProspectsToExclusionListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = AddProspectsToExclusionListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddProspectsToExclusionListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = AddProspectsToExclusionListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AddProspectsToExclusionListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AddProspectsToExclusionListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddProspectsToExclusionListResponse200
    | AddProspectsToExclusionListResponse400
    | AddProspectsToExclusionListResponse401
    | AddProspectsToExclusionListResponse402
    | AddProspectsToExclusionListResponse403
    | AddProspectsToExclusionListResponse404
    | AddProspectsToExclusionListResponse429
    | AddProspectsToExclusionListResponse500
    | AddProspectsToExclusionListResponse503
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
    body: AddProspectsToExclusionListBody,
) -> Response[
    AddProspectsToExclusionListResponse200
    | AddProspectsToExclusionListResponse400
    | AddProspectsToExclusionListResponse401
    | AddProspectsToExclusionListResponse402
    | AddProspectsToExclusionListResponse403
    | AddProspectsToExclusionListResponse404
    | AddProspectsToExclusionListResponse429
    | AddProspectsToExclusionListResponse500
    | AddProspectsToExclusionListResponse503
]:
    r"""Add prospects to a prospect exclusion list

     Add prospects to a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddProspectsToExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddProspectsToExclusionListResponse200 | AddProspectsToExclusionListResponse400 | AddProspectsToExclusionListResponse401 | AddProspectsToExclusionListResponse402 | AddProspectsToExclusionListResponse403 | AddProspectsToExclusionListResponse404 | AddProspectsToExclusionListResponse429 | AddProspectsToExclusionListResponse500 | AddProspectsToExclusionListResponse503]
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
    body: AddProspectsToExclusionListBody,
) -> (
    AddProspectsToExclusionListResponse200
    | AddProspectsToExclusionListResponse400
    | AddProspectsToExclusionListResponse401
    | AddProspectsToExclusionListResponse402
    | AddProspectsToExclusionListResponse403
    | AddProspectsToExclusionListResponse404
    | AddProspectsToExclusionListResponse429
    | AddProspectsToExclusionListResponse500
    | AddProspectsToExclusionListResponse503
    | None
):
    r"""Add prospects to a prospect exclusion list

     Add prospects to a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddProspectsToExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddProspectsToExclusionListResponse200 | AddProspectsToExclusionListResponse400 | AddProspectsToExclusionListResponse401 | AddProspectsToExclusionListResponse402 | AddProspectsToExclusionListResponse403 | AddProspectsToExclusionListResponse404 | AddProspectsToExclusionListResponse429 | AddProspectsToExclusionListResponse500 | AddProspectsToExclusionListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddProspectsToExclusionListBody,
) -> Response[
    AddProspectsToExclusionListResponse200
    | AddProspectsToExclusionListResponse400
    | AddProspectsToExclusionListResponse401
    | AddProspectsToExclusionListResponse402
    | AddProspectsToExclusionListResponse403
    | AddProspectsToExclusionListResponse404
    | AddProspectsToExclusionListResponse429
    | AddProspectsToExclusionListResponse500
    | AddProspectsToExclusionListResponse503
]:
    r"""Add prospects to a prospect exclusion list

     Add prospects to a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddProspectsToExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddProspectsToExclusionListResponse200 | AddProspectsToExclusionListResponse400 | AddProspectsToExclusionListResponse401 | AddProspectsToExclusionListResponse402 | AddProspectsToExclusionListResponse403 | AddProspectsToExclusionListResponse404 | AddProspectsToExclusionListResponse429 | AddProspectsToExclusionListResponse500 | AddProspectsToExclusionListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AddProspectsToExclusionListBody,
) -> (
    AddProspectsToExclusionListResponse200
    | AddProspectsToExclusionListResponse400
    | AddProspectsToExclusionListResponse401
    | AddProspectsToExclusionListResponse402
    | AddProspectsToExclusionListResponse403
    | AddProspectsToExclusionListResponse404
    | AddProspectsToExclusionListResponse429
    | AddProspectsToExclusionListResponse500
    | AddProspectsToExclusionListResponse503
    | None
):
    r"""Add prospects to a prospect exclusion list

     Add prospects to a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddProspectsToExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddProspectsToExclusionListResponse200 | AddProspectsToExclusionListResponse400 | AddProspectsToExclusionListResponse401 | AddProspectsToExclusionListResponse402 | AddProspectsToExclusionListResponse403 | AddProspectsToExclusionListResponse404 | AddProspectsToExclusionListResponse429 | AddProspectsToExclusionListResponse500 | AddProspectsToExclusionListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
