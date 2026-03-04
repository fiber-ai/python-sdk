from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_current_companies_in_saved_search_body import GetCurrentCompaniesInSavedSearchBody
from ...models.get_current_companies_in_saved_search_response_200 import GetCurrentCompaniesInSavedSearchResponse200
from ...models.get_current_companies_in_saved_search_response_400 import GetCurrentCompaniesInSavedSearchResponse400
from ...models.get_current_companies_in_saved_search_response_401 import GetCurrentCompaniesInSavedSearchResponse401
from ...models.get_current_companies_in_saved_search_response_402 import GetCurrentCompaniesInSavedSearchResponse402
from ...models.get_current_companies_in_saved_search_response_403 import GetCurrentCompaniesInSavedSearchResponse403
from ...models.get_current_companies_in_saved_search_response_404 import GetCurrentCompaniesInSavedSearchResponse404
from ...models.get_current_companies_in_saved_search_response_429 import GetCurrentCompaniesInSavedSearchResponse429
from ...models.get_current_companies_in_saved_search_response_500 import GetCurrentCompaniesInSavedSearchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GetCurrentCompaniesInSavedSearchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/current/companies",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]]:
    if response.status_code == 200:
        response_200 = GetCurrentCompaniesInSavedSearchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetCurrentCompaniesInSavedSearchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetCurrentCompaniesInSavedSearchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = GetCurrentCompaniesInSavedSearchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = GetCurrentCompaniesInSavedSearchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetCurrentCompaniesInSavedSearchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetCurrentCompaniesInSavedSearchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetCurrentCompaniesInSavedSearchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetCurrentCompaniesInSavedSearchBody,

) -> Response[Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]]:
    r""" Get current companies in saved search

     Get current companies found for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCurrentCompaniesInSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]]
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
    client: Union[AuthenticatedClient, Client],
    body: GetCurrentCompaniesInSavedSearchBody,

) -> Optional[Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]]:
    r""" Get current companies in saved search

     Get current companies found for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCurrentCompaniesInSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetCurrentCompaniesInSavedSearchBody,

) -> Response[Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]]:
    r""" Get current companies in saved search

     Get current companies found for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCurrentCompaniesInSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetCurrentCompaniesInSavedSearchBody,

) -> Optional[Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]]:
    r""" Get current companies in saved search

     Get current companies found for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCurrentCompaniesInSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCurrentCompaniesInSavedSearchResponse200, GetCurrentCompaniesInSavedSearchResponse400, GetCurrentCompaniesInSavedSearchResponse401, GetCurrentCompaniesInSavedSearchResponse402, GetCurrentCompaniesInSavedSearchResponse403, GetCurrentCompaniesInSavedSearchResponse404, GetCurrentCompaniesInSavedSearchResponse429, GetCurrentCompaniesInSavedSearchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
