from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_tracker_person_lists_response_200 import ListTrackerPersonListsResponse200
from ...models.list_tracker_person_lists_response_400 import ListTrackerPersonListsResponse400
from ...models.list_tracker_person_lists_response_401 import ListTrackerPersonListsResponse401
from ...models.list_tracker_person_lists_response_402 import ListTrackerPersonListsResponse402
from ...models.list_tracker_person_lists_response_403 import ListTrackerPersonListsResponse403
from ...models.list_tracker_person_lists_response_404 import ListTrackerPersonListsResponse404
from ...models.list_tracker_person_lists_response_429 import ListTrackerPersonListsResponse429
from ...models.list_tracker_person_lists_response_500 import ListTrackerPersonListsResponse500
from ...models.list_tracker_person_lists_response_503 import ListTrackerPersonListsResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    api_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tracker/person-lists",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListTrackerPersonListsResponse200
    | ListTrackerPersonListsResponse400
    | ListTrackerPersonListsResponse401
    | ListTrackerPersonListsResponse402
    | ListTrackerPersonListsResponse403
    | ListTrackerPersonListsResponse404
    | ListTrackerPersonListsResponse429
    | ListTrackerPersonListsResponse500
    | ListTrackerPersonListsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListTrackerPersonListsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListTrackerPersonListsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListTrackerPersonListsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListTrackerPersonListsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListTrackerPersonListsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListTrackerPersonListsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ListTrackerPersonListsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListTrackerPersonListsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListTrackerPersonListsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListTrackerPersonListsResponse200
    | ListTrackerPersonListsResponse400
    | ListTrackerPersonListsResponse401
    | ListTrackerPersonListsResponse402
    | ListTrackerPersonListsResponse403
    | ListTrackerPersonListsResponse404
    | ListTrackerPersonListsResponse429
    | ListTrackerPersonListsResponse500
    | ListTrackerPersonListsResponse503
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
    api_key: str,
) -> Response[
    ListTrackerPersonListsResponse200
    | ListTrackerPersonListsResponse400
    | ListTrackerPersonListsResponse401
    | ListTrackerPersonListsResponse402
    | ListTrackerPersonListsResponse403
    | ListTrackerPersonListsResponse404
    | ListTrackerPersonListsResponse429
    | ListTrackerPersonListsResponse500
    | ListTrackerPersonListsResponse503
]:
    r"""List person tracker lists

     List all person tracker lists for your organization.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTrackerPersonListsResponse200 | ListTrackerPersonListsResponse400 | ListTrackerPersonListsResponse401 | ListTrackerPersonListsResponse402 | ListTrackerPersonListsResponse403 | ListTrackerPersonListsResponse404 | ListTrackerPersonListsResponse429 | ListTrackerPersonListsResponse500 | ListTrackerPersonListsResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    ListTrackerPersonListsResponse200
    | ListTrackerPersonListsResponse400
    | ListTrackerPersonListsResponse401
    | ListTrackerPersonListsResponse402
    | ListTrackerPersonListsResponse403
    | ListTrackerPersonListsResponse404
    | ListTrackerPersonListsResponse429
    | ListTrackerPersonListsResponse500
    | ListTrackerPersonListsResponse503
    | None
):
    r"""List person tracker lists

     List all person tracker lists for your organization.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTrackerPersonListsResponse200 | ListTrackerPersonListsResponse400 | ListTrackerPersonListsResponse401 | ListTrackerPersonListsResponse402 | ListTrackerPersonListsResponse403 | ListTrackerPersonListsResponse404 | ListTrackerPersonListsResponse429 | ListTrackerPersonListsResponse500 | ListTrackerPersonListsResponse503
    """

    return sync_detailed(
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    ListTrackerPersonListsResponse200
    | ListTrackerPersonListsResponse400
    | ListTrackerPersonListsResponse401
    | ListTrackerPersonListsResponse402
    | ListTrackerPersonListsResponse403
    | ListTrackerPersonListsResponse404
    | ListTrackerPersonListsResponse429
    | ListTrackerPersonListsResponse500
    | ListTrackerPersonListsResponse503
]:
    r"""List person tracker lists

     List all person tracker lists for your organization.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTrackerPersonListsResponse200 | ListTrackerPersonListsResponse400 | ListTrackerPersonListsResponse401 | ListTrackerPersonListsResponse402 | ListTrackerPersonListsResponse403 | ListTrackerPersonListsResponse404 | ListTrackerPersonListsResponse429 | ListTrackerPersonListsResponse500 | ListTrackerPersonListsResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    ListTrackerPersonListsResponse200
    | ListTrackerPersonListsResponse400
    | ListTrackerPersonListsResponse401
    | ListTrackerPersonListsResponse402
    | ListTrackerPersonListsResponse403
    | ListTrackerPersonListsResponse404
    | ListTrackerPersonListsResponse429
    | ListTrackerPersonListsResponse500
    | ListTrackerPersonListsResponse503
    | None
):
    r"""List person tracker lists

     List all person tracker lists for your organization.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTrackerPersonListsResponse200 | ListTrackerPersonListsResponse400 | ListTrackerPersonListsResponse401 | ListTrackerPersonListsResponse402 | ListTrackerPersonListsResponse403 | ListTrackerPersonListsResponse404 | ListTrackerPersonListsResponse429 | ListTrackerPersonListsResponse500 | ListTrackerPersonListsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
