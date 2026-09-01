from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.yelp_place_body import YelpPlaceBody
from ...models.yelp_place_response_200 import YelpPlaceResponse200
from ...models.yelp_place_response_400 import YelpPlaceResponse400
from ...models.yelp_place_response_401 import YelpPlaceResponse401
from ...models.yelp_place_response_402 import YelpPlaceResponse402
from ...models.yelp_place_response_403 import YelpPlaceResponse403
from ...models.yelp_place_response_404 import YelpPlaceResponse404
from ...models.yelp_place_response_422 import YelpPlaceResponse422
from ...models.yelp_place_response_429 import YelpPlaceResponse429
from ...models.yelp_place_response_500 import YelpPlaceResponse500
from ...models.yelp_place_response_503 import YelpPlaceResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: YelpPlaceBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/yelp/place",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    YelpPlaceResponse200
    | YelpPlaceResponse400
    | YelpPlaceResponse401
    | YelpPlaceResponse402
    | YelpPlaceResponse403
    | YelpPlaceResponse404
    | YelpPlaceResponse422
    | YelpPlaceResponse429
    | YelpPlaceResponse500
    | YelpPlaceResponse503
    | None
):
    if response.status_code == 200:
        response_200 = YelpPlaceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = YelpPlaceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = YelpPlaceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = YelpPlaceResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = YelpPlaceResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = YelpPlaceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = YelpPlaceResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = YelpPlaceResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = YelpPlaceResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = YelpPlaceResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    YelpPlaceResponse200
    | YelpPlaceResponse400
    | YelpPlaceResponse401
    | YelpPlaceResponse402
    | YelpPlaceResponse403
    | YelpPlaceResponse404
    | YelpPlaceResponse422
    | YelpPlaceResponse429
    | YelpPlaceResponse500
    | YelpPlaceResponse503
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
    body: YelpPlaceBody,
) -> Response[
    YelpPlaceResponse200
    | YelpPlaceResponse400
    | YelpPlaceResponse401
    | YelpPlaceResponse402
    | YelpPlaceResponse403
    | YelpPlaceResponse404
    | YelpPlaceResponse422
    | YelpPlaceResponse429
    | YelpPlaceResponse500
    | YelpPlaceResponse503
]:
    """Get a Yelp business page

     Get detailed information about a Yelp Place. Search for Yelp places via /yelp/search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per business page&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpPlaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YelpPlaceResponse200 | YelpPlaceResponse400 | YelpPlaceResponse401 | YelpPlaceResponse402 | YelpPlaceResponse403 | YelpPlaceResponse404 | YelpPlaceResponse422 | YelpPlaceResponse429 | YelpPlaceResponse500 | YelpPlaceResponse503]
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
    body: YelpPlaceBody,
) -> (
    YelpPlaceResponse200
    | YelpPlaceResponse400
    | YelpPlaceResponse401
    | YelpPlaceResponse402
    | YelpPlaceResponse403
    | YelpPlaceResponse404
    | YelpPlaceResponse422
    | YelpPlaceResponse429
    | YelpPlaceResponse500
    | YelpPlaceResponse503
    | None
):
    """Get a Yelp business page

     Get detailed information about a Yelp Place. Search for Yelp places via /yelp/search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per business page&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpPlaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YelpPlaceResponse200 | YelpPlaceResponse400 | YelpPlaceResponse401 | YelpPlaceResponse402 | YelpPlaceResponse403 | YelpPlaceResponse404 | YelpPlaceResponse422 | YelpPlaceResponse429 | YelpPlaceResponse500 | YelpPlaceResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: YelpPlaceBody,
) -> Response[
    YelpPlaceResponse200
    | YelpPlaceResponse400
    | YelpPlaceResponse401
    | YelpPlaceResponse402
    | YelpPlaceResponse403
    | YelpPlaceResponse404
    | YelpPlaceResponse422
    | YelpPlaceResponse429
    | YelpPlaceResponse500
    | YelpPlaceResponse503
]:
    """Get a Yelp business page

     Get detailed information about a Yelp Place. Search for Yelp places via /yelp/search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per business page&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpPlaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[YelpPlaceResponse200 | YelpPlaceResponse400 | YelpPlaceResponse401 | YelpPlaceResponse402 | YelpPlaceResponse403 | YelpPlaceResponse404 | YelpPlaceResponse422 | YelpPlaceResponse429 | YelpPlaceResponse500 | YelpPlaceResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: YelpPlaceBody,
) -> (
    YelpPlaceResponse200
    | YelpPlaceResponse400
    | YelpPlaceResponse401
    | YelpPlaceResponse402
    | YelpPlaceResponse403
    | YelpPlaceResponse404
    | YelpPlaceResponse422
    | YelpPlaceResponse429
    | YelpPlaceResponse500
    | YelpPlaceResponse503
    | None
):
    """Get a Yelp business page

     Get detailed information about a Yelp Place. Search for Yelp places via /yelp/search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per business page&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (YelpPlaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        YelpPlaceResponse200 | YelpPlaceResponse400 | YelpPlaceResponse401 | YelpPlaceResponse402 | YelpPlaceResponse403 | YelpPlaceResponse404 | YelpPlaceResponse422 | YelpPlaceResponse429 | YelpPlaceResponse500 | YelpPlaceResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
