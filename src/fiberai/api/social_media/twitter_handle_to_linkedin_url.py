from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.twitter_handle_to_linkedin_url_body import TwitterHandleToLinkedinUrlBody
from ...models.twitter_handle_to_linkedin_url_response_200 import TwitterHandleToLinkedinUrlResponse200
from ...models.twitter_handle_to_linkedin_url_response_400 import TwitterHandleToLinkedinUrlResponse400
from ...models.twitter_handle_to_linkedin_url_response_401 import TwitterHandleToLinkedinUrlResponse401
from ...models.twitter_handle_to_linkedin_url_response_402 import TwitterHandleToLinkedinUrlResponse402
from ...models.twitter_handle_to_linkedin_url_response_403 import TwitterHandleToLinkedinUrlResponse403
from ...models.twitter_handle_to_linkedin_url_response_404 import TwitterHandleToLinkedinUrlResponse404
from ...models.twitter_handle_to_linkedin_url_response_429 import TwitterHandleToLinkedinUrlResponse429
from ...models.twitter_handle_to_linkedin_url_response_500 import TwitterHandleToLinkedinUrlResponse500
from ...models.twitter_handle_to_linkedin_url_response_503 import TwitterHandleToLinkedinUrlResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TwitterHandleToLinkedinUrlBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/twitter-handle-to-linkedin/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TwitterHandleToLinkedinUrlResponse200
    | TwitterHandleToLinkedinUrlResponse400
    | TwitterHandleToLinkedinUrlResponse401
    | TwitterHandleToLinkedinUrlResponse402
    | TwitterHandleToLinkedinUrlResponse403
    | TwitterHandleToLinkedinUrlResponse404
    | TwitterHandleToLinkedinUrlResponse429
    | TwitterHandleToLinkedinUrlResponse500
    | TwitterHandleToLinkedinUrlResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TwitterHandleToLinkedinUrlResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TwitterHandleToLinkedinUrlResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TwitterHandleToLinkedinUrlResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TwitterHandleToLinkedinUrlResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TwitterHandleToLinkedinUrlResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TwitterHandleToLinkedinUrlResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TwitterHandleToLinkedinUrlResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TwitterHandleToLinkedinUrlResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TwitterHandleToLinkedinUrlResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TwitterHandleToLinkedinUrlResponse200
    | TwitterHandleToLinkedinUrlResponse400
    | TwitterHandleToLinkedinUrlResponse401
    | TwitterHandleToLinkedinUrlResponse402
    | TwitterHandleToLinkedinUrlResponse403
    | TwitterHandleToLinkedinUrlResponse404
    | TwitterHandleToLinkedinUrlResponse429
    | TwitterHandleToLinkedinUrlResponse500
    | TwitterHandleToLinkedinUrlResponse503
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
    body: TwitterHandleToLinkedinUrlBody,
) -> Response[
    TwitterHandleToLinkedinUrlResponse200
    | TwitterHandleToLinkedinUrlResponse400
    | TwitterHandleToLinkedinUrlResponse401
    | TwitterHandleToLinkedinUrlResponse402
    | TwitterHandleToLinkedinUrlResponse403
    | TwitterHandleToLinkedinUrlResponse404
    | TwitterHandleToLinkedinUrlResponse429
    | TwitterHandleToLinkedinUrlResponse500
    | TwitterHandleToLinkedinUrlResponse503
]:
    r"""Find LinkedIn URL from X (Twitter) handle

     Given an X (Twitter) handle, find the person's LinkedIn profile URL. Accepts bare handles (with or
    without '@') and full X / Twitter profile URLs.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per X→LinkedIn lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (TwitterHandleToLinkedinUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterHandleToLinkedinUrlResponse200 | TwitterHandleToLinkedinUrlResponse400 | TwitterHandleToLinkedinUrlResponse401 | TwitterHandleToLinkedinUrlResponse402 | TwitterHandleToLinkedinUrlResponse403 | TwitterHandleToLinkedinUrlResponse404 | TwitterHandleToLinkedinUrlResponse429 | TwitterHandleToLinkedinUrlResponse500 | TwitterHandleToLinkedinUrlResponse503]
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
    body: TwitterHandleToLinkedinUrlBody,
) -> (
    TwitterHandleToLinkedinUrlResponse200
    | TwitterHandleToLinkedinUrlResponse400
    | TwitterHandleToLinkedinUrlResponse401
    | TwitterHandleToLinkedinUrlResponse402
    | TwitterHandleToLinkedinUrlResponse403
    | TwitterHandleToLinkedinUrlResponse404
    | TwitterHandleToLinkedinUrlResponse429
    | TwitterHandleToLinkedinUrlResponse500
    | TwitterHandleToLinkedinUrlResponse503
    | None
):
    r"""Find LinkedIn URL from X (Twitter) handle

     Given an X (Twitter) handle, find the person's LinkedIn profile URL. Accepts bare handles (with or
    without '@') and full X / Twitter profile URLs.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per X→LinkedIn lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (TwitterHandleToLinkedinUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterHandleToLinkedinUrlResponse200 | TwitterHandleToLinkedinUrlResponse400 | TwitterHandleToLinkedinUrlResponse401 | TwitterHandleToLinkedinUrlResponse402 | TwitterHandleToLinkedinUrlResponse403 | TwitterHandleToLinkedinUrlResponse404 | TwitterHandleToLinkedinUrlResponse429 | TwitterHandleToLinkedinUrlResponse500 | TwitterHandleToLinkedinUrlResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterHandleToLinkedinUrlBody,
) -> Response[
    TwitterHandleToLinkedinUrlResponse200
    | TwitterHandleToLinkedinUrlResponse400
    | TwitterHandleToLinkedinUrlResponse401
    | TwitterHandleToLinkedinUrlResponse402
    | TwitterHandleToLinkedinUrlResponse403
    | TwitterHandleToLinkedinUrlResponse404
    | TwitterHandleToLinkedinUrlResponse429
    | TwitterHandleToLinkedinUrlResponse500
    | TwitterHandleToLinkedinUrlResponse503
]:
    r"""Find LinkedIn URL from X (Twitter) handle

     Given an X (Twitter) handle, find the person's LinkedIn profile URL. Accepts bare handles (with or
    without '@') and full X / Twitter profile URLs.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per X→LinkedIn lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (TwitterHandleToLinkedinUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterHandleToLinkedinUrlResponse200 | TwitterHandleToLinkedinUrlResponse400 | TwitterHandleToLinkedinUrlResponse401 | TwitterHandleToLinkedinUrlResponse402 | TwitterHandleToLinkedinUrlResponse403 | TwitterHandleToLinkedinUrlResponse404 | TwitterHandleToLinkedinUrlResponse429 | TwitterHandleToLinkedinUrlResponse500 | TwitterHandleToLinkedinUrlResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterHandleToLinkedinUrlBody,
) -> (
    TwitterHandleToLinkedinUrlResponse200
    | TwitterHandleToLinkedinUrlResponse400
    | TwitterHandleToLinkedinUrlResponse401
    | TwitterHandleToLinkedinUrlResponse402
    | TwitterHandleToLinkedinUrlResponse403
    | TwitterHandleToLinkedinUrlResponse404
    | TwitterHandleToLinkedinUrlResponse429
    | TwitterHandleToLinkedinUrlResponse500
    | TwitterHandleToLinkedinUrlResponse503
    | None
):
    r"""Find LinkedIn URL from X (Twitter) handle

     Given an X (Twitter) handle, find the person's LinkedIn profile URL. Accepts bare handles (with or
    without '@') and full X / Twitter profile URLs.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per X→LinkedIn lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (TwitterHandleToLinkedinUrlBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterHandleToLinkedinUrlResponse200 | TwitterHandleToLinkedinUrlResponse400 | TwitterHandleToLinkedinUrlResponse401 | TwitterHandleToLinkedinUrlResponse402 | TwitterHandleToLinkedinUrlResponse403 | TwitterHandleToLinkedinUrlResponse404 | TwitterHandleToLinkedinUrlResponse429 | TwitterHandleToLinkedinUrlResponse500 | TwitterHandleToLinkedinUrlResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
