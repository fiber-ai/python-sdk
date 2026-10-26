from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_org_contributors_body import GithubOrgContributorsBody
from ...models.github_org_contributors_response_200 import GithubOrgContributorsResponse200
from ...models.github_org_contributors_response_400 import GithubOrgContributorsResponse400
from ...models.github_org_contributors_response_401 import GithubOrgContributorsResponse401
from ...models.github_org_contributors_response_402 import GithubOrgContributorsResponse402
from ...models.github_org_contributors_response_403 import GithubOrgContributorsResponse403
from ...models.github_org_contributors_response_404 import GithubOrgContributorsResponse404
from ...models.github_org_contributors_response_422 import GithubOrgContributorsResponse422
from ...models.github_org_contributors_response_429 import GithubOrgContributorsResponse429
from ...models.github_org_contributors_response_500 import GithubOrgContributorsResponse500
from ...models.github_org_contributors_response_503 import GithubOrgContributorsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GithubOrgContributorsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/github/org-contributors/trigger",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GithubOrgContributorsResponse200
    | GithubOrgContributorsResponse400
    | GithubOrgContributorsResponse401
    | GithubOrgContributorsResponse402
    | GithubOrgContributorsResponse403
    | GithubOrgContributorsResponse404
    | GithubOrgContributorsResponse422
    | GithubOrgContributorsResponse429
    | GithubOrgContributorsResponse500
    | GithubOrgContributorsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GithubOrgContributorsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GithubOrgContributorsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GithubOrgContributorsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GithubOrgContributorsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GithubOrgContributorsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GithubOrgContributorsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GithubOrgContributorsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GithubOrgContributorsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GithubOrgContributorsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GithubOrgContributorsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GithubOrgContributorsResponse200
    | GithubOrgContributorsResponse400
    | GithubOrgContributorsResponse401
    | GithubOrgContributorsResponse402
    | GithubOrgContributorsResponse403
    | GithubOrgContributorsResponse404
    | GithubOrgContributorsResponse422
    | GithubOrgContributorsResponse429
    | GithubOrgContributorsResponse500
    | GithubOrgContributorsResponse503
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
    body: GithubOrgContributorsBody,
) -> Response[
    GithubOrgContributorsResponse200
    | GithubOrgContributorsResponse400
    | GithubOrgContributorsResponse401
    | GithubOrgContributorsResponse402
    | GithubOrgContributorsResponse403
    | GithubOrgContributorsResponse404
    | GithubOrgContributorsResponse422
    | GithubOrgContributorsResponse429
    | GithubOrgContributorsResponse500
    | GithubOrgContributorsResponse503
]:
    """Start an organization contributor scan

     Scans an organization's public repositories and collects their contributors. Forks are skipped. At
    most 500 repositories are scanned, and at most the top 500 contributors of each repository are kept.
    Poll with the returned run id.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per repository scanned&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubOrgContributorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubOrgContributorsResponse200 | GithubOrgContributorsResponse400 | GithubOrgContributorsResponse401 | GithubOrgContributorsResponse402 | GithubOrgContributorsResponse403 | GithubOrgContributorsResponse404 | GithubOrgContributorsResponse422 | GithubOrgContributorsResponse429 | GithubOrgContributorsResponse500 | GithubOrgContributorsResponse503]
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
    body: GithubOrgContributorsBody,
) -> (
    GithubOrgContributorsResponse200
    | GithubOrgContributorsResponse400
    | GithubOrgContributorsResponse401
    | GithubOrgContributorsResponse402
    | GithubOrgContributorsResponse403
    | GithubOrgContributorsResponse404
    | GithubOrgContributorsResponse422
    | GithubOrgContributorsResponse429
    | GithubOrgContributorsResponse500
    | GithubOrgContributorsResponse503
    | None
):
    """Start an organization contributor scan

     Scans an organization's public repositories and collects their contributors. Forks are skipped. At
    most 500 repositories are scanned, and at most the top 500 contributors of each repository are kept.
    Poll with the returned run id.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per repository scanned&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubOrgContributorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubOrgContributorsResponse200 | GithubOrgContributorsResponse400 | GithubOrgContributorsResponse401 | GithubOrgContributorsResponse402 | GithubOrgContributorsResponse403 | GithubOrgContributorsResponse404 | GithubOrgContributorsResponse422 | GithubOrgContributorsResponse429 | GithubOrgContributorsResponse500 | GithubOrgContributorsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GithubOrgContributorsBody,
) -> Response[
    GithubOrgContributorsResponse200
    | GithubOrgContributorsResponse400
    | GithubOrgContributorsResponse401
    | GithubOrgContributorsResponse402
    | GithubOrgContributorsResponse403
    | GithubOrgContributorsResponse404
    | GithubOrgContributorsResponse422
    | GithubOrgContributorsResponse429
    | GithubOrgContributorsResponse500
    | GithubOrgContributorsResponse503
]:
    """Start an organization contributor scan

     Scans an organization's public repositories and collects their contributors. Forks are skipped. At
    most 500 repositories are scanned, and at most the top 500 contributors of each repository are kept.
    Poll with the returned run id.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per repository scanned&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubOrgContributorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubOrgContributorsResponse200 | GithubOrgContributorsResponse400 | GithubOrgContributorsResponse401 | GithubOrgContributorsResponse402 | GithubOrgContributorsResponse403 | GithubOrgContributorsResponse404 | GithubOrgContributorsResponse422 | GithubOrgContributorsResponse429 | GithubOrgContributorsResponse500 | GithubOrgContributorsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GithubOrgContributorsBody,
) -> (
    GithubOrgContributorsResponse200
    | GithubOrgContributorsResponse400
    | GithubOrgContributorsResponse401
    | GithubOrgContributorsResponse402
    | GithubOrgContributorsResponse403
    | GithubOrgContributorsResponse404
    | GithubOrgContributorsResponse422
    | GithubOrgContributorsResponse429
    | GithubOrgContributorsResponse500
    | GithubOrgContributorsResponse503
    | None
):
    """Start an organization contributor scan

     Scans an organization's public repositories and collects their contributors. Forks are skipped. At
    most 500 repositories are scanned, and at most the top 500 contributors of each repository are kept.
    Poll with the returned run id.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per repository scanned&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (GithubOrgContributorsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubOrgContributorsResponse200 | GithubOrgContributorsResponse400 | GithubOrgContributorsResponse401 | GithubOrgContributorsResponse402 | GithubOrgContributorsResponse403 | GithubOrgContributorsResponse404 | GithubOrgContributorsResponse422 | GithubOrgContributorsResponse429 | GithubOrgContributorsResponse500 | GithubOrgContributorsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
