from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_job_change_list_body import UpdateJobChangeListBody
from ...models.update_job_change_list_response_200 import UpdateJobChangeListResponse200
from ...models.update_job_change_list_response_400 import UpdateJobChangeListResponse400
from ...models.update_job_change_list_response_401 import UpdateJobChangeListResponse401
from ...models.update_job_change_list_response_402 import UpdateJobChangeListResponse402
from ...models.update_job_change_list_response_403 import UpdateJobChangeListResponse403
from ...models.update_job_change_list_response_404 import UpdateJobChangeListResponse404
from ...models.update_job_change_list_response_429 import UpdateJobChangeListResponse429
from ...models.update_job_change_list_response_500 import UpdateJobChangeListResponse500
from ...models.update_job_change_list_response_503 import UpdateJobChangeListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateJobChangeListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job-changes/update-list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateJobChangeListResponse200
    | UpdateJobChangeListResponse400
    | UpdateJobChangeListResponse401
    | UpdateJobChangeListResponse402
    | UpdateJobChangeListResponse403
    | UpdateJobChangeListResponse404
    | UpdateJobChangeListResponse429
    | UpdateJobChangeListResponse500
    | UpdateJobChangeListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = UpdateJobChangeListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateJobChangeListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateJobChangeListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = UpdateJobChangeListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = UpdateJobChangeListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateJobChangeListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = UpdateJobChangeListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateJobChangeListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateJobChangeListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateJobChangeListResponse200
    | UpdateJobChangeListResponse400
    | UpdateJobChangeListResponse401
    | UpdateJobChangeListResponse402
    | UpdateJobChangeListResponse403
    | UpdateJobChangeListResponse404
    | UpdateJobChangeListResponse429
    | UpdateJobChangeListResponse500
    | UpdateJobChangeListResponse503
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
    body: UpdateJobChangeListBody,
) -> Response[
    UpdateJobChangeListResponse200
    | UpdateJobChangeListResponse400
    | UpdateJobChangeListResponse401
    | UpdateJobChangeListResponse402
    | UpdateJobChangeListResponse403
    | UpdateJobChangeListResponse404
    | UpdateJobChangeListResponse429
    | UpdateJobChangeListResponse500
    | UpdateJobChangeListResponse503
]:
    r"""Update job change list

     Update a job changes list. Track people when they change their jobs.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (UpdateJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateJobChangeListResponse200 | UpdateJobChangeListResponse400 | UpdateJobChangeListResponse401 | UpdateJobChangeListResponse402 | UpdateJobChangeListResponse403 | UpdateJobChangeListResponse404 | UpdateJobChangeListResponse429 | UpdateJobChangeListResponse500 | UpdateJobChangeListResponse503]
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
    body: UpdateJobChangeListBody,
) -> (
    UpdateJobChangeListResponse200
    | UpdateJobChangeListResponse400
    | UpdateJobChangeListResponse401
    | UpdateJobChangeListResponse402
    | UpdateJobChangeListResponse403
    | UpdateJobChangeListResponse404
    | UpdateJobChangeListResponse429
    | UpdateJobChangeListResponse500
    | UpdateJobChangeListResponse503
    | None
):
    r"""Update job change list

     Update a job changes list. Track people when they change their jobs.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (UpdateJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateJobChangeListResponse200 | UpdateJobChangeListResponse400 | UpdateJobChangeListResponse401 | UpdateJobChangeListResponse402 | UpdateJobChangeListResponse403 | UpdateJobChangeListResponse404 | UpdateJobChangeListResponse429 | UpdateJobChangeListResponse500 | UpdateJobChangeListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateJobChangeListBody,
) -> Response[
    UpdateJobChangeListResponse200
    | UpdateJobChangeListResponse400
    | UpdateJobChangeListResponse401
    | UpdateJobChangeListResponse402
    | UpdateJobChangeListResponse403
    | UpdateJobChangeListResponse404
    | UpdateJobChangeListResponse429
    | UpdateJobChangeListResponse500
    | UpdateJobChangeListResponse503
]:
    r"""Update job change list

     Update a job changes list. Track people when they change their jobs.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (UpdateJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateJobChangeListResponse200 | UpdateJobChangeListResponse400 | UpdateJobChangeListResponse401 | UpdateJobChangeListResponse402 | UpdateJobChangeListResponse403 | UpdateJobChangeListResponse404 | UpdateJobChangeListResponse429 | UpdateJobChangeListResponse500 | UpdateJobChangeListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateJobChangeListBody,
) -> (
    UpdateJobChangeListResponse200
    | UpdateJobChangeListResponse400
    | UpdateJobChangeListResponse401
    | UpdateJobChangeListResponse402
    | UpdateJobChangeListResponse403
    | UpdateJobChangeListResponse404
    | UpdateJobChangeListResponse429
    | UpdateJobChangeListResponse500
    | UpdateJobChangeListResponse503
    | None
):
    r"""Update job change list

     Update a job changes list. Track people when they change their jobs.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (UpdateJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateJobChangeListResponse200 | UpdateJobChangeListResponse400 | UpdateJobChangeListResponse401 | UpdateJobChangeListResponse402 | UpdateJobChangeListResponse403 | UpdateJobChangeListResponse404 | UpdateJobChangeListResponse429 | UpdateJobChangeListResponse500 | UpdateJobChangeListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
