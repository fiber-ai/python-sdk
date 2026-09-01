from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instant_contact_reveal_body import InstantContactRevealBody
from ...models.instant_contact_reveal_response_200 import InstantContactRevealResponse200
from ...models.instant_contact_reveal_response_400 import InstantContactRevealResponse400
from ...models.instant_contact_reveal_response_401 import InstantContactRevealResponse401
from ...models.instant_contact_reveal_response_402 import InstantContactRevealResponse402
from ...models.instant_contact_reveal_response_403 import InstantContactRevealResponse403
from ...models.instant_contact_reveal_response_404 import InstantContactRevealResponse404
from ...models.instant_contact_reveal_response_422 import InstantContactRevealResponse422
from ...models.instant_contact_reveal_response_429 import InstantContactRevealResponse429
from ...models.instant_contact_reveal_response_500 import InstantContactRevealResponse500
from ...models.instant_contact_reveal_response_503 import InstantContactRevealResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: InstantContactRevealBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/instant",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InstantContactRevealResponse200
    | InstantContactRevealResponse400
    | InstantContactRevealResponse401
    | InstantContactRevealResponse402
    | InstantContactRevealResponse403
    | InstantContactRevealResponse404
    | InstantContactRevealResponse422
    | InstantContactRevealResponse429
    | InstantContactRevealResponse500
    | InstantContactRevealResponse503
    | None
):
    if response.status_code == 200:
        response_200 = InstantContactRevealResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InstantContactRevealResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InstantContactRevealResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = InstantContactRevealResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = InstantContactRevealResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InstantContactRevealResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = InstantContactRevealResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = InstantContactRevealResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InstantContactRevealResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = InstantContactRevealResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InstantContactRevealResponse200
    | InstantContactRevealResponse400
    | InstantContactRevealResponse401
    | InstantContactRevealResponse402
    | InstantContactRevealResponse403
    | InstantContactRevealResponse404
    | InstantContactRevealResponse422
    | InstantContactRevealResponse429
    | InstantContactRevealResponse500
    | InstantContactRevealResponse503
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
    body: InstantContactRevealBody,
) -> Response[
    InstantContactRevealResponse200
    | InstantContactRevealResponse400
    | InstantContactRevealResponse401
    | InstantContactRevealResponse402
    | InstantContactRevealResponse403
    | InstantContactRevealResponse404
    | InstantContactRevealResponse422
    | InstantContactRevealResponse429
    | InstantContactRevealResponse500
    | InstantContactRevealResponse503
]:
    """Reveal contact details (instant)

     Fast contact lookup that returns emails and phone numbers already on file for the person. Does not
    perform additional discovery or re-verify addresses at request time, so yield is lower than other
    contact-reveal endpoints and validationStatus may be unknown. Accepts a LinkedIn profile identifier
    or a name plus company domain.

    <span>⚡ <strong>Rate limit:</strong> 500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per instant email reveal + 1 credit per instant phone
    reveal&nbsp;<span title="Pricing shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 15 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 15 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (InstantContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstantContactRevealResponse200 | InstantContactRevealResponse400 | InstantContactRevealResponse401 | InstantContactRevealResponse402 | InstantContactRevealResponse403 | InstantContactRevealResponse404 | InstantContactRevealResponse422 | InstantContactRevealResponse429 | InstantContactRevealResponse500 | InstantContactRevealResponse503]
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
    body: InstantContactRevealBody,
) -> (
    InstantContactRevealResponse200
    | InstantContactRevealResponse400
    | InstantContactRevealResponse401
    | InstantContactRevealResponse402
    | InstantContactRevealResponse403
    | InstantContactRevealResponse404
    | InstantContactRevealResponse422
    | InstantContactRevealResponse429
    | InstantContactRevealResponse500
    | InstantContactRevealResponse503
    | None
):
    """Reveal contact details (instant)

     Fast contact lookup that returns emails and phone numbers already on file for the person. Does not
    perform additional discovery or re-verify addresses at request time, so yield is lower than other
    contact-reveal endpoints and validationStatus may be unknown. Accepts a LinkedIn profile identifier
    or a name plus company domain.

    <span>⚡ <strong>Rate limit:</strong> 500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per instant email reveal + 1 credit per instant phone
    reveal&nbsp;<span title="Pricing shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 15 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 15 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (InstantContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstantContactRevealResponse200 | InstantContactRevealResponse400 | InstantContactRevealResponse401 | InstantContactRevealResponse402 | InstantContactRevealResponse403 | InstantContactRevealResponse404 | InstantContactRevealResponse422 | InstantContactRevealResponse429 | InstantContactRevealResponse500 | InstantContactRevealResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InstantContactRevealBody,
) -> Response[
    InstantContactRevealResponse200
    | InstantContactRevealResponse400
    | InstantContactRevealResponse401
    | InstantContactRevealResponse402
    | InstantContactRevealResponse403
    | InstantContactRevealResponse404
    | InstantContactRevealResponse422
    | InstantContactRevealResponse429
    | InstantContactRevealResponse500
    | InstantContactRevealResponse503
]:
    """Reveal contact details (instant)

     Fast contact lookup that returns emails and phone numbers already on file for the person. Does not
    perform additional discovery or re-verify addresses at request time, so yield is lower than other
    contact-reveal endpoints and validationStatus may be unknown. Accepts a LinkedIn profile identifier
    or a name plus company domain.

    <span>⚡ <strong>Rate limit:</strong> 500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per instant email reveal + 1 credit per instant phone
    reveal&nbsp;<span title="Pricing shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 15 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 15 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (InstantContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstantContactRevealResponse200 | InstantContactRevealResponse400 | InstantContactRevealResponse401 | InstantContactRevealResponse402 | InstantContactRevealResponse403 | InstantContactRevealResponse404 | InstantContactRevealResponse422 | InstantContactRevealResponse429 | InstantContactRevealResponse500 | InstantContactRevealResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InstantContactRevealBody,
) -> (
    InstantContactRevealResponse200
    | InstantContactRevealResponse400
    | InstantContactRevealResponse401
    | InstantContactRevealResponse402
    | InstantContactRevealResponse403
    | InstantContactRevealResponse404
    | InstantContactRevealResponse422
    | InstantContactRevealResponse429
    | InstantContactRevealResponse500
    | InstantContactRevealResponse503
    | None
):
    """Reveal contact details (instant)

     Fast contact lookup that returns emails and phone numbers already on file for the person. Does not
    perform additional discovery or re-verify addresses at request time, so yield is lower than other
    contact-reveal endpoints and validationStatus may be unknown. Accepts a LinkedIn profile identifier
    or a name plus company domain.

    <span>⚡ <strong>Rate limit:</strong> 500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per instant email reveal + 1 credit per instant phone
    reveal&nbsp;<span title="Pricing shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 15 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 15 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (InstantContactRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstantContactRevealResponse200 | InstantContactRevealResponse400 | InstantContactRevealResponse401 | InstantContactRevealResponse402 | InstantContactRevealResponse403 | InstantContactRevealResponse404 | InstantContactRevealResponse422 | InstantContactRevealResponse429 | InstantContactRevealResponse500 | InstantContactRevealResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
