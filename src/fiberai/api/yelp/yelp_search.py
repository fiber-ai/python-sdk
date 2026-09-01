from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.yelp_search_body import YelpSearchBody
from ...models.yelp_search_response_200 import YelpSearchResponse200
from ...models.yelp_search_response_400 import YelpSearchResponse400
from ...models.yelp_search_response_401 import YelpSearchResponse401
from ...models.yelp_search_response_402 import YelpSearchResponse402
from ...models.yelp_search_response_403 import YelpSearchResponse403
from ...models.yelp_search_response_404 import YelpSearchResponse404
from ...models.yelp_search_response_422 import YelpSearchResponse422
from ...models.yelp_search_response_429 import YelpSearchResponse429
from ...models.yelp_search_response_500 import YelpSearchResponse500
from ...models.yelp_search_response_503 import YelpSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: YelpSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/yelp/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    YelpSearchResponse200
    | YelpSearchResponse400
    | YelpSearchResponse401
    | YelpSearchResponse402
    | YelpSearchResponse403
    | YelpSearchResponse404
    | YelpSearchResponse422
    | YelpSearchResponse429
    | YelpSearchResponse500
    | YelpSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = YelpSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = YelpSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = YelpSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = YelpSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = YelpSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = YelpSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = YelpSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = YelpSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = YelpSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = YelpSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    YelpSearchResponse200
    | YelpSearchResponse400
    | YelpSearchResponse401
    | YelpSearchResponse402
    | YelpSearchResponse403
    | YelpSearchResponse404
    | YelpSearchResponse422
    | YelpSearchResponse429
    | YelpSearchResponse500
    | YelpSearchResponse503
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
    body: YelpSearchBody,
) -> Response[
    YelpSearchResponse200
    | YelpSearchResponse400
    | YelpSearchResponse401
    | YelpSearchResponse402
    | YelpSearchResponse403
    | YelpSearchResponse404
    | YelpSearchResponse422
    | YelpSearchResponse429
    | YelpSearchResponse500
    | YelpSearchResponse503
]:
    """Search Yelp businesses

     Searches Yelp for businesses matching a query in a location, and returns matching businesses with
    ratings, review counts, and contact details.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YelpSearchResponse200 | YelpSearchResponse400 | YelpSearchResponse401 | YelpSearchResponse402 | YelpSearchResponse403 | YelpSearchResponse404 | YelpSearchResponse422 | YelpSearchResponse429 | YelpSearchResponse500 | YelpSearchResponse503]
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
    body: YelpSearchBody,
) -> (
    YelpSearchResponse200
    | YelpSearchResponse400
    | YelpSearchResponse401
    | YelpSearchResponse402
    | YelpSearchResponse403
    | YelpSearchResponse404
    | YelpSearchResponse422
    | YelpSearchResponse429
    | YelpSearchResponse500
    | YelpSearchResponse503
    | None
):
    """Search Yelp businesses

     Searches Yelp for businesses matching a query in a location, and returns matching businesses with
    ratings, review counts, and contact details.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YelpSearchResponse200 | YelpSearchResponse400 | YelpSearchResponse401 | YelpSearchResponse402 | YelpSearchResponse403 | YelpSearchResponse404 | YelpSearchResponse422 | YelpSearchResponse429 | YelpSearchResponse500 | YelpSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: YelpSearchBody,
) -> Response[
    YelpSearchResponse200
    | YelpSearchResponse400
    | YelpSearchResponse401
    | YelpSearchResponse402
    | YelpSearchResponse403
    | YelpSearchResponse404
    | YelpSearchResponse422
    | YelpSearchResponse429
    | YelpSearchResponse500
    | YelpSearchResponse503
]:
    """Search Yelp businesses

     Searches Yelp for businesses matching a query in a location, and returns matching businesses with
    ratings, review counts, and contact details.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YelpSearchResponse200 | YelpSearchResponse400 | YelpSearchResponse401 | YelpSearchResponse402 | YelpSearchResponse403 | YelpSearchResponse404 | YelpSearchResponse422 | YelpSearchResponse429 | YelpSearchResponse500 | YelpSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: YelpSearchBody,
) -> (
    YelpSearchResponse200
    | YelpSearchResponse400
    | YelpSearchResponse401
    | YelpSearchResponse402
    | YelpSearchResponse403
    | YelpSearchResponse404
    | YelpSearchResponse422
    | YelpSearchResponse429
    | YelpSearchResponse500
    | YelpSearchResponse503
    | None
):
    """Search Yelp businesses

     Searches Yelp for businesses matching a query in a location, and returns matching businesses with
    ratings, review counts, and contact details.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YelpSearchResponse200 | YelpSearchResponse400 | YelpSearchResponse401 | YelpSearchResponse402 | YelpSearchResponse403 | YelpSearchResponse404 | YelpSearchResponse422 | YelpSearchResponse429 | YelpSearchResponse500 | YelpSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
