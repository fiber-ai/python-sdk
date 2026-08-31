from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.skip_next_saved_search_run_body import SkipNextSavedSearchRunBody
from ...models.skip_next_saved_search_run_response_200 import SkipNextSavedSearchRunResponse200
from ...models.skip_next_saved_search_run_response_400 import SkipNextSavedSearchRunResponse400
from ...models.skip_next_saved_search_run_response_401 import SkipNextSavedSearchRunResponse401
from ...models.skip_next_saved_search_run_response_402 import SkipNextSavedSearchRunResponse402
from ...models.skip_next_saved_search_run_response_403 import SkipNextSavedSearchRunResponse403
from ...models.skip_next_saved_search_run_response_404 import SkipNextSavedSearchRunResponse404
from ...models.skip_next_saved_search_run_response_422 import SkipNextSavedSearchRunResponse422
from ...models.skip_next_saved_search_run_response_429 import SkipNextSavedSearchRunResponse429
from ...models.skip_next_saved_search_run_response_500 import SkipNextSavedSearchRunResponse500
from ...models.skip_next_saved_search_run_response_503 import SkipNextSavedSearchRunResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SkipNextSavedSearchRunBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/skip-next-run",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SkipNextSavedSearchRunResponse200
    | SkipNextSavedSearchRunResponse400
    | SkipNextSavedSearchRunResponse401
    | SkipNextSavedSearchRunResponse402
    | SkipNextSavedSearchRunResponse403
    | SkipNextSavedSearchRunResponse404
    | SkipNextSavedSearchRunResponse422
    | SkipNextSavedSearchRunResponse429
    | SkipNextSavedSearchRunResponse500
    | SkipNextSavedSearchRunResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SkipNextSavedSearchRunResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SkipNextSavedSearchRunResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SkipNextSavedSearchRunResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SkipNextSavedSearchRunResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SkipNextSavedSearchRunResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SkipNextSavedSearchRunResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = SkipNextSavedSearchRunResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = SkipNextSavedSearchRunResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SkipNextSavedSearchRunResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SkipNextSavedSearchRunResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SkipNextSavedSearchRunResponse200
    | SkipNextSavedSearchRunResponse400
    | SkipNextSavedSearchRunResponse401
    | SkipNextSavedSearchRunResponse402
    | SkipNextSavedSearchRunResponse403
    | SkipNextSavedSearchRunResponse404
    | SkipNextSavedSearchRunResponse422
    | SkipNextSavedSearchRunResponse429
    | SkipNextSavedSearchRunResponse500
    | SkipNextSavedSearchRunResponse503
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
    body: SkipNextSavedSearchRunBody,
) -> Response[
    SkipNextSavedSearchRunResponse200
    | SkipNextSavedSearchRunResponse400
    | SkipNextSavedSearchRunResponse401
    | SkipNextSavedSearchRunResponse402
    | SkipNextSavedSearchRunResponse403
    | SkipNextSavedSearchRunResponse404
    | SkipNextSavedSearchRunResponse422
    | SkipNextSavedSearchRunResponse429
    | SkipNextSavedSearchRunResponse500
    | SkipNextSavedSearchRunResponse503
]:
    """Skip next saved search auto-run

     Skip the next scheduled auto-run for a saved search. The search will resume its normal schedule
    after one skipped cycle. Manual runs are not affected.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (SkipNextSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SkipNextSavedSearchRunResponse200 | SkipNextSavedSearchRunResponse400 | SkipNextSavedSearchRunResponse401 | SkipNextSavedSearchRunResponse402 | SkipNextSavedSearchRunResponse403 | SkipNextSavedSearchRunResponse404 | SkipNextSavedSearchRunResponse422 | SkipNextSavedSearchRunResponse429 | SkipNextSavedSearchRunResponse500 | SkipNextSavedSearchRunResponse503]
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
    body: SkipNextSavedSearchRunBody,
) -> (
    SkipNextSavedSearchRunResponse200
    | SkipNextSavedSearchRunResponse400
    | SkipNextSavedSearchRunResponse401
    | SkipNextSavedSearchRunResponse402
    | SkipNextSavedSearchRunResponse403
    | SkipNextSavedSearchRunResponse404
    | SkipNextSavedSearchRunResponse422
    | SkipNextSavedSearchRunResponse429
    | SkipNextSavedSearchRunResponse500
    | SkipNextSavedSearchRunResponse503
    | None
):
    """Skip next saved search auto-run

     Skip the next scheduled auto-run for a saved search. The search will resume its normal schedule
    after one skipped cycle. Manual runs are not affected.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (SkipNextSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SkipNextSavedSearchRunResponse200 | SkipNextSavedSearchRunResponse400 | SkipNextSavedSearchRunResponse401 | SkipNextSavedSearchRunResponse402 | SkipNextSavedSearchRunResponse403 | SkipNextSavedSearchRunResponse404 | SkipNextSavedSearchRunResponse422 | SkipNextSavedSearchRunResponse429 | SkipNextSavedSearchRunResponse500 | SkipNextSavedSearchRunResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SkipNextSavedSearchRunBody,
) -> Response[
    SkipNextSavedSearchRunResponse200
    | SkipNextSavedSearchRunResponse400
    | SkipNextSavedSearchRunResponse401
    | SkipNextSavedSearchRunResponse402
    | SkipNextSavedSearchRunResponse403
    | SkipNextSavedSearchRunResponse404
    | SkipNextSavedSearchRunResponse422
    | SkipNextSavedSearchRunResponse429
    | SkipNextSavedSearchRunResponse500
    | SkipNextSavedSearchRunResponse503
]:
    """Skip next saved search auto-run

     Skip the next scheduled auto-run for a saved search. The search will resume its normal schedule
    after one skipped cycle. Manual runs are not affected.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (SkipNextSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SkipNextSavedSearchRunResponse200 | SkipNextSavedSearchRunResponse400 | SkipNextSavedSearchRunResponse401 | SkipNextSavedSearchRunResponse402 | SkipNextSavedSearchRunResponse403 | SkipNextSavedSearchRunResponse404 | SkipNextSavedSearchRunResponse422 | SkipNextSavedSearchRunResponse429 | SkipNextSavedSearchRunResponse500 | SkipNextSavedSearchRunResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SkipNextSavedSearchRunBody,
) -> (
    SkipNextSavedSearchRunResponse200
    | SkipNextSavedSearchRunResponse400
    | SkipNextSavedSearchRunResponse401
    | SkipNextSavedSearchRunResponse402
    | SkipNextSavedSearchRunResponse403
    | SkipNextSavedSearchRunResponse404
    | SkipNextSavedSearchRunResponse422
    | SkipNextSavedSearchRunResponse429
    | SkipNextSavedSearchRunResponse500
    | SkipNextSavedSearchRunResponse503
    | None
):
    """Skip next saved search auto-run

     Skip the next scheduled auto-run for a saved search. The search will resume its normal schedule
    after one skipped cycle. Manual runs are not affected.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (SkipNextSavedSearchRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SkipNextSavedSearchRunResponse200 | SkipNextSavedSearchRunResponse400 | SkipNextSavedSearchRunResponse401 | SkipNextSavedSearchRunResponse402 | SkipNextSavedSearchRunResponse403 | SkipNextSavedSearchRunResponse404 | SkipNextSavedSearchRunResponse422 | SkipNextSavedSearchRunResponse429 | SkipNextSavedSearchRunResponse500 | SkipNextSavedSearchRunResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
