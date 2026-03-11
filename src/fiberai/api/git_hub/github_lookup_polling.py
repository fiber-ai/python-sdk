from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_lookup_polling_body import GithubLookupPollingBody
from ...models.github_lookup_polling_response_200 import GithubLookupPollingResponse200
from ...models.github_lookup_polling_response_400 import GithubLookupPollingResponse400
from ...models.github_lookup_polling_response_401 import GithubLookupPollingResponse401
from ...models.github_lookup_polling_response_402 import GithubLookupPollingResponse402
from ...models.github_lookup_polling_response_403 import GithubLookupPollingResponse403
from ...models.github_lookup_polling_response_404 import GithubLookupPollingResponse404
from ...models.github_lookup_polling_response_429 import GithubLookupPollingResponse429
from ...models.github_lookup_polling_response_500 import GithubLookupPollingResponse500
from ...models.github_lookup_polling_response_503 import GithubLookupPollingResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GithubLookupPollingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/github-lookup/polling",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GithubLookupPollingResponse200
    | GithubLookupPollingResponse400
    | GithubLookupPollingResponse401
    | GithubLookupPollingResponse402
    | GithubLookupPollingResponse403
    | GithubLookupPollingResponse404
    | GithubLookupPollingResponse429
    | GithubLookupPollingResponse500
    | GithubLookupPollingResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GithubLookupPollingResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GithubLookupPollingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GithubLookupPollingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GithubLookupPollingResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GithubLookupPollingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GithubLookupPollingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GithubLookupPollingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GithubLookupPollingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GithubLookupPollingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GithubLookupPollingResponse200
    | GithubLookupPollingResponse400
    | GithubLookupPollingResponse401
    | GithubLookupPollingResponse402
    | GithubLookupPollingResponse403
    | GithubLookupPollingResponse404
    | GithubLookupPollingResponse429
    | GithubLookupPollingResponse500
    | GithubLookupPollingResponse503
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
    body: GithubLookupPollingBody,
) -> Response[
    GithubLookupPollingResponse200
    | GithubLookupPollingResponse400
    | GithubLookupPollingResponse401
    | GithubLookupPollingResponse402
    | GithubLookupPollingResponse403
    | GithubLookupPollingResponse404
    | GithubLookupPollingResponse429
    | GithubLookupPollingResponse500
    | GithubLookupPollingResponse503
]:
    """Poll GitHub lookup

     Poll for the results of a GitHub lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (GithubLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubLookupPollingResponse200 | GithubLookupPollingResponse400 | GithubLookupPollingResponse401 | GithubLookupPollingResponse402 | GithubLookupPollingResponse403 | GithubLookupPollingResponse404 | GithubLookupPollingResponse429 | GithubLookupPollingResponse500 | GithubLookupPollingResponse503]
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
    body: GithubLookupPollingBody,
) -> (
    GithubLookupPollingResponse200
    | GithubLookupPollingResponse400
    | GithubLookupPollingResponse401
    | GithubLookupPollingResponse402
    | GithubLookupPollingResponse403
    | GithubLookupPollingResponse404
    | GithubLookupPollingResponse429
    | GithubLookupPollingResponse500
    | GithubLookupPollingResponse503
    | None
):
    """Poll GitHub lookup

     Poll for the results of a GitHub lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (GithubLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubLookupPollingResponse200 | GithubLookupPollingResponse400 | GithubLookupPollingResponse401 | GithubLookupPollingResponse402 | GithubLookupPollingResponse403 | GithubLookupPollingResponse404 | GithubLookupPollingResponse429 | GithubLookupPollingResponse500 | GithubLookupPollingResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GithubLookupPollingBody,
) -> Response[
    GithubLookupPollingResponse200
    | GithubLookupPollingResponse400
    | GithubLookupPollingResponse401
    | GithubLookupPollingResponse402
    | GithubLookupPollingResponse403
    | GithubLookupPollingResponse404
    | GithubLookupPollingResponse429
    | GithubLookupPollingResponse500
    | GithubLookupPollingResponse503
]:
    """Poll GitHub lookup

     Poll for the results of a GitHub lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (GithubLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubLookupPollingResponse200 | GithubLookupPollingResponse400 | GithubLookupPollingResponse401 | GithubLookupPollingResponse402 | GithubLookupPollingResponse403 | GithubLookupPollingResponse404 | GithubLookupPollingResponse429 | GithubLookupPollingResponse500 | GithubLookupPollingResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GithubLookupPollingBody,
) -> (
    GithubLookupPollingResponse200
    | GithubLookupPollingResponse400
    | GithubLookupPollingResponse401
    | GithubLookupPollingResponse402
    | GithubLookupPollingResponse403
    | GithubLookupPollingResponse404
    | GithubLookupPollingResponse429
    | GithubLookupPollingResponse500
    | GithubLookupPollingResponse503
    | None
):
    """Poll GitHub lookup

     Poll for the results of a GitHub lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (GithubLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubLookupPollingResponse200 | GithubLookupPollingResponse400 | GithubLookupPollingResponse401 | GithubLookupPollingResponse402 | GithubLookupPollingResponse403 | GithubLookupPollingResponse404 | GithubLookupPollingResponse429 | GithubLookupPollingResponse500 | GithubLookupPollingResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
