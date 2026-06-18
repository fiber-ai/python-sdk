from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.standardize_company_bulk_body import StandardizeCompanyBulkBody
from ...models.standardize_company_bulk_response_200 import StandardizeCompanyBulkResponse200
from ...models.standardize_company_bulk_response_400 import StandardizeCompanyBulkResponse400
from ...models.standardize_company_bulk_response_401 import StandardizeCompanyBulkResponse401
from ...models.standardize_company_bulk_response_402 import StandardizeCompanyBulkResponse402
from ...models.standardize_company_bulk_response_403 import StandardizeCompanyBulkResponse403
from ...models.standardize_company_bulk_response_404 import StandardizeCompanyBulkResponse404
from ...models.standardize_company_bulk_response_422 import StandardizeCompanyBulkResponse422
from ...models.standardize_company_bulk_response_429 import StandardizeCompanyBulkResponse429
from ...models.standardize_company_bulk_response_500 import StandardizeCompanyBulkResponse500
from ...models.standardize_company_bulk_response_503 import StandardizeCompanyBulkResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: StandardizeCompanyBulkBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/standardize/company/bulk",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StandardizeCompanyBulkResponse200
    | StandardizeCompanyBulkResponse400
    | StandardizeCompanyBulkResponse401
    | StandardizeCompanyBulkResponse402
    | StandardizeCompanyBulkResponse403
    | StandardizeCompanyBulkResponse404
    | StandardizeCompanyBulkResponse422
    | StandardizeCompanyBulkResponse429
    | StandardizeCompanyBulkResponse500
    | StandardizeCompanyBulkResponse503
    | None
):
    if response.status_code == 200:
        response_200 = StandardizeCompanyBulkResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StandardizeCompanyBulkResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StandardizeCompanyBulkResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = StandardizeCompanyBulkResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = StandardizeCompanyBulkResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StandardizeCompanyBulkResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = StandardizeCompanyBulkResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = StandardizeCompanyBulkResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = StandardizeCompanyBulkResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = StandardizeCompanyBulkResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StandardizeCompanyBulkResponse200
    | StandardizeCompanyBulkResponse400
    | StandardizeCompanyBulkResponse401
    | StandardizeCompanyBulkResponse402
    | StandardizeCompanyBulkResponse403
    | StandardizeCompanyBulkResponse404
    | StandardizeCompanyBulkResponse422
    | StandardizeCompanyBulkResponse429
    | StandardizeCompanyBulkResponse500
    | StandardizeCompanyBulkResponse503
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
    body: StandardizeCompanyBulkBody,
) -> Response[
    StandardizeCompanyBulkResponse200
    | StandardizeCompanyBulkResponse400
    | StandardizeCompanyBulkResponse401
    | StandardizeCompanyBulkResponse402
    | StandardizeCompanyBulkResponse403
    | StandardizeCompanyBulkResponse404
    | StandardizeCompanyBulkResponse422
    | StandardizeCompanyBulkResponse429
    | StandardizeCompanyBulkResponse500
    | StandardizeCompanyBulkResponse503
]:
    r"""Bulk standardize LinkedIn company identifiers

     Resolves many company LinkedIn identifiers (slug, organization ID, or URL) to standardized LinkedIn
    company URLs with metadata. Unresolved identifiers are listed separately and are not charged. If you
    have company names or domains instead of LinkedIn identifiers, use the bulk kitchen sink endpoint
    (POST /v1/kitchen-sink/bulk/company) instead.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company standardized&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (StandardizeCompanyBulkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StandardizeCompanyBulkResponse200 | StandardizeCompanyBulkResponse400 | StandardizeCompanyBulkResponse401 | StandardizeCompanyBulkResponse402 | StandardizeCompanyBulkResponse403 | StandardizeCompanyBulkResponse404 | StandardizeCompanyBulkResponse422 | StandardizeCompanyBulkResponse429 | StandardizeCompanyBulkResponse500 | StandardizeCompanyBulkResponse503]
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
    body: StandardizeCompanyBulkBody,
) -> (
    StandardizeCompanyBulkResponse200
    | StandardizeCompanyBulkResponse400
    | StandardizeCompanyBulkResponse401
    | StandardizeCompanyBulkResponse402
    | StandardizeCompanyBulkResponse403
    | StandardizeCompanyBulkResponse404
    | StandardizeCompanyBulkResponse422
    | StandardizeCompanyBulkResponse429
    | StandardizeCompanyBulkResponse500
    | StandardizeCompanyBulkResponse503
    | None
):
    r"""Bulk standardize LinkedIn company identifiers

     Resolves many company LinkedIn identifiers (slug, organization ID, or URL) to standardized LinkedIn
    company URLs with metadata. Unresolved identifiers are listed separately and are not charged. If you
    have company names or domains instead of LinkedIn identifiers, use the bulk kitchen sink endpoint
    (POST /v1/kitchen-sink/bulk/company) instead.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company standardized&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (StandardizeCompanyBulkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StandardizeCompanyBulkResponse200 | StandardizeCompanyBulkResponse400 | StandardizeCompanyBulkResponse401 | StandardizeCompanyBulkResponse402 | StandardizeCompanyBulkResponse403 | StandardizeCompanyBulkResponse404 | StandardizeCompanyBulkResponse422 | StandardizeCompanyBulkResponse429 | StandardizeCompanyBulkResponse500 | StandardizeCompanyBulkResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StandardizeCompanyBulkBody,
) -> Response[
    StandardizeCompanyBulkResponse200
    | StandardizeCompanyBulkResponse400
    | StandardizeCompanyBulkResponse401
    | StandardizeCompanyBulkResponse402
    | StandardizeCompanyBulkResponse403
    | StandardizeCompanyBulkResponse404
    | StandardizeCompanyBulkResponse422
    | StandardizeCompanyBulkResponse429
    | StandardizeCompanyBulkResponse500
    | StandardizeCompanyBulkResponse503
]:
    r"""Bulk standardize LinkedIn company identifiers

     Resolves many company LinkedIn identifiers (slug, organization ID, or URL) to standardized LinkedIn
    company URLs with metadata. Unresolved identifiers are listed separately and are not charged. If you
    have company names or domains instead of LinkedIn identifiers, use the bulk kitchen sink endpoint
    (POST /v1/kitchen-sink/bulk/company) instead.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company standardized&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (StandardizeCompanyBulkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StandardizeCompanyBulkResponse200 | StandardizeCompanyBulkResponse400 | StandardizeCompanyBulkResponse401 | StandardizeCompanyBulkResponse402 | StandardizeCompanyBulkResponse403 | StandardizeCompanyBulkResponse404 | StandardizeCompanyBulkResponse422 | StandardizeCompanyBulkResponse429 | StandardizeCompanyBulkResponse500 | StandardizeCompanyBulkResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StandardizeCompanyBulkBody,
) -> (
    StandardizeCompanyBulkResponse200
    | StandardizeCompanyBulkResponse400
    | StandardizeCompanyBulkResponse401
    | StandardizeCompanyBulkResponse402
    | StandardizeCompanyBulkResponse403
    | StandardizeCompanyBulkResponse404
    | StandardizeCompanyBulkResponse422
    | StandardizeCompanyBulkResponse429
    | StandardizeCompanyBulkResponse500
    | StandardizeCompanyBulkResponse503
    | None
):
    r"""Bulk standardize LinkedIn company identifiers

     Resolves many company LinkedIn identifiers (slug, organization ID, or URL) to standardized LinkedIn
    company URLs with metadata. Unresolved identifiers are listed separately and are not charged. If you
    have company names or domains instead of LinkedIn identifiers, use the bulk kitchen sink endpoint
    (POST /v1/kitchen-sink/bulk/company) instead.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company standardized&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (StandardizeCompanyBulkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StandardizeCompanyBulkResponse200 | StandardizeCompanyBulkResponse400 | StandardizeCompanyBulkResponse401 | StandardizeCompanyBulkResponse402 | StandardizeCompanyBulkResponse403 | StandardizeCompanyBulkResponse404 | StandardizeCompanyBulkResponse422 | StandardizeCompanyBulkResponse429 | StandardizeCompanyBulkResponse500 | StandardizeCompanyBulkResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
