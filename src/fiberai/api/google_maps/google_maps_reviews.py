from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.google_maps_reviews_body import GoogleMapsReviewsBody
from ...models.google_maps_reviews_response_200 import GoogleMapsReviewsResponse200
from ...models.google_maps_reviews_response_400 import GoogleMapsReviewsResponse400
from ...models.google_maps_reviews_response_401 import GoogleMapsReviewsResponse401
from ...models.google_maps_reviews_response_402 import GoogleMapsReviewsResponse402
from ...models.google_maps_reviews_response_403 import GoogleMapsReviewsResponse403
from ...models.google_maps_reviews_response_404 import GoogleMapsReviewsResponse404
from ...models.google_maps_reviews_response_422 import GoogleMapsReviewsResponse422
from ...models.google_maps_reviews_response_429 import GoogleMapsReviewsResponse429
from ...models.google_maps_reviews_response_500 import GoogleMapsReviewsResponse500
from ...models.google_maps_reviews_response_503 import GoogleMapsReviewsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GoogleMapsReviewsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/google-maps/reviews",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GoogleMapsReviewsResponse200
    | GoogleMapsReviewsResponse400
    | GoogleMapsReviewsResponse401
    | GoogleMapsReviewsResponse402
    | GoogleMapsReviewsResponse403
    | GoogleMapsReviewsResponse404
    | GoogleMapsReviewsResponse422
    | GoogleMapsReviewsResponse429
    | GoogleMapsReviewsResponse500
    | GoogleMapsReviewsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GoogleMapsReviewsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GoogleMapsReviewsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GoogleMapsReviewsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GoogleMapsReviewsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GoogleMapsReviewsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GoogleMapsReviewsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GoogleMapsReviewsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GoogleMapsReviewsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GoogleMapsReviewsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GoogleMapsReviewsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GoogleMapsReviewsResponse200
    | GoogleMapsReviewsResponse400
    | GoogleMapsReviewsResponse401
    | GoogleMapsReviewsResponse402
    | GoogleMapsReviewsResponse403
    | GoogleMapsReviewsResponse404
    | GoogleMapsReviewsResponse422
    | GoogleMapsReviewsResponse429
    | GoogleMapsReviewsResponse500
    | GoogleMapsReviewsResponse503
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
    body: GoogleMapsReviewsBody,
) -> Response[
    GoogleMapsReviewsResponse200
    | GoogleMapsReviewsResponse400
    | GoogleMapsReviewsResponse401
    | GoogleMapsReviewsResponse402
    | GoogleMapsReviewsResponse403
    | GoogleMapsReviewsResponse404
    | GoogleMapsReviewsResponse422
    | GoogleMapsReviewsResponse429
    | GoogleMapsReviewsResponse500
    | GoogleMapsReviewsResponse503
]:
    """Get Google Maps place reviews

     Get reviews of a Google Maps place, paginated, with reviewer details, ratings, and full review text.
    Obtain the place ID via `POST /v1/google-maps/search`.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per reviews page&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GoogleMapsReviewsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleMapsReviewsResponse200 | GoogleMapsReviewsResponse400 | GoogleMapsReviewsResponse401 | GoogleMapsReviewsResponse402 | GoogleMapsReviewsResponse403 | GoogleMapsReviewsResponse404 | GoogleMapsReviewsResponse422 | GoogleMapsReviewsResponse429 | GoogleMapsReviewsResponse500 | GoogleMapsReviewsResponse503]
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
    body: GoogleMapsReviewsBody,
) -> (
    GoogleMapsReviewsResponse200
    | GoogleMapsReviewsResponse400
    | GoogleMapsReviewsResponse401
    | GoogleMapsReviewsResponse402
    | GoogleMapsReviewsResponse403
    | GoogleMapsReviewsResponse404
    | GoogleMapsReviewsResponse422
    | GoogleMapsReviewsResponse429
    | GoogleMapsReviewsResponse500
    | GoogleMapsReviewsResponse503
    | None
):
    """Get Google Maps place reviews

     Get reviews of a Google Maps place, paginated, with reviewer details, ratings, and full review text.
    Obtain the place ID via `POST /v1/google-maps/search`.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per reviews page&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GoogleMapsReviewsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleMapsReviewsResponse200 | GoogleMapsReviewsResponse400 | GoogleMapsReviewsResponse401 | GoogleMapsReviewsResponse402 | GoogleMapsReviewsResponse403 | GoogleMapsReviewsResponse404 | GoogleMapsReviewsResponse422 | GoogleMapsReviewsResponse429 | GoogleMapsReviewsResponse500 | GoogleMapsReviewsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GoogleMapsReviewsBody,
) -> Response[
    GoogleMapsReviewsResponse200
    | GoogleMapsReviewsResponse400
    | GoogleMapsReviewsResponse401
    | GoogleMapsReviewsResponse402
    | GoogleMapsReviewsResponse403
    | GoogleMapsReviewsResponse404
    | GoogleMapsReviewsResponse422
    | GoogleMapsReviewsResponse429
    | GoogleMapsReviewsResponse500
    | GoogleMapsReviewsResponse503
]:
    """Get Google Maps place reviews

     Get reviews of a Google Maps place, paginated, with reviewer details, ratings, and full review text.
    Obtain the place ID via `POST /v1/google-maps/search`.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per reviews page&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GoogleMapsReviewsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleMapsReviewsResponse200 | GoogleMapsReviewsResponse400 | GoogleMapsReviewsResponse401 | GoogleMapsReviewsResponse402 | GoogleMapsReviewsResponse403 | GoogleMapsReviewsResponse404 | GoogleMapsReviewsResponse422 | GoogleMapsReviewsResponse429 | GoogleMapsReviewsResponse500 | GoogleMapsReviewsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GoogleMapsReviewsBody,
) -> (
    GoogleMapsReviewsResponse200
    | GoogleMapsReviewsResponse400
    | GoogleMapsReviewsResponse401
    | GoogleMapsReviewsResponse402
    | GoogleMapsReviewsResponse403
    | GoogleMapsReviewsResponse404
    | GoogleMapsReviewsResponse422
    | GoogleMapsReviewsResponse429
    | GoogleMapsReviewsResponse500
    | GoogleMapsReviewsResponse503
    | None
):
    """Get Google Maps place reviews

     Get reviews of a Google Maps place, paginated, with reviewer details, ratings, and full review text.
    Obtain the place ID via `POST /v1/google-maps/search`.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per reviews page&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GoogleMapsReviewsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleMapsReviewsResponse200 | GoogleMapsReviewsResponse400 | GoogleMapsReviewsResponse401 | GoogleMapsReviewsResponse402 | GoogleMapsReviewsResponse403 | GoogleMapsReviewsResponse404 | GoogleMapsReviewsResponse422 | GoogleMapsReviewsResponse429 | GoogleMapsReviewsResponse500 | GoogleMapsReviewsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
