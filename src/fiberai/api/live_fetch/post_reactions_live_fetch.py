from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_reactions_live_fetch_body import PostReactionsLiveFetchBody
from ...models.post_reactions_live_fetch_response_200 import PostReactionsLiveFetchResponse200
from ...models.post_reactions_live_fetch_response_400 import PostReactionsLiveFetchResponse400
from ...models.post_reactions_live_fetch_response_401 import PostReactionsLiveFetchResponse401
from ...models.post_reactions_live_fetch_response_402 import PostReactionsLiveFetchResponse402
from ...models.post_reactions_live_fetch_response_403 import PostReactionsLiveFetchResponse403
from ...models.post_reactions_live_fetch_response_404 import PostReactionsLiveFetchResponse404
from ...models.post_reactions_live_fetch_response_429 import PostReactionsLiveFetchResponse429
from ...models.post_reactions_live_fetch_response_500 import PostReactionsLiveFetchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: PostReactionsLiveFetchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/post-reactions",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]]:
    if response.status_code == 200:
        response_200 = PostReactionsLiveFetchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostReactionsLiveFetchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostReactionsLiveFetchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = PostReactionsLiveFetchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = PostReactionsLiveFetchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostReactionsLiveFetchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = PostReactionsLiveFetchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = PostReactionsLiveFetchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostReactionsLiveFetchBody,

) -> Response[Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]]:
    r""" Fetch LinkedIn post reactions

     Fetches paginated reactions of a specific type for a LinkedIn post. Each page contains up to 10
    reactions.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PostReactionsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]]
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
    body: PostReactionsLiveFetchBody,

) -> Optional[Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]]:
    r""" Fetch LinkedIn post reactions

     Fetches paginated reactions of a specific type for a LinkedIn post. Each page contains up to 10
    reactions.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PostReactionsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostReactionsLiveFetchBody,

) -> Response[Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]]:
    r""" Fetch LinkedIn post reactions

     Fetches paginated reactions of a specific type for a LinkedIn post. Each page contains up to 10
    reactions.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PostReactionsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]]
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
    body: PostReactionsLiveFetchBody,

) -> Optional[Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]]:
    r""" Fetch LinkedIn post reactions

     Fetches paginated reactions of a specific type for a LinkedIn post. Each page contains up to 10
    reactions.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PostReactionsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostReactionsLiveFetchResponse200, PostReactionsLiveFetchResponse400, PostReactionsLiveFetchResponse401, PostReactionsLiveFetchResponse402, PostReactionsLiveFetchResponse403, PostReactionsLiveFetchResponse404, PostReactionsLiveFetchResponse429, PostReactionsLiveFetchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
