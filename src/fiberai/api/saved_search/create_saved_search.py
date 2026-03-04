from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_saved_search_body import CreateSavedSearchBody
from ...models.create_saved_search_response_200 import CreateSavedSearchResponse200
from ...models.create_saved_search_response_400 import CreateSavedSearchResponse400
from ...models.create_saved_search_response_401 import CreateSavedSearchResponse401
from ...models.create_saved_search_response_402 import CreateSavedSearchResponse402
from ...models.create_saved_search_response_403 import CreateSavedSearchResponse403
from ...models.create_saved_search_response_404 import CreateSavedSearchResponse404
from ...models.create_saved_search_response_429 import CreateSavedSearchResponse429
from ...models.create_saved_search_response_500 import CreateSavedSearchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: CreateSavedSearchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/create",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]]:
    if response.status_code == 200:
        response_200 = CreateSavedSearchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = CreateSavedSearchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateSavedSearchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = CreateSavedSearchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = CreateSavedSearchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CreateSavedSearchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = CreateSavedSearchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = CreateSavedSearchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateSavedSearchBody,

) -> Response[Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]]:
    r""" Create saved search

     Create a new saved search. Given search params, it automatically re-runs it periodically and tells
    you which new people and/or companies fit your parameters over time (and also who drops out or
    returns). You are charged for each new prospect or company we find, depending on your desired type.
    You can also manually run the saved search if you don't want to wait for the next auto-run.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per prospect/company found in search&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]]
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
    body: CreateSavedSearchBody,

) -> Optional[Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]]:
    r""" Create saved search

     Create a new saved search. Given search params, it automatically re-runs it periodically and tells
    you which new people and/or companies fit your parameters over time (and also who drops out or
    returns). You are charged for each new prospect or company we find, depending on your desired type.
    You can also manually run the saved search if you don't want to wait for the next auto-run.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per prospect/company found in search&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateSavedSearchBody,

) -> Response[Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]]:
    r""" Create saved search

     Create a new saved search. Given search params, it automatically re-runs it periodically and tells
    you which new people and/or companies fit your parameters over time (and also who drops out or
    returns). You are charged for each new prospect or company we find, depending on your desired type.
    You can also manually run the saved search if you don't want to wait for the next auto-run.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per prospect/company found in search&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]]
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
    body: CreateSavedSearchBody,

) -> Optional[Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]]:
    r""" Create saved search

     Create a new saved search. Given search params, it automatically re-runs it periodically and tells
    you which new people and/or companies fit your parameters over time (and also who drops out or
    returns). You are charged for each new prospect or company we find, depending on your desired type.
    You can also manually run the saved search if you don't want to wait for the next auto-run.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per prospect/company found in search&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateSavedSearchResponse200, CreateSavedSearchResponse400, CreateSavedSearchResponse401, CreateSavedSearchResponse402, CreateSavedSearchResponse403, CreateSavedSearchResponse404, CreateSavedSearchResponse429, CreateSavedSearchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
