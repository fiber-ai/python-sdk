from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_saved_search_run_profiles_body import GetSavedSearchRunProfilesBody
from ...models.get_saved_search_run_profiles_response_200 import GetSavedSearchRunProfilesResponse200
from ...models.get_saved_search_run_profiles_response_400 import GetSavedSearchRunProfilesResponse400
from ...models.get_saved_search_run_profiles_response_401 import GetSavedSearchRunProfilesResponse401
from ...models.get_saved_search_run_profiles_response_402 import GetSavedSearchRunProfilesResponse402
from ...models.get_saved_search_run_profiles_response_403 import GetSavedSearchRunProfilesResponse403
from ...models.get_saved_search_run_profiles_response_404 import GetSavedSearchRunProfilesResponse404
from ...models.get_saved_search_run_profiles_response_429 import GetSavedSearchRunProfilesResponse429
from ...models.get_saved_search_run_profiles_response_500 import GetSavedSearchRunProfilesResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GetSavedSearchRunProfilesBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/run/profiles",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]]:
    if response.status_code == 200:
        response_200 = GetSavedSearchRunProfilesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetSavedSearchRunProfilesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetSavedSearchRunProfilesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = GetSavedSearchRunProfilesResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = GetSavedSearchRunProfilesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetSavedSearchRunProfilesResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetSavedSearchRunProfilesResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetSavedSearchRunProfilesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetSavedSearchRunProfilesBody,

) -> Response[Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]]:
    r""" Get saved search run profiles

     Get the profiles found for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunProfilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]]
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
    body: GetSavedSearchRunProfilesBody,

) -> Optional[Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]]:
    r""" Get saved search run profiles

     Get the profiles found for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunProfilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetSavedSearchRunProfilesBody,

) -> Response[Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]]:
    r""" Get saved search run profiles

     Get the profiles found for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunProfilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]]
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
    body: GetSavedSearchRunProfilesBody,

) -> Optional[Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]]:
    r""" Get saved search run profiles

     Get the profiles found for a specific saved search run

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetSavedSearchRunProfilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSavedSearchRunProfilesResponse200, GetSavedSearchRunProfilesResponse400, GetSavedSearchRunProfilesResponse401, GetSavedSearchRunProfilesResponse402, GetSavedSearchRunProfilesResponse403, GetSavedSearchRunProfilesResponse404, GetSavedSearchRunProfilesResponse429, GetSavedSearchRunProfilesResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
