from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.start_batch_contact_enrichment_body import StartBatchContactEnrichmentBody
from ...models.start_batch_contact_enrichment_response_200 import StartBatchContactEnrichmentResponse200
from ...models.start_batch_contact_enrichment_response_400 import StartBatchContactEnrichmentResponse400
from ...models.start_batch_contact_enrichment_response_401 import StartBatchContactEnrichmentResponse401
from ...models.start_batch_contact_enrichment_response_402 import StartBatchContactEnrichmentResponse402
from ...models.start_batch_contact_enrichment_response_403 import StartBatchContactEnrichmentResponse403
from ...models.start_batch_contact_enrichment_response_404 import StartBatchContactEnrichmentResponse404
from ...models.start_batch_contact_enrichment_response_429 import StartBatchContactEnrichmentResponse429
from ...models.start_batch_contact_enrichment_response_500 import StartBatchContactEnrichmentResponse500
from typing import cast



def _get_kwargs(
    *,
    body: StartBatchContactEnrichmentBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-enrich/batch/start",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]]:
    if response.status_code == 200:
        response_200 = StartBatchContactEnrichmentResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = StartBatchContactEnrichmentResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = StartBatchContactEnrichmentResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = StartBatchContactEnrichmentResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = StartBatchContactEnrichmentResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = StartBatchContactEnrichmentResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = StartBatchContactEnrichmentResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = StartBatchContactEnrichmentResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StartBatchContactEnrichmentBody,

) -> Response[Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]]:
    r""" Start batch contact enrichment

     Starts fetching contact details for multiple people (up to 10000) in batch. This is an asynchronous
    task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Credits are charged upfront for all unique people queued (after deduping).
    Undelivered data is refunded per operation.\">ⓘ</span></span>

    Args:
        body (StartBatchContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]]
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
    body: StartBatchContactEnrichmentBody,

) -> Optional[Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]]:
    r""" Start batch contact enrichment

     Starts fetching contact details for multiple people (up to 10000) in batch. This is an asynchronous
    task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Credits are charged upfront for all unique people queued (after deduping).
    Undelivered data is refunded per operation.\">ⓘ</span></span>

    Args:
        body (StartBatchContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StartBatchContactEnrichmentBody,

) -> Response[Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]]:
    r""" Start batch contact enrichment

     Starts fetching contact details for multiple people (up to 10000) in batch. This is an asynchronous
    task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Credits are charged upfront for all unique people queued (after deduping).
    Undelivered data is refunded per operation.\">ⓘ</span></span>

    Args:
        body (StartBatchContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]]
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
    body: StartBatchContactEnrichmentBody,

) -> Optional[Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]]:
    r""" Start batch contact enrichment

     Starts fetching contact details for multiple people (up to 10000) in batch. This is an asynchronous
    task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Credits are charged upfront for all unique people queued (after deduping).
    Undelivered data is refunded per operation.\">ⓘ</span></span>

    Args:
        body (StartBatchContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StartBatchContactEnrichmentResponse200, StartBatchContactEnrichmentResponse400, StartBatchContactEnrichmentResponse401, StartBatchContactEnrichmentResponse402, StartBatchContactEnrichmentResponse403, StartBatchContactEnrichmentResponse404, StartBatchContactEnrichmentResponse429, StartBatchContactEnrichmentResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
