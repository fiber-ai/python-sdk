from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.domain_lookup_polling_body import DomainLookupPollingBody
from ...models.domain_lookup_polling_response_200 import DomainLookupPollingResponse200
from ...models.domain_lookup_polling_response_400 import DomainLookupPollingResponse400
from ...models.domain_lookup_polling_response_401 import DomainLookupPollingResponse401
from ...models.domain_lookup_polling_response_402 import DomainLookupPollingResponse402
from ...models.domain_lookup_polling_response_403 import DomainLookupPollingResponse403
from ...models.domain_lookup_polling_response_404 import DomainLookupPollingResponse404
from ...models.domain_lookup_polling_response_429 import DomainLookupPollingResponse429
from ...models.domain_lookup_polling_response_500 import DomainLookupPollingResponse500
from typing import cast



def _get_kwargs(
    *,
    body: DomainLookupPollingBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/domain-lookup/polling",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]]:
    if response.status_code == 200:
        response_200 = DomainLookupPollingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DomainLookupPollingResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DomainLookupPollingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = DomainLookupPollingResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = DomainLookupPollingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DomainLookupPollingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = DomainLookupPollingResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = DomainLookupPollingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DomainLookupPollingBody,

) -> Response[Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]]:
    """ Poll Domain lookup

     Poll for the results of a domain lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (DomainLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]]
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
    body: DomainLookupPollingBody,

) -> Optional[Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]]:
    """ Poll Domain lookup

     Poll for the results of a domain lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (DomainLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DomainLookupPollingBody,

) -> Response[Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]]:
    """ Poll Domain lookup

     Poll for the results of a domain lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (DomainLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]]
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
    body: DomainLookupPollingBody,

) -> Optional[Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]]:
    """ Poll Domain lookup

     Poll for the results of a domain lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (DomainLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DomainLookupPollingResponse200, DomainLookupPollingResponse400, DomainLookupPollingResponse401, DomainLookupPollingResponse402, DomainLookupPollingResponse403, DomainLookupPollingResponse404, DomainLookupPollingResponse429, DomainLookupPollingResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
