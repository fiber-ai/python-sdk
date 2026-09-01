from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_talent_flow_rivals_body import GetTalentFlowRivalsBody
from ...models.get_talent_flow_rivals_response_200 import GetTalentFlowRivalsResponse200
from ...models.get_talent_flow_rivals_response_400 import GetTalentFlowRivalsResponse400
from ...models.get_talent_flow_rivals_response_401 import GetTalentFlowRivalsResponse401
from ...models.get_talent_flow_rivals_response_402 import GetTalentFlowRivalsResponse402
from ...models.get_talent_flow_rivals_response_403 import GetTalentFlowRivalsResponse403
from ...models.get_talent_flow_rivals_response_404 import GetTalentFlowRivalsResponse404
from ...models.get_talent_flow_rivals_response_422 import GetTalentFlowRivalsResponse422
from ...models.get_talent_flow_rivals_response_429 import GetTalentFlowRivalsResponse429
from ...models.get_talent_flow_rivals_response_500 import GetTalentFlowRivalsResponse500
from ...models.get_talent_flow_rivals_response_503 import GetTalentFlowRivalsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetTalentFlowRivalsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/talent-flow/rivals",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetTalentFlowRivalsResponse200
    | GetTalentFlowRivalsResponse400
    | GetTalentFlowRivalsResponse401
    | GetTalentFlowRivalsResponse402
    | GetTalentFlowRivalsResponse403
    | GetTalentFlowRivalsResponse404
    | GetTalentFlowRivalsResponse422
    | GetTalentFlowRivalsResponse429
    | GetTalentFlowRivalsResponse500
    | GetTalentFlowRivalsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetTalentFlowRivalsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetTalentFlowRivalsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetTalentFlowRivalsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetTalentFlowRivalsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetTalentFlowRivalsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTalentFlowRivalsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetTalentFlowRivalsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetTalentFlowRivalsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetTalentFlowRivalsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetTalentFlowRivalsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetTalentFlowRivalsResponse200
    | GetTalentFlowRivalsResponse400
    | GetTalentFlowRivalsResponse401
    | GetTalentFlowRivalsResponse402
    | GetTalentFlowRivalsResponse403
    | GetTalentFlowRivalsResponse404
    | GetTalentFlowRivalsResponse422
    | GetTalentFlowRivalsResponse429
    | GetTalentFlowRivalsResponse500
    | GetTalentFlowRivalsResponse503
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
    body: GetTalentFlowRivalsBody,
) -> Response[
    GetTalentFlowRivalsResponse200
    | GetTalentFlowRivalsResponse400
    | GetTalentFlowRivalsResponse401
    | GetTalentFlowRivalsResponse402
    | GetTalentFlowRivalsResponse403
    | GetTalentFlowRivalsResponse404
    | GetTalentFlowRivalsResponse422
    | GetTalentFlowRivalsResponse429
    | GetTalentFlowRivalsResponse500
    | GetTalentFlowRivalsResponse503
]:
    """Get top talent sources/destinations for a company

     Given a company, find the companies where most of its talent is heading to or coming from, in both
    directions. For instance, company A might have gained N people from company X but lost M people to
    them in a given window. Reports the two-way head-to-head flow for the most important sources and
    destinations of the chosen firm. Processes up to 10,000 profiles per direction. Large companies may
    take up to four minutes to analyze.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per talent flow report&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 4 minutes&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 4 minutes for this endpoint.">ⓘ</span></span>

    Args:
        body (GetTalentFlowRivalsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTalentFlowRivalsResponse200 | GetTalentFlowRivalsResponse400 | GetTalentFlowRivalsResponse401 | GetTalentFlowRivalsResponse402 | GetTalentFlowRivalsResponse403 | GetTalentFlowRivalsResponse404 | GetTalentFlowRivalsResponse422 | GetTalentFlowRivalsResponse429 | GetTalentFlowRivalsResponse500 | GetTalentFlowRivalsResponse503]
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
    body: GetTalentFlowRivalsBody,
) -> (
    GetTalentFlowRivalsResponse200
    | GetTalentFlowRivalsResponse400
    | GetTalentFlowRivalsResponse401
    | GetTalentFlowRivalsResponse402
    | GetTalentFlowRivalsResponse403
    | GetTalentFlowRivalsResponse404
    | GetTalentFlowRivalsResponse422
    | GetTalentFlowRivalsResponse429
    | GetTalentFlowRivalsResponse500
    | GetTalentFlowRivalsResponse503
    | None
):
    """Get top talent sources/destinations for a company

     Given a company, find the companies where most of its talent is heading to or coming from, in both
    directions. For instance, company A might have gained N people from company X but lost M people to
    them in a given window. Reports the two-way head-to-head flow for the most important sources and
    destinations of the chosen firm. Processes up to 10,000 profiles per direction. Large companies may
    take up to four minutes to analyze.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per talent flow report&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 4 minutes&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 4 minutes for this endpoint.">ⓘ</span></span>

    Args:
        body (GetTalentFlowRivalsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTalentFlowRivalsResponse200 | GetTalentFlowRivalsResponse400 | GetTalentFlowRivalsResponse401 | GetTalentFlowRivalsResponse402 | GetTalentFlowRivalsResponse403 | GetTalentFlowRivalsResponse404 | GetTalentFlowRivalsResponse422 | GetTalentFlowRivalsResponse429 | GetTalentFlowRivalsResponse500 | GetTalentFlowRivalsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetTalentFlowRivalsBody,
) -> Response[
    GetTalentFlowRivalsResponse200
    | GetTalentFlowRivalsResponse400
    | GetTalentFlowRivalsResponse401
    | GetTalentFlowRivalsResponse402
    | GetTalentFlowRivalsResponse403
    | GetTalentFlowRivalsResponse404
    | GetTalentFlowRivalsResponse422
    | GetTalentFlowRivalsResponse429
    | GetTalentFlowRivalsResponse500
    | GetTalentFlowRivalsResponse503
]:
    """Get top talent sources/destinations for a company

     Given a company, find the companies where most of its talent is heading to or coming from, in both
    directions. For instance, company A might have gained N people from company X but lost M people to
    them in a given window. Reports the two-way head-to-head flow for the most important sources and
    destinations of the chosen firm. Processes up to 10,000 profiles per direction. Large companies may
    take up to four minutes to analyze.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per talent flow report&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 4 minutes&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 4 minutes for this endpoint.">ⓘ</span></span>

    Args:
        body (GetTalentFlowRivalsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTalentFlowRivalsResponse200 | GetTalentFlowRivalsResponse400 | GetTalentFlowRivalsResponse401 | GetTalentFlowRivalsResponse402 | GetTalentFlowRivalsResponse403 | GetTalentFlowRivalsResponse404 | GetTalentFlowRivalsResponse422 | GetTalentFlowRivalsResponse429 | GetTalentFlowRivalsResponse500 | GetTalentFlowRivalsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetTalentFlowRivalsBody,
) -> (
    GetTalentFlowRivalsResponse200
    | GetTalentFlowRivalsResponse400
    | GetTalentFlowRivalsResponse401
    | GetTalentFlowRivalsResponse402
    | GetTalentFlowRivalsResponse403
    | GetTalentFlowRivalsResponse404
    | GetTalentFlowRivalsResponse422
    | GetTalentFlowRivalsResponse429
    | GetTalentFlowRivalsResponse500
    | GetTalentFlowRivalsResponse503
    | None
):
    """Get top talent sources/destinations for a company

     Given a company, find the companies where most of its talent is heading to or coming from, in both
    directions. For instance, company A might have gained N people from company X but lost M people to
    them in a given window. Reports the two-way head-to-head flow for the most important sources and
    destinations of the chosen firm. Processes up to 10,000 profiles per direction. Large companies may
    take up to four minutes to analyze.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 5 credits per talent flow report&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 4 minutes&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 4 minutes for this endpoint.">ⓘ</span></span>

    Args:
        body (GetTalentFlowRivalsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTalentFlowRivalsResponse200 | GetTalentFlowRivalsResponse400 | GetTalentFlowRivalsResponse401 | GetTalentFlowRivalsResponse402 | GetTalentFlowRivalsResponse403 | GetTalentFlowRivalsResponse404 | GetTalentFlowRivalsResponse422 | GetTalentFlowRivalsResponse429 | GetTalentFlowRivalsResponse500 | GetTalentFlowRivalsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
