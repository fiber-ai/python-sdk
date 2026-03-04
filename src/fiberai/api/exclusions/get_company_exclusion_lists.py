from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_company_exclusion_lists_body import GetCompanyExclusionListsBody
from ...models.get_company_exclusion_lists_response_200 import GetCompanyExclusionListsResponse200
from ...models.get_company_exclusion_lists_response_400 import GetCompanyExclusionListsResponse400
from ...models.get_company_exclusion_lists_response_401 import GetCompanyExclusionListsResponse401
from ...models.get_company_exclusion_lists_response_402 import GetCompanyExclusionListsResponse402
from ...models.get_company_exclusion_lists_response_403 import GetCompanyExclusionListsResponse403
from ...models.get_company_exclusion_lists_response_404 import GetCompanyExclusionListsResponse404
from ...models.get_company_exclusion_lists_response_429 import GetCompanyExclusionListsResponse429
from ...models.get_company_exclusion_lists_response_500 import GetCompanyExclusionListsResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GetCompanyExclusionListsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exclusions/companies/get-lists",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]]:
    if response.status_code == 200:
        response_200 = GetCompanyExclusionListsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetCompanyExclusionListsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetCompanyExclusionListsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = GetCompanyExclusionListsResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = GetCompanyExclusionListsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetCompanyExclusionListsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = GetCompanyExclusionListsResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = GetCompanyExclusionListsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetCompanyExclusionListsBody,

) -> Response[Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]]:
    r""" Get company exclusion list

     Get company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCompanyExclusionListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]]
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
    body: GetCompanyExclusionListsBody,

) -> Optional[Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]]:
    r""" Get company exclusion list

     Get company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCompanyExclusionListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetCompanyExclusionListsBody,

) -> Response[Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]]:
    r""" Get company exclusion list

     Get company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCompanyExclusionListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]]
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
    body: GetCompanyExclusionListsBody,

) -> Optional[Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]]:
    r""" Get company exclusion list

     Get company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCompanyExclusionListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCompanyExclusionListsResponse200, GetCompanyExclusionListsResponse400, GetCompanyExclusionListsResponse401, GetCompanyExclusionListsResponse402, GetCompanyExclusionListsResponse403, GetCompanyExclusionListsResponse404, GetCompanyExclusionListsResponse429, GetCompanyExclusionListsResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
