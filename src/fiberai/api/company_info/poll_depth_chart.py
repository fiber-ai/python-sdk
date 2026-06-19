from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.poll_depth_chart_body import PollDepthChartBody
from ...models.poll_depth_chart_response_200 import PollDepthChartResponse200
from ...models.poll_depth_chart_response_400 import PollDepthChartResponse400
from ...models.poll_depth_chart_response_401 import PollDepthChartResponse401
from ...models.poll_depth_chart_response_402 import PollDepthChartResponse402
from ...models.poll_depth_chart_response_403 import PollDepthChartResponse403
from ...models.poll_depth_chart_response_404 import PollDepthChartResponse404
from ...models.poll_depth_chart_response_422 import PollDepthChartResponse422
from ...models.poll_depth_chart_response_429 import PollDepthChartResponse429
from ...models.poll_depth_chart_response_500 import PollDepthChartResponse500
from ...models.poll_depth_chart_response_503 import PollDepthChartResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PollDepthChartBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/depth-chart/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PollDepthChartResponse200
    | PollDepthChartResponse400
    | PollDepthChartResponse401
    | PollDepthChartResponse402
    | PollDepthChartResponse403
    | PollDepthChartResponse404
    | PollDepthChartResponse422
    | PollDepthChartResponse429
    | PollDepthChartResponse500
    | PollDepthChartResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PollDepthChartResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PollDepthChartResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PollDepthChartResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PollDepthChartResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PollDepthChartResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PollDepthChartResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PollDepthChartResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PollDepthChartResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PollDepthChartResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PollDepthChartResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PollDepthChartResponse200
    | PollDepthChartResponse400
    | PollDepthChartResponse401
    | PollDepthChartResponse402
    | PollDepthChartResponse403
    | PollDepthChartResponse404
    | PollDepthChartResponse422
    | PollDepthChartResponse429
    | PollDepthChartResponse500
    | PollDepthChartResponse503
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
    body: PollDepthChartBody,
) -> Response[
    PollDepthChartResponse200
    | PollDepthChartResponse400
    | PollDepthChartResponse401
    | PollDepthChartResponse402
    | PollDepthChartResponse403
    | PollDepthChartResponse404
    | PollDepthChartResponse422
    | PollDepthChartResponse429
    | PollDepthChartResponse500
    | PollDepthChartResponse503
]:
    """Poll depth chart generation result

     Retrieves the employee breakdown started by the `depth-chart/start` endpoint. Pass the report ID you
    received when you started the report. Returns the current status and, once complete, numerical
    counts of employees grouped by department, seniority, or both, plus a printable markdown summary in
    tabular format — useful for CLI output or for LLMs building reports. Returns summary stats per
    bucket, not the individual people in each bucket.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (PollDepthChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollDepthChartResponse200 | PollDepthChartResponse400 | PollDepthChartResponse401 | PollDepthChartResponse402 | PollDepthChartResponse403 | PollDepthChartResponse404 | PollDepthChartResponse422 | PollDepthChartResponse429 | PollDepthChartResponse500 | PollDepthChartResponse503]
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
    body: PollDepthChartBody,
) -> (
    PollDepthChartResponse200
    | PollDepthChartResponse400
    | PollDepthChartResponse401
    | PollDepthChartResponse402
    | PollDepthChartResponse403
    | PollDepthChartResponse404
    | PollDepthChartResponse422
    | PollDepthChartResponse429
    | PollDepthChartResponse500
    | PollDepthChartResponse503
    | None
):
    """Poll depth chart generation result

     Retrieves the employee breakdown started by the `depth-chart/start` endpoint. Pass the report ID you
    received when you started the report. Returns the current status and, once complete, numerical
    counts of employees grouped by department, seniority, or both, plus a printable markdown summary in
    tabular format — useful for CLI output or for LLMs building reports. Returns summary stats per
    bucket, not the individual people in each bucket.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (PollDepthChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollDepthChartResponse200 | PollDepthChartResponse400 | PollDepthChartResponse401 | PollDepthChartResponse402 | PollDepthChartResponse403 | PollDepthChartResponse404 | PollDepthChartResponse422 | PollDepthChartResponse429 | PollDepthChartResponse500 | PollDepthChartResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PollDepthChartBody,
) -> Response[
    PollDepthChartResponse200
    | PollDepthChartResponse400
    | PollDepthChartResponse401
    | PollDepthChartResponse402
    | PollDepthChartResponse403
    | PollDepthChartResponse404
    | PollDepthChartResponse422
    | PollDepthChartResponse429
    | PollDepthChartResponse500
    | PollDepthChartResponse503
]:
    """Poll depth chart generation result

     Retrieves the employee breakdown started by the `depth-chart/start` endpoint. Pass the report ID you
    received when you started the report. Returns the current status and, once complete, numerical
    counts of employees grouped by department, seniority, or both, plus a printable markdown summary in
    tabular format — useful for CLI output or for LLMs building reports. Returns summary stats per
    bucket, not the individual people in each bucket.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (PollDepthChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollDepthChartResponse200 | PollDepthChartResponse400 | PollDepthChartResponse401 | PollDepthChartResponse402 | PollDepthChartResponse403 | PollDepthChartResponse404 | PollDepthChartResponse422 | PollDepthChartResponse429 | PollDepthChartResponse500 | PollDepthChartResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PollDepthChartBody,
) -> (
    PollDepthChartResponse200
    | PollDepthChartResponse400
    | PollDepthChartResponse401
    | PollDepthChartResponse402
    | PollDepthChartResponse403
    | PollDepthChartResponse404
    | PollDepthChartResponse422
    | PollDepthChartResponse429
    | PollDepthChartResponse500
    | PollDepthChartResponse503
    | None
):
    """Poll depth chart generation result

     Retrieves the employee breakdown started by the `depth-chart/start` endpoint. Pass the report ID you
    received when you started the report. Returns the current status and, once complete, numerical
    counts of employees grouped by department, seniority, or both, plus a printable markdown summary in
    tabular format — useful for CLI output or for LLMs building reports. Returns summary stats per
    bucket, not the individual people in each bucket.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    Args:
        body (PollDepthChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollDepthChartResponse200 | PollDepthChartResponse400 | PollDepthChartResponse401 | PollDepthChartResponse402 | PollDepthChartResponse403 | PollDepthChartResponse404 | PollDepthChartResponse422 | PollDepthChartResponse429 | PollDepthChartResponse500 | PollDepthChartResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
