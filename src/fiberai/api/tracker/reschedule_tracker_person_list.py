from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reschedule_tracker_person_list_body import RescheduleTrackerPersonListBody
from ...models.reschedule_tracker_person_list_response_200 import RescheduleTrackerPersonListResponse200
from ...models.reschedule_tracker_person_list_response_400 import RescheduleTrackerPersonListResponse400
from ...models.reschedule_tracker_person_list_response_401 import RescheduleTrackerPersonListResponse401
from ...models.reschedule_tracker_person_list_response_402 import RescheduleTrackerPersonListResponse402
from ...models.reschedule_tracker_person_list_response_403 import RescheduleTrackerPersonListResponse403
from ...models.reschedule_tracker_person_list_response_404 import RescheduleTrackerPersonListResponse404
from ...models.reschedule_tracker_person_list_response_422 import RescheduleTrackerPersonListResponse422
from ...models.reschedule_tracker_person_list_response_429 import RescheduleTrackerPersonListResponse429
from ...models.reschedule_tracker_person_list_response_500 import RescheduleTrackerPersonListResponse500
from ...models.reschedule_tracker_person_list_response_503 import RescheduleTrackerPersonListResponse503
from ...types import Response


def _get_kwargs(
    list_id: str,
    *,
    body: RescheduleTrackerPersonListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tracker/person-lists/{list_id}/reschedule".format(
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
    RescheduleTrackerPersonListResponse200
    | RescheduleTrackerPersonListResponse400
    | RescheduleTrackerPersonListResponse401
    | RescheduleTrackerPersonListResponse402
    | RescheduleTrackerPersonListResponse403
    | RescheduleTrackerPersonListResponse404
    | RescheduleTrackerPersonListResponse422
    | RescheduleTrackerPersonListResponse429
    | RescheduleTrackerPersonListResponse500
    | RescheduleTrackerPersonListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RescheduleTrackerPersonListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RescheduleTrackerPersonListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RescheduleTrackerPersonListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RescheduleTrackerPersonListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RescheduleTrackerPersonListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RescheduleTrackerPersonListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = RescheduleTrackerPersonListResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = RescheduleTrackerPersonListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RescheduleTrackerPersonListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RescheduleTrackerPersonListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RescheduleTrackerPersonListResponse200
    | RescheduleTrackerPersonListResponse400
    | RescheduleTrackerPersonListResponse401
    | RescheduleTrackerPersonListResponse402
    | RescheduleTrackerPersonListResponse403
    | RescheduleTrackerPersonListResponse404
    | RescheduleTrackerPersonListResponse422
    | RescheduleTrackerPersonListResponse429
    | RescheduleTrackerPersonListResponse500
    | RescheduleTrackerPersonListResponse503
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
    body: RescheduleTrackerPersonListBody,
) -> Response[
    RescheduleTrackerPersonListResponse200
    | RescheduleTrackerPersonListResponse400
    | RescheduleTrackerPersonListResponse401
    | RescheduleTrackerPersonListResponse402
    | RescheduleTrackerPersonListResponse403
    | RescheduleTrackerPersonListResponse404
    | RescheduleTrackerPersonListResponse422
    | RescheduleTrackerPersonListResponse429
    | RescheduleTrackerPersonListResponse500
    | RescheduleTrackerPersonListResponse503
]:
    """Reschedule person tracker list refresh

     Move this list's next scheduled refresh to a chosen date (UTC) — later (for example to skip a cycle
    or align with a billing period) or earlier, as long as the date is tomorrow or later. The refresh
    runs on the chosen date and checks all tracked people in the list, with credits charged per entity
    as usual. Future refreshes continue at the list's regular interval, counted from the rescheduled
    run. Changing the list's refresh interval later resets the schedule from that moment. To refresh a
    list immediately, use the refresh endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        body (RescheduleTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RescheduleTrackerPersonListResponse200 | RescheduleTrackerPersonListResponse400 | RescheduleTrackerPersonListResponse401 | RescheduleTrackerPersonListResponse402 | RescheduleTrackerPersonListResponse403 | RescheduleTrackerPersonListResponse404 | RescheduleTrackerPersonListResponse422 | RescheduleTrackerPersonListResponse429 | RescheduleTrackerPersonListResponse500 | RescheduleTrackerPersonListResponse503]
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
    body: RescheduleTrackerPersonListBody,
) -> (
    RescheduleTrackerPersonListResponse200
    | RescheduleTrackerPersonListResponse400
    | RescheduleTrackerPersonListResponse401
    | RescheduleTrackerPersonListResponse402
    | RescheduleTrackerPersonListResponse403
    | RescheduleTrackerPersonListResponse404
    | RescheduleTrackerPersonListResponse422
    | RescheduleTrackerPersonListResponse429
    | RescheduleTrackerPersonListResponse500
    | RescheduleTrackerPersonListResponse503
    | None
):
    """Reschedule person tracker list refresh

     Move this list's next scheduled refresh to a chosen date (UTC) — later (for example to skip a cycle
    or align with a billing period) or earlier, as long as the date is tomorrow or later. The refresh
    runs on the chosen date and checks all tracked people in the list, with credits charged per entity
    as usual. Future refreshes continue at the list's regular interval, counted from the rescheduled
    run. Changing the list's refresh interval later resets the schedule from that moment. To refresh a
    list immediately, use the refresh endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        body (RescheduleTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RescheduleTrackerPersonListResponse200 | RescheduleTrackerPersonListResponse400 | RescheduleTrackerPersonListResponse401 | RescheduleTrackerPersonListResponse402 | RescheduleTrackerPersonListResponse403 | RescheduleTrackerPersonListResponse404 | RescheduleTrackerPersonListResponse422 | RescheduleTrackerPersonListResponse429 | RescheduleTrackerPersonListResponse500 | RescheduleTrackerPersonListResponse503
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
    body: RescheduleTrackerPersonListBody,
) -> Response[
    RescheduleTrackerPersonListResponse200
    | RescheduleTrackerPersonListResponse400
    | RescheduleTrackerPersonListResponse401
    | RescheduleTrackerPersonListResponse402
    | RescheduleTrackerPersonListResponse403
    | RescheduleTrackerPersonListResponse404
    | RescheduleTrackerPersonListResponse422
    | RescheduleTrackerPersonListResponse429
    | RescheduleTrackerPersonListResponse500
    | RescheduleTrackerPersonListResponse503
]:
    """Reschedule person tracker list refresh

     Move this list's next scheduled refresh to a chosen date (UTC) — later (for example to skip a cycle
    or align with a billing period) or earlier, as long as the date is tomorrow or later. The refresh
    runs on the chosen date and checks all tracked people in the list, with credits charged per entity
    as usual. Future refreshes continue at the list's regular interval, counted from the rescheduled
    run. Changing the list's refresh interval later resets the schedule from that moment. To refresh a
    list immediately, use the refresh endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        body (RescheduleTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RescheduleTrackerPersonListResponse200 | RescheduleTrackerPersonListResponse400 | RescheduleTrackerPersonListResponse401 | RescheduleTrackerPersonListResponse402 | RescheduleTrackerPersonListResponse403 | RescheduleTrackerPersonListResponse404 | RescheduleTrackerPersonListResponse422 | RescheduleTrackerPersonListResponse429 | RescheduleTrackerPersonListResponse500 | RescheduleTrackerPersonListResponse503]
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
    body: RescheduleTrackerPersonListBody,
) -> (
    RescheduleTrackerPersonListResponse200
    | RescheduleTrackerPersonListResponse400
    | RescheduleTrackerPersonListResponse401
    | RescheduleTrackerPersonListResponse402
    | RescheduleTrackerPersonListResponse403
    | RescheduleTrackerPersonListResponse404
    | RescheduleTrackerPersonListResponse422
    | RescheduleTrackerPersonListResponse429
    | RescheduleTrackerPersonListResponse500
    | RescheduleTrackerPersonListResponse503
    | None
):
    """Reschedule person tracker list refresh

     Move this list's next scheduled refresh to a chosen date (UTC) — later (for example to skip a cycle
    or align with a billing period) or earlier, as long as the date is tomorrow or later. The refresh
    runs on the chosen date and checks all tracked people in the list, with credits charged per entity
    as usual. Future refreshes continue at the list's regular interval, counted from the rescheduled
    run. Changing the list's refresh interval later resets the schedule from that moment. To refresh a
    list immediately, use the refresh endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        list_id (str):
        body (RescheduleTrackerPersonListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RescheduleTrackerPersonListResponse200 | RescheduleTrackerPersonListResponse400 | RescheduleTrackerPersonListResponse401 | RescheduleTrackerPersonListResponse402 | RescheduleTrackerPersonListResponse403 | RescheduleTrackerPersonListResponse404 | RescheduleTrackerPersonListResponse422 | RescheduleTrackerPersonListResponse429 | RescheduleTrackerPersonListResponse500 | RescheduleTrackerPersonListResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
