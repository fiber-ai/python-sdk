from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lite_contact_reveal_body import LiteContactRevealBody
from ...models.lite_contact_reveal_response_200 import LiteContactRevealResponse200
from ...models.lite_contact_reveal_response_400 import LiteContactRevealResponse400
from ...models.lite_contact_reveal_response_401 import LiteContactRevealResponse401
from ...models.lite_contact_reveal_response_402 import LiteContactRevealResponse402
from ...models.lite_contact_reveal_response_403 import LiteContactRevealResponse403
from ...models.lite_contact_reveal_response_404 import LiteContactRevealResponse404
from ...models.lite_contact_reveal_response_429 import LiteContactRevealResponse429
from ...models.lite_contact_reveal_response_500 import LiteContactRevealResponse500
from ...models.lite_contact_reveal_response_503 import LiteContactRevealResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: LiteContactRevealBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/lite",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LiteContactRevealResponse200
    | LiteContactRevealResponse400
    | LiteContactRevealResponse401
    | LiteContactRevealResponse402
    | LiteContactRevealResponse403
    | LiteContactRevealResponse404
    | LiteContactRevealResponse429
    | LiteContactRevealResponse500
    | LiteContactRevealResponse503
    | None
):
    if response.status_code == 200:
        response_200 = LiteContactRevealResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LiteContactRevealResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LiteContactRevealResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = LiteContactRevealResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = LiteContactRevealResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LiteContactRevealResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = LiteContactRevealResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = LiteContactRevealResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = LiteContactRevealResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LiteContactRevealResponse200
    | LiteContactRevealResponse400
    | LiteContactRevealResponse401
    | LiteContactRevealResponse402
    | LiteContactRevealResponse403
    | LiteContactRevealResponse404
    | LiteContactRevealResponse429
    | LiteContactRevealResponse500
    | LiteContactRevealResponse503
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
    body: LiteContactRevealBody,
) -> Response[
    LiteContactRevealResponse200
    | LiteContactRevealResponse400
    | LiteContactRevealResponse401
    | LiteContactRevealResponse402
    | LiteContactRevealResponse403
    | LiteContactRevealResponse404
    | LiteContactRevealResponse429
    | LiteContactRevealResponse500
    | LiteContactRevealResponse503
]:
    r"""Reveal contact details (lite)

     Low-cost contact reveal path that searches differently. Compared with other contact reveal
    endpoints, this endpoint is priced lower but has lower yield (it may miss contacts that other
    endpoints can find).

    <span>⚡ <strong>Rate limit:</strong> 500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per lite email reveal&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (LiteContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiteContactRevealResponse200 | LiteContactRevealResponse400 | LiteContactRevealResponse401 | LiteContactRevealResponse402 | LiteContactRevealResponse403 | LiteContactRevealResponse404 | LiteContactRevealResponse429 | LiteContactRevealResponse500 | LiteContactRevealResponse503]
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
    body: LiteContactRevealBody,
) -> (
    LiteContactRevealResponse200
    | LiteContactRevealResponse400
    | LiteContactRevealResponse401
    | LiteContactRevealResponse402
    | LiteContactRevealResponse403
    | LiteContactRevealResponse404
    | LiteContactRevealResponse429
    | LiteContactRevealResponse500
    | LiteContactRevealResponse503
    | None
):
    r"""Reveal contact details (lite)

     Low-cost contact reveal path that searches differently. Compared with other contact reveal
    endpoints, this endpoint is priced lower but has lower yield (it may miss contacts that other
    endpoints can find).

    <span>⚡ <strong>Rate limit:</strong> 500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per lite email reveal&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (LiteContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiteContactRevealResponse200 | LiteContactRevealResponse400 | LiteContactRevealResponse401 | LiteContactRevealResponse402 | LiteContactRevealResponse403 | LiteContactRevealResponse404 | LiteContactRevealResponse429 | LiteContactRevealResponse500 | LiteContactRevealResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LiteContactRevealBody,
) -> Response[
    LiteContactRevealResponse200
    | LiteContactRevealResponse400
    | LiteContactRevealResponse401
    | LiteContactRevealResponse402
    | LiteContactRevealResponse403
    | LiteContactRevealResponse404
    | LiteContactRevealResponse429
    | LiteContactRevealResponse500
    | LiteContactRevealResponse503
]:
    r"""Reveal contact details (lite)

     Low-cost contact reveal path that searches differently. Compared with other contact reveal
    endpoints, this endpoint is priced lower but has lower yield (it may miss contacts that other
    endpoints can find).

    <span>⚡ <strong>Rate limit:</strong> 500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per lite email reveal&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (LiteContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiteContactRevealResponse200 | LiteContactRevealResponse400 | LiteContactRevealResponse401 | LiteContactRevealResponse402 | LiteContactRevealResponse403 | LiteContactRevealResponse404 | LiteContactRevealResponse429 | LiteContactRevealResponse500 | LiteContactRevealResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LiteContactRevealBody,
) -> (
    LiteContactRevealResponse200
    | LiteContactRevealResponse400
    | LiteContactRevealResponse401
    | LiteContactRevealResponse402
    | LiteContactRevealResponse403
    | LiteContactRevealResponse404
    | LiteContactRevealResponse429
    | LiteContactRevealResponse500
    | LiteContactRevealResponse503
    | None
):
    r"""Reveal contact details (lite)

     Low-cost contact reveal path that searches differently. Compared with other contact reveal
    endpoints, this endpoint is priced lower but has lower yield (it may miss contacts that other
    endpoints can find).

    <span>⚡ <strong>Rate limit:</strong> 500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per lite email reveal&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (LiteContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiteContactRevealResponse200 | LiteContactRevealResponse400 | LiteContactRevealResponse401 | LiteContactRevealResponse402 | LiteContactRevealResponse403 | LiteContactRevealResponse404 | LiteContactRevealResponse429 | LiteContactRevealResponse500 | LiteContactRevealResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
