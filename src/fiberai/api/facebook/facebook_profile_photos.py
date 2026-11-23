from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_profile_photos_body import FacebookProfilePhotosBody
from ...models.facebook_profile_photos_response_200 import FacebookProfilePhotosResponse200
from ...models.facebook_profile_photos_response_400 import FacebookProfilePhotosResponse400
from ...models.facebook_profile_photos_response_401 import FacebookProfilePhotosResponse401
from ...models.facebook_profile_photos_response_402 import FacebookProfilePhotosResponse402
from ...models.facebook_profile_photos_response_403 import FacebookProfilePhotosResponse403
from ...models.facebook_profile_photos_response_404 import FacebookProfilePhotosResponse404
from ...models.facebook_profile_photos_response_422 import FacebookProfilePhotosResponse422
from ...models.facebook_profile_photos_response_429 import FacebookProfilePhotosResponse429
from ...models.facebook_profile_photos_response_500 import FacebookProfilePhotosResponse500
from ...models.facebook_profile_photos_response_503 import FacebookProfilePhotosResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookProfilePhotosBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/profile/photos",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookProfilePhotosResponse200
    | FacebookProfilePhotosResponse400
    | FacebookProfilePhotosResponse401
    | FacebookProfilePhotosResponse402
    | FacebookProfilePhotosResponse403
    | FacebookProfilePhotosResponse404
    | FacebookProfilePhotosResponse422
    | FacebookProfilePhotosResponse429
    | FacebookProfilePhotosResponse500
    | FacebookProfilePhotosResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookProfilePhotosResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookProfilePhotosResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookProfilePhotosResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookProfilePhotosResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookProfilePhotosResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookProfilePhotosResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookProfilePhotosResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookProfilePhotosResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookProfilePhotosResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookProfilePhotosResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookProfilePhotosResponse200
    | FacebookProfilePhotosResponse400
    | FacebookProfilePhotosResponse401
    | FacebookProfilePhotosResponse402
    | FacebookProfilePhotosResponse403
    | FacebookProfilePhotosResponse404
    | FacebookProfilePhotosResponse422
    | FacebookProfilePhotosResponse429
    | FacebookProfilePhotosResponse500
    | FacebookProfilePhotosResponse503
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
    body: FacebookProfilePhotosBody,
) -> Response[
    FacebookProfilePhotosResponse200
    | FacebookProfilePhotosResponse400
    | FacebookProfilePhotosResponse401
    | FacebookProfilePhotosResponse402
    | FacebookProfilePhotosResponse403
    | FacebookProfilePhotosResponse404
    | FacebookProfilePhotosResponse422
    | FacebookProfilePhotosResponse429
    | FacebookProfilePhotosResponse500
    | FacebookProfilePhotosResponse503
]:
    """Fetch Facebook page photos

     Fetches a page of photos from a public Facebook page or profile. Use the response's `nextPageToken`
    to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfilePhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookProfilePhotosResponse200 | FacebookProfilePhotosResponse400 | FacebookProfilePhotosResponse401 | FacebookProfilePhotosResponse402 | FacebookProfilePhotosResponse403 | FacebookProfilePhotosResponse404 | FacebookProfilePhotosResponse422 | FacebookProfilePhotosResponse429 | FacebookProfilePhotosResponse500 | FacebookProfilePhotosResponse503]
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
    body: FacebookProfilePhotosBody,
) -> (
    FacebookProfilePhotosResponse200
    | FacebookProfilePhotosResponse400
    | FacebookProfilePhotosResponse401
    | FacebookProfilePhotosResponse402
    | FacebookProfilePhotosResponse403
    | FacebookProfilePhotosResponse404
    | FacebookProfilePhotosResponse422
    | FacebookProfilePhotosResponse429
    | FacebookProfilePhotosResponse500
    | FacebookProfilePhotosResponse503
    | None
):
    """Fetch Facebook page photos

     Fetches a page of photos from a public Facebook page or profile. Use the response's `nextPageToken`
    to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfilePhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookProfilePhotosResponse200 | FacebookProfilePhotosResponse400 | FacebookProfilePhotosResponse401 | FacebookProfilePhotosResponse402 | FacebookProfilePhotosResponse403 | FacebookProfilePhotosResponse404 | FacebookProfilePhotosResponse422 | FacebookProfilePhotosResponse429 | FacebookProfilePhotosResponse500 | FacebookProfilePhotosResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookProfilePhotosBody,
) -> Response[
    FacebookProfilePhotosResponse200
    | FacebookProfilePhotosResponse400
    | FacebookProfilePhotosResponse401
    | FacebookProfilePhotosResponse402
    | FacebookProfilePhotosResponse403
    | FacebookProfilePhotosResponse404
    | FacebookProfilePhotosResponse422
    | FacebookProfilePhotosResponse429
    | FacebookProfilePhotosResponse500
    | FacebookProfilePhotosResponse503
]:
    """Fetch Facebook page photos

     Fetches a page of photos from a public Facebook page or profile. Use the response's `nextPageToken`
    to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfilePhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookProfilePhotosResponse200 | FacebookProfilePhotosResponse400 | FacebookProfilePhotosResponse401 | FacebookProfilePhotosResponse402 | FacebookProfilePhotosResponse403 | FacebookProfilePhotosResponse404 | FacebookProfilePhotosResponse422 | FacebookProfilePhotosResponse429 | FacebookProfilePhotosResponse500 | FacebookProfilePhotosResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookProfilePhotosBody,
) -> (
    FacebookProfilePhotosResponse200
    | FacebookProfilePhotosResponse400
    | FacebookProfilePhotosResponse401
    | FacebookProfilePhotosResponse402
    | FacebookProfilePhotosResponse403
    | FacebookProfilePhotosResponse404
    | FacebookProfilePhotosResponse422
    | FacebookProfilePhotosResponse429
    | FacebookProfilePhotosResponse500
    | FacebookProfilePhotosResponse503
    | None
):
    """Fetch Facebook page photos

     Fetches a page of photos from a public Facebook page or profile. Use the response's `nextPageToken`
    to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfilePhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookProfilePhotosResponse200 | FacebookProfilePhotosResponse400 | FacebookProfilePhotosResponse401 | FacebookProfilePhotosResponse402 | FacebookProfilePhotosResponse403 | FacebookProfilePhotosResponse404 | FacebookProfilePhotosResponse422 | FacebookProfilePhotosResponse429 | FacebookProfilePhotosResponse500 | FacebookProfilePhotosResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
