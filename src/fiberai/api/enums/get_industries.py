from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_industries_response_200 import GetIndustriesResponse200
from ...models.get_industries_response_400 import GetIndustriesResponse400
from ...models.get_industries_response_401 import GetIndustriesResponse401
from ...models.get_industries_response_402 import GetIndustriesResponse402
from ...models.get_industries_response_403 import GetIndustriesResponse403
from ...models.get_industries_response_404 import GetIndustriesResponse404
from ...models.get_industries_response_429 import GetIndustriesResponse429
from ...models.get_industries_response_500 import GetIndustriesResponse500
from typing import cast



def _get_kwargs(
    *,
    api_key: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["apiKey"] = api_key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/enums/industries",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]]:
    if response.status_code == 200:
        response_200 = GetIndustriesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetIndustriesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetIndustriesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = GetIndustriesResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = GetIndustriesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetIndustriesResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetIndustriesResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetIndustriesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: str,

) -> Response[Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]]:
    r""" List industries

     Get lists of various industry categorizations. Useful for our company search API.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]]
     """


    kwargs = _get_kwargs(
        api_key=api_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: str,

) -> Optional[Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]]:
    r""" List industries

     Get lists of various industry categorizations. Useful for our company search API.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]
     """


    return sync_detailed(
        client=client,
api_key=api_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: str,

) -> Response[Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]]:
    r""" List industries

     Get lists of various industry categorizations. Useful for our company search API.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]]
     """


    kwargs = _get_kwargs(
        api_key=api_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: str,

) -> Optional[Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]]:
    r""" List industries

     Get lists of various industry categorizations. Useful for our company search API.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetIndustriesResponse200, GetIndustriesResponse400, GetIndustriesResponse401, GetIndustriesResponse402, GetIndustriesResponse403, GetIndustriesResponse404, GetIndustriesResponse429, GetIndustriesResponse500]
     """


    return (await asyncio_detailed(
        client=client,
api_key=api_key,

    )).parsed
