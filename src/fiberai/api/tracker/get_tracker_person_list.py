from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tracker_person_list_response_400 import GetTrackerPersonListResponse400
from ...models.get_tracker_person_list_response_401 import GetTrackerPersonListResponse401
from ...models.get_tracker_person_list_response_402 import GetTrackerPersonListResponse402
from ...models.get_tracker_person_list_response_403 import GetTrackerPersonListResponse403
from ...models.get_tracker_person_list_response_404 import GetTrackerPersonListResponse404
from ...models.get_tracker_person_list_response_422 import GetTrackerPersonListResponse422
from ...models.get_tracker_person_list_response_429 import GetTrackerPersonListResponse429
from ...models.get_tracker_person_list_response_500 import GetTrackerPersonListResponse500
from ...models.get_tracker_person_list_response_503 import GetTrackerPersonListResponse503
from ...types import UNSET, Response


def _get_kwargs(
    list_id: str,
    *,
    api_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tracker/person-lists/{list_id}".format(
            list_id=quote(str(list_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetTrackerPersonListResponse400
    | GetTrackerPersonListResponse401
    | GetTrackerPersonListResponse402
    | GetTrackerPersonListResponse403
    | GetTrackerPersonListResponse404
    | GetTrackerPersonListResponse422
    | GetTrackerPersonListResponse429
    | GetTrackerPersonListResponse500
    | GetTrackerPersonListResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetTrackerPersonListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetTrackerPersonListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetTrackerPersonListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetTrackerPersonListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTrackerPersonListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetTrackerPersonListResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetTrackerPersonListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetTrackerPersonListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetTrackerPersonListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetTrackerPersonListResponse400
    | GetTrackerPersonListResponse401
    | GetTrackerPersonListResponse402
    | GetTrackerPersonListResponse403
    | GetTrackerPersonListResponse404
    | GetTrackerPersonListResponse422
    | GetTrackerPersonListResponse429
    | GetTrackerPersonListResponse500
    | GetTrackerPersonListResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    GetTrackerPersonListResponse400
    | GetTrackerPersonListResponse401
    | GetTrackerPersonListResponse402
    | GetTrackerPersonListResponse403
    | GetTrackerPersonListResponse404
    | GetTrackerPersonListResponse422
    | GetTrackerPersonListResponse429
    | GetTrackerPersonListResponse500
    | GetTrackerPersonListResponse503
]:
    r"""Get person tracker list

     Get a single person tracker list by ID.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTrackerPersonListResponse400 | GetTrackerPersonListResponse401 | GetTrackerPersonListResponse402 | GetTrackerPersonListResponse403 | GetTrackerPersonListResponse404 | GetTrackerPersonListResponse422 | GetTrackerPersonListResponse429 | GetTrackerPersonListResponse500 | GetTrackerPersonListResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetTrackerPersonListResponse400
    | GetTrackerPersonListResponse401
    | GetTrackerPersonListResponse402
    | GetTrackerPersonListResponse403
    | GetTrackerPersonListResponse404
    | GetTrackerPersonListResponse422
    | GetTrackerPersonListResponse429
    | GetTrackerPersonListResponse500
    | GetTrackerPersonListResponse503
    | None
):
    r"""Get person tracker list

     Get a single person tracker list by ID.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTrackerPersonListResponse400 | GetTrackerPersonListResponse401 | GetTrackerPersonListResponse402 | GetTrackerPersonListResponse403 | GetTrackerPersonListResponse404 | GetTrackerPersonListResponse422 | GetTrackerPersonListResponse429 | GetTrackerPersonListResponse500 | GetTrackerPersonListResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    GetTrackerPersonListResponse400
    | GetTrackerPersonListResponse401
    | GetTrackerPersonListResponse402
    | GetTrackerPersonListResponse403
    | GetTrackerPersonListResponse404
    | GetTrackerPersonListResponse422
    | GetTrackerPersonListResponse429
    | GetTrackerPersonListResponse500
    | GetTrackerPersonListResponse503
]:
    r"""Get person tracker list

     Get a single person tracker list by ID.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTrackerPersonListResponse400 | GetTrackerPersonListResponse401 | GetTrackerPersonListResponse402 | GetTrackerPersonListResponse403 | GetTrackerPersonListResponse404 | GetTrackerPersonListResponse422 | GetTrackerPersonListResponse429 | GetTrackerPersonListResponse500 | GetTrackerPersonListResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetTrackerPersonListResponse400
    | GetTrackerPersonListResponse401
    | GetTrackerPersonListResponse402
    | GetTrackerPersonListResponse403
    | GetTrackerPersonListResponse404
    | GetTrackerPersonListResponse422
    | GetTrackerPersonListResponse429
    | GetTrackerPersonListResponse500
    | GetTrackerPersonListResponse503
    | None
):
    r"""Get person tracker list

     Get a single person tracker list by ID.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTrackerPersonListResponse400 | GetTrackerPersonListResponse401 | GetTrackerPersonListResponse402 | GetTrackerPersonListResponse403 | GetTrackerPersonListResponse404 | GetTrackerPersonListResponse422 | GetTrackerPersonListResponse429 | GetTrackerPersonListResponse500 | GetTrackerPersonListResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            api_key=api_key,
        )
    ).parsed
