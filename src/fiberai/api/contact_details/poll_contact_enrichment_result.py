from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.poll_contact_enrichment_result_body import PollContactEnrichmentResultBody
from ...models.poll_contact_enrichment_result_response_200 import PollContactEnrichmentResultResponse200
from ...models.poll_contact_enrichment_result_response_400 import PollContactEnrichmentResultResponse400
from ...models.poll_contact_enrichment_result_response_401 import PollContactEnrichmentResultResponse401
from ...models.poll_contact_enrichment_result_response_402 import PollContactEnrichmentResultResponse402
from ...models.poll_contact_enrichment_result_response_403 import PollContactEnrichmentResultResponse403
from ...models.poll_contact_enrichment_result_response_404 import PollContactEnrichmentResultResponse404
from ...models.poll_contact_enrichment_result_response_429 import PollContactEnrichmentResultResponse429
from ...models.poll_contact_enrichment_result_response_500 import PollContactEnrichmentResultResponse500
from ...models.poll_contact_enrichment_result_response_503 import PollContactEnrichmentResultResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PollContactEnrichmentResultBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PollContactEnrichmentResultResponse200
    | PollContactEnrichmentResultResponse400
    | PollContactEnrichmentResultResponse401
    | PollContactEnrichmentResultResponse402
    | PollContactEnrichmentResultResponse403
    | PollContactEnrichmentResultResponse404
    | PollContactEnrichmentResultResponse429
    | PollContactEnrichmentResultResponse500
    | PollContactEnrichmentResultResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PollContactEnrichmentResultResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PollContactEnrichmentResultResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PollContactEnrichmentResultResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PollContactEnrichmentResultResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PollContactEnrichmentResultResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PollContactEnrichmentResultResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PollContactEnrichmentResultResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PollContactEnrichmentResultResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PollContactEnrichmentResultResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PollContactEnrichmentResultResponse200
    | PollContactEnrichmentResultResponse400
    | PollContactEnrichmentResultResponse401
    | PollContactEnrichmentResultResponse402
    | PollContactEnrichmentResultResponse403
    | PollContactEnrichmentResultResponse404
    | PollContactEnrichmentResultResponse429
    | PollContactEnrichmentResultResponse500
    | PollContactEnrichmentResultResponse503
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
    body: PollContactEnrichmentResultBody,
) -> Response[
    PollContactEnrichmentResultResponse200
    | PollContactEnrichmentResultResponse400
    | PollContactEnrichmentResultResponse401
    | PollContactEnrichmentResultResponse402
    | PollContactEnrichmentResultResponse403
    | PollContactEnrichmentResultResponse404
    | PollContactEnrichmentResultResponse429
    | PollContactEnrichmentResultResponse500
    | PollContactEnrichmentResultResponse503
]:
    """Poll contact details fetching task

     Polls an asynchronous contact detail enrichment task. Call this with the task ID returned from the
    'Start fetching person's contact details' endpoint.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    Args:
        body (PollContactEnrichmentResultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollContactEnrichmentResultResponse200 | PollContactEnrichmentResultResponse400 | PollContactEnrichmentResultResponse401 | PollContactEnrichmentResultResponse402 | PollContactEnrichmentResultResponse403 | PollContactEnrichmentResultResponse404 | PollContactEnrichmentResultResponse429 | PollContactEnrichmentResultResponse500 | PollContactEnrichmentResultResponse503]
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
    body: PollContactEnrichmentResultBody,
) -> (
    PollContactEnrichmentResultResponse200
    | PollContactEnrichmentResultResponse400
    | PollContactEnrichmentResultResponse401
    | PollContactEnrichmentResultResponse402
    | PollContactEnrichmentResultResponse403
    | PollContactEnrichmentResultResponse404
    | PollContactEnrichmentResultResponse429
    | PollContactEnrichmentResultResponse500
    | PollContactEnrichmentResultResponse503
    | None
):
    """Poll contact details fetching task

     Polls an asynchronous contact detail enrichment task. Call this with the task ID returned from the
    'Start fetching person's contact details' endpoint.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    Args:
        body (PollContactEnrichmentResultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollContactEnrichmentResultResponse200 | PollContactEnrichmentResultResponse400 | PollContactEnrichmentResultResponse401 | PollContactEnrichmentResultResponse402 | PollContactEnrichmentResultResponse403 | PollContactEnrichmentResultResponse404 | PollContactEnrichmentResultResponse429 | PollContactEnrichmentResultResponse500 | PollContactEnrichmentResultResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PollContactEnrichmentResultBody,
) -> Response[
    PollContactEnrichmentResultResponse200
    | PollContactEnrichmentResultResponse400
    | PollContactEnrichmentResultResponse401
    | PollContactEnrichmentResultResponse402
    | PollContactEnrichmentResultResponse403
    | PollContactEnrichmentResultResponse404
    | PollContactEnrichmentResultResponse429
    | PollContactEnrichmentResultResponse500
    | PollContactEnrichmentResultResponse503
]:
    """Poll contact details fetching task

     Polls an asynchronous contact detail enrichment task. Call this with the task ID returned from the
    'Start fetching person's contact details' endpoint.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    Args:
        body (PollContactEnrichmentResultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollContactEnrichmentResultResponse200 | PollContactEnrichmentResultResponse400 | PollContactEnrichmentResultResponse401 | PollContactEnrichmentResultResponse402 | PollContactEnrichmentResultResponse403 | PollContactEnrichmentResultResponse404 | PollContactEnrichmentResultResponse429 | PollContactEnrichmentResultResponse500 | PollContactEnrichmentResultResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PollContactEnrichmentResultBody,
) -> (
    PollContactEnrichmentResultResponse200
    | PollContactEnrichmentResultResponse400
    | PollContactEnrichmentResultResponse401
    | PollContactEnrichmentResultResponse402
    | PollContactEnrichmentResultResponse403
    | PollContactEnrichmentResultResponse404
    | PollContactEnrichmentResultResponse429
    | PollContactEnrichmentResultResponse500
    | PollContactEnrichmentResultResponse503
    | None
):
    """Poll contact details fetching task

     Polls an asynchronous contact detail enrichment task. Call this with the task ID returned from the
    'Start fetching person's contact details' endpoint.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    Args:
        body (PollContactEnrichmentResultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollContactEnrichmentResultResponse200 | PollContactEnrichmentResultResponse400 | PollContactEnrichmentResultResponse401 | PollContactEnrichmentResultResponse402 | PollContactEnrichmentResultResponse403 | PollContactEnrichmentResultResponse404 | PollContactEnrichmentResultResponse429 | PollContactEnrichmentResultResponse500 | PollContactEnrichmentResultResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
