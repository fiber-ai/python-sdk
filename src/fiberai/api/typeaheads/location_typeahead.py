from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.location_typeahead_body import LocationTypeaheadBody
from ...models.location_typeahead_response_200 import LocationTypeaheadResponse200
from ...models.location_typeahead_response_400 import LocationTypeaheadResponse400
from ...models.location_typeahead_response_401 import LocationTypeaheadResponse401
from ...models.location_typeahead_response_402 import LocationTypeaheadResponse402
from ...models.location_typeahead_response_403 import LocationTypeaheadResponse403
from ...models.location_typeahead_response_404 import LocationTypeaheadResponse404
from ...models.location_typeahead_response_429 import LocationTypeaheadResponse429
from ...models.location_typeahead_response_500 import LocationTypeaheadResponse500
from typing import cast



def _get_kwargs(
    *,
    body: LocationTypeaheadBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/typeahead/location",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]]:
    if response.status_code == 200:
        response_200 = LocationTypeaheadResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = LocationTypeaheadResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = LocationTypeaheadResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = LocationTypeaheadResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = LocationTypeaheadResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = LocationTypeaheadResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = LocationTypeaheadResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = LocationTypeaheadResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LocationTypeaheadBody,

) -> Response[Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]]:
    r""" Location typeahead

     Get the latitude/longitude of a given city, including prefixes (e.g. 'san fr'). This makes it good
    for typeaheads in your UI.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (LocationTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]]
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
    body: LocationTypeaheadBody,

) -> Optional[Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]]:
    r""" Location typeahead

     Get the latitude/longitude of a given city, including prefixes (e.g. 'san fr'). This makes it good
    for typeaheads in your UI.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (LocationTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LocationTypeaheadBody,

) -> Response[Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]]:
    r""" Location typeahead

     Get the latitude/longitude of a given city, including prefixes (e.g. 'san fr'). This makes it good
    for typeaheads in your UI.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (LocationTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]]
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
    body: LocationTypeaheadBody,

) -> Optional[Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]]:
    r""" Location typeahead

     Get the latitude/longitude of a given city, including prefixes (e.g. 'san fr'). This makes it good
    for typeaheads in your UI.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (LocationTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[LocationTypeaheadResponse200, LocationTypeaheadResponse400, LocationTypeaheadResponse401, LocationTypeaheadResponse402, LocationTypeaheadResponse403, LocationTypeaheadResponse404, LocationTypeaheadResponse429, LocationTypeaheadResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
