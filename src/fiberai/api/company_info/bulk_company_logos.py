from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_company_logos_body import BulkCompanyLogosBody
from ...models.bulk_company_logos_response_200 import BulkCompanyLogosResponse200
from ...models.bulk_company_logos_response_400 import BulkCompanyLogosResponse400
from ...models.bulk_company_logos_response_401 import BulkCompanyLogosResponse401
from ...models.bulk_company_logos_response_402 import BulkCompanyLogosResponse402
from ...models.bulk_company_logos_response_403 import BulkCompanyLogosResponse403
from ...models.bulk_company_logos_response_404 import BulkCompanyLogosResponse404
from ...models.bulk_company_logos_response_429 import BulkCompanyLogosResponse429
from ...models.bulk_company_logos_response_500 import BulkCompanyLogosResponse500
from typing import cast



def _get_kwargs(
    *,
    body: BulkCompanyLogosBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/company-logos/bulk",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]]:
    if response.status_code == 200:
        response_200 = BulkCompanyLogosResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BulkCompanyLogosResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = BulkCompanyLogosResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = BulkCompanyLogosResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = BulkCompanyLogosResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = BulkCompanyLogosResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = BulkCompanyLogosResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = BulkCompanyLogosResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BulkCompanyLogosBody,

) -> Response[Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]]:
    r""" Bulk company logos

     Get logo URLs for a list of companies. Max 10,000 companies can be looked up at a time.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per company logo lookup&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (BulkCompanyLogosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]]
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
    body: BulkCompanyLogosBody,

) -> Optional[Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]]:
    r""" Bulk company logos

     Get logo URLs for a list of companies. Max 10,000 companies can be looked up at a time.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per company logo lookup&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (BulkCompanyLogosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BulkCompanyLogosBody,

) -> Response[Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]]:
    r""" Bulk company logos

     Get logo URLs for a list of companies. Max 10,000 companies can be looked up at a time.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per company logo lookup&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (BulkCompanyLogosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]]
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
    body: BulkCompanyLogosBody,

) -> Optional[Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]]:
    r""" Bulk company logos

     Get logo URLs for a list of companies. Max 10,000 companies can be looked up at a time.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per company logo lookup&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (BulkCompanyLogosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkCompanyLogosResponse200, BulkCompanyLogosResponse400, BulkCompanyLogosResponse401, BulkCompanyLogosResponse402, BulkCompanyLogosResponse403, BulkCompanyLogosResponse404, BulkCompanyLogosResponse429, BulkCompanyLogosResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
