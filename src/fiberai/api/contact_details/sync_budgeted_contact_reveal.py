from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sync_budgeted_contact_reveal_body_type_0 import SyncBudgetedContactRevealBodyType0
from ...models.sync_budgeted_contact_reveal_body_type_1 import SyncBudgetedContactRevealBodyType1
from ...models.sync_budgeted_contact_reveal_body_type_2 import SyncBudgetedContactRevealBodyType2
from ...models.sync_budgeted_contact_reveal_response_200 import SyncBudgetedContactRevealResponse200
from ...models.sync_budgeted_contact_reveal_response_400 import SyncBudgetedContactRevealResponse400
from ...models.sync_budgeted_contact_reveal_response_401 import SyncBudgetedContactRevealResponse401
from ...models.sync_budgeted_contact_reveal_response_402 import SyncBudgetedContactRevealResponse402
from ...models.sync_budgeted_contact_reveal_response_403 import SyncBudgetedContactRevealResponse403
from ...models.sync_budgeted_contact_reveal_response_404 import SyncBudgetedContactRevealResponse404
from ...models.sync_budgeted_contact_reveal_response_422 import SyncBudgetedContactRevealResponse422
from ...models.sync_budgeted_contact_reveal_response_429 import SyncBudgetedContactRevealResponse429
from ...models.sync_budgeted_contact_reveal_response_500 import SyncBudgetedContactRevealResponse500
from ...models.sync_budgeted_contact_reveal_response_503 import SyncBudgetedContactRevealResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SyncBudgetedContactRevealBodyType0 | SyncBudgetedContactRevealBodyType1 | SyncBudgetedContactRevealBodyType2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/reveal",
    }

    if isinstance(body, SyncBudgetedContactRevealBodyType0):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, SyncBudgetedContactRevealBodyType1):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SyncBudgetedContactRevealResponse200
    | SyncBudgetedContactRevealResponse400
    | SyncBudgetedContactRevealResponse401
    | SyncBudgetedContactRevealResponse402
    | SyncBudgetedContactRevealResponse403
    | SyncBudgetedContactRevealResponse404
    | SyncBudgetedContactRevealResponse422
    | SyncBudgetedContactRevealResponse429
    | SyncBudgetedContactRevealResponse500
    | SyncBudgetedContactRevealResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SyncBudgetedContactRevealResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SyncBudgetedContactRevealResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SyncBudgetedContactRevealResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SyncBudgetedContactRevealResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SyncBudgetedContactRevealResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SyncBudgetedContactRevealResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = SyncBudgetedContactRevealResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = SyncBudgetedContactRevealResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SyncBudgetedContactRevealResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SyncBudgetedContactRevealResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SyncBudgetedContactRevealResponse200
    | SyncBudgetedContactRevealResponse400
    | SyncBudgetedContactRevealResponse401
    | SyncBudgetedContactRevealResponse402
    | SyncBudgetedContactRevealResponse403
    | SyncBudgetedContactRevealResponse404
    | SyncBudgetedContactRevealResponse422
    | SyncBudgetedContactRevealResponse429
    | SyncBudgetedContactRevealResponse500
    | SyncBudgetedContactRevealResponse503
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
    body: SyncBudgetedContactRevealBodyType0 | SyncBudgetedContactRevealBodyType1 | SyncBudgetedContactRevealBodyType2,
) -> Response[
    SyncBudgetedContactRevealResponse200
    | SyncBudgetedContactRevealResponse400
    | SyncBudgetedContactRevealResponse401
    | SyncBudgetedContactRevealResponse402
    | SyncBudgetedContactRevealResponse403
    | SyncBudgetedContactRevealResponse404
    | SyncBudgetedContactRevealResponse422
    | SyncBudgetedContactRevealResponse429
    | SyncBudgetedContactRevealResponse500
    | SyncBudgetedContactRevealResponse503
]:
    """Reveal contact details (time-budgeted)

     Return a person's work email, personal email, and/or phone number, guaranteed to finish within your
    specified time window. You can pick how deep in our 'waterfall' we go; higher depths increase yield
    but will cost more. This is a beta endpoint, but we recommend trying it over the other contact
    reveal endpoints.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Only delivered items are billed — nothing delivered means nothing
    charged. Prices by depth:<br />• instant — 1 credit(s) per email type, 1 if phone numbers are
    delivered.<br />• quick — 1 credit(s) per email type, 2 if phone numbers are delivered.<br />•
    medium — flat bundle: 5 credit(s) for emails + phone, 3 all emails, 2 work email only, 2 personal
    email only, 3 phone only, 5 work email + phone, 5 personal email + phone.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 90 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 90 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (SyncBudgetedContactRevealBodyType0 | SyncBudgetedContactRevealBodyType1 |
            SyncBudgetedContactRevealBodyType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncBudgetedContactRevealResponse200 | SyncBudgetedContactRevealResponse400 | SyncBudgetedContactRevealResponse401 | SyncBudgetedContactRevealResponse402 | SyncBudgetedContactRevealResponse403 | SyncBudgetedContactRevealResponse404 | SyncBudgetedContactRevealResponse422 | SyncBudgetedContactRevealResponse429 | SyncBudgetedContactRevealResponse500 | SyncBudgetedContactRevealResponse503]
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
    body: SyncBudgetedContactRevealBodyType0 | SyncBudgetedContactRevealBodyType1 | SyncBudgetedContactRevealBodyType2,
) -> (
    SyncBudgetedContactRevealResponse200
    | SyncBudgetedContactRevealResponse400
    | SyncBudgetedContactRevealResponse401
    | SyncBudgetedContactRevealResponse402
    | SyncBudgetedContactRevealResponse403
    | SyncBudgetedContactRevealResponse404
    | SyncBudgetedContactRevealResponse422
    | SyncBudgetedContactRevealResponse429
    | SyncBudgetedContactRevealResponse500
    | SyncBudgetedContactRevealResponse503
    | None
):
    """Reveal contact details (time-budgeted)

     Return a person's work email, personal email, and/or phone number, guaranteed to finish within your
    specified time window. You can pick how deep in our 'waterfall' we go; higher depths increase yield
    but will cost more. This is a beta endpoint, but we recommend trying it over the other contact
    reveal endpoints.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Only delivered items are billed — nothing delivered means nothing
    charged. Prices by depth:<br />• instant — 1 credit(s) per email type, 1 if phone numbers are
    delivered.<br />• quick — 1 credit(s) per email type, 2 if phone numbers are delivered.<br />•
    medium — flat bundle: 5 credit(s) for emails + phone, 3 all emails, 2 work email only, 2 personal
    email only, 3 phone only, 5 work email + phone, 5 personal email + phone.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 90 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 90 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (SyncBudgetedContactRevealBodyType0 | SyncBudgetedContactRevealBodyType1 |
            SyncBudgetedContactRevealBodyType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncBudgetedContactRevealResponse200 | SyncBudgetedContactRevealResponse400 | SyncBudgetedContactRevealResponse401 | SyncBudgetedContactRevealResponse402 | SyncBudgetedContactRevealResponse403 | SyncBudgetedContactRevealResponse404 | SyncBudgetedContactRevealResponse422 | SyncBudgetedContactRevealResponse429 | SyncBudgetedContactRevealResponse500 | SyncBudgetedContactRevealResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncBudgetedContactRevealBodyType0 | SyncBudgetedContactRevealBodyType1 | SyncBudgetedContactRevealBodyType2,
) -> Response[
    SyncBudgetedContactRevealResponse200
    | SyncBudgetedContactRevealResponse400
    | SyncBudgetedContactRevealResponse401
    | SyncBudgetedContactRevealResponse402
    | SyncBudgetedContactRevealResponse403
    | SyncBudgetedContactRevealResponse404
    | SyncBudgetedContactRevealResponse422
    | SyncBudgetedContactRevealResponse429
    | SyncBudgetedContactRevealResponse500
    | SyncBudgetedContactRevealResponse503
]:
    """Reveal contact details (time-budgeted)

     Return a person's work email, personal email, and/or phone number, guaranteed to finish within your
    specified time window. You can pick how deep in our 'waterfall' we go; higher depths increase yield
    but will cost more. This is a beta endpoint, but we recommend trying it over the other contact
    reveal endpoints.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Only delivered items are billed — nothing delivered means nothing
    charged. Prices by depth:<br />• instant — 1 credit(s) per email type, 1 if phone numbers are
    delivered.<br />• quick — 1 credit(s) per email type, 2 if phone numbers are delivered.<br />•
    medium — flat bundle: 5 credit(s) for emails + phone, 3 all emails, 2 work email only, 2 personal
    email only, 3 phone only, 5 work email + phone, 5 personal email + phone.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 90 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 90 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (SyncBudgetedContactRevealBodyType0 | SyncBudgetedContactRevealBodyType1 |
            SyncBudgetedContactRevealBodyType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SyncBudgetedContactRevealResponse200 | SyncBudgetedContactRevealResponse400 | SyncBudgetedContactRevealResponse401 | SyncBudgetedContactRevealResponse402 | SyncBudgetedContactRevealResponse403 | SyncBudgetedContactRevealResponse404 | SyncBudgetedContactRevealResponse422 | SyncBudgetedContactRevealResponse429 | SyncBudgetedContactRevealResponse500 | SyncBudgetedContactRevealResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SyncBudgetedContactRevealBodyType0 | SyncBudgetedContactRevealBodyType1 | SyncBudgetedContactRevealBodyType2,
) -> (
    SyncBudgetedContactRevealResponse200
    | SyncBudgetedContactRevealResponse400
    | SyncBudgetedContactRevealResponse401
    | SyncBudgetedContactRevealResponse402
    | SyncBudgetedContactRevealResponse403
    | SyncBudgetedContactRevealResponse404
    | SyncBudgetedContactRevealResponse422
    | SyncBudgetedContactRevealResponse429
    | SyncBudgetedContactRevealResponse500
    | SyncBudgetedContactRevealResponse503
    | None
):
    """Reveal contact details (time-budgeted)

     Return a person's work email, personal email, and/or phone number, guaranteed to finish within your
    specified time window. You can pick how deep in our 'waterfall' we go; higher depths increase yield
    but will cost more. This is a beta endpoint, but we recommend trying it over the other contact
    reveal endpoints.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Only delivered items are billed — nothing delivered means nothing
    charged. Prices by depth:<br />• instant — 1 credit(s) per email type, 1 if phone numbers are
    delivered.<br />• quick — 1 credit(s) per email type, 2 if phone numbers are delivered.<br />•
    medium — flat bundle: 5 credit(s) for emails + phone, 3 all emails, 2 work email only, 2 personal
    email only, 3 phone only, 5 work email + phone, 5 personal email + phone.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 90 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 90 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (SyncBudgetedContactRevealBodyType0 | SyncBudgetedContactRevealBodyType1 |
            SyncBudgetedContactRevealBodyType2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SyncBudgetedContactRevealResponse200 | SyncBudgetedContactRevealResponse400 | SyncBudgetedContactRevealResponse401 | SyncBudgetedContactRevealResponse402 | SyncBudgetedContactRevealResponse403 | SyncBudgetedContactRevealResponse404 | SyncBudgetedContactRevealResponse422 | SyncBudgetedContactRevealResponse429 | SyncBudgetedContactRevealResponse500 | SyncBudgetedContactRevealResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
