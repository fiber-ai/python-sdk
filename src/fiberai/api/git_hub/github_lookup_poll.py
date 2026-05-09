from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_lookup_poll_body import GithubLookupPollBody
from ...models.github_lookup_poll_response_200 import GithubLookupPollResponse200
from ...models.github_lookup_poll_response_400 import GithubLookupPollResponse400
from ...models.github_lookup_poll_response_401 import GithubLookupPollResponse401
from ...models.github_lookup_poll_response_402 import GithubLookupPollResponse402
from ...models.github_lookup_poll_response_403 import GithubLookupPollResponse403
from ...models.github_lookup_poll_response_404 import GithubLookupPollResponse404
from ...models.github_lookup_poll_response_429 import GithubLookupPollResponse429
from ...models.github_lookup_poll_response_500 import GithubLookupPollResponse500
from ...models.github_lookup_poll_response_503 import GithubLookupPollResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GithubLookupPollBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/github-lookup/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GithubLookupPollResponse200
    | GithubLookupPollResponse400
    | GithubLookupPollResponse401
    | GithubLookupPollResponse402
    | GithubLookupPollResponse403
    | GithubLookupPollResponse404
    | GithubLookupPollResponse429
    | GithubLookupPollResponse500
    | GithubLookupPollResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GithubLookupPollResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GithubLookupPollResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GithubLookupPollResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GithubLookupPollResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GithubLookupPollResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GithubLookupPollResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GithubLookupPollResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GithubLookupPollResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GithubLookupPollResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GithubLookupPollResponse200
    | GithubLookupPollResponse400
    | GithubLookupPollResponse401
    | GithubLookupPollResponse402
    | GithubLookupPollResponse403
    | GithubLookupPollResponse404
    | GithubLookupPollResponse429
    | GithubLookupPollResponse500
    | GithubLookupPollResponse503
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
    body: GithubLookupPollBody,
) -> Response[
    GithubLookupPollResponse200
    | GithubLookupPollResponse400
    | GithubLookupPollResponse401
    | GithubLookupPollResponse402
    | GithubLookupPollResponse403
    | GithubLookupPollResponse404
    | GithubLookupPollResponse429
    | GithubLookupPollResponse500
    | GithubLookupPollResponse503
]:
    """Poll GitHub lookup results

     Poll for the results of a GitHub lookup task. Returns progress breakdown and all completed results
    in a single response (no pagination).

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (GithubLookupPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubLookupPollResponse200 | GithubLookupPollResponse400 | GithubLookupPollResponse401 | GithubLookupPollResponse402 | GithubLookupPollResponse403 | GithubLookupPollResponse404 | GithubLookupPollResponse429 | GithubLookupPollResponse500 | GithubLookupPollResponse503]
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
    body: GithubLookupPollBody,
) -> (
    GithubLookupPollResponse200
    | GithubLookupPollResponse400
    | GithubLookupPollResponse401
    | GithubLookupPollResponse402
    | GithubLookupPollResponse403
    | GithubLookupPollResponse404
    | GithubLookupPollResponse429
    | GithubLookupPollResponse500
    | GithubLookupPollResponse503
    | None
):
    """Poll GitHub lookup results

     Poll for the results of a GitHub lookup task. Returns progress breakdown and all completed results
    in a single response (no pagination).

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (GithubLookupPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubLookupPollResponse200 | GithubLookupPollResponse400 | GithubLookupPollResponse401 | GithubLookupPollResponse402 | GithubLookupPollResponse403 | GithubLookupPollResponse404 | GithubLookupPollResponse429 | GithubLookupPollResponse500 | GithubLookupPollResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GithubLookupPollBody,
) -> Response[
    GithubLookupPollResponse200
    | GithubLookupPollResponse400
    | GithubLookupPollResponse401
    | GithubLookupPollResponse402
    | GithubLookupPollResponse403
    | GithubLookupPollResponse404
    | GithubLookupPollResponse429
    | GithubLookupPollResponse500
    | GithubLookupPollResponse503
]:
    """Poll GitHub lookup results

     Poll for the results of a GitHub lookup task. Returns progress breakdown and all completed results
    in a single response (no pagination).

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (GithubLookupPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubLookupPollResponse200 | GithubLookupPollResponse400 | GithubLookupPollResponse401 | GithubLookupPollResponse402 | GithubLookupPollResponse403 | GithubLookupPollResponse404 | GithubLookupPollResponse429 | GithubLookupPollResponse500 | GithubLookupPollResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GithubLookupPollBody,
) -> (
    GithubLookupPollResponse200
    | GithubLookupPollResponse400
    | GithubLookupPollResponse401
    | GithubLookupPollResponse402
    | GithubLookupPollResponse403
    | GithubLookupPollResponse404
    | GithubLookupPollResponse429
    | GithubLookupPollResponse500
    | GithubLookupPollResponse503
    | None
):
    """Poll GitHub lookup results

     Poll for the results of a GitHub lookup task. Returns progress breakdown and all completed results
    in a single response (no pagination).

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (GithubLookupPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubLookupPollResponse200 | GithubLookupPollResponse400 | GithubLookupPollResponse401 | GithubLookupPollResponse402 | GithubLookupPollResponse403 | GithubLookupPollResponse404 | GithubLookupPollResponse429 | GithubLookupPollResponse500 | GithubLookupPollResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
