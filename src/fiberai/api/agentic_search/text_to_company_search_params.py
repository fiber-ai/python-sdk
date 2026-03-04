from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.text_to_company_search_params_body import TextToCompanySearchParamsBody
from ...models.text_to_company_search_params_response_200 import TextToCompanySearchParamsResponse200
from ...models.text_to_company_search_params_response_400 import TextToCompanySearchParamsResponse400
from ...models.text_to_company_search_params_response_401 import TextToCompanySearchParamsResponse401
from ...models.text_to_company_search_params_response_402 import TextToCompanySearchParamsResponse402
from ...models.text_to_company_search_params_response_403 import TextToCompanySearchParamsResponse403
from ...models.text_to_company_search_params_response_404 import TextToCompanySearchParamsResponse404
from ...models.text_to_company_search_params_response_429 import TextToCompanySearchParamsResponse429
from ...models.text_to_company_search_params_response_500 import TextToCompanySearchParamsResponse500
from typing import cast



def _get_kwargs(
    *,
    body: TextToCompanySearchParamsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/text-to-search-params/companies",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]]:
    if response.status_code == 200:
        response_200 = TextToCompanySearchParamsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = TextToCompanySearchParamsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = TextToCompanySearchParamsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = TextToCompanySearchParamsResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = TextToCompanySearchParamsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = TextToCompanySearchParamsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = TextToCompanySearchParamsResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = TextToCompanySearchParamsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TextToCompanySearchParamsBody,

) -> Response[Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]]:
    r""" Convert text into company search filters

     Takes free-form text (e.g., 'Series A startups in USA with 50–200 employees') and converts it into a
    structured set of filters for company search.         This endpoint helps transform natural language
    queries into standardized search parameters such as industries, funding stages, headcount ranges,
    locations, and more.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCompanySearchParamsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]]
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
    body: TextToCompanySearchParamsBody,

) -> Optional[Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]]:
    r""" Convert text into company search filters

     Takes free-form text (e.g., 'Series A startups in USA with 50–200 employees') and converts it into a
    structured set of filters for company search.         This endpoint helps transform natural language
    queries into standardized search parameters such as industries, funding stages, headcount ranges,
    locations, and more.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCompanySearchParamsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TextToCompanySearchParamsBody,

) -> Response[Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]]:
    r""" Convert text into company search filters

     Takes free-form text (e.g., 'Series A startups in USA with 50–200 employees') and converts it into a
    structured set of filters for company search.         This endpoint helps transform natural language
    queries into standardized search parameters such as industries, funding stages, headcount ranges,
    locations, and more.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCompanySearchParamsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]]
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
    body: TextToCompanySearchParamsBody,

) -> Optional[Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]]:
    r""" Convert text into company search filters

     Takes free-form text (e.g., 'Series A startups in USA with 50–200 employees') and converts it into a
    structured set of filters for company search.         This endpoint helps transform natural language
    queries into standardized search parameters such as industries, funding stages, headcount ranges,
    locations, and more.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCompanySearchParamsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TextToCompanySearchParamsResponse200, TextToCompanySearchParamsResponse400, TextToCompanySearchParamsResponse401, TextToCompanySearchParamsResponse402, TextToCompanySearchParamsResponse403, TextToCompanySearchParamsResponse404, TextToCompanySearchParamsResponse429, TextToCompanySearchParamsResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
