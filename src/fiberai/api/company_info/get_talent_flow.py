from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_talent_flow_body import GetTalentFlowBody
from ...models.get_talent_flow_response_200 import GetTalentFlowResponse200
from ...models.get_talent_flow_response_400 import GetTalentFlowResponse400
from ...models.get_talent_flow_response_401 import GetTalentFlowResponse401
from ...models.get_talent_flow_response_402 import GetTalentFlowResponse402
from ...models.get_talent_flow_response_403 import GetTalentFlowResponse403
from ...models.get_talent_flow_response_404 import GetTalentFlowResponse404
from ...models.get_talent_flow_response_422 import GetTalentFlowResponse422
from ...models.get_talent_flow_response_429 import GetTalentFlowResponse429
from ...models.get_talent_flow_response_500 import GetTalentFlowResponse500
from ...models.get_talent_flow_response_503 import GetTalentFlowResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetTalentFlowBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/talent-flow",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetTalentFlowResponse200
    | GetTalentFlowResponse400
    | GetTalentFlowResponse401
    | GetTalentFlowResponse402
    | GetTalentFlowResponse403
    | GetTalentFlowResponse404
    | GetTalentFlowResponse422
    | GetTalentFlowResponse429
    | GetTalentFlowResponse500
    | GetTalentFlowResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetTalentFlowResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetTalentFlowResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetTalentFlowResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetTalentFlowResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetTalentFlowResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTalentFlowResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetTalentFlowResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetTalentFlowResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetTalentFlowResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetTalentFlowResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetTalentFlowResponse200
    | GetTalentFlowResponse400
    | GetTalentFlowResponse401
    | GetTalentFlowResponse402
    | GetTalentFlowResponse403
    | GetTalentFlowResponse404
    | GetTalentFlowResponse422
    | GetTalentFlowResponse429
    | GetTalentFlowResponse500
    | GetTalentFlowResponse503
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
    body: GetTalentFlowBody,
) -> Response[
    GetTalentFlowResponse200
    | GetTalentFlowResponse400
    | GetTalentFlowResponse401
    | GetTalentFlowResponse402
    | GetTalentFlowResponse403
    | GetTalentFlowResponse404
    | GetTalentFlowResponse422
    | GetTalentFlowResponse429
    | GetTalentFlowResponse500
    | GetTalentFlowResponse503
]:
    r"""Get talent flow analysis for a company

     Visualizes talent movement at a company. Use 'joiners' to see where a company is hiring from — which
    competitors, universities, and regions it pulls talent from during the time window. Use 'leavers' to
    see where a company's alumni are going — which companies or startups are attracting its former
    employees. Processes up to 10,000 profiles per request. Large companies may take up to two minutes
    to analyze.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per talent flow report&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (GetTalentFlowBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTalentFlowResponse200 | GetTalentFlowResponse400 | GetTalentFlowResponse401 | GetTalentFlowResponse402 | GetTalentFlowResponse403 | GetTalentFlowResponse404 | GetTalentFlowResponse422 | GetTalentFlowResponse429 | GetTalentFlowResponse500 | GetTalentFlowResponse503]
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
    body: GetTalentFlowBody,
) -> (
    GetTalentFlowResponse200
    | GetTalentFlowResponse400
    | GetTalentFlowResponse401
    | GetTalentFlowResponse402
    | GetTalentFlowResponse403
    | GetTalentFlowResponse404
    | GetTalentFlowResponse422
    | GetTalentFlowResponse429
    | GetTalentFlowResponse500
    | GetTalentFlowResponse503
    | None
):
    r"""Get talent flow analysis for a company

     Visualizes talent movement at a company. Use 'joiners' to see where a company is hiring from — which
    competitors, universities, and regions it pulls talent from during the time window. Use 'leavers' to
    see where a company's alumni are going — which companies or startups are attracting its former
    employees. Processes up to 10,000 profiles per request. Large companies may take up to two minutes
    to analyze.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per talent flow report&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (GetTalentFlowBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTalentFlowResponse200 | GetTalentFlowResponse400 | GetTalentFlowResponse401 | GetTalentFlowResponse402 | GetTalentFlowResponse403 | GetTalentFlowResponse404 | GetTalentFlowResponse422 | GetTalentFlowResponse429 | GetTalentFlowResponse500 | GetTalentFlowResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetTalentFlowBody,
) -> Response[
    GetTalentFlowResponse200
    | GetTalentFlowResponse400
    | GetTalentFlowResponse401
    | GetTalentFlowResponse402
    | GetTalentFlowResponse403
    | GetTalentFlowResponse404
    | GetTalentFlowResponse422
    | GetTalentFlowResponse429
    | GetTalentFlowResponse500
    | GetTalentFlowResponse503
]:
    r"""Get talent flow analysis for a company

     Visualizes talent movement at a company. Use 'joiners' to see where a company is hiring from — which
    competitors, universities, and regions it pulls talent from during the time window. Use 'leavers' to
    see where a company's alumni are going — which companies or startups are attracting its former
    employees. Processes up to 10,000 profiles per request. Large companies may take up to two minutes
    to analyze.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per talent flow report&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (GetTalentFlowBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTalentFlowResponse200 | GetTalentFlowResponse400 | GetTalentFlowResponse401 | GetTalentFlowResponse402 | GetTalentFlowResponse403 | GetTalentFlowResponse404 | GetTalentFlowResponse422 | GetTalentFlowResponse429 | GetTalentFlowResponse500 | GetTalentFlowResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetTalentFlowBody,
) -> (
    GetTalentFlowResponse200
    | GetTalentFlowResponse400
    | GetTalentFlowResponse401
    | GetTalentFlowResponse402
    | GetTalentFlowResponse403
    | GetTalentFlowResponse404
    | GetTalentFlowResponse422
    | GetTalentFlowResponse429
    | GetTalentFlowResponse500
    | GetTalentFlowResponse503
    | None
):
    r"""Get talent flow analysis for a company

     Visualizes talent movement at a company. Use 'joiners' to see where a company is hiring from — which
    competitors, universities, and regions it pulls talent from during the time window. Use 'leavers' to
    see where a company's alumni are going — which companies or startups are attracting its former
    employees. Processes up to 10,000 profiles per request. Large companies may take up to two minutes
    to analyze.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per talent flow report&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 2 minutes&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 2 minutes for this endpoint.\">ⓘ</span></span>

    Args:
        body (GetTalentFlowBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTalentFlowResponse200 | GetTalentFlowResponse400 | GetTalentFlowResponse401 | GetTalentFlowResponse402 | GetTalentFlowResponse403 | GetTalentFlowResponse404 | GetTalentFlowResponse422 | GetTalentFlowResponse429 | GetTalentFlowResponse500 | GetTalentFlowResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
