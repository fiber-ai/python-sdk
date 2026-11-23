from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_post_details_body import FacebookPostDetailsBody
from ...models.facebook_post_details_response_200 import FacebookPostDetailsResponse200
from ...models.facebook_post_details_response_400 import FacebookPostDetailsResponse400
from ...models.facebook_post_details_response_401 import FacebookPostDetailsResponse401
from ...models.facebook_post_details_response_402 import FacebookPostDetailsResponse402
from ...models.facebook_post_details_response_403 import FacebookPostDetailsResponse403
from ...models.facebook_post_details_response_404 import FacebookPostDetailsResponse404
from ...models.facebook_post_details_response_422 import FacebookPostDetailsResponse422
from ...models.facebook_post_details_response_429 import FacebookPostDetailsResponse429
from ...models.facebook_post_details_response_500 import FacebookPostDetailsResponse500
from ...models.facebook_post_details_response_503 import FacebookPostDetailsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookPostDetailsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/post/details",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookPostDetailsResponse200
    | FacebookPostDetailsResponse400
    | FacebookPostDetailsResponse401
    | FacebookPostDetailsResponse402
    | FacebookPostDetailsResponse403
    | FacebookPostDetailsResponse404
    | FacebookPostDetailsResponse422
    | FacebookPostDetailsResponse429
    | FacebookPostDetailsResponse500
    | FacebookPostDetailsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookPostDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookPostDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookPostDetailsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookPostDetailsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookPostDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookPostDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookPostDetailsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookPostDetailsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookPostDetailsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookPostDetailsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookPostDetailsResponse200
    | FacebookPostDetailsResponse400
    | FacebookPostDetailsResponse401
    | FacebookPostDetailsResponse402
    | FacebookPostDetailsResponse403
    | FacebookPostDetailsResponse404
    | FacebookPostDetailsResponse422
    | FacebookPostDetailsResponse429
    | FacebookPostDetailsResponse500
    | FacebookPostDetailsResponse503
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
    body: FacebookPostDetailsBody,
) -> Response[
    FacebookPostDetailsResponse200
    | FacebookPostDetailsResponse400
    | FacebookPostDetailsResponse401
    | FacebookPostDetailsResponse402
    | FacebookPostDetailsResponse403
    | FacebookPostDetailsResponse404
    | FacebookPostDetailsResponse422
    | FacebookPostDetailsResponse429
    | FacebookPostDetailsResponse500
    | FacebookPostDetailsResponse503
]:
    """Fetch Facebook post

     Fetches a single public Facebook post or Reel, including its text, media, engagement counts, and the
    feedback ID used to fetch its comments quickly.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookPostDetailsResponse200 | FacebookPostDetailsResponse400 | FacebookPostDetailsResponse401 | FacebookPostDetailsResponse402 | FacebookPostDetailsResponse403 | FacebookPostDetailsResponse404 | FacebookPostDetailsResponse422 | FacebookPostDetailsResponse429 | FacebookPostDetailsResponse500 | FacebookPostDetailsResponse503]
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
    body: FacebookPostDetailsBody,
) -> (
    FacebookPostDetailsResponse200
    | FacebookPostDetailsResponse400
    | FacebookPostDetailsResponse401
    | FacebookPostDetailsResponse402
    | FacebookPostDetailsResponse403
    | FacebookPostDetailsResponse404
    | FacebookPostDetailsResponse422
    | FacebookPostDetailsResponse429
    | FacebookPostDetailsResponse500
    | FacebookPostDetailsResponse503
    | None
):
    """Fetch Facebook post

     Fetches a single public Facebook post or Reel, including its text, media, engagement counts, and the
    feedback ID used to fetch its comments quickly.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookPostDetailsResponse200 | FacebookPostDetailsResponse400 | FacebookPostDetailsResponse401 | FacebookPostDetailsResponse402 | FacebookPostDetailsResponse403 | FacebookPostDetailsResponse404 | FacebookPostDetailsResponse422 | FacebookPostDetailsResponse429 | FacebookPostDetailsResponse500 | FacebookPostDetailsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookPostDetailsBody,
) -> Response[
    FacebookPostDetailsResponse200
    | FacebookPostDetailsResponse400
    | FacebookPostDetailsResponse401
    | FacebookPostDetailsResponse402
    | FacebookPostDetailsResponse403
    | FacebookPostDetailsResponse404
    | FacebookPostDetailsResponse422
    | FacebookPostDetailsResponse429
    | FacebookPostDetailsResponse500
    | FacebookPostDetailsResponse503
]:
    """Fetch Facebook post

     Fetches a single public Facebook post or Reel, including its text, media, engagement counts, and the
    feedback ID used to fetch its comments quickly.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookPostDetailsResponse200 | FacebookPostDetailsResponse400 | FacebookPostDetailsResponse401 | FacebookPostDetailsResponse402 | FacebookPostDetailsResponse403 | FacebookPostDetailsResponse404 | FacebookPostDetailsResponse422 | FacebookPostDetailsResponse429 | FacebookPostDetailsResponse500 | FacebookPostDetailsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookPostDetailsBody,
) -> (
    FacebookPostDetailsResponse200
    | FacebookPostDetailsResponse400
    | FacebookPostDetailsResponse401
    | FacebookPostDetailsResponse402
    | FacebookPostDetailsResponse403
    | FacebookPostDetailsResponse404
    | FacebookPostDetailsResponse422
    | FacebookPostDetailsResponse429
    | FacebookPostDetailsResponse500
    | FacebookPostDetailsResponse503
    | None
):
    """Fetch Facebook post

     Fetches a single public Facebook post or Reel, including its text, media, engagement counts, and the
    feedback ID used to fetch its comments quickly.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookPostDetailsResponse200 | FacebookPostDetailsResponse400 | FacebookPostDetailsResponse401 | FacebookPostDetailsResponse402 | FacebookPostDetailsResponse403 | FacebookPostDetailsResponse404 | FacebookPostDetailsResponse422 | FacebookPostDetailsResponse429 | FacebookPostDetailsResponse500 | FacebookPostDetailsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
