from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trigger_contact_enrichment_body import TriggerContactEnrichmentBody
from ...models.trigger_contact_enrichment_response_200 import TriggerContactEnrichmentResponse200
from ...models.trigger_contact_enrichment_response_400 import TriggerContactEnrichmentResponse400
from ...models.trigger_contact_enrichment_response_401 import TriggerContactEnrichmentResponse401
from ...models.trigger_contact_enrichment_response_402 import TriggerContactEnrichmentResponse402
from ...models.trigger_contact_enrichment_response_403 import TriggerContactEnrichmentResponse403
from ...models.trigger_contact_enrichment_response_404 import TriggerContactEnrichmentResponse404
from ...models.trigger_contact_enrichment_response_429 import TriggerContactEnrichmentResponse429
from ...models.trigger_contact_enrichment_response_500 import TriggerContactEnrichmentResponse500
from ...models.trigger_contact_enrichment_response_503 import TriggerContactEnrichmentResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TriggerContactEnrichmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TriggerContactEnrichmentResponse200
    | TriggerContactEnrichmentResponse400
    | TriggerContactEnrichmentResponse401
    | TriggerContactEnrichmentResponse402
    | TriggerContactEnrichmentResponse403
    | TriggerContactEnrichmentResponse404
    | TriggerContactEnrichmentResponse429
    | TriggerContactEnrichmentResponse500
    | TriggerContactEnrichmentResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TriggerContactEnrichmentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TriggerContactEnrichmentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TriggerContactEnrichmentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TriggerContactEnrichmentResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TriggerContactEnrichmentResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TriggerContactEnrichmentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TriggerContactEnrichmentResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TriggerContactEnrichmentResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TriggerContactEnrichmentResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TriggerContactEnrichmentResponse200
    | TriggerContactEnrichmentResponse400
    | TriggerContactEnrichmentResponse401
    | TriggerContactEnrichmentResponse402
    | TriggerContactEnrichmentResponse403
    | TriggerContactEnrichmentResponse404
    | TriggerContactEnrichmentResponse429
    | TriggerContactEnrichmentResponse500
    | TriggerContactEnrichmentResponse503
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
    body: TriggerContactEnrichmentBody,
) -> Response[
    TriggerContactEnrichmentResponse200
    | TriggerContactEnrichmentResponse400
    | TriggerContactEnrichmentResponse401
    | TriggerContactEnrichmentResponse402
    | TriggerContactEnrichmentResponse403
    | TriggerContactEnrichmentResponse404
    | TriggerContactEnrichmentResponse429
    | TriggerContactEnrichmentResponse500
    | TriggerContactEnrichmentResponse503
]:
    r"""Start fetching person's contact details

     Starts fetching a single person's contact details: personal email, work email, and/or phone number.
    This is an asynchronous task; use the polling endpoint afterward.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails (12 credits if exhaustive)<br />• 2 credits for work email only (5 credits if
    exhaustive)<br />• 2 credits for personal email only (5 credits if exhaustive)<br />• 3 credits for
    phone only (4 credits if exhaustive)<br />• 0 credits for all emails (9 credits if
    exhaustive)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Credits
    are charged after the reveal completes so partial reveals only bill for delivered
    data.\">ⓘ</span></span>

    Args:
        body (TriggerContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TriggerContactEnrichmentResponse200 | TriggerContactEnrichmentResponse400 | TriggerContactEnrichmentResponse401 | TriggerContactEnrichmentResponse402 | TriggerContactEnrichmentResponse403 | TriggerContactEnrichmentResponse404 | TriggerContactEnrichmentResponse429 | TriggerContactEnrichmentResponse500 | TriggerContactEnrichmentResponse503]
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
    body: TriggerContactEnrichmentBody,
) -> (
    TriggerContactEnrichmentResponse200
    | TriggerContactEnrichmentResponse400
    | TriggerContactEnrichmentResponse401
    | TriggerContactEnrichmentResponse402
    | TriggerContactEnrichmentResponse403
    | TriggerContactEnrichmentResponse404
    | TriggerContactEnrichmentResponse429
    | TriggerContactEnrichmentResponse500
    | TriggerContactEnrichmentResponse503
    | None
):
    r"""Start fetching person's contact details

     Starts fetching a single person's contact details: personal email, work email, and/or phone number.
    This is an asynchronous task; use the polling endpoint afterward.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails (12 credits if exhaustive)<br />• 2 credits for work email only (5 credits if
    exhaustive)<br />• 2 credits for personal email only (5 credits if exhaustive)<br />• 3 credits for
    phone only (4 credits if exhaustive)<br />• 0 credits for all emails (9 credits if
    exhaustive)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Credits
    are charged after the reveal completes so partial reveals only bill for delivered
    data.\">ⓘ</span></span>

    Args:
        body (TriggerContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TriggerContactEnrichmentResponse200 | TriggerContactEnrichmentResponse400 | TriggerContactEnrichmentResponse401 | TriggerContactEnrichmentResponse402 | TriggerContactEnrichmentResponse403 | TriggerContactEnrichmentResponse404 | TriggerContactEnrichmentResponse429 | TriggerContactEnrichmentResponse500 | TriggerContactEnrichmentResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TriggerContactEnrichmentBody,
) -> Response[
    TriggerContactEnrichmentResponse200
    | TriggerContactEnrichmentResponse400
    | TriggerContactEnrichmentResponse401
    | TriggerContactEnrichmentResponse402
    | TriggerContactEnrichmentResponse403
    | TriggerContactEnrichmentResponse404
    | TriggerContactEnrichmentResponse429
    | TriggerContactEnrichmentResponse500
    | TriggerContactEnrichmentResponse503
]:
    r"""Start fetching person's contact details

     Starts fetching a single person's contact details: personal email, work email, and/or phone number.
    This is an asynchronous task; use the polling endpoint afterward.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails (12 credits if exhaustive)<br />• 2 credits for work email only (5 credits if
    exhaustive)<br />• 2 credits for personal email only (5 credits if exhaustive)<br />• 3 credits for
    phone only (4 credits if exhaustive)<br />• 0 credits for all emails (9 credits if
    exhaustive)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Credits
    are charged after the reveal completes so partial reveals only bill for delivered
    data.\">ⓘ</span></span>

    Args:
        body (TriggerContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TriggerContactEnrichmentResponse200 | TriggerContactEnrichmentResponse400 | TriggerContactEnrichmentResponse401 | TriggerContactEnrichmentResponse402 | TriggerContactEnrichmentResponse403 | TriggerContactEnrichmentResponse404 | TriggerContactEnrichmentResponse429 | TriggerContactEnrichmentResponse500 | TriggerContactEnrichmentResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TriggerContactEnrichmentBody,
) -> (
    TriggerContactEnrichmentResponse200
    | TriggerContactEnrichmentResponse400
    | TriggerContactEnrichmentResponse401
    | TriggerContactEnrichmentResponse402
    | TriggerContactEnrichmentResponse403
    | TriggerContactEnrichmentResponse404
    | TriggerContactEnrichmentResponse429
    | TriggerContactEnrichmentResponse500
    | TriggerContactEnrichmentResponse503
    | None
):
    r"""Start fetching person's contact details

     Starts fetching a single person's contact details: personal email, work email, and/or phone number.
    This is an asynchronous task; use the polling endpoint afterward.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails (12 credits if exhaustive)<br />• 2 credits for work email only (5 credits if
    exhaustive)<br />• 2 credits for personal email only (5 credits if exhaustive)<br />• 3 credits for
    phone only (4 credits if exhaustive)<br />• 0 credits for all emails (9 credits if
    exhaustive)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Credits
    are charged after the reveal completes so partial reveals only bill for delivered
    data.\">ⓘ</span></span>

    Args:
        body (TriggerContactEnrichmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TriggerContactEnrichmentResponse200 | TriggerContactEnrichmentResponse400 | TriggerContactEnrichmentResponse401 | TriggerContactEnrichmentResponse402 | TriggerContactEnrichmentResponse403 | TriggerContactEnrichmentResponse404 | TriggerContactEnrichmentResponse429 | TriggerContactEnrichmentResponse500 | TriggerContactEnrichmentResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
