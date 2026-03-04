from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.sync_contact_enrichment_body import SyncContactEnrichmentBody
from ...models.sync_contact_enrichment_response_200 import SyncContactEnrichmentResponse200
from ...models.sync_contact_enrichment_response_400 import SyncContactEnrichmentResponse400
from ...models.sync_contact_enrichment_response_401 import SyncContactEnrichmentResponse401
from ...models.sync_contact_enrichment_response_402 import SyncContactEnrichmentResponse402
from ...models.sync_contact_enrichment_response_403 import SyncContactEnrichmentResponse403
from ...models.sync_contact_enrichment_response_404 import SyncContactEnrichmentResponse404
from ...models.sync_contact_enrichment_response_429 import SyncContactEnrichmentResponse429
from ...models.sync_contact_enrichment_response_500 import SyncContactEnrichmentResponse500
from typing import cast



def _get_kwargs(
    *,
    body: SyncContactEnrichmentBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/sync",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]]:
    if response.status_code == 200:
        response_200 = SyncContactEnrichmentResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = SyncContactEnrichmentResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = SyncContactEnrichmentResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = SyncContactEnrichmentResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = SyncContactEnrichmentResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SyncContactEnrichmentResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = SyncContactEnrichmentResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = SyncContactEnrichmentResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SyncContactEnrichmentBody,

) -> Response[Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]]:
    r""" Synchronously fetch contact details

     Fetches a single person's work email, personal email, and/or phone number synchronously, meaning
    that you don't need to poll separately. This endpoint is slow, though, since it waits for the task
    to finish before returning.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only<br />• Plus 1 credits when the liveFetch flag is set&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary. Partial reveals only bill for
    delivered data.\">ⓘ</span></span>

    Args:
        body (SyncContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]]
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
    body: SyncContactEnrichmentBody,

) -> Optional[Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]]:
    r""" Synchronously fetch contact details

     Fetches a single person's work email, personal email, and/or phone number synchronously, meaning
    that you don't need to poll separately. This endpoint is slow, though, since it waits for the task
    to finish before returning.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only<br />• Plus 1 credits when the liveFetch flag is set&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary. Partial reveals only bill for
    delivered data.\">ⓘ</span></span>

    Args:
        body (SyncContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SyncContactEnrichmentBody,

) -> Response[Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]]:
    r""" Synchronously fetch contact details

     Fetches a single person's work email, personal email, and/or phone number synchronously, meaning
    that you don't need to poll separately. This endpoint is slow, though, since it waits for the task
    to finish before returning.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only<br />• Plus 1 credits when the liveFetch flag is set&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary. Partial reveals only bill for
    delivered data.\">ⓘ</span></span>

    Args:
        body (SyncContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]]
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
    body: SyncContactEnrichmentBody,

) -> Optional[Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]]:
    r""" Synchronously fetch contact details

     Fetches a single person's work email, personal email, and/or phone number synchronously, meaning
    that you don't need to poll separately. This endpoint is slow, though, since it waits for the task
    to finish before returning.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only<br />• Plus 1 credits when the liveFetch flag is set&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary. Partial reveals only bill for
    delivered data.\">ⓘ</span></span>

    Args:
        body (SyncContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SyncContactEnrichmentResponse200, SyncContactEnrichmentResponse400, SyncContactEnrichmentResponse401, SyncContactEnrichmentResponse402, SyncContactEnrichmentResponse403, SyncContactEnrichmentResponse404, SyncContactEnrichmentResponse429, SyncContactEnrichmentResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
