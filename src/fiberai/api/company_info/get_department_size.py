from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_department_size_body import GetDepartmentSizeBody
from ...models.get_department_size_response_200 import GetDepartmentSizeResponse200
from ...models.get_department_size_response_400 import GetDepartmentSizeResponse400
from ...models.get_department_size_response_401 import GetDepartmentSizeResponse401
from ...models.get_department_size_response_402 import GetDepartmentSizeResponse402
from ...models.get_department_size_response_403 import GetDepartmentSizeResponse403
from ...models.get_department_size_response_404 import GetDepartmentSizeResponse404
from ...models.get_department_size_response_422 import GetDepartmentSizeResponse422
from ...models.get_department_size_response_429 import GetDepartmentSizeResponse429
from ...models.get_department_size_response_500 import GetDepartmentSizeResponse500
from ...models.get_department_size_response_503 import GetDepartmentSizeResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetDepartmentSizeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/department-size",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetDepartmentSizeResponse200
    | GetDepartmentSizeResponse400
    | GetDepartmentSizeResponse401
    | GetDepartmentSizeResponse402
    | GetDepartmentSizeResponse403
    | GetDepartmentSizeResponse404
    | GetDepartmentSizeResponse422
    | GetDepartmentSizeResponse429
    | GetDepartmentSizeResponse500
    | GetDepartmentSizeResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetDepartmentSizeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetDepartmentSizeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetDepartmentSizeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetDepartmentSizeResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetDepartmentSizeResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetDepartmentSizeResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetDepartmentSizeResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetDepartmentSizeResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetDepartmentSizeResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetDepartmentSizeResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetDepartmentSizeResponse200
    | GetDepartmentSizeResponse400
    | GetDepartmentSizeResponse401
    | GetDepartmentSizeResponse402
    | GetDepartmentSizeResponse403
    | GetDepartmentSizeResponse404
    | GetDepartmentSizeResponse422
    | GetDepartmentSizeResponse429
    | GetDepartmentSizeResponse500
    | GetDepartmentSizeResponse503
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
    body: GetDepartmentSizeBody,
) -> Response[
    GetDepartmentSizeResponse200
    | GetDepartmentSizeResponse400
    | GetDepartmentSizeResponse401
    | GetDepartmentSizeResponse402
    | GetDepartmentSizeResponse403
    | GetDepartmentSizeResponse404
    | GetDepartmentSizeResponse422
    | GetDepartmentSizeResponse429
    | GetDepartmentSizeResponse500
    | GetDepartmentSizeResponse503
]:
    r"""Count employees per department

     Counts how many current employees at a company fall into each department you define. Unlike the
    depth-chart endpoint, this Synchronous endpoint provides immediate results without waiting for
    background job generation. You supply the job titles that define each department (no seniority is
    considered), and every current employee is counted — not just a sample. This endpoint performs a
    headcount snapshot for direct, actionable data.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (GetDepartmentSizeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDepartmentSizeResponse200 | GetDepartmentSizeResponse400 | GetDepartmentSizeResponse401 | GetDepartmentSizeResponse402 | GetDepartmentSizeResponse403 | GetDepartmentSizeResponse404 | GetDepartmentSizeResponse422 | GetDepartmentSizeResponse429 | GetDepartmentSizeResponse500 | GetDepartmentSizeResponse503]
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
    body: GetDepartmentSizeBody,
) -> (
    GetDepartmentSizeResponse200
    | GetDepartmentSizeResponse400
    | GetDepartmentSizeResponse401
    | GetDepartmentSizeResponse402
    | GetDepartmentSizeResponse403
    | GetDepartmentSizeResponse404
    | GetDepartmentSizeResponse422
    | GetDepartmentSizeResponse429
    | GetDepartmentSizeResponse500
    | GetDepartmentSizeResponse503
    | None
):
    r"""Count employees per department

     Counts how many current employees at a company fall into each department you define. Unlike the
    depth-chart endpoint, this Synchronous endpoint provides immediate results without waiting for
    background job generation. You supply the job titles that define each department (no seniority is
    considered), and every current employee is counted — not just a sample. This endpoint performs a
    headcount snapshot for direct, actionable data.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (GetDepartmentSizeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDepartmentSizeResponse200 | GetDepartmentSizeResponse400 | GetDepartmentSizeResponse401 | GetDepartmentSizeResponse402 | GetDepartmentSizeResponse403 | GetDepartmentSizeResponse404 | GetDepartmentSizeResponse422 | GetDepartmentSizeResponse429 | GetDepartmentSizeResponse500 | GetDepartmentSizeResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetDepartmentSizeBody,
) -> Response[
    GetDepartmentSizeResponse200
    | GetDepartmentSizeResponse400
    | GetDepartmentSizeResponse401
    | GetDepartmentSizeResponse402
    | GetDepartmentSizeResponse403
    | GetDepartmentSizeResponse404
    | GetDepartmentSizeResponse422
    | GetDepartmentSizeResponse429
    | GetDepartmentSizeResponse500
    | GetDepartmentSizeResponse503
]:
    r"""Count employees per department

     Counts how many current employees at a company fall into each department you define. Unlike the
    depth-chart endpoint, this Synchronous endpoint provides immediate results without waiting for
    background job generation. You supply the job titles that define each department (no seniority is
    considered), and every current employee is counted — not just a sample. This endpoint performs a
    headcount snapshot for direct, actionable data.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (GetDepartmentSizeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDepartmentSizeResponse200 | GetDepartmentSizeResponse400 | GetDepartmentSizeResponse401 | GetDepartmentSizeResponse402 | GetDepartmentSizeResponse403 | GetDepartmentSizeResponse404 | GetDepartmentSizeResponse422 | GetDepartmentSizeResponse429 | GetDepartmentSizeResponse500 | GetDepartmentSizeResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetDepartmentSizeBody,
) -> (
    GetDepartmentSizeResponse200
    | GetDepartmentSizeResponse400
    | GetDepartmentSizeResponse401
    | GetDepartmentSizeResponse402
    | GetDepartmentSizeResponse403
    | GetDepartmentSizeResponse404
    | GetDepartmentSizeResponse422
    | GetDepartmentSizeResponse429
    | GetDepartmentSizeResponse500
    | GetDepartmentSizeResponse503
    | None
):
    r"""Count employees per department

     Counts how many current employees at a company fall into each department you define. Unlike the
    depth-chart endpoint, this Synchronous endpoint provides immediate results without waiting for
    background job generation. You supply the job titles that define each department (no seniority is
    considered), and every current employee is counted — not just a sample. This endpoint performs a
    headcount snapshot for direct, actionable data.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (GetDepartmentSizeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDepartmentSizeResponse200 | GetDepartmentSizeResponse400 | GetDepartmentSizeResponse401 | GetDepartmentSizeResponse402 | GetDepartmentSizeResponse403 | GetDepartmentSizeResponse404 | GetDepartmentSizeResponse422 | GetDepartmentSizeResponse429 | GetDepartmentSizeResponse500 | GetDepartmentSizeResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
