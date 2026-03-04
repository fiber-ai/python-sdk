from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.kitchen_sink_bulk_company_body import KitchenSinkBulkCompanyBody
from ...models.kitchen_sink_bulk_company_response_200 import KitchenSinkBulkCompanyResponse200
from ...models.kitchen_sink_bulk_company_response_400 import KitchenSinkBulkCompanyResponse400
from ...models.kitchen_sink_bulk_company_response_401 import KitchenSinkBulkCompanyResponse401
from ...models.kitchen_sink_bulk_company_response_402 import KitchenSinkBulkCompanyResponse402
from ...models.kitchen_sink_bulk_company_response_403 import KitchenSinkBulkCompanyResponse403
from ...models.kitchen_sink_bulk_company_response_404 import KitchenSinkBulkCompanyResponse404
from ...models.kitchen_sink_bulk_company_response_429 import KitchenSinkBulkCompanyResponse429
from ...models.kitchen_sink_bulk_company_response_500 import KitchenSinkBulkCompanyResponse500
from typing import cast



def _get_kwargs(
    *,
    body: KitchenSinkBulkCompanyBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/kitchen-sink/bulk/company",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]]:
    if response.status_code == 200:
        response_200 = KitchenSinkBulkCompanyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = KitchenSinkBulkCompanyResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = KitchenSinkBulkCompanyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = KitchenSinkBulkCompanyResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = KitchenSinkBulkCompanyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = KitchenSinkBulkCompanyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = KitchenSinkBulkCompanyResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = KitchenSinkBulkCompanyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: KitchenSinkBulkCompanyBody,

) -> Response[Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]]:
    r""" Kitchen sink bulk company lookup

     Search for many companies using a variety of parameters such as LinkedIn slug, LinkedIn URL, name,
    etc. Returns complete company data if found.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (KitchenSinkBulkCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]]
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
    body: KitchenSinkBulkCompanyBody,

) -> Optional[Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]]:
    r""" Kitchen sink bulk company lookup

     Search for many companies using a variety of parameters such as LinkedIn slug, LinkedIn URL, name,
    etc. Returns complete company data if found.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (KitchenSinkBulkCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: KitchenSinkBulkCompanyBody,

) -> Response[Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]]:
    r""" Kitchen sink bulk company lookup

     Search for many companies using a variety of parameters such as LinkedIn slug, LinkedIn URL, name,
    etc. Returns complete company data if found.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (KitchenSinkBulkCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]]
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
    body: KitchenSinkBulkCompanyBody,

) -> Optional[Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]]:
    r""" Kitchen sink bulk company lookup

     Search for many companies using a variety of parameters such as LinkedIn slug, LinkedIn URL, name,
    etc. Returns complete company data if found.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (KitchenSinkBulkCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[KitchenSinkBulkCompanyResponse200, KitchenSinkBulkCompanyResponse400, KitchenSinkBulkCompanyResponse401, KitchenSinkBulkCompanyResponse402, KitchenSinkBulkCompanyResponse403, KitchenSinkBulkCompanyResponse404, KitchenSinkBulkCompanyResponse429, KitchenSinkBulkCompanyResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
