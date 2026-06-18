from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_tracker_person_list_body import UpdateTrackerPersonListBody
from ...models.update_tracker_person_list_response_400 import UpdateTrackerPersonListResponse400
from ...models.update_tracker_person_list_response_401 import UpdateTrackerPersonListResponse401
from ...models.update_tracker_person_list_response_402 import UpdateTrackerPersonListResponse402
from ...models.update_tracker_person_list_response_403 import UpdateTrackerPersonListResponse403
from ...models.update_tracker_person_list_response_404 import UpdateTrackerPersonListResponse404
from ...models.update_tracker_person_list_response_422 import UpdateTrackerPersonListResponse422
from ...models.update_tracker_person_list_response_429 import UpdateTrackerPersonListResponse429
from ...models.update_tracker_person_list_response_500 import UpdateTrackerPersonListResponse500
from ...models.update_tracker_person_list_response_503 import UpdateTrackerPersonListResponse503
from ...types import Response


def _get_kwargs(
    list_id: str,
    *,
    body: UpdateTrackerPersonListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/tracker/person-lists/{list_id}".format(
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
    UpdateTrackerPersonListResponse400
    | UpdateTrackerPersonListResponse401
    | UpdateTrackerPersonListResponse402
    | UpdateTrackerPersonListResponse403
    | UpdateTrackerPersonListResponse404
    | UpdateTrackerPersonListResponse422
    | UpdateTrackerPersonListResponse429
    | UpdateTrackerPersonListResponse500
    | UpdateTrackerPersonListResponse503
    | None
):
    if response.status_code == 400:
        response_400 = UpdateTrackerPersonListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateTrackerPersonListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = UpdateTrackerPersonListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = UpdateTrackerPersonListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateTrackerPersonListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = UpdateTrackerPersonListResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = UpdateTrackerPersonListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateTrackerPersonListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateTrackerPersonListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateTrackerPersonListResponse400
    | UpdateTrackerPersonListResponse401
    | UpdateTrackerPersonListResponse402
    | UpdateTrackerPersonListResponse403
    | UpdateTrackerPersonListResponse404
    | UpdateTrackerPersonListResponse422
    | UpdateTrackerPersonListResponse429
    | UpdateTrackerPersonListResponse500
    | UpdateTrackerPersonListResponse503
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
    body: UpdateTrackerPersonListBody,
) -> Response[
    UpdateTrackerPersonListResponse400
    | UpdateTrackerPersonListResponse401
    | UpdateTrackerPersonListResponse402
    | UpdateTrackerPersonListResponse403
    | UpdateTrackerPersonListResponse404
    | UpdateTrackerPersonListResponse422
    | UpdateTrackerPersonListResponse429
    | UpdateTrackerPersonListResponse500
    | UpdateTrackerPersonListResponse503
]:
    r"""Update person tracker list

     Update a person tracker list. Supports replace-all (`trackingRules`) or granular
    (`addRules`/`removeRuleIds`) rule management — but not both in one request.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (UpdateTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTrackerPersonListResponse400 | UpdateTrackerPersonListResponse401 | UpdateTrackerPersonListResponse402 | UpdateTrackerPersonListResponse403 | UpdateTrackerPersonListResponse404 | UpdateTrackerPersonListResponse422 | UpdateTrackerPersonListResponse429 | UpdateTrackerPersonListResponse500 | UpdateTrackerPersonListResponse503]
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
    body: UpdateTrackerPersonListBody,
) -> (
    UpdateTrackerPersonListResponse400
    | UpdateTrackerPersonListResponse401
    | UpdateTrackerPersonListResponse402
    | UpdateTrackerPersonListResponse403
    | UpdateTrackerPersonListResponse404
    | UpdateTrackerPersonListResponse422
    | UpdateTrackerPersonListResponse429
    | UpdateTrackerPersonListResponse500
    | UpdateTrackerPersonListResponse503
    | None
):
    r"""Update person tracker list

     Update a person tracker list. Supports replace-all (`trackingRules`) or granular
    (`addRules`/`removeRuleIds`) rule management — but not both in one request.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (UpdateTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTrackerPersonListResponse400 | UpdateTrackerPersonListResponse401 | UpdateTrackerPersonListResponse402 | UpdateTrackerPersonListResponse403 | UpdateTrackerPersonListResponse404 | UpdateTrackerPersonListResponse422 | UpdateTrackerPersonListResponse429 | UpdateTrackerPersonListResponse500 | UpdateTrackerPersonListResponse503
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
    body: UpdateTrackerPersonListBody,
) -> Response[
    UpdateTrackerPersonListResponse400
    | UpdateTrackerPersonListResponse401
    | UpdateTrackerPersonListResponse402
    | UpdateTrackerPersonListResponse403
    | UpdateTrackerPersonListResponse404
    | UpdateTrackerPersonListResponse422
    | UpdateTrackerPersonListResponse429
    | UpdateTrackerPersonListResponse500
    | UpdateTrackerPersonListResponse503
]:
    r"""Update person tracker list

     Update a person tracker list. Supports replace-all (`trackingRules`) or granular
    (`addRules`/`removeRuleIds`) rule management — but not both in one request.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (UpdateTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTrackerPersonListResponse400 | UpdateTrackerPersonListResponse401 | UpdateTrackerPersonListResponse402 | UpdateTrackerPersonListResponse403 | UpdateTrackerPersonListResponse404 | UpdateTrackerPersonListResponse422 | UpdateTrackerPersonListResponse429 | UpdateTrackerPersonListResponse500 | UpdateTrackerPersonListResponse503]
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
    body: UpdateTrackerPersonListBody,
) -> (
    UpdateTrackerPersonListResponse400
    | UpdateTrackerPersonListResponse401
    | UpdateTrackerPersonListResponse402
    | UpdateTrackerPersonListResponse403
    | UpdateTrackerPersonListResponse404
    | UpdateTrackerPersonListResponse422
    | UpdateTrackerPersonListResponse429
    | UpdateTrackerPersonListResponse500
    | UpdateTrackerPersonListResponse503
    | None
):
    r"""Update person tracker list

     Update a person tracker list. Supports replace-all (`trackingRules`) or granular
    (`addRules`/`removeRuleIds`) rule management — but not both in one request.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        body (UpdateTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTrackerPersonListResponse400 | UpdateTrackerPersonListResponse401 | UpdateTrackerPersonListResponse402 | UpdateTrackerPersonListResponse403 | UpdateTrackerPersonListResponse404 | UpdateTrackerPersonListResponse422 | UpdateTrackerPersonListResponse429 | UpdateTrackerPersonListResponse500 | UpdateTrackerPersonListResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
