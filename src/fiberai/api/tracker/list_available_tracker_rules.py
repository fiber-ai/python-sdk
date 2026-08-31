from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_available_tracker_rules_response_200 import ListAvailableTrackerRulesResponse200
from ...models.list_available_tracker_rules_response_400 import ListAvailableTrackerRulesResponse400
from ...models.list_available_tracker_rules_response_401 import ListAvailableTrackerRulesResponse401
from ...models.list_available_tracker_rules_response_402 import ListAvailableTrackerRulesResponse402
from ...models.list_available_tracker_rules_response_403 import ListAvailableTrackerRulesResponse403
from ...models.list_available_tracker_rules_response_404 import ListAvailableTrackerRulesResponse404
from ...models.list_available_tracker_rules_response_422 import ListAvailableTrackerRulesResponse422
from ...models.list_available_tracker_rules_response_429 import ListAvailableTrackerRulesResponse429
from ...models.list_available_tracker_rules_response_500 import ListAvailableTrackerRulesResponse500
from ...models.list_available_tracker_rules_response_503 import ListAvailableTrackerRulesResponse503
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
        "url": "/v1/tracker/rules",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListAvailableTrackerRulesResponse200
    | ListAvailableTrackerRulesResponse400
    | ListAvailableTrackerRulesResponse401
    | ListAvailableTrackerRulesResponse402
    | ListAvailableTrackerRulesResponse403
    | ListAvailableTrackerRulesResponse404
    | ListAvailableTrackerRulesResponse422
    | ListAvailableTrackerRulesResponse429
    | ListAvailableTrackerRulesResponse500
    | ListAvailableTrackerRulesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListAvailableTrackerRulesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListAvailableTrackerRulesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListAvailableTrackerRulesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListAvailableTrackerRulesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListAvailableTrackerRulesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListAvailableTrackerRulesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ListAvailableTrackerRulesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ListAvailableTrackerRulesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListAvailableTrackerRulesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListAvailableTrackerRulesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListAvailableTrackerRulesResponse200
    | ListAvailableTrackerRulesResponse400
    | ListAvailableTrackerRulesResponse401
    | ListAvailableTrackerRulesResponse402
    | ListAvailableTrackerRulesResponse403
    | ListAvailableTrackerRulesResponse404
    | ListAvailableTrackerRulesResponse422
    | ListAvailableTrackerRulesResponse429
    | ListAvailableTrackerRulesResponse500
    | ListAvailableTrackerRulesResponse503
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
    ListAvailableTrackerRulesResponse200
    | ListAvailableTrackerRulesResponse400
    | ListAvailableTrackerRulesResponse401
    | ListAvailableTrackerRulesResponse402
    | ListAvailableTrackerRulesResponse403
    | ListAvailableTrackerRulesResponse404
    | ListAvailableTrackerRulesResponse422
    | ListAvailableTrackerRulesResponse429
    | ListAvailableTrackerRulesResponse500
    | ListAvailableTrackerRulesResponse503
]:
    """List available tracker rules

     Returns all available tracker rule types with descriptions, configuration schemas, example configs,
    and example signal payloads. Use this to discover what rules exist before creating tracker lists.
    The response is deterministic — same output on every call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAvailableTrackerRulesResponse200 | ListAvailableTrackerRulesResponse400 | ListAvailableTrackerRulesResponse401 | ListAvailableTrackerRulesResponse402 | ListAvailableTrackerRulesResponse403 | ListAvailableTrackerRulesResponse404 | ListAvailableTrackerRulesResponse422 | ListAvailableTrackerRulesResponse429 | ListAvailableTrackerRulesResponse500 | ListAvailableTrackerRulesResponse503]
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
    ListAvailableTrackerRulesResponse200
    | ListAvailableTrackerRulesResponse400
    | ListAvailableTrackerRulesResponse401
    | ListAvailableTrackerRulesResponse402
    | ListAvailableTrackerRulesResponse403
    | ListAvailableTrackerRulesResponse404
    | ListAvailableTrackerRulesResponse422
    | ListAvailableTrackerRulesResponse429
    | ListAvailableTrackerRulesResponse500
    | ListAvailableTrackerRulesResponse503
    | None
):
    """List available tracker rules

     Returns all available tracker rule types with descriptions, configuration schemas, example configs,
    and example signal payloads. Use this to discover what rules exist before creating tracker lists.
    The response is deterministic — same output on every call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAvailableTrackerRulesResponse200 | ListAvailableTrackerRulesResponse400 | ListAvailableTrackerRulesResponse401 | ListAvailableTrackerRulesResponse402 | ListAvailableTrackerRulesResponse403 | ListAvailableTrackerRulesResponse404 | ListAvailableTrackerRulesResponse422 | ListAvailableTrackerRulesResponse429 | ListAvailableTrackerRulesResponse500 | ListAvailableTrackerRulesResponse503
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
    ListAvailableTrackerRulesResponse200
    | ListAvailableTrackerRulesResponse400
    | ListAvailableTrackerRulesResponse401
    | ListAvailableTrackerRulesResponse402
    | ListAvailableTrackerRulesResponse403
    | ListAvailableTrackerRulesResponse404
    | ListAvailableTrackerRulesResponse422
    | ListAvailableTrackerRulesResponse429
    | ListAvailableTrackerRulesResponse500
    | ListAvailableTrackerRulesResponse503
]:
    """List available tracker rules

     Returns all available tracker rule types with descriptions, configuration schemas, example configs,
    and example signal payloads. Use this to discover what rules exist before creating tracker lists.
    The response is deterministic — same output on every call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAvailableTrackerRulesResponse200 | ListAvailableTrackerRulesResponse400 | ListAvailableTrackerRulesResponse401 | ListAvailableTrackerRulesResponse402 | ListAvailableTrackerRulesResponse403 | ListAvailableTrackerRulesResponse404 | ListAvailableTrackerRulesResponse422 | ListAvailableTrackerRulesResponse429 | ListAvailableTrackerRulesResponse500 | ListAvailableTrackerRulesResponse503]
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
    ListAvailableTrackerRulesResponse200
    | ListAvailableTrackerRulesResponse400
    | ListAvailableTrackerRulesResponse401
    | ListAvailableTrackerRulesResponse402
    | ListAvailableTrackerRulesResponse403
    | ListAvailableTrackerRulesResponse404
    | ListAvailableTrackerRulesResponse422
    | ListAvailableTrackerRulesResponse429
    | ListAvailableTrackerRulesResponse500
    | ListAvailableTrackerRulesResponse503
    | None
):
    """List available tracker rules

     Returns all available tracker rule types with descriptions, configuration schemas, example configs,
    and example signal payloads. Use this to discover what rules exist before creating tracker lists.
    The response is deterministic — same output on every call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAvailableTrackerRulesResponse200 | ListAvailableTrackerRulesResponse400 | ListAvailableTrackerRulesResponse401 | ListAvailableTrackerRulesResponse402 | ListAvailableTrackerRulesResponse403 | ListAvailableTrackerRulesResponse404 | ListAvailableTrackerRulesResponse422 | ListAvailableTrackerRulesResponse429 | ListAvailableTrackerRulesResponse500 | ListAvailableTrackerRulesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
