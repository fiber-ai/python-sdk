from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.domain_lookup_trigger_body import DomainLookupTriggerBody
from ...models.domain_lookup_trigger_response_200 import DomainLookupTriggerResponse200
from ...models.domain_lookup_trigger_response_400 import DomainLookupTriggerResponse400
from ...models.domain_lookup_trigger_response_401 import DomainLookupTriggerResponse401
from ...models.domain_lookup_trigger_response_402 import DomainLookupTriggerResponse402
from ...models.domain_lookup_trigger_response_403 import DomainLookupTriggerResponse403
from ...models.domain_lookup_trigger_response_404 import DomainLookupTriggerResponse404
from ...models.domain_lookup_trigger_response_429 import DomainLookupTriggerResponse429
from ...models.domain_lookup_trigger_response_500 import DomainLookupTriggerResponse500
from typing import cast



def _get_kwargs(
    *,
    body: DomainLookupTriggerBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/domain-lookup/trigger",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]]:
    if response.status_code == 200:
        response_200 = DomainLookupTriggerResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DomainLookupTriggerResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DomainLookupTriggerResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = DomainLookupTriggerResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = DomainLookupTriggerResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DomainLookupTriggerResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = DomainLookupTriggerResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = DomainLookupTriggerResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DomainLookupTriggerBody,

) -> Response[Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]]:
    r""" Start Domain lookup

     Use our AI agent to find a company's domain and email domains using a variety of parameters such as
    company name, country, state, city, address, other context, and description. NOTE: Maximum 2000
    companies can be provided at a time. Estimated time to complete 600 companies is an hour.

    <span>⚡ <strong>Rate limit:</strong> 5 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DomainLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]]
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
    body: DomainLookupTriggerBody,

) -> Optional[Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]]:
    r""" Start Domain lookup

     Use our AI agent to find a company's domain and email domains using a variety of parameters such as
    company name, country, state, city, address, other context, and description. NOTE: Maximum 2000
    companies can be provided at a time. Estimated time to complete 600 companies is an hour.

    <span>⚡ <strong>Rate limit:</strong> 5 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DomainLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DomainLookupTriggerBody,

) -> Response[Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]]:
    r""" Start Domain lookup

     Use our AI agent to find a company's domain and email domains using a variety of parameters such as
    company name, country, state, city, address, other context, and description. NOTE: Maximum 2000
    companies can be provided at a time. Estimated time to complete 600 companies is an hour.

    <span>⚡ <strong>Rate limit:</strong> 5 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DomainLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]]
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
    body: DomainLookupTriggerBody,

) -> Optional[Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]]:
    r""" Start Domain lookup

     Use our AI agent to find a company's domain and email domains using a variety of parameters such as
    company name, country, state, city, address, other context, and description. NOTE: Maximum 2000
    companies can be provided at a time. Estimated time to complete 600 companies is an hour.

    <span>⚡ <strong>Rate limit:</strong> 5 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DomainLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DomainLookupTriggerResponse200, DomainLookupTriggerResponse400, DomainLookupTriggerResponse401, DomainLookupTriggerResponse402, DomainLookupTriggerResponse403, DomainLookupTriggerResponse404, DomainLookupTriggerResponse429, DomainLookupTriggerResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
