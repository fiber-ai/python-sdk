from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.poll_local_business_search_body import PollLocalBusinessSearchBody
from ...models.poll_local_business_search_response_200 import PollLocalBusinessSearchResponse200
from ...models.poll_local_business_search_response_400 import PollLocalBusinessSearchResponse400
from ...models.poll_local_business_search_response_401 import PollLocalBusinessSearchResponse401
from ...models.poll_local_business_search_response_402 import PollLocalBusinessSearchResponse402
from ...models.poll_local_business_search_response_403 import PollLocalBusinessSearchResponse403
from ...models.poll_local_business_search_response_404 import PollLocalBusinessSearchResponse404
from ...models.poll_local_business_search_response_429 import PollLocalBusinessSearchResponse429
from ...models.poll_local_business_search_response_500 import PollLocalBusinessSearchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: PollLocalBusinessSearchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/local-business-search/poll",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]]:
    if response.status_code == 200:
        response_200 = PollLocalBusinessSearchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PollLocalBusinessSearchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PollLocalBusinessSearchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = PollLocalBusinessSearchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = PollLocalBusinessSearchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PollLocalBusinessSearchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = PollLocalBusinessSearchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = PollLocalBusinessSearchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PollLocalBusinessSearchBody,

) -> Response[Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]]:
    """ Poll local business search

     Coming Soon! Poll a local business search task

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    Args:
        body (PollLocalBusinessSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]]
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
    body: PollLocalBusinessSearchBody,

) -> Optional[Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]]:
    """ Poll local business search

     Coming Soon! Poll a local business search task

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    Args:
        body (PollLocalBusinessSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PollLocalBusinessSearchBody,

) -> Response[Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]]:
    """ Poll local business search

     Coming Soon! Poll a local business search task

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    Args:
        body (PollLocalBusinessSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]]
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
    body: PollLocalBusinessSearchBody,

) -> Optional[Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]]:
    """ Poll local business search

     Coming Soon! Poll a local business search task

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    Args:
        body (PollLocalBusinessSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PollLocalBusinessSearchResponse200, PollLocalBusinessSearchResponse400, PollLocalBusinessSearchResponse401, PollLocalBusinessSearchResponse402, PollLocalBusinessSearchResponse403, PollLocalBusinessSearchResponse404, PollLocalBusinessSearchResponse429, PollLocalBusinessSearchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
