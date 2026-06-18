from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.social_media_lookup_batch_polling_body import SocialMediaLookupBatchPollingBody
from ...models.social_media_lookup_batch_polling_response_200 import SocialMediaLookupBatchPollingResponse200
from ...models.social_media_lookup_batch_polling_response_400 import SocialMediaLookupBatchPollingResponse400
from ...models.social_media_lookup_batch_polling_response_401 import SocialMediaLookupBatchPollingResponse401
from ...models.social_media_lookup_batch_polling_response_402 import SocialMediaLookupBatchPollingResponse402
from ...models.social_media_lookup_batch_polling_response_403 import SocialMediaLookupBatchPollingResponse403
from ...models.social_media_lookup_batch_polling_response_404 import SocialMediaLookupBatchPollingResponse404
from ...models.social_media_lookup_batch_polling_response_422 import SocialMediaLookupBatchPollingResponse422
from ...models.social_media_lookup_batch_polling_response_429 import SocialMediaLookupBatchPollingResponse429
from ...models.social_media_lookup_batch_polling_response_500 import SocialMediaLookupBatchPollingResponse500
from ...models.social_media_lookup_batch_polling_response_503 import SocialMediaLookupBatchPollingResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SocialMediaLookupBatchPollingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/social-media-lookup/batch/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SocialMediaLookupBatchPollingResponse200
    | SocialMediaLookupBatchPollingResponse400
    | SocialMediaLookupBatchPollingResponse401
    | SocialMediaLookupBatchPollingResponse402
    | SocialMediaLookupBatchPollingResponse403
    | SocialMediaLookupBatchPollingResponse404
    | SocialMediaLookupBatchPollingResponse422
    | SocialMediaLookupBatchPollingResponse429
    | SocialMediaLookupBatchPollingResponse500
    | SocialMediaLookupBatchPollingResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SocialMediaLookupBatchPollingResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SocialMediaLookupBatchPollingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SocialMediaLookupBatchPollingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SocialMediaLookupBatchPollingResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SocialMediaLookupBatchPollingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SocialMediaLookupBatchPollingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = SocialMediaLookupBatchPollingResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = SocialMediaLookupBatchPollingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SocialMediaLookupBatchPollingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SocialMediaLookupBatchPollingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SocialMediaLookupBatchPollingResponse200
    | SocialMediaLookupBatchPollingResponse400
    | SocialMediaLookupBatchPollingResponse401
    | SocialMediaLookupBatchPollingResponse402
    | SocialMediaLookupBatchPollingResponse403
    | SocialMediaLookupBatchPollingResponse404
    | SocialMediaLookupBatchPollingResponse422
    | SocialMediaLookupBatchPollingResponse429
    | SocialMediaLookupBatchPollingResponse500
    | SocialMediaLookupBatchPollingResponse503
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
    body: SocialMediaLookupBatchPollingBody,
) -> Response[
    SocialMediaLookupBatchPollingResponse200
    | SocialMediaLookupBatchPollingResponse400
    | SocialMediaLookupBatchPollingResponse401
    | SocialMediaLookupBatchPollingResponse402
    | SocialMediaLookupBatchPollingResponse403
    | SocialMediaLookupBatchPollingResponse404
    | SocialMediaLookupBatchPollingResponse422
    | SocialMediaLookupBatchPollingResponse429
    | SocialMediaLookupBatchPollingResponse500
    | SocialMediaLookupBatchPollingResponse503
]:
    """Poll batch social media lookup

     Poll for the results of a batch social media lookup. Returns partial results as they become
    available, with overall progress statistics.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    Args:
        body (SocialMediaLookupBatchPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialMediaLookupBatchPollingResponse200 | SocialMediaLookupBatchPollingResponse400 | SocialMediaLookupBatchPollingResponse401 | SocialMediaLookupBatchPollingResponse402 | SocialMediaLookupBatchPollingResponse403 | SocialMediaLookupBatchPollingResponse404 | SocialMediaLookupBatchPollingResponse422 | SocialMediaLookupBatchPollingResponse429 | SocialMediaLookupBatchPollingResponse500 | SocialMediaLookupBatchPollingResponse503]
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
    body: SocialMediaLookupBatchPollingBody,
) -> (
    SocialMediaLookupBatchPollingResponse200
    | SocialMediaLookupBatchPollingResponse400
    | SocialMediaLookupBatchPollingResponse401
    | SocialMediaLookupBatchPollingResponse402
    | SocialMediaLookupBatchPollingResponse403
    | SocialMediaLookupBatchPollingResponse404
    | SocialMediaLookupBatchPollingResponse422
    | SocialMediaLookupBatchPollingResponse429
    | SocialMediaLookupBatchPollingResponse500
    | SocialMediaLookupBatchPollingResponse503
    | None
):
    """Poll batch social media lookup

     Poll for the results of a batch social media lookup. Returns partial results as they become
    available, with overall progress statistics.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    Args:
        body (SocialMediaLookupBatchPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialMediaLookupBatchPollingResponse200 | SocialMediaLookupBatchPollingResponse400 | SocialMediaLookupBatchPollingResponse401 | SocialMediaLookupBatchPollingResponse402 | SocialMediaLookupBatchPollingResponse403 | SocialMediaLookupBatchPollingResponse404 | SocialMediaLookupBatchPollingResponse422 | SocialMediaLookupBatchPollingResponse429 | SocialMediaLookupBatchPollingResponse500 | SocialMediaLookupBatchPollingResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SocialMediaLookupBatchPollingBody,
) -> Response[
    SocialMediaLookupBatchPollingResponse200
    | SocialMediaLookupBatchPollingResponse400
    | SocialMediaLookupBatchPollingResponse401
    | SocialMediaLookupBatchPollingResponse402
    | SocialMediaLookupBatchPollingResponse403
    | SocialMediaLookupBatchPollingResponse404
    | SocialMediaLookupBatchPollingResponse422
    | SocialMediaLookupBatchPollingResponse429
    | SocialMediaLookupBatchPollingResponse500
    | SocialMediaLookupBatchPollingResponse503
]:
    """Poll batch social media lookup

     Poll for the results of a batch social media lookup. Returns partial results as they become
    available, with overall progress statistics.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    Args:
        body (SocialMediaLookupBatchPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialMediaLookupBatchPollingResponse200 | SocialMediaLookupBatchPollingResponse400 | SocialMediaLookupBatchPollingResponse401 | SocialMediaLookupBatchPollingResponse402 | SocialMediaLookupBatchPollingResponse403 | SocialMediaLookupBatchPollingResponse404 | SocialMediaLookupBatchPollingResponse422 | SocialMediaLookupBatchPollingResponse429 | SocialMediaLookupBatchPollingResponse500 | SocialMediaLookupBatchPollingResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SocialMediaLookupBatchPollingBody,
) -> (
    SocialMediaLookupBatchPollingResponse200
    | SocialMediaLookupBatchPollingResponse400
    | SocialMediaLookupBatchPollingResponse401
    | SocialMediaLookupBatchPollingResponse402
    | SocialMediaLookupBatchPollingResponse403
    | SocialMediaLookupBatchPollingResponse404
    | SocialMediaLookupBatchPollingResponse422
    | SocialMediaLookupBatchPollingResponse429
    | SocialMediaLookupBatchPollingResponse500
    | SocialMediaLookupBatchPollingResponse503
    | None
):
    """Poll batch social media lookup

     Poll for the results of a batch social media lookup. Returns partial results as they become
    available, with overall progress statistics.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    Args:
        body (SocialMediaLookupBatchPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialMediaLookupBatchPollingResponse200 | SocialMediaLookupBatchPollingResponse400 | SocialMediaLookupBatchPollingResponse401 | SocialMediaLookupBatchPollingResponse402 | SocialMediaLookupBatchPollingResponse403 | SocialMediaLookupBatchPollingResponse404 | SocialMediaLookupBatchPollingResponse422 | SocialMediaLookupBatchPollingResponse429 | SocialMediaLookupBatchPollingResponse500 | SocialMediaLookupBatchPollingResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
