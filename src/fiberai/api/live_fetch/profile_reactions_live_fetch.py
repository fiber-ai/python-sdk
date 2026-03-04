from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.profile_reactions_live_fetch_body import ProfileReactionsLiveFetchBody
from ...models.profile_reactions_live_fetch_response_200 import ProfileReactionsLiveFetchResponse200
from ...models.profile_reactions_live_fetch_response_400 import ProfileReactionsLiveFetchResponse400
from ...models.profile_reactions_live_fetch_response_401 import ProfileReactionsLiveFetchResponse401
from ...models.profile_reactions_live_fetch_response_402 import ProfileReactionsLiveFetchResponse402
from ...models.profile_reactions_live_fetch_response_403 import ProfileReactionsLiveFetchResponse403
from ...models.profile_reactions_live_fetch_response_404 import ProfileReactionsLiveFetchResponse404
from ...models.profile_reactions_live_fetch_response_429 import ProfileReactionsLiveFetchResponse429
from ...models.profile_reactions_live_fetch_response_500 import ProfileReactionsLiveFetchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: ProfileReactionsLiveFetchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/profile-reactions",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]]:
    if response.status_code == 200:
        response_200 = ProfileReactionsLiveFetchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ProfileReactionsLiveFetchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ProfileReactionsLiveFetchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = ProfileReactionsLiveFetchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = ProfileReactionsLiveFetchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ProfileReactionsLiveFetchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = ProfileReactionsLiveFetchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ProfileReactionsLiveFetchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ProfileReactionsLiveFetchBody,

) -> Response[Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]]:
    r""" Fetch LinkedIn profile reactions

     Fetches reactions made by a LinkedIn profile. Returns a paginated feed of reactions with optional
    cursor for pagination. Each page returns up to 10 reactions.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileReactionsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]]
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
    body: ProfileReactionsLiveFetchBody,

) -> Optional[Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]]:
    r""" Fetch LinkedIn profile reactions

     Fetches reactions made by a LinkedIn profile. Returns a paginated feed of reactions with optional
    cursor for pagination. Each page returns up to 10 reactions.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileReactionsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ProfileReactionsLiveFetchBody,

) -> Response[Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]]:
    r""" Fetch LinkedIn profile reactions

     Fetches reactions made by a LinkedIn profile. Returns a paginated feed of reactions with optional
    cursor for pagination. Each page returns up to 10 reactions.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileReactionsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]]
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
    body: ProfileReactionsLiveFetchBody,

) -> Optional[Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]]:
    r""" Fetch LinkedIn profile reactions

     Fetches reactions made by a LinkedIn profile. Returns a paginated feed of reactions with optional
    cursor for pagination. Each page returns up to 10 reactions.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileReactionsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProfileReactionsLiveFetchResponse200, ProfileReactionsLiveFetchResponse400, ProfileReactionsLiveFetchResponse401, ProfileReactionsLiveFetchResponse402, ProfileReactionsLiveFetchResponse403, ProfileReactionsLiveFetchResponse404, ProfileReactionsLiveFetchResponse429, ProfileReactionsLiveFetchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
