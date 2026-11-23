from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_profile_body import FacebookProfileBody
from ...models.facebook_profile_response_200 import FacebookProfileResponse200
from ...models.facebook_profile_response_400 import FacebookProfileResponse400
from ...models.facebook_profile_response_401 import FacebookProfileResponse401
from ...models.facebook_profile_response_402 import FacebookProfileResponse402
from ...models.facebook_profile_response_403 import FacebookProfileResponse403
from ...models.facebook_profile_response_404 import FacebookProfileResponse404
from ...models.facebook_profile_response_422 import FacebookProfileResponse422
from ...models.facebook_profile_response_429 import FacebookProfileResponse429
from ...models.facebook_profile_response_500 import FacebookProfileResponse500
from ...models.facebook_profile_response_503 import FacebookProfileResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookProfileBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/profile",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookProfileResponse200
    | FacebookProfileResponse400
    | FacebookProfileResponse401
    | FacebookProfileResponse402
    | FacebookProfileResponse403
    | FacebookProfileResponse404
    | FacebookProfileResponse422
    | FacebookProfileResponse429
    | FacebookProfileResponse500
    | FacebookProfileResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookProfileResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookProfileResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookProfileResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookProfileResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookProfileResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookProfileResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookProfileResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookProfileResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookProfileResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookProfileResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookProfileResponse200
    | FacebookProfileResponse400
    | FacebookProfileResponse401
    | FacebookProfileResponse402
    | FacebookProfileResponse403
    | FacebookProfileResponse404
    | FacebookProfileResponse422
    | FacebookProfileResponse429
    | FacebookProfileResponse500
    | FacebookProfileResponse503
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
    body: FacebookProfileBody,
) -> Response[
    FacebookProfileResponse200
    | FacebookProfileResponse400
    | FacebookProfileResponse401
    | FacebookProfileResponse402
    | FacebookProfileResponse403
    | FacebookProfileResponse404
    | FacebookProfileResponse422
    | FacebookProfileResponse429
    | FacebookProfileResponse500
    | FacebookProfileResponse503
]:
    """Fetch Facebook page or profile

     Fetches public info for a Facebook page or profile, including business and organization pages: name,
    category, follower and like counts, intro text, and any public contact details (email, phone,
    website, address) the page lists.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookProfileResponse200 | FacebookProfileResponse400 | FacebookProfileResponse401 | FacebookProfileResponse402 | FacebookProfileResponse403 | FacebookProfileResponse404 | FacebookProfileResponse422 | FacebookProfileResponse429 | FacebookProfileResponse500 | FacebookProfileResponse503]
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
    body: FacebookProfileBody,
) -> (
    FacebookProfileResponse200
    | FacebookProfileResponse400
    | FacebookProfileResponse401
    | FacebookProfileResponse402
    | FacebookProfileResponse403
    | FacebookProfileResponse404
    | FacebookProfileResponse422
    | FacebookProfileResponse429
    | FacebookProfileResponse500
    | FacebookProfileResponse503
    | None
):
    """Fetch Facebook page or profile

     Fetches public info for a Facebook page or profile, including business and organization pages: name,
    category, follower and like counts, intro text, and any public contact details (email, phone,
    website, address) the page lists.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookProfileResponse200 | FacebookProfileResponse400 | FacebookProfileResponse401 | FacebookProfileResponse402 | FacebookProfileResponse403 | FacebookProfileResponse404 | FacebookProfileResponse422 | FacebookProfileResponse429 | FacebookProfileResponse500 | FacebookProfileResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookProfileBody,
) -> Response[
    FacebookProfileResponse200
    | FacebookProfileResponse400
    | FacebookProfileResponse401
    | FacebookProfileResponse402
    | FacebookProfileResponse403
    | FacebookProfileResponse404
    | FacebookProfileResponse422
    | FacebookProfileResponse429
    | FacebookProfileResponse500
    | FacebookProfileResponse503
]:
    """Fetch Facebook page or profile

     Fetches public info for a Facebook page or profile, including business and organization pages: name,
    category, follower and like counts, intro text, and any public contact details (email, phone,
    website, address) the page lists.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookProfileResponse200 | FacebookProfileResponse400 | FacebookProfileResponse401 | FacebookProfileResponse402 | FacebookProfileResponse403 | FacebookProfileResponse404 | FacebookProfileResponse422 | FacebookProfileResponse429 | FacebookProfileResponse500 | FacebookProfileResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookProfileBody,
) -> (
    FacebookProfileResponse200
    | FacebookProfileResponse400
    | FacebookProfileResponse401
    | FacebookProfileResponse402
    | FacebookProfileResponse403
    | FacebookProfileResponse404
    | FacebookProfileResponse422
    | FacebookProfileResponse429
    | FacebookProfileResponse500
    | FacebookProfileResponse503
    | None
):
    """Fetch Facebook page or profile

     Fetches public info for a Facebook page or profile, including business and organization pages: name,
    category, follower and like counts, intro text, and any public contact details (email, phone,
    website, address) the page lists.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookProfileResponse200 | FacebookProfileResponse400 | FacebookProfileResponse401 | FacebookProfileResponse402 | FacebookProfileResponse403 | FacebookProfileResponse404 | FacebookProfileResponse422 | FacebookProfileResponse429 | FacebookProfileResponse500 | FacebookProfileResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
