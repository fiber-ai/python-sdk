from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_repo_contributors_body import GithubRepoContributorsBody
from ...models.github_repo_contributors_response_200 import GithubRepoContributorsResponse200
from ...models.github_repo_contributors_response_400 import GithubRepoContributorsResponse400
from ...models.github_repo_contributors_response_401 import GithubRepoContributorsResponse401
from ...models.github_repo_contributors_response_402 import GithubRepoContributorsResponse402
from ...models.github_repo_contributors_response_403 import GithubRepoContributorsResponse403
from ...models.github_repo_contributors_response_404 import GithubRepoContributorsResponse404
from ...models.github_repo_contributors_response_422 import GithubRepoContributorsResponse422
from ...models.github_repo_contributors_response_429 import GithubRepoContributorsResponse429
from ...models.github_repo_contributors_response_500 import GithubRepoContributorsResponse500
from ...models.github_repo_contributors_response_503 import GithubRepoContributorsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GithubRepoContributorsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/github/repo-contributors",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GithubRepoContributorsResponse200
    | GithubRepoContributorsResponse400
    | GithubRepoContributorsResponse401
    | GithubRepoContributorsResponse402
    | GithubRepoContributorsResponse403
    | GithubRepoContributorsResponse404
    | GithubRepoContributorsResponse422
    | GithubRepoContributorsResponse429
    | GithubRepoContributorsResponse500
    | GithubRepoContributorsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GithubRepoContributorsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GithubRepoContributorsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GithubRepoContributorsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GithubRepoContributorsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GithubRepoContributorsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GithubRepoContributorsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GithubRepoContributorsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GithubRepoContributorsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GithubRepoContributorsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GithubRepoContributorsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GithubRepoContributorsResponse200
    | GithubRepoContributorsResponse400
    | GithubRepoContributorsResponse401
    | GithubRepoContributorsResponse402
    | GithubRepoContributorsResponse403
    | GithubRepoContributorsResponse404
    | GithubRepoContributorsResponse422
    | GithubRepoContributorsResponse429
    | GithubRepoContributorsResponse500
    | GithubRepoContributorsResponse503
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
    body: GithubRepoContributorsBody,
) -> Response[
    GithubRepoContributorsResponse200
    | GithubRepoContributorsResponse400
    | GithubRepoContributorsResponse401
    | GithubRepoContributorsResponse402
    | GithubRepoContributorsResponse403
    | GithubRepoContributorsResponse404
    | GithubRepoContributorsResponse422
    | GithubRepoContributorsResponse429
    | GithubRepoContributorsResponse500
    | GithubRepoContributorsResponse503
]:
    """List contributors to a repository

     Returns one page of contributors for a repository, up to 100 per page. Only the top 500 contributors
    are available. Bot accounts are omitted. A repository whose contributor list cannot be retrieved
    responds with 422.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of contributors&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoContributorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubRepoContributorsResponse200 | GithubRepoContributorsResponse400 | GithubRepoContributorsResponse401 | GithubRepoContributorsResponse402 | GithubRepoContributorsResponse403 | GithubRepoContributorsResponse404 | GithubRepoContributorsResponse422 | GithubRepoContributorsResponse429 | GithubRepoContributorsResponse500 | GithubRepoContributorsResponse503]
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
    body: GithubRepoContributorsBody,
) -> (
    GithubRepoContributorsResponse200
    | GithubRepoContributorsResponse400
    | GithubRepoContributorsResponse401
    | GithubRepoContributorsResponse402
    | GithubRepoContributorsResponse403
    | GithubRepoContributorsResponse404
    | GithubRepoContributorsResponse422
    | GithubRepoContributorsResponse429
    | GithubRepoContributorsResponse500
    | GithubRepoContributorsResponse503
    | None
):
    """List contributors to a repository

     Returns one page of contributors for a repository, up to 100 per page. Only the top 500 contributors
    are available. Bot accounts are omitted. A repository whose contributor list cannot be retrieved
    responds with 422.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of contributors&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoContributorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubRepoContributorsResponse200 | GithubRepoContributorsResponse400 | GithubRepoContributorsResponse401 | GithubRepoContributorsResponse402 | GithubRepoContributorsResponse403 | GithubRepoContributorsResponse404 | GithubRepoContributorsResponse422 | GithubRepoContributorsResponse429 | GithubRepoContributorsResponse500 | GithubRepoContributorsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GithubRepoContributorsBody,
) -> Response[
    GithubRepoContributorsResponse200
    | GithubRepoContributorsResponse400
    | GithubRepoContributorsResponse401
    | GithubRepoContributorsResponse402
    | GithubRepoContributorsResponse403
    | GithubRepoContributorsResponse404
    | GithubRepoContributorsResponse422
    | GithubRepoContributorsResponse429
    | GithubRepoContributorsResponse500
    | GithubRepoContributorsResponse503
]:
    """List contributors to a repository

     Returns one page of contributors for a repository, up to 100 per page. Only the top 500 contributors
    are available. Bot accounts are omitted. A repository whose contributor list cannot be retrieved
    responds with 422.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of contributors&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoContributorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubRepoContributorsResponse200 | GithubRepoContributorsResponse400 | GithubRepoContributorsResponse401 | GithubRepoContributorsResponse402 | GithubRepoContributorsResponse403 | GithubRepoContributorsResponse404 | GithubRepoContributorsResponse422 | GithubRepoContributorsResponse429 | GithubRepoContributorsResponse500 | GithubRepoContributorsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GithubRepoContributorsBody,
) -> (
    GithubRepoContributorsResponse200
    | GithubRepoContributorsResponse400
    | GithubRepoContributorsResponse401
    | GithubRepoContributorsResponse402
    | GithubRepoContributorsResponse403
    | GithubRepoContributorsResponse404
    | GithubRepoContributorsResponse422
    | GithubRepoContributorsResponse429
    | GithubRepoContributorsResponse500
    | GithubRepoContributorsResponse503
    | None
):
    """List contributors to a repository

     Returns one page of contributors for a repository, up to 100 per page. Only the top 500 contributors
    are available. Bot accounts are omitted. A repository whose contributor list cannot be retrieved
    responds with 422.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of contributors&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoContributorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubRepoContributorsResponse200 | GithubRepoContributorsResponse400 | GithubRepoContributorsResponse401 | GithubRepoContributorsResponse402 | GithubRepoContributorsResponse403 | GithubRepoContributorsResponse404 | GithubRepoContributorsResponse422 | GithubRepoContributorsResponse429 | GithubRepoContributorsResponse500 | GithubRepoContributorsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
