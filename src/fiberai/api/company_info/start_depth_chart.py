from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_depth_chart_body import StartDepthChartBody
from ...models.start_depth_chart_response_200 import StartDepthChartResponse200
from ...models.start_depth_chart_response_400 import StartDepthChartResponse400
from ...models.start_depth_chart_response_401 import StartDepthChartResponse401
from ...models.start_depth_chart_response_402 import StartDepthChartResponse402
from ...models.start_depth_chart_response_403 import StartDepthChartResponse403
from ...models.start_depth_chart_response_404 import StartDepthChartResponse404
from ...models.start_depth_chart_response_429 import StartDepthChartResponse429
from ...models.start_depth_chart_response_500 import StartDepthChartResponse500
from ...models.start_depth_chart_response_503 import StartDepthChartResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: StartDepthChartBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/depth-chart/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StartDepthChartResponse200
    | StartDepthChartResponse400
    | StartDepthChartResponse401
    | StartDepthChartResponse402
    | StartDepthChartResponse403
    | StartDepthChartResponse404
    | StartDepthChartResponse429
    | StartDepthChartResponse500
    | StartDepthChartResponse503
    | None
):
    if response.status_code == 200:
        response_200 = StartDepthChartResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StartDepthChartResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StartDepthChartResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = StartDepthChartResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = StartDepthChartResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StartDepthChartResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = StartDepthChartResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = StartDepthChartResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = StartDepthChartResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StartDepthChartResponse200
    | StartDepthChartResponse400
    | StartDepthChartResponse401
    | StartDepthChartResponse402
    | StartDepthChartResponse403
    | StartDepthChartResponse404
    | StartDepthChartResponse429
    | StartDepthChartResponse500
    | StartDepthChartResponse503
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
    body: StartDepthChartBody,
) -> Response[
    StartDepthChartResponse200
    | StartDepthChartResponse400
    | StartDepthChartResponse401
    | StartDepthChartResponse402
    | StartDepthChartResponse403
    | StartDepthChartResponse404
    | StartDepthChartResponse429
    | StartDepthChartResponse500
    | StartDepthChartResponse503
]:
    """Start depth chart generation

     Generates an organizational depth chart for a company — a close analog to the company's internal org
    chart. Classifies employees by function (Engineering, Sales, Marketing, etc.) and seniority level
    (Junior through Executive). This is asynchronous: call this endpoint to start generation, then poll
    /depth-chart/poll with the returned report ID. Processing typically takes 1-5 minutes depending on
    company size. Depth chart generation processes up to 10,000 employee profiles per report; larger
    companies are truncated to the most relevant profiles.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    Args:
        body (StartDepthChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartDepthChartResponse200 | StartDepthChartResponse400 | StartDepthChartResponse401 | StartDepthChartResponse402 | StartDepthChartResponse403 | StartDepthChartResponse404 | StartDepthChartResponse429 | StartDepthChartResponse500 | StartDepthChartResponse503]
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
    body: StartDepthChartBody,
) -> (
    StartDepthChartResponse200
    | StartDepthChartResponse400
    | StartDepthChartResponse401
    | StartDepthChartResponse402
    | StartDepthChartResponse403
    | StartDepthChartResponse404
    | StartDepthChartResponse429
    | StartDepthChartResponse500
    | StartDepthChartResponse503
    | None
):
    """Start depth chart generation

     Generates an organizational depth chart for a company — a close analog to the company's internal org
    chart. Classifies employees by function (Engineering, Sales, Marketing, etc.) and seniority level
    (Junior through Executive). This is asynchronous: call this endpoint to start generation, then poll
    /depth-chart/poll with the returned report ID. Processing typically takes 1-5 minutes depending on
    company size. Depth chart generation processes up to 10,000 employee profiles per report; larger
    companies are truncated to the most relevant profiles.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    Args:
        body (StartDepthChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartDepthChartResponse200 | StartDepthChartResponse400 | StartDepthChartResponse401 | StartDepthChartResponse402 | StartDepthChartResponse403 | StartDepthChartResponse404 | StartDepthChartResponse429 | StartDepthChartResponse500 | StartDepthChartResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartDepthChartBody,
) -> Response[
    StartDepthChartResponse200
    | StartDepthChartResponse400
    | StartDepthChartResponse401
    | StartDepthChartResponse402
    | StartDepthChartResponse403
    | StartDepthChartResponse404
    | StartDepthChartResponse429
    | StartDepthChartResponse500
    | StartDepthChartResponse503
]:
    """Start depth chart generation

     Generates an organizational depth chart for a company — a close analog to the company's internal org
    chart. Classifies employees by function (Engineering, Sales, Marketing, etc.) and seniority level
    (Junior through Executive). This is asynchronous: call this endpoint to start generation, then poll
    /depth-chart/poll with the returned report ID. Processing typically takes 1-5 minutes depending on
    company size. Depth chart generation processes up to 10,000 employee profiles per report; larger
    companies are truncated to the most relevant profiles.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    Args:
        body (StartDepthChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartDepthChartResponse200 | StartDepthChartResponse400 | StartDepthChartResponse401 | StartDepthChartResponse402 | StartDepthChartResponse403 | StartDepthChartResponse404 | StartDepthChartResponse429 | StartDepthChartResponse500 | StartDepthChartResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StartDepthChartBody,
) -> (
    StartDepthChartResponse200
    | StartDepthChartResponse400
    | StartDepthChartResponse401
    | StartDepthChartResponse402
    | StartDepthChartResponse403
    | StartDepthChartResponse404
    | StartDepthChartResponse429
    | StartDepthChartResponse500
    | StartDepthChartResponse503
    | None
):
    """Start depth chart generation

     Generates an organizational depth chart for a company — a close analog to the company's internal org
    chart. Classifies employees by function (Engineering, Sales, Marketing, etc.) and seniority level
    (Junior through Executive). This is asynchronous: call this endpoint to start generation, then poll
    /depth-chart/poll with the returned report ID. Processing typically takes 1-5 minutes depending on
    company size. Depth chart generation processes up to 10,000 employee profiles per report; larger
    companies are truncated to the most relevant profiles.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    Args:
        body (StartDepthChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartDepthChartResponse200 | StartDepthChartResponse400 | StartDepthChartResponse401 | StartDepthChartResponse402 | StartDepthChartResponse403 | StartDepthChartResponse404 | StartDepthChartResponse429 | StartDepthChartResponse500 | StartDepthChartResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
