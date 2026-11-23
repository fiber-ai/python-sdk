from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_repo_forkers_body import GithubRepoForkersBody
from ...models.github_repo_forkers_response_200 import GithubRepoForkersResponse200
from ...models.github_repo_forkers_response_400 import GithubRepoForkersResponse400
from ...models.github_repo_forkers_response_401 import GithubRepoForkersResponse401
from ...models.github_repo_forkers_response_402 import GithubRepoForkersResponse402
from ...models.github_repo_forkers_response_403 import GithubRepoForkersResponse403
from ...models.github_repo_forkers_response_404 import GithubRepoForkersResponse404
from ...models.github_repo_forkers_response_422 import GithubRepoForkersResponse422
from ...models.github_repo_forkers_response_429 import GithubRepoForkersResponse429
from ...models.github_repo_forkers_response_500 import GithubRepoForkersResponse500
from ...models.github_repo_forkers_response_503 import GithubRepoForkersResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GithubRepoForkersBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/github/repo-forkers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GithubRepoForkersResponse200
    | GithubRepoForkersResponse400
    | GithubRepoForkersResponse401
    | GithubRepoForkersResponse402
    | GithubRepoForkersResponse403
    | GithubRepoForkersResponse404
    | GithubRepoForkersResponse422
    | GithubRepoForkersResponse429
    | GithubRepoForkersResponse500
    | GithubRepoForkersResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GithubRepoForkersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GithubRepoForkersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GithubRepoForkersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GithubRepoForkersResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GithubRepoForkersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GithubRepoForkersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GithubRepoForkersResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GithubRepoForkersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GithubRepoForkersResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GithubRepoForkersResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GithubRepoForkersResponse200
    | GithubRepoForkersResponse400
    | GithubRepoForkersResponse401
    | GithubRepoForkersResponse402
    | GithubRepoForkersResponse403
    | GithubRepoForkersResponse404
    | GithubRepoForkersResponse422
    | GithubRepoForkersResponse429
    | GithubRepoForkersResponse500
    | GithubRepoForkersResponse503
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
    body: GithubRepoForkersBody,
) -> Response[
    GithubRepoForkersResponse200
    | GithubRepoForkersResponse400
    | GithubRepoForkersResponse401
    | GithubRepoForkersResponse402
    | GithubRepoForkersResponse403
    | GithubRepoForkersResponse404
    | GithubRepoForkersResponse422
    | GithubRepoForkersResponse429
    | GithubRepoForkersResponse500
    | GithubRepoForkersResponse503
]:
    """List people who forked a repository

     Returns one page of people who forked a repository, up to 100 per page, newest first. Organization
    and bot accounts are omitted. Pass nextPageToken until it is null to continue. Paging is not capped;
    a large repository can run to hundreds of pages.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of forkers&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoForkersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubRepoForkersResponse200 | GithubRepoForkersResponse400 | GithubRepoForkersResponse401 | GithubRepoForkersResponse402 | GithubRepoForkersResponse403 | GithubRepoForkersResponse404 | GithubRepoForkersResponse422 | GithubRepoForkersResponse429 | GithubRepoForkersResponse500 | GithubRepoForkersResponse503]
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
    body: GithubRepoForkersBody,
) -> (
    GithubRepoForkersResponse200
    | GithubRepoForkersResponse400
    | GithubRepoForkersResponse401
    | GithubRepoForkersResponse402
    | GithubRepoForkersResponse403
    | GithubRepoForkersResponse404
    | GithubRepoForkersResponse422
    | GithubRepoForkersResponse429
    | GithubRepoForkersResponse500
    | GithubRepoForkersResponse503
    | None
):
    """List people who forked a repository

     Returns one page of people who forked a repository, up to 100 per page, newest first. Organization
    and bot accounts are omitted. Pass nextPageToken until it is null to continue. Paging is not capped;
    a large repository can run to hundreds of pages.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of forkers&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoForkersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubRepoForkersResponse200 | GithubRepoForkersResponse400 | GithubRepoForkersResponse401 | GithubRepoForkersResponse402 | GithubRepoForkersResponse403 | GithubRepoForkersResponse404 | GithubRepoForkersResponse422 | GithubRepoForkersResponse429 | GithubRepoForkersResponse500 | GithubRepoForkersResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GithubRepoForkersBody,
) -> Response[
    GithubRepoForkersResponse200
    | GithubRepoForkersResponse400
    | GithubRepoForkersResponse401
    | GithubRepoForkersResponse402
    | GithubRepoForkersResponse403
    | GithubRepoForkersResponse404
    | GithubRepoForkersResponse422
    | GithubRepoForkersResponse429
    | GithubRepoForkersResponse500
    | GithubRepoForkersResponse503
]:
    """List people who forked a repository

     Returns one page of people who forked a repository, up to 100 per page, newest first. Organization
    and bot accounts are omitted. Pass nextPageToken until it is null to continue. Paging is not capped;
    a large repository can run to hundreds of pages.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of forkers&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoForkersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubRepoForkersResponse200 | GithubRepoForkersResponse400 | GithubRepoForkersResponse401 | GithubRepoForkersResponse402 | GithubRepoForkersResponse403 | GithubRepoForkersResponse404 | GithubRepoForkersResponse422 | GithubRepoForkersResponse429 | GithubRepoForkersResponse500 | GithubRepoForkersResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GithubRepoForkersBody,
) -> (
    GithubRepoForkersResponse200
    | GithubRepoForkersResponse400
    | GithubRepoForkersResponse401
    | GithubRepoForkersResponse402
    | GithubRepoForkersResponse403
    | GithubRepoForkersResponse404
    | GithubRepoForkersResponse422
    | GithubRepoForkersResponse429
    | GithubRepoForkersResponse500
    | GithubRepoForkersResponse503
    | None
):
    """List people who forked a repository

     Returns one page of people who forked a repository, up to 100 per page, newest first. Organization
    and bot accounts are omitted. Pass nextPageToken until it is null to continue. Paging is not capped;
    a large repository can run to hundreds of pages.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of forkers&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoForkersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubRepoForkersResponse200 | GithubRepoForkersResponse400 | GithubRepoForkersResponse401 | GithubRepoForkersResponse402 | GithubRepoForkersResponse403 | GithubRepoForkersResponse404 | GithubRepoForkersResponse422 | GithubRepoForkersResponse429 | GithubRepoForkersResponse500 | GithubRepoForkersResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
