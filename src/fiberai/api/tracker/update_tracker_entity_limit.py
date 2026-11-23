from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_tracker_entity_limit_body import UpdateTrackerEntityLimitBody
from ...models.update_tracker_entity_limit_response_200 import UpdateTrackerEntityLimitResponse200
from ...models.update_tracker_entity_limit_response_400 import UpdateTrackerEntityLimitResponse400
from ...models.update_tracker_entity_limit_response_401 import UpdateTrackerEntityLimitResponse401
from ...models.update_tracker_entity_limit_response_402 import UpdateTrackerEntityLimitResponse402
from ...models.update_tracker_entity_limit_response_403 import UpdateTrackerEntityLimitResponse403
from ...models.update_tracker_entity_limit_response_404 import UpdateTrackerEntityLimitResponse404
from ...models.update_tracker_entity_limit_response_422 import UpdateTrackerEntityLimitResponse422
from ...models.update_tracker_entity_limit_response_429 import UpdateTrackerEntityLimitResponse429
from ...models.update_tracker_entity_limit_response_500 import UpdateTrackerEntityLimitResponse500
from ...models.update_tracker_entity_limit_response_503 import UpdateTrackerEntityLimitResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateTrackerEntityLimitBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tracker/entity-limit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateTrackerEntityLimitResponse200
    | UpdateTrackerEntityLimitResponse400
    | UpdateTrackerEntityLimitResponse401
    | UpdateTrackerEntityLimitResponse402
    | UpdateTrackerEntityLimitResponse403
    | UpdateTrackerEntityLimitResponse404
    | UpdateTrackerEntityLimitResponse422
    | UpdateTrackerEntityLimitResponse429
    | UpdateTrackerEntityLimitResponse500
    | UpdateTrackerEntityLimitResponse503
    | None
):
    if response.status_code == 200:
        response_200 = UpdateTrackerEntityLimitResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateTrackerEntityLimitResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateTrackerEntityLimitResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = UpdateTrackerEntityLimitResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = UpdateTrackerEntityLimitResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateTrackerEntityLimitResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = UpdateTrackerEntityLimitResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = UpdateTrackerEntityLimitResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateTrackerEntityLimitResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateTrackerEntityLimitResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateTrackerEntityLimitResponse200
    | UpdateTrackerEntityLimitResponse400
    | UpdateTrackerEntityLimitResponse401
    | UpdateTrackerEntityLimitResponse402
    | UpdateTrackerEntityLimitResponse403
    | UpdateTrackerEntityLimitResponse404
    | UpdateTrackerEntityLimitResponse422
    | UpdateTrackerEntityLimitResponse429
    | UpdateTrackerEntityLimitResponse500
    | UpdateTrackerEntityLimitResponse503
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
    body: UpdateTrackerEntityLimitBody,
) -> Response[
    UpdateTrackerEntityLimitResponse200
    | UpdateTrackerEntityLimitResponse400
    | UpdateTrackerEntityLimitResponse401
    | UpdateTrackerEntityLimitResponse402
    | UpdateTrackerEntityLimitResponse403
    | UpdateTrackerEntityLimitResponse404
    | UpdateTrackerEntityLimitResponse422
    | UpdateTrackerEntityLimitResponse429
    | UpdateTrackerEntityLimitResponse500
    | UpdateTrackerEntityLimitResponse503
]:
    """Update tracker entity limits

     Set, raise, lower or remove your organization's limit on how many companies or how many people it
    tracks across its active tracker lists (paused lists don't count). Once a limit is reached, adding
    entities and resuming a paused list are rejected until you raise the limit or remove entities, and
    dynamic lists stop adding new matches. Lowering a limit below the current count removes nothing.
    Returns both limits with current usage; GET /v1/tracker/overview returns the same block.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateTrackerEntityLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTrackerEntityLimitResponse200 | UpdateTrackerEntityLimitResponse400 | UpdateTrackerEntityLimitResponse401 | UpdateTrackerEntityLimitResponse402 | UpdateTrackerEntityLimitResponse403 | UpdateTrackerEntityLimitResponse404 | UpdateTrackerEntityLimitResponse422 | UpdateTrackerEntityLimitResponse429 | UpdateTrackerEntityLimitResponse500 | UpdateTrackerEntityLimitResponse503]
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
    body: UpdateTrackerEntityLimitBody,
) -> (
    UpdateTrackerEntityLimitResponse200
    | UpdateTrackerEntityLimitResponse400
    | UpdateTrackerEntityLimitResponse401
    | UpdateTrackerEntityLimitResponse402
    | UpdateTrackerEntityLimitResponse403
    | UpdateTrackerEntityLimitResponse404
    | UpdateTrackerEntityLimitResponse422
    | UpdateTrackerEntityLimitResponse429
    | UpdateTrackerEntityLimitResponse500
    | UpdateTrackerEntityLimitResponse503
    | None
):
    """Update tracker entity limits

     Set, raise, lower or remove your organization's limit on how many companies or how many people it
    tracks across its active tracker lists (paused lists don't count). Once a limit is reached, adding
    entities and resuming a paused list are rejected until you raise the limit or remove entities, and
    dynamic lists stop adding new matches. Lowering a limit below the current count removes nothing.
    Returns both limits with current usage; GET /v1/tracker/overview returns the same block.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateTrackerEntityLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTrackerEntityLimitResponse200 | UpdateTrackerEntityLimitResponse400 | UpdateTrackerEntityLimitResponse401 | UpdateTrackerEntityLimitResponse402 | UpdateTrackerEntityLimitResponse403 | UpdateTrackerEntityLimitResponse404 | UpdateTrackerEntityLimitResponse422 | UpdateTrackerEntityLimitResponse429 | UpdateTrackerEntityLimitResponse500 | UpdateTrackerEntityLimitResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTrackerEntityLimitBody,
) -> Response[
    UpdateTrackerEntityLimitResponse200
    | UpdateTrackerEntityLimitResponse400
    | UpdateTrackerEntityLimitResponse401
    | UpdateTrackerEntityLimitResponse402
    | UpdateTrackerEntityLimitResponse403
    | UpdateTrackerEntityLimitResponse404
    | UpdateTrackerEntityLimitResponse422
    | UpdateTrackerEntityLimitResponse429
    | UpdateTrackerEntityLimitResponse500
    | UpdateTrackerEntityLimitResponse503
]:
    """Update tracker entity limits

     Set, raise, lower or remove your organization's limit on how many companies or how many people it
    tracks across its active tracker lists (paused lists don't count). Once a limit is reached, adding
    entities and resuming a paused list are rejected until you raise the limit or remove entities, and
    dynamic lists stop adding new matches. Lowering a limit below the current count removes nothing.
    Returns both limits with current usage; GET /v1/tracker/overview returns the same block.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateTrackerEntityLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTrackerEntityLimitResponse200 | UpdateTrackerEntityLimitResponse400 | UpdateTrackerEntityLimitResponse401 | UpdateTrackerEntityLimitResponse402 | UpdateTrackerEntityLimitResponse403 | UpdateTrackerEntityLimitResponse404 | UpdateTrackerEntityLimitResponse422 | UpdateTrackerEntityLimitResponse429 | UpdateTrackerEntityLimitResponse500 | UpdateTrackerEntityLimitResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTrackerEntityLimitBody,
) -> (
    UpdateTrackerEntityLimitResponse200
    | UpdateTrackerEntityLimitResponse400
    | UpdateTrackerEntityLimitResponse401
    | UpdateTrackerEntityLimitResponse402
    | UpdateTrackerEntityLimitResponse403
    | UpdateTrackerEntityLimitResponse404
    | UpdateTrackerEntityLimitResponse422
    | UpdateTrackerEntityLimitResponse429
    | UpdateTrackerEntityLimitResponse500
    | UpdateTrackerEntityLimitResponse503
    | None
):
    """Update tracker entity limits

     Set, raise, lower or remove your organization's limit on how many companies or how many people it
    tracks across its active tracker lists (paused lists don't count). Once a limit is reached, adding
    entities and resuming a paused list are rejected until you raise the limit or remove entities, and
    dynamic lists stop adding new matches. Lowering a limit below the current count removes nothing.
    Returns both limits with current usage; GET /v1/tracker/overview returns the same block.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (UpdateTrackerEntityLimitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTrackerEntityLimitResponse200 | UpdateTrackerEntityLimitResponse400 | UpdateTrackerEntityLimitResponse401 | UpdateTrackerEntityLimitResponse402 | UpdateTrackerEntityLimitResponse403 | UpdateTrackerEntityLimitResponse404 | UpdateTrackerEntityLimitResponse422 | UpdateTrackerEntityLimitResponse429 | UpdateTrackerEntityLimitResponse500 | UpdateTrackerEntityLimitResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
