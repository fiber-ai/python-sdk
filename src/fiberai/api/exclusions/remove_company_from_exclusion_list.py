from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.remove_company_from_exclusion_list_body import RemoveCompanyFromExclusionListBody
from ...models.remove_company_from_exclusion_list_response_200 import RemoveCompanyFromExclusionListResponse200
from ...models.remove_company_from_exclusion_list_response_400 import RemoveCompanyFromExclusionListResponse400
from ...models.remove_company_from_exclusion_list_response_401 import RemoveCompanyFromExclusionListResponse401
from ...models.remove_company_from_exclusion_list_response_402 import RemoveCompanyFromExclusionListResponse402
from ...models.remove_company_from_exclusion_list_response_403 import RemoveCompanyFromExclusionListResponse403
from ...models.remove_company_from_exclusion_list_response_404 import RemoveCompanyFromExclusionListResponse404
from ...models.remove_company_from_exclusion_list_response_429 import RemoveCompanyFromExclusionListResponse429
from ...models.remove_company_from_exclusion_list_response_500 import RemoveCompanyFromExclusionListResponse500
from typing import cast



def _get_kwargs(
    *,
    body: RemoveCompanyFromExclusionListBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exclusions/companies/remove-from-list",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]]:
    if response.status_code == 200:
        response_200 = RemoveCompanyFromExclusionListResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = RemoveCompanyFromExclusionListResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = RemoveCompanyFromExclusionListResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = RemoveCompanyFromExclusionListResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = RemoveCompanyFromExclusionListResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = RemoveCompanyFromExclusionListResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = RemoveCompanyFromExclusionListResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = RemoveCompanyFromExclusionListResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RemoveCompanyFromExclusionListBody,

) -> Response[Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]]:
    r""" Remove company from company exclusion list

     Remove a company from a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RemoveCompanyFromExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]]
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
    body: RemoveCompanyFromExclusionListBody,

) -> Optional[Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]]:
    r""" Remove company from company exclusion list

     Remove a company from a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RemoveCompanyFromExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RemoveCompanyFromExclusionListBody,

) -> Response[Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]]:
    r""" Remove company from company exclusion list

     Remove a company from a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RemoveCompanyFromExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]]
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
    body: RemoveCompanyFromExclusionListBody,

) -> Optional[Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]]:
    r""" Remove company from company exclusion list

     Remove a company from a company exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RemoveCompanyFromExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RemoveCompanyFromExclusionListResponse200, RemoveCompanyFromExclusionListResponse400, RemoveCompanyFromExclusionListResponse401, RemoveCompanyFromExclusionListResponse402, RemoveCompanyFromExclusionListResponse403, RemoveCompanyFromExclusionListResponse404, RemoveCompanyFromExclusionListResponse429, RemoveCompanyFromExclusionListResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
