from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.social_media_lookup_polling_body import SocialMediaLookupPollingBody
from ...models.social_media_lookup_polling_response_200 import SocialMediaLookupPollingResponse200
from ...models.social_media_lookup_polling_response_400 import SocialMediaLookupPollingResponse400
from ...models.social_media_lookup_polling_response_401 import SocialMediaLookupPollingResponse401
from ...models.social_media_lookup_polling_response_402 import SocialMediaLookupPollingResponse402
from ...models.social_media_lookup_polling_response_403 import SocialMediaLookupPollingResponse403
from ...models.social_media_lookup_polling_response_404 import SocialMediaLookupPollingResponse404
from ...models.social_media_lookup_polling_response_429 import SocialMediaLookupPollingResponse429
from ...models.social_media_lookup_polling_response_500 import SocialMediaLookupPollingResponse500
from ...models.social_media_lookup_polling_response_503 import SocialMediaLookupPollingResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SocialMediaLookupPollingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/social-media-lookup/polling",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SocialMediaLookupPollingResponse200
    | SocialMediaLookupPollingResponse400
    | SocialMediaLookupPollingResponse401
    | SocialMediaLookupPollingResponse402
    | SocialMediaLookupPollingResponse403
    | SocialMediaLookupPollingResponse404
    | SocialMediaLookupPollingResponse429
    | SocialMediaLookupPollingResponse500
    | SocialMediaLookupPollingResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SocialMediaLookupPollingResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SocialMediaLookupPollingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SocialMediaLookupPollingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SocialMediaLookupPollingResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SocialMediaLookupPollingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SocialMediaLookupPollingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = SocialMediaLookupPollingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SocialMediaLookupPollingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SocialMediaLookupPollingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SocialMediaLookupPollingResponse200
    | SocialMediaLookupPollingResponse400
    | SocialMediaLookupPollingResponse401
    | SocialMediaLookupPollingResponse402
    | SocialMediaLookupPollingResponse403
    | SocialMediaLookupPollingResponse404
    | SocialMediaLookupPollingResponse429
    | SocialMediaLookupPollingResponse500
    | SocialMediaLookupPollingResponse503
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
    body: SocialMediaLookupPollingBody,
) -> Response[
    SocialMediaLookupPollingResponse200
    | SocialMediaLookupPollingResponse400
    | SocialMediaLookupPollingResponse401
    | SocialMediaLookupPollingResponse402
    | SocialMediaLookupPollingResponse403
    | SocialMediaLookupPollingResponse404
    | SocialMediaLookupPollingResponse429
    | SocialMediaLookupPollingResponse500
    | SocialMediaLookupPollingResponse503
]:
    """Poll social media lookup

     Poll for the results of a social media lookup task.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (SocialMediaLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialMediaLookupPollingResponse200 | SocialMediaLookupPollingResponse400 | SocialMediaLookupPollingResponse401 | SocialMediaLookupPollingResponse402 | SocialMediaLookupPollingResponse403 | SocialMediaLookupPollingResponse404 | SocialMediaLookupPollingResponse429 | SocialMediaLookupPollingResponse500 | SocialMediaLookupPollingResponse503]
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
    body: SocialMediaLookupPollingBody,
) -> (
    SocialMediaLookupPollingResponse200
    | SocialMediaLookupPollingResponse400
    | SocialMediaLookupPollingResponse401
    | SocialMediaLookupPollingResponse402
    | SocialMediaLookupPollingResponse403
    | SocialMediaLookupPollingResponse404
    | SocialMediaLookupPollingResponse429
    | SocialMediaLookupPollingResponse500
    | SocialMediaLookupPollingResponse503
    | None
):
    """Poll social media lookup

     Poll for the results of a social media lookup task.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (SocialMediaLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialMediaLookupPollingResponse200 | SocialMediaLookupPollingResponse400 | SocialMediaLookupPollingResponse401 | SocialMediaLookupPollingResponse402 | SocialMediaLookupPollingResponse403 | SocialMediaLookupPollingResponse404 | SocialMediaLookupPollingResponse429 | SocialMediaLookupPollingResponse500 | SocialMediaLookupPollingResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SocialMediaLookupPollingBody,
) -> Response[
    SocialMediaLookupPollingResponse200
    | SocialMediaLookupPollingResponse400
    | SocialMediaLookupPollingResponse401
    | SocialMediaLookupPollingResponse402
    | SocialMediaLookupPollingResponse403
    | SocialMediaLookupPollingResponse404
    | SocialMediaLookupPollingResponse429
    | SocialMediaLookupPollingResponse500
    | SocialMediaLookupPollingResponse503
]:
    """Poll social media lookup

     Poll for the results of a social media lookup task.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (SocialMediaLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialMediaLookupPollingResponse200 | SocialMediaLookupPollingResponse400 | SocialMediaLookupPollingResponse401 | SocialMediaLookupPollingResponse402 | SocialMediaLookupPollingResponse403 | SocialMediaLookupPollingResponse404 | SocialMediaLookupPollingResponse429 | SocialMediaLookupPollingResponse500 | SocialMediaLookupPollingResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SocialMediaLookupPollingBody,
) -> (
    SocialMediaLookupPollingResponse200
    | SocialMediaLookupPollingResponse400
    | SocialMediaLookupPollingResponse401
    | SocialMediaLookupPollingResponse402
    | SocialMediaLookupPollingResponse403
    | SocialMediaLookupPollingResponse404
    | SocialMediaLookupPollingResponse429
    | SocialMediaLookupPollingResponse500
    | SocialMediaLookupPollingResponse503
    | None
):
    """Poll social media lookup

     Poll for the results of a social media lookup task.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (SocialMediaLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialMediaLookupPollingResponse200 | SocialMediaLookupPollingResponse400 | SocialMediaLookupPollingResponse401 | SocialMediaLookupPollingResponse402 | SocialMediaLookupPollingResponse403 | SocialMediaLookupPollingResponse404 | SocialMediaLookupPollingResponse429 | SocialMediaLookupPollingResponse500 | SocialMediaLookupPollingResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
