from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.preview_tracker_signal_body import PreviewTrackerSignalBody
from ...models.preview_tracker_signal_response_200 import PreviewTrackerSignalResponse200
from ...models.preview_tracker_signal_response_400 import PreviewTrackerSignalResponse400
from ...models.preview_tracker_signal_response_401 import PreviewTrackerSignalResponse401
from ...models.preview_tracker_signal_response_402 import PreviewTrackerSignalResponse402
from ...models.preview_tracker_signal_response_403 import PreviewTrackerSignalResponse403
from ...models.preview_tracker_signal_response_404 import PreviewTrackerSignalResponse404
from ...models.preview_tracker_signal_response_422 import PreviewTrackerSignalResponse422
from ...models.preview_tracker_signal_response_429 import PreviewTrackerSignalResponse429
from ...models.preview_tracker_signal_response_500 import PreviewTrackerSignalResponse500
from ...models.preview_tracker_signal_response_503 import PreviewTrackerSignalResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PreviewTrackerSignalBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tracker/rules/preview-signal",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PreviewTrackerSignalResponse200
    | PreviewTrackerSignalResponse400
    | PreviewTrackerSignalResponse401
    | PreviewTrackerSignalResponse402
    | PreviewTrackerSignalResponse403
    | PreviewTrackerSignalResponse404
    | PreviewTrackerSignalResponse422
    | PreviewTrackerSignalResponse429
    | PreviewTrackerSignalResponse500
    | PreviewTrackerSignalResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PreviewTrackerSignalResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PreviewTrackerSignalResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PreviewTrackerSignalResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PreviewTrackerSignalResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PreviewTrackerSignalResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PreviewTrackerSignalResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PreviewTrackerSignalResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PreviewTrackerSignalResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PreviewTrackerSignalResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PreviewTrackerSignalResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PreviewTrackerSignalResponse200
    | PreviewTrackerSignalResponse400
    | PreviewTrackerSignalResponse401
    | PreviewTrackerSignalResponse402
    | PreviewTrackerSignalResponse403
    | PreviewTrackerSignalResponse404
    | PreviewTrackerSignalResponse422
    | PreviewTrackerSignalResponse429
    | PreviewTrackerSignalResponse500
    | PreviewTrackerSignalResponse503
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
    body: PreviewTrackerSignalBody,
) -> Response[
    PreviewTrackerSignalResponse200
    | PreviewTrackerSignalResponse400
    | PreviewTrackerSignalResponse401
    | PreviewTrackerSignalResponse402
    | PreviewTrackerSignalResponse403
    | PreviewTrackerSignalResponse404
    | PreviewTrackerSignalResponse422
    | PreviewTrackerSignalResponse429
    | PreviewTrackerSignalResponse500
    | PreviewTrackerSignalResponse503
]:
    r"""Preview a signal

     Returns an example signal payload for a given rule configuration. No side effects — nothing is
    created or dispatched. Free to call. Useful for understanding signal shapes before creating rules.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PreviewTrackerSignalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PreviewTrackerSignalResponse200 | PreviewTrackerSignalResponse400 | PreviewTrackerSignalResponse401 | PreviewTrackerSignalResponse402 | PreviewTrackerSignalResponse403 | PreviewTrackerSignalResponse404 | PreviewTrackerSignalResponse422 | PreviewTrackerSignalResponse429 | PreviewTrackerSignalResponse500 | PreviewTrackerSignalResponse503]
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
    body: PreviewTrackerSignalBody,
) -> (
    PreviewTrackerSignalResponse200
    | PreviewTrackerSignalResponse400
    | PreviewTrackerSignalResponse401
    | PreviewTrackerSignalResponse402
    | PreviewTrackerSignalResponse403
    | PreviewTrackerSignalResponse404
    | PreviewTrackerSignalResponse422
    | PreviewTrackerSignalResponse429
    | PreviewTrackerSignalResponse500
    | PreviewTrackerSignalResponse503
    | None
):
    r"""Preview a signal

     Returns an example signal payload for a given rule configuration. No side effects — nothing is
    created or dispatched. Free to call. Useful for understanding signal shapes before creating rules.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PreviewTrackerSignalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PreviewTrackerSignalResponse200 | PreviewTrackerSignalResponse400 | PreviewTrackerSignalResponse401 | PreviewTrackerSignalResponse402 | PreviewTrackerSignalResponse403 | PreviewTrackerSignalResponse404 | PreviewTrackerSignalResponse422 | PreviewTrackerSignalResponse429 | PreviewTrackerSignalResponse500 | PreviewTrackerSignalResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PreviewTrackerSignalBody,
) -> Response[
    PreviewTrackerSignalResponse200
    | PreviewTrackerSignalResponse400
    | PreviewTrackerSignalResponse401
    | PreviewTrackerSignalResponse402
    | PreviewTrackerSignalResponse403
    | PreviewTrackerSignalResponse404
    | PreviewTrackerSignalResponse422
    | PreviewTrackerSignalResponse429
    | PreviewTrackerSignalResponse500
    | PreviewTrackerSignalResponse503
]:
    r"""Preview a signal

     Returns an example signal payload for a given rule configuration. No side effects — nothing is
    created or dispatched. Free to call. Useful for understanding signal shapes before creating rules.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PreviewTrackerSignalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PreviewTrackerSignalResponse200 | PreviewTrackerSignalResponse400 | PreviewTrackerSignalResponse401 | PreviewTrackerSignalResponse402 | PreviewTrackerSignalResponse403 | PreviewTrackerSignalResponse404 | PreviewTrackerSignalResponse422 | PreviewTrackerSignalResponse429 | PreviewTrackerSignalResponse500 | PreviewTrackerSignalResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PreviewTrackerSignalBody,
) -> (
    PreviewTrackerSignalResponse200
    | PreviewTrackerSignalResponse400
    | PreviewTrackerSignalResponse401
    | PreviewTrackerSignalResponse402
    | PreviewTrackerSignalResponse403
    | PreviewTrackerSignalResponse404
    | PreviewTrackerSignalResponse422
    | PreviewTrackerSignalResponse429
    | PreviewTrackerSignalResponse500
    | PreviewTrackerSignalResponse503
    | None
):
    r"""Preview a signal

     Returns an example signal payload for a given rule configuration. No side effects — nothing is
    created or dispatched. Free to call. Useful for understanding signal shapes before creating rules.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PreviewTrackerSignalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PreviewTrackerSignalResponse200 | PreviewTrackerSignalResponse400 | PreviewTrackerSignalResponse401 | PreviewTrackerSignalResponse402 | PreviewTrackerSignalResponse403 | PreviewTrackerSignalResponse404 | PreviewTrackerSignalResponse422 | PreviewTrackerSignalResponse429 | PreviewTrackerSignalResponse500 | PreviewTrackerSignalResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
