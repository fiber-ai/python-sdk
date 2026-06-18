from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.social_media_lookup_trigger_body import SocialMediaLookupTriggerBody
from ...models.social_media_lookup_trigger_response_200 import SocialMediaLookupTriggerResponse200
from ...models.social_media_lookup_trigger_response_400 import SocialMediaLookupTriggerResponse400
from ...models.social_media_lookup_trigger_response_401 import SocialMediaLookupTriggerResponse401
from ...models.social_media_lookup_trigger_response_402 import SocialMediaLookupTriggerResponse402
from ...models.social_media_lookup_trigger_response_403 import SocialMediaLookupTriggerResponse403
from ...models.social_media_lookup_trigger_response_404 import SocialMediaLookupTriggerResponse404
from ...models.social_media_lookup_trigger_response_422 import SocialMediaLookupTriggerResponse422
from ...models.social_media_lookup_trigger_response_429 import SocialMediaLookupTriggerResponse429
from ...models.social_media_lookup_trigger_response_500 import SocialMediaLookupTriggerResponse500
from ...models.social_media_lookup_trigger_response_503 import SocialMediaLookupTriggerResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SocialMediaLookupTriggerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/social-media-lookup/trigger",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SocialMediaLookupTriggerResponse200
    | SocialMediaLookupTriggerResponse400
    | SocialMediaLookupTriggerResponse401
    | SocialMediaLookupTriggerResponse402
    | SocialMediaLookupTriggerResponse403
    | SocialMediaLookupTriggerResponse404
    | SocialMediaLookupTriggerResponse422
    | SocialMediaLookupTriggerResponse429
    | SocialMediaLookupTriggerResponse500
    | SocialMediaLookupTriggerResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SocialMediaLookupTriggerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SocialMediaLookupTriggerResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SocialMediaLookupTriggerResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SocialMediaLookupTriggerResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SocialMediaLookupTriggerResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SocialMediaLookupTriggerResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = SocialMediaLookupTriggerResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = SocialMediaLookupTriggerResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SocialMediaLookupTriggerResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SocialMediaLookupTriggerResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SocialMediaLookupTriggerResponse200
    | SocialMediaLookupTriggerResponse400
    | SocialMediaLookupTriggerResponse401
    | SocialMediaLookupTriggerResponse402
    | SocialMediaLookupTriggerResponse403
    | SocialMediaLookupTriggerResponse404
    | SocialMediaLookupTriggerResponse422
    | SocialMediaLookupTriggerResponse429
    | SocialMediaLookupTriggerResponse500
    | SocialMediaLookupTriggerResponse503
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
    body: SocialMediaLookupTriggerBody,
) -> Response[
    SocialMediaLookupTriggerResponse200
    | SocialMediaLookupTriggerResponse400
    | SocialMediaLookupTriggerResponse401
    | SocialMediaLookupTriggerResponse402
    | SocialMediaLookupTriggerResponse403
    | SocialMediaLookupTriggerResponse404
    | SocialMediaLookupTriggerResponse422
    | SocialMediaLookupTriggerResponse429
    | SocialMediaLookupTriggerResponse500
    | SocialMediaLookupTriggerResponse503
]:
    r"""Start social media lookup

     Use our AI agent to find social media profiles (Twitter, Instagram) for a person using name and
    optional context like LinkedIn URL, work email, company, and job title.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per platform searched&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SocialMediaLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialMediaLookupTriggerResponse200 | SocialMediaLookupTriggerResponse400 | SocialMediaLookupTriggerResponse401 | SocialMediaLookupTriggerResponse402 | SocialMediaLookupTriggerResponse403 | SocialMediaLookupTriggerResponse404 | SocialMediaLookupTriggerResponse422 | SocialMediaLookupTriggerResponse429 | SocialMediaLookupTriggerResponse500 | SocialMediaLookupTriggerResponse503]
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
    body: SocialMediaLookupTriggerBody,
) -> (
    SocialMediaLookupTriggerResponse200
    | SocialMediaLookupTriggerResponse400
    | SocialMediaLookupTriggerResponse401
    | SocialMediaLookupTriggerResponse402
    | SocialMediaLookupTriggerResponse403
    | SocialMediaLookupTriggerResponse404
    | SocialMediaLookupTriggerResponse422
    | SocialMediaLookupTriggerResponse429
    | SocialMediaLookupTriggerResponse500
    | SocialMediaLookupTriggerResponse503
    | None
):
    r"""Start social media lookup

     Use our AI agent to find social media profiles (Twitter, Instagram) for a person using name and
    optional context like LinkedIn URL, work email, company, and job title.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per platform searched&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SocialMediaLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialMediaLookupTriggerResponse200 | SocialMediaLookupTriggerResponse400 | SocialMediaLookupTriggerResponse401 | SocialMediaLookupTriggerResponse402 | SocialMediaLookupTriggerResponse403 | SocialMediaLookupTriggerResponse404 | SocialMediaLookupTriggerResponse422 | SocialMediaLookupTriggerResponse429 | SocialMediaLookupTriggerResponse500 | SocialMediaLookupTriggerResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SocialMediaLookupTriggerBody,
) -> Response[
    SocialMediaLookupTriggerResponse200
    | SocialMediaLookupTriggerResponse400
    | SocialMediaLookupTriggerResponse401
    | SocialMediaLookupTriggerResponse402
    | SocialMediaLookupTriggerResponse403
    | SocialMediaLookupTriggerResponse404
    | SocialMediaLookupTriggerResponse422
    | SocialMediaLookupTriggerResponse429
    | SocialMediaLookupTriggerResponse500
    | SocialMediaLookupTriggerResponse503
]:
    r"""Start social media lookup

     Use our AI agent to find social media profiles (Twitter, Instagram) for a person using name and
    optional context like LinkedIn URL, work email, company, and job title.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per platform searched&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SocialMediaLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SocialMediaLookupTriggerResponse200 | SocialMediaLookupTriggerResponse400 | SocialMediaLookupTriggerResponse401 | SocialMediaLookupTriggerResponse402 | SocialMediaLookupTriggerResponse403 | SocialMediaLookupTriggerResponse404 | SocialMediaLookupTriggerResponse422 | SocialMediaLookupTriggerResponse429 | SocialMediaLookupTriggerResponse500 | SocialMediaLookupTriggerResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SocialMediaLookupTriggerBody,
) -> (
    SocialMediaLookupTriggerResponse200
    | SocialMediaLookupTriggerResponse400
    | SocialMediaLookupTriggerResponse401
    | SocialMediaLookupTriggerResponse402
    | SocialMediaLookupTriggerResponse403
    | SocialMediaLookupTriggerResponse404
    | SocialMediaLookupTriggerResponse422
    | SocialMediaLookupTriggerResponse429
    | SocialMediaLookupTriggerResponse500
    | SocialMediaLookupTriggerResponse503
    | None
):
    r"""Start social media lookup

     Use our AI agent to find social media profiles (Twitter, Instagram) for a person using name and
    optional context like LinkedIn URL, work email, company, and job title.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per platform searched&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SocialMediaLookupTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SocialMediaLookupTriggerResponse200 | SocialMediaLookupTriggerResponse400 | SocialMediaLookupTriggerResponse401 | SocialMediaLookupTriggerResponse402 | SocialMediaLookupTriggerResponse403 | SocialMediaLookupTriggerResponse404 | SocialMediaLookupTriggerResponse422 | SocialMediaLookupTriggerResponse429 | SocialMediaLookupTriggerResponse500 | SocialMediaLookupTriggerResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
