from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_repo_search_body import GithubRepoSearchBody
from ...models.github_repo_search_response_200 import GithubRepoSearchResponse200
from ...models.github_repo_search_response_400 import GithubRepoSearchResponse400
from ...models.github_repo_search_response_401 import GithubRepoSearchResponse401
from ...models.github_repo_search_response_402 import GithubRepoSearchResponse402
from ...models.github_repo_search_response_403 import GithubRepoSearchResponse403
from ...models.github_repo_search_response_404 import GithubRepoSearchResponse404
from ...models.github_repo_search_response_422 import GithubRepoSearchResponse422
from ...models.github_repo_search_response_429 import GithubRepoSearchResponse429
from ...models.github_repo_search_response_500 import GithubRepoSearchResponse500
from ...models.github_repo_search_response_503 import GithubRepoSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GithubRepoSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/github/repo-search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GithubRepoSearchResponse200
    | GithubRepoSearchResponse400
    | GithubRepoSearchResponse401
    | GithubRepoSearchResponse402
    | GithubRepoSearchResponse403
    | GithubRepoSearchResponse404
    | GithubRepoSearchResponse422
    | GithubRepoSearchResponse429
    | GithubRepoSearchResponse500
    | GithubRepoSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GithubRepoSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GithubRepoSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GithubRepoSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GithubRepoSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GithubRepoSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GithubRepoSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GithubRepoSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GithubRepoSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GithubRepoSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GithubRepoSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GithubRepoSearchResponse200
    | GithubRepoSearchResponse400
    | GithubRepoSearchResponse401
    | GithubRepoSearchResponse402
    | GithubRepoSearchResponse403
    | GithubRepoSearchResponse404
    | GithubRepoSearchResponse422
    | GithubRepoSearchResponse429
    | GithubRepoSearchResponse500
    | GithubRepoSearchResponse503
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
    body: GithubRepoSearchBody,
) -> Response[
    GithubRepoSearchResponse200
    | GithubRepoSearchResponse400
    | GithubRepoSearchResponse401
    | GithubRepoSearchResponse402
    | GithubRepoSearchResponse403
    | GithubRepoSearchResponse404
    | GithubRepoSearchResponse422
    | GithubRepoSearchResponse429
    | GithubRepoSearchResponse500
    | GithubRepoSearchResponse503
]:
    """Search repositories

     Returns one page of repositories matching a search query, up to 100 per page. At most 1,000 results
    can be paged through.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubRepoSearchResponse200 | GithubRepoSearchResponse400 | GithubRepoSearchResponse401 | GithubRepoSearchResponse402 | GithubRepoSearchResponse403 | GithubRepoSearchResponse404 | GithubRepoSearchResponse422 | GithubRepoSearchResponse429 | GithubRepoSearchResponse500 | GithubRepoSearchResponse503]
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
    body: GithubRepoSearchBody,
) -> (
    GithubRepoSearchResponse200
    | GithubRepoSearchResponse400
    | GithubRepoSearchResponse401
    | GithubRepoSearchResponse402
    | GithubRepoSearchResponse403
    | GithubRepoSearchResponse404
    | GithubRepoSearchResponse422
    | GithubRepoSearchResponse429
    | GithubRepoSearchResponse500
    | GithubRepoSearchResponse503
    | None
):
    """Search repositories

     Returns one page of repositories matching a search query, up to 100 per page. At most 1,000 results
    can be paged through.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubRepoSearchResponse200 | GithubRepoSearchResponse400 | GithubRepoSearchResponse401 | GithubRepoSearchResponse402 | GithubRepoSearchResponse403 | GithubRepoSearchResponse404 | GithubRepoSearchResponse422 | GithubRepoSearchResponse429 | GithubRepoSearchResponse500 | GithubRepoSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GithubRepoSearchBody,
) -> Response[
    GithubRepoSearchResponse200
    | GithubRepoSearchResponse400
    | GithubRepoSearchResponse401
    | GithubRepoSearchResponse402
    | GithubRepoSearchResponse403
    | GithubRepoSearchResponse404
    | GithubRepoSearchResponse422
    | GithubRepoSearchResponse429
    | GithubRepoSearchResponse500
    | GithubRepoSearchResponse503
]:
    """Search repositories

     Returns one page of repositories matching a search query, up to 100 per page. At most 1,000 results
    can be paged through.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubRepoSearchResponse200 | GithubRepoSearchResponse400 | GithubRepoSearchResponse401 | GithubRepoSearchResponse402 | GithubRepoSearchResponse403 | GithubRepoSearchResponse404 | GithubRepoSearchResponse422 | GithubRepoSearchResponse429 | GithubRepoSearchResponse500 | GithubRepoSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GithubRepoSearchBody,
) -> (
    GithubRepoSearchResponse200
    | GithubRepoSearchResponse400
    | GithubRepoSearchResponse401
    | GithubRepoSearchResponse402
    | GithubRepoSearchResponse403
    | GithubRepoSearchResponse404
    | GithubRepoSearchResponse422
    | GithubRepoSearchResponse429
    | GithubRepoSearchResponse500
    | GithubRepoSearchResponse503
    | None
):
    """Search repositories

     Returns one page of repositories matching a search query, up to 100 per page. At most 1,000 results
    can be paged through.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubRepoSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubRepoSearchResponse200 | GithubRepoSearchResponse400 | GithubRepoSearchResponse401 | GithubRepoSearchResponse402 | GithubRepoSearchResponse403 | GithubRepoSearchResponse404 | GithubRepoSearchResponse422 | GithubRepoSearchResponse429 | GithubRepoSearchResponse500 | GithubRepoSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
