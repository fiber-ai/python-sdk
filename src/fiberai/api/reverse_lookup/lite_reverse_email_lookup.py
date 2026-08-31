from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lite_reverse_email_lookup_body import LiteReverseEmailLookupBody
from ...models.lite_reverse_email_lookup_response_200 import LiteReverseEmailLookupResponse200
from ...models.lite_reverse_email_lookup_response_400 import LiteReverseEmailLookupResponse400
from ...models.lite_reverse_email_lookup_response_401 import LiteReverseEmailLookupResponse401
from ...models.lite_reverse_email_lookup_response_402 import LiteReverseEmailLookupResponse402
from ...models.lite_reverse_email_lookup_response_403 import LiteReverseEmailLookupResponse403
from ...models.lite_reverse_email_lookup_response_404 import LiteReverseEmailLookupResponse404
from ...models.lite_reverse_email_lookup_response_422 import LiteReverseEmailLookupResponse422
from ...models.lite_reverse_email_lookup_response_429 import LiteReverseEmailLookupResponse429
from ...models.lite_reverse_email_lookup_response_500 import LiteReverseEmailLookupResponse500
from ...models.lite_reverse_email_lookup_response_503 import LiteReverseEmailLookupResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: LiteReverseEmailLookupBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/email-to-person/single/lite",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LiteReverseEmailLookupResponse200
    | LiteReverseEmailLookupResponse400
    | LiteReverseEmailLookupResponse401
    | LiteReverseEmailLookupResponse402
    | LiteReverseEmailLookupResponse403
    | LiteReverseEmailLookupResponse404
    | LiteReverseEmailLookupResponse422
    | LiteReverseEmailLookupResponse429
    | LiteReverseEmailLookupResponse500
    | LiteReverseEmailLookupResponse503
    | None
):
    if response.status_code == 200:
        response_200 = LiteReverseEmailLookupResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LiteReverseEmailLookupResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LiteReverseEmailLookupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = LiteReverseEmailLookupResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = LiteReverseEmailLookupResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LiteReverseEmailLookupResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = LiteReverseEmailLookupResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = LiteReverseEmailLookupResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = LiteReverseEmailLookupResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = LiteReverseEmailLookupResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LiteReverseEmailLookupResponse200
    | LiteReverseEmailLookupResponse400
    | LiteReverseEmailLookupResponse401
    | LiteReverseEmailLookupResponse402
    | LiteReverseEmailLookupResponse403
    | LiteReverseEmailLookupResponse404
    | LiteReverseEmailLookupResponse422
    | LiteReverseEmailLookupResponse429
    | LiteReverseEmailLookupResponse500
    | LiteReverseEmailLookupResponse503
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
    body: LiteReverseEmailLookupBody,
) -> Response[
    LiteReverseEmailLookupResponse200
    | LiteReverseEmailLookupResponse400
    | LiteReverseEmailLookupResponse401
    | LiteReverseEmailLookupResponse402
    | LiteReverseEmailLookupResponse403
    | LiteReverseEmailLookupResponse404
    | LiteReverseEmailLookupResponse422
    | LiteReverseEmailLookupResponse429
    | LiteReverseEmailLookupResponse500
    | LiteReverseEmailLookupResponse503
]:
    """Find person by email (lite, high-volume)

     Given an email address, find the person's LinkedIn profile.
    Lite version optimized for high-volume usage at lower cost. Skips expensive yield increasing
    operations.

    <span>⚡ <strong>Rate limit:</strong> 3000 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per email lookup (lite)&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (LiteReverseEmailLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiteReverseEmailLookupResponse200 | LiteReverseEmailLookupResponse400 | LiteReverseEmailLookupResponse401 | LiteReverseEmailLookupResponse402 | LiteReverseEmailLookupResponse403 | LiteReverseEmailLookupResponse404 | LiteReverseEmailLookupResponse422 | LiteReverseEmailLookupResponse429 | LiteReverseEmailLookupResponse500 | LiteReverseEmailLookupResponse503]
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
    body: LiteReverseEmailLookupBody,
) -> (
    LiteReverseEmailLookupResponse200
    | LiteReverseEmailLookupResponse400
    | LiteReverseEmailLookupResponse401
    | LiteReverseEmailLookupResponse402
    | LiteReverseEmailLookupResponse403
    | LiteReverseEmailLookupResponse404
    | LiteReverseEmailLookupResponse422
    | LiteReverseEmailLookupResponse429
    | LiteReverseEmailLookupResponse500
    | LiteReverseEmailLookupResponse503
    | None
):
    """Find person by email (lite, high-volume)

     Given an email address, find the person's LinkedIn profile.
    Lite version optimized for high-volume usage at lower cost. Skips expensive yield increasing
    operations.

    <span>⚡ <strong>Rate limit:</strong> 3000 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per email lookup (lite)&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (LiteReverseEmailLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiteReverseEmailLookupResponse200 | LiteReverseEmailLookupResponse400 | LiteReverseEmailLookupResponse401 | LiteReverseEmailLookupResponse402 | LiteReverseEmailLookupResponse403 | LiteReverseEmailLookupResponse404 | LiteReverseEmailLookupResponse422 | LiteReverseEmailLookupResponse429 | LiteReverseEmailLookupResponse500 | LiteReverseEmailLookupResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LiteReverseEmailLookupBody,
) -> Response[
    LiteReverseEmailLookupResponse200
    | LiteReverseEmailLookupResponse400
    | LiteReverseEmailLookupResponse401
    | LiteReverseEmailLookupResponse402
    | LiteReverseEmailLookupResponse403
    | LiteReverseEmailLookupResponse404
    | LiteReverseEmailLookupResponse422
    | LiteReverseEmailLookupResponse429
    | LiteReverseEmailLookupResponse500
    | LiteReverseEmailLookupResponse503
]:
    """Find person by email (lite, high-volume)

     Given an email address, find the person's LinkedIn profile.
    Lite version optimized for high-volume usage at lower cost. Skips expensive yield increasing
    operations.

    <span>⚡ <strong>Rate limit:</strong> 3000 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per email lookup (lite)&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (LiteReverseEmailLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiteReverseEmailLookupResponse200 | LiteReverseEmailLookupResponse400 | LiteReverseEmailLookupResponse401 | LiteReverseEmailLookupResponse402 | LiteReverseEmailLookupResponse403 | LiteReverseEmailLookupResponse404 | LiteReverseEmailLookupResponse422 | LiteReverseEmailLookupResponse429 | LiteReverseEmailLookupResponse500 | LiteReverseEmailLookupResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LiteReverseEmailLookupBody,
) -> (
    LiteReverseEmailLookupResponse200
    | LiteReverseEmailLookupResponse400
    | LiteReverseEmailLookupResponse401
    | LiteReverseEmailLookupResponse402
    | LiteReverseEmailLookupResponse403
    | LiteReverseEmailLookupResponse404
    | LiteReverseEmailLookupResponse422
    | LiteReverseEmailLookupResponse429
    | LiteReverseEmailLookupResponse500
    | LiteReverseEmailLookupResponse503
    | None
):
    """Find person by email (lite, high-volume)

     Given an email address, find the person's LinkedIn profile.
    Lite version optimized for high-volume usage at lower cost. Skips expensive yield increasing
    operations.

    <span>⚡ <strong>Rate limit:</strong> 3000 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per email lookup (lite)&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (LiteReverseEmailLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiteReverseEmailLookupResponse200 | LiteReverseEmailLookupResponse400 | LiteReverseEmailLookupResponse401 | LiteReverseEmailLookupResponse402 | LiteReverseEmailLookupResponse403 | LiteReverseEmailLookupResponse404 | LiteReverseEmailLookupResponse422 | LiteReverseEmailLookupResponse429 | LiteReverseEmailLookupResponse500 | LiteReverseEmailLookupResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
