from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_enrichment_status_response_200 import GetEnrichmentStatusResponse200
from ...models.get_enrichment_status_response_400 import GetEnrichmentStatusResponse400
from ...models.get_enrichment_status_response_401 import GetEnrichmentStatusResponse401
from ...models.get_enrichment_status_response_402 import GetEnrichmentStatusResponse402
from ...models.get_enrichment_status_response_403 import GetEnrichmentStatusResponse403
from ...models.get_enrichment_status_response_404 import GetEnrichmentStatusResponse404
from ...models.get_enrichment_status_response_429 import GetEnrichmentStatusResponse429
from ...models.get_enrichment_status_response_500 import GetEnrichmentStatusResponse500
from ...models.get_enrichment_status_response_503 import GetEnrichmentStatusResponse503
from ...types import UNSET, Response


def _get_kwargs(
    audience_id: str,
    *,
    api_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audiences/{audience_id}/enrichment/status".format(
            audience_id=quote(str(audience_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetEnrichmentStatusResponse200
    | GetEnrichmentStatusResponse400
    | GetEnrichmentStatusResponse401
    | GetEnrichmentStatusResponse402
    | GetEnrichmentStatusResponse403
    | GetEnrichmentStatusResponse404
    | GetEnrichmentStatusResponse429
    | GetEnrichmentStatusResponse500
    | GetEnrichmentStatusResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetEnrichmentStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetEnrichmentStatusResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetEnrichmentStatusResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetEnrichmentStatusResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetEnrichmentStatusResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetEnrichmentStatusResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetEnrichmentStatusResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetEnrichmentStatusResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetEnrichmentStatusResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetEnrichmentStatusResponse200
    | GetEnrichmentStatusResponse400
    | GetEnrichmentStatusResponse401
    | GetEnrichmentStatusResponse402
    | GetEnrichmentStatusResponse403
    | GetEnrichmentStatusResponse404
    | GetEnrichmentStatusResponse429
    | GetEnrichmentStatusResponse500
    | GetEnrichmentStatusResponse503
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
    api_key: str,
) -> Response[
    GetEnrichmentStatusResponse200
    | GetEnrichmentStatusResponse400
    | GetEnrichmentStatusResponse401
    | GetEnrichmentStatusResponse402
    | GetEnrichmentStatusResponse403
    | GetEnrichmentStatusResponse404
    | GetEnrichmentStatusResponse429
    | GetEnrichmentStatusResponse500
    | GetEnrichmentStatusResponse503
]:
    r"""Get enrichment status

     Gets the current status of an audience enrichment run. Returns progress information including
    current stage, progress percentage, completed steps, and remaining steps. Use this endpoint to poll
    for enrichment completion. Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEnrichmentStatusResponse200 | GetEnrichmentStatusResponse400 | GetEnrichmentStatusResponse401 | GetEnrichmentStatusResponse402 | GetEnrichmentStatusResponse403 | GetEnrichmentStatusResponse404 | GetEnrichmentStatusResponse429 | GetEnrichmentStatusResponse500 | GetEnrichmentStatusResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetEnrichmentStatusResponse200
    | GetEnrichmentStatusResponse400
    | GetEnrichmentStatusResponse401
    | GetEnrichmentStatusResponse402
    | GetEnrichmentStatusResponse403
    | GetEnrichmentStatusResponse404
    | GetEnrichmentStatusResponse429
    | GetEnrichmentStatusResponse500
    | GetEnrichmentStatusResponse503
    | None
):
    r"""Get enrichment status

     Gets the current status of an audience enrichment run. Returns progress information including
    current stage, progress percentage, completed steps, and remaining steps. Use this endpoint to poll
    for enrichment completion. Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEnrichmentStatusResponse200 | GetEnrichmentStatusResponse400 | GetEnrichmentStatusResponse401 | GetEnrichmentStatusResponse402 | GetEnrichmentStatusResponse403 | GetEnrichmentStatusResponse404 | GetEnrichmentStatusResponse429 | GetEnrichmentStatusResponse500 | GetEnrichmentStatusResponse503
    """

    return sync_detailed(
        audience_id=audience_id,
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    GetEnrichmentStatusResponse200
    | GetEnrichmentStatusResponse400
    | GetEnrichmentStatusResponse401
    | GetEnrichmentStatusResponse402
    | GetEnrichmentStatusResponse403
    | GetEnrichmentStatusResponse404
    | GetEnrichmentStatusResponse429
    | GetEnrichmentStatusResponse500
    | GetEnrichmentStatusResponse503
]:
    r"""Get enrichment status

     Gets the current status of an audience enrichment run. Returns progress information including
    current stage, progress percentage, completed steps, and remaining steps. Use this endpoint to poll
    for enrichment completion. Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEnrichmentStatusResponse200 | GetEnrichmentStatusResponse400 | GetEnrichmentStatusResponse401 | GetEnrichmentStatusResponse402 | GetEnrichmentStatusResponse403 | GetEnrichmentStatusResponse404 | GetEnrichmentStatusResponse429 | GetEnrichmentStatusResponse500 | GetEnrichmentStatusResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetEnrichmentStatusResponse200
    | GetEnrichmentStatusResponse400
    | GetEnrichmentStatusResponse401
    | GetEnrichmentStatusResponse402
    | GetEnrichmentStatusResponse403
    | GetEnrichmentStatusResponse404
    | GetEnrichmentStatusResponse429
    | GetEnrichmentStatusResponse500
    | GetEnrichmentStatusResponse503
    | None
):
    r"""Get enrichment status

     Gets the current status of an audience enrichment run. Returns progress information including
    current stage, progress percentage, completed steps, and remaining steps. Use this endpoint to poll
    for enrichment completion. Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEnrichmentStatusResponse200 | GetEnrichmentStatusResponse400 | GetEnrichmentStatusResponse401 | GetEnrichmentStatusResponse402 | GetEnrichmentStatusResponse403 | GetEnrichmentStatusResponse404 | GetEnrichmentStatusResponse429 | GetEnrichmentStatusResponse500 | GetEnrichmentStatusResponse503
    """

    return (
        await asyncio_detailed(
            audience_id=audience_id,
            client=client,
            api_key=api_key,
        )
    ).parsed
