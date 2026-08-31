from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_job_change_list_body import GetJobChangeListBody
from ...models.get_job_change_list_response_200 import GetJobChangeListResponse200
from ...models.get_job_change_list_response_400 import GetJobChangeListResponse400
from ...models.get_job_change_list_response_401 import GetJobChangeListResponse401
from ...models.get_job_change_list_response_402 import GetJobChangeListResponse402
from ...models.get_job_change_list_response_403 import GetJobChangeListResponse403
from ...models.get_job_change_list_response_404 import GetJobChangeListResponse404
from ...models.get_job_change_list_response_422 import GetJobChangeListResponse422
from ...models.get_job_change_list_response_429 import GetJobChangeListResponse429
from ...models.get_job_change_list_response_500 import GetJobChangeListResponse500
from ...models.get_job_change_list_response_503 import GetJobChangeListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetJobChangeListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job-changes/get-list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetJobChangeListResponse200
    | GetJobChangeListResponse400
    | GetJobChangeListResponse401
    | GetJobChangeListResponse402
    | GetJobChangeListResponse403
    | GetJobChangeListResponse404
    | GetJobChangeListResponse422
    | GetJobChangeListResponse429
    | GetJobChangeListResponse500
    | GetJobChangeListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetJobChangeListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetJobChangeListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetJobChangeListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetJobChangeListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetJobChangeListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetJobChangeListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetJobChangeListResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetJobChangeListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetJobChangeListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetJobChangeListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetJobChangeListResponse200
    | GetJobChangeListResponse400
    | GetJobChangeListResponse401
    | GetJobChangeListResponse402
    | GetJobChangeListResponse403
    | GetJobChangeListResponse404
    | GetJobChangeListResponse422
    | GetJobChangeListResponse429
    | GetJobChangeListResponse500
    | GetJobChangeListResponse503
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
    body: GetJobChangeListBody,
) -> Response[
    GetJobChangeListResponse200
    | GetJobChangeListResponse400
    | GetJobChangeListResponse401
    | GetJobChangeListResponse402
    | GetJobChangeListResponse403
    | GetJobChangeListResponse404
    | GetJobChangeListResponse422
    | GetJobChangeListResponse429
    | GetJobChangeListResponse500
    | GetJobChangeListResponse503
]:
    """Get a job changes list

     Get a job changes list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GetJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobChangeListResponse200 | GetJobChangeListResponse400 | GetJobChangeListResponse401 | GetJobChangeListResponse402 | GetJobChangeListResponse403 | GetJobChangeListResponse404 | GetJobChangeListResponse422 | GetJobChangeListResponse429 | GetJobChangeListResponse500 | GetJobChangeListResponse503]
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
    body: GetJobChangeListBody,
) -> (
    GetJobChangeListResponse200
    | GetJobChangeListResponse400
    | GetJobChangeListResponse401
    | GetJobChangeListResponse402
    | GetJobChangeListResponse403
    | GetJobChangeListResponse404
    | GetJobChangeListResponse422
    | GetJobChangeListResponse429
    | GetJobChangeListResponse500
    | GetJobChangeListResponse503
    | None
):
    """Get a job changes list

     Get a job changes list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GetJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobChangeListResponse200 | GetJobChangeListResponse400 | GetJobChangeListResponse401 | GetJobChangeListResponse402 | GetJobChangeListResponse403 | GetJobChangeListResponse404 | GetJobChangeListResponse422 | GetJobChangeListResponse429 | GetJobChangeListResponse500 | GetJobChangeListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetJobChangeListBody,
) -> Response[
    GetJobChangeListResponse200
    | GetJobChangeListResponse400
    | GetJobChangeListResponse401
    | GetJobChangeListResponse402
    | GetJobChangeListResponse403
    | GetJobChangeListResponse404
    | GetJobChangeListResponse422
    | GetJobChangeListResponse429
    | GetJobChangeListResponse500
    | GetJobChangeListResponse503
]:
    """Get a job changes list

     Get a job changes list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GetJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobChangeListResponse200 | GetJobChangeListResponse400 | GetJobChangeListResponse401 | GetJobChangeListResponse402 | GetJobChangeListResponse403 | GetJobChangeListResponse404 | GetJobChangeListResponse422 | GetJobChangeListResponse429 | GetJobChangeListResponse500 | GetJobChangeListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetJobChangeListBody,
) -> (
    GetJobChangeListResponse200
    | GetJobChangeListResponse400
    | GetJobChangeListResponse401
    | GetJobChangeListResponse402
    | GetJobChangeListResponse403
    | GetJobChangeListResponse404
    | GetJobChangeListResponse422
    | GetJobChangeListResponse429
    | GetJobChangeListResponse500
    | GetJobChangeListResponse503
    | None
):
    """Get a job changes list

     Get a job changes list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (GetJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobChangeListResponse200 | GetJobChangeListResponse400 | GetJobChangeListResponse401 | GetJobChangeListResponse402 | GetJobChangeListResponse403 | GetJobChangeListResponse404 | GetJobChangeListResponse422 | GetJobChangeListResponse429 | GetJobChangeListResponse500 | GetJobChangeListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
