from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.profile_last_activity_date_live_fetch_body import ProfileLastActivityDateLiveFetchBody
from ...models.profile_last_activity_date_live_fetch_response_200 import ProfileLastActivityDateLiveFetchResponse200
from ...models.profile_last_activity_date_live_fetch_response_400 import ProfileLastActivityDateLiveFetchResponse400
from ...models.profile_last_activity_date_live_fetch_response_401 import ProfileLastActivityDateLiveFetchResponse401
from ...models.profile_last_activity_date_live_fetch_response_402 import ProfileLastActivityDateLiveFetchResponse402
from ...models.profile_last_activity_date_live_fetch_response_403 import ProfileLastActivityDateLiveFetchResponse403
from ...models.profile_last_activity_date_live_fetch_response_404 import ProfileLastActivityDateLiveFetchResponse404
from ...models.profile_last_activity_date_live_fetch_response_429 import ProfileLastActivityDateLiveFetchResponse429
from ...models.profile_last_activity_date_live_fetch_response_500 import ProfileLastActivityDateLiveFetchResponse500
from ...models.profile_last_activity_date_live_fetch_response_503 import ProfileLastActivityDateLiveFetchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ProfileLastActivityDateLiveFetchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/profile-last-activity-date",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProfileLastActivityDateLiveFetchResponse200
    | ProfileLastActivityDateLiveFetchResponse400
    | ProfileLastActivityDateLiveFetchResponse401
    | ProfileLastActivityDateLiveFetchResponse402
    | ProfileLastActivityDateLiveFetchResponse403
    | ProfileLastActivityDateLiveFetchResponse404
    | ProfileLastActivityDateLiveFetchResponse429
    | ProfileLastActivityDateLiveFetchResponse500
    | ProfileLastActivityDateLiveFetchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ProfileLastActivityDateLiveFetchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProfileLastActivityDateLiveFetchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfileLastActivityDateLiveFetchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ProfileLastActivityDateLiveFetchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ProfileLastActivityDateLiveFetchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProfileLastActivityDateLiveFetchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ProfileLastActivityDateLiveFetchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ProfileLastActivityDateLiveFetchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ProfileLastActivityDateLiveFetchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProfileLastActivityDateLiveFetchResponse200
    | ProfileLastActivityDateLiveFetchResponse400
    | ProfileLastActivityDateLiveFetchResponse401
    | ProfileLastActivityDateLiveFetchResponse402
    | ProfileLastActivityDateLiveFetchResponse403
    | ProfileLastActivityDateLiveFetchResponse404
    | ProfileLastActivityDateLiveFetchResponse429
    | ProfileLastActivityDateLiveFetchResponse500
    | ProfileLastActivityDateLiveFetchResponse503
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
    body: ProfileLastActivityDateLiveFetchBody,
) -> Response[
    ProfileLastActivityDateLiveFetchResponse200
    | ProfileLastActivityDateLiveFetchResponse400
    | ProfileLastActivityDateLiveFetchResponse401
    | ProfileLastActivityDateLiveFetchResponse402
    | ProfileLastActivityDateLiveFetchResponse403
    | ProfileLastActivityDateLiveFetchResponse404
    | ProfileLastActivityDateLiveFetchResponse429
    | ProfileLastActivityDateLiveFetchResponse500
    | ProfileLastActivityDateLiveFetchResponse503
]:
    r"""Fetch last activity date for a LinkedIn profile

     Fetches the last date where the person made a publicly visible action on LinkedIn, such as a post,
    comment, reaction, or repost. This does not include logging in or other private actions.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (ProfileLastActivityDateLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileLastActivityDateLiveFetchResponse200 | ProfileLastActivityDateLiveFetchResponse400 | ProfileLastActivityDateLiveFetchResponse401 | ProfileLastActivityDateLiveFetchResponse402 | ProfileLastActivityDateLiveFetchResponse403 | ProfileLastActivityDateLiveFetchResponse404 | ProfileLastActivityDateLiveFetchResponse429 | ProfileLastActivityDateLiveFetchResponse500 | ProfileLastActivityDateLiveFetchResponse503]
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
    body: ProfileLastActivityDateLiveFetchBody,
) -> (
    ProfileLastActivityDateLiveFetchResponse200
    | ProfileLastActivityDateLiveFetchResponse400
    | ProfileLastActivityDateLiveFetchResponse401
    | ProfileLastActivityDateLiveFetchResponse402
    | ProfileLastActivityDateLiveFetchResponse403
    | ProfileLastActivityDateLiveFetchResponse404
    | ProfileLastActivityDateLiveFetchResponse429
    | ProfileLastActivityDateLiveFetchResponse500
    | ProfileLastActivityDateLiveFetchResponse503
    | None
):
    r"""Fetch last activity date for a LinkedIn profile

     Fetches the last date where the person made a publicly visible action on LinkedIn, such as a post,
    comment, reaction, or repost. This does not include logging in or other private actions.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (ProfileLastActivityDateLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileLastActivityDateLiveFetchResponse200 | ProfileLastActivityDateLiveFetchResponse400 | ProfileLastActivityDateLiveFetchResponse401 | ProfileLastActivityDateLiveFetchResponse402 | ProfileLastActivityDateLiveFetchResponse403 | ProfileLastActivityDateLiveFetchResponse404 | ProfileLastActivityDateLiveFetchResponse429 | ProfileLastActivityDateLiveFetchResponse500 | ProfileLastActivityDateLiveFetchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProfileLastActivityDateLiveFetchBody,
) -> Response[
    ProfileLastActivityDateLiveFetchResponse200
    | ProfileLastActivityDateLiveFetchResponse400
    | ProfileLastActivityDateLiveFetchResponse401
    | ProfileLastActivityDateLiveFetchResponse402
    | ProfileLastActivityDateLiveFetchResponse403
    | ProfileLastActivityDateLiveFetchResponse404
    | ProfileLastActivityDateLiveFetchResponse429
    | ProfileLastActivityDateLiveFetchResponse500
    | ProfileLastActivityDateLiveFetchResponse503
]:
    r"""Fetch last activity date for a LinkedIn profile

     Fetches the last date where the person made a publicly visible action on LinkedIn, such as a post,
    comment, reaction, or repost. This does not include logging in or other private actions.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (ProfileLastActivityDateLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileLastActivityDateLiveFetchResponse200 | ProfileLastActivityDateLiveFetchResponse400 | ProfileLastActivityDateLiveFetchResponse401 | ProfileLastActivityDateLiveFetchResponse402 | ProfileLastActivityDateLiveFetchResponse403 | ProfileLastActivityDateLiveFetchResponse404 | ProfileLastActivityDateLiveFetchResponse429 | ProfileLastActivityDateLiveFetchResponse500 | ProfileLastActivityDateLiveFetchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ProfileLastActivityDateLiveFetchBody,
) -> (
    ProfileLastActivityDateLiveFetchResponse200
    | ProfileLastActivityDateLiveFetchResponse400
    | ProfileLastActivityDateLiveFetchResponse401
    | ProfileLastActivityDateLiveFetchResponse402
    | ProfileLastActivityDateLiveFetchResponse403
    | ProfileLastActivityDateLiveFetchResponse404
    | ProfileLastActivityDateLiveFetchResponse429
    | ProfileLastActivityDateLiveFetchResponse500
    | ProfileLastActivityDateLiveFetchResponse503
    | None
):
    r"""Fetch last activity date for a LinkedIn profile

     Fetches the last date where the person made a publicly visible action on LinkedIn, such as a post,
    comment, reaction, or repost. This does not include logging in or other private actions.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (ProfileLastActivityDateLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileLastActivityDateLiveFetchResponse200 | ProfileLastActivityDateLiveFetchResponse400 | ProfileLastActivityDateLiveFetchResponse401 | ProfileLastActivityDateLiveFetchResponse402 | ProfileLastActivityDateLiveFetchResponse403 | ProfileLastActivityDateLiveFetchResponse404 | ProfileLastActivityDateLiveFetchResponse429 | ProfileLastActivityDateLiveFetchResponse500 | ProfileLastActivityDateLiveFetchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
