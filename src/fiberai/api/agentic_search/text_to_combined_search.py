from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.text_to_combined_search_body import TextToCombinedSearchBody
from ...models.text_to_combined_search_response_200 import TextToCombinedSearchResponse200
from ...models.text_to_combined_search_response_400 import TextToCombinedSearchResponse400
from ...models.text_to_combined_search_response_401 import TextToCombinedSearchResponse401
from ...models.text_to_combined_search_response_402 import TextToCombinedSearchResponse402
from ...models.text_to_combined_search_response_403 import TextToCombinedSearchResponse403
from ...models.text_to_combined_search_response_404 import TextToCombinedSearchResponse404
from ...models.text_to_combined_search_response_429 import TextToCombinedSearchResponse429
from ...models.text_to_combined_search_response_500 import TextToCombinedSearchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: TextToCombinedSearchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/natural-language-search/combined/sync",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]]:
    if response.status_code == 200:
        response_200 = TextToCombinedSearchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = TextToCombinedSearchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = TextToCombinedSearchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = TextToCombinedSearchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = TextToCombinedSearchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = TextToCombinedSearchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = TextToCombinedSearchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = TextToCombinedSearchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TextToCombinedSearchBody,

) -> Response[Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]]:
    r""" Search companies and prospects from text

     Takes free-form text (e.g., 'Senior Product Managers from Series A to C FinTech startups in New
    York') and produces standardized filters (industries, funding stages, headcount ranges, locations,
    titles, seniorities, etc.). When limits are provided, executes the search and returns matching
    companies and people in a single synchronous call.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request:<br />• 2 credits for company search params
    generation based on prompt, if required<br />• 2 credits for profile search params generation based
    on prompt, if required<br /><br />Additional credits are charged for each company and profile
    returned, based on the search results.&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]]
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
    body: TextToCombinedSearchBody,

) -> Optional[Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]]:
    r""" Search companies and prospects from text

     Takes free-form text (e.g., 'Senior Product Managers from Series A to C FinTech startups in New
    York') and produces standardized filters (industries, funding stages, headcount ranges, locations,
    titles, seniorities, etc.). When limits are provided, executes the search and returns matching
    companies and people in a single synchronous call.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request:<br />• 2 credits for company search params
    generation based on prompt, if required<br />• 2 credits for profile search params generation based
    on prompt, if required<br /><br />Additional credits are charged for each company and profile
    returned, based on the search results.&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TextToCombinedSearchBody,

) -> Response[Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]]:
    r""" Search companies and prospects from text

     Takes free-form text (e.g., 'Senior Product Managers from Series A to C FinTech startups in New
    York') and produces standardized filters (industries, funding stages, headcount ranges, locations,
    titles, seniorities, etc.). When limits are provided, executes the search and returns matching
    companies and people in a single synchronous call.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request:<br />• 2 credits for company search params
    generation based on prompt, if required<br />• 2 credits for profile search params generation based
    on prompt, if required<br /><br />Additional credits are charged for each company and profile
    returned, based on the search results.&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]]
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
    body: TextToCombinedSearchBody,

) -> Optional[Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]]:
    r""" Search companies and prospects from text

     Takes free-form text (e.g., 'Senior Product Managers from Series A to C FinTech startups in New
    York') and produces standardized filters (industries, funding stages, headcount ranges, locations,
    titles, seniorities, etc.). When limits are provided, executes the search and returns matching
    companies and people in a single synchronous call.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request:<br />• 2 credits for company search params
    generation based on prompt, if required<br />• 2 credits for profile search params generation based
    on prompt, if required<br /><br />Additional credits are charged for each company and profile
    returned, based on the search results.&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCombinedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TextToCombinedSearchResponse200, TextToCombinedSearchResponse400, TextToCombinedSearchResponse401, TextToCombinedSearchResponse402, TextToCombinedSearchResponse403, TextToCombinedSearchResponse404, TextToCombinedSearchResponse429, TextToCombinedSearchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
