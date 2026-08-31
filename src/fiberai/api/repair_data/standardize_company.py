from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.standardize_company_body import StandardizeCompanyBody
from ...models.standardize_company_response_200 import StandardizeCompanyResponse200
from ...models.standardize_company_response_400 import StandardizeCompanyResponse400
from ...models.standardize_company_response_401 import StandardizeCompanyResponse401
from ...models.standardize_company_response_402 import StandardizeCompanyResponse402
from ...models.standardize_company_response_403 import StandardizeCompanyResponse403
from ...models.standardize_company_response_404 import StandardizeCompanyResponse404
from ...models.standardize_company_response_422 import StandardizeCompanyResponse422
from ...models.standardize_company_response_429 import StandardizeCompanyResponse429
from ...models.standardize_company_response_500 import StandardizeCompanyResponse500
from ...models.standardize_company_response_503 import StandardizeCompanyResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: StandardizeCompanyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/standardize/company/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StandardizeCompanyResponse200
    | StandardizeCompanyResponse400
    | StandardizeCompanyResponse401
    | StandardizeCompanyResponse402
    | StandardizeCompanyResponse403
    | StandardizeCompanyResponse404
    | StandardizeCompanyResponse422
    | StandardizeCompanyResponse429
    | StandardizeCompanyResponse500
    | StandardizeCompanyResponse503
    | None
):
    if response.status_code == 200:
        response_200 = StandardizeCompanyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StandardizeCompanyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StandardizeCompanyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = StandardizeCompanyResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = StandardizeCompanyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StandardizeCompanyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = StandardizeCompanyResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = StandardizeCompanyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = StandardizeCompanyResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = StandardizeCompanyResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StandardizeCompanyResponse200
    | StandardizeCompanyResponse400
    | StandardizeCompanyResponse401
    | StandardizeCompanyResponse402
    | StandardizeCompanyResponse403
    | StandardizeCompanyResponse404
    | StandardizeCompanyResponse422
    | StandardizeCompanyResponse429
    | StandardizeCompanyResponse500
    | StandardizeCompanyResponse503
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
    body: StandardizeCompanyBody,
) -> Response[
    StandardizeCompanyResponse200
    | StandardizeCompanyResponse400
    | StandardizeCompanyResponse401
    | StandardizeCompanyResponse402
    | StandardizeCompanyResponse403
    | StandardizeCompanyResponse404
    | StandardizeCompanyResponse422
    | StandardizeCompanyResponse429
    | StandardizeCompanyResponse500
    | StandardizeCompanyResponse503
]:
    """Standardize LinkedIn company identifier

     Resolves a company LinkedIn identifier (slug, organization ID, or URL) to a standardized LinkedIn
    company URL with metadata. Useful for normalizing company identifiers from different sources.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company standardized&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (StandardizeCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StandardizeCompanyResponse200 | StandardizeCompanyResponse400 | StandardizeCompanyResponse401 | StandardizeCompanyResponse402 | StandardizeCompanyResponse403 | StandardizeCompanyResponse404 | StandardizeCompanyResponse422 | StandardizeCompanyResponse429 | StandardizeCompanyResponse500 | StandardizeCompanyResponse503]
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
    body: StandardizeCompanyBody,
) -> (
    StandardizeCompanyResponse200
    | StandardizeCompanyResponse400
    | StandardizeCompanyResponse401
    | StandardizeCompanyResponse402
    | StandardizeCompanyResponse403
    | StandardizeCompanyResponse404
    | StandardizeCompanyResponse422
    | StandardizeCompanyResponse429
    | StandardizeCompanyResponse500
    | StandardizeCompanyResponse503
    | None
):
    """Standardize LinkedIn company identifier

     Resolves a company LinkedIn identifier (slug, organization ID, or URL) to a standardized LinkedIn
    company URL with metadata. Useful for normalizing company identifiers from different sources.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company standardized&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (StandardizeCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StandardizeCompanyResponse200 | StandardizeCompanyResponse400 | StandardizeCompanyResponse401 | StandardizeCompanyResponse402 | StandardizeCompanyResponse403 | StandardizeCompanyResponse404 | StandardizeCompanyResponse422 | StandardizeCompanyResponse429 | StandardizeCompanyResponse500 | StandardizeCompanyResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StandardizeCompanyBody,
) -> Response[
    StandardizeCompanyResponse200
    | StandardizeCompanyResponse400
    | StandardizeCompanyResponse401
    | StandardizeCompanyResponse402
    | StandardizeCompanyResponse403
    | StandardizeCompanyResponse404
    | StandardizeCompanyResponse422
    | StandardizeCompanyResponse429
    | StandardizeCompanyResponse500
    | StandardizeCompanyResponse503
]:
    """Standardize LinkedIn company identifier

     Resolves a company LinkedIn identifier (slug, organization ID, or URL) to a standardized LinkedIn
    company URL with metadata. Useful for normalizing company identifiers from different sources.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company standardized&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (StandardizeCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StandardizeCompanyResponse200 | StandardizeCompanyResponse400 | StandardizeCompanyResponse401 | StandardizeCompanyResponse402 | StandardizeCompanyResponse403 | StandardizeCompanyResponse404 | StandardizeCompanyResponse422 | StandardizeCompanyResponse429 | StandardizeCompanyResponse500 | StandardizeCompanyResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StandardizeCompanyBody,
) -> (
    StandardizeCompanyResponse200
    | StandardizeCompanyResponse400
    | StandardizeCompanyResponse401
    | StandardizeCompanyResponse402
    | StandardizeCompanyResponse403
    | StandardizeCompanyResponse404
    | StandardizeCompanyResponse422
    | StandardizeCompanyResponse429
    | StandardizeCompanyResponse500
    | StandardizeCompanyResponse503
    | None
):
    """Standardize LinkedIn company identifier

     Resolves a company LinkedIn identifier (slug, organization ID, or URL) to a standardized LinkedIn
    company URL with metadata. Useful for normalizing company identifiers from different sources.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company standardized&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (StandardizeCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StandardizeCompanyResponse200 | StandardizeCompanyResponse400 | StandardizeCompanyResponse401 | StandardizeCompanyResponse402 | StandardizeCompanyResponse403 | StandardizeCompanyResponse404 | StandardizeCompanyResponse422 | StandardizeCompanyResponse429 | StandardizeCompanyResponse500 | StandardizeCompanyResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
