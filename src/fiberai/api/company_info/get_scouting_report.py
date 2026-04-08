from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_scouting_report_body import GetScoutingReportBody
from ...models.get_scouting_report_response_200 import GetScoutingReportResponse200
from ...models.get_scouting_report_response_400 import GetScoutingReportResponse400
from ...models.get_scouting_report_response_401 import GetScoutingReportResponse401
from ...models.get_scouting_report_response_402 import GetScoutingReportResponse402
from ...models.get_scouting_report_response_403 import GetScoutingReportResponse403
from ...models.get_scouting_report_response_404 import GetScoutingReportResponse404
from ...models.get_scouting_report_response_429 import GetScoutingReportResponse429
from ...models.get_scouting_report_response_500 import GetScoutingReportResponse500
from ...models.get_scouting_report_response_503 import GetScoutingReportResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetScoutingReportBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/scouting-report",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetScoutingReportResponse200
    | GetScoutingReportResponse400
    | GetScoutingReportResponse401
    | GetScoutingReportResponse402
    | GetScoutingReportResponse403
    | GetScoutingReportResponse404
    | GetScoutingReportResponse429
    | GetScoutingReportResponse500
    | GetScoutingReportResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetScoutingReportResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetScoutingReportResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetScoutingReportResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetScoutingReportResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetScoutingReportResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetScoutingReportResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetScoutingReportResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetScoutingReportResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetScoutingReportResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetScoutingReportResponse200
    | GetScoutingReportResponse400
    | GetScoutingReportResponse401
    | GetScoutingReportResponse402
    | GetScoutingReportResponse403
    | GetScoutingReportResponse404
    | GetScoutingReportResponse429
    | GetScoutingReportResponse500
    | GetScoutingReportResponse503
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
    body: GetScoutingReportBody,
) -> Response[
    GetScoutingReportResponse200
    | GetScoutingReportResponse400
    | GetScoutingReportResponse401
    | GetScoutingReportResponse402
    | GetScoutingReportResponse403
    | GetScoutingReportResponse404
    | GetScoutingReportResponse429
    | GetScoutingReportResponse500
    | GetScoutingReportResponse503
]:
    r"""Get company scouting report

     Generates a comprehensive scouting report for a company including news, founders, funding, media
    links, and historical headcount. This endpoint may take 1-2 minutes to respond as it gathers data
    from multiple sources — please set a generous client timeout (at least 120 seconds).

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 6 credits per scouting report&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetScoutingReportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetScoutingReportResponse200 | GetScoutingReportResponse400 | GetScoutingReportResponse401 | GetScoutingReportResponse402 | GetScoutingReportResponse403 | GetScoutingReportResponse404 | GetScoutingReportResponse429 | GetScoutingReportResponse500 | GetScoutingReportResponse503]
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
    body: GetScoutingReportBody,
) -> (
    GetScoutingReportResponse200
    | GetScoutingReportResponse400
    | GetScoutingReportResponse401
    | GetScoutingReportResponse402
    | GetScoutingReportResponse403
    | GetScoutingReportResponse404
    | GetScoutingReportResponse429
    | GetScoutingReportResponse500
    | GetScoutingReportResponse503
    | None
):
    r"""Get company scouting report

     Generates a comprehensive scouting report for a company including news, founders, funding, media
    links, and historical headcount. This endpoint may take 1-2 minutes to respond as it gathers data
    from multiple sources — please set a generous client timeout (at least 120 seconds).

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 6 credits per scouting report&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetScoutingReportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetScoutingReportResponse200 | GetScoutingReportResponse400 | GetScoutingReportResponse401 | GetScoutingReportResponse402 | GetScoutingReportResponse403 | GetScoutingReportResponse404 | GetScoutingReportResponse429 | GetScoutingReportResponse500 | GetScoutingReportResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetScoutingReportBody,
) -> Response[
    GetScoutingReportResponse200
    | GetScoutingReportResponse400
    | GetScoutingReportResponse401
    | GetScoutingReportResponse402
    | GetScoutingReportResponse403
    | GetScoutingReportResponse404
    | GetScoutingReportResponse429
    | GetScoutingReportResponse500
    | GetScoutingReportResponse503
]:
    r"""Get company scouting report

     Generates a comprehensive scouting report for a company including news, founders, funding, media
    links, and historical headcount. This endpoint may take 1-2 minutes to respond as it gathers data
    from multiple sources — please set a generous client timeout (at least 120 seconds).

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 6 credits per scouting report&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetScoutingReportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetScoutingReportResponse200 | GetScoutingReportResponse400 | GetScoutingReportResponse401 | GetScoutingReportResponse402 | GetScoutingReportResponse403 | GetScoutingReportResponse404 | GetScoutingReportResponse429 | GetScoutingReportResponse500 | GetScoutingReportResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetScoutingReportBody,
) -> (
    GetScoutingReportResponse200
    | GetScoutingReportResponse400
    | GetScoutingReportResponse401
    | GetScoutingReportResponse402
    | GetScoutingReportResponse403
    | GetScoutingReportResponse404
    | GetScoutingReportResponse429
    | GetScoutingReportResponse500
    | GetScoutingReportResponse503
    | None
):
    r"""Get company scouting report

     Generates a comprehensive scouting report for a company including news, founders, funding, media
    links, and historical headcount. This endpoint may take 1-2 minutes to respond as it gathers data
    from multiple sources — please set a generous client timeout (at least 120 seconds).

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 6 credits per scouting report&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetScoutingReportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetScoutingReportResponse200 | GetScoutingReportResponse400 | GetScoutingReportResponse401 | GetScoutingReportResponse402 | GetScoutingReportResponse403 | GetScoutingReportResponse404 | GetScoutingReportResponse429 | GetScoutingReportResponse500 | GetScoutingReportResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
