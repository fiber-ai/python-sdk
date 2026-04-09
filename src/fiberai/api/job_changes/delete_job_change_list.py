from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_job_change_list_body import DeleteJobChangeListBody
from ...models.delete_job_change_list_response_200 import DeleteJobChangeListResponse200
from ...models.delete_job_change_list_response_400 import DeleteJobChangeListResponse400
from ...models.delete_job_change_list_response_401 import DeleteJobChangeListResponse401
from ...models.delete_job_change_list_response_402 import DeleteJobChangeListResponse402
from ...models.delete_job_change_list_response_403 import DeleteJobChangeListResponse403
from ...models.delete_job_change_list_response_404 import DeleteJobChangeListResponse404
from ...models.delete_job_change_list_response_429 import DeleteJobChangeListResponse429
from ...models.delete_job_change_list_response_500 import DeleteJobChangeListResponse500
from ...models.delete_job_change_list_response_503 import DeleteJobChangeListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteJobChangeListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job-changes/delete-list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteJobChangeListResponse200
    | DeleteJobChangeListResponse400
    | DeleteJobChangeListResponse401
    | DeleteJobChangeListResponse402
    | DeleteJobChangeListResponse403
    | DeleteJobChangeListResponse404
    | DeleteJobChangeListResponse429
    | DeleteJobChangeListResponse500
    | DeleteJobChangeListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = DeleteJobChangeListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteJobChangeListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteJobChangeListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = DeleteJobChangeListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = DeleteJobChangeListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteJobChangeListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = DeleteJobChangeListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteJobChangeListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteJobChangeListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteJobChangeListResponse200
    | DeleteJobChangeListResponse400
    | DeleteJobChangeListResponse401
    | DeleteJobChangeListResponse402
    | DeleteJobChangeListResponse403
    | DeleteJobChangeListResponse404
    | DeleteJobChangeListResponse429
    | DeleteJobChangeListResponse500
    | DeleteJobChangeListResponse503
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
    body: DeleteJobChangeListBody,
) -> Response[
    DeleteJobChangeListResponse200
    | DeleteJobChangeListResponse400
    | DeleteJobChangeListResponse401
    | DeleteJobChangeListResponse402
    | DeleteJobChangeListResponse403
    | DeleteJobChangeListResponse404
    | DeleteJobChangeListResponse429
    | DeleteJobChangeListResponse500
    | DeleteJobChangeListResponse503
]:
    r"""Delete a job changes list

     Deletes a job changes list. This will remove the list and stop tracking job changes for prospects in
    this list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DeleteJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteJobChangeListResponse200 | DeleteJobChangeListResponse400 | DeleteJobChangeListResponse401 | DeleteJobChangeListResponse402 | DeleteJobChangeListResponse403 | DeleteJobChangeListResponse404 | DeleteJobChangeListResponse429 | DeleteJobChangeListResponse500 | DeleteJobChangeListResponse503]
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
    body: DeleteJobChangeListBody,
) -> (
    DeleteJobChangeListResponse200
    | DeleteJobChangeListResponse400
    | DeleteJobChangeListResponse401
    | DeleteJobChangeListResponse402
    | DeleteJobChangeListResponse403
    | DeleteJobChangeListResponse404
    | DeleteJobChangeListResponse429
    | DeleteJobChangeListResponse500
    | DeleteJobChangeListResponse503
    | None
):
    r"""Delete a job changes list

     Deletes a job changes list. This will remove the list and stop tracking job changes for prospects in
    this list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DeleteJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteJobChangeListResponse200 | DeleteJobChangeListResponse400 | DeleteJobChangeListResponse401 | DeleteJobChangeListResponse402 | DeleteJobChangeListResponse403 | DeleteJobChangeListResponse404 | DeleteJobChangeListResponse429 | DeleteJobChangeListResponse500 | DeleteJobChangeListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteJobChangeListBody,
) -> Response[
    DeleteJobChangeListResponse200
    | DeleteJobChangeListResponse400
    | DeleteJobChangeListResponse401
    | DeleteJobChangeListResponse402
    | DeleteJobChangeListResponse403
    | DeleteJobChangeListResponse404
    | DeleteJobChangeListResponse429
    | DeleteJobChangeListResponse500
    | DeleteJobChangeListResponse503
]:
    r"""Delete a job changes list

     Deletes a job changes list. This will remove the list and stop tracking job changes for prospects in
    this list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DeleteJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteJobChangeListResponse200 | DeleteJobChangeListResponse400 | DeleteJobChangeListResponse401 | DeleteJobChangeListResponse402 | DeleteJobChangeListResponse403 | DeleteJobChangeListResponse404 | DeleteJobChangeListResponse429 | DeleteJobChangeListResponse500 | DeleteJobChangeListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteJobChangeListBody,
) -> (
    DeleteJobChangeListResponse200
    | DeleteJobChangeListResponse400
    | DeleteJobChangeListResponse401
    | DeleteJobChangeListResponse402
    | DeleteJobChangeListResponse403
    | DeleteJobChangeListResponse404
    | DeleteJobChangeListResponse429
    | DeleteJobChangeListResponse500
    | DeleteJobChangeListResponse503
    | None
):
    r"""Delete a job changes list

     Deletes a job changes list. This will remove the list and stop tracking job changes for prospects in
    this list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DeleteJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteJobChangeListResponse200 | DeleteJobChangeListResponse400 | DeleteJobChangeListResponse401 | DeleteJobChangeListResponse402 | DeleteJobChangeListResponse403 | DeleteJobChangeListResponse404 | DeleteJobChangeListResponse429 | DeleteJobChangeListResponse500 | DeleteJobChangeListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
