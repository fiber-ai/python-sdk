from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.sync_combined_search_body import SyncCombinedSearchBody
from ...models.sync_combined_search_response_200 import SyncCombinedSearchResponse200
from ...models.sync_combined_search_response_400 import SyncCombinedSearchResponse400
from ...models.sync_combined_search_response_401 import SyncCombinedSearchResponse401
from ...models.sync_combined_search_response_402 import SyncCombinedSearchResponse402
from ...models.sync_combined_search_response_403 import SyncCombinedSearchResponse403
from ...models.sync_combined_search_response_404 import SyncCombinedSearchResponse404
from ...models.sync_combined_search_response_429 import SyncCombinedSearchResponse429
from ...models.sync_combined_search_response_500 import SyncCombinedSearchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: SyncCombinedSearchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/combined-search/sync",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]]:
    if response.status_code == 200:
        response_200 = SyncCombinedSearchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = SyncCombinedSearchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = SyncCombinedSearchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = SyncCombinedSearchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = SyncCombinedSearchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SyncCombinedSearchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = SyncCombinedSearchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = SyncCombinedSearchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SyncCombinedSearchBody,

) -> Response[Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]]:
    r""" Sync combined search

     A synchronous endpoint that lets you search for companies and then prospects in these companies.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the search completes based on results: 1
    credits per company found and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary. Your total charge will vary based on the number of
    companies and profiles returned in your results.\">ⓘ</span></span>

    Args:
        body (SyncCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]]
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
    body: SyncCombinedSearchBody,

) -> Optional[Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]]:
    r""" Sync combined search

     A synchronous endpoint that lets you search for companies and then prospects in these companies.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the search completes based on results: 1
    credits per company found and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary. Your total charge will vary based on the number of
    companies and profiles returned in your results.\">ⓘ</span></span>

    Args:
        body (SyncCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SyncCombinedSearchBody,

) -> Response[Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]]:
    r""" Sync combined search

     A synchronous endpoint that lets you search for companies and then prospects in these companies.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the search completes based on results: 1
    credits per company found and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary. Your total charge will vary based on the number of
    companies and profiles returned in your results.\">ⓘ</span></span>

    Args:
        body (SyncCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]]
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
    body: SyncCombinedSearchBody,

) -> Optional[Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]]:
    r""" Sync combined search

     A synchronous endpoint that lets you search for companies and then prospects in these companies.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the search completes based on results: 1
    credits per company found and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary. Your total charge will vary based on the number of
    companies and profiles returned in your results.\">ⓘ</span></span>

    Args:
        body (SyncCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SyncCombinedSearchResponse200, SyncCombinedSearchResponse400, SyncCombinedSearchResponse401, SyncCombinedSearchResponse402, SyncCombinedSearchResponse403, SyncCombinedSearchResponse404, SyncCombinedSearchResponse429, SyncCombinedSearchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
