from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_google_maps_results_body import CheckGoogleMapsResultsBody
from ...models.check_google_maps_results_response_200 import CheckGoogleMapsResultsResponse200
from ...models.check_google_maps_results_response_400 import CheckGoogleMapsResultsResponse400
from ...models.check_google_maps_results_response_401 import CheckGoogleMapsResultsResponse401
from ...models.check_google_maps_results_response_402 import CheckGoogleMapsResultsResponse402
from ...models.check_google_maps_results_response_403 import CheckGoogleMapsResultsResponse403
from ...models.check_google_maps_results_response_404 import CheckGoogleMapsResultsResponse404
from ...models.check_google_maps_results_response_429 import CheckGoogleMapsResultsResponse429
from ...models.check_google_maps_results_response_500 import CheckGoogleMapsResultsResponse500
from ...models.check_google_maps_results_response_503 import CheckGoogleMapsResultsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CheckGoogleMapsResultsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/google-maps-search/check",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CheckGoogleMapsResultsResponse200
    | CheckGoogleMapsResultsResponse400
    | CheckGoogleMapsResultsResponse401
    | CheckGoogleMapsResultsResponse402
    | CheckGoogleMapsResultsResponse403
    | CheckGoogleMapsResultsResponse404
    | CheckGoogleMapsResultsResponse429
    | CheckGoogleMapsResultsResponse500
    | CheckGoogleMapsResultsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CheckGoogleMapsResultsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CheckGoogleMapsResultsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CheckGoogleMapsResultsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CheckGoogleMapsResultsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CheckGoogleMapsResultsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CheckGoogleMapsResultsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CheckGoogleMapsResultsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CheckGoogleMapsResultsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CheckGoogleMapsResultsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CheckGoogleMapsResultsResponse200
    | CheckGoogleMapsResultsResponse400
    | CheckGoogleMapsResultsResponse401
    | CheckGoogleMapsResultsResponse402
    | CheckGoogleMapsResultsResponse403
    | CheckGoogleMapsResultsResponse404
    | CheckGoogleMapsResultsResponse429
    | CheckGoogleMapsResultsResponse500
    | CheckGoogleMapsResultsResponse503
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
    body: CheckGoogleMapsResultsBody,
) -> Response[
    CheckGoogleMapsResultsResponse200
    | CheckGoogleMapsResultsResponse400
    | CheckGoogleMapsResultsResponse401
    | CheckGoogleMapsResultsResponse402
    | CheckGoogleMapsResultsResponse403
    | CheckGoogleMapsResultsResponse404
    | CheckGoogleMapsResultsResponse429
    | CheckGoogleMapsResultsResponse500
    | CheckGoogleMapsResultsResponse503
]:
    """Check progress for Google Maps results

     Check progress for Google Maps results

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (CheckGoogleMapsResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckGoogleMapsResultsResponse200 | CheckGoogleMapsResultsResponse400 | CheckGoogleMapsResultsResponse401 | CheckGoogleMapsResultsResponse402 | CheckGoogleMapsResultsResponse403 | CheckGoogleMapsResultsResponse404 | CheckGoogleMapsResultsResponse429 | CheckGoogleMapsResultsResponse500 | CheckGoogleMapsResultsResponse503]
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
    body: CheckGoogleMapsResultsBody,
) -> (
    CheckGoogleMapsResultsResponse200
    | CheckGoogleMapsResultsResponse400
    | CheckGoogleMapsResultsResponse401
    | CheckGoogleMapsResultsResponse402
    | CheckGoogleMapsResultsResponse403
    | CheckGoogleMapsResultsResponse404
    | CheckGoogleMapsResultsResponse429
    | CheckGoogleMapsResultsResponse500
    | CheckGoogleMapsResultsResponse503
    | None
):
    """Check progress for Google Maps results

     Check progress for Google Maps results

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (CheckGoogleMapsResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckGoogleMapsResultsResponse200 | CheckGoogleMapsResultsResponse400 | CheckGoogleMapsResultsResponse401 | CheckGoogleMapsResultsResponse402 | CheckGoogleMapsResultsResponse403 | CheckGoogleMapsResultsResponse404 | CheckGoogleMapsResultsResponse429 | CheckGoogleMapsResultsResponse500 | CheckGoogleMapsResultsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckGoogleMapsResultsBody,
) -> Response[
    CheckGoogleMapsResultsResponse200
    | CheckGoogleMapsResultsResponse400
    | CheckGoogleMapsResultsResponse401
    | CheckGoogleMapsResultsResponse402
    | CheckGoogleMapsResultsResponse403
    | CheckGoogleMapsResultsResponse404
    | CheckGoogleMapsResultsResponse429
    | CheckGoogleMapsResultsResponse500
    | CheckGoogleMapsResultsResponse503
]:
    """Check progress for Google Maps results

     Check progress for Google Maps results

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (CheckGoogleMapsResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckGoogleMapsResultsResponse200 | CheckGoogleMapsResultsResponse400 | CheckGoogleMapsResultsResponse401 | CheckGoogleMapsResultsResponse402 | CheckGoogleMapsResultsResponse403 | CheckGoogleMapsResultsResponse404 | CheckGoogleMapsResultsResponse429 | CheckGoogleMapsResultsResponse500 | CheckGoogleMapsResultsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CheckGoogleMapsResultsBody,
) -> (
    CheckGoogleMapsResultsResponse200
    | CheckGoogleMapsResultsResponse400
    | CheckGoogleMapsResultsResponse401
    | CheckGoogleMapsResultsResponse402
    | CheckGoogleMapsResultsResponse403
    | CheckGoogleMapsResultsResponse404
    | CheckGoogleMapsResultsResponse429
    | CheckGoogleMapsResultsResponse500
    | CheckGoogleMapsResultsResponse503
    | None
):
    """Check progress for Google Maps results

     Check progress for Google Maps results

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (CheckGoogleMapsResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckGoogleMapsResultsResponse200 | CheckGoogleMapsResultsResponse400 | CheckGoogleMapsResultsResponse401 | CheckGoogleMapsResultsResponse402 | CheckGoogleMapsResultsResponse403 | CheckGoogleMapsResultsResponse404 | CheckGoogleMapsResultsResponse429 | CheckGoogleMapsResultsResponse500 | CheckGoogleMapsResultsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
