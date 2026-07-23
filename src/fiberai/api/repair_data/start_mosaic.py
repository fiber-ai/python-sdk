from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_mosaic_body import StartMosaicBody
from ...models.start_mosaic_response_200 import StartMosaicResponse200
from ...models.start_mosaic_response_400 import StartMosaicResponse400
from ...models.start_mosaic_response_401 import StartMosaicResponse401
from ...models.start_mosaic_response_402 import StartMosaicResponse402
from ...models.start_mosaic_response_403 import StartMosaicResponse403
from ...models.start_mosaic_response_404 import StartMosaicResponse404
from ...models.start_mosaic_response_422 import StartMosaicResponse422
from ...models.start_mosaic_response_429 import StartMosaicResponse429
from ...models.start_mosaic_response_500 import StartMosaicResponse500
from ...models.start_mosaic_response_503 import StartMosaicResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: StartMosaicBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/mosaic/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StartMosaicResponse200
    | StartMosaicResponse400
    | StartMosaicResponse401
    | StartMosaicResponse402
    | StartMosaicResponse403
    | StartMosaicResponse404
    | StartMosaicResponse422
    | StartMosaicResponse429
    | StartMosaicResponse500
    | StartMosaicResponse503
    | None
):
    if response.status_code == 200:
        response_200 = StartMosaicResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StartMosaicResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StartMosaicResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = StartMosaicResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = StartMosaicResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StartMosaicResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = StartMosaicResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = StartMosaicResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = StartMosaicResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = StartMosaicResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StartMosaicResponse200
    | StartMosaicResponse400
    | StartMosaicResponse401
    | StartMosaicResponse402
    | StartMosaicResponse403
    | StartMosaicResponse404
    | StartMosaicResponse422
    | StartMosaicResponse429
    | StartMosaicResponse500
    | StartMosaicResponse503
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
    body: StartMosaicBody,
) -> Response[
    StartMosaicResponse200
    | StartMosaicResponse400
    | StartMosaicResponse401
    | StartMosaicResponse402
    | StartMosaicResponse403
    | StartMosaicResponse404
    | StartMosaicResponse422
    | StartMosaicResponse429
    | StartMosaicResponse500
    | StartMosaicResponse503
]:
    r"""Start Mosaic CSV healing

     Starts an asynchronous Mosaic job that heals and enriches an arbitrary CSV, TXT, XLSX, or public
    Google Sheet. Pass a public HTTPS URL (Google Drive / Sheets, Dropbox, OneDrive, or a direct file
    link). The file is securely fetched and stored before processing. Credits are charged inside the
    background job after the file is parsed (based on row count and selected options). Use the polling
    endpoint with the returned run ID to retrieve status and download links.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the file is parsed inside the background
    job. Cost is based on the number of billable rows plus any optional enrichments (contact details,
    company details) you enable. The first Mosaic run for an organization may be a free trial (first
    1,000 rows free; overage billed against normal credits).&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary. Final charge depends on parsed row count and the options you
    select.\">ⓘ</span></span>

    Args:
        body (StartMosaicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartMosaicResponse200 | StartMosaicResponse400 | StartMosaicResponse401 | StartMosaicResponse402 | StartMosaicResponse403 | StartMosaicResponse404 | StartMosaicResponse422 | StartMosaicResponse429 | StartMosaicResponse500 | StartMosaicResponse503]
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
    body: StartMosaicBody,
) -> (
    StartMosaicResponse200
    | StartMosaicResponse400
    | StartMosaicResponse401
    | StartMosaicResponse402
    | StartMosaicResponse403
    | StartMosaicResponse404
    | StartMosaicResponse422
    | StartMosaicResponse429
    | StartMosaicResponse500
    | StartMosaicResponse503
    | None
):
    r"""Start Mosaic CSV healing

     Starts an asynchronous Mosaic job that heals and enriches an arbitrary CSV, TXT, XLSX, or public
    Google Sheet. Pass a public HTTPS URL (Google Drive / Sheets, Dropbox, OneDrive, or a direct file
    link). The file is securely fetched and stored before processing. Credits are charged inside the
    background job after the file is parsed (based on row count and selected options). Use the polling
    endpoint with the returned run ID to retrieve status and download links.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the file is parsed inside the background
    job. Cost is based on the number of billable rows plus any optional enrichments (contact details,
    company details) you enable. The first Mosaic run for an organization may be a free trial (first
    1,000 rows free; overage billed against normal credits).&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary. Final charge depends on parsed row count and the options you
    select.\">ⓘ</span></span>

    Args:
        body (StartMosaicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartMosaicResponse200 | StartMosaicResponse400 | StartMosaicResponse401 | StartMosaicResponse402 | StartMosaicResponse403 | StartMosaicResponse404 | StartMosaicResponse422 | StartMosaicResponse429 | StartMosaicResponse500 | StartMosaicResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartMosaicBody,
) -> Response[
    StartMosaicResponse200
    | StartMosaicResponse400
    | StartMosaicResponse401
    | StartMosaicResponse402
    | StartMosaicResponse403
    | StartMosaicResponse404
    | StartMosaicResponse422
    | StartMosaicResponse429
    | StartMosaicResponse500
    | StartMosaicResponse503
]:
    r"""Start Mosaic CSV healing

     Starts an asynchronous Mosaic job that heals and enriches an arbitrary CSV, TXT, XLSX, or public
    Google Sheet. Pass a public HTTPS URL (Google Drive / Sheets, Dropbox, OneDrive, or a direct file
    link). The file is securely fetched and stored before processing. Credits are charged inside the
    background job after the file is parsed (based on row count and selected options). Use the polling
    endpoint with the returned run ID to retrieve status and download links.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the file is parsed inside the background
    job. Cost is based on the number of billable rows plus any optional enrichments (contact details,
    company details) you enable. The first Mosaic run for an organization may be a free trial (first
    1,000 rows free; overage billed against normal credits).&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary. Final charge depends on parsed row count and the options you
    select.\">ⓘ</span></span>

    Args:
        body (StartMosaicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartMosaicResponse200 | StartMosaicResponse400 | StartMosaicResponse401 | StartMosaicResponse402 | StartMosaicResponse403 | StartMosaicResponse404 | StartMosaicResponse422 | StartMosaicResponse429 | StartMosaicResponse500 | StartMosaicResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StartMosaicBody,
) -> (
    StartMosaicResponse200
    | StartMosaicResponse400
    | StartMosaicResponse401
    | StartMosaicResponse402
    | StartMosaicResponse403
    | StartMosaicResponse404
    | StartMosaicResponse422
    | StartMosaicResponse429
    | StartMosaicResponse500
    | StartMosaicResponse503
    | None
):
    r"""Start Mosaic CSV healing

     Starts an asynchronous Mosaic job that heals and enriches an arbitrary CSV, TXT, XLSX, or public
    Google Sheet. Pass a public HTTPS URL (Google Drive / Sheets, Dropbox, OneDrive, or a direct file
    link). The file is securely fetched and stored before processing. Credits are charged inside the
    background job after the file is parsed (based on row count and selected options). Use the polling
    endpoint with the returned run ID to retrieve status and download links.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the file is parsed inside the background
    job. Cost is based on the number of billable rows plus any optional enrichments (contact details,
    company details) you enable. The first Mosaic run for an organization may be a free trial (first
    1,000 rows free; overage billed against normal credits).&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary. Final charge depends on parsed row count and the options you
    select.\">ⓘ</span></span>

    Args:
        body (StartMosaicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartMosaicResponse200 | StartMosaicResponse400 | StartMosaicResponse401 | StartMosaicResponse402 | StartMosaicResponse403 | StartMosaicResponse404 | StartMosaicResponse422 | StartMosaicResponse429 | StartMosaicResponse500 | StartMosaicResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
