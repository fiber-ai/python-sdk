from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.google_maps_search_body import GoogleMapsSearchBody
from ...models.google_maps_search_response_200 import GoogleMapsSearchResponse200
from ...models.google_maps_search_response_400 import GoogleMapsSearchResponse400
from ...models.google_maps_search_response_401 import GoogleMapsSearchResponse401
from ...models.google_maps_search_response_402 import GoogleMapsSearchResponse402
from ...models.google_maps_search_response_403 import GoogleMapsSearchResponse403
from ...models.google_maps_search_response_404 import GoogleMapsSearchResponse404
from ...models.google_maps_search_response_429 import GoogleMapsSearchResponse429
from ...models.google_maps_search_response_500 import GoogleMapsSearchResponse500
from ...models.google_maps_search_response_503 import GoogleMapsSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GoogleMapsSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/google-maps-search/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GoogleMapsSearchResponse200
    | GoogleMapsSearchResponse400
    | GoogleMapsSearchResponse401
    | GoogleMapsSearchResponse402
    | GoogleMapsSearchResponse403
    | GoogleMapsSearchResponse404
    | GoogleMapsSearchResponse429
    | GoogleMapsSearchResponse500
    | GoogleMapsSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GoogleMapsSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GoogleMapsSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GoogleMapsSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GoogleMapsSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GoogleMapsSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GoogleMapsSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GoogleMapsSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GoogleMapsSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GoogleMapsSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GoogleMapsSearchResponse200
    | GoogleMapsSearchResponse400
    | GoogleMapsSearchResponse401
    | GoogleMapsSearchResponse402
    | GoogleMapsSearchResponse403
    | GoogleMapsSearchResponse404
    | GoogleMapsSearchResponse429
    | GoogleMapsSearchResponse500
    | GoogleMapsSearchResponse503
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
    body: GoogleMapsSearchBody,
) -> Response[
    GoogleMapsSearchResponse200
    | GoogleMapsSearchResponse400
    | GoogleMapsSearchResponse401
    | GoogleMapsSearchResponse402
    | GoogleMapsSearchResponse403
    | GoogleMapsSearchResponse404
    | GoogleMapsSearchResponse429
    | GoogleMapsSearchResponse500
    | GoogleMapsSearchResponse503
]:
    r"""Start a search on Google Maps

     Start a search for local businesses or other places of interest on Google Maps

    <span>⚡ <strong>Rate limit:</strong> 5 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per business found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GoogleMapsSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleMapsSearchResponse200 | GoogleMapsSearchResponse400 | GoogleMapsSearchResponse401 | GoogleMapsSearchResponse402 | GoogleMapsSearchResponse403 | GoogleMapsSearchResponse404 | GoogleMapsSearchResponse429 | GoogleMapsSearchResponse500 | GoogleMapsSearchResponse503]
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
    body: GoogleMapsSearchBody,
) -> (
    GoogleMapsSearchResponse200
    | GoogleMapsSearchResponse400
    | GoogleMapsSearchResponse401
    | GoogleMapsSearchResponse402
    | GoogleMapsSearchResponse403
    | GoogleMapsSearchResponse404
    | GoogleMapsSearchResponse429
    | GoogleMapsSearchResponse500
    | GoogleMapsSearchResponse503
    | None
):
    r"""Start a search on Google Maps

     Start a search for local businesses or other places of interest on Google Maps

    <span>⚡ <strong>Rate limit:</strong> 5 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per business found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GoogleMapsSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleMapsSearchResponse200 | GoogleMapsSearchResponse400 | GoogleMapsSearchResponse401 | GoogleMapsSearchResponse402 | GoogleMapsSearchResponse403 | GoogleMapsSearchResponse404 | GoogleMapsSearchResponse429 | GoogleMapsSearchResponse500 | GoogleMapsSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GoogleMapsSearchBody,
) -> Response[
    GoogleMapsSearchResponse200
    | GoogleMapsSearchResponse400
    | GoogleMapsSearchResponse401
    | GoogleMapsSearchResponse402
    | GoogleMapsSearchResponse403
    | GoogleMapsSearchResponse404
    | GoogleMapsSearchResponse429
    | GoogleMapsSearchResponse500
    | GoogleMapsSearchResponse503
]:
    r"""Start a search on Google Maps

     Start a search for local businesses or other places of interest on Google Maps

    <span>⚡ <strong>Rate limit:</strong> 5 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per business found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GoogleMapsSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleMapsSearchResponse200 | GoogleMapsSearchResponse400 | GoogleMapsSearchResponse401 | GoogleMapsSearchResponse402 | GoogleMapsSearchResponse403 | GoogleMapsSearchResponse404 | GoogleMapsSearchResponse429 | GoogleMapsSearchResponse500 | GoogleMapsSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GoogleMapsSearchBody,
) -> (
    GoogleMapsSearchResponse200
    | GoogleMapsSearchResponse400
    | GoogleMapsSearchResponse401
    | GoogleMapsSearchResponse402
    | GoogleMapsSearchResponse403
    | GoogleMapsSearchResponse404
    | GoogleMapsSearchResponse429
    | GoogleMapsSearchResponse500
    | GoogleMapsSearchResponse503
    | None
):
    r"""Start a search on Google Maps

     Start a search for local businesses or other places of interest on Google Maps

    <span>⚡ <strong>Rate limit:</strong> 5 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per business found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GoogleMapsSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleMapsSearchResponse200 | GoogleMapsSearchResponse400 | GoogleMapsSearchResponse401 | GoogleMapsSearchResponse402 | GoogleMapsSearchResponse403 | GoogleMapsSearchResponse404 | GoogleMapsSearchResponse429 | GoogleMapsSearchResponse500 | GoogleMapsSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
