from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_tracker_companies_body import AddTrackerCompaniesBody
from ...models.add_tracker_companies_response_200 import AddTrackerCompaniesResponse200
from ...models.add_tracker_companies_response_400 import AddTrackerCompaniesResponse400
from ...models.add_tracker_companies_response_401 import AddTrackerCompaniesResponse401
from ...models.add_tracker_companies_response_402 import AddTrackerCompaniesResponse402
from ...models.add_tracker_companies_response_403 import AddTrackerCompaniesResponse403
from ...models.add_tracker_companies_response_404 import AddTrackerCompaniesResponse404
from ...models.add_tracker_companies_response_422 import AddTrackerCompaniesResponse422
from ...models.add_tracker_companies_response_429 import AddTrackerCompaniesResponse429
from ...models.add_tracker_companies_response_500 import AddTrackerCompaniesResponse500
from ...models.add_tracker_companies_response_503 import AddTrackerCompaniesResponse503
from ...types import Response


def _get_kwargs(
    list_id: str,
    *,
    body: AddTrackerCompaniesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/tracker/company-lists/{list_id}/companies".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddTrackerCompaniesResponse200
    | AddTrackerCompaniesResponse400
    | AddTrackerCompaniesResponse401
    | AddTrackerCompaniesResponse402
    | AddTrackerCompaniesResponse403
    | AddTrackerCompaniesResponse404
    | AddTrackerCompaniesResponse422
    | AddTrackerCompaniesResponse429
    | AddTrackerCompaniesResponse500
    | AddTrackerCompaniesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AddTrackerCompaniesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddTrackerCompaniesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddTrackerCompaniesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = AddTrackerCompaniesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = AddTrackerCompaniesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddTrackerCompaniesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = AddTrackerCompaniesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = AddTrackerCompaniesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AddTrackerCompaniesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AddTrackerCompaniesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddTrackerCompaniesResponse200
    | AddTrackerCompaniesResponse400
    | AddTrackerCompaniesResponse401
    | AddTrackerCompaniesResponse402
    | AddTrackerCompaniesResponse403
    | AddTrackerCompaniesResponse404
    | AddTrackerCompaniesResponse422
    | AddTrackerCompaniesResponse429
    | AddTrackerCompaniesResponse500
    | AddTrackerCompaniesResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTrackerCompaniesBody,
) -> Response[
    AddTrackerCompaniesResponse200
    | AddTrackerCompaniesResponse400
    | AddTrackerCompaniesResponse401
    | AddTrackerCompaniesResponse402
    | AddTrackerCompaniesResponse403
    | AddTrackerCompaniesResponse404
    | AddTrackerCompaniesResponse422
    | AddTrackerCompaniesResponse429
    | AddTrackerCompaniesResponse500
    | AddTrackerCompaniesResponse503
]:
    r"""Add companies to tracker list

     Add companies to a company tracker list. Identify companies by LinkedIn URL, organization ID, slug,
    or website domain. At least one identifier is required per company.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (AddTrackerCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddTrackerCompaniesResponse200 | AddTrackerCompaniesResponse400 | AddTrackerCompaniesResponse401 | AddTrackerCompaniesResponse402 | AddTrackerCompaniesResponse403 | AddTrackerCompaniesResponse404 | AddTrackerCompaniesResponse422 | AddTrackerCompaniesResponse429 | AddTrackerCompaniesResponse500 | AddTrackerCompaniesResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTrackerCompaniesBody,
) -> (
    AddTrackerCompaniesResponse200
    | AddTrackerCompaniesResponse400
    | AddTrackerCompaniesResponse401
    | AddTrackerCompaniesResponse402
    | AddTrackerCompaniesResponse403
    | AddTrackerCompaniesResponse404
    | AddTrackerCompaniesResponse422
    | AddTrackerCompaniesResponse429
    | AddTrackerCompaniesResponse500
    | AddTrackerCompaniesResponse503
    | None
):
    r"""Add companies to tracker list

     Add companies to a company tracker list. Identify companies by LinkedIn URL, organization ID, slug,
    or website domain. At least one identifier is required per company.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (AddTrackerCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddTrackerCompaniesResponse200 | AddTrackerCompaniesResponse400 | AddTrackerCompaniesResponse401 | AddTrackerCompaniesResponse402 | AddTrackerCompaniesResponse403 | AddTrackerCompaniesResponse404 | AddTrackerCompaniesResponse422 | AddTrackerCompaniesResponse429 | AddTrackerCompaniesResponse500 | AddTrackerCompaniesResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTrackerCompaniesBody,
) -> Response[
    AddTrackerCompaniesResponse200
    | AddTrackerCompaniesResponse400
    | AddTrackerCompaniesResponse401
    | AddTrackerCompaniesResponse402
    | AddTrackerCompaniesResponse403
    | AddTrackerCompaniesResponse404
    | AddTrackerCompaniesResponse422
    | AddTrackerCompaniesResponse429
    | AddTrackerCompaniesResponse500
    | AddTrackerCompaniesResponse503
]:
    r"""Add companies to tracker list

     Add companies to a company tracker list. Identify companies by LinkedIn URL, organization ID, slug,
    or website domain. At least one identifier is required per company.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (AddTrackerCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddTrackerCompaniesResponse200 | AddTrackerCompaniesResponse400 | AddTrackerCompaniesResponse401 | AddTrackerCompaniesResponse402 | AddTrackerCompaniesResponse403 | AddTrackerCompaniesResponse404 | AddTrackerCompaniesResponse422 | AddTrackerCompaniesResponse429 | AddTrackerCompaniesResponse500 | AddTrackerCompaniesResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTrackerCompaniesBody,
) -> (
    AddTrackerCompaniesResponse200
    | AddTrackerCompaniesResponse400
    | AddTrackerCompaniesResponse401
    | AddTrackerCompaniesResponse402
    | AddTrackerCompaniesResponse403
    | AddTrackerCompaniesResponse404
    | AddTrackerCompaniesResponse422
    | AddTrackerCompaniesResponse429
    | AddTrackerCompaniesResponse500
    | AddTrackerCompaniesResponse503
    | None
):
    r"""Add companies to tracker list

     Add companies to a company tracker list. Identify companies by LinkedIn URL, organization ID, slug,
    or website domain. At least one identifier is required per company.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (AddTrackerCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddTrackerCompaniesResponse200 | AddTrackerCompaniesResponse400 | AddTrackerCompaniesResponse401 | AddTrackerCompaniesResponse402 | AddTrackerCompaniesResponse403 | AddTrackerCompaniesResponse404 | AddTrackerCompaniesResponse422 | AddTrackerCompaniesResponse429 | AddTrackerCompaniesResponse500 | AddTrackerCompaniesResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
