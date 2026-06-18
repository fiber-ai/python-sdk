from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_all_job_change_lists_body import ListAllJobChangeListsBody
from ...models.list_all_job_change_lists_response_200 import ListAllJobChangeListsResponse200
from ...models.list_all_job_change_lists_response_400 import ListAllJobChangeListsResponse400
from ...models.list_all_job_change_lists_response_401 import ListAllJobChangeListsResponse401
from ...models.list_all_job_change_lists_response_402 import ListAllJobChangeListsResponse402
from ...models.list_all_job_change_lists_response_403 import ListAllJobChangeListsResponse403
from ...models.list_all_job_change_lists_response_404 import ListAllJobChangeListsResponse404
from ...models.list_all_job_change_lists_response_422 import ListAllJobChangeListsResponse422
from ...models.list_all_job_change_lists_response_429 import ListAllJobChangeListsResponse429
from ...models.list_all_job_change_lists_response_500 import ListAllJobChangeListsResponse500
from ...models.list_all_job_change_lists_response_503 import ListAllJobChangeListsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ListAllJobChangeListsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job-changes/list-all",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListAllJobChangeListsResponse200
    | ListAllJobChangeListsResponse400
    | ListAllJobChangeListsResponse401
    | ListAllJobChangeListsResponse402
    | ListAllJobChangeListsResponse403
    | ListAllJobChangeListsResponse404
    | ListAllJobChangeListsResponse422
    | ListAllJobChangeListsResponse429
    | ListAllJobChangeListsResponse500
    | ListAllJobChangeListsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListAllJobChangeListsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListAllJobChangeListsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListAllJobChangeListsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListAllJobChangeListsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListAllJobChangeListsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListAllJobChangeListsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ListAllJobChangeListsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ListAllJobChangeListsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListAllJobChangeListsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListAllJobChangeListsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListAllJobChangeListsResponse200
    | ListAllJobChangeListsResponse400
    | ListAllJobChangeListsResponse401
    | ListAllJobChangeListsResponse402
    | ListAllJobChangeListsResponse403
    | ListAllJobChangeListsResponse404
    | ListAllJobChangeListsResponse422
    | ListAllJobChangeListsResponse429
    | ListAllJobChangeListsResponse500
    | ListAllJobChangeListsResponse503
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
    body: ListAllJobChangeListsBody,
) -> Response[
    ListAllJobChangeListsResponse200
    | ListAllJobChangeListsResponse400
    | ListAllJobChangeListsResponse401
    | ListAllJobChangeListsResponse402
    | ListAllJobChangeListsResponse403
    | ListAllJobChangeListsResponse404
    | ListAllJobChangeListsResponse422
    | ListAllJobChangeListsResponse429
    | ListAllJobChangeListsResponse500
    | ListAllJobChangeListsResponse503
]:
    r"""List all job changes lists

     Lists all job changes lists for your organization. Returns basic info for each list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListAllJobChangeListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllJobChangeListsResponse200 | ListAllJobChangeListsResponse400 | ListAllJobChangeListsResponse401 | ListAllJobChangeListsResponse402 | ListAllJobChangeListsResponse403 | ListAllJobChangeListsResponse404 | ListAllJobChangeListsResponse422 | ListAllJobChangeListsResponse429 | ListAllJobChangeListsResponse500 | ListAllJobChangeListsResponse503]
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
    body: ListAllJobChangeListsBody,
) -> (
    ListAllJobChangeListsResponse200
    | ListAllJobChangeListsResponse400
    | ListAllJobChangeListsResponse401
    | ListAllJobChangeListsResponse402
    | ListAllJobChangeListsResponse403
    | ListAllJobChangeListsResponse404
    | ListAllJobChangeListsResponse422
    | ListAllJobChangeListsResponse429
    | ListAllJobChangeListsResponse500
    | ListAllJobChangeListsResponse503
    | None
):
    r"""List all job changes lists

     Lists all job changes lists for your organization. Returns basic info for each list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListAllJobChangeListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAllJobChangeListsResponse200 | ListAllJobChangeListsResponse400 | ListAllJobChangeListsResponse401 | ListAllJobChangeListsResponse402 | ListAllJobChangeListsResponse403 | ListAllJobChangeListsResponse404 | ListAllJobChangeListsResponse422 | ListAllJobChangeListsResponse429 | ListAllJobChangeListsResponse500 | ListAllJobChangeListsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListAllJobChangeListsBody,
) -> Response[
    ListAllJobChangeListsResponse200
    | ListAllJobChangeListsResponse400
    | ListAllJobChangeListsResponse401
    | ListAllJobChangeListsResponse402
    | ListAllJobChangeListsResponse403
    | ListAllJobChangeListsResponse404
    | ListAllJobChangeListsResponse422
    | ListAllJobChangeListsResponse429
    | ListAllJobChangeListsResponse500
    | ListAllJobChangeListsResponse503
]:
    r"""List all job changes lists

     Lists all job changes lists for your organization. Returns basic info for each list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListAllJobChangeListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllJobChangeListsResponse200 | ListAllJobChangeListsResponse400 | ListAllJobChangeListsResponse401 | ListAllJobChangeListsResponse402 | ListAllJobChangeListsResponse403 | ListAllJobChangeListsResponse404 | ListAllJobChangeListsResponse422 | ListAllJobChangeListsResponse429 | ListAllJobChangeListsResponse500 | ListAllJobChangeListsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListAllJobChangeListsBody,
) -> (
    ListAllJobChangeListsResponse200
    | ListAllJobChangeListsResponse400
    | ListAllJobChangeListsResponse401
    | ListAllJobChangeListsResponse402
    | ListAllJobChangeListsResponse403
    | ListAllJobChangeListsResponse404
    | ListAllJobChangeListsResponse422
    | ListAllJobChangeListsResponse429
    | ListAllJobChangeListsResponse500
    | ListAllJobChangeListsResponse503
    | None
):
    r"""List all job changes lists

     Lists all job changes lists for your organization. Returns basic info for each list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListAllJobChangeListsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAllJobChangeListsResponse200 | ListAllJobChangeListsResponse400 | ListAllJobChangeListsResponse401 | ListAllJobChangeListsResponse402 | ListAllJobChangeListsResponse403 | ListAllJobChangeListsResponse404 | ListAllJobChangeListsResponse422 | ListAllJobChangeListsResponse429 | ListAllJobChangeListsResponse500 | ListAllJobChangeListsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
