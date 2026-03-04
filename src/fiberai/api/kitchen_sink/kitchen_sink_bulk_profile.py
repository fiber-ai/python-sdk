from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.kitchen_sink_bulk_profile_body import KitchenSinkBulkProfileBody
from ...models.kitchen_sink_bulk_profile_response_200 import KitchenSinkBulkProfileResponse200
from ...models.kitchen_sink_bulk_profile_response_400 import KitchenSinkBulkProfileResponse400
from ...models.kitchen_sink_bulk_profile_response_401 import KitchenSinkBulkProfileResponse401
from ...models.kitchen_sink_bulk_profile_response_402 import KitchenSinkBulkProfileResponse402
from ...models.kitchen_sink_bulk_profile_response_403 import KitchenSinkBulkProfileResponse403
from ...models.kitchen_sink_bulk_profile_response_404 import KitchenSinkBulkProfileResponse404
from ...models.kitchen_sink_bulk_profile_response_429 import KitchenSinkBulkProfileResponse429
from ...models.kitchen_sink_bulk_profile_response_500 import KitchenSinkBulkProfileResponse500
from typing import cast



def _get_kwargs(
    *,
    body: KitchenSinkBulkProfileBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/kitchen-sink/bulk/profile",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]]:
    if response.status_code == 200:
        response_200 = KitchenSinkBulkProfileResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = KitchenSinkBulkProfileResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = KitchenSinkBulkProfileResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = KitchenSinkBulkProfileResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = KitchenSinkBulkProfileResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = KitchenSinkBulkProfileResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = KitchenSinkBulkProfileResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = KitchenSinkBulkProfileResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: KitchenSinkBulkProfileBody,

) -> Response[Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]]:
    r""" Kitchen sink bulk profile lookup

     Search for many people using a variety of parameters such as LinkedIn slug, LinkedIn URL, or their
    current company information. Returns profile data for the person if found.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay per person: 2 credits per lookup, plus 2 additional credits when
    the liveFetch flag is set.&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary. LinkedIn live fetch credits only apply when the liveFetch flag is set.\">ⓘ</span></span>

    Args:
        body (KitchenSinkBulkProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]]
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
    body: KitchenSinkBulkProfileBody,

) -> Optional[Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]]:
    r""" Kitchen sink bulk profile lookup

     Search for many people using a variety of parameters such as LinkedIn slug, LinkedIn URL, or their
    current company information. Returns profile data for the person if found.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay per person: 2 credits per lookup, plus 2 additional credits when
    the liveFetch flag is set.&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary. LinkedIn live fetch credits only apply when the liveFetch flag is set.\">ⓘ</span></span>

    Args:
        body (KitchenSinkBulkProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: KitchenSinkBulkProfileBody,

) -> Response[Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]]:
    r""" Kitchen sink bulk profile lookup

     Search for many people using a variety of parameters such as LinkedIn slug, LinkedIn URL, or their
    current company information. Returns profile data for the person if found.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay per person: 2 credits per lookup, plus 2 additional credits when
    the liveFetch flag is set.&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary. LinkedIn live fetch credits only apply when the liveFetch flag is set.\">ⓘ</span></span>

    Args:
        body (KitchenSinkBulkProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]]
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
    body: KitchenSinkBulkProfileBody,

) -> Optional[Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]]:
    r""" Kitchen sink bulk profile lookup

     Search for many people using a variety of parameters such as LinkedIn slug, LinkedIn URL, or their
    current company information. Returns profile data for the person if found.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay per person: 2 credits per lookup, plus 2 additional credits when
    the liveFetch flag is set.&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary. LinkedIn live fetch credits only apply when the liveFetch flag is set.\">ⓘ</span></span>

    Args:
        body (KitchenSinkBulkProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[KitchenSinkBulkProfileResponse200, KitchenSinkBulkProfileResponse400, KitchenSinkBulkProfileResponse401, KitchenSinkBulkProfileResponse402, KitchenSinkBulkProfileResponse403, KitchenSinkBulkProfileResponse404, KitchenSinkBulkProfileResponse429, KitchenSinkBulkProfileResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
