from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_saved_search_runs_body import ListSavedSearchRunsBody
from ...models.list_saved_search_runs_response_200 import ListSavedSearchRunsResponse200
from ...models.list_saved_search_runs_response_400 import ListSavedSearchRunsResponse400
from ...models.list_saved_search_runs_response_401 import ListSavedSearchRunsResponse401
from ...models.list_saved_search_runs_response_402 import ListSavedSearchRunsResponse402
from ...models.list_saved_search_runs_response_403 import ListSavedSearchRunsResponse403
from ...models.list_saved_search_runs_response_404 import ListSavedSearchRunsResponse404
from ...models.list_saved_search_runs_response_429 import ListSavedSearchRunsResponse429
from ...models.list_saved_search_runs_response_500 import ListSavedSearchRunsResponse500
from typing import cast



def _get_kwargs(
    *,
    body: ListSavedSearchRunsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/run/list",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]]:
    if response.status_code == 200:
        response_200 = ListSavedSearchRunsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ListSavedSearchRunsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ListSavedSearchRunsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = ListSavedSearchRunsResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = ListSavedSearchRunsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ListSavedSearchRunsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = ListSavedSearchRunsResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ListSavedSearchRunsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ListSavedSearchRunsBody,

) -> Response[Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]]:
    r""" List saved search runs

     List saved search runs

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListSavedSearchRunsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]]
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
    body: ListSavedSearchRunsBody,

) -> Optional[Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]]:
    r""" List saved search runs

     List saved search runs

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListSavedSearchRunsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ListSavedSearchRunsBody,

) -> Response[Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]]:
    r""" List saved search runs

     List saved search runs

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListSavedSearchRunsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]]
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
    body: ListSavedSearchRunsBody,

) -> Optional[Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]]:
    r""" List saved search runs

     List saved search runs

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListSavedSearchRunsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListSavedSearchRunsResponse200, ListSavedSearchRunsResponse400, ListSavedSearchRunsResponse401, ListSavedSearchRunsResponse402, ListSavedSearchRunsResponse403, ListSavedSearchRunsResponse404, ListSavedSearchRunsResponse429, ListSavedSearchRunsResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
