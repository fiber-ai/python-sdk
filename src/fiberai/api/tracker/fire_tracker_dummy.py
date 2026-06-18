from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fire_tracker_dummy_response_200 import FireTrackerDummyResponse200
from ...models.fire_tracker_dummy_response_400 import FireTrackerDummyResponse400
from ...models.fire_tracker_dummy_response_401 import FireTrackerDummyResponse401
from ...models.fire_tracker_dummy_response_402 import FireTrackerDummyResponse402
from ...models.fire_tracker_dummy_response_403 import FireTrackerDummyResponse403
from ...models.fire_tracker_dummy_response_404 import FireTrackerDummyResponse404
from ...models.fire_tracker_dummy_response_422 import FireTrackerDummyResponse422
from ...models.fire_tracker_dummy_response_429 import FireTrackerDummyResponse429
from ...models.fire_tracker_dummy_response_500 import FireTrackerDummyResponse500
from ...models.fire_tracker_dummy_response_503 import FireTrackerDummyResponse503
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
        "method": "post",
        "url": "/v1/tracker/fire-dummy/{list_id}".format(
            list_id=quote(str(list_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FireTrackerDummyResponse200
    | FireTrackerDummyResponse400
    | FireTrackerDummyResponse401
    | FireTrackerDummyResponse402
    | FireTrackerDummyResponse403
    | FireTrackerDummyResponse404
    | FireTrackerDummyResponse422
    | FireTrackerDummyResponse429
    | FireTrackerDummyResponse500
    | FireTrackerDummyResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FireTrackerDummyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FireTrackerDummyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FireTrackerDummyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FireTrackerDummyResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FireTrackerDummyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FireTrackerDummyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FireTrackerDummyResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FireTrackerDummyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FireTrackerDummyResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FireTrackerDummyResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FireTrackerDummyResponse200
    | FireTrackerDummyResponse400
    | FireTrackerDummyResponse401
    | FireTrackerDummyResponse402
    | FireTrackerDummyResponse403
    | FireTrackerDummyResponse404
    | FireTrackerDummyResponse422
    | FireTrackerDummyResponse429
    | FireTrackerDummyResponse500
    | FireTrackerDummyResponse503
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
    FireTrackerDummyResponse200
    | FireTrackerDummyResponse400
    | FireTrackerDummyResponse401
    | FireTrackerDummyResponse402
    | FireTrackerDummyResponse403
    | FireTrackerDummyResponse404
    | FireTrackerDummyResponse422
    | FireTrackerDummyResponse429
    | FireTrackerDummyResponse500
    | FireTrackerDummyResponse503
]:
    r"""Fire test signals

     Send test signals to validate your integration end-to-end. Add rules with `isDummy: true` to your
    list, then call this endpoint. Each dummy rule produces a synthetic signal and persists it to your
    account. If the list has no entities, a well-known example (Google for company lists, Bill Gates for
    person lists) is added automatically.

    **Via webhooks** — If you have a webhook endpoint configured, test signals are delivered immediately
    with `isDummy: true` in the payload so you can distinguish them from real signals.

    **Via API polling** — If you consume signals by polling the API, retrieve your test signals with
    `GET /v1/tracker/signals/:listId?filter=dummy`. This returns the same response format as production
    signals, so you can validate your parsing logic without needing a webhook endpoint.

    Completely free, re-triggerable with no cooldown, and has no effect on real monitoring. Dummy rules
    are never evaluated during normal scheduled runs.

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
        Response[FireTrackerDummyResponse200 | FireTrackerDummyResponse400 | FireTrackerDummyResponse401 | FireTrackerDummyResponse402 | FireTrackerDummyResponse403 | FireTrackerDummyResponse404 | FireTrackerDummyResponse422 | FireTrackerDummyResponse429 | FireTrackerDummyResponse500 | FireTrackerDummyResponse503]
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
    FireTrackerDummyResponse200
    | FireTrackerDummyResponse400
    | FireTrackerDummyResponse401
    | FireTrackerDummyResponse402
    | FireTrackerDummyResponse403
    | FireTrackerDummyResponse404
    | FireTrackerDummyResponse422
    | FireTrackerDummyResponse429
    | FireTrackerDummyResponse500
    | FireTrackerDummyResponse503
    | None
):
    r"""Fire test signals

     Send test signals to validate your integration end-to-end. Add rules with `isDummy: true` to your
    list, then call this endpoint. Each dummy rule produces a synthetic signal and persists it to your
    account. If the list has no entities, a well-known example (Google for company lists, Bill Gates for
    person lists) is added automatically.

    **Via webhooks** — If you have a webhook endpoint configured, test signals are delivered immediately
    with `isDummy: true` in the payload so you can distinguish them from real signals.

    **Via API polling** — If you consume signals by polling the API, retrieve your test signals with
    `GET /v1/tracker/signals/:listId?filter=dummy`. This returns the same response format as production
    signals, so you can validate your parsing logic without needing a webhook endpoint.

    Completely free, re-triggerable with no cooldown, and has no effect on real monitoring. Dummy rules
    are never evaluated during normal scheduled runs.

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
        FireTrackerDummyResponse200 | FireTrackerDummyResponse400 | FireTrackerDummyResponse401 | FireTrackerDummyResponse402 | FireTrackerDummyResponse403 | FireTrackerDummyResponse404 | FireTrackerDummyResponse422 | FireTrackerDummyResponse429 | FireTrackerDummyResponse500 | FireTrackerDummyResponse503
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
    FireTrackerDummyResponse200
    | FireTrackerDummyResponse400
    | FireTrackerDummyResponse401
    | FireTrackerDummyResponse402
    | FireTrackerDummyResponse403
    | FireTrackerDummyResponse404
    | FireTrackerDummyResponse422
    | FireTrackerDummyResponse429
    | FireTrackerDummyResponse500
    | FireTrackerDummyResponse503
]:
    r"""Fire test signals

     Send test signals to validate your integration end-to-end. Add rules with `isDummy: true` to your
    list, then call this endpoint. Each dummy rule produces a synthetic signal and persists it to your
    account. If the list has no entities, a well-known example (Google for company lists, Bill Gates for
    person lists) is added automatically.

    **Via webhooks** — If you have a webhook endpoint configured, test signals are delivered immediately
    with `isDummy: true` in the payload so you can distinguish them from real signals.

    **Via API polling** — If you consume signals by polling the API, retrieve your test signals with
    `GET /v1/tracker/signals/:listId?filter=dummy`. This returns the same response format as production
    signals, so you can validate your parsing logic without needing a webhook endpoint.

    Completely free, re-triggerable with no cooldown, and has no effect on real monitoring. Dummy rules
    are never evaluated during normal scheduled runs.

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
        Response[FireTrackerDummyResponse200 | FireTrackerDummyResponse400 | FireTrackerDummyResponse401 | FireTrackerDummyResponse402 | FireTrackerDummyResponse403 | FireTrackerDummyResponse404 | FireTrackerDummyResponse422 | FireTrackerDummyResponse429 | FireTrackerDummyResponse500 | FireTrackerDummyResponse503]
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
    FireTrackerDummyResponse200
    | FireTrackerDummyResponse400
    | FireTrackerDummyResponse401
    | FireTrackerDummyResponse402
    | FireTrackerDummyResponse403
    | FireTrackerDummyResponse404
    | FireTrackerDummyResponse422
    | FireTrackerDummyResponse429
    | FireTrackerDummyResponse500
    | FireTrackerDummyResponse503
    | None
):
    r"""Fire test signals

     Send test signals to validate your integration end-to-end. Add rules with `isDummy: true` to your
    list, then call this endpoint. Each dummy rule produces a synthetic signal and persists it to your
    account. If the list has no entities, a well-known example (Google for company lists, Bill Gates for
    person lists) is added automatically.

    **Via webhooks** — If you have a webhook endpoint configured, test signals are delivered immediately
    with `isDummy: true` in the payload so you can distinguish them from real signals.

    **Via API polling** — If you consume signals by polling the API, retrieve your test signals with
    `GET /v1/tracker/signals/:listId?filter=dummy`. This returns the same response format as production
    signals, so you can validate your parsing logic without needing a webhook endpoint.

    Completely free, re-triggerable with no cooldown, and has no effect on real monitoring. Dummy rules
    are never evaluated during normal scheduled runs.

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
        FireTrackerDummyResponse200 | FireTrackerDummyResponse400 | FireTrackerDummyResponse401 | FireTrackerDummyResponse402 | FireTrackerDummyResponse403 | FireTrackerDummyResponse404 | FireTrackerDummyResponse422 | FireTrackerDummyResponse429 | FireTrackerDummyResponse500 | FireTrackerDummyResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            api_key=api_key,
        )
    ).parsed
