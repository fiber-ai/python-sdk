from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.premium_phone_reveal_body import PremiumPhoneRevealBody
from ...models.premium_phone_reveal_response_200 import PremiumPhoneRevealResponse200
from ...models.premium_phone_reveal_response_400 import PremiumPhoneRevealResponse400
from ...models.premium_phone_reveal_response_401 import PremiumPhoneRevealResponse401
from ...models.premium_phone_reveal_response_402 import PremiumPhoneRevealResponse402
from ...models.premium_phone_reveal_response_403 import PremiumPhoneRevealResponse403
from ...models.premium_phone_reveal_response_404 import PremiumPhoneRevealResponse404
from ...models.premium_phone_reveal_response_422 import PremiumPhoneRevealResponse422
from ...models.premium_phone_reveal_response_429 import PremiumPhoneRevealResponse429
from ...models.premium_phone_reveal_response_500 import PremiumPhoneRevealResponse500
from ...models.premium_phone_reveal_response_503 import PremiumPhoneRevealResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PremiumPhoneRevealBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/premium-phone/sync",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PremiumPhoneRevealResponse200
    | PremiumPhoneRevealResponse400
    | PremiumPhoneRevealResponse401
    | PremiumPhoneRevealResponse402
    | PremiumPhoneRevealResponse403
    | PremiumPhoneRevealResponse404
    | PremiumPhoneRevealResponse422
    | PremiumPhoneRevealResponse429
    | PremiumPhoneRevealResponse500
    | PremiumPhoneRevealResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PremiumPhoneRevealResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PremiumPhoneRevealResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PremiumPhoneRevealResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PremiumPhoneRevealResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PremiumPhoneRevealResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PremiumPhoneRevealResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PremiumPhoneRevealResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PremiumPhoneRevealResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PremiumPhoneRevealResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PremiumPhoneRevealResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PremiumPhoneRevealResponse200
    | PremiumPhoneRevealResponse400
    | PremiumPhoneRevealResponse401
    | PremiumPhoneRevealResponse402
    | PremiumPhoneRevealResponse403
    | PremiumPhoneRevealResponse404
    | PremiumPhoneRevealResponse422
    | PremiumPhoneRevealResponse429
    | PremiumPhoneRevealResponse500
    | PremiumPhoneRevealResponse503
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
    body: PremiumPhoneRevealBody,
) -> Response[
    PremiumPhoneRevealResponse200
    | PremiumPhoneRevealResponse400
    | PremiumPhoneRevealResponse401
    | PremiumPhoneRevealResponse402
    | PremiumPhoneRevealResponse403
    | PremiumPhoneRevealResponse404
    | PremiumPhoneRevealResponse422
    | PremiumPhoneRevealResponse429
    | PremiumPhoneRevealResponse500
    | PremiumPhoneRevealResponse503
]:
    r"""Premium phone number lookup

     Find and verify phone numbers for a LinkedIn profile using multiple data sources.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PremiumPhoneRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PremiumPhoneRevealResponse200 | PremiumPhoneRevealResponse400 | PremiumPhoneRevealResponse401 | PremiumPhoneRevealResponse402 | PremiumPhoneRevealResponse403 | PremiumPhoneRevealResponse404 | PremiumPhoneRevealResponse422 | PremiumPhoneRevealResponse429 | PremiumPhoneRevealResponse500 | PremiumPhoneRevealResponse503]
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
    body: PremiumPhoneRevealBody,
) -> (
    PremiumPhoneRevealResponse200
    | PremiumPhoneRevealResponse400
    | PremiumPhoneRevealResponse401
    | PremiumPhoneRevealResponse402
    | PremiumPhoneRevealResponse403
    | PremiumPhoneRevealResponse404
    | PremiumPhoneRevealResponse422
    | PremiumPhoneRevealResponse429
    | PremiumPhoneRevealResponse500
    | PremiumPhoneRevealResponse503
    | None
):
    r"""Premium phone number lookup

     Find and verify phone numbers for a LinkedIn profile using multiple data sources.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PremiumPhoneRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PremiumPhoneRevealResponse200 | PremiumPhoneRevealResponse400 | PremiumPhoneRevealResponse401 | PremiumPhoneRevealResponse402 | PremiumPhoneRevealResponse403 | PremiumPhoneRevealResponse404 | PremiumPhoneRevealResponse422 | PremiumPhoneRevealResponse429 | PremiumPhoneRevealResponse500 | PremiumPhoneRevealResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PremiumPhoneRevealBody,
) -> Response[
    PremiumPhoneRevealResponse200
    | PremiumPhoneRevealResponse400
    | PremiumPhoneRevealResponse401
    | PremiumPhoneRevealResponse402
    | PremiumPhoneRevealResponse403
    | PremiumPhoneRevealResponse404
    | PremiumPhoneRevealResponse422
    | PremiumPhoneRevealResponse429
    | PremiumPhoneRevealResponse500
    | PremiumPhoneRevealResponse503
]:
    r"""Premium phone number lookup

     Find and verify phone numbers for a LinkedIn profile using multiple data sources.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PremiumPhoneRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PremiumPhoneRevealResponse200 | PremiumPhoneRevealResponse400 | PremiumPhoneRevealResponse401 | PremiumPhoneRevealResponse402 | PremiumPhoneRevealResponse403 | PremiumPhoneRevealResponse404 | PremiumPhoneRevealResponse422 | PremiumPhoneRevealResponse429 | PremiumPhoneRevealResponse500 | PremiumPhoneRevealResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PremiumPhoneRevealBody,
) -> (
    PremiumPhoneRevealResponse200
    | PremiumPhoneRevealResponse400
    | PremiumPhoneRevealResponse401
    | PremiumPhoneRevealResponse402
    | PremiumPhoneRevealResponse403
    | PremiumPhoneRevealResponse404
    | PremiumPhoneRevealResponse422
    | PremiumPhoneRevealResponse429
    | PremiumPhoneRevealResponse500
    | PremiumPhoneRevealResponse503
    | None
):
    r"""Premium phone number lookup

     Find and verify phone numbers for a LinkedIn profile using multiple data sources.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PremiumPhoneRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PremiumPhoneRevealResponse200 | PremiumPhoneRevealResponse400 | PremiumPhoneRevealResponse401 | PremiumPhoneRevealResponse402 | PremiumPhoneRevealResponse403 | PremiumPhoneRevealResponse404 | PremiumPhoneRevealResponse422 | PremiumPhoneRevealResponse429 | PremiumPhoneRevealResponse500 | PremiumPhoneRevealResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
