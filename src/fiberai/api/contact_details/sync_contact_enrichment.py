from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sync_contact_enrichment_body import SyncContactEnrichmentBody
from ...models.sync_contact_enrichment_response_200 import SyncContactEnrichmentResponse200
from ...models.sync_contact_enrichment_response_400 import SyncContactEnrichmentResponse400
from ...models.sync_contact_enrichment_response_401 import SyncContactEnrichmentResponse401
from ...models.sync_contact_enrichment_response_402 import SyncContactEnrichmentResponse402
from ...models.sync_contact_enrichment_response_403 import SyncContactEnrichmentResponse403
from ...models.sync_contact_enrichment_response_404 import SyncContactEnrichmentResponse404
from ...models.sync_contact_enrichment_response_429 import SyncContactEnrichmentResponse429
from ...models.sync_contact_enrichment_response_500 import SyncContactEnrichmentResponse500
from ...models.sync_contact_enrichment_response_503 import SyncContactEnrichmentResponse503
from ...types import Response


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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SyncContactEnrichmentResponse200
    | SyncContactEnrichmentResponse400
    | SyncContactEnrichmentResponse401
    | SyncContactEnrichmentResponse402
    | SyncContactEnrichmentResponse403
    | SyncContactEnrichmentResponse404
    | SyncContactEnrichmentResponse429
    | SyncContactEnrichmentResponse500
    | SyncContactEnrichmentResponse503
    | None
):
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

    if response.status_code == 503:
        response_503 = SyncContactEnrichmentResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SyncContactEnrichmentResponse200
    | SyncContactEnrichmentResponse400
    | SyncContactEnrichmentResponse401
    | SyncContactEnrichmentResponse402
    | SyncContactEnrichmentResponse403
    | SyncContactEnrichmentResponse404
    | SyncContactEnrichmentResponse429
    | SyncContactEnrichmentResponse500
    | SyncContactEnrichmentResponse503
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
    body: SyncContactEnrichmentBody,
) -> Response[
    SyncContactEnrichmentResponse200
    | SyncContactEnrichmentResponse400
    | SyncContactEnrichmentResponse401
    | SyncContactEnrichmentResponse402
    | SyncContactEnrichmentResponse403
    | SyncContactEnrichmentResponse404
    | SyncContactEnrichmentResponse429
    | SyncContactEnrichmentResponse500
    | SyncContactEnrichmentResponse503
]:
    r"""Synchronously fetch contact details

     Fetches a single person's work email, personal email, and/or phone number synchronously, meaning
    that you don't need to poll separately. This endpoint is slow, though, since it waits for the task
    to finish before returning.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails (12 credits if exhaustive)<br />• 2 credits for work email only (5 credits if
    exhaustive)<br />• 2 credits for personal email only (5 credits if exhaustive)<br />• 3 credits for
    phone only (4 credits if exhaustive)<br />• 0 credits for all emails (9 credits if
    exhaustive)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Partial
    reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncContactEnrichmentResponse200 | SyncContactEnrichmentResponse400 | SyncContactEnrichmentResponse401 | SyncContactEnrichmentResponse402 | SyncContactEnrichmentResponse403 | SyncContactEnrichmentResponse404 | SyncContactEnrichmentResponse429 | SyncContactEnrichmentResponse500 | SyncContactEnrichmentResponse503]
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
    body: SyncContactEnrichmentBody,
) -> (
    SyncContactEnrichmentResponse200
    | SyncContactEnrichmentResponse400
    | SyncContactEnrichmentResponse401
    | SyncContactEnrichmentResponse402
    | SyncContactEnrichmentResponse403
    | SyncContactEnrichmentResponse404
    | SyncContactEnrichmentResponse429
    | SyncContactEnrichmentResponse500
    | SyncContactEnrichmentResponse503
    | None
):
    r"""Synchronously fetch contact details

     Fetches a single person's work email, personal email, and/or phone number synchronously, meaning
    that you don't need to poll separately. This endpoint is slow, though, since it waits for the task
    to finish before returning.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails (12 credits if exhaustive)<br />• 2 credits for work email only (5 credits if
    exhaustive)<br />• 2 credits for personal email only (5 credits if exhaustive)<br />• 3 credits for
    phone only (4 credits if exhaustive)<br />• 0 credits for all emails (9 credits if
    exhaustive)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Partial
    reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncContactEnrichmentResponse200 | SyncContactEnrichmentResponse400 | SyncContactEnrichmentResponse401 | SyncContactEnrichmentResponse402 | SyncContactEnrichmentResponse403 | SyncContactEnrichmentResponse404 | SyncContactEnrichmentResponse429 | SyncContactEnrichmentResponse500 | SyncContactEnrichmentResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncContactEnrichmentBody,
) -> Response[
    SyncContactEnrichmentResponse200
    | SyncContactEnrichmentResponse400
    | SyncContactEnrichmentResponse401
    | SyncContactEnrichmentResponse402
    | SyncContactEnrichmentResponse403
    | SyncContactEnrichmentResponse404
    | SyncContactEnrichmentResponse429
    | SyncContactEnrichmentResponse500
    | SyncContactEnrichmentResponse503
]:
    r"""Synchronously fetch contact details

     Fetches a single person's work email, personal email, and/or phone number synchronously, meaning
    that you don't need to poll separately. This endpoint is slow, though, since it waits for the task
    to finish before returning.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails (12 credits if exhaustive)<br />• 2 credits for work email only (5 credits if
    exhaustive)<br />• 2 credits for personal email only (5 credits if exhaustive)<br />• 3 credits for
    phone only (4 credits if exhaustive)<br />• 0 credits for all emails (9 credits if
    exhaustive)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Partial
    reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncContactEnrichmentResponse200 | SyncContactEnrichmentResponse400 | SyncContactEnrichmentResponse401 | SyncContactEnrichmentResponse402 | SyncContactEnrichmentResponse403 | SyncContactEnrichmentResponse404 | SyncContactEnrichmentResponse429 | SyncContactEnrichmentResponse500 | SyncContactEnrichmentResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SyncContactEnrichmentBody,
) -> (
    SyncContactEnrichmentResponse200
    | SyncContactEnrichmentResponse400
    | SyncContactEnrichmentResponse401
    | SyncContactEnrichmentResponse402
    | SyncContactEnrichmentResponse403
    | SyncContactEnrichmentResponse404
    | SyncContactEnrichmentResponse429
    | SyncContactEnrichmentResponse500
    | SyncContactEnrichmentResponse503
    | None
):
    r"""Synchronously fetch contact details

     Fetches a single person's work email, personal email, and/or phone number synchronously, meaning
    that you don't need to poll separately. This endpoint is slow, though, since it waits for the task
    to finish before returning.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails (12 credits if exhaustive)<br />• 2 credits for work email only (5 credits if
    exhaustive)<br />• 2 credits for personal email only (5 credits if exhaustive)<br />• 3 credits for
    phone only (4 credits if exhaustive)<br />• 0 credits for all emails (9 credits if
    exhaustive)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Partial
    reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncContactEnrichmentResponse200 | SyncContactEnrichmentResponse400 | SyncContactEnrichmentResponse401 | SyncContactEnrichmentResponse402 | SyncContactEnrichmentResponse403 | SyncContactEnrichmentResponse404 | SyncContactEnrichmentResponse429 | SyncContactEnrichmentResponse500 | SyncContactEnrichmentResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
