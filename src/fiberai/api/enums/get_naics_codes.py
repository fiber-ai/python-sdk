from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_naics_codes_response_200 import GetNaicsCodesResponse200
from ...models.get_naics_codes_response_400 import GetNaicsCodesResponse400
from ...models.get_naics_codes_response_401 import GetNaicsCodesResponse401
from ...models.get_naics_codes_response_402 import GetNaicsCodesResponse402
from ...models.get_naics_codes_response_403 import GetNaicsCodesResponse403
from ...models.get_naics_codes_response_404 import GetNaicsCodesResponse404
from ...models.get_naics_codes_response_429 import GetNaicsCodesResponse429
from ...models.get_naics_codes_response_500 import GetNaicsCodesResponse500
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
        "url": "/v1/enums/naics-codes",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]]:
    if response.status_code == 200:
        response_200 = GetNaicsCodesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetNaicsCodesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetNaicsCodesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = GetNaicsCodesResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = GetNaicsCodesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetNaicsCodesResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetNaicsCodesResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetNaicsCodesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]]:
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

) -> Response[Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]]:
    r""" List NAICS codes

     Get all NAICS (North American Industry Classification System) codes from the 2017 version. Returns
    both the code and its corresponding title/description. You can use this in our company search APIs.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]]
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

) -> Optional[Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]]:
    r""" List NAICS codes

     Get all NAICS (North American Industry Classification System) codes from the 2017 version. Returns
    both the code and its corresponding title/description. You can use this in our company search APIs.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]
     """


    return sync_detailed(
        client=client,
api_key=api_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: str,

) -> Response[Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]]:
    r""" List NAICS codes

     Get all NAICS (North American Industry Classification System) codes from the 2017 version. Returns
    both the code and its corresponding title/description. You can use this in our company search APIs.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]]
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

) -> Optional[Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]]:
    r""" List NAICS codes

     Get all NAICS (North American Industry Classification System) codes from the 2017 version. Returns
    both the code and its corresponding title/description. You can use this in our company search APIs.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetNaicsCodesResponse200, GetNaicsCodesResponse400, GetNaicsCodesResponse401, GetNaicsCodesResponse402, GetNaicsCodesResponse403, GetNaicsCodesResponse404, GetNaicsCodesResponse429, GetNaicsCodesResponse500]
     """


    return (await asyncio_detailed(
        client=client,
api_key=api_key,

    )).parsed
