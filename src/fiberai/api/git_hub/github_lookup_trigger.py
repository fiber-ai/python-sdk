from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_lookup_trigger_body import GithubLookupTriggerBody
from ...models.github_lookup_trigger_response_200 import GithubLookupTriggerResponse200
from ...models.github_lookup_trigger_response_400 import GithubLookupTriggerResponse400
from ...models.github_lookup_trigger_response_401 import GithubLookupTriggerResponse401
from ...models.github_lookup_trigger_response_402 import GithubLookupTriggerResponse402
from ...models.github_lookup_trigger_response_403 import GithubLookupTriggerResponse403
from ...models.github_lookup_trigger_response_404 import GithubLookupTriggerResponse404
from ...models.github_lookup_trigger_response_429 import GithubLookupTriggerResponse429
from ...models.github_lookup_trigger_response_500 import GithubLookupTriggerResponse500
from ...models.github_lookup_trigger_response_503 import GithubLookupTriggerResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GithubLookupTriggerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/github-lookup/trigger",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GithubLookupTriggerResponse200
    | GithubLookupTriggerResponse400
    | GithubLookupTriggerResponse401
    | GithubLookupTriggerResponse402
    | GithubLookupTriggerResponse403
    | GithubLookupTriggerResponse404
    | GithubLookupTriggerResponse429
    | GithubLookupTriggerResponse500
    | GithubLookupTriggerResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GithubLookupTriggerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GithubLookupTriggerResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GithubLookupTriggerResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GithubLookupTriggerResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GithubLookupTriggerResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GithubLookupTriggerResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GithubLookupTriggerResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GithubLookupTriggerResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GithubLookupTriggerResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GithubLookupTriggerResponse200
    | GithubLookupTriggerResponse400
    | GithubLookupTriggerResponse401
    | GithubLookupTriggerResponse402
    | GithubLookupTriggerResponse403
    | GithubLookupTriggerResponse404
    | GithubLookupTriggerResponse429
    | GithubLookupTriggerResponse500
    | GithubLookupTriggerResponse503
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
    body: GithubLookupTriggerBody,
) -> Response[
    GithubLookupTriggerResponse200
    | GithubLookupTriggerResponse400
    | GithubLookupTriggerResponse401
    | GithubLookupTriggerResponse402
    | GithubLookupTriggerResponse403
    | GithubLookupTriggerResponse404
    | GithubLookupTriggerResponse429
    | GithubLookupTriggerResponse500
    | GithubLookupTriggerResponse503
]:
    r"""Start GitHub lookup

     Use our AI agent to find GitHub profiles for a list of people using name and optional context like
    LinkedIn URL, work email, company, and job title.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per person&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GithubLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubLookupTriggerResponse200 | GithubLookupTriggerResponse400 | GithubLookupTriggerResponse401 | GithubLookupTriggerResponse402 | GithubLookupTriggerResponse403 | GithubLookupTriggerResponse404 | GithubLookupTriggerResponse429 | GithubLookupTriggerResponse500 | GithubLookupTriggerResponse503]
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
    body: GithubLookupTriggerBody,
) -> (
    GithubLookupTriggerResponse200
    | GithubLookupTriggerResponse400
    | GithubLookupTriggerResponse401
    | GithubLookupTriggerResponse402
    | GithubLookupTriggerResponse403
    | GithubLookupTriggerResponse404
    | GithubLookupTriggerResponse429
    | GithubLookupTriggerResponse500
    | GithubLookupTriggerResponse503
    | None
):
    r"""Start GitHub lookup

     Use our AI agent to find GitHub profiles for a list of people using name and optional context like
    LinkedIn URL, work email, company, and job title.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per person&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GithubLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubLookupTriggerResponse200 | GithubLookupTriggerResponse400 | GithubLookupTriggerResponse401 | GithubLookupTriggerResponse402 | GithubLookupTriggerResponse403 | GithubLookupTriggerResponse404 | GithubLookupTriggerResponse429 | GithubLookupTriggerResponse500 | GithubLookupTriggerResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GithubLookupTriggerBody,
) -> Response[
    GithubLookupTriggerResponse200
    | GithubLookupTriggerResponse400
    | GithubLookupTriggerResponse401
    | GithubLookupTriggerResponse402
    | GithubLookupTriggerResponse403
    | GithubLookupTriggerResponse404
    | GithubLookupTriggerResponse429
    | GithubLookupTriggerResponse500
    | GithubLookupTriggerResponse503
]:
    r"""Start GitHub lookup

     Use our AI agent to find GitHub profiles for a list of people using name and optional context like
    LinkedIn URL, work email, company, and job title.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per person&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GithubLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubLookupTriggerResponse200 | GithubLookupTriggerResponse400 | GithubLookupTriggerResponse401 | GithubLookupTriggerResponse402 | GithubLookupTriggerResponse403 | GithubLookupTriggerResponse404 | GithubLookupTriggerResponse429 | GithubLookupTriggerResponse500 | GithubLookupTriggerResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GithubLookupTriggerBody,
) -> (
    GithubLookupTriggerResponse200
    | GithubLookupTriggerResponse400
    | GithubLookupTriggerResponse401
    | GithubLookupTriggerResponse402
    | GithubLookupTriggerResponse403
    | GithubLookupTriggerResponse404
    | GithubLookupTriggerResponse429
    | GithubLookupTriggerResponse500
    | GithubLookupTriggerResponse503
    | None
):
    r"""Start GitHub lookup

     Use our AI agent to find GitHub profiles for a list of people using name and optional context like
    LinkedIn URL, work email, company, and job title.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per person&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GithubLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubLookupTriggerResponse200 | GithubLookupTriggerResponse400 | GithubLookupTriggerResponse401 | GithubLookupTriggerResponse402 | GithubLookupTriggerResponse403 | GithubLookupTriggerResponse404 | GithubLookupTriggerResponse429 | GithubLookupTriggerResponse500 | GithubLookupTriggerResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
