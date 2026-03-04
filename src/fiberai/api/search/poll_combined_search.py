from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.poll_combined_search_body import PollCombinedSearchBody
from ...models.poll_combined_search_response_200 import PollCombinedSearchResponse200
from ...models.poll_combined_search_response_400 import PollCombinedSearchResponse400
from ...models.poll_combined_search_response_401 import PollCombinedSearchResponse401
from ...models.poll_combined_search_response_402 import PollCombinedSearchResponse402
from ...models.poll_combined_search_response_403 import PollCombinedSearchResponse403
from ...models.poll_combined_search_response_404 import PollCombinedSearchResponse404
from ...models.poll_combined_search_response_429 import PollCombinedSearchResponse429
from ...models.poll_combined_search_response_500 import PollCombinedSearchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: PollCombinedSearchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/combined-search/poll",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]]:
    if response.status_code == 200:
        response_200 = PollCombinedSearchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PollCombinedSearchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PollCombinedSearchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = PollCombinedSearchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = PollCombinedSearchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PollCombinedSearchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = PollCombinedSearchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = PollCombinedSearchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PollCombinedSearchBody,

) -> Response[Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]]:
    """ Poll combined search

     Poll for the companies and profiles from the combined search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (PollCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]]
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
    body: PollCombinedSearchBody,

) -> Optional[Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]]:
    """ Poll combined search

     Poll for the companies and profiles from the combined search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (PollCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PollCombinedSearchBody,

) -> Response[Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]]:
    """ Poll combined search

     Poll for the companies and profiles from the combined search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (PollCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]]
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
    body: PollCombinedSearchBody,

) -> Optional[Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]]:
    """ Poll combined search

     Poll for the companies and profiles from the combined search

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (PollCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PollCombinedSearchResponse200, PollCombinedSearchResponse400, PollCombinedSearchResponse401, PollCombinedSearchResponse402, PollCombinedSearchResponse403, PollCombinedSearchResponse404, PollCombinedSearchResponse429, PollCombinedSearchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
