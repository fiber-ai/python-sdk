from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blue_collar_resolve_company_body import BlueCollarResolveCompanyBody
from ...models.blue_collar_resolve_company_response_200 import BlueCollarResolveCompanyResponse200
from ...models.blue_collar_resolve_company_response_400 import BlueCollarResolveCompanyResponse400
from ...models.blue_collar_resolve_company_response_401 import BlueCollarResolveCompanyResponse401
from ...models.blue_collar_resolve_company_response_402 import BlueCollarResolveCompanyResponse402
from ...models.blue_collar_resolve_company_response_403 import BlueCollarResolveCompanyResponse403
from ...models.blue_collar_resolve_company_response_404 import BlueCollarResolveCompanyResponse404
from ...models.blue_collar_resolve_company_response_422 import BlueCollarResolveCompanyResponse422
from ...models.blue_collar_resolve_company_response_429 import BlueCollarResolveCompanyResponse429
from ...models.blue_collar_resolve_company_response_500 import BlueCollarResolveCompanyResponse500
from ...models.blue_collar_resolve_company_response_503 import BlueCollarResolveCompanyResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: BlueCollarResolveCompanyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/blue-collar-jobs/resolve-company",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BlueCollarResolveCompanyResponse200
    | BlueCollarResolveCompanyResponse400
    | BlueCollarResolveCompanyResponse401
    | BlueCollarResolveCompanyResponse402
    | BlueCollarResolveCompanyResponse403
    | BlueCollarResolveCompanyResponse404
    | BlueCollarResolveCompanyResponse422
    | BlueCollarResolveCompanyResponse429
    | BlueCollarResolveCompanyResponse500
    | BlueCollarResolveCompanyResponse503
    | None
):
    if response.status_code == 200:
        response_200 = BlueCollarResolveCompanyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BlueCollarResolveCompanyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BlueCollarResolveCompanyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = BlueCollarResolveCompanyResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = BlueCollarResolveCompanyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = BlueCollarResolveCompanyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = BlueCollarResolveCompanyResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = BlueCollarResolveCompanyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = BlueCollarResolveCompanyResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = BlueCollarResolveCompanyResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BlueCollarResolveCompanyResponse200
    | BlueCollarResolveCompanyResponse400
    | BlueCollarResolveCompanyResponse401
    | BlueCollarResolveCompanyResponse402
    | BlueCollarResolveCompanyResponse403
    | BlueCollarResolveCompanyResponse404
    | BlueCollarResolveCompanyResponse422
    | BlueCollarResolveCompanyResponse429
    | BlueCollarResolveCompanyResponse500
    | BlueCollarResolveCompanyResponse503
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
    body: BlueCollarResolveCompanyBody,
) -> Response[
    BlueCollarResolveCompanyResponse200
    | BlueCollarResolveCompanyResponse400
    | BlueCollarResolveCompanyResponse401
    | BlueCollarResolveCompanyResponse402
    | BlueCollarResolveCompanyResponse403
    | BlueCollarResolveCompanyResponse404
    | BlueCollarResolveCompanyResponse422
    | BlueCollarResolveCompanyResponse429
    | BlueCollarResolveCompanyResponse500
    | BlueCollarResolveCompanyResponse503
]:
    r"""Resolve company to blue collar job board identifier

     Resolve a company to the identifier used for searching their blue collar job listings on boards such
    as Indeed. Provide a company name, a website domain or URL, or both for best results. Use the
    returned slug in the companySlug field of the blue collar jobs search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per resolution attempt&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (BlueCollarResolveCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlueCollarResolveCompanyResponse200 | BlueCollarResolveCompanyResponse400 | BlueCollarResolveCompanyResponse401 | BlueCollarResolveCompanyResponse402 | BlueCollarResolveCompanyResponse403 | BlueCollarResolveCompanyResponse404 | BlueCollarResolveCompanyResponse422 | BlueCollarResolveCompanyResponse429 | BlueCollarResolveCompanyResponse500 | BlueCollarResolveCompanyResponse503]
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
    body: BlueCollarResolveCompanyBody,
) -> (
    BlueCollarResolveCompanyResponse200
    | BlueCollarResolveCompanyResponse400
    | BlueCollarResolveCompanyResponse401
    | BlueCollarResolveCompanyResponse402
    | BlueCollarResolveCompanyResponse403
    | BlueCollarResolveCompanyResponse404
    | BlueCollarResolveCompanyResponse422
    | BlueCollarResolveCompanyResponse429
    | BlueCollarResolveCompanyResponse500
    | BlueCollarResolveCompanyResponse503
    | None
):
    r"""Resolve company to blue collar job board identifier

     Resolve a company to the identifier used for searching their blue collar job listings on boards such
    as Indeed. Provide a company name, a website domain or URL, or both for best results. Use the
    returned slug in the companySlug field of the blue collar jobs search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per resolution attempt&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (BlueCollarResolveCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlueCollarResolveCompanyResponse200 | BlueCollarResolveCompanyResponse400 | BlueCollarResolveCompanyResponse401 | BlueCollarResolveCompanyResponse402 | BlueCollarResolveCompanyResponse403 | BlueCollarResolveCompanyResponse404 | BlueCollarResolveCompanyResponse422 | BlueCollarResolveCompanyResponse429 | BlueCollarResolveCompanyResponse500 | BlueCollarResolveCompanyResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BlueCollarResolveCompanyBody,
) -> Response[
    BlueCollarResolveCompanyResponse200
    | BlueCollarResolveCompanyResponse400
    | BlueCollarResolveCompanyResponse401
    | BlueCollarResolveCompanyResponse402
    | BlueCollarResolveCompanyResponse403
    | BlueCollarResolveCompanyResponse404
    | BlueCollarResolveCompanyResponse422
    | BlueCollarResolveCompanyResponse429
    | BlueCollarResolveCompanyResponse500
    | BlueCollarResolveCompanyResponse503
]:
    r"""Resolve company to blue collar job board identifier

     Resolve a company to the identifier used for searching their blue collar job listings on boards such
    as Indeed. Provide a company name, a website domain or URL, or both for best results. Use the
    returned slug in the companySlug field of the blue collar jobs search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per resolution attempt&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (BlueCollarResolveCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlueCollarResolveCompanyResponse200 | BlueCollarResolveCompanyResponse400 | BlueCollarResolveCompanyResponse401 | BlueCollarResolveCompanyResponse402 | BlueCollarResolveCompanyResponse403 | BlueCollarResolveCompanyResponse404 | BlueCollarResolveCompanyResponse422 | BlueCollarResolveCompanyResponse429 | BlueCollarResolveCompanyResponse500 | BlueCollarResolveCompanyResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BlueCollarResolveCompanyBody,
) -> (
    BlueCollarResolveCompanyResponse200
    | BlueCollarResolveCompanyResponse400
    | BlueCollarResolveCompanyResponse401
    | BlueCollarResolveCompanyResponse402
    | BlueCollarResolveCompanyResponse403
    | BlueCollarResolveCompanyResponse404
    | BlueCollarResolveCompanyResponse422
    | BlueCollarResolveCompanyResponse429
    | BlueCollarResolveCompanyResponse500
    | BlueCollarResolveCompanyResponse503
    | None
):
    r"""Resolve company to blue collar job board identifier

     Resolve a company to the identifier used for searching their blue collar job listings on boards such
    as Indeed. Provide a company name, a website domain or URL, or both for best results. Use the
    returned slug in the companySlug field of the blue collar jobs search endpoint.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per resolution attempt&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 30 seconds&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 30 seconds for this endpoint.\">ⓘ</span></span>

    Args:
        body (BlueCollarResolveCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlueCollarResolveCompanyResponse200 | BlueCollarResolveCompanyResponse400 | BlueCollarResolveCompanyResponse401 | BlueCollarResolveCompanyResponse402 | BlueCollarResolveCompanyResponse403 | BlueCollarResolveCompanyResponse404 | BlueCollarResolveCompanyResponse422 | BlueCollarResolveCompanyResponse429 | BlueCollarResolveCompanyResponse500 | BlueCollarResolveCompanyResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
