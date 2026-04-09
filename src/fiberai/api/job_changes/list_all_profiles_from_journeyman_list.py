from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_all_profiles_from_journeyman_list_body import ListAllProfilesFromJourneymanListBody
from ...models.list_all_profiles_from_journeyman_list_response_200 import ListAllProfilesFromJourneymanListResponse200
from ...models.list_all_profiles_from_journeyman_list_response_400 import ListAllProfilesFromJourneymanListResponse400
from ...models.list_all_profiles_from_journeyman_list_response_401 import ListAllProfilesFromJourneymanListResponse401
from ...models.list_all_profiles_from_journeyman_list_response_402 import ListAllProfilesFromJourneymanListResponse402
from ...models.list_all_profiles_from_journeyman_list_response_403 import ListAllProfilesFromJourneymanListResponse403
from ...models.list_all_profiles_from_journeyman_list_response_404 import ListAllProfilesFromJourneymanListResponse404
from ...models.list_all_profiles_from_journeyman_list_response_429 import ListAllProfilesFromJourneymanListResponse429
from ...models.list_all_profiles_from_journeyman_list_response_500 import ListAllProfilesFromJourneymanListResponse500
from ...models.list_all_profiles_from_journeyman_list_response_503 import ListAllProfilesFromJourneymanListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ListAllProfilesFromJourneymanListBody,
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
    ListAllProfilesFromJourneymanListResponse200
    | ListAllProfilesFromJourneymanListResponse400
    | ListAllProfilesFromJourneymanListResponse401
    | ListAllProfilesFromJourneymanListResponse402
    | ListAllProfilesFromJourneymanListResponse403
    | ListAllProfilesFromJourneymanListResponse404
    | ListAllProfilesFromJourneymanListResponse429
    | ListAllProfilesFromJourneymanListResponse500
    | ListAllProfilesFromJourneymanListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListAllProfilesFromJourneymanListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListAllProfilesFromJourneymanListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListAllProfilesFromJourneymanListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListAllProfilesFromJourneymanListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListAllProfilesFromJourneymanListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListAllProfilesFromJourneymanListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ListAllProfilesFromJourneymanListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListAllProfilesFromJourneymanListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListAllProfilesFromJourneymanListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListAllProfilesFromJourneymanListResponse200
    | ListAllProfilesFromJourneymanListResponse400
    | ListAllProfilesFromJourneymanListResponse401
    | ListAllProfilesFromJourneymanListResponse402
    | ListAllProfilesFromJourneymanListResponse403
    | ListAllProfilesFromJourneymanListResponse404
    | ListAllProfilesFromJourneymanListResponse429
    | ListAllProfilesFromJourneymanListResponse500
    | ListAllProfilesFromJourneymanListResponse503
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
    body: ListAllProfilesFromJourneymanListBody,
) -> Response[
    ListAllProfilesFromJourneymanListResponse200
    | ListAllProfilesFromJourneymanListResponse400
    | ListAllProfilesFromJourneymanListResponse401
    | ListAllProfilesFromJourneymanListResponse402
    | ListAllProfilesFromJourneymanListResponse403
    | ListAllProfilesFromJourneymanListResponse404
    | ListAllProfilesFromJourneymanListResponse429
    | ListAllProfilesFromJourneymanListResponse500
    | ListAllProfilesFromJourneymanListResponse503
]:
    r"""Lists all profiles from a job change list

     Get current state of all profiles from the list. Returns basic info for each profile.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListAllProfilesFromJourneymanListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllProfilesFromJourneymanListResponse200 | ListAllProfilesFromJourneymanListResponse400 | ListAllProfilesFromJourneymanListResponse401 | ListAllProfilesFromJourneymanListResponse402 | ListAllProfilesFromJourneymanListResponse403 | ListAllProfilesFromJourneymanListResponse404 | ListAllProfilesFromJourneymanListResponse429 | ListAllProfilesFromJourneymanListResponse500 | ListAllProfilesFromJourneymanListResponse503]
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
    body: ListAllProfilesFromJourneymanListBody,
) -> (
    ListAllProfilesFromJourneymanListResponse200
    | ListAllProfilesFromJourneymanListResponse400
    | ListAllProfilesFromJourneymanListResponse401
    | ListAllProfilesFromJourneymanListResponse402
    | ListAllProfilesFromJourneymanListResponse403
    | ListAllProfilesFromJourneymanListResponse404
    | ListAllProfilesFromJourneymanListResponse429
    | ListAllProfilesFromJourneymanListResponse500
    | ListAllProfilesFromJourneymanListResponse503
    | None
):
    r"""Lists all profiles from a job change list

     Get current state of all profiles from the list. Returns basic info for each profile.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListAllProfilesFromJourneymanListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAllProfilesFromJourneymanListResponse200 | ListAllProfilesFromJourneymanListResponse400 | ListAllProfilesFromJourneymanListResponse401 | ListAllProfilesFromJourneymanListResponse402 | ListAllProfilesFromJourneymanListResponse403 | ListAllProfilesFromJourneymanListResponse404 | ListAllProfilesFromJourneymanListResponse429 | ListAllProfilesFromJourneymanListResponse500 | ListAllProfilesFromJourneymanListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListAllProfilesFromJourneymanListBody,
) -> Response[
    ListAllProfilesFromJourneymanListResponse200
    | ListAllProfilesFromJourneymanListResponse400
    | ListAllProfilesFromJourneymanListResponse401
    | ListAllProfilesFromJourneymanListResponse402
    | ListAllProfilesFromJourneymanListResponse403
    | ListAllProfilesFromJourneymanListResponse404
    | ListAllProfilesFromJourneymanListResponse429
    | ListAllProfilesFromJourneymanListResponse500
    | ListAllProfilesFromJourneymanListResponse503
]:
    r"""Lists all profiles from a job change list

     Get current state of all profiles from the list. Returns basic info for each profile.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListAllProfilesFromJourneymanListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAllProfilesFromJourneymanListResponse200 | ListAllProfilesFromJourneymanListResponse400 | ListAllProfilesFromJourneymanListResponse401 | ListAllProfilesFromJourneymanListResponse402 | ListAllProfilesFromJourneymanListResponse403 | ListAllProfilesFromJourneymanListResponse404 | ListAllProfilesFromJourneymanListResponse429 | ListAllProfilesFromJourneymanListResponse500 | ListAllProfilesFromJourneymanListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListAllProfilesFromJourneymanListBody,
) -> (
    ListAllProfilesFromJourneymanListResponse200
    | ListAllProfilesFromJourneymanListResponse400
    | ListAllProfilesFromJourneymanListResponse401
    | ListAllProfilesFromJourneymanListResponse402
    | ListAllProfilesFromJourneymanListResponse403
    | ListAllProfilesFromJourneymanListResponse404
    | ListAllProfilesFromJourneymanListResponse429
    | ListAllProfilesFromJourneymanListResponse500
    | ListAllProfilesFromJourneymanListResponse503
    | None
):
    r"""Lists all profiles from a job change list

     Get current state of all profiles from the list. Returns basic info for each profile.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListAllProfilesFromJourneymanListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAllProfilesFromJourneymanListResponse200 | ListAllProfilesFromJourneymanListResponse400 | ListAllProfilesFromJourneymanListResponse401 | ListAllProfilesFromJourneymanListResponse402 | ListAllProfilesFromJourneymanListResponse403 | ListAllProfilesFromJourneymanListResponse404 | ListAllProfilesFromJourneymanListResponse429 | ListAllProfilesFromJourneymanListResponse500 | ListAllProfilesFromJourneymanListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
