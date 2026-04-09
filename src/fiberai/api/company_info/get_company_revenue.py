from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_company_revenue_body import GetCompanyRevenueBody
from ...models.get_company_revenue_response_200 import GetCompanyRevenueResponse200
from ...models.get_company_revenue_response_400 import GetCompanyRevenueResponse400
from ...models.get_company_revenue_response_401 import GetCompanyRevenueResponse401
from ...models.get_company_revenue_response_402 import GetCompanyRevenueResponse402
from ...models.get_company_revenue_response_403 import GetCompanyRevenueResponse403
from ...models.get_company_revenue_response_404 import GetCompanyRevenueResponse404
from ...models.get_company_revenue_response_429 import GetCompanyRevenueResponse429
from ...models.get_company_revenue_response_500 import GetCompanyRevenueResponse500
from ...models.get_company_revenue_response_503 import GetCompanyRevenueResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetCompanyRevenueBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/company-revenue",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetCompanyRevenueResponse200
    | GetCompanyRevenueResponse400
    | GetCompanyRevenueResponse401
    | GetCompanyRevenueResponse402
    | GetCompanyRevenueResponse403
    | GetCompanyRevenueResponse404
    | GetCompanyRevenueResponse429
    | GetCompanyRevenueResponse500
    | GetCompanyRevenueResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetCompanyRevenueResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCompanyRevenueResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetCompanyRevenueResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetCompanyRevenueResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetCompanyRevenueResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCompanyRevenueResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetCompanyRevenueResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetCompanyRevenueResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetCompanyRevenueResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetCompanyRevenueResponse200
    | GetCompanyRevenueResponse400
    | GetCompanyRevenueResponse401
    | GetCompanyRevenueResponse402
    | GetCompanyRevenueResponse403
    | GetCompanyRevenueResponse404
    | GetCompanyRevenueResponse429
    | GetCompanyRevenueResponse500
    | GetCompanyRevenueResponse503
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
    body: GetCompanyRevenueBody,
) -> Response[
    GetCompanyRevenueResponse200
    | GetCompanyRevenueResponse400
    | GetCompanyRevenueResponse401
    | GetCompanyRevenueResponse402
    | GetCompanyRevenueResponse403
    | GetCompanyRevenueResponse404
    | GetCompanyRevenueResponse429
    | GetCompanyRevenueResponse500
    | GetCompanyRevenueResponse503
]:
    r"""Get company revenue estimate

     Fetches the most recent annual revenue estimate for a company. Pass a LinkedIn company URL, domain,
    and/or company name.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 4 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCompanyRevenueBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompanyRevenueResponse200 | GetCompanyRevenueResponse400 | GetCompanyRevenueResponse401 | GetCompanyRevenueResponse402 | GetCompanyRevenueResponse403 | GetCompanyRevenueResponse404 | GetCompanyRevenueResponse429 | GetCompanyRevenueResponse500 | GetCompanyRevenueResponse503]
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
    body: GetCompanyRevenueBody,
) -> (
    GetCompanyRevenueResponse200
    | GetCompanyRevenueResponse400
    | GetCompanyRevenueResponse401
    | GetCompanyRevenueResponse402
    | GetCompanyRevenueResponse403
    | GetCompanyRevenueResponse404
    | GetCompanyRevenueResponse429
    | GetCompanyRevenueResponse500
    | GetCompanyRevenueResponse503
    | None
):
    r"""Get company revenue estimate

     Fetches the most recent annual revenue estimate for a company. Pass a LinkedIn company URL, domain,
    and/or company name.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 4 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCompanyRevenueBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompanyRevenueResponse200 | GetCompanyRevenueResponse400 | GetCompanyRevenueResponse401 | GetCompanyRevenueResponse402 | GetCompanyRevenueResponse403 | GetCompanyRevenueResponse404 | GetCompanyRevenueResponse429 | GetCompanyRevenueResponse500 | GetCompanyRevenueResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetCompanyRevenueBody,
) -> Response[
    GetCompanyRevenueResponse200
    | GetCompanyRevenueResponse400
    | GetCompanyRevenueResponse401
    | GetCompanyRevenueResponse402
    | GetCompanyRevenueResponse403
    | GetCompanyRevenueResponse404
    | GetCompanyRevenueResponse429
    | GetCompanyRevenueResponse500
    | GetCompanyRevenueResponse503
]:
    r"""Get company revenue estimate

     Fetches the most recent annual revenue estimate for a company. Pass a LinkedIn company URL, domain,
    and/or company name.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 4 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCompanyRevenueBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompanyRevenueResponse200 | GetCompanyRevenueResponse400 | GetCompanyRevenueResponse401 | GetCompanyRevenueResponse402 | GetCompanyRevenueResponse403 | GetCompanyRevenueResponse404 | GetCompanyRevenueResponse429 | GetCompanyRevenueResponse500 | GetCompanyRevenueResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetCompanyRevenueBody,
) -> (
    GetCompanyRevenueResponse200
    | GetCompanyRevenueResponse400
    | GetCompanyRevenueResponse401
    | GetCompanyRevenueResponse402
    | GetCompanyRevenueResponse403
    | GetCompanyRevenueResponse404
    | GetCompanyRevenueResponse429
    | GetCompanyRevenueResponse500
    | GetCompanyRevenueResponse503
    | None
):
    r"""Get company revenue estimate

     Fetches the most recent annual revenue estimate for a company. Pass a LinkedIn company URL, domain,
    and/or company name.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 4 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetCompanyRevenueBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompanyRevenueResponse200 | GetCompanyRevenueResponse400 | GetCompanyRevenueResponse401 | GetCompanyRevenueResponse402 | GetCompanyRevenueResponse403 | GetCompanyRevenueResponse404 | GetCompanyRevenueResponse429 | GetCompanyRevenueResponse500 | GetCompanyRevenueResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
