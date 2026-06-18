from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_tracker_people_body import AddTrackerPeopleBody
from ...models.add_tracker_people_response_200 import AddTrackerPeopleResponse200
from ...models.add_tracker_people_response_400 import AddTrackerPeopleResponse400
from ...models.add_tracker_people_response_401 import AddTrackerPeopleResponse401
from ...models.add_tracker_people_response_402 import AddTrackerPeopleResponse402
from ...models.add_tracker_people_response_403 import AddTrackerPeopleResponse403
from ...models.add_tracker_people_response_404 import AddTrackerPeopleResponse404
from ...models.add_tracker_people_response_422 import AddTrackerPeopleResponse422
from ...models.add_tracker_people_response_429 import AddTrackerPeopleResponse429
from ...models.add_tracker_people_response_500 import AddTrackerPeopleResponse500
from ...models.add_tracker_people_response_503 import AddTrackerPeopleResponse503
from ...types import Response


def _get_kwargs(
    list_id: str,
    *,
    body: AddTrackerPeopleBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/tracker/person-lists/{list_id}/people".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddTrackerPeopleResponse200
    | AddTrackerPeopleResponse400
    | AddTrackerPeopleResponse401
    | AddTrackerPeopleResponse402
    | AddTrackerPeopleResponse403
    | AddTrackerPeopleResponse404
    | AddTrackerPeopleResponse422
    | AddTrackerPeopleResponse429
    | AddTrackerPeopleResponse500
    | AddTrackerPeopleResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AddTrackerPeopleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddTrackerPeopleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddTrackerPeopleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = AddTrackerPeopleResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = AddTrackerPeopleResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddTrackerPeopleResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = AddTrackerPeopleResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = AddTrackerPeopleResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AddTrackerPeopleResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AddTrackerPeopleResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddTrackerPeopleResponse200
    | AddTrackerPeopleResponse400
    | AddTrackerPeopleResponse401
    | AddTrackerPeopleResponse402
    | AddTrackerPeopleResponse403
    | AddTrackerPeopleResponse404
    | AddTrackerPeopleResponse422
    | AddTrackerPeopleResponse429
    | AddTrackerPeopleResponse500
    | AddTrackerPeopleResponse503
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
    body: AddTrackerPeopleBody,
) -> Response[
    AddTrackerPeopleResponse200
    | AddTrackerPeopleResponse400
    | AddTrackerPeopleResponse401
    | AddTrackerPeopleResponse402
    | AddTrackerPeopleResponse403
    | AddTrackerPeopleResponse404
    | AddTrackerPeopleResponse422
    | AddTrackerPeopleResponse429
    | AddTrackerPeopleResponse500
    | AddTrackerPeopleResponse503
]:
    r"""Add people to tracker list

     Add people to a person tracker list. Identify people by LinkedIn URL, user ID, or slug. At least one
    identifier is required per person.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (AddTrackerPeopleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddTrackerPeopleResponse200 | AddTrackerPeopleResponse400 | AddTrackerPeopleResponse401 | AddTrackerPeopleResponse402 | AddTrackerPeopleResponse403 | AddTrackerPeopleResponse404 | AddTrackerPeopleResponse422 | AddTrackerPeopleResponse429 | AddTrackerPeopleResponse500 | AddTrackerPeopleResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTrackerPeopleBody,
) -> (
    AddTrackerPeopleResponse200
    | AddTrackerPeopleResponse400
    | AddTrackerPeopleResponse401
    | AddTrackerPeopleResponse402
    | AddTrackerPeopleResponse403
    | AddTrackerPeopleResponse404
    | AddTrackerPeopleResponse422
    | AddTrackerPeopleResponse429
    | AddTrackerPeopleResponse500
    | AddTrackerPeopleResponse503
    | None
):
    r"""Add people to tracker list

     Add people to a person tracker list. Identify people by LinkedIn URL, user ID, or slug. At least one
    identifier is required per person.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (AddTrackerPeopleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddTrackerPeopleResponse200 | AddTrackerPeopleResponse400 | AddTrackerPeopleResponse401 | AddTrackerPeopleResponse402 | AddTrackerPeopleResponse403 | AddTrackerPeopleResponse404 | AddTrackerPeopleResponse422 | AddTrackerPeopleResponse429 | AddTrackerPeopleResponse500 | AddTrackerPeopleResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTrackerPeopleBody,
) -> Response[
    AddTrackerPeopleResponse200
    | AddTrackerPeopleResponse400
    | AddTrackerPeopleResponse401
    | AddTrackerPeopleResponse402
    | AddTrackerPeopleResponse403
    | AddTrackerPeopleResponse404
    | AddTrackerPeopleResponse422
    | AddTrackerPeopleResponse429
    | AddTrackerPeopleResponse500
    | AddTrackerPeopleResponse503
]:
    r"""Add people to tracker list

     Add people to a person tracker list. Identify people by LinkedIn URL, user ID, or slug. At least one
    identifier is required per person.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (AddTrackerPeopleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddTrackerPeopleResponse200 | AddTrackerPeopleResponse400 | AddTrackerPeopleResponse401 | AddTrackerPeopleResponse402 | AddTrackerPeopleResponse403 | AddTrackerPeopleResponse404 | AddTrackerPeopleResponse422 | AddTrackerPeopleResponse429 | AddTrackerPeopleResponse500 | AddTrackerPeopleResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddTrackerPeopleBody,
) -> (
    AddTrackerPeopleResponse200
    | AddTrackerPeopleResponse400
    | AddTrackerPeopleResponse401
    | AddTrackerPeopleResponse402
    | AddTrackerPeopleResponse403
    | AddTrackerPeopleResponse404
    | AddTrackerPeopleResponse422
    | AddTrackerPeopleResponse429
    | AddTrackerPeopleResponse500
    | AddTrackerPeopleResponse503
    | None
):
    r"""Add people to tracker list

     Add people to a person tracker list. Identify people by LinkedIn URL, user ID, or slug. At least one
    identifier is required per person.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (AddTrackerPeopleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddTrackerPeopleResponse200 | AddTrackerPeopleResponse400 | AddTrackerPeopleResponse401 | AddTrackerPeopleResponse402 | AddTrackerPeopleResponse403 | AddTrackerPeopleResponse404 | AddTrackerPeopleResponse422 | AddTrackerPeopleResponse429 | AddTrackerPeopleResponse500 | AddTrackerPeopleResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
