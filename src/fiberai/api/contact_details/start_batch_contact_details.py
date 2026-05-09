from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_batch_contact_details_body import StartBatchContactDetailsBody
from ...models.start_batch_contact_details_response_200 import StartBatchContactDetailsResponse200
from ...models.start_batch_contact_details_response_400 import StartBatchContactDetailsResponse400
from ...models.start_batch_contact_details_response_401 import StartBatchContactDetailsResponse401
from ...models.start_batch_contact_details_response_402 import StartBatchContactDetailsResponse402
from ...models.start_batch_contact_details_response_403 import StartBatchContactDetailsResponse403
from ...models.start_batch_contact_details_response_404 import StartBatchContactDetailsResponse404
from ...models.start_batch_contact_details_response_429 import StartBatchContactDetailsResponse429
from ...models.start_batch_contact_details_response_500 import StartBatchContactDetailsResponse500
from ...models.start_batch_contact_details_response_503 import StartBatchContactDetailsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: StartBatchContactDetailsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/batch/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StartBatchContactDetailsResponse200
    | StartBatchContactDetailsResponse400
    | StartBatchContactDetailsResponse401
    | StartBatchContactDetailsResponse402
    | StartBatchContactDetailsResponse403
    | StartBatchContactDetailsResponse404
    | StartBatchContactDetailsResponse429
    | StartBatchContactDetailsResponse500
    | StartBatchContactDetailsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = StartBatchContactDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StartBatchContactDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StartBatchContactDetailsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = StartBatchContactDetailsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = StartBatchContactDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StartBatchContactDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = StartBatchContactDetailsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = StartBatchContactDetailsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = StartBatchContactDetailsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StartBatchContactDetailsResponse200
    | StartBatchContactDetailsResponse400
    | StartBatchContactDetailsResponse401
    | StartBatchContactDetailsResponse402
    | StartBatchContactDetailsResponse403
    | StartBatchContactDetailsResponse404
    | StartBatchContactDetailsResponse429
    | StartBatchContactDetailsResponse500
    | StartBatchContactDetailsResponse503
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
    body: StartBatchContactDetailsBody,
) -> Response[
    StartBatchContactDetailsResponse200
    | StartBatchContactDetailsResponse400
    | StartBatchContactDetailsResponse401
    | StartBatchContactDetailsResponse402
    | StartBatchContactDetailsResponse403
    | StartBatchContactDetailsResponse404
    | StartBatchContactDetailsResponse429
    | StartBatchContactDetailsResponse500
    | StartBatchContactDetailsResponse503
]:
    r"""Start batch contact details

     Starts fetching contact details for multiple people (up to 2000) in batch. This is an asynchronous
    task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Credits are charged upfront for all unique people queued (after deduping).
    Undelivered data is refunded per operation.\">ⓘ</span></span>

    Args:
        body (StartBatchContactDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartBatchContactDetailsResponse200 | StartBatchContactDetailsResponse400 | StartBatchContactDetailsResponse401 | StartBatchContactDetailsResponse402 | StartBatchContactDetailsResponse403 | StartBatchContactDetailsResponse404 | StartBatchContactDetailsResponse429 | StartBatchContactDetailsResponse500 | StartBatchContactDetailsResponse503]
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
    body: StartBatchContactDetailsBody,
) -> (
    StartBatchContactDetailsResponse200
    | StartBatchContactDetailsResponse400
    | StartBatchContactDetailsResponse401
    | StartBatchContactDetailsResponse402
    | StartBatchContactDetailsResponse403
    | StartBatchContactDetailsResponse404
    | StartBatchContactDetailsResponse429
    | StartBatchContactDetailsResponse500
    | StartBatchContactDetailsResponse503
    | None
):
    r"""Start batch contact details

     Starts fetching contact details for multiple people (up to 2000) in batch. This is an asynchronous
    task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Credits are charged upfront for all unique people queued (after deduping).
    Undelivered data is refunded per operation.\">ⓘ</span></span>

    Args:
        body (StartBatchContactDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartBatchContactDetailsResponse200 | StartBatchContactDetailsResponse400 | StartBatchContactDetailsResponse401 | StartBatchContactDetailsResponse402 | StartBatchContactDetailsResponse403 | StartBatchContactDetailsResponse404 | StartBatchContactDetailsResponse429 | StartBatchContactDetailsResponse500 | StartBatchContactDetailsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartBatchContactDetailsBody,
) -> Response[
    StartBatchContactDetailsResponse200
    | StartBatchContactDetailsResponse400
    | StartBatchContactDetailsResponse401
    | StartBatchContactDetailsResponse402
    | StartBatchContactDetailsResponse403
    | StartBatchContactDetailsResponse404
    | StartBatchContactDetailsResponse429
    | StartBatchContactDetailsResponse500
    | StartBatchContactDetailsResponse503
]:
    r"""Start batch contact details

     Starts fetching contact details for multiple people (up to 2000) in batch. This is an asynchronous
    task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Credits are charged upfront for all unique people queued (after deduping).
    Undelivered data is refunded per operation.\">ⓘ</span></span>

    Args:
        body (StartBatchContactDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartBatchContactDetailsResponse200 | StartBatchContactDetailsResponse400 | StartBatchContactDetailsResponse401 | StartBatchContactDetailsResponse402 | StartBatchContactDetailsResponse403 | StartBatchContactDetailsResponse404 | StartBatchContactDetailsResponse429 | StartBatchContactDetailsResponse500 | StartBatchContactDetailsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StartBatchContactDetailsBody,
) -> (
    StartBatchContactDetailsResponse200
    | StartBatchContactDetailsResponse400
    | StartBatchContactDetailsResponse401
    | StartBatchContactDetailsResponse402
    | StartBatchContactDetailsResponse403
    | StartBatchContactDetailsResponse404
    | StartBatchContactDetailsResponse429
    | StartBatchContactDetailsResponse500
    | StartBatchContactDetailsResponse503
    | None
):
    r"""Start batch contact details

     Starts fetching contact details for multiple people (up to 2000) in batch. This is an asynchronous
    task; use the polling endpoint to check progress and get results.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay only for the data you request:<br />• 5 credits for all phone
    numbers AND all emails<br />• 2 credits for work email only<br />• 2 credits for personal email
    only<br />• 3 credits for phone only&nbsp;<span title=\"Pricing shown is default pricing. Actual
    pricing may vary. Credits are charged upfront for all unique people queued (after deduping).
    Undelivered data is refunded per operation.\">ⓘ</span></span>

    Args:
        body (StartBatchContactDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartBatchContactDetailsResponse200 | StartBatchContactDetailsResponse400 | StartBatchContactDetailsResponse401 | StartBatchContactDetailsResponse402 | StartBatchContactDetailsResponse403 | StartBatchContactDetailsResponse404 | StartBatchContactDetailsResponse429 | StartBatchContactDetailsResponse500 | StartBatchContactDetailsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
