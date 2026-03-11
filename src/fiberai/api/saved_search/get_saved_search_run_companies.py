from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_saved_search_run_companies_body import GetSavedSearchRunCompaniesBody
from ...models.get_saved_search_run_companies_response_200 import GetSavedSearchRunCompaniesResponse200
from ...models.get_saved_search_run_companies_response_400 import GetSavedSearchRunCompaniesResponse400
from ...models.get_saved_search_run_companies_response_401 import GetSavedSearchRunCompaniesResponse401
from ...models.get_saved_search_run_companies_response_402 import GetSavedSearchRunCompaniesResponse402
from ...models.get_saved_search_run_companies_response_403 import GetSavedSearchRunCompaniesResponse403
from ...models.get_saved_search_run_companies_response_404 import GetSavedSearchRunCompaniesResponse404
from ...models.get_saved_search_run_companies_response_429 import GetSavedSearchRunCompaniesResponse429
from ...models.get_saved_search_run_companies_response_500 import GetSavedSearchRunCompaniesResponse500
from ...models.get_saved_search_run_companies_response_503 import GetSavedSearchRunCompaniesResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetSavedSearchRunCompaniesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/run/companies",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSavedSearchRunCompaniesResponse200
    | GetSavedSearchRunCompaniesResponse400
    | GetSavedSearchRunCompaniesResponse401
    | GetSavedSearchRunCompaniesResponse402
    | GetSavedSearchRunCompaniesResponse403
    | GetSavedSearchRunCompaniesResponse404
    | GetSavedSearchRunCompaniesResponse429
    | GetSavedSearchRunCompaniesResponse500
    | GetSavedSearchRunCompaniesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetSavedSearchRunCompaniesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSavedSearchRunCompaniesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSavedSearchRunCompaniesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetSavedSearchRunCompaniesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetSavedSearchRunCompaniesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSavedSearchRunCompaniesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetSavedSearchRunCompaniesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetSavedSearchRunCompaniesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSavedSearchRunCompaniesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSavedSearchRunCompaniesResponse200
    | GetSavedSearchRunCompaniesResponse400
    | GetSavedSearchRunCompaniesResponse401
    | GetSavedSearchRunCompaniesResponse402
    | GetSavedSearchRunCompaniesResponse403
    | GetSavedSearchRunCompaniesResponse404
    | GetSavedSearchRunCompaniesResponse429
    | GetSavedSearchRunCompaniesResponse500
    | GetSavedSearchRunCompaniesResponse503
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
    body: GetSavedSearchRunCompaniesBody,
) -> Response[
    GetSavedSearchRunCompaniesResponse200
    | GetSavedSearchRunCompaniesResponse400
    | GetSavedSearchRunCompaniesResponse401
    | GetSavedSearchRunCompaniesResponse402
    | GetSavedSearchRunCompaniesResponse403
    | GetSavedSearchRunCompaniesResponse404
    | GetSavedSearchRunCompaniesResponse429
    | GetSavedSearchRunCompaniesResponse500
    | GetSavedSearchRunCompaniesResponse503
]:
    r"""Get saved search run companies

     Get the companies found for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavedSearchRunCompaniesResponse200 | GetSavedSearchRunCompaniesResponse400 | GetSavedSearchRunCompaniesResponse401 | GetSavedSearchRunCompaniesResponse402 | GetSavedSearchRunCompaniesResponse403 | GetSavedSearchRunCompaniesResponse404 | GetSavedSearchRunCompaniesResponse429 | GetSavedSearchRunCompaniesResponse500 | GetSavedSearchRunCompaniesResponse503]
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
    body: GetSavedSearchRunCompaniesBody,
) -> (
    GetSavedSearchRunCompaniesResponse200
    | GetSavedSearchRunCompaniesResponse400
    | GetSavedSearchRunCompaniesResponse401
    | GetSavedSearchRunCompaniesResponse402
    | GetSavedSearchRunCompaniesResponse403
    | GetSavedSearchRunCompaniesResponse404
    | GetSavedSearchRunCompaniesResponse429
    | GetSavedSearchRunCompaniesResponse500
    | GetSavedSearchRunCompaniesResponse503
    | None
):
    r"""Get saved search run companies

     Get the companies found for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavedSearchRunCompaniesResponse200 | GetSavedSearchRunCompaniesResponse400 | GetSavedSearchRunCompaniesResponse401 | GetSavedSearchRunCompaniesResponse402 | GetSavedSearchRunCompaniesResponse403 | GetSavedSearchRunCompaniesResponse404 | GetSavedSearchRunCompaniesResponse429 | GetSavedSearchRunCompaniesResponse500 | GetSavedSearchRunCompaniesResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetSavedSearchRunCompaniesBody,
) -> Response[
    GetSavedSearchRunCompaniesResponse200
    | GetSavedSearchRunCompaniesResponse400
    | GetSavedSearchRunCompaniesResponse401
    | GetSavedSearchRunCompaniesResponse402
    | GetSavedSearchRunCompaniesResponse403
    | GetSavedSearchRunCompaniesResponse404
    | GetSavedSearchRunCompaniesResponse429
    | GetSavedSearchRunCompaniesResponse500
    | GetSavedSearchRunCompaniesResponse503
]:
    r"""Get saved search run companies

     Get the companies found for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavedSearchRunCompaniesResponse200 | GetSavedSearchRunCompaniesResponse400 | GetSavedSearchRunCompaniesResponse401 | GetSavedSearchRunCompaniesResponse402 | GetSavedSearchRunCompaniesResponse403 | GetSavedSearchRunCompaniesResponse404 | GetSavedSearchRunCompaniesResponse429 | GetSavedSearchRunCompaniesResponse500 | GetSavedSearchRunCompaniesResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetSavedSearchRunCompaniesBody,
) -> (
    GetSavedSearchRunCompaniesResponse200
    | GetSavedSearchRunCompaniesResponse400
    | GetSavedSearchRunCompaniesResponse401
    | GetSavedSearchRunCompaniesResponse402
    | GetSavedSearchRunCompaniesResponse403
    | GetSavedSearchRunCompaniesResponse404
    | GetSavedSearchRunCompaniesResponse429
    | GetSavedSearchRunCompaniesResponse500
    | GetSavedSearchRunCompaniesResponse503
    | None
):
    r"""Get saved search run companies

     Get the companies found for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavedSearchRunCompaniesResponse200 | GetSavedSearchRunCompaniesResponse400 | GetSavedSearchRunCompaniesResponse401 | GetSavedSearchRunCompaniesResponse402 | GetSavedSearchRunCompaniesResponse403 | GetSavedSearchRunCompaniesResponse404 | GetSavedSearchRunCompaniesResponse429 | GetSavedSearchRunCompaniesResponse500 | GetSavedSearchRunCompaniesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
