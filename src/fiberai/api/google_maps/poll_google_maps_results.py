from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.poll_google_maps_results_body import PollGoogleMapsResultsBody
from ...models.poll_google_maps_results_response_200 import PollGoogleMapsResultsResponse200
from ...models.poll_google_maps_results_response_400 import PollGoogleMapsResultsResponse400
from ...models.poll_google_maps_results_response_401 import PollGoogleMapsResultsResponse401
from ...models.poll_google_maps_results_response_402 import PollGoogleMapsResultsResponse402
from ...models.poll_google_maps_results_response_403 import PollGoogleMapsResultsResponse403
from ...models.poll_google_maps_results_response_404 import PollGoogleMapsResultsResponse404
from ...models.poll_google_maps_results_response_429 import PollGoogleMapsResultsResponse429
from ...models.poll_google_maps_results_response_500 import PollGoogleMapsResultsResponse500
from ...models.poll_google_maps_results_response_503 import PollGoogleMapsResultsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PollGoogleMapsResultsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/google-maps-search/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PollGoogleMapsResultsResponse200
    | PollGoogleMapsResultsResponse400
    | PollGoogleMapsResultsResponse401
    | PollGoogleMapsResultsResponse402
    | PollGoogleMapsResultsResponse403
    | PollGoogleMapsResultsResponse404
    | PollGoogleMapsResultsResponse429
    | PollGoogleMapsResultsResponse500
    | PollGoogleMapsResultsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PollGoogleMapsResultsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PollGoogleMapsResultsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PollGoogleMapsResultsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PollGoogleMapsResultsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PollGoogleMapsResultsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PollGoogleMapsResultsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PollGoogleMapsResultsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PollGoogleMapsResultsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PollGoogleMapsResultsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PollGoogleMapsResultsResponse200
    | PollGoogleMapsResultsResponse400
    | PollGoogleMapsResultsResponse401
    | PollGoogleMapsResultsResponse402
    | PollGoogleMapsResultsResponse403
    | PollGoogleMapsResultsResponse404
    | PollGoogleMapsResultsResponse429
    | PollGoogleMapsResultsResponse500
    | PollGoogleMapsResultsResponse503
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
    body: PollGoogleMapsResultsBody,
) -> Response[
    PollGoogleMapsResultsResponse200
    | PollGoogleMapsResultsResponse400
    | PollGoogleMapsResultsResponse401
    | PollGoogleMapsResultsResponse402
    | PollGoogleMapsResultsResponse403
    | PollGoogleMapsResultsResponse404
    | PollGoogleMapsResultsResponse429
    | PollGoogleMapsResultsResponse500
    | PollGoogleMapsResultsResponse503
]:
    """Poll for Google Maps results

     Poll for Google Maps results

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (PollGoogleMapsResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollGoogleMapsResultsResponse200 | PollGoogleMapsResultsResponse400 | PollGoogleMapsResultsResponse401 | PollGoogleMapsResultsResponse402 | PollGoogleMapsResultsResponse403 | PollGoogleMapsResultsResponse404 | PollGoogleMapsResultsResponse429 | PollGoogleMapsResultsResponse500 | PollGoogleMapsResultsResponse503]
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
    body: PollGoogleMapsResultsBody,
) -> (
    PollGoogleMapsResultsResponse200
    | PollGoogleMapsResultsResponse400
    | PollGoogleMapsResultsResponse401
    | PollGoogleMapsResultsResponse402
    | PollGoogleMapsResultsResponse403
    | PollGoogleMapsResultsResponse404
    | PollGoogleMapsResultsResponse429
    | PollGoogleMapsResultsResponse500
    | PollGoogleMapsResultsResponse503
    | None
):
    """Poll for Google Maps results

     Poll for Google Maps results

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (PollGoogleMapsResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollGoogleMapsResultsResponse200 | PollGoogleMapsResultsResponse400 | PollGoogleMapsResultsResponse401 | PollGoogleMapsResultsResponse402 | PollGoogleMapsResultsResponse403 | PollGoogleMapsResultsResponse404 | PollGoogleMapsResultsResponse429 | PollGoogleMapsResultsResponse500 | PollGoogleMapsResultsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PollGoogleMapsResultsBody,
) -> Response[
    PollGoogleMapsResultsResponse200
    | PollGoogleMapsResultsResponse400
    | PollGoogleMapsResultsResponse401
    | PollGoogleMapsResultsResponse402
    | PollGoogleMapsResultsResponse403
    | PollGoogleMapsResultsResponse404
    | PollGoogleMapsResultsResponse429
    | PollGoogleMapsResultsResponse500
    | PollGoogleMapsResultsResponse503
]:
    """Poll for Google Maps results

     Poll for Google Maps results

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (PollGoogleMapsResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollGoogleMapsResultsResponse200 | PollGoogleMapsResultsResponse400 | PollGoogleMapsResultsResponse401 | PollGoogleMapsResultsResponse402 | PollGoogleMapsResultsResponse403 | PollGoogleMapsResultsResponse404 | PollGoogleMapsResultsResponse429 | PollGoogleMapsResultsResponse500 | PollGoogleMapsResultsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PollGoogleMapsResultsBody,
) -> (
    PollGoogleMapsResultsResponse200
    | PollGoogleMapsResultsResponse400
    | PollGoogleMapsResultsResponse401
    | PollGoogleMapsResultsResponse402
    | PollGoogleMapsResultsResponse403
    | PollGoogleMapsResultsResponse404
    | PollGoogleMapsResultsResponse429
    | PollGoogleMapsResultsResponse500
    | PollGoogleMapsResultsResponse503
    | None
):
    """Poll for Google Maps results

     Poll for Google Maps results

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (PollGoogleMapsResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollGoogleMapsResultsResponse200 | PollGoogleMapsResultsResponse400 | PollGoogleMapsResultsResponse401 | PollGoogleMapsResultsResponse402 | PollGoogleMapsResultsResponse403 | PollGoogleMapsResultsResponse404 | PollGoogleMapsResultsResponse429 | PollGoogleMapsResultsResponse500 | PollGoogleMapsResultsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
