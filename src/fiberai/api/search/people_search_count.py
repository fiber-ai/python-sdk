from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.people_search_count_body import PeopleSearchCountBody
from ...models.people_search_count_response_200 import PeopleSearchCountResponse200
from ...models.people_search_count_response_400 import PeopleSearchCountResponse400
from ...models.people_search_count_response_401 import PeopleSearchCountResponse401
from ...models.people_search_count_response_402 import PeopleSearchCountResponse402
from ...models.people_search_count_response_403 import PeopleSearchCountResponse403
from ...models.people_search_count_response_404 import PeopleSearchCountResponse404
from ...models.people_search_count_response_429 import PeopleSearchCountResponse429
from ...models.people_search_count_response_500 import PeopleSearchCountResponse500
from typing import cast



def _get_kwargs(
    *,
    body: PeopleSearchCountBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/people-search/count",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]]:
    if response.status_code == 200:
        response_200 = PeopleSearchCountResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PeopleSearchCountResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PeopleSearchCountResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = PeopleSearchCountResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = PeopleSearchCountResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PeopleSearchCountResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = PeopleSearchCountResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = PeopleSearchCountResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PeopleSearchCountBody,

) -> Response[Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]]:
    r""" People search count

     Get count of profiles matching search filters

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PeopleSearchCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]]
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
    body: PeopleSearchCountBody,

) -> Optional[Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]]:
    r""" People search count

     Get count of profiles matching search filters

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PeopleSearchCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PeopleSearchCountBody,

) -> Response[Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]]:
    r""" People search count

     Get count of profiles matching search filters

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PeopleSearchCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]]
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
    body: PeopleSearchCountBody,

) -> Optional[Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]]:
    r""" People search count

     Get count of profiles matching search filters

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PeopleSearchCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PeopleSearchCountResponse200, PeopleSearchCountResponse400, PeopleSearchCountResponse401, PeopleSearchCountResponse402, PeopleSearchCountResponse403, PeopleSearchCountResponse404, PeopleSearchCountResponse429, PeopleSearchCountResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
