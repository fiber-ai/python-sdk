from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_saved_search_run_status_body import GetSavedSearchRunStatusBody
from ...models.get_saved_search_run_status_response_200 import GetSavedSearchRunStatusResponse200
from ...models.get_saved_search_run_status_response_400 import GetSavedSearchRunStatusResponse400
from ...models.get_saved_search_run_status_response_401 import GetSavedSearchRunStatusResponse401
from ...models.get_saved_search_run_status_response_402 import GetSavedSearchRunStatusResponse402
from ...models.get_saved_search_run_status_response_403 import GetSavedSearchRunStatusResponse403
from ...models.get_saved_search_run_status_response_404 import GetSavedSearchRunStatusResponse404
from ...models.get_saved_search_run_status_response_429 import GetSavedSearchRunStatusResponse429
from ...models.get_saved_search_run_status_response_500 import GetSavedSearchRunStatusResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GetSavedSearchRunStatusBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/run/status",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]]:
    if response.status_code == 200:
        response_200 = GetSavedSearchRunStatusResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetSavedSearchRunStatusResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetSavedSearchRunStatusResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = GetSavedSearchRunStatusResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = GetSavedSearchRunStatusResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetSavedSearchRunStatusResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetSavedSearchRunStatusResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetSavedSearchRunStatusResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetSavedSearchRunStatusBody,

) -> Response[Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]]:
    r""" Get saved search run status

     Returns the execution status and metadata for a saved search run, including start time, completion
    time (if finished), and current status (NOT_STARTED, PROCESSING, COMPLETED, or FAILED)

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]]
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
    body: GetSavedSearchRunStatusBody,

) -> Optional[Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]]:
    r""" Get saved search run status

     Returns the execution status and metadata for a saved search run, including start time, completion
    time (if finished), and current status (NOT_STARTED, PROCESSING, COMPLETED, or FAILED)

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetSavedSearchRunStatusBody,

) -> Response[Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]]:
    r""" Get saved search run status

     Returns the execution status and metadata for a saved search run, including start time, completion
    time (if finished), and current status (NOT_STARTED, PROCESSING, COMPLETED, or FAILED)

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]]
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
    body: GetSavedSearchRunStatusBody,

) -> Optional[Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]]:
    r""" Get saved search run status

     Returns the execution status and metadata for a saved search run, including start time, completion
    time (if finished), and current status (NOT_STARTED, PROCESSING, COMPLETED, or FAILED)

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSavedSearchRunStatusResponse200, GetSavedSearchRunStatusResponse400, GetSavedSearchRunStatusResponse401, GetSavedSearchRunStatusResponse402, GetSavedSearchRunStatusResponse403, GetSavedSearchRunStatusResponse404, GetSavedSearchRunStatusResponse429, GetSavedSearchRunStatusResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
