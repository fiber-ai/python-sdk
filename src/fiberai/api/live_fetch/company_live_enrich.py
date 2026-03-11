from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_live_enrich_body import CompanyLiveEnrichBody
from ...models.company_live_enrich_response_200 import CompanyLiveEnrichResponse200
from ...models.company_live_enrich_response_400 import CompanyLiveEnrichResponse400
from ...models.company_live_enrich_response_401 import CompanyLiveEnrichResponse401
from ...models.company_live_enrich_response_402 import CompanyLiveEnrichResponse402
from ...models.company_live_enrich_response_403 import CompanyLiveEnrichResponse403
from ...models.company_live_enrich_response_404 import CompanyLiveEnrichResponse404
from ...models.company_live_enrich_response_429 import CompanyLiveEnrichResponse429
from ...models.company_live_enrich_response_500 import CompanyLiveEnrichResponse500
from ...models.company_live_enrich_response_503 import CompanyLiveEnrichResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CompanyLiveEnrichBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/company/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CompanyLiveEnrichResponse200
    | CompanyLiveEnrichResponse400
    | CompanyLiveEnrichResponse401
    | CompanyLiveEnrichResponse402
    | CompanyLiveEnrichResponse403
    | CompanyLiveEnrichResponse404
    | CompanyLiveEnrichResponse429
    | CompanyLiveEnrichResponse500
    | CompanyLiveEnrichResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CompanyLiveEnrichResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CompanyLiveEnrichResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CompanyLiveEnrichResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CompanyLiveEnrichResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CompanyLiveEnrichResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CompanyLiveEnrichResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CompanyLiveEnrichResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CompanyLiveEnrichResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CompanyLiveEnrichResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CompanyLiveEnrichResponse200
    | CompanyLiveEnrichResponse400
    | CompanyLiveEnrichResponse401
    | CompanyLiveEnrichResponse402
    | CompanyLiveEnrichResponse403
    | CompanyLiveEnrichResponse404
    | CompanyLiveEnrichResponse429
    | CompanyLiveEnrichResponse500
    | CompanyLiveEnrichResponse503
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
    body: CompanyLiveEnrichBody,
) -> Response[
    CompanyLiveEnrichResponse200
    | CompanyLiveEnrichResponse400
    | CompanyLiveEnrichResponse401
    | CompanyLiveEnrichResponse402
    | CompanyLiveEnrichResponse403
    | CompanyLiveEnrichResponse404
    | CompanyLiveEnrichResponse429
    | CompanyLiveEnrichResponse500
    | CompanyLiveEnrichResponse503
]:
    r"""Live fetch LinkedIn company

     Returns an enriched company with details for a given LinkedIn company identifier

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company live fetch&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyLiveEnrichResponse200 | CompanyLiveEnrichResponse400 | CompanyLiveEnrichResponse401 | CompanyLiveEnrichResponse402 | CompanyLiveEnrichResponse403 | CompanyLiveEnrichResponse404 | CompanyLiveEnrichResponse429 | CompanyLiveEnrichResponse500 | CompanyLiveEnrichResponse503]
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
    body: CompanyLiveEnrichBody,
) -> (
    CompanyLiveEnrichResponse200
    | CompanyLiveEnrichResponse400
    | CompanyLiveEnrichResponse401
    | CompanyLiveEnrichResponse402
    | CompanyLiveEnrichResponse403
    | CompanyLiveEnrichResponse404
    | CompanyLiveEnrichResponse429
    | CompanyLiveEnrichResponse500
    | CompanyLiveEnrichResponse503
    | None
):
    r"""Live fetch LinkedIn company

     Returns an enriched company with details for a given LinkedIn company identifier

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company live fetch&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyLiveEnrichResponse200 | CompanyLiveEnrichResponse400 | CompanyLiveEnrichResponse401 | CompanyLiveEnrichResponse402 | CompanyLiveEnrichResponse403 | CompanyLiveEnrichResponse404 | CompanyLiveEnrichResponse429 | CompanyLiveEnrichResponse500 | CompanyLiveEnrichResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompanyLiveEnrichBody,
) -> Response[
    CompanyLiveEnrichResponse200
    | CompanyLiveEnrichResponse400
    | CompanyLiveEnrichResponse401
    | CompanyLiveEnrichResponse402
    | CompanyLiveEnrichResponse403
    | CompanyLiveEnrichResponse404
    | CompanyLiveEnrichResponse429
    | CompanyLiveEnrichResponse500
    | CompanyLiveEnrichResponse503
]:
    r"""Live fetch LinkedIn company

     Returns an enriched company with details for a given LinkedIn company identifier

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company live fetch&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyLiveEnrichResponse200 | CompanyLiveEnrichResponse400 | CompanyLiveEnrichResponse401 | CompanyLiveEnrichResponse402 | CompanyLiveEnrichResponse403 | CompanyLiveEnrichResponse404 | CompanyLiveEnrichResponse429 | CompanyLiveEnrichResponse500 | CompanyLiveEnrichResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CompanyLiveEnrichBody,
) -> (
    CompanyLiveEnrichResponse200
    | CompanyLiveEnrichResponse400
    | CompanyLiveEnrichResponse401
    | CompanyLiveEnrichResponse402
    | CompanyLiveEnrichResponse403
    | CompanyLiveEnrichResponse404
    | CompanyLiveEnrichResponse429
    | CompanyLiveEnrichResponse500
    | CompanyLiveEnrichResponse503
    | None
):
    r"""Live fetch LinkedIn company

     Returns an enriched company with details for a given LinkedIn company identifier

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company live fetch&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyLiveEnrichResponse200 | CompanyLiveEnrichResponse400 | CompanyLiveEnrichResponse401 | CompanyLiveEnrichResponse402 | CompanyLiveEnrichResponse403 | CompanyLiveEnrichResponse404 | CompanyLiveEnrichResponse429 | CompanyLiveEnrichResponse500 | CompanyLiveEnrichResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
