from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_company_exclusion_list_body import CreateCompanyExclusionListBody
from ...models.create_company_exclusion_list_response_200 import CreateCompanyExclusionListResponse200
from ...models.create_company_exclusion_list_response_400 import CreateCompanyExclusionListResponse400
from ...models.create_company_exclusion_list_response_401 import CreateCompanyExclusionListResponse401
from ...models.create_company_exclusion_list_response_402 import CreateCompanyExclusionListResponse402
from ...models.create_company_exclusion_list_response_403 import CreateCompanyExclusionListResponse403
from ...models.create_company_exclusion_list_response_404 import CreateCompanyExclusionListResponse404
from ...models.create_company_exclusion_list_response_429 import CreateCompanyExclusionListResponse429
from ...models.create_company_exclusion_list_response_500 import CreateCompanyExclusionListResponse500
from ...models.create_company_exclusion_list_response_503 import CreateCompanyExclusionListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCompanyExclusionListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exclusions/companies/create-list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateCompanyExclusionListResponse200
    | CreateCompanyExclusionListResponse400
    | CreateCompanyExclusionListResponse401
    | CreateCompanyExclusionListResponse402
    | CreateCompanyExclusionListResponse403
    | CreateCompanyExclusionListResponse404
    | CreateCompanyExclusionListResponse429
    | CreateCompanyExclusionListResponse500
    | CreateCompanyExclusionListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CreateCompanyExclusionListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateCompanyExclusionListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateCompanyExclusionListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CreateCompanyExclusionListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CreateCompanyExclusionListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateCompanyExclusionListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CreateCompanyExclusionListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateCompanyExclusionListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateCompanyExclusionListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateCompanyExclusionListResponse200
    | CreateCompanyExclusionListResponse400
    | CreateCompanyExclusionListResponse401
    | CreateCompanyExclusionListResponse402
    | CreateCompanyExclusionListResponse403
    | CreateCompanyExclusionListResponse404
    | CreateCompanyExclusionListResponse429
    | CreateCompanyExclusionListResponse500
    | CreateCompanyExclusionListResponse503
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
    body: CreateCompanyExclusionListBody,
) -> Response[
    CreateCompanyExclusionListResponse200
    | CreateCompanyExclusionListResponse400
    | CreateCompanyExclusionListResponse401
    | CreateCompanyExclusionListResponse402
    | CreateCompanyExclusionListResponse403
    | CreateCompanyExclusionListResponse404
    | CreateCompanyExclusionListResponse429
    | CreateCompanyExclusionListResponse500
    | CreateCompanyExclusionListResponse503
]:
    r"""Create company exclusion list

     Create a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateCompanyExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCompanyExclusionListResponse200 | CreateCompanyExclusionListResponse400 | CreateCompanyExclusionListResponse401 | CreateCompanyExclusionListResponse402 | CreateCompanyExclusionListResponse403 | CreateCompanyExclusionListResponse404 | CreateCompanyExclusionListResponse429 | CreateCompanyExclusionListResponse500 | CreateCompanyExclusionListResponse503]
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
    body: CreateCompanyExclusionListBody,
) -> (
    CreateCompanyExclusionListResponse200
    | CreateCompanyExclusionListResponse400
    | CreateCompanyExclusionListResponse401
    | CreateCompanyExclusionListResponse402
    | CreateCompanyExclusionListResponse403
    | CreateCompanyExclusionListResponse404
    | CreateCompanyExclusionListResponse429
    | CreateCompanyExclusionListResponse500
    | CreateCompanyExclusionListResponse503
    | None
):
    r"""Create company exclusion list

     Create a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateCompanyExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCompanyExclusionListResponse200 | CreateCompanyExclusionListResponse400 | CreateCompanyExclusionListResponse401 | CreateCompanyExclusionListResponse402 | CreateCompanyExclusionListResponse403 | CreateCompanyExclusionListResponse404 | CreateCompanyExclusionListResponse429 | CreateCompanyExclusionListResponse500 | CreateCompanyExclusionListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCompanyExclusionListBody,
) -> Response[
    CreateCompanyExclusionListResponse200
    | CreateCompanyExclusionListResponse400
    | CreateCompanyExclusionListResponse401
    | CreateCompanyExclusionListResponse402
    | CreateCompanyExclusionListResponse403
    | CreateCompanyExclusionListResponse404
    | CreateCompanyExclusionListResponse429
    | CreateCompanyExclusionListResponse500
    | CreateCompanyExclusionListResponse503
]:
    r"""Create company exclusion list

     Create a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateCompanyExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCompanyExclusionListResponse200 | CreateCompanyExclusionListResponse400 | CreateCompanyExclusionListResponse401 | CreateCompanyExclusionListResponse402 | CreateCompanyExclusionListResponse403 | CreateCompanyExclusionListResponse404 | CreateCompanyExclusionListResponse429 | CreateCompanyExclusionListResponse500 | CreateCompanyExclusionListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCompanyExclusionListBody,
) -> (
    CreateCompanyExclusionListResponse200
    | CreateCompanyExclusionListResponse400
    | CreateCompanyExclusionListResponse401
    | CreateCompanyExclusionListResponse402
    | CreateCompanyExclusionListResponse403
    | CreateCompanyExclusionListResponse404
    | CreateCompanyExclusionListResponse429
    | CreateCompanyExclusionListResponse500
    | CreateCompanyExclusionListResponse503
    | None
):
    r"""Create company exclusion list

     Create a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateCompanyExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCompanyExclusionListResponse200 | CreateCompanyExclusionListResponse400 | CreateCompanyExclusionListResponse401 | CreateCompanyExclusionListResponse402 | CreateCompanyExclusionListResponse403 | CreateCompanyExclusionListResponse404 | CreateCompanyExclusionListResponse429 | CreateCompanyExclusionListResponse500 | CreateCompanyExclusionListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
