from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.poll_batch_contact_enrichment_body import PollBatchContactEnrichmentBody
from ...models.poll_batch_contact_enrichment_response_200 import PollBatchContactEnrichmentResponse200
from ...models.poll_batch_contact_enrichment_response_400 import PollBatchContactEnrichmentResponse400
from ...models.poll_batch_contact_enrichment_response_401 import PollBatchContactEnrichmentResponse401
from ...models.poll_batch_contact_enrichment_response_402 import PollBatchContactEnrichmentResponse402
from ...models.poll_batch_contact_enrichment_response_403 import PollBatchContactEnrichmentResponse403
from ...models.poll_batch_contact_enrichment_response_404 import PollBatchContactEnrichmentResponse404
from ...models.poll_batch_contact_enrichment_response_429 import PollBatchContactEnrichmentResponse429
from ...models.poll_batch_contact_enrichment_response_500 import PollBatchContactEnrichmentResponse500
from typing import cast



def _get_kwargs(
    *,
    body: PollBatchContactEnrichmentBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-enrich/batch/poll",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]]:
    if response.status_code == 200:
        response_200 = PollBatchContactEnrichmentResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PollBatchContactEnrichmentResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PollBatchContactEnrichmentResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = PollBatchContactEnrichmentResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = PollBatchContactEnrichmentResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PollBatchContactEnrichmentResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = PollBatchContactEnrichmentResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = PollBatchContactEnrichmentResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PollBatchContactEnrichmentBody,

) -> Response[Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]]:
    """ Poll batch contact enrichment

     Polls a batch contact enrichment task. Returns partial results as they complete. Call this endpoint
    repeatedly until the 'done' field is true. Use the task ID returned from the 'Start batch contact
    enrichment' endpoint.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    Args:
        body (PollBatchContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]]
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
    body: PollBatchContactEnrichmentBody,

) -> Optional[Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]]:
    """ Poll batch contact enrichment

     Polls a batch contact enrichment task. Returns partial results as they complete. Call this endpoint
    repeatedly until the 'done' field is true. Use the task ID returned from the 'Start batch contact
    enrichment' endpoint.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    Args:
        body (PollBatchContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PollBatchContactEnrichmentBody,

) -> Response[Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]]:
    """ Poll batch contact enrichment

     Polls a batch contact enrichment task. Returns partial results as they complete. Call this endpoint
    repeatedly until the 'done' field is true. Use the task ID returned from the 'Start batch contact
    enrichment' endpoint.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    Args:
        body (PollBatchContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]]
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
    body: PollBatchContactEnrichmentBody,

) -> Optional[Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]]:
    """ Poll batch contact enrichment

     Polls a batch contact enrichment task. Returns partial results as they complete. Call this endpoint
    repeatedly until the 'done' field is true. Use the task ID returned from the 'Start batch contact
    enrichment' endpoint.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    Args:
        body (PollBatchContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PollBatchContactEnrichmentResponse200, PollBatchContactEnrichmentResponse400, PollBatchContactEnrichmentResponse401, PollBatchContactEnrichmentResponse402, PollBatchContactEnrichmentResponse403, PollBatchContactEnrichmentResponse404, PollBatchContactEnrichmentResponse429, PollBatchContactEnrichmentResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
