from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.quick_company_resolve_body import QuickCompanyResolveBody
from ...models.quick_company_resolve_response_200 import QuickCompanyResolveResponse200
from ...models.quick_company_resolve_response_400 import QuickCompanyResolveResponse400
from ...models.quick_company_resolve_response_401 import QuickCompanyResolveResponse401
from ...models.quick_company_resolve_response_402 import QuickCompanyResolveResponse402
from ...models.quick_company_resolve_response_403 import QuickCompanyResolveResponse403
from ...models.quick_company_resolve_response_404 import QuickCompanyResolveResponse404
from ...models.quick_company_resolve_response_422 import QuickCompanyResolveResponse422
from ...models.quick_company_resolve_response_429 import QuickCompanyResolveResponse429
from ...models.quick_company_resolve_response_500 import QuickCompanyResolveResponse500
from ...models.quick_company_resolve_response_503 import QuickCompanyResolveResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: QuickCompanyResolveBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/company-resolve",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    QuickCompanyResolveResponse200
    | QuickCompanyResolveResponse400
    | QuickCompanyResolveResponse401
    | QuickCompanyResolveResponse402
    | QuickCompanyResolveResponse403
    | QuickCompanyResolveResponse404
    | QuickCompanyResolveResponse422
    | QuickCompanyResolveResponse429
    | QuickCompanyResolveResponse500
    | QuickCompanyResolveResponse503
    | None
):
    if response.status_code == 200:
        response_200 = QuickCompanyResolveResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = QuickCompanyResolveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = QuickCompanyResolveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = QuickCompanyResolveResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = QuickCompanyResolveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = QuickCompanyResolveResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = QuickCompanyResolveResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = QuickCompanyResolveResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = QuickCompanyResolveResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = QuickCompanyResolveResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    QuickCompanyResolveResponse200
    | QuickCompanyResolveResponse400
    | QuickCompanyResolveResponse401
    | QuickCompanyResolveResponse402
    | QuickCompanyResolveResponse403
    | QuickCompanyResolveResponse404
    | QuickCompanyResolveResponse422
    | QuickCompanyResolveResponse429
    | QuickCompanyResolveResponse500
    | QuickCompanyResolveResponse503
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
    body: QuickCompanyResolveBody,
) -> Response[
    QuickCompanyResolveResponse200
    | QuickCompanyResolveResponse400
    | QuickCompanyResolveResponse401
    | QuickCompanyResolveResponse402
    | QuickCompanyResolveResponse403
    | QuickCompanyResolveResponse404
    | QuickCompanyResolveResponse422
    | QuickCompanyResolveResponse429
    | QuickCompanyResolveResponse500
    | QuickCompanyResolveResponse503
]:
    r"""Quickly resolve company identifiers

     Resolves many company identifiers — LinkedIn slug, LinkedIn organization ID, LinkedIn company URL,
    or domain — to full company records in a single request.

    <span>⚡ <strong>Rate limit:</strong> 1500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company resolved&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (QuickCompanyResolveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QuickCompanyResolveResponse200 | QuickCompanyResolveResponse400 | QuickCompanyResolveResponse401 | QuickCompanyResolveResponse402 | QuickCompanyResolveResponse403 | QuickCompanyResolveResponse404 | QuickCompanyResolveResponse422 | QuickCompanyResolveResponse429 | QuickCompanyResolveResponse500 | QuickCompanyResolveResponse503]
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
    body: QuickCompanyResolveBody,
) -> (
    QuickCompanyResolveResponse200
    | QuickCompanyResolveResponse400
    | QuickCompanyResolveResponse401
    | QuickCompanyResolveResponse402
    | QuickCompanyResolveResponse403
    | QuickCompanyResolveResponse404
    | QuickCompanyResolveResponse422
    | QuickCompanyResolveResponse429
    | QuickCompanyResolveResponse500
    | QuickCompanyResolveResponse503
    | None
):
    r"""Quickly resolve company identifiers

     Resolves many company identifiers — LinkedIn slug, LinkedIn organization ID, LinkedIn company URL,
    or domain — to full company records in a single request.

    <span>⚡ <strong>Rate limit:</strong> 1500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company resolved&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (QuickCompanyResolveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QuickCompanyResolveResponse200 | QuickCompanyResolveResponse400 | QuickCompanyResolveResponse401 | QuickCompanyResolveResponse402 | QuickCompanyResolveResponse403 | QuickCompanyResolveResponse404 | QuickCompanyResolveResponse422 | QuickCompanyResolveResponse429 | QuickCompanyResolveResponse500 | QuickCompanyResolveResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QuickCompanyResolveBody,
) -> Response[
    QuickCompanyResolveResponse200
    | QuickCompanyResolveResponse400
    | QuickCompanyResolveResponse401
    | QuickCompanyResolveResponse402
    | QuickCompanyResolveResponse403
    | QuickCompanyResolveResponse404
    | QuickCompanyResolveResponse422
    | QuickCompanyResolveResponse429
    | QuickCompanyResolveResponse500
    | QuickCompanyResolveResponse503
]:
    r"""Quickly resolve company identifiers

     Resolves many company identifiers — LinkedIn slug, LinkedIn organization ID, LinkedIn company URL,
    or domain — to full company records in a single request.

    <span>⚡ <strong>Rate limit:</strong> 1500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company resolved&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (QuickCompanyResolveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QuickCompanyResolveResponse200 | QuickCompanyResolveResponse400 | QuickCompanyResolveResponse401 | QuickCompanyResolveResponse402 | QuickCompanyResolveResponse403 | QuickCompanyResolveResponse404 | QuickCompanyResolveResponse422 | QuickCompanyResolveResponse429 | QuickCompanyResolveResponse500 | QuickCompanyResolveResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QuickCompanyResolveBody,
) -> (
    QuickCompanyResolveResponse200
    | QuickCompanyResolveResponse400
    | QuickCompanyResolveResponse401
    | QuickCompanyResolveResponse402
    | QuickCompanyResolveResponse403
    | QuickCompanyResolveResponse404
    | QuickCompanyResolveResponse422
    | QuickCompanyResolveResponse429
    | QuickCompanyResolveResponse500
    | QuickCompanyResolveResponse503
    | None
):
    r"""Quickly resolve company identifiers

     Resolves many company identifiers — LinkedIn slug, LinkedIn organization ID, LinkedIn company URL,
    or domain — to full company records in a single request.

    <span>⚡ <strong>Rate limit:</strong> 1500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company resolved&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (QuickCompanyResolveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QuickCompanyResolveResponse200 | QuickCompanyResolveResponse400 | QuickCompanyResolveResponse401 | QuickCompanyResolveResponse402 | QuickCompanyResolveResponse403 | QuickCompanyResolveResponse404 | QuickCompanyResolveResponse422 | QuickCompanyResolveResponse429 | QuickCompanyResolveResponse500 | QuickCompanyResolveResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
