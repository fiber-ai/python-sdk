from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_prospect_exclusion_list_from_audience_body import CreateProspectExclusionListFromAudienceBody
from ...models.create_prospect_exclusion_list_from_audience_response_200 import CreateProspectExclusionListFromAudienceResponse200
from ...models.create_prospect_exclusion_list_from_audience_response_400 import CreateProspectExclusionListFromAudienceResponse400
from ...models.create_prospect_exclusion_list_from_audience_response_401 import CreateProspectExclusionListFromAudienceResponse401
from ...models.create_prospect_exclusion_list_from_audience_response_402 import CreateProspectExclusionListFromAudienceResponse402
from ...models.create_prospect_exclusion_list_from_audience_response_403 import CreateProspectExclusionListFromAudienceResponse403
from ...models.create_prospect_exclusion_list_from_audience_response_404 import CreateProspectExclusionListFromAudienceResponse404
from ...models.create_prospect_exclusion_list_from_audience_response_429 import CreateProspectExclusionListFromAudienceResponse429
from ...models.create_prospect_exclusion_list_from_audience_response_500 import CreateProspectExclusionListFromAudienceResponse500
from typing import cast



def _get_kwargs(
    *,
    body: CreateProspectExclusionListFromAudienceBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exclusions/prospects/audience/create-list",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]]:
    if response.status_code == 200:
        response_200 = CreateProspectExclusionListFromAudienceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = CreateProspectExclusionListFromAudienceResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateProspectExclusionListFromAudienceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = CreateProspectExclusionListFromAudienceResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = CreateProspectExclusionListFromAudienceResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CreateProspectExclusionListFromAudienceResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = CreateProspectExclusionListFromAudienceResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = CreateProspectExclusionListFromAudienceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateProspectExclusionListFromAudienceBody,

) -> Response[Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]]:
    r""" Create prospect exclusion list from audience

     Create a prospect exclusion list from an audience's prospects

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateProspectExclusionListFromAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]]
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
    body: CreateProspectExclusionListFromAudienceBody,

) -> Optional[Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]]:
    r""" Create prospect exclusion list from audience

     Create a prospect exclusion list from an audience's prospects

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateProspectExclusionListFromAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateProspectExclusionListFromAudienceBody,

) -> Response[Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]]:
    r""" Create prospect exclusion list from audience

     Create a prospect exclusion list from an audience's prospects

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateProspectExclusionListFromAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]]
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
    body: CreateProspectExclusionListFromAudienceBody,

) -> Optional[Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]]:
    r""" Create prospect exclusion list from audience

     Create a prospect exclusion list from an audience's prospects

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateProspectExclusionListFromAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProspectExclusionListFromAudienceResponse200, CreateProspectExclusionListFromAudienceResponse400, CreateProspectExclusionListFromAudienceResponse401, CreateProspectExclusionListFromAudienceResponse402, CreateProspectExclusionListFromAudienceResponse403, CreateProspectExclusionListFromAudienceResponse404, CreateProspectExclusionListFromAudienceResponse429, CreateProspectExclusionListFromAudienceResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
