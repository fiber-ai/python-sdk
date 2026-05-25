from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_tracker_person_list_body import CreateTrackerPersonListBody
from ...models.create_tracker_person_list_response_200 import CreateTrackerPersonListResponse200
from ...models.create_tracker_person_list_response_400 import CreateTrackerPersonListResponse400
from ...models.create_tracker_person_list_response_401 import CreateTrackerPersonListResponse401
from ...models.create_tracker_person_list_response_402 import CreateTrackerPersonListResponse402
from ...models.create_tracker_person_list_response_403 import CreateTrackerPersonListResponse403
from ...models.create_tracker_person_list_response_404 import CreateTrackerPersonListResponse404
from ...models.create_tracker_person_list_response_429 import CreateTrackerPersonListResponse429
from ...models.create_tracker_person_list_response_500 import CreateTrackerPersonListResponse500
from ...models.create_tracker_person_list_response_503 import CreateTrackerPersonListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CreateTrackerPersonListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tracker/person-lists",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateTrackerPersonListResponse200
    | CreateTrackerPersonListResponse400
    | CreateTrackerPersonListResponse401
    | CreateTrackerPersonListResponse402
    | CreateTrackerPersonListResponse403
    | CreateTrackerPersonListResponse404
    | CreateTrackerPersonListResponse429
    | CreateTrackerPersonListResponse500
    | CreateTrackerPersonListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CreateTrackerPersonListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateTrackerPersonListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateTrackerPersonListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CreateTrackerPersonListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CreateTrackerPersonListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateTrackerPersonListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CreateTrackerPersonListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateTrackerPersonListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateTrackerPersonListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateTrackerPersonListResponse200
    | CreateTrackerPersonListResponse400
    | CreateTrackerPersonListResponse401
    | CreateTrackerPersonListResponse402
    | CreateTrackerPersonListResponse403
    | CreateTrackerPersonListResponse404
    | CreateTrackerPersonListResponse429
    | CreateTrackerPersonListResponse500
    | CreateTrackerPersonListResponse503
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
    body: CreateTrackerPersonListBody,
) -> Response[
    CreateTrackerPersonListResponse200
    | CreateTrackerPersonListResponse400
    | CreateTrackerPersonListResponse401
    | CreateTrackerPersonListResponse402
    | CreateTrackerPersonListResponse403
    | CreateTrackerPersonListResponse404
    | CreateTrackerPersonListResponse429
    | CreateTrackerPersonListResponse500
    | CreateTrackerPersonListResponse503
]:
    r"""Create person tracker list

     Create a new person tracker list. Add people to the list, and we will periodically check them for
    changes matching your tracking rule. Pricing: 2 credits per entity per refresh cycle. Volume
    discounts (50%+) are available for high-volume tracking (10,000+ entities). Contact sales for
    details.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTrackerPersonListResponse200 | CreateTrackerPersonListResponse400 | CreateTrackerPersonListResponse401 | CreateTrackerPersonListResponse402 | CreateTrackerPersonListResponse403 | CreateTrackerPersonListResponse404 | CreateTrackerPersonListResponse429 | CreateTrackerPersonListResponse500 | CreateTrackerPersonListResponse503]
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
    body: CreateTrackerPersonListBody,
) -> (
    CreateTrackerPersonListResponse200
    | CreateTrackerPersonListResponse400
    | CreateTrackerPersonListResponse401
    | CreateTrackerPersonListResponse402
    | CreateTrackerPersonListResponse403
    | CreateTrackerPersonListResponse404
    | CreateTrackerPersonListResponse429
    | CreateTrackerPersonListResponse500
    | CreateTrackerPersonListResponse503
    | None
):
    r"""Create person tracker list

     Create a new person tracker list. Add people to the list, and we will periodically check them for
    changes matching your tracking rule. Pricing: 2 credits per entity per refresh cycle. Volume
    discounts (50%+) are available for high-volume tracking (10,000+ entities). Contact sales for
    details.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTrackerPersonListResponse200 | CreateTrackerPersonListResponse400 | CreateTrackerPersonListResponse401 | CreateTrackerPersonListResponse402 | CreateTrackerPersonListResponse403 | CreateTrackerPersonListResponse404 | CreateTrackerPersonListResponse429 | CreateTrackerPersonListResponse500 | CreateTrackerPersonListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTrackerPersonListBody,
) -> Response[
    CreateTrackerPersonListResponse200
    | CreateTrackerPersonListResponse400
    | CreateTrackerPersonListResponse401
    | CreateTrackerPersonListResponse402
    | CreateTrackerPersonListResponse403
    | CreateTrackerPersonListResponse404
    | CreateTrackerPersonListResponse429
    | CreateTrackerPersonListResponse500
    | CreateTrackerPersonListResponse503
]:
    r"""Create person tracker list

     Create a new person tracker list. Add people to the list, and we will periodically check them for
    changes matching your tracking rule. Pricing: 2 credits per entity per refresh cycle. Volume
    discounts (50%+) are available for high-volume tracking (10,000+ entities). Contact sales for
    details.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTrackerPersonListResponse200 | CreateTrackerPersonListResponse400 | CreateTrackerPersonListResponse401 | CreateTrackerPersonListResponse402 | CreateTrackerPersonListResponse403 | CreateTrackerPersonListResponse404 | CreateTrackerPersonListResponse429 | CreateTrackerPersonListResponse500 | CreateTrackerPersonListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTrackerPersonListBody,
) -> (
    CreateTrackerPersonListResponse200
    | CreateTrackerPersonListResponse400
    | CreateTrackerPersonListResponse401
    | CreateTrackerPersonListResponse402
    | CreateTrackerPersonListResponse403
    | CreateTrackerPersonListResponse404
    | CreateTrackerPersonListResponse429
    | CreateTrackerPersonListResponse500
    | CreateTrackerPersonListResponse503
    | None
):
    r"""Create person tracker list

     Create a new person tracker list. Add people to the list, and we will periodically check them for
    changes matching your tracking rule. Pricing: 2 credits per entity per refresh cycle. Volume
    discounts (50%+) are available for high-volume tracking (10,000+ entities). Contact sales for
    details.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTrackerPersonListResponse200 | CreateTrackerPersonListResponse400 | CreateTrackerPersonListResponse401 | CreateTrackerPersonListResponse402 | CreateTrackerPersonListResponse403 | CreateTrackerPersonListResponse404 | CreateTrackerPersonListResponse429 | CreateTrackerPersonListResponse500 | CreateTrackerPersonListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
