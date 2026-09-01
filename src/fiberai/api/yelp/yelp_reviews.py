from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.yelp_reviews_body import YelpReviewsBody
from ...models.yelp_reviews_response_200 import YelpReviewsResponse200
from ...models.yelp_reviews_response_400 import YelpReviewsResponse400
from ...models.yelp_reviews_response_401 import YelpReviewsResponse401
from ...models.yelp_reviews_response_402 import YelpReviewsResponse402
from ...models.yelp_reviews_response_403 import YelpReviewsResponse403
from ...models.yelp_reviews_response_404 import YelpReviewsResponse404
from ...models.yelp_reviews_response_422 import YelpReviewsResponse422
from ...models.yelp_reviews_response_429 import YelpReviewsResponse429
from ...models.yelp_reviews_response_500 import YelpReviewsResponse500
from ...models.yelp_reviews_response_503 import YelpReviewsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: YelpReviewsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/yelp/reviews",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    YelpReviewsResponse200
    | YelpReviewsResponse400
    | YelpReviewsResponse401
    | YelpReviewsResponse402
    | YelpReviewsResponse403
    | YelpReviewsResponse404
    | YelpReviewsResponse422
    | YelpReviewsResponse429
    | YelpReviewsResponse500
    | YelpReviewsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = YelpReviewsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = YelpReviewsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = YelpReviewsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = YelpReviewsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = YelpReviewsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = YelpReviewsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = YelpReviewsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = YelpReviewsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = YelpReviewsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = YelpReviewsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    YelpReviewsResponse200
    | YelpReviewsResponse400
    | YelpReviewsResponse401
    | YelpReviewsResponse402
    | YelpReviewsResponse403
    | YelpReviewsResponse404
    | YelpReviewsResponse422
    | YelpReviewsResponse429
    | YelpReviewsResponse500
    | YelpReviewsResponse503
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
    body: YelpReviewsBody,
) -> Response[
    YelpReviewsResponse200
    | YelpReviewsResponse400
    | YelpReviewsResponse401
    | YelpReviewsResponse402
    | YelpReviewsResponse403
    | YelpReviewsResponse404
    | YelpReviewsResponse422
    | YelpReviewsResponse429
    | YelpReviewsResponse500
    | YelpReviewsResponse503
]:
    """Get Yelp business reviews

     Get reviews of a Yelp business, paginated, with reviewer details, ratings, and full review text.
    Obtain the business ID via the /yelp/search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per reviews page&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpReviewsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YelpReviewsResponse200 | YelpReviewsResponse400 | YelpReviewsResponse401 | YelpReviewsResponse402 | YelpReviewsResponse403 | YelpReviewsResponse404 | YelpReviewsResponse422 | YelpReviewsResponse429 | YelpReviewsResponse500 | YelpReviewsResponse503]
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
    body: YelpReviewsBody,
) -> (
    YelpReviewsResponse200
    | YelpReviewsResponse400
    | YelpReviewsResponse401
    | YelpReviewsResponse402
    | YelpReviewsResponse403
    | YelpReviewsResponse404
    | YelpReviewsResponse422
    | YelpReviewsResponse429
    | YelpReviewsResponse500
    | YelpReviewsResponse503
    | None
):
    """Get Yelp business reviews

     Get reviews of a Yelp business, paginated, with reviewer details, ratings, and full review text.
    Obtain the business ID via the /yelp/search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per reviews page&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpReviewsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YelpReviewsResponse200 | YelpReviewsResponse400 | YelpReviewsResponse401 | YelpReviewsResponse402 | YelpReviewsResponse403 | YelpReviewsResponse404 | YelpReviewsResponse422 | YelpReviewsResponse429 | YelpReviewsResponse500 | YelpReviewsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: YelpReviewsBody,
) -> Response[
    YelpReviewsResponse200
    | YelpReviewsResponse400
    | YelpReviewsResponse401
    | YelpReviewsResponse402
    | YelpReviewsResponse403
    | YelpReviewsResponse404
    | YelpReviewsResponse422
    | YelpReviewsResponse429
    | YelpReviewsResponse500
    | YelpReviewsResponse503
]:
    """Get Yelp business reviews

     Get reviews of a Yelp business, paginated, with reviewer details, ratings, and full review text.
    Obtain the business ID via the /yelp/search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per reviews page&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpReviewsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YelpReviewsResponse200 | YelpReviewsResponse400 | YelpReviewsResponse401 | YelpReviewsResponse402 | YelpReviewsResponse403 | YelpReviewsResponse404 | YelpReviewsResponse422 | YelpReviewsResponse429 | YelpReviewsResponse500 | YelpReviewsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: YelpReviewsBody,
) -> (
    YelpReviewsResponse200
    | YelpReviewsResponse400
    | YelpReviewsResponse401
    | YelpReviewsResponse402
    | YelpReviewsResponse403
    | YelpReviewsResponse404
    | YelpReviewsResponse422
    | YelpReviewsResponse429
    | YelpReviewsResponse500
    | YelpReviewsResponse503
    | None
):
    """Get Yelp business reviews

     Get reviews of a Yelp business, paginated, with reviewer details, ratings, and full review text.
    Obtain the business ID via the /yelp/search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per reviews page&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpReviewsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YelpReviewsResponse200 | YelpReviewsResponse400 | YelpReviewsResponse401 | YelpReviewsResponse402 | YelpReviewsResponse403 | YelpReviewsResponse404 | YelpReviewsResponse422 | YelpReviewsResponse429 | YelpReviewsResponse500 | YelpReviewsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
