from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_to_linkedin_single_body import GithubToLinkedinSingleBody
from ...models.github_to_linkedin_single_response_200 import GithubToLinkedinSingleResponse200
from ...models.github_to_linkedin_single_response_400 import GithubToLinkedinSingleResponse400
from ...models.github_to_linkedin_single_response_401 import GithubToLinkedinSingleResponse401
from ...models.github_to_linkedin_single_response_402 import GithubToLinkedinSingleResponse402
from ...models.github_to_linkedin_single_response_403 import GithubToLinkedinSingleResponse403
from ...models.github_to_linkedin_single_response_404 import GithubToLinkedinSingleResponse404
from ...models.github_to_linkedin_single_response_422 import GithubToLinkedinSingleResponse422
from ...models.github_to_linkedin_single_response_429 import GithubToLinkedinSingleResponse429
from ...models.github_to_linkedin_single_response_500 import GithubToLinkedinSingleResponse500
from ...models.github_to_linkedin_single_response_503 import GithubToLinkedinSingleResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GithubToLinkedinSingleBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/github-to-linkedin/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GithubToLinkedinSingleResponse200
    | GithubToLinkedinSingleResponse400
    | GithubToLinkedinSingleResponse401
    | GithubToLinkedinSingleResponse402
    | GithubToLinkedinSingleResponse403
    | GithubToLinkedinSingleResponse404
    | GithubToLinkedinSingleResponse422
    | GithubToLinkedinSingleResponse429
    | GithubToLinkedinSingleResponse500
    | GithubToLinkedinSingleResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GithubToLinkedinSingleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GithubToLinkedinSingleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GithubToLinkedinSingleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GithubToLinkedinSingleResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GithubToLinkedinSingleResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GithubToLinkedinSingleResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GithubToLinkedinSingleResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GithubToLinkedinSingleResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GithubToLinkedinSingleResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GithubToLinkedinSingleResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GithubToLinkedinSingleResponse200
    | GithubToLinkedinSingleResponse400
    | GithubToLinkedinSingleResponse401
    | GithubToLinkedinSingleResponse402
    | GithubToLinkedinSingleResponse403
    | GithubToLinkedinSingleResponse404
    | GithubToLinkedinSingleResponse422
    | GithubToLinkedinSingleResponse429
    | GithubToLinkedinSingleResponse500
    | GithubToLinkedinSingleResponse503
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
    body: GithubToLinkedinSingleBody,
) -> Response[
    GithubToLinkedinSingleResponse200
    | GithubToLinkedinSingleResponse400
    | GithubToLinkedinSingleResponse401
    | GithubToLinkedinSingleResponse402
    | GithubToLinkedinSingleResponse403
    | GithubToLinkedinSingleResponse404
    | GithubToLinkedinSingleResponse422
    | GithubToLinkedinSingleResponse429
    | GithubToLinkedinSingleResponse500
    | GithubToLinkedinSingleResponse503
]:
    r"""Find person by GitHub username (single)

     Given a GitHub username, find the person's LinkedIn profile and extract work emails.
    Use `outputType` to control what data is returned and charged for.
    For outputType=linkedin we only return LinkedIn fields, for outputType=email we only return emails,
    for outputType=both we return both.
    To avoid 429 errors, spread requests evenly instead of sending a burst.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per person (LinkedIn lookup) + 3 credits per person (email
    extraction)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (GithubToLinkedinSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubToLinkedinSingleResponse200 | GithubToLinkedinSingleResponse400 | GithubToLinkedinSingleResponse401 | GithubToLinkedinSingleResponse402 | GithubToLinkedinSingleResponse403 | GithubToLinkedinSingleResponse404 | GithubToLinkedinSingleResponse422 | GithubToLinkedinSingleResponse429 | GithubToLinkedinSingleResponse500 | GithubToLinkedinSingleResponse503]
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
    body: GithubToLinkedinSingleBody,
) -> (
    GithubToLinkedinSingleResponse200
    | GithubToLinkedinSingleResponse400
    | GithubToLinkedinSingleResponse401
    | GithubToLinkedinSingleResponse402
    | GithubToLinkedinSingleResponse403
    | GithubToLinkedinSingleResponse404
    | GithubToLinkedinSingleResponse422
    | GithubToLinkedinSingleResponse429
    | GithubToLinkedinSingleResponse500
    | GithubToLinkedinSingleResponse503
    | None
):
    r"""Find person by GitHub username (single)

     Given a GitHub username, find the person's LinkedIn profile and extract work emails.
    Use `outputType` to control what data is returned and charged for.
    For outputType=linkedin we only return LinkedIn fields, for outputType=email we only return emails,
    for outputType=both we return both.
    To avoid 429 errors, spread requests evenly instead of sending a burst.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per person (LinkedIn lookup) + 3 credits per person (email
    extraction)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (GithubToLinkedinSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubToLinkedinSingleResponse200 | GithubToLinkedinSingleResponse400 | GithubToLinkedinSingleResponse401 | GithubToLinkedinSingleResponse402 | GithubToLinkedinSingleResponse403 | GithubToLinkedinSingleResponse404 | GithubToLinkedinSingleResponse422 | GithubToLinkedinSingleResponse429 | GithubToLinkedinSingleResponse500 | GithubToLinkedinSingleResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GithubToLinkedinSingleBody,
) -> Response[
    GithubToLinkedinSingleResponse200
    | GithubToLinkedinSingleResponse400
    | GithubToLinkedinSingleResponse401
    | GithubToLinkedinSingleResponse402
    | GithubToLinkedinSingleResponse403
    | GithubToLinkedinSingleResponse404
    | GithubToLinkedinSingleResponse422
    | GithubToLinkedinSingleResponse429
    | GithubToLinkedinSingleResponse500
    | GithubToLinkedinSingleResponse503
]:
    r"""Find person by GitHub username (single)

     Given a GitHub username, find the person's LinkedIn profile and extract work emails.
    Use `outputType` to control what data is returned and charged for.
    For outputType=linkedin we only return LinkedIn fields, for outputType=email we only return emails,
    for outputType=both we return both.
    To avoid 429 errors, spread requests evenly instead of sending a burst.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per person (LinkedIn lookup) + 3 credits per person (email
    extraction)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (GithubToLinkedinSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubToLinkedinSingleResponse200 | GithubToLinkedinSingleResponse400 | GithubToLinkedinSingleResponse401 | GithubToLinkedinSingleResponse402 | GithubToLinkedinSingleResponse403 | GithubToLinkedinSingleResponse404 | GithubToLinkedinSingleResponse422 | GithubToLinkedinSingleResponse429 | GithubToLinkedinSingleResponse500 | GithubToLinkedinSingleResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GithubToLinkedinSingleBody,
) -> (
    GithubToLinkedinSingleResponse200
    | GithubToLinkedinSingleResponse400
    | GithubToLinkedinSingleResponse401
    | GithubToLinkedinSingleResponse402
    | GithubToLinkedinSingleResponse403
    | GithubToLinkedinSingleResponse404
    | GithubToLinkedinSingleResponse422
    | GithubToLinkedinSingleResponse429
    | GithubToLinkedinSingleResponse500
    | GithubToLinkedinSingleResponse503
    | None
):
    r"""Find person by GitHub username (single)

     Given a GitHub username, find the person's LinkedIn profile and extract work emails.
    Use `outputType` to control what data is returned and charged for.
    For outputType=linkedin we only return LinkedIn fields, for outputType=email we only return emails,
    for outputType=both we return both.
    To avoid 429 errors, spread requests evenly instead of sending a burst.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per person (LinkedIn lookup) + 3 credits per person (email
    extraction)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (GithubToLinkedinSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubToLinkedinSingleResponse200 | GithubToLinkedinSingleResponse400 | GithubToLinkedinSingleResponse401 | GithubToLinkedinSingleResponse402 | GithubToLinkedinSingleResponse403 | GithubToLinkedinSingleResponse404 | GithubToLinkedinSingleResponse422 | GithubToLinkedinSingleResponse429 | GithubToLinkedinSingleResponse500 | GithubToLinkedinSingleResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
