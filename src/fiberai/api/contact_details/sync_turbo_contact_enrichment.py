from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sync_turbo_contact_enrichment_body import SyncTurboContactEnrichmentBody
from ...models.sync_turbo_contact_enrichment_response_200 import SyncTurboContactEnrichmentResponse200
from ...models.sync_turbo_contact_enrichment_response_400 import SyncTurboContactEnrichmentResponse400
from ...models.sync_turbo_contact_enrichment_response_401 import SyncTurboContactEnrichmentResponse401
from ...models.sync_turbo_contact_enrichment_response_402 import SyncTurboContactEnrichmentResponse402
from ...models.sync_turbo_contact_enrichment_response_403 import SyncTurboContactEnrichmentResponse403
from ...models.sync_turbo_contact_enrichment_response_404 import SyncTurboContactEnrichmentResponse404
from ...models.sync_turbo_contact_enrichment_response_429 import SyncTurboContactEnrichmentResponse429
from ...models.sync_turbo_contact_enrichment_response_500 import SyncTurboContactEnrichmentResponse500
from ...models.sync_turbo_contact_enrichment_response_503 import SyncTurboContactEnrichmentResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SyncTurboContactEnrichmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/turbo/sync",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SyncTurboContactEnrichmentResponse200
    | SyncTurboContactEnrichmentResponse400
    | SyncTurboContactEnrichmentResponse401
    | SyncTurboContactEnrichmentResponse402
    | SyncTurboContactEnrichmentResponse403
    | SyncTurboContactEnrichmentResponse404
    | SyncTurboContactEnrichmentResponse429
    | SyncTurboContactEnrichmentResponse500
    | SyncTurboContactEnrichmentResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SyncTurboContactEnrichmentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SyncTurboContactEnrichmentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SyncTurboContactEnrichmentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SyncTurboContactEnrichmentResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SyncTurboContactEnrichmentResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SyncTurboContactEnrichmentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = SyncTurboContactEnrichmentResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SyncTurboContactEnrichmentResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SyncTurboContactEnrichmentResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SyncTurboContactEnrichmentResponse200
    | SyncTurboContactEnrichmentResponse400
    | SyncTurboContactEnrichmentResponse401
    | SyncTurboContactEnrichmentResponse402
    | SyncTurboContactEnrichmentResponse403
    | SyncTurboContactEnrichmentResponse404
    | SyncTurboContactEnrichmentResponse429
    | SyncTurboContactEnrichmentResponse500
    | SyncTurboContactEnrichmentResponse503
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
    body: SyncTurboContactEnrichmentBody,
) -> Response[
    SyncTurboContactEnrichmentResponse200
    | SyncTurboContactEnrichmentResponse400
    | SyncTurboContactEnrichmentResponse401
    | SyncTurboContactEnrichmentResponse402
    | SyncTurboContactEnrichmentResponse403
    | SyncTurboContactEnrichmentResponse404
    | SyncTurboContactEnrichmentResponse429
    | SyncTurboContactEnrichmentResponse500
    | SyncTurboContactEnrichmentResponse503
]:
    r"""Synchronously fetch contact details (turbo mode)

     Turbo mode: fetch contact details quickly. This endpoint uses a special faster enrichment stack and
    is optimized for speed and synchronous calls.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 7 credits for all phone
    numbers AND all emails<br />• 3 credits for work email only<br />• 3 credits for personal email
    only<br />• 5 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncTurboContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncTurboContactEnrichmentResponse200 | SyncTurboContactEnrichmentResponse400 | SyncTurboContactEnrichmentResponse401 | SyncTurboContactEnrichmentResponse402 | SyncTurboContactEnrichmentResponse403 | SyncTurboContactEnrichmentResponse404 | SyncTurboContactEnrichmentResponse429 | SyncTurboContactEnrichmentResponse500 | SyncTurboContactEnrichmentResponse503]
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
    body: SyncTurboContactEnrichmentBody,
) -> (
    SyncTurboContactEnrichmentResponse200
    | SyncTurboContactEnrichmentResponse400
    | SyncTurboContactEnrichmentResponse401
    | SyncTurboContactEnrichmentResponse402
    | SyncTurboContactEnrichmentResponse403
    | SyncTurboContactEnrichmentResponse404
    | SyncTurboContactEnrichmentResponse429
    | SyncTurboContactEnrichmentResponse500
    | SyncTurboContactEnrichmentResponse503
    | None
):
    r"""Synchronously fetch contact details (turbo mode)

     Turbo mode: fetch contact details quickly. This endpoint uses a special faster enrichment stack and
    is optimized for speed and synchronous calls.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 7 credits for all phone
    numbers AND all emails<br />• 3 credits for work email only<br />• 3 credits for personal email
    only<br />• 5 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncTurboContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncTurboContactEnrichmentResponse200 | SyncTurboContactEnrichmentResponse400 | SyncTurboContactEnrichmentResponse401 | SyncTurboContactEnrichmentResponse402 | SyncTurboContactEnrichmentResponse403 | SyncTurboContactEnrichmentResponse404 | SyncTurboContactEnrichmentResponse429 | SyncTurboContactEnrichmentResponse500 | SyncTurboContactEnrichmentResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncTurboContactEnrichmentBody,
) -> Response[
    SyncTurboContactEnrichmentResponse200
    | SyncTurboContactEnrichmentResponse400
    | SyncTurboContactEnrichmentResponse401
    | SyncTurboContactEnrichmentResponse402
    | SyncTurboContactEnrichmentResponse403
    | SyncTurboContactEnrichmentResponse404
    | SyncTurboContactEnrichmentResponse429
    | SyncTurboContactEnrichmentResponse500
    | SyncTurboContactEnrichmentResponse503
]:
    r"""Synchronously fetch contact details (turbo mode)

     Turbo mode: fetch contact details quickly. This endpoint uses a special faster enrichment stack and
    is optimized for speed and synchronous calls.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 7 credits for all phone
    numbers AND all emails<br />• 3 credits for work email only<br />• 3 credits for personal email
    only<br />• 5 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncTurboContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncTurboContactEnrichmentResponse200 | SyncTurboContactEnrichmentResponse400 | SyncTurboContactEnrichmentResponse401 | SyncTurboContactEnrichmentResponse402 | SyncTurboContactEnrichmentResponse403 | SyncTurboContactEnrichmentResponse404 | SyncTurboContactEnrichmentResponse429 | SyncTurboContactEnrichmentResponse500 | SyncTurboContactEnrichmentResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SyncTurboContactEnrichmentBody,
) -> (
    SyncTurboContactEnrichmentResponse200
    | SyncTurboContactEnrichmentResponse400
    | SyncTurboContactEnrichmentResponse401
    | SyncTurboContactEnrichmentResponse402
    | SyncTurboContactEnrichmentResponse403
    | SyncTurboContactEnrichmentResponse404
    | SyncTurboContactEnrichmentResponse429
    | SyncTurboContactEnrichmentResponse500
    | SyncTurboContactEnrichmentResponse503
    | None
):
    r"""Synchronously fetch contact details (turbo mode)

     Turbo mode: fetch contact details quickly. This endpoint uses a special faster enrichment stack and
    is optimized for speed and synchronous calls.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 7 credits for all phone
    numbers AND all emails<br />• 3 credits for work email only<br />• 3 credits for personal email
    only<br />• 5 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncTurboContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncTurboContactEnrichmentResponse200 | SyncTurboContactEnrichmentResponse400 | SyncTurboContactEnrichmentResponse401 | SyncTurboContactEnrichmentResponse402 | SyncTurboContactEnrichmentResponse403 | SyncTurboContactEnrichmentResponse404 | SyncTurboContactEnrichmentResponse429 | SyncTurboContactEnrichmentResponse500 | SyncTurboContactEnrichmentResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
