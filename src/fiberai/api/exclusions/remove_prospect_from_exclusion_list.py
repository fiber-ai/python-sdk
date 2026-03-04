from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.remove_prospect_from_exclusion_list_body import RemoveProspectFromExclusionListBody
from ...models.remove_prospect_from_exclusion_list_response_200 import RemoveProspectFromExclusionListResponse200
from ...models.remove_prospect_from_exclusion_list_response_400 import RemoveProspectFromExclusionListResponse400
from ...models.remove_prospect_from_exclusion_list_response_401 import RemoveProspectFromExclusionListResponse401
from ...models.remove_prospect_from_exclusion_list_response_402 import RemoveProspectFromExclusionListResponse402
from ...models.remove_prospect_from_exclusion_list_response_403 import RemoveProspectFromExclusionListResponse403
from ...models.remove_prospect_from_exclusion_list_response_404 import RemoveProspectFromExclusionListResponse404
from ...models.remove_prospect_from_exclusion_list_response_429 import RemoveProspectFromExclusionListResponse429
from ...models.remove_prospect_from_exclusion_list_response_500 import RemoveProspectFromExclusionListResponse500
from typing import cast



def _get_kwargs(
    *,
    body: RemoveProspectFromExclusionListBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exclusions/prospects/remove-from-list",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]]:
    if response.status_code == 200:
        response_200 = RemoveProspectFromExclusionListResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = RemoveProspectFromExclusionListResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = RemoveProspectFromExclusionListResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = RemoveProspectFromExclusionListResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = RemoveProspectFromExclusionListResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = RemoveProspectFromExclusionListResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = RemoveProspectFromExclusionListResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = RemoveProspectFromExclusionListResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RemoveProspectFromExclusionListBody,

) -> Response[Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]]:
    r""" Remove prospect from prospect exclusion list

     Remove a prospect from a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RemoveProspectFromExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]]
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
    body: RemoveProspectFromExclusionListBody,

) -> Optional[Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]]:
    r""" Remove prospect from prospect exclusion list

     Remove a prospect from a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RemoveProspectFromExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RemoveProspectFromExclusionListBody,

) -> Response[Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]]:
    r""" Remove prospect from prospect exclusion list

     Remove a prospect from a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RemoveProspectFromExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]]
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
    body: RemoveProspectFromExclusionListBody,

) -> Optional[Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]]:
    r""" Remove prospect from prospect exclusion list

     Remove a prospect from a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (RemoveProspectFromExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RemoveProspectFromExclusionListResponse200, RemoveProspectFromExclusionListResponse400, RemoveProspectFromExclusionListResponse401, RemoveProspectFromExclusionListResponse402, RemoveProspectFromExclusionListResponse403, RemoveProspectFromExclusionListResponse404, RemoveProspectFromExclusionListResponse429, RemoveProspectFromExclusionListResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
