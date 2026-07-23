from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reverse_phone_lookup_body import ReversePhoneLookupBody
from ...models.reverse_phone_lookup_response_200 import ReversePhoneLookupResponse200
from ...models.reverse_phone_lookup_response_400 import ReversePhoneLookupResponse400
from ...models.reverse_phone_lookup_response_401 import ReversePhoneLookupResponse401
from ...models.reverse_phone_lookup_response_402 import ReversePhoneLookupResponse402
from ...models.reverse_phone_lookup_response_403 import ReversePhoneLookupResponse403
from ...models.reverse_phone_lookup_response_404 import ReversePhoneLookupResponse404
from ...models.reverse_phone_lookup_response_422 import ReversePhoneLookupResponse422
from ...models.reverse_phone_lookup_response_429 import ReversePhoneLookupResponse429
from ...models.reverse_phone_lookup_response_500 import ReversePhoneLookupResponse500
from ...models.reverse_phone_lookup_response_503 import ReversePhoneLookupResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ReversePhoneLookupBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/phone-to-person/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ReversePhoneLookupResponse200
    | ReversePhoneLookupResponse400
    | ReversePhoneLookupResponse401
    | ReversePhoneLookupResponse402
    | ReversePhoneLookupResponse403
    | ReversePhoneLookupResponse404
    | ReversePhoneLookupResponse422
    | ReversePhoneLookupResponse429
    | ReversePhoneLookupResponse500
    | ReversePhoneLookupResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ReversePhoneLookupResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ReversePhoneLookupResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ReversePhoneLookupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ReversePhoneLookupResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ReversePhoneLookupResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ReversePhoneLookupResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ReversePhoneLookupResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ReversePhoneLookupResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ReversePhoneLookupResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ReversePhoneLookupResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ReversePhoneLookupResponse200
    | ReversePhoneLookupResponse400
    | ReversePhoneLookupResponse401
    | ReversePhoneLookupResponse402
    | ReversePhoneLookupResponse403
    | ReversePhoneLookupResponse404
    | ReversePhoneLookupResponse422
    | ReversePhoneLookupResponse429
    | ReversePhoneLookupResponse500
    | ReversePhoneLookupResponse503
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
    body: ReversePhoneLookupBody,
) -> Response[
    ReversePhoneLookupResponse200
    | ReversePhoneLookupResponse400
    | ReversePhoneLookupResponse401
    | ReversePhoneLookupResponse402
    | ReversePhoneLookupResponse403
    | ReversePhoneLookupResponse404
    | ReversePhoneLookupResponse422
    | ReversePhoneLookupResponse429
    | ReversePhoneLookupResponse500
    | ReversePhoneLookupResponse503
]:
    r"""Find person or company by phone (single)

     Given a phone number, find the associated LinkedIn profile or company.

    Mobile and home phones typically resolve to people, while front desk or business phones may resolve
    to companies.

    Only charges 1 credit when a result is found. No charge for invalid numbers or misses.

    If you have additional identifiers (name, company, email) beyond just the phone number, use the
    Kitchen Sink endpoint instead for better match quality.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per phone lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (ReversePhoneLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReversePhoneLookupResponse200 | ReversePhoneLookupResponse400 | ReversePhoneLookupResponse401 | ReversePhoneLookupResponse402 | ReversePhoneLookupResponse403 | ReversePhoneLookupResponse404 | ReversePhoneLookupResponse422 | ReversePhoneLookupResponse429 | ReversePhoneLookupResponse500 | ReversePhoneLookupResponse503]
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
    body: ReversePhoneLookupBody,
) -> (
    ReversePhoneLookupResponse200
    | ReversePhoneLookupResponse400
    | ReversePhoneLookupResponse401
    | ReversePhoneLookupResponse402
    | ReversePhoneLookupResponse403
    | ReversePhoneLookupResponse404
    | ReversePhoneLookupResponse422
    | ReversePhoneLookupResponse429
    | ReversePhoneLookupResponse500
    | ReversePhoneLookupResponse503
    | None
):
    r"""Find person or company by phone (single)

     Given a phone number, find the associated LinkedIn profile or company.

    Mobile and home phones typically resolve to people, while front desk or business phones may resolve
    to companies.

    Only charges 1 credit when a result is found. No charge for invalid numbers or misses.

    If you have additional identifiers (name, company, email) beyond just the phone number, use the
    Kitchen Sink endpoint instead for better match quality.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per phone lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (ReversePhoneLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReversePhoneLookupResponse200 | ReversePhoneLookupResponse400 | ReversePhoneLookupResponse401 | ReversePhoneLookupResponse402 | ReversePhoneLookupResponse403 | ReversePhoneLookupResponse404 | ReversePhoneLookupResponse422 | ReversePhoneLookupResponse429 | ReversePhoneLookupResponse500 | ReversePhoneLookupResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReversePhoneLookupBody,
) -> Response[
    ReversePhoneLookupResponse200
    | ReversePhoneLookupResponse400
    | ReversePhoneLookupResponse401
    | ReversePhoneLookupResponse402
    | ReversePhoneLookupResponse403
    | ReversePhoneLookupResponse404
    | ReversePhoneLookupResponse422
    | ReversePhoneLookupResponse429
    | ReversePhoneLookupResponse500
    | ReversePhoneLookupResponse503
]:
    r"""Find person or company by phone (single)

     Given a phone number, find the associated LinkedIn profile or company.

    Mobile and home phones typically resolve to people, while front desk or business phones may resolve
    to companies.

    Only charges 1 credit when a result is found. No charge for invalid numbers or misses.

    If you have additional identifiers (name, company, email) beyond just the phone number, use the
    Kitchen Sink endpoint instead for better match quality.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per phone lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (ReversePhoneLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReversePhoneLookupResponse200 | ReversePhoneLookupResponse400 | ReversePhoneLookupResponse401 | ReversePhoneLookupResponse402 | ReversePhoneLookupResponse403 | ReversePhoneLookupResponse404 | ReversePhoneLookupResponse422 | ReversePhoneLookupResponse429 | ReversePhoneLookupResponse500 | ReversePhoneLookupResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReversePhoneLookupBody,
) -> (
    ReversePhoneLookupResponse200
    | ReversePhoneLookupResponse400
    | ReversePhoneLookupResponse401
    | ReversePhoneLookupResponse402
    | ReversePhoneLookupResponse403
    | ReversePhoneLookupResponse404
    | ReversePhoneLookupResponse422
    | ReversePhoneLookupResponse429
    | ReversePhoneLookupResponse500
    | ReversePhoneLookupResponse503
    | None
):
    r"""Find person or company by phone (single)

     Given a phone number, find the associated LinkedIn profile or company.

    Mobile and home phones typically resolve to people, while front desk or business phones may resolve
    to companies.

    Only charges 1 credit when a result is found. No charge for invalid numbers or misses.

    If you have additional identifiers (name, company, email) beyond just the phone number, use the
    Kitchen Sink endpoint instead for better match quality.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per phone lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (ReversePhoneLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReversePhoneLookupResponse200 | ReversePhoneLookupResponse400 | ReversePhoneLookupResponse401 | ReversePhoneLookupResponse402 | ReversePhoneLookupResponse403 | ReversePhoneLookupResponse404 | ReversePhoneLookupResponse422 | ReversePhoneLookupResponse429 | ReversePhoneLookupResponse500 | ReversePhoneLookupResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
