from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_batch_live_enrich_body import StartBatchLiveEnrichBody
from ...models.start_batch_live_enrich_response_200 import StartBatchLiveEnrichResponse200
from ...models.start_batch_live_enrich_response_400 import StartBatchLiveEnrichResponse400
from ...models.start_batch_live_enrich_response_401 import StartBatchLiveEnrichResponse401
from ...models.start_batch_live_enrich_response_402 import StartBatchLiveEnrichResponse402
from ...models.start_batch_live_enrich_response_403 import StartBatchLiveEnrichResponse403
from ...models.start_batch_live_enrich_response_404 import StartBatchLiveEnrichResponse404
from ...models.start_batch_live_enrich_response_422 import StartBatchLiveEnrichResponse422
from ...models.start_batch_live_enrich_response_429 import StartBatchLiveEnrichResponse429
from ...models.start_batch_live_enrich_response_500 import StartBatchLiveEnrichResponse500
from ...models.start_batch_live_enrich_response_503 import StartBatchLiveEnrichResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: StartBatchLiveEnrichBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/batch/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StartBatchLiveEnrichResponse200
    | StartBatchLiveEnrichResponse400
    | StartBatchLiveEnrichResponse401
    | StartBatchLiveEnrichResponse402
    | StartBatchLiveEnrichResponse403
    | StartBatchLiveEnrichResponse404
    | StartBatchLiveEnrichResponse422
    | StartBatchLiveEnrichResponse429
    | StartBatchLiveEnrichResponse500
    | StartBatchLiveEnrichResponse503
    | None
):
    if response.status_code == 200:
        response_200 = StartBatchLiveEnrichResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StartBatchLiveEnrichResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StartBatchLiveEnrichResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = StartBatchLiveEnrichResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = StartBatchLiveEnrichResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StartBatchLiveEnrichResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = StartBatchLiveEnrichResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = StartBatchLiveEnrichResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = StartBatchLiveEnrichResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = StartBatchLiveEnrichResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StartBatchLiveEnrichResponse200
    | StartBatchLiveEnrichResponse400
    | StartBatchLiveEnrichResponse401
    | StartBatchLiveEnrichResponse402
    | StartBatchLiveEnrichResponse403
    | StartBatchLiveEnrichResponse404
    | StartBatchLiveEnrichResponse422
    | StartBatchLiveEnrichResponse429
    | StartBatchLiveEnrichResponse500
    | StartBatchLiveEnrichResponse503
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
    body: StartBatchLiveEnrichBody,
) -> Response[
    StartBatchLiveEnrichResponse200
    | StartBatchLiveEnrichResponse400
    | StartBatchLiveEnrichResponse401
    | StartBatchLiveEnrichResponse402
    | StartBatchLiveEnrichResponse403
    | StartBatchLiveEnrichResponse404
    | StartBatchLiveEnrichResponse422
    | StartBatchLiveEnrichResponse429
    | StartBatchLiveEnrichResponse500
    | StartBatchLiveEnrichResponse503
]:
    """Start batch live enrichment

     Starts a batch live enrichment job for multiple LinkedIn profiles or companies (up to 10,000). This
    is an asynchronous task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per live fetch&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (StartBatchLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartBatchLiveEnrichResponse200 | StartBatchLiveEnrichResponse400 | StartBatchLiveEnrichResponse401 | StartBatchLiveEnrichResponse402 | StartBatchLiveEnrichResponse403 | StartBatchLiveEnrichResponse404 | StartBatchLiveEnrichResponse422 | StartBatchLiveEnrichResponse429 | StartBatchLiveEnrichResponse500 | StartBatchLiveEnrichResponse503]
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
    body: StartBatchLiveEnrichBody,
) -> (
    StartBatchLiveEnrichResponse200
    | StartBatchLiveEnrichResponse400
    | StartBatchLiveEnrichResponse401
    | StartBatchLiveEnrichResponse402
    | StartBatchLiveEnrichResponse403
    | StartBatchLiveEnrichResponse404
    | StartBatchLiveEnrichResponse422
    | StartBatchLiveEnrichResponse429
    | StartBatchLiveEnrichResponse500
    | StartBatchLiveEnrichResponse503
    | None
):
    """Start batch live enrichment

     Starts a batch live enrichment job for multiple LinkedIn profiles or companies (up to 10,000). This
    is an asynchronous task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per live fetch&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (StartBatchLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartBatchLiveEnrichResponse200 | StartBatchLiveEnrichResponse400 | StartBatchLiveEnrichResponse401 | StartBatchLiveEnrichResponse402 | StartBatchLiveEnrichResponse403 | StartBatchLiveEnrichResponse404 | StartBatchLiveEnrichResponse422 | StartBatchLiveEnrichResponse429 | StartBatchLiveEnrichResponse500 | StartBatchLiveEnrichResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartBatchLiveEnrichBody,
) -> Response[
    StartBatchLiveEnrichResponse200
    | StartBatchLiveEnrichResponse400
    | StartBatchLiveEnrichResponse401
    | StartBatchLiveEnrichResponse402
    | StartBatchLiveEnrichResponse403
    | StartBatchLiveEnrichResponse404
    | StartBatchLiveEnrichResponse422
    | StartBatchLiveEnrichResponse429
    | StartBatchLiveEnrichResponse500
    | StartBatchLiveEnrichResponse503
]:
    """Start batch live enrichment

     Starts a batch live enrichment job for multiple LinkedIn profiles or companies (up to 10,000). This
    is an asynchronous task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per live fetch&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (StartBatchLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartBatchLiveEnrichResponse200 | StartBatchLiveEnrichResponse400 | StartBatchLiveEnrichResponse401 | StartBatchLiveEnrichResponse402 | StartBatchLiveEnrichResponse403 | StartBatchLiveEnrichResponse404 | StartBatchLiveEnrichResponse422 | StartBatchLiveEnrichResponse429 | StartBatchLiveEnrichResponse500 | StartBatchLiveEnrichResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StartBatchLiveEnrichBody,
) -> (
    StartBatchLiveEnrichResponse200
    | StartBatchLiveEnrichResponse400
    | StartBatchLiveEnrichResponse401
    | StartBatchLiveEnrichResponse402
    | StartBatchLiveEnrichResponse403
    | StartBatchLiveEnrichResponse404
    | StartBatchLiveEnrichResponse422
    | StartBatchLiveEnrichResponse429
    | StartBatchLiveEnrichResponse500
    | StartBatchLiveEnrichResponse503
    | None
):
    """Start batch live enrichment

     Starts a batch live enrichment job for multiple LinkedIn profiles or companies (up to 10,000). This
    is an asynchronous task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per live fetch&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (StartBatchLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartBatchLiveEnrichResponse200 | StartBatchLiveEnrichResponse400 | StartBatchLiveEnrichResponse401 | StartBatchLiveEnrichResponse402 | StartBatchLiveEnrichResponse403 | StartBatchLiveEnrichResponse404 | StartBatchLiveEnrichResponse422 | StartBatchLiveEnrichResponse429 | StartBatchLiveEnrichResponse500 | StartBatchLiveEnrichResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
