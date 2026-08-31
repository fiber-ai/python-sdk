from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_all_profiles_from_job_change_list_body import ListAllProfilesFromJobChangeListBody
from ...models.list_all_profiles_from_job_change_list_response_200 import ListAllProfilesFromJobChangeListResponse200
from ...models.list_all_profiles_from_job_change_list_response_400 import ListAllProfilesFromJobChangeListResponse400
from ...models.list_all_profiles_from_job_change_list_response_401 import ListAllProfilesFromJobChangeListResponse401
from ...models.list_all_profiles_from_job_change_list_response_402 import ListAllProfilesFromJobChangeListResponse402
from ...models.list_all_profiles_from_job_change_list_response_403 import ListAllProfilesFromJobChangeListResponse403
from ...models.list_all_profiles_from_job_change_list_response_404 import ListAllProfilesFromJobChangeListResponse404
from ...models.list_all_profiles_from_job_change_list_response_422 import ListAllProfilesFromJobChangeListResponse422
from ...models.list_all_profiles_from_job_change_list_response_429 import ListAllProfilesFromJobChangeListResponse429
from ...models.list_all_profiles_from_job_change_list_response_500 import ListAllProfilesFromJobChangeListResponse500
from ...models.list_all_profiles_from_job_change_list_response_503 import ListAllProfilesFromJobChangeListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ListAllProfilesFromJobChangeListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job-changes/list-all-profiles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListAllProfilesFromJobChangeListResponse200
    | ListAllProfilesFromJobChangeListResponse400
    | ListAllProfilesFromJobChangeListResponse401
    | ListAllProfilesFromJobChangeListResponse402
    | ListAllProfilesFromJobChangeListResponse403
    | ListAllProfilesFromJobChangeListResponse404
    | ListAllProfilesFromJobChangeListResponse422
    | ListAllProfilesFromJobChangeListResponse429
    | ListAllProfilesFromJobChangeListResponse500
    | ListAllProfilesFromJobChangeListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListAllProfilesFromJobChangeListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListAllProfilesFromJobChangeListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListAllProfilesFromJobChangeListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListAllProfilesFromJobChangeListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListAllProfilesFromJobChangeListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListAllProfilesFromJobChangeListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ListAllProfilesFromJobChangeListResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ListAllProfilesFromJobChangeListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListAllProfilesFromJobChangeListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListAllProfilesFromJobChangeListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListAllProfilesFromJobChangeListResponse200
    | ListAllProfilesFromJobChangeListResponse400
    | ListAllProfilesFromJobChangeListResponse401
    | ListAllProfilesFromJobChangeListResponse402
    | ListAllProfilesFromJobChangeListResponse403
    | ListAllProfilesFromJobChangeListResponse404
    | ListAllProfilesFromJobChangeListResponse422
    | ListAllProfilesFromJobChangeListResponse429
    | ListAllProfilesFromJobChangeListResponse500
    | ListAllProfilesFromJobChangeListResponse503
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
    body: ListAllProfilesFromJobChangeListBody,
) -> Response[
    ListAllProfilesFromJobChangeListResponse200
    | ListAllProfilesFromJobChangeListResponse400
    | ListAllProfilesFromJobChangeListResponse401
    | ListAllProfilesFromJobChangeListResponse402
    | ListAllProfilesFromJobChangeListResponse403
    | ListAllProfilesFromJobChangeListResponse404
    | ListAllProfilesFromJobChangeListResponse422
    | ListAllProfilesFromJobChangeListResponse429
    | ListAllProfilesFromJobChangeListResponse500
    | ListAllProfilesFromJobChangeListResponse503
]:
    """Lists all profiles from a job change list

     Get current state of all profiles from the list. Returns basic info for each profile.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListAllProfilesFromJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllProfilesFromJobChangeListResponse200 | ListAllProfilesFromJobChangeListResponse400 | ListAllProfilesFromJobChangeListResponse401 | ListAllProfilesFromJobChangeListResponse402 | ListAllProfilesFromJobChangeListResponse403 | ListAllProfilesFromJobChangeListResponse404 | ListAllProfilesFromJobChangeListResponse422 | ListAllProfilesFromJobChangeListResponse429 | ListAllProfilesFromJobChangeListResponse500 | ListAllProfilesFromJobChangeListResponse503]
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
    body: ListAllProfilesFromJobChangeListBody,
) -> (
    ListAllProfilesFromJobChangeListResponse200
    | ListAllProfilesFromJobChangeListResponse400
    | ListAllProfilesFromJobChangeListResponse401
    | ListAllProfilesFromJobChangeListResponse402
    | ListAllProfilesFromJobChangeListResponse403
    | ListAllProfilesFromJobChangeListResponse404
    | ListAllProfilesFromJobChangeListResponse422
    | ListAllProfilesFromJobChangeListResponse429
    | ListAllProfilesFromJobChangeListResponse500
    | ListAllProfilesFromJobChangeListResponse503
    | None
):
    """Lists all profiles from a job change list

     Get current state of all profiles from the list. Returns basic info for each profile.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListAllProfilesFromJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAllProfilesFromJobChangeListResponse200 | ListAllProfilesFromJobChangeListResponse400 | ListAllProfilesFromJobChangeListResponse401 | ListAllProfilesFromJobChangeListResponse402 | ListAllProfilesFromJobChangeListResponse403 | ListAllProfilesFromJobChangeListResponse404 | ListAllProfilesFromJobChangeListResponse422 | ListAllProfilesFromJobChangeListResponse429 | ListAllProfilesFromJobChangeListResponse500 | ListAllProfilesFromJobChangeListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListAllProfilesFromJobChangeListBody,
) -> Response[
    ListAllProfilesFromJobChangeListResponse200
    | ListAllProfilesFromJobChangeListResponse400
    | ListAllProfilesFromJobChangeListResponse401
    | ListAllProfilesFromJobChangeListResponse402
    | ListAllProfilesFromJobChangeListResponse403
    | ListAllProfilesFromJobChangeListResponse404
    | ListAllProfilesFromJobChangeListResponse422
    | ListAllProfilesFromJobChangeListResponse429
    | ListAllProfilesFromJobChangeListResponse500
    | ListAllProfilesFromJobChangeListResponse503
]:
    """Lists all profiles from a job change list

     Get current state of all profiles from the list. Returns basic info for each profile.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListAllProfilesFromJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllProfilesFromJobChangeListResponse200 | ListAllProfilesFromJobChangeListResponse400 | ListAllProfilesFromJobChangeListResponse401 | ListAllProfilesFromJobChangeListResponse402 | ListAllProfilesFromJobChangeListResponse403 | ListAllProfilesFromJobChangeListResponse404 | ListAllProfilesFromJobChangeListResponse422 | ListAllProfilesFromJobChangeListResponse429 | ListAllProfilesFromJobChangeListResponse500 | ListAllProfilesFromJobChangeListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListAllProfilesFromJobChangeListBody,
) -> (
    ListAllProfilesFromJobChangeListResponse200
    | ListAllProfilesFromJobChangeListResponse400
    | ListAllProfilesFromJobChangeListResponse401
    | ListAllProfilesFromJobChangeListResponse402
    | ListAllProfilesFromJobChangeListResponse403
    | ListAllProfilesFromJobChangeListResponse404
    | ListAllProfilesFromJobChangeListResponse422
    | ListAllProfilesFromJobChangeListResponse429
    | ListAllProfilesFromJobChangeListResponse500
    | ListAllProfilesFromJobChangeListResponse503
    | None
):
    """Lists all profiles from a job change list

     Get current state of all profiles from the list. Returns basic info for each profile.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListAllProfilesFromJobChangeListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAllProfilesFromJobChangeListResponse200 | ListAllProfilesFromJobChangeListResponse400 | ListAllProfilesFromJobChangeListResponse401 | ListAllProfilesFromJobChangeListResponse402 | ListAllProfilesFromJobChangeListResponse403 | ListAllProfilesFromJobChangeListResponse404 | ListAllProfilesFromJobChangeListResponse422 | ListAllProfilesFromJobChangeListResponse429 | ListAllProfilesFromJobChangeListResponse500 | ListAllProfilesFromJobChangeListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
