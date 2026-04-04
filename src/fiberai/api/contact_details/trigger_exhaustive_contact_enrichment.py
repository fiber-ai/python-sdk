from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trigger_exhaustive_contact_enrichment_body import TriggerExhaustiveContactEnrichmentBody
from ...models.trigger_exhaustive_contact_enrichment_response_200 import TriggerExhaustiveContactEnrichmentResponse200
from ...models.trigger_exhaustive_contact_enrichment_response_400 import TriggerExhaustiveContactEnrichmentResponse400
from ...models.trigger_exhaustive_contact_enrichment_response_401 import TriggerExhaustiveContactEnrichmentResponse401
from ...models.trigger_exhaustive_contact_enrichment_response_402 import TriggerExhaustiveContactEnrichmentResponse402
from ...models.trigger_exhaustive_contact_enrichment_response_403 import TriggerExhaustiveContactEnrichmentResponse403
from ...models.trigger_exhaustive_contact_enrichment_response_404 import TriggerExhaustiveContactEnrichmentResponse404
from ...models.trigger_exhaustive_contact_enrichment_response_429 import TriggerExhaustiveContactEnrichmentResponse429
from ...models.trigger_exhaustive_contact_enrichment_response_500 import TriggerExhaustiveContactEnrichmentResponse500
from ...models.trigger_exhaustive_contact_enrichment_response_503 import TriggerExhaustiveContactEnrichmentResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TriggerExhaustiveContactEnrichmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/exhaustive/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TriggerExhaustiveContactEnrichmentResponse200
    | TriggerExhaustiveContactEnrichmentResponse400
    | TriggerExhaustiveContactEnrichmentResponse401
    | TriggerExhaustiveContactEnrichmentResponse402
    | TriggerExhaustiveContactEnrichmentResponse403
    | TriggerExhaustiveContactEnrichmentResponse404
    | TriggerExhaustiveContactEnrichmentResponse429
    | TriggerExhaustiveContactEnrichmentResponse500
    | TriggerExhaustiveContactEnrichmentResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TriggerExhaustiveContactEnrichmentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TriggerExhaustiveContactEnrichmentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TriggerExhaustiveContactEnrichmentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TriggerExhaustiveContactEnrichmentResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TriggerExhaustiveContactEnrichmentResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TriggerExhaustiveContactEnrichmentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TriggerExhaustiveContactEnrichmentResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TriggerExhaustiveContactEnrichmentResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TriggerExhaustiveContactEnrichmentResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TriggerExhaustiveContactEnrichmentResponse200
    | TriggerExhaustiveContactEnrichmentResponse400
    | TriggerExhaustiveContactEnrichmentResponse401
    | TriggerExhaustiveContactEnrichmentResponse402
    | TriggerExhaustiveContactEnrichmentResponse403
    | TriggerExhaustiveContactEnrichmentResponse404
    | TriggerExhaustiveContactEnrichmentResponse429
    | TriggerExhaustiveContactEnrichmentResponse500
    | TriggerExhaustiveContactEnrichmentResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TriggerExhaustiveContactEnrichmentBody,
) -> Response[
    TriggerExhaustiveContactEnrichmentResponse200
    | TriggerExhaustiveContactEnrichmentResponse400
    | TriggerExhaustiveContactEnrichmentResponse401
    | TriggerExhaustiveContactEnrichmentResponse402
    | TriggerExhaustiveContactEnrichmentResponse403
    | TriggerExhaustiveContactEnrichmentResponse404
    | TriggerExhaustiveContactEnrichmentResponse429
    | TriggerExhaustiveContactEnrichmentResponse500
    | TriggerExhaustiveContactEnrichmentResponse503
]:
    r"""Start exhaustive contact details reveal

     Maximum-coverage contact reveal — runs all available vendors in parallel for the most comprehensive
    results. This is asynchronous: call this endpoint to start the task, then poll /contact-
    details/exhaustive/poll with the returned task ID. Slower and more expensive than the synchronous
    endpoints, but returns more emails and phone numbers on average. For faster synchronous results, use
    /contact-details/single (standard) or /contact-details/turbo/sync (fastest).

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request (exhaustive mode):<br />• 12
    credits for all phone numbers AND all emails<br />• 5 credits for work email only<br />• 5 credits
    for personal email only<br />• 4 credits for phone only<br />• 9 credits for all emails&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary. Credits are charged after the
    reveal completes so partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (TriggerExhaustiveContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TriggerExhaustiveContactEnrichmentResponse200 | TriggerExhaustiveContactEnrichmentResponse400 | TriggerExhaustiveContactEnrichmentResponse401 | TriggerExhaustiveContactEnrichmentResponse402 | TriggerExhaustiveContactEnrichmentResponse403 | TriggerExhaustiveContactEnrichmentResponse404 | TriggerExhaustiveContactEnrichmentResponse429 | TriggerExhaustiveContactEnrichmentResponse500 | TriggerExhaustiveContactEnrichmentResponse503]
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
    client: AuthenticatedClient | Client,
    body: TriggerExhaustiveContactEnrichmentBody,
) -> (
    TriggerExhaustiveContactEnrichmentResponse200
    | TriggerExhaustiveContactEnrichmentResponse400
    | TriggerExhaustiveContactEnrichmentResponse401
    | TriggerExhaustiveContactEnrichmentResponse402
    | TriggerExhaustiveContactEnrichmentResponse403
    | TriggerExhaustiveContactEnrichmentResponse404
    | TriggerExhaustiveContactEnrichmentResponse429
    | TriggerExhaustiveContactEnrichmentResponse500
    | TriggerExhaustiveContactEnrichmentResponse503
    | None
):
    r"""Start exhaustive contact details reveal

     Maximum-coverage contact reveal — runs all available vendors in parallel for the most comprehensive
    results. This is asynchronous: call this endpoint to start the task, then poll /contact-
    details/exhaustive/poll with the returned task ID. Slower and more expensive than the synchronous
    endpoints, but returns more emails and phone numbers on average. For faster synchronous results, use
    /contact-details/single (standard) or /contact-details/turbo/sync (fastest).

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request (exhaustive mode):<br />• 12
    credits for all phone numbers AND all emails<br />• 5 credits for work email only<br />• 5 credits
    for personal email only<br />• 4 credits for phone only<br />• 9 credits for all emails&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary. Credits are charged after the
    reveal completes so partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (TriggerExhaustiveContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TriggerExhaustiveContactEnrichmentResponse200 | TriggerExhaustiveContactEnrichmentResponse400 | TriggerExhaustiveContactEnrichmentResponse401 | TriggerExhaustiveContactEnrichmentResponse402 | TriggerExhaustiveContactEnrichmentResponse403 | TriggerExhaustiveContactEnrichmentResponse404 | TriggerExhaustiveContactEnrichmentResponse429 | TriggerExhaustiveContactEnrichmentResponse500 | TriggerExhaustiveContactEnrichmentResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TriggerExhaustiveContactEnrichmentBody,
) -> Response[
    TriggerExhaustiveContactEnrichmentResponse200
    | TriggerExhaustiveContactEnrichmentResponse400
    | TriggerExhaustiveContactEnrichmentResponse401
    | TriggerExhaustiveContactEnrichmentResponse402
    | TriggerExhaustiveContactEnrichmentResponse403
    | TriggerExhaustiveContactEnrichmentResponse404
    | TriggerExhaustiveContactEnrichmentResponse429
    | TriggerExhaustiveContactEnrichmentResponse500
    | TriggerExhaustiveContactEnrichmentResponse503
]:
    r"""Start exhaustive contact details reveal

     Maximum-coverage contact reveal — runs all available vendors in parallel for the most comprehensive
    results. This is asynchronous: call this endpoint to start the task, then poll /contact-
    details/exhaustive/poll with the returned task ID. Slower and more expensive than the synchronous
    endpoints, but returns more emails and phone numbers on average. For faster synchronous results, use
    /contact-details/single (standard) or /contact-details/turbo/sync (fastest).

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request (exhaustive mode):<br />• 12
    credits for all phone numbers AND all emails<br />• 5 credits for work email only<br />• 5 credits
    for personal email only<br />• 4 credits for phone only<br />• 9 credits for all emails&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary. Credits are charged after the
    reveal completes so partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (TriggerExhaustiveContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TriggerExhaustiveContactEnrichmentResponse200 | TriggerExhaustiveContactEnrichmentResponse400 | TriggerExhaustiveContactEnrichmentResponse401 | TriggerExhaustiveContactEnrichmentResponse402 | TriggerExhaustiveContactEnrichmentResponse403 | TriggerExhaustiveContactEnrichmentResponse404 | TriggerExhaustiveContactEnrichmentResponse429 | TriggerExhaustiveContactEnrichmentResponse500 | TriggerExhaustiveContactEnrichmentResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TriggerExhaustiveContactEnrichmentBody,
) -> (
    TriggerExhaustiveContactEnrichmentResponse200
    | TriggerExhaustiveContactEnrichmentResponse400
    | TriggerExhaustiveContactEnrichmentResponse401
    | TriggerExhaustiveContactEnrichmentResponse402
    | TriggerExhaustiveContactEnrichmentResponse403
    | TriggerExhaustiveContactEnrichmentResponse404
    | TriggerExhaustiveContactEnrichmentResponse429
    | TriggerExhaustiveContactEnrichmentResponse500
    | TriggerExhaustiveContactEnrichmentResponse503
    | None
):
    r"""Start exhaustive contact details reveal

     Maximum-coverage contact reveal — runs all available vendors in parallel for the most comprehensive
    results. This is asynchronous: call this endpoint to start the task, then poll /contact-
    details/exhaustive/poll with the returned task ID. Slower and more expensive than the synchronous
    endpoints, but returns more emails and phone numbers on average. For faster synchronous results, use
    /contact-details/single (standard) or /contact-details/turbo/sync (fastest).

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request (exhaustive mode):<br />• 12
    credits for all phone numbers AND all emails<br />• 5 credits for work email only<br />• 5 credits
    for personal email only<br />• 4 credits for phone only<br />• 9 credits for all emails&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary. Credits are charged after the
    reveal completes so partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (TriggerExhaustiveContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TriggerExhaustiveContactEnrichmentResponse200 | TriggerExhaustiveContactEnrichmentResponse400 | TriggerExhaustiveContactEnrichmentResponse401 | TriggerExhaustiveContactEnrichmentResponse402 | TriggerExhaustiveContactEnrichmentResponse403 | TriggerExhaustiveContactEnrichmentResponse404 | TriggerExhaustiveContactEnrichmentResponse429 | TriggerExhaustiveContactEnrichmentResponse500 | TriggerExhaustiveContactEnrichmentResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
