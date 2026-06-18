from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webpage_screenshot_body import WebpageScreenshotBody
from ...models.webpage_screenshot_response_200 import WebpageScreenshotResponse200
from ...models.webpage_screenshot_response_400 import WebpageScreenshotResponse400
from ...models.webpage_screenshot_response_401 import WebpageScreenshotResponse401
from ...models.webpage_screenshot_response_402 import WebpageScreenshotResponse402
from ...models.webpage_screenshot_response_403 import WebpageScreenshotResponse403
from ...models.webpage_screenshot_response_404 import WebpageScreenshotResponse404
from ...models.webpage_screenshot_response_422 import WebpageScreenshotResponse422
from ...models.webpage_screenshot_response_429 import WebpageScreenshotResponse429
from ...models.webpage_screenshot_response_500 import WebpageScreenshotResponse500
from ...models.webpage_screenshot_response_503 import WebpageScreenshotResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: WebpageScreenshotBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/live-fetch/webpage/screenshot",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    WebpageScreenshotResponse200
    | WebpageScreenshotResponse400
    | WebpageScreenshotResponse401
    | WebpageScreenshotResponse402
    | WebpageScreenshotResponse403
    | WebpageScreenshotResponse404
    | WebpageScreenshotResponse422
    | WebpageScreenshotResponse429
    | WebpageScreenshotResponse500
    | WebpageScreenshotResponse503
    | None
):
    if response.status_code == 200:
        response_200 = WebpageScreenshotResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = WebpageScreenshotResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = WebpageScreenshotResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = WebpageScreenshotResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = WebpageScreenshotResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = WebpageScreenshotResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = WebpageScreenshotResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = WebpageScreenshotResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = WebpageScreenshotResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = WebpageScreenshotResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    WebpageScreenshotResponse200
    | WebpageScreenshotResponse400
    | WebpageScreenshotResponse401
    | WebpageScreenshotResponse402
    | WebpageScreenshotResponse403
    | WebpageScreenshotResponse404
    | WebpageScreenshotResponse422
    | WebpageScreenshotResponse429
    | WebpageScreenshotResponse500
    | WebpageScreenshotResponse503
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
    body: WebpageScreenshotBody,
) -> Response[
    WebpageScreenshotResponse200
    | WebpageScreenshotResponse400
    | WebpageScreenshotResponse401
    | WebpageScreenshotResponse402
    | WebpageScreenshotResponse403
    | WebpageScreenshotResponse404
    | WebpageScreenshotResponse422
    | WebpageScreenshotResponse429
    | WebpageScreenshotResponse500
    | WebpageScreenshotResponse503
]:
    r"""Capture webpage screenshot

     Captures a screenshot of a public webpage and returns a hosted image URL. Supports both viewport-
    only and full-page captures. The returned URL is permanent and does not expire.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per screenshot&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (WebpageScreenshotBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebpageScreenshotResponse200 | WebpageScreenshotResponse400 | WebpageScreenshotResponse401 | WebpageScreenshotResponse402 | WebpageScreenshotResponse403 | WebpageScreenshotResponse404 | WebpageScreenshotResponse422 | WebpageScreenshotResponse429 | WebpageScreenshotResponse500 | WebpageScreenshotResponse503]
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
    body: WebpageScreenshotBody,
) -> (
    WebpageScreenshotResponse200
    | WebpageScreenshotResponse400
    | WebpageScreenshotResponse401
    | WebpageScreenshotResponse402
    | WebpageScreenshotResponse403
    | WebpageScreenshotResponse404
    | WebpageScreenshotResponse422
    | WebpageScreenshotResponse429
    | WebpageScreenshotResponse500
    | WebpageScreenshotResponse503
    | None
):
    r"""Capture webpage screenshot

     Captures a screenshot of a public webpage and returns a hosted image URL. Supports both viewport-
    only and full-page captures. The returned URL is permanent and does not expire.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per screenshot&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (WebpageScreenshotBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebpageScreenshotResponse200 | WebpageScreenshotResponse400 | WebpageScreenshotResponse401 | WebpageScreenshotResponse402 | WebpageScreenshotResponse403 | WebpageScreenshotResponse404 | WebpageScreenshotResponse422 | WebpageScreenshotResponse429 | WebpageScreenshotResponse500 | WebpageScreenshotResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WebpageScreenshotBody,
) -> Response[
    WebpageScreenshotResponse200
    | WebpageScreenshotResponse400
    | WebpageScreenshotResponse401
    | WebpageScreenshotResponse402
    | WebpageScreenshotResponse403
    | WebpageScreenshotResponse404
    | WebpageScreenshotResponse422
    | WebpageScreenshotResponse429
    | WebpageScreenshotResponse500
    | WebpageScreenshotResponse503
]:
    r"""Capture webpage screenshot

     Captures a screenshot of a public webpage and returns a hosted image URL. Supports both viewport-
    only and full-page captures. The returned URL is permanent and does not expire.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per screenshot&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (WebpageScreenshotBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebpageScreenshotResponse200 | WebpageScreenshotResponse400 | WebpageScreenshotResponse401 | WebpageScreenshotResponse402 | WebpageScreenshotResponse403 | WebpageScreenshotResponse404 | WebpageScreenshotResponse422 | WebpageScreenshotResponse429 | WebpageScreenshotResponse500 | WebpageScreenshotResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: WebpageScreenshotBody,
) -> (
    WebpageScreenshotResponse200
    | WebpageScreenshotResponse400
    | WebpageScreenshotResponse401
    | WebpageScreenshotResponse402
    | WebpageScreenshotResponse403
    | WebpageScreenshotResponse404
    | WebpageScreenshotResponse422
    | WebpageScreenshotResponse429
    | WebpageScreenshotResponse500
    | WebpageScreenshotResponse503
    | None
):
    r"""Capture webpage screenshot

     Captures a screenshot of a public webpage and returns a hosted image URL. Supports both viewport-
    only and full-page captures. The returned URL is permanent and does not expire.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per screenshot&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (WebpageScreenshotBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebpageScreenshotResponse200 | WebpageScreenshotResponse400 | WebpageScreenshotResponse401 | WebpageScreenshotResponse402 | WebpageScreenshotResponse403 | WebpageScreenshotResponse404 | WebpageScreenshotResponse422 | WebpageScreenshotResponse429 | WebpageScreenshotResponse500 | WebpageScreenshotResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
