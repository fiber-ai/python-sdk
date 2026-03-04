from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_saved_search_body import GetSavedSearchBody
from ...models.get_saved_search_response_400 import GetSavedSearchResponse400
from ...models.get_saved_search_response_401 import GetSavedSearchResponse401
from ...models.get_saved_search_response_402 import GetSavedSearchResponse402
from ...models.get_saved_search_response_403 import GetSavedSearchResponse403
from ...models.get_saved_search_response_404 import GetSavedSearchResponse404
from ...models.get_saved_search_response_429 import GetSavedSearchResponse429
from ...models.get_saved_search_response_500 import GetSavedSearchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GetSavedSearchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/get",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]]:
    if response.status_code == 400:
        response_400 = GetSavedSearchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetSavedSearchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = GetSavedSearchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = GetSavedSearchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetSavedSearchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetSavedSearchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetSavedSearchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetSavedSearchBody,

) -> Response[Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]]:
    r""" Get saved search

     Get all details for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]]
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
    body: GetSavedSearchBody,

) -> Optional[Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]]:
    r""" Get saved search

     Get all details for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetSavedSearchBody,

) -> Response[Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]]:
    r""" Get saved search

     Get all details for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]]
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
    body: GetSavedSearchBody,

) -> Optional[Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]]:
    r""" Get saved search

     Get all details for a specific saved search

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSavedSearchResponse400, GetSavedSearchResponse401, GetSavedSearchResponse402, GetSavedSearchResponse403, GetSavedSearchResponse404, GetSavedSearchResponse429, GetSavedSearchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
