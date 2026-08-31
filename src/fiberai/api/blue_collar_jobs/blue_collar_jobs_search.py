from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blue_collar_jobs_search_body import BlueCollarJobsSearchBody
from ...models.blue_collar_jobs_search_response_200 import BlueCollarJobsSearchResponse200
from ...models.blue_collar_jobs_search_response_400 import BlueCollarJobsSearchResponse400
from ...models.blue_collar_jobs_search_response_401 import BlueCollarJobsSearchResponse401
from ...models.blue_collar_jobs_search_response_402 import BlueCollarJobsSearchResponse402
from ...models.blue_collar_jobs_search_response_403 import BlueCollarJobsSearchResponse403
from ...models.blue_collar_jobs_search_response_404 import BlueCollarJobsSearchResponse404
from ...models.blue_collar_jobs_search_response_422 import BlueCollarJobsSearchResponse422
from ...models.blue_collar_jobs_search_response_429 import BlueCollarJobsSearchResponse429
from ...models.blue_collar_jobs_search_response_500 import BlueCollarJobsSearchResponse500
from ...models.blue_collar_jobs_search_response_503 import BlueCollarJobsSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: BlueCollarJobsSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/blue-collar-jobs/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BlueCollarJobsSearchResponse200
    | BlueCollarJobsSearchResponse400
    | BlueCollarJobsSearchResponse401
    | BlueCollarJobsSearchResponse402
    | BlueCollarJobsSearchResponse403
    | BlueCollarJobsSearchResponse404
    | BlueCollarJobsSearchResponse422
    | BlueCollarJobsSearchResponse429
    | BlueCollarJobsSearchResponse500
    | BlueCollarJobsSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = BlueCollarJobsSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BlueCollarJobsSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BlueCollarJobsSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = BlueCollarJobsSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = BlueCollarJobsSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = BlueCollarJobsSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = BlueCollarJobsSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = BlueCollarJobsSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = BlueCollarJobsSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = BlueCollarJobsSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BlueCollarJobsSearchResponse200
    | BlueCollarJobsSearchResponse400
    | BlueCollarJobsSearchResponse401
    | BlueCollarJobsSearchResponse402
    | BlueCollarJobsSearchResponse403
    | BlueCollarJobsSearchResponse404
    | BlueCollarJobsSearchResponse422
    | BlueCollarJobsSearchResponse429
    | BlueCollarJobsSearchResponse500
    | BlueCollarJobsSearchResponse503
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
    body: BlueCollarJobsSearchBody,
) -> Response[
    BlueCollarJobsSearchResponse200
    | BlueCollarJobsSearchResponse400
    | BlueCollarJobsSearchResponse401
    | BlueCollarJobsSearchResponse402
    | BlueCollarJobsSearchResponse403
    | BlueCollarJobsSearchResponse404
    | BlueCollarJobsSearchResponse422
    | BlueCollarJobsSearchResponse429
    | BlueCollarJobsSearchResponse500
    | BlueCollarJobsSearchResponse503
]:
    """Search blue collar job listings

     Search blue collar and trade job postings. Ideal for finding service, manufacturing, trades, and
    other non-desk positions. Currently US-only. Supports search by company, job title/keyword, and
    location. Supports pagination via nextPageToken.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (BlueCollarJobsSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlueCollarJobsSearchResponse200 | BlueCollarJobsSearchResponse400 | BlueCollarJobsSearchResponse401 | BlueCollarJobsSearchResponse402 | BlueCollarJobsSearchResponse403 | BlueCollarJobsSearchResponse404 | BlueCollarJobsSearchResponse422 | BlueCollarJobsSearchResponse429 | BlueCollarJobsSearchResponse500 | BlueCollarJobsSearchResponse503]
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
    body: BlueCollarJobsSearchBody,
) -> (
    BlueCollarJobsSearchResponse200
    | BlueCollarJobsSearchResponse400
    | BlueCollarJobsSearchResponse401
    | BlueCollarJobsSearchResponse402
    | BlueCollarJobsSearchResponse403
    | BlueCollarJobsSearchResponse404
    | BlueCollarJobsSearchResponse422
    | BlueCollarJobsSearchResponse429
    | BlueCollarJobsSearchResponse500
    | BlueCollarJobsSearchResponse503
    | None
):
    """Search blue collar job listings

     Search blue collar and trade job postings. Ideal for finding service, manufacturing, trades, and
    other non-desk positions. Currently US-only. Supports search by company, job title/keyword, and
    location. Supports pagination via nextPageToken.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (BlueCollarJobsSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlueCollarJobsSearchResponse200 | BlueCollarJobsSearchResponse400 | BlueCollarJobsSearchResponse401 | BlueCollarJobsSearchResponse402 | BlueCollarJobsSearchResponse403 | BlueCollarJobsSearchResponse404 | BlueCollarJobsSearchResponse422 | BlueCollarJobsSearchResponse429 | BlueCollarJobsSearchResponse500 | BlueCollarJobsSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BlueCollarJobsSearchBody,
) -> Response[
    BlueCollarJobsSearchResponse200
    | BlueCollarJobsSearchResponse400
    | BlueCollarJobsSearchResponse401
    | BlueCollarJobsSearchResponse402
    | BlueCollarJobsSearchResponse403
    | BlueCollarJobsSearchResponse404
    | BlueCollarJobsSearchResponse422
    | BlueCollarJobsSearchResponse429
    | BlueCollarJobsSearchResponse500
    | BlueCollarJobsSearchResponse503
]:
    """Search blue collar job listings

     Search blue collar and trade job postings. Ideal for finding service, manufacturing, trades, and
    other non-desk positions. Currently US-only. Supports search by company, job title/keyword, and
    location. Supports pagination via nextPageToken.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (BlueCollarJobsSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlueCollarJobsSearchResponse200 | BlueCollarJobsSearchResponse400 | BlueCollarJobsSearchResponse401 | BlueCollarJobsSearchResponse402 | BlueCollarJobsSearchResponse403 | BlueCollarJobsSearchResponse404 | BlueCollarJobsSearchResponse422 | BlueCollarJobsSearchResponse429 | BlueCollarJobsSearchResponse500 | BlueCollarJobsSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BlueCollarJobsSearchBody,
) -> (
    BlueCollarJobsSearchResponse200
    | BlueCollarJobsSearchResponse400
    | BlueCollarJobsSearchResponse401
    | BlueCollarJobsSearchResponse402
    | BlueCollarJobsSearchResponse403
    | BlueCollarJobsSearchResponse404
    | BlueCollarJobsSearchResponse422
    | BlueCollarJobsSearchResponse429
    | BlueCollarJobsSearchResponse500
    | BlueCollarJobsSearchResponse503
    | None
):
    """Search blue collar job listings

     Search blue collar and trade job postings. Ideal for finding service, manufacturing, trades, and
    other non-desk positions. Currently US-only. Supports search by company, job title/keyword, and
    location. Supports pagination via nextPageToken.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per search&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (BlueCollarJobsSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlueCollarJobsSearchResponse200 | BlueCollarJobsSearchResponse400 | BlueCollarJobsSearchResponse401 | BlueCollarJobsSearchResponse402 | BlueCollarJobsSearchResponse403 | BlueCollarJobsSearchResponse404 | BlueCollarJobsSearchResponse422 | BlueCollarJobsSearchResponse429 | BlueCollarJobsSearchResponse500 | BlueCollarJobsSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
