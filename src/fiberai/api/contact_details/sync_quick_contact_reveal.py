from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sync_quick_contact_reveal_body import SyncQuickContactRevealBody
from ...models.sync_quick_contact_reveal_response_200 import SyncQuickContactRevealResponse200
from ...models.sync_quick_contact_reveal_response_400 import SyncQuickContactRevealResponse400
from ...models.sync_quick_contact_reveal_response_401 import SyncQuickContactRevealResponse401
from ...models.sync_quick_contact_reveal_response_402 import SyncQuickContactRevealResponse402
from ...models.sync_quick_contact_reveal_response_403 import SyncQuickContactRevealResponse403
from ...models.sync_quick_contact_reveal_response_404 import SyncQuickContactRevealResponse404
from ...models.sync_quick_contact_reveal_response_429 import SyncQuickContactRevealResponse429
from ...models.sync_quick_contact_reveal_response_500 import SyncQuickContactRevealResponse500
from ...models.sync_quick_contact_reveal_response_503 import SyncQuickContactRevealResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SyncQuickContactRevealBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SyncQuickContactRevealResponse200
    | SyncQuickContactRevealResponse400
    | SyncQuickContactRevealResponse401
    | SyncQuickContactRevealResponse402
    | SyncQuickContactRevealResponse403
    | SyncQuickContactRevealResponse404
    | SyncQuickContactRevealResponse429
    | SyncQuickContactRevealResponse500
    | SyncQuickContactRevealResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SyncQuickContactRevealResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SyncQuickContactRevealResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SyncQuickContactRevealResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SyncQuickContactRevealResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SyncQuickContactRevealResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SyncQuickContactRevealResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = SyncQuickContactRevealResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SyncQuickContactRevealResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SyncQuickContactRevealResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SyncQuickContactRevealResponse200
    | SyncQuickContactRevealResponse400
    | SyncQuickContactRevealResponse401
    | SyncQuickContactRevealResponse402
    | SyncQuickContactRevealResponse403
    | SyncQuickContactRevealResponse404
    | SyncQuickContactRevealResponse429
    | SyncQuickContactRevealResponse500
    | SyncQuickContactRevealResponse503
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
    body: SyncQuickContactRevealBody,
) -> Response[
    SyncQuickContactRevealResponse200
    | SyncQuickContactRevealResponse400
    | SyncQuickContactRevealResponse401
    | SyncQuickContactRevealResponse402
    | SyncQuickContactRevealResponse403
    | SyncQuickContactRevealResponse404
    | SyncQuickContactRevealResponse429
    | SyncQuickContactRevealResponse500
    | SyncQuickContactRevealResponse503
]:
    r"""Reveal contact details (new, synchronous)

     Streamlined synchronous contact reveal. Only requires a LinkedIn URL — profile details are resolved
    automatically. Uses a faster enrichment stack. For hyper-speed requirements, consider using the
    turbo endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 200 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncQuickContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncQuickContactRevealResponse200 | SyncQuickContactRevealResponse400 | SyncQuickContactRevealResponse401 | SyncQuickContactRevealResponse402 | SyncQuickContactRevealResponse403 | SyncQuickContactRevealResponse404 | SyncQuickContactRevealResponse429 | SyncQuickContactRevealResponse500 | SyncQuickContactRevealResponse503]
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
    body: SyncQuickContactRevealBody,
) -> (
    SyncQuickContactRevealResponse200
    | SyncQuickContactRevealResponse400
    | SyncQuickContactRevealResponse401
    | SyncQuickContactRevealResponse402
    | SyncQuickContactRevealResponse403
    | SyncQuickContactRevealResponse404
    | SyncQuickContactRevealResponse429
    | SyncQuickContactRevealResponse500
    | SyncQuickContactRevealResponse503
    | None
):
    r"""Reveal contact details (new, synchronous)

     Streamlined synchronous contact reveal. Only requires a LinkedIn URL — profile details are resolved
    automatically. Uses a faster enrichment stack. For hyper-speed requirements, consider using the
    turbo endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 200 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncQuickContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncQuickContactRevealResponse200 | SyncQuickContactRevealResponse400 | SyncQuickContactRevealResponse401 | SyncQuickContactRevealResponse402 | SyncQuickContactRevealResponse403 | SyncQuickContactRevealResponse404 | SyncQuickContactRevealResponse429 | SyncQuickContactRevealResponse500 | SyncQuickContactRevealResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncQuickContactRevealBody,
) -> Response[
    SyncQuickContactRevealResponse200
    | SyncQuickContactRevealResponse400
    | SyncQuickContactRevealResponse401
    | SyncQuickContactRevealResponse402
    | SyncQuickContactRevealResponse403
    | SyncQuickContactRevealResponse404
    | SyncQuickContactRevealResponse429
    | SyncQuickContactRevealResponse500
    | SyncQuickContactRevealResponse503
]:
    r"""Reveal contact details (new, synchronous)

     Streamlined synchronous contact reveal. Only requires a LinkedIn URL — profile details are resolved
    automatically. Uses a faster enrichment stack. For hyper-speed requirements, consider using the
    turbo endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 200 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncQuickContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncQuickContactRevealResponse200 | SyncQuickContactRevealResponse400 | SyncQuickContactRevealResponse401 | SyncQuickContactRevealResponse402 | SyncQuickContactRevealResponse403 | SyncQuickContactRevealResponse404 | SyncQuickContactRevealResponse429 | SyncQuickContactRevealResponse500 | SyncQuickContactRevealResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SyncQuickContactRevealBody,
) -> (
    SyncQuickContactRevealResponse200
    | SyncQuickContactRevealResponse400
    | SyncQuickContactRevealResponse401
    | SyncQuickContactRevealResponse402
    | SyncQuickContactRevealResponse403
    | SyncQuickContactRevealResponse404
    | SyncQuickContactRevealResponse429
    | SyncQuickContactRevealResponse500
    | SyncQuickContactRevealResponse503
    | None
):
    r"""Reveal contact details (new, synchronous)

     Streamlined synchronous contact reveal. Only requires a LinkedIn URL — profile details are resolved
    automatically. Uses a faster enrichment stack. For hyper-speed requirements, consider using the
    turbo endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 200 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Partial reveals only bill for delivered data.\">ⓘ</span></span>

    Args:
        body (SyncQuickContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncQuickContactRevealResponse200 | SyncQuickContactRevealResponse400 | SyncQuickContactRevealResponse401 | SyncQuickContactRevealResponse402 | SyncQuickContactRevealResponse403 | SyncQuickContactRevealResponse404 | SyncQuickContactRevealResponse429 | SyncQuickContactRevealResponse500 | SyncQuickContactRevealResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
