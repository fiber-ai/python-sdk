from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_org_credits_response_200 import GetOrgCreditsResponse200
from ...models.get_org_credits_response_400 import GetOrgCreditsResponse400
from ...models.get_org_credits_response_401 import GetOrgCreditsResponse401
from ...models.get_org_credits_response_402 import GetOrgCreditsResponse402
from ...models.get_org_credits_response_403 import GetOrgCreditsResponse403
from ...models.get_org_credits_response_404 import GetOrgCreditsResponse404
from ...models.get_org_credits_response_429 import GetOrgCreditsResponse429
from ...models.get_org_credits_response_500 import GetOrgCreditsResponse500
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
        "url": "/v1/get-org-credits",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]]:
    if response.status_code == 200:
        response_200 = GetOrgCreditsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetOrgCreditsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetOrgCreditsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = GetOrgCreditsResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = GetOrgCreditsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetOrgCreditsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetOrgCreditsResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetOrgCreditsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]]:
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

) -> Response[Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]]:
    r""" Get organization credits

     Get credits for an organization

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]]
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

) -> Optional[Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]]:
    r""" Get organization credits

     Get credits for an organization

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]
     """


    return sync_detailed(
        client=client,
api_key=api_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: str,

) -> Response[Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]]:
    r""" Get organization credits

     Get credits for an organization

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]]
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

) -> Optional[Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]]:
    r""" Get organization credits

     Get credits for an organization

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOrgCreditsResponse200, GetOrgCreditsResponse400, GetOrgCreditsResponse401, GetOrgCreditsResponse402, GetOrgCreditsResponse403, GetOrgCreditsResponse404, GetOrgCreditsResponse429, GetOrgCreditsResponse500]
     """


    return (await asyncio_detailed(
        client=client,
api_key=api_key,

    )).parsed
