from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.profile_latest_activities_live_fetch_body import ProfileLatestActivitiesLiveFetchBody
from ...models.profile_latest_activities_live_fetch_response_200 import ProfileLatestActivitiesLiveFetchResponse200
from ...models.profile_latest_activities_live_fetch_response_400 import ProfileLatestActivitiesLiveFetchResponse400
from ...models.profile_latest_activities_live_fetch_response_401 import ProfileLatestActivitiesLiveFetchResponse401
from ...models.profile_latest_activities_live_fetch_response_402 import ProfileLatestActivitiesLiveFetchResponse402
from ...models.profile_latest_activities_live_fetch_response_403 import ProfileLatestActivitiesLiveFetchResponse403
from ...models.profile_latest_activities_live_fetch_response_404 import ProfileLatestActivitiesLiveFetchResponse404
from ...models.profile_latest_activities_live_fetch_response_429 import ProfileLatestActivitiesLiveFetchResponse429
from ...models.profile_latest_activities_live_fetch_response_500 import ProfileLatestActivitiesLiveFetchResponse500
from ...models.profile_latest_activities_live_fetch_response_503 import ProfileLatestActivitiesLiveFetchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ProfileLatestActivitiesLiveFetchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/profile-latest-activities",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProfileLatestActivitiesLiveFetchResponse200
    | ProfileLatestActivitiesLiveFetchResponse400
    | ProfileLatestActivitiesLiveFetchResponse401
    | ProfileLatestActivitiesLiveFetchResponse402
    | ProfileLatestActivitiesLiveFetchResponse403
    | ProfileLatestActivitiesLiveFetchResponse404
    | ProfileLatestActivitiesLiveFetchResponse429
    | ProfileLatestActivitiesLiveFetchResponse500
    | ProfileLatestActivitiesLiveFetchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ProfileLatestActivitiesLiveFetchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProfileLatestActivitiesLiveFetchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfileLatestActivitiesLiveFetchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ProfileLatestActivitiesLiveFetchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ProfileLatestActivitiesLiveFetchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProfileLatestActivitiesLiveFetchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ProfileLatestActivitiesLiveFetchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ProfileLatestActivitiesLiveFetchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ProfileLatestActivitiesLiveFetchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProfileLatestActivitiesLiveFetchResponse200
    | ProfileLatestActivitiesLiveFetchResponse400
    | ProfileLatestActivitiesLiveFetchResponse401
    | ProfileLatestActivitiesLiveFetchResponse402
    | ProfileLatestActivitiesLiveFetchResponse403
    | ProfileLatestActivitiesLiveFetchResponse404
    | ProfileLatestActivitiesLiveFetchResponse429
    | ProfileLatestActivitiesLiveFetchResponse500
    | ProfileLatestActivitiesLiveFetchResponse503
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
    body: ProfileLatestActivitiesLiveFetchBody,
) -> Response[
    ProfileLatestActivitiesLiveFetchResponse200
    | ProfileLatestActivitiesLiveFetchResponse400
    | ProfileLatestActivitiesLiveFetchResponse401
    | ProfileLatestActivitiesLiveFetchResponse402
    | ProfileLatestActivitiesLiveFetchResponse403
    | ProfileLatestActivitiesLiveFetchResponse404
    | ProfileLatestActivitiesLiveFetchResponse429
    | ProfileLatestActivitiesLiveFetchResponse500
    | ProfileLatestActivitiesLiveFetchResponse503
]:
    r"""Fetch latest LinkedIn activities for a profile

     Fetches up to 30 of a person's most recent LinkedIn activities (posts, comments, reactions, shares,
    and reposts) in newest-first order. If you only need to know when a person was last active, use the
    lighter profile-last-activity-date endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (ProfileLatestActivitiesLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileLatestActivitiesLiveFetchResponse200 | ProfileLatestActivitiesLiveFetchResponse400 | ProfileLatestActivitiesLiveFetchResponse401 | ProfileLatestActivitiesLiveFetchResponse402 | ProfileLatestActivitiesLiveFetchResponse403 | ProfileLatestActivitiesLiveFetchResponse404 | ProfileLatestActivitiesLiveFetchResponse429 | ProfileLatestActivitiesLiveFetchResponse500 | ProfileLatestActivitiesLiveFetchResponse503]
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
    body: ProfileLatestActivitiesLiveFetchBody,
) -> (
    ProfileLatestActivitiesLiveFetchResponse200
    | ProfileLatestActivitiesLiveFetchResponse400
    | ProfileLatestActivitiesLiveFetchResponse401
    | ProfileLatestActivitiesLiveFetchResponse402
    | ProfileLatestActivitiesLiveFetchResponse403
    | ProfileLatestActivitiesLiveFetchResponse404
    | ProfileLatestActivitiesLiveFetchResponse429
    | ProfileLatestActivitiesLiveFetchResponse500
    | ProfileLatestActivitiesLiveFetchResponse503
    | None
):
    r"""Fetch latest LinkedIn activities for a profile

     Fetches up to 30 of a person's most recent LinkedIn activities (posts, comments, reactions, shares,
    and reposts) in newest-first order. If you only need to know when a person was last active, use the
    lighter profile-last-activity-date endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (ProfileLatestActivitiesLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileLatestActivitiesLiveFetchResponse200 | ProfileLatestActivitiesLiveFetchResponse400 | ProfileLatestActivitiesLiveFetchResponse401 | ProfileLatestActivitiesLiveFetchResponse402 | ProfileLatestActivitiesLiveFetchResponse403 | ProfileLatestActivitiesLiveFetchResponse404 | ProfileLatestActivitiesLiveFetchResponse429 | ProfileLatestActivitiesLiveFetchResponse500 | ProfileLatestActivitiesLiveFetchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProfileLatestActivitiesLiveFetchBody,
) -> Response[
    ProfileLatestActivitiesLiveFetchResponse200
    | ProfileLatestActivitiesLiveFetchResponse400
    | ProfileLatestActivitiesLiveFetchResponse401
    | ProfileLatestActivitiesLiveFetchResponse402
    | ProfileLatestActivitiesLiveFetchResponse403
    | ProfileLatestActivitiesLiveFetchResponse404
    | ProfileLatestActivitiesLiveFetchResponse429
    | ProfileLatestActivitiesLiveFetchResponse500
    | ProfileLatestActivitiesLiveFetchResponse503
]:
    r"""Fetch latest LinkedIn activities for a profile

     Fetches up to 30 of a person's most recent LinkedIn activities (posts, comments, reactions, shares,
    and reposts) in newest-first order. If you only need to know when a person was last active, use the
    lighter profile-last-activity-date endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (ProfileLatestActivitiesLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileLatestActivitiesLiveFetchResponse200 | ProfileLatestActivitiesLiveFetchResponse400 | ProfileLatestActivitiesLiveFetchResponse401 | ProfileLatestActivitiesLiveFetchResponse402 | ProfileLatestActivitiesLiveFetchResponse403 | ProfileLatestActivitiesLiveFetchResponse404 | ProfileLatestActivitiesLiveFetchResponse429 | ProfileLatestActivitiesLiveFetchResponse500 | ProfileLatestActivitiesLiveFetchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ProfileLatestActivitiesLiveFetchBody,
) -> (
    ProfileLatestActivitiesLiveFetchResponse200
    | ProfileLatestActivitiesLiveFetchResponse400
    | ProfileLatestActivitiesLiveFetchResponse401
    | ProfileLatestActivitiesLiveFetchResponse402
    | ProfileLatestActivitiesLiveFetchResponse403
    | ProfileLatestActivitiesLiveFetchResponse404
    | ProfileLatestActivitiesLiveFetchResponse429
    | ProfileLatestActivitiesLiveFetchResponse500
    | ProfileLatestActivitiesLiveFetchResponse503
    | None
):
    r"""Fetch latest LinkedIn activities for a profile

     Fetches up to 30 of a person's most recent LinkedIn activities (posts, comments, reactions, shares,
    and reposts) in newest-first order. If you only need to know when a person was last active, use the
    lighter profile-last-activity-date endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (ProfileLatestActivitiesLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileLatestActivitiesLiveFetchResponse200 | ProfileLatestActivitiesLiveFetchResponse400 | ProfileLatestActivitiesLiveFetchResponse401 | ProfileLatestActivitiesLiveFetchResponse402 | ProfileLatestActivitiesLiveFetchResponse403 | ProfileLatestActivitiesLiveFetchResponse404 | ProfileLatestActivitiesLiveFetchResponse429 | ProfileLatestActivitiesLiveFetchResponse500 | ProfileLatestActivitiesLiveFetchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
