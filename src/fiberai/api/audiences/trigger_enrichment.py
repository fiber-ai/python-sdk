from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trigger_enrichment_body import TriggerEnrichmentBody
from ...models.trigger_enrichment_response_200 import TriggerEnrichmentResponse200
from ...models.trigger_enrichment_response_400 import TriggerEnrichmentResponse400
from ...models.trigger_enrichment_response_401 import TriggerEnrichmentResponse401
from ...models.trigger_enrichment_response_402 import TriggerEnrichmentResponse402
from ...models.trigger_enrichment_response_403 import TriggerEnrichmentResponse403
from ...models.trigger_enrichment_response_404 import TriggerEnrichmentResponse404
from ...models.trigger_enrichment_response_429 import TriggerEnrichmentResponse429
from ...models.trigger_enrichment_response_500 import TriggerEnrichmentResponse500
from ...models.trigger_enrichment_response_503 import TriggerEnrichmentResponse503
from ...types import Response


def _get_kwargs(
    audience_id: str,
    *,
    body: TriggerEnrichmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/audiences/{audience_id}/enrich".format(
            audience_id=quote(str(audience_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TriggerEnrichmentResponse200
    | TriggerEnrichmentResponse400
    | TriggerEnrichmentResponse401
    | TriggerEnrichmentResponse402
    | TriggerEnrichmentResponse403
    | TriggerEnrichmentResponse404
    | TriggerEnrichmentResponse429
    | TriggerEnrichmentResponse500
    | TriggerEnrichmentResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TriggerEnrichmentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TriggerEnrichmentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TriggerEnrichmentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TriggerEnrichmentResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TriggerEnrichmentResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TriggerEnrichmentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TriggerEnrichmentResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TriggerEnrichmentResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TriggerEnrichmentResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TriggerEnrichmentResponse200
    | TriggerEnrichmentResponse400
    | TriggerEnrichmentResponse401
    | TriggerEnrichmentResponse402
    | TriggerEnrichmentResponse403
    | TriggerEnrichmentResponse404
    | TriggerEnrichmentResponse429
    | TriggerEnrichmentResponse500
    | TriggerEnrichmentResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TriggerEnrichmentBody,
) -> Response[
    TriggerEnrichmentResponse200
    | TriggerEnrichmentResponse400
    | TriggerEnrichmentResponse401
    | TriggerEnrichmentResponse402
    | TriggerEnrichmentResponse403
    | TriggerEnrichmentResponse404
    | TriggerEnrichmentResponse429
    | TriggerEnrichmentResponse500
    | TriggerEnrichmentResponse503
]:
    r"""Trigger audience enrichment

     Triggers the audience enrichment process. This runs company and prospect enrichment (live data,
    Sales Navigator, contact details) based on the configured enrichment types. The enrichment runs
    asynchronously - use the get-enrichment-status endpoint to poll for completion. Credits are charged
    immediately based on the estimated cost.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged immediately: 2 per work email, 2 per personal
    email, 3 per phone number, 1 per prospect live enrichment.&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary. Your total charge will vary based on the enrichment types
    selected and number of prospects.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (TriggerEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TriggerEnrichmentResponse200 | TriggerEnrichmentResponse400 | TriggerEnrichmentResponse401 | TriggerEnrichmentResponse402 | TriggerEnrichmentResponse403 | TriggerEnrichmentResponse404 | TriggerEnrichmentResponse429 | TriggerEnrichmentResponse500 | TriggerEnrichmentResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TriggerEnrichmentBody,
) -> (
    TriggerEnrichmentResponse200
    | TriggerEnrichmentResponse400
    | TriggerEnrichmentResponse401
    | TriggerEnrichmentResponse402
    | TriggerEnrichmentResponse403
    | TriggerEnrichmentResponse404
    | TriggerEnrichmentResponse429
    | TriggerEnrichmentResponse500
    | TriggerEnrichmentResponse503
    | None
):
    r"""Trigger audience enrichment

     Triggers the audience enrichment process. This runs company and prospect enrichment (live data,
    Sales Navigator, contact details) based on the configured enrichment types. The enrichment runs
    asynchronously - use the get-enrichment-status endpoint to poll for completion. Credits are charged
    immediately based on the estimated cost.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged immediately: 2 per work email, 2 per personal
    email, 3 per phone number, 1 per prospect live enrichment.&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary. Your total charge will vary based on the enrichment types
    selected and number of prospects.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (TriggerEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TriggerEnrichmentResponse200 | TriggerEnrichmentResponse400 | TriggerEnrichmentResponse401 | TriggerEnrichmentResponse402 | TriggerEnrichmentResponse403 | TriggerEnrichmentResponse404 | TriggerEnrichmentResponse429 | TriggerEnrichmentResponse500 | TriggerEnrichmentResponse503
    """

    return sync_detailed(
        audience_id=audience_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TriggerEnrichmentBody,
) -> Response[
    TriggerEnrichmentResponse200
    | TriggerEnrichmentResponse400
    | TriggerEnrichmentResponse401
    | TriggerEnrichmentResponse402
    | TriggerEnrichmentResponse403
    | TriggerEnrichmentResponse404
    | TriggerEnrichmentResponse429
    | TriggerEnrichmentResponse500
    | TriggerEnrichmentResponse503
]:
    r"""Trigger audience enrichment

     Triggers the audience enrichment process. This runs company and prospect enrichment (live data,
    Sales Navigator, contact details) based on the configured enrichment types. The enrichment runs
    asynchronously - use the get-enrichment-status endpoint to poll for completion. Credits are charged
    immediately based on the estimated cost.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged immediately: 2 per work email, 2 per personal
    email, 3 per phone number, 1 per prospect live enrichment.&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary. Your total charge will vary based on the enrichment types
    selected and number of prospects.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (TriggerEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TriggerEnrichmentResponse200 | TriggerEnrichmentResponse400 | TriggerEnrichmentResponse401 | TriggerEnrichmentResponse402 | TriggerEnrichmentResponse403 | TriggerEnrichmentResponse404 | TriggerEnrichmentResponse429 | TriggerEnrichmentResponse500 | TriggerEnrichmentResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TriggerEnrichmentBody,
) -> (
    TriggerEnrichmentResponse200
    | TriggerEnrichmentResponse400
    | TriggerEnrichmentResponse401
    | TriggerEnrichmentResponse402
    | TriggerEnrichmentResponse403
    | TriggerEnrichmentResponse404
    | TriggerEnrichmentResponse429
    | TriggerEnrichmentResponse500
    | TriggerEnrichmentResponse503
    | None
):
    r"""Trigger audience enrichment

     Triggers the audience enrichment process. This runs company and prospect enrichment (live data,
    Sales Navigator, contact details) based on the configured enrichment types. The enrichment runs
    asynchronously - use the get-enrichment-status endpoint to poll for completion. Credits are charged
    immediately based on the estimated cost.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged immediately: 2 per work email, 2 per personal
    email, 3 per phone number, 1 per prospect live enrichment.&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary. Your total charge will vary based on the enrichment types
    selected and number of prospects.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (TriggerEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TriggerEnrichmentResponse200 | TriggerEnrichmentResponse400 | TriggerEnrichmentResponse401 | TriggerEnrichmentResponse402 | TriggerEnrichmentResponse403 | TriggerEnrichmentResponse404 | TriggerEnrichmentResponse429 | TriggerEnrichmentResponse500 | TriggerEnrichmentResponse503
    """

    return (
        await asyncio_detailed(
            audience_id=audience_id,
            client=client,
            body=body,
        )
    ).parsed
