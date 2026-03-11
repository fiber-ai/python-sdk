from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_companies_to_exclusion_list_body import AddCompaniesToExclusionListBody
from ...models.add_companies_to_exclusion_list_response_200 import AddCompaniesToExclusionListResponse200
from ...models.add_companies_to_exclusion_list_response_400 import AddCompaniesToExclusionListResponse400
from ...models.add_companies_to_exclusion_list_response_401 import AddCompaniesToExclusionListResponse401
from ...models.add_companies_to_exclusion_list_response_402 import AddCompaniesToExclusionListResponse402
from ...models.add_companies_to_exclusion_list_response_403 import AddCompaniesToExclusionListResponse403
from ...models.add_companies_to_exclusion_list_response_404 import AddCompaniesToExclusionListResponse404
from ...models.add_companies_to_exclusion_list_response_429 import AddCompaniesToExclusionListResponse429
from ...models.add_companies_to_exclusion_list_response_500 import AddCompaniesToExclusionListResponse500
from ...models.add_companies_to_exclusion_list_response_503 import AddCompaniesToExclusionListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: AddCompaniesToExclusionListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exclusions/companies/add-to-list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddCompaniesToExclusionListResponse200
    | AddCompaniesToExclusionListResponse400
    | AddCompaniesToExclusionListResponse401
    | AddCompaniesToExclusionListResponse402
    | AddCompaniesToExclusionListResponse403
    | AddCompaniesToExclusionListResponse404
    | AddCompaniesToExclusionListResponse429
    | AddCompaniesToExclusionListResponse500
    | AddCompaniesToExclusionListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AddCompaniesToExclusionListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddCompaniesToExclusionListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddCompaniesToExclusionListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = AddCompaniesToExclusionListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = AddCompaniesToExclusionListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddCompaniesToExclusionListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = AddCompaniesToExclusionListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AddCompaniesToExclusionListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AddCompaniesToExclusionListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddCompaniesToExclusionListResponse200
    | AddCompaniesToExclusionListResponse400
    | AddCompaniesToExclusionListResponse401
    | AddCompaniesToExclusionListResponse402
    | AddCompaniesToExclusionListResponse403
    | AddCompaniesToExclusionListResponse404
    | AddCompaniesToExclusionListResponse429
    | AddCompaniesToExclusionListResponse500
    | AddCompaniesToExclusionListResponse503
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
    body: AddCompaniesToExclusionListBody,
) -> Response[
    AddCompaniesToExclusionListResponse200
    | AddCompaniesToExclusionListResponse400
    | AddCompaniesToExclusionListResponse401
    | AddCompaniesToExclusionListResponse402
    | AddCompaniesToExclusionListResponse403
    | AddCompaniesToExclusionListResponse404
    | AddCompaniesToExclusionListResponse429
    | AddCompaniesToExclusionListResponse500
    | AddCompaniesToExclusionListResponse503
]:
    r"""Add companies to a company exclusion list

     Add companies to a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddCompaniesToExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddCompaniesToExclusionListResponse200 | AddCompaniesToExclusionListResponse400 | AddCompaniesToExclusionListResponse401 | AddCompaniesToExclusionListResponse402 | AddCompaniesToExclusionListResponse403 | AddCompaniesToExclusionListResponse404 | AddCompaniesToExclusionListResponse429 | AddCompaniesToExclusionListResponse500 | AddCompaniesToExclusionListResponse503]
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
    body: AddCompaniesToExclusionListBody,
) -> (
    AddCompaniesToExclusionListResponse200
    | AddCompaniesToExclusionListResponse400
    | AddCompaniesToExclusionListResponse401
    | AddCompaniesToExclusionListResponse402
    | AddCompaniesToExclusionListResponse403
    | AddCompaniesToExclusionListResponse404
    | AddCompaniesToExclusionListResponse429
    | AddCompaniesToExclusionListResponse500
    | AddCompaniesToExclusionListResponse503
    | None
):
    r"""Add companies to a company exclusion list

     Add companies to a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddCompaniesToExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddCompaniesToExclusionListResponse200 | AddCompaniesToExclusionListResponse400 | AddCompaniesToExclusionListResponse401 | AddCompaniesToExclusionListResponse402 | AddCompaniesToExclusionListResponse403 | AddCompaniesToExclusionListResponse404 | AddCompaniesToExclusionListResponse429 | AddCompaniesToExclusionListResponse500 | AddCompaniesToExclusionListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddCompaniesToExclusionListBody,
) -> Response[
    AddCompaniesToExclusionListResponse200
    | AddCompaniesToExclusionListResponse400
    | AddCompaniesToExclusionListResponse401
    | AddCompaniesToExclusionListResponse402
    | AddCompaniesToExclusionListResponse403
    | AddCompaniesToExclusionListResponse404
    | AddCompaniesToExclusionListResponse429
    | AddCompaniesToExclusionListResponse500
    | AddCompaniesToExclusionListResponse503
]:
    r"""Add companies to a company exclusion list

     Add companies to a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddCompaniesToExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddCompaniesToExclusionListResponse200 | AddCompaniesToExclusionListResponse400 | AddCompaniesToExclusionListResponse401 | AddCompaniesToExclusionListResponse402 | AddCompaniesToExclusionListResponse403 | AddCompaniesToExclusionListResponse404 | AddCompaniesToExclusionListResponse429 | AddCompaniesToExclusionListResponse500 | AddCompaniesToExclusionListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AddCompaniesToExclusionListBody,
) -> (
    AddCompaniesToExclusionListResponse200
    | AddCompaniesToExclusionListResponse400
    | AddCompaniesToExclusionListResponse401
    | AddCompaniesToExclusionListResponse402
    | AddCompaniesToExclusionListResponse403
    | AddCompaniesToExclusionListResponse404
    | AddCompaniesToExclusionListResponse429
    | AddCompaniesToExclusionListResponse500
    | AddCompaniesToExclusionListResponse503
    | None
):
    r"""Add companies to a company exclusion list

     Add companies to a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddCompaniesToExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddCompaniesToExclusionListResponse200 | AddCompaniesToExclusionListResponse400 | AddCompaniesToExclusionListResponse401 | AddCompaniesToExclusionListResponse402 | AddCompaniesToExclusionListResponse403 | AddCompaniesToExclusionListResponse404 | AddCompaniesToExclusionListResponse429 | AddCompaniesToExclusionListResponse500 | AddCompaniesToExclusionListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
