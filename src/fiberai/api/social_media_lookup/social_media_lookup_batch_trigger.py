from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.social_media_lookup_batch_trigger_body import SocialMediaLookupBatchTriggerBody
from ...models.social_media_lookup_batch_trigger_response_200 import SocialMediaLookupBatchTriggerResponse200
from ...models.social_media_lookup_batch_trigger_response_400 import SocialMediaLookupBatchTriggerResponse400
from ...models.social_media_lookup_batch_trigger_response_401 import SocialMediaLookupBatchTriggerResponse401
from ...models.social_media_lookup_batch_trigger_response_402 import SocialMediaLookupBatchTriggerResponse402
from ...models.social_media_lookup_batch_trigger_response_403 import SocialMediaLookupBatchTriggerResponse403
from ...models.social_media_lookup_batch_trigger_response_404 import SocialMediaLookupBatchTriggerResponse404
from ...models.social_media_lookup_batch_trigger_response_422 import SocialMediaLookupBatchTriggerResponse422
from ...models.social_media_lookup_batch_trigger_response_429 import SocialMediaLookupBatchTriggerResponse429
from ...models.social_media_lookup_batch_trigger_response_500 import SocialMediaLookupBatchTriggerResponse500
from ...models.social_media_lookup_batch_trigger_response_503 import SocialMediaLookupBatchTriggerResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SocialMediaLookupBatchTriggerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/social-media-lookup/batch/trigger",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SocialMediaLookupBatchTriggerResponse200
    | SocialMediaLookupBatchTriggerResponse400
    | SocialMediaLookupBatchTriggerResponse401
    | SocialMediaLookupBatchTriggerResponse402
    | SocialMediaLookupBatchTriggerResponse403
    | SocialMediaLookupBatchTriggerResponse404
    | SocialMediaLookupBatchTriggerResponse422
    | SocialMediaLookupBatchTriggerResponse429
    | SocialMediaLookupBatchTriggerResponse500
    | SocialMediaLookupBatchTriggerResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SocialMediaLookupBatchTriggerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SocialMediaLookupBatchTriggerResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SocialMediaLookupBatchTriggerResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SocialMediaLookupBatchTriggerResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SocialMediaLookupBatchTriggerResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SocialMediaLookupBatchTriggerResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = SocialMediaLookupBatchTriggerResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = SocialMediaLookupBatchTriggerResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SocialMediaLookupBatchTriggerResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SocialMediaLookupBatchTriggerResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SocialMediaLookupBatchTriggerResponse200
    | SocialMediaLookupBatchTriggerResponse400
    | SocialMediaLookupBatchTriggerResponse401
    | SocialMediaLookupBatchTriggerResponse402
    | SocialMediaLookupBatchTriggerResponse403
    | SocialMediaLookupBatchTriggerResponse404
    | SocialMediaLookupBatchTriggerResponse422
    | SocialMediaLookupBatchTriggerResponse429
    | SocialMediaLookupBatchTriggerResponse500
    | SocialMediaLookupBatchTriggerResponse503
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
    body: SocialMediaLookupBatchTriggerBody,
) -> Response[
    SocialMediaLookupBatchTriggerResponse200
    | SocialMediaLookupBatchTriggerResponse400
    | SocialMediaLookupBatchTriggerResponse401
    | SocialMediaLookupBatchTriggerResponse402
    | SocialMediaLookupBatchTriggerResponse403
    | SocialMediaLookupBatchTriggerResponse404
    | SocialMediaLookupBatchTriggerResponse422
    | SocialMediaLookupBatchTriggerResponse429
    | SocialMediaLookupBatchTriggerResponse500
    | SocialMediaLookupBatchTriggerResponse503
]:
    r"""Start batch social media lookup (X, Instagram)

     Start a batch social media lookup for multiple people. Find X (Twitter) and Instagram profiles using
    LinkedIn URLs, user IDs, or manual name+context. Results are available via the batch polling
    endpoint.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per platform searched per person&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SocialMediaLookupBatchTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialMediaLookupBatchTriggerResponse200 | SocialMediaLookupBatchTriggerResponse400 | SocialMediaLookupBatchTriggerResponse401 | SocialMediaLookupBatchTriggerResponse402 | SocialMediaLookupBatchTriggerResponse403 | SocialMediaLookupBatchTriggerResponse404 | SocialMediaLookupBatchTriggerResponse422 | SocialMediaLookupBatchTriggerResponse429 | SocialMediaLookupBatchTriggerResponse500 | SocialMediaLookupBatchTriggerResponse503]
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
    body: SocialMediaLookupBatchTriggerBody,
) -> (
    SocialMediaLookupBatchTriggerResponse200
    | SocialMediaLookupBatchTriggerResponse400
    | SocialMediaLookupBatchTriggerResponse401
    | SocialMediaLookupBatchTriggerResponse402
    | SocialMediaLookupBatchTriggerResponse403
    | SocialMediaLookupBatchTriggerResponse404
    | SocialMediaLookupBatchTriggerResponse422
    | SocialMediaLookupBatchTriggerResponse429
    | SocialMediaLookupBatchTriggerResponse500
    | SocialMediaLookupBatchTriggerResponse503
    | None
):
    r"""Start batch social media lookup (X, Instagram)

     Start a batch social media lookup for multiple people. Find X (Twitter) and Instagram profiles using
    LinkedIn URLs, user IDs, or manual name+context. Results are available via the batch polling
    endpoint.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per platform searched per person&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SocialMediaLookupBatchTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialMediaLookupBatchTriggerResponse200 | SocialMediaLookupBatchTriggerResponse400 | SocialMediaLookupBatchTriggerResponse401 | SocialMediaLookupBatchTriggerResponse402 | SocialMediaLookupBatchTriggerResponse403 | SocialMediaLookupBatchTriggerResponse404 | SocialMediaLookupBatchTriggerResponse422 | SocialMediaLookupBatchTriggerResponse429 | SocialMediaLookupBatchTriggerResponse500 | SocialMediaLookupBatchTriggerResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SocialMediaLookupBatchTriggerBody,
) -> Response[
    SocialMediaLookupBatchTriggerResponse200
    | SocialMediaLookupBatchTriggerResponse400
    | SocialMediaLookupBatchTriggerResponse401
    | SocialMediaLookupBatchTriggerResponse402
    | SocialMediaLookupBatchTriggerResponse403
    | SocialMediaLookupBatchTriggerResponse404
    | SocialMediaLookupBatchTriggerResponse422
    | SocialMediaLookupBatchTriggerResponse429
    | SocialMediaLookupBatchTriggerResponse500
    | SocialMediaLookupBatchTriggerResponse503
]:
    r"""Start batch social media lookup (X, Instagram)

     Start a batch social media lookup for multiple people. Find X (Twitter) and Instagram profiles using
    LinkedIn URLs, user IDs, or manual name+context. Results are available via the batch polling
    endpoint.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per platform searched per person&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SocialMediaLookupBatchTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialMediaLookupBatchTriggerResponse200 | SocialMediaLookupBatchTriggerResponse400 | SocialMediaLookupBatchTriggerResponse401 | SocialMediaLookupBatchTriggerResponse402 | SocialMediaLookupBatchTriggerResponse403 | SocialMediaLookupBatchTriggerResponse404 | SocialMediaLookupBatchTriggerResponse422 | SocialMediaLookupBatchTriggerResponse429 | SocialMediaLookupBatchTriggerResponse500 | SocialMediaLookupBatchTriggerResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SocialMediaLookupBatchTriggerBody,
) -> (
    SocialMediaLookupBatchTriggerResponse200
    | SocialMediaLookupBatchTriggerResponse400
    | SocialMediaLookupBatchTriggerResponse401
    | SocialMediaLookupBatchTriggerResponse402
    | SocialMediaLookupBatchTriggerResponse403
    | SocialMediaLookupBatchTriggerResponse404
    | SocialMediaLookupBatchTriggerResponse422
    | SocialMediaLookupBatchTriggerResponse429
    | SocialMediaLookupBatchTriggerResponse500
    | SocialMediaLookupBatchTriggerResponse503
    | None
):
    r"""Start batch social media lookup (X, Instagram)

     Start a batch social media lookup for multiple people. Find X (Twitter) and Instagram profiles using
    LinkedIn URLs, user IDs, or manual name+context. Results are available via the batch polling
    endpoint.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per platform searched per person&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SocialMediaLookupBatchTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialMediaLookupBatchTriggerResponse200 | SocialMediaLookupBatchTriggerResponse400 | SocialMediaLookupBatchTriggerResponse401 | SocialMediaLookupBatchTriggerResponse402 | SocialMediaLookupBatchTriggerResponse403 | SocialMediaLookupBatchTriggerResponse404 | SocialMediaLookupBatchTriggerResponse422 | SocialMediaLookupBatchTriggerResponse429 | SocialMediaLookupBatchTriggerResponse500 | SocialMediaLookupBatchTriggerResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
