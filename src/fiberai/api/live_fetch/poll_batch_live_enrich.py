from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.poll_batch_live_enrich_body import PollBatchLiveEnrichBody
from ...models.poll_batch_live_enrich_response_200 import PollBatchLiveEnrichResponse200
from ...models.poll_batch_live_enrich_response_400 import PollBatchLiveEnrichResponse400
from ...models.poll_batch_live_enrich_response_401 import PollBatchLiveEnrichResponse401
from ...models.poll_batch_live_enrich_response_402 import PollBatchLiveEnrichResponse402
from ...models.poll_batch_live_enrich_response_403 import PollBatchLiveEnrichResponse403
from ...models.poll_batch_live_enrich_response_404 import PollBatchLiveEnrichResponse404
from ...models.poll_batch_live_enrich_response_429 import PollBatchLiveEnrichResponse429
from ...models.poll_batch_live_enrich_response_500 import PollBatchLiveEnrichResponse500
from ...models.poll_batch_live_enrich_response_503 import PollBatchLiveEnrichResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PollBatchLiveEnrichBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/batch/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PollBatchLiveEnrichResponse200
    | PollBatchLiveEnrichResponse400
    | PollBatchLiveEnrichResponse401
    | PollBatchLiveEnrichResponse402
    | PollBatchLiveEnrichResponse403
    | PollBatchLiveEnrichResponse404
    | PollBatchLiveEnrichResponse429
    | PollBatchLiveEnrichResponse500
    | PollBatchLiveEnrichResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PollBatchLiveEnrichResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PollBatchLiveEnrichResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PollBatchLiveEnrichResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PollBatchLiveEnrichResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PollBatchLiveEnrichResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PollBatchLiveEnrichResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PollBatchLiveEnrichResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PollBatchLiveEnrichResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PollBatchLiveEnrichResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PollBatchLiveEnrichResponse200
    | PollBatchLiveEnrichResponse400
    | PollBatchLiveEnrichResponse401
    | PollBatchLiveEnrichResponse402
    | PollBatchLiveEnrichResponse403
    | PollBatchLiveEnrichResponse404
    | PollBatchLiveEnrichResponse429
    | PollBatchLiveEnrichResponse500
    | PollBatchLiveEnrichResponse503
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
    body: PollBatchLiveEnrichBody,
) -> Response[
    PollBatchLiveEnrichResponse200
    | PollBatchLiveEnrichResponse400
    | PollBatchLiveEnrichResponse401
    | PollBatchLiveEnrichResponse402
    | PollBatchLiveEnrichResponse403
    | PollBatchLiveEnrichResponse404
    | PollBatchLiveEnrichResponse429
    | PollBatchLiveEnrichResponse500
    | PollBatchLiveEnrichResponse503
]:
    """Poll batch live enrichment

     Polls a batch live enrichment task for progress and results. Returns paginated enrichment results as
    they complete. Call repeatedly until status is 'completed' or 'failed'.

    <span>⚡ <strong>Rate limit:</strong> 360 requests per 1 minute</span>

    Args:
        body (PollBatchLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollBatchLiveEnrichResponse200 | PollBatchLiveEnrichResponse400 | PollBatchLiveEnrichResponse401 | PollBatchLiveEnrichResponse402 | PollBatchLiveEnrichResponse403 | PollBatchLiveEnrichResponse404 | PollBatchLiveEnrichResponse429 | PollBatchLiveEnrichResponse500 | PollBatchLiveEnrichResponse503]
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
    body: PollBatchLiveEnrichBody,
) -> (
    PollBatchLiveEnrichResponse200
    | PollBatchLiveEnrichResponse400
    | PollBatchLiveEnrichResponse401
    | PollBatchLiveEnrichResponse402
    | PollBatchLiveEnrichResponse403
    | PollBatchLiveEnrichResponse404
    | PollBatchLiveEnrichResponse429
    | PollBatchLiveEnrichResponse500
    | PollBatchLiveEnrichResponse503
    | None
):
    """Poll batch live enrichment

     Polls a batch live enrichment task for progress and results. Returns paginated enrichment results as
    they complete. Call repeatedly until status is 'completed' or 'failed'.

    <span>⚡ <strong>Rate limit:</strong> 360 requests per 1 minute</span>

    Args:
        body (PollBatchLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollBatchLiveEnrichResponse200 | PollBatchLiveEnrichResponse400 | PollBatchLiveEnrichResponse401 | PollBatchLiveEnrichResponse402 | PollBatchLiveEnrichResponse403 | PollBatchLiveEnrichResponse404 | PollBatchLiveEnrichResponse429 | PollBatchLiveEnrichResponse500 | PollBatchLiveEnrichResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PollBatchLiveEnrichBody,
) -> Response[
    PollBatchLiveEnrichResponse200
    | PollBatchLiveEnrichResponse400
    | PollBatchLiveEnrichResponse401
    | PollBatchLiveEnrichResponse402
    | PollBatchLiveEnrichResponse403
    | PollBatchLiveEnrichResponse404
    | PollBatchLiveEnrichResponse429
    | PollBatchLiveEnrichResponse500
    | PollBatchLiveEnrichResponse503
]:
    """Poll batch live enrichment

     Polls a batch live enrichment task for progress and results. Returns paginated enrichment results as
    they complete. Call repeatedly until status is 'completed' or 'failed'.

    <span>⚡ <strong>Rate limit:</strong> 360 requests per 1 minute</span>

    Args:
        body (PollBatchLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollBatchLiveEnrichResponse200 | PollBatchLiveEnrichResponse400 | PollBatchLiveEnrichResponse401 | PollBatchLiveEnrichResponse402 | PollBatchLiveEnrichResponse403 | PollBatchLiveEnrichResponse404 | PollBatchLiveEnrichResponse429 | PollBatchLiveEnrichResponse500 | PollBatchLiveEnrichResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PollBatchLiveEnrichBody,
) -> (
    PollBatchLiveEnrichResponse200
    | PollBatchLiveEnrichResponse400
    | PollBatchLiveEnrichResponse401
    | PollBatchLiveEnrichResponse402
    | PollBatchLiveEnrichResponse403
    | PollBatchLiveEnrichResponse404
    | PollBatchLiveEnrichResponse429
    | PollBatchLiveEnrichResponse500
    | PollBatchLiveEnrichResponse503
    | None
):
    """Poll batch live enrichment

     Polls a batch live enrichment task for progress and results. Returns paginated enrichment results as
    they complete. Call repeatedly until status is 'completed' or 'failed'.

    <span>⚡ <strong>Rate limit:</strong> 360 requests per 1 minute</span>

    Args:
        body (PollBatchLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollBatchLiveEnrichResponse200 | PollBatchLiveEnrichResponse400 | PollBatchLiveEnrichResponse401 | PollBatchLiveEnrichResponse402 | PollBatchLiveEnrichResponse403 | PollBatchLiveEnrichResponse404 | PollBatchLiveEnrichResponse429 | PollBatchLiveEnrichResponse500 | PollBatchLiveEnrichResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
