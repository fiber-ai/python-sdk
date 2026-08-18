from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_tracker_company_list_body import CreateTrackerCompanyListBody
from ...models.create_tracker_company_list_response_400 import CreateTrackerCompanyListResponse400
from ...models.create_tracker_company_list_response_401 import CreateTrackerCompanyListResponse401
from ...models.create_tracker_company_list_response_402 import CreateTrackerCompanyListResponse402
from ...models.create_tracker_company_list_response_403 import CreateTrackerCompanyListResponse403
from ...models.create_tracker_company_list_response_404 import CreateTrackerCompanyListResponse404
from ...models.create_tracker_company_list_response_422 import CreateTrackerCompanyListResponse422
from ...models.create_tracker_company_list_response_429 import CreateTrackerCompanyListResponse429
from ...models.create_tracker_company_list_response_500 import CreateTrackerCompanyListResponse500
from ...models.create_tracker_company_list_response_503 import CreateTrackerCompanyListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CreateTrackerCompanyListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tracker/company-lists",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateTrackerCompanyListResponse400
    | CreateTrackerCompanyListResponse401
    | CreateTrackerCompanyListResponse402
    | CreateTrackerCompanyListResponse403
    | CreateTrackerCompanyListResponse404
    | CreateTrackerCompanyListResponse422
    | CreateTrackerCompanyListResponse429
    | CreateTrackerCompanyListResponse500
    | CreateTrackerCompanyListResponse503
    | None
):
    if response.status_code == 400:
        response_400 = CreateTrackerCompanyListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateTrackerCompanyListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CreateTrackerCompanyListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CreateTrackerCompanyListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateTrackerCompanyListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = CreateTrackerCompanyListResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = CreateTrackerCompanyListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateTrackerCompanyListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateTrackerCompanyListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateTrackerCompanyListResponse400
    | CreateTrackerCompanyListResponse401
    | CreateTrackerCompanyListResponse402
    | CreateTrackerCompanyListResponse403
    | CreateTrackerCompanyListResponse404
    | CreateTrackerCompanyListResponse422
    | CreateTrackerCompanyListResponse429
    | CreateTrackerCompanyListResponse500
    | CreateTrackerCompanyListResponse503
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
    body: CreateTrackerCompanyListBody,
) -> Response[
    CreateTrackerCompanyListResponse400
    | CreateTrackerCompanyListResponse401
    | CreateTrackerCompanyListResponse402
    | CreateTrackerCompanyListResponse403
    | CreateTrackerCompanyListResponse404
    | CreateTrackerCompanyListResponse422
    | CreateTrackerCompanyListResponse429
    | CreateTrackerCompanyListResponse500
    | CreateTrackerCompanyListResponse503
]:
    r"""Create company tracker list

     Create a new company tracker list. By default you add companies manually and we periodically check
    them for changes matching your tracking rules. Provide `companySearchParams` to instead create a
    DYNAMIC list that auto-populates with companies matching a query and refreshes over time. Credits
    are charged per entity per refresh cycle (see your plan's pricing for exact rates). Creating the
    list itself is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateTrackerCompanyListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTrackerCompanyListResponse400 | CreateTrackerCompanyListResponse401 | CreateTrackerCompanyListResponse402 | CreateTrackerCompanyListResponse403 | CreateTrackerCompanyListResponse404 | CreateTrackerCompanyListResponse422 | CreateTrackerCompanyListResponse429 | CreateTrackerCompanyListResponse500 | CreateTrackerCompanyListResponse503]
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
    body: CreateTrackerCompanyListBody,
) -> (
    CreateTrackerCompanyListResponse400
    | CreateTrackerCompanyListResponse401
    | CreateTrackerCompanyListResponse402
    | CreateTrackerCompanyListResponse403
    | CreateTrackerCompanyListResponse404
    | CreateTrackerCompanyListResponse422
    | CreateTrackerCompanyListResponse429
    | CreateTrackerCompanyListResponse500
    | CreateTrackerCompanyListResponse503
    | None
):
    r"""Create company tracker list

     Create a new company tracker list. By default you add companies manually and we periodically check
    them for changes matching your tracking rules. Provide `companySearchParams` to instead create a
    DYNAMIC list that auto-populates with companies matching a query and refreshes over time. Credits
    are charged per entity per refresh cycle (see your plan's pricing for exact rates). Creating the
    list itself is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateTrackerCompanyListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTrackerCompanyListResponse400 | CreateTrackerCompanyListResponse401 | CreateTrackerCompanyListResponse402 | CreateTrackerCompanyListResponse403 | CreateTrackerCompanyListResponse404 | CreateTrackerCompanyListResponse422 | CreateTrackerCompanyListResponse429 | CreateTrackerCompanyListResponse500 | CreateTrackerCompanyListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTrackerCompanyListBody,
) -> Response[
    CreateTrackerCompanyListResponse400
    | CreateTrackerCompanyListResponse401
    | CreateTrackerCompanyListResponse402
    | CreateTrackerCompanyListResponse403
    | CreateTrackerCompanyListResponse404
    | CreateTrackerCompanyListResponse422
    | CreateTrackerCompanyListResponse429
    | CreateTrackerCompanyListResponse500
    | CreateTrackerCompanyListResponse503
]:
    r"""Create company tracker list

     Create a new company tracker list. By default you add companies manually and we periodically check
    them for changes matching your tracking rules. Provide `companySearchParams` to instead create a
    DYNAMIC list that auto-populates with companies matching a query and refreshes over time. Credits
    are charged per entity per refresh cycle (see your plan's pricing for exact rates). Creating the
    list itself is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateTrackerCompanyListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTrackerCompanyListResponse400 | CreateTrackerCompanyListResponse401 | CreateTrackerCompanyListResponse402 | CreateTrackerCompanyListResponse403 | CreateTrackerCompanyListResponse404 | CreateTrackerCompanyListResponse422 | CreateTrackerCompanyListResponse429 | CreateTrackerCompanyListResponse500 | CreateTrackerCompanyListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTrackerCompanyListBody,
) -> (
    CreateTrackerCompanyListResponse400
    | CreateTrackerCompanyListResponse401
    | CreateTrackerCompanyListResponse402
    | CreateTrackerCompanyListResponse403
    | CreateTrackerCompanyListResponse404
    | CreateTrackerCompanyListResponse422
    | CreateTrackerCompanyListResponse429
    | CreateTrackerCompanyListResponse500
    | CreateTrackerCompanyListResponse503
    | None
):
    r"""Create company tracker list

     Create a new company tracker list. By default you add companies manually and we periodically check
    them for changes matching your tracking rules. Provide `companySearchParams` to instead create a
    DYNAMIC list that auto-populates with companies matching a query and refreshes over time. Credits
    are charged per entity per refresh cycle (see your plan's pricing for exact rates). Creating the
    list itself is free.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateTrackerCompanyListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTrackerCompanyListResponse400 | CreateTrackerCompanyListResponse401 | CreateTrackerCompanyListResponse402 | CreateTrackerCompanyListResponse403 | CreateTrackerCompanyListResponse404 | CreateTrackerCompanyListResponse422 | CreateTrackerCompanyListResponse429 | CreateTrackerCompanyListResponse500 | CreateTrackerCompanyListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
