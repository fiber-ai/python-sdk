from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.profile_comments_live_fetch_body import ProfileCommentsLiveFetchBody
from ...models.profile_comments_live_fetch_response_200 import ProfileCommentsLiveFetchResponse200
from ...models.profile_comments_live_fetch_response_400 import ProfileCommentsLiveFetchResponse400
from ...models.profile_comments_live_fetch_response_401 import ProfileCommentsLiveFetchResponse401
from ...models.profile_comments_live_fetch_response_402 import ProfileCommentsLiveFetchResponse402
from ...models.profile_comments_live_fetch_response_403 import ProfileCommentsLiveFetchResponse403
from ...models.profile_comments_live_fetch_response_404 import ProfileCommentsLiveFetchResponse404
from ...models.profile_comments_live_fetch_response_429 import ProfileCommentsLiveFetchResponse429
from ...models.profile_comments_live_fetch_response_500 import ProfileCommentsLiveFetchResponse500
from ...models.profile_comments_live_fetch_response_503 import ProfileCommentsLiveFetchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ProfileCommentsLiveFetchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/profile-comments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProfileCommentsLiveFetchResponse200
    | ProfileCommentsLiveFetchResponse400
    | ProfileCommentsLiveFetchResponse401
    | ProfileCommentsLiveFetchResponse402
    | ProfileCommentsLiveFetchResponse403
    | ProfileCommentsLiveFetchResponse404
    | ProfileCommentsLiveFetchResponse429
    | ProfileCommentsLiveFetchResponse500
    | ProfileCommentsLiveFetchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ProfileCommentsLiveFetchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProfileCommentsLiveFetchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfileCommentsLiveFetchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ProfileCommentsLiveFetchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ProfileCommentsLiveFetchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProfileCommentsLiveFetchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ProfileCommentsLiveFetchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ProfileCommentsLiveFetchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ProfileCommentsLiveFetchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProfileCommentsLiveFetchResponse200
    | ProfileCommentsLiveFetchResponse400
    | ProfileCommentsLiveFetchResponse401
    | ProfileCommentsLiveFetchResponse402
    | ProfileCommentsLiveFetchResponse403
    | ProfileCommentsLiveFetchResponse404
    | ProfileCommentsLiveFetchResponse429
    | ProfileCommentsLiveFetchResponse500
    | ProfileCommentsLiveFetchResponse503
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
    body: ProfileCommentsLiveFetchBody,
) -> Response[
    ProfileCommentsLiveFetchResponse200
    | ProfileCommentsLiveFetchResponse400
    | ProfileCommentsLiveFetchResponse401
    | ProfileCommentsLiveFetchResponse402
    | ProfileCommentsLiveFetchResponse403
    | ProfileCommentsLiveFetchResponse404
    | ProfileCommentsLiveFetchResponse429
    | ProfileCommentsLiveFetchResponse500
    | ProfileCommentsLiveFetchResponse503
]:
    r"""Fetch LinkedIn profile comments

     Fetches comments made by a LinkedIn profile. Returns a paginated feed of comments with optional
    cursor for pagination. Each page returns up to 10 comments.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileCommentsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileCommentsLiveFetchResponse200 | ProfileCommentsLiveFetchResponse400 | ProfileCommentsLiveFetchResponse401 | ProfileCommentsLiveFetchResponse402 | ProfileCommentsLiveFetchResponse403 | ProfileCommentsLiveFetchResponse404 | ProfileCommentsLiveFetchResponse429 | ProfileCommentsLiveFetchResponse500 | ProfileCommentsLiveFetchResponse503]
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
    body: ProfileCommentsLiveFetchBody,
) -> (
    ProfileCommentsLiveFetchResponse200
    | ProfileCommentsLiveFetchResponse400
    | ProfileCommentsLiveFetchResponse401
    | ProfileCommentsLiveFetchResponse402
    | ProfileCommentsLiveFetchResponse403
    | ProfileCommentsLiveFetchResponse404
    | ProfileCommentsLiveFetchResponse429
    | ProfileCommentsLiveFetchResponse500
    | ProfileCommentsLiveFetchResponse503
    | None
):
    r"""Fetch LinkedIn profile comments

     Fetches comments made by a LinkedIn profile. Returns a paginated feed of comments with optional
    cursor for pagination. Each page returns up to 10 comments.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileCommentsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileCommentsLiveFetchResponse200 | ProfileCommentsLiveFetchResponse400 | ProfileCommentsLiveFetchResponse401 | ProfileCommentsLiveFetchResponse402 | ProfileCommentsLiveFetchResponse403 | ProfileCommentsLiveFetchResponse404 | ProfileCommentsLiveFetchResponse429 | ProfileCommentsLiveFetchResponse500 | ProfileCommentsLiveFetchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProfileCommentsLiveFetchBody,
) -> Response[
    ProfileCommentsLiveFetchResponse200
    | ProfileCommentsLiveFetchResponse400
    | ProfileCommentsLiveFetchResponse401
    | ProfileCommentsLiveFetchResponse402
    | ProfileCommentsLiveFetchResponse403
    | ProfileCommentsLiveFetchResponse404
    | ProfileCommentsLiveFetchResponse429
    | ProfileCommentsLiveFetchResponse500
    | ProfileCommentsLiveFetchResponse503
]:
    r"""Fetch LinkedIn profile comments

     Fetches comments made by a LinkedIn profile. Returns a paginated feed of comments with optional
    cursor for pagination. Each page returns up to 10 comments.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileCommentsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileCommentsLiveFetchResponse200 | ProfileCommentsLiveFetchResponse400 | ProfileCommentsLiveFetchResponse401 | ProfileCommentsLiveFetchResponse402 | ProfileCommentsLiveFetchResponse403 | ProfileCommentsLiveFetchResponse404 | ProfileCommentsLiveFetchResponse429 | ProfileCommentsLiveFetchResponse500 | ProfileCommentsLiveFetchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ProfileCommentsLiveFetchBody,
) -> (
    ProfileCommentsLiveFetchResponse200
    | ProfileCommentsLiveFetchResponse400
    | ProfileCommentsLiveFetchResponse401
    | ProfileCommentsLiveFetchResponse402
    | ProfileCommentsLiveFetchResponse403
    | ProfileCommentsLiveFetchResponse404
    | ProfileCommentsLiveFetchResponse429
    | ProfileCommentsLiveFetchResponse500
    | ProfileCommentsLiveFetchResponse503
    | None
):
    r"""Fetch LinkedIn profile comments

     Fetches comments made by a LinkedIn profile. Returns a paginated feed of comments with optional
    cursor for pagination. Each page returns up to 10 comments.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileCommentsLiveFetchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileCommentsLiveFetchResponse200 | ProfileCommentsLiveFetchResponse400 | ProfileCommentsLiveFetchResponse401 | ProfileCommentsLiveFetchResponse402 | ProfileCommentsLiveFetchResponse403 | ProfileCommentsLiveFetchResponse404 | ProfileCommentsLiveFetchResponse429 | ProfileCommentsLiveFetchResponse500 | ProfileCommentsLiveFetchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
