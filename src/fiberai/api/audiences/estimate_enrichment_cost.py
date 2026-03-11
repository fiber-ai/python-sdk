from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.estimate_enrichment_cost_body import EstimateEnrichmentCostBody
from ...models.estimate_enrichment_cost_response_200 import EstimateEnrichmentCostResponse200
from ...models.estimate_enrichment_cost_response_400 import EstimateEnrichmentCostResponse400
from ...models.estimate_enrichment_cost_response_401 import EstimateEnrichmentCostResponse401
from ...models.estimate_enrichment_cost_response_402 import EstimateEnrichmentCostResponse402
from ...models.estimate_enrichment_cost_response_403 import EstimateEnrichmentCostResponse403
from ...models.estimate_enrichment_cost_response_404 import EstimateEnrichmentCostResponse404
from ...models.estimate_enrichment_cost_response_429 import EstimateEnrichmentCostResponse429
from ...models.estimate_enrichment_cost_response_500 import EstimateEnrichmentCostResponse500
from ...models.estimate_enrichment_cost_response_503 import EstimateEnrichmentCostResponse503
from ...types import Response


def _get_kwargs(
    audience_id: str,
    *,
    body: EstimateEnrichmentCostBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/audiences/{audience_id}/enrichment/estimate".format(
            audience_id=quote(str(audience_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EstimateEnrichmentCostResponse200
    | EstimateEnrichmentCostResponse400
    | EstimateEnrichmentCostResponse401
    | EstimateEnrichmentCostResponse402
    | EstimateEnrichmentCostResponse403
    | EstimateEnrichmentCostResponse404
    | EstimateEnrichmentCostResponse429
    | EstimateEnrichmentCostResponse500
    | EstimateEnrichmentCostResponse503
    | None
):
    if response.status_code == 200:
        response_200 = EstimateEnrichmentCostResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EstimateEnrichmentCostResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = EstimateEnrichmentCostResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = EstimateEnrichmentCostResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = EstimateEnrichmentCostResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = EstimateEnrichmentCostResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = EstimateEnrichmentCostResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = EstimateEnrichmentCostResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = EstimateEnrichmentCostResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EstimateEnrichmentCostResponse200
    | EstimateEnrichmentCostResponse400
    | EstimateEnrichmentCostResponse401
    | EstimateEnrichmentCostResponse402
    | EstimateEnrichmentCostResponse403
    | EstimateEnrichmentCostResponse404
    | EstimateEnrichmentCostResponse429
    | EstimateEnrichmentCostResponse500
    | EstimateEnrichmentCostResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EstimateEnrichmentCostBody,
) -> Response[
    EstimateEnrichmentCostResponse200
    | EstimateEnrichmentCostResponse400
    | EstimateEnrichmentCostResponse401
    | EstimateEnrichmentCostResponse402
    | EstimateEnrichmentCostResponse403
    | EstimateEnrichmentCostResponse404
    | EstimateEnrichmentCostResponse429
    | EstimateEnrichmentCostResponse500
    | EstimateEnrichmentCostResponse503
]:
    r"""Estimate enrichment cost

     Estimates the credit cost for an audience enrichment run before triggering it. Returns detailed
    breakdown by operation type (Sales Navigator, live enrichment, contact enrichment, validation) and
    estimated completion time. This endpoint is free and does not charge any credits.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (EstimateEnrichmentCostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EstimateEnrichmentCostResponse200 | EstimateEnrichmentCostResponse400 | EstimateEnrichmentCostResponse401 | EstimateEnrichmentCostResponse402 | EstimateEnrichmentCostResponse403 | EstimateEnrichmentCostResponse404 | EstimateEnrichmentCostResponse429 | EstimateEnrichmentCostResponse500 | EstimateEnrichmentCostResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EstimateEnrichmentCostBody,
) -> (
    EstimateEnrichmentCostResponse200
    | EstimateEnrichmentCostResponse400
    | EstimateEnrichmentCostResponse401
    | EstimateEnrichmentCostResponse402
    | EstimateEnrichmentCostResponse403
    | EstimateEnrichmentCostResponse404
    | EstimateEnrichmentCostResponse429
    | EstimateEnrichmentCostResponse500
    | EstimateEnrichmentCostResponse503
    | None
):
    r"""Estimate enrichment cost

     Estimates the credit cost for an audience enrichment run before triggering it. Returns detailed
    breakdown by operation type (Sales Navigator, live enrichment, contact enrichment, validation) and
    estimated completion time. This endpoint is free and does not charge any credits.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (EstimateEnrichmentCostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EstimateEnrichmentCostResponse200 | EstimateEnrichmentCostResponse400 | EstimateEnrichmentCostResponse401 | EstimateEnrichmentCostResponse402 | EstimateEnrichmentCostResponse403 | EstimateEnrichmentCostResponse404 | EstimateEnrichmentCostResponse429 | EstimateEnrichmentCostResponse500 | EstimateEnrichmentCostResponse503
    """

    return sync_detailed(
        audience_id=audience_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EstimateEnrichmentCostBody,
) -> Response[
    EstimateEnrichmentCostResponse200
    | EstimateEnrichmentCostResponse400
    | EstimateEnrichmentCostResponse401
    | EstimateEnrichmentCostResponse402
    | EstimateEnrichmentCostResponse403
    | EstimateEnrichmentCostResponse404
    | EstimateEnrichmentCostResponse429
    | EstimateEnrichmentCostResponse500
    | EstimateEnrichmentCostResponse503
]:
    r"""Estimate enrichment cost

     Estimates the credit cost for an audience enrichment run before triggering it. Returns detailed
    breakdown by operation type (Sales Navigator, live enrichment, contact enrichment, validation) and
    estimated completion time. This endpoint is free and does not charge any credits.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (EstimateEnrichmentCostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EstimateEnrichmentCostResponse200 | EstimateEnrichmentCostResponse400 | EstimateEnrichmentCostResponse401 | EstimateEnrichmentCostResponse402 | EstimateEnrichmentCostResponse403 | EstimateEnrichmentCostResponse404 | EstimateEnrichmentCostResponse429 | EstimateEnrichmentCostResponse500 | EstimateEnrichmentCostResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EstimateEnrichmentCostBody,
) -> (
    EstimateEnrichmentCostResponse200
    | EstimateEnrichmentCostResponse400
    | EstimateEnrichmentCostResponse401
    | EstimateEnrichmentCostResponse402
    | EstimateEnrichmentCostResponse403
    | EstimateEnrichmentCostResponse404
    | EstimateEnrichmentCostResponse429
    | EstimateEnrichmentCostResponse500
    | EstimateEnrichmentCostResponse503
    | None
):
    r"""Estimate enrichment cost

     Estimates the credit cost for an audience enrichment run before triggering it. Returns detailed
    breakdown by operation type (Sales Navigator, live enrichment, contact enrichment, validation) and
    estimated completion time. This endpoint is free and does not charge any credits.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (EstimateEnrichmentCostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EstimateEnrichmentCostResponse200 | EstimateEnrichmentCostResponse400 | EstimateEnrichmentCostResponse401 | EstimateEnrichmentCostResponse402 | EstimateEnrichmentCostResponse403 | EstimateEnrichmentCostResponse404 | EstimateEnrichmentCostResponse429 | EstimateEnrichmentCostResponse500 | EstimateEnrichmentCostResponse503
    """

    return (
        await asyncio_detailed(
            audience_id=audience_id,
            client=client,
            body=body,
        )
    ).parsed
