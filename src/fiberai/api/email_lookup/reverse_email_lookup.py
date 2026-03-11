from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reverse_email_lookup_body import ReverseEmailLookupBody
from ...models.reverse_email_lookup_response_200 import ReverseEmailLookupResponse200
from ...models.reverse_email_lookup_response_400 import ReverseEmailLookupResponse400
from ...models.reverse_email_lookup_response_401 import ReverseEmailLookupResponse401
from ...models.reverse_email_lookup_response_402 import ReverseEmailLookupResponse402
from ...models.reverse_email_lookup_response_403 import ReverseEmailLookupResponse403
from ...models.reverse_email_lookup_response_404 import ReverseEmailLookupResponse404
from ...models.reverse_email_lookup_response_429 import ReverseEmailLookupResponse429
from ...models.reverse_email_lookup_response_500 import ReverseEmailLookupResponse500
from ...models.reverse_email_lookup_response_503 import ReverseEmailLookupResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ReverseEmailLookupBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/email-to-person/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ReverseEmailLookupResponse200
    | ReverseEmailLookupResponse400
    | ReverseEmailLookupResponse401
    | ReverseEmailLookupResponse402
    | ReverseEmailLookupResponse403
    | ReverseEmailLookupResponse404
    | ReverseEmailLookupResponse429
    | ReverseEmailLookupResponse500
    | ReverseEmailLookupResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ReverseEmailLookupResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ReverseEmailLookupResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ReverseEmailLookupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ReverseEmailLookupResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ReverseEmailLookupResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ReverseEmailLookupResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ReverseEmailLookupResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ReverseEmailLookupResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ReverseEmailLookupResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ReverseEmailLookupResponse200
    | ReverseEmailLookupResponse400
    | ReverseEmailLookupResponse401
    | ReverseEmailLookupResponse402
    | ReverseEmailLookupResponse403
    | ReverseEmailLookupResponse404
    | ReverseEmailLookupResponse429
    | ReverseEmailLookupResponse500
    | ReverseEmailLookupResponse503
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
    body: ReverseEmailLookupBody,
) -> Response[
    ReverseEmailLookupResponse200
    | ReverseEmailLookupResponse400
    | ReverseEmailLookupResponse401
    | ReverseEmailLookupResponse402
    | ReverseEmailLookupResponse403
    | ReverseEmailLookupResponse404
    | ReverseEmailLookupResponse429
    | ReverseEmailLookupResponse500
    | ReverseEmailLookupResponse503
]:
    r"""Find person by email (single)

     Given an email address, find the person's LinkedIn profile and personal details.
    If you also have the person's name, company, or other identifiers, use the Kitchen Sink endpoint
    instead — it accepts all available signals and produces better matches.
    **Rate limit**: 50 requests per second. To avoid 429 errors, space requests evenly (~20ms apart)
    rather than bursting them all at once. Bursting can trigger the fixed-window rate limiter even below
    the stated limit.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 second</span>

    <span>💰 <strong>Cost:</strong> 2 credits per email lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ReverseEmailLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReverseEmailLookupResponse200 | ReverseEmailLookupResponse400 | ReverseEmailLookupResponse401 | ReverseEmailLookupResponse402 | ReverseEmailLookupResponse403 | ReverseEmailLookupResponse404 | ReverseEmailLookupResponse429 | ReverseEmailLookupResponse500 | ReverseEmailLookupResponse503]
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
    body: ReverseEmailLookupBody,
) -> (
    ReverseEmailLookupResponse200
    | ReverseEmailLookupResponse400
    | ReverseEmailLookupResponse401
    | ReverseEmailLookupResponse402
    | ReverseEmailLookupResponse403
    | ReverseEmailLookupResponse404
    | ReverseEmailLookupResponse429
    | ReverseEmailLookupResponse500
    | ReverseEmailLookupResponse503
    | None
):
    r"""Find person by email (single)

     Given an email address, find the person's LinkedIn profile and personal details.
    If you also have the person's name, company, or other identifiers, use the Kitchen Sink endpoint
    instead — it accepts all available signals and produces better matches.
    **Rate limit**: 50 requests per second. To avoid 429 errors, space requests evenly (~20ms apart)
    rather than bursting them all at once. Bursting can trigger the fixed-window rate limiter even below
    the stated limit.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 second</span>

    <span>💰 <strong>Cost:</strong> 2 credits per email lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ReverseEmailLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReverseEmailLookupResponse200 | ReverseEmailLookupResponse400 | ReverseEmailLookupResponse401 | ReverseEmailLookupResponse402 | ReverseEmailLookupResponse403 | ReverseEmailLookupResponse404 | ReverseEmailLookupResponse429 | ReverseEmailLookupResponse500 | ReverseEmailLookupResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReverseEmailLookupBody,
) -> Response[
    ReverseEmailLookupResponse200
    | ReverseEmailLookupResponse400
    | ReverseEmailLookupResponse401
    | ReverseEmailLookupResponse402
    | ReverseEmailLookupResponse403
    | ReverseEmailLookupResponse404
    | ReverseEmailLookupResponse429
    | ReverseEmailLookupResponse500
    | ReverseEmailLookupResponse503
]:
    r"""Find person by email (single)

     Given an email address, find the person's LinkedIn profile and personal details.
    If you also have the person's name, company, or other identifiers, use the Kitchen Sink endpoint
    instead — it accepts all available signals and produces better matches.
    **Rate limit**: 50 requests per second. To avoid 429 errors, space requests evenly (~20ms apart)
    rather than bursting them all at once. Bursting can trigger the fixed-window rate limiter even below
    the stated limit.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 second</span>

    <span>💰 <strong>Cost:</strong> 2 credits per email lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ReverseEmailLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReverseEmailLookupResponse200 | ReverseEmailLookupResponse400 | ReverseEmailLookupResponse401 | ReverseEmailLookupResponse402 | ReverseEmailLookupResponse403 | ReverseEmailLookupResponse404 | ReverseEmailLookupResponse429 | ReverseEmailLookupResponse500 | ReverseEmailLookupResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReverseEmailLookupBody,
) -> (
    ReverseEmailLookupResponse200
    | ReverseEmailLookupResponse400
    | ReverseEmailLookupResponse401
    | ReverseEmailLookupResponse402
    | ReverseEmailLookupResponse403
    | ReverseEmailLookupResponse404
    | ReverseEmailLookupResponse429
    | ReverseEmailLookupResponse500
    | ReverseEmailLookupResponse503
    | None
):
    r"""Find person by email (single)

     Given an email address, find the person's LinkedIn profile and personal details.
    If you also have the person's name, company, or other identifiers, use the Kitchen Sink endpoint
    instead — it accepts all available signals and produces better matches.
    **Rate limit**: 50 requests per second. To avoid 429 errors, space requests evenly (~20ms apart)
    rather than bursting them all at once. Bursting can trigger the fixed-window rate limiter even below
    the stated limit.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 second</span>

    <span>💰 <strong>Cost:</strong> 2 credits per email lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ReverseEmailLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReverseEmailLookupResponse200 | ReverseEmailLookupResponse400 | ReverseEmailLookupResponse401 | ReverseEmailLookupResponse402 | ReverseEmailLookupResponse403 | ReverseEmailLookupResponse404 | ReverseEmailLookupResponse429 | ReverseEmailLookupResponse500 | ReverseEmailLookupResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
