from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_audiences_response_200 import ListAudiencesResponse200
from ...models.list_audiences_response_400 import ListAudiencesResponse400
from ...models.list_audiences_response_401 import ListAudiencesResponse401
from ...models.list_audiences_response_402 import ListAudiencesResponse402
from ...models.list_audiences_response_403 import ListAudiencesResponse403
from ...models.list_audiences_response_404 import ListAudiencesResponse404
from ...models.list_audiences_response_429 import ListAudiencesResponse429
from ...models.list_audiences_response_500 import ListAudiencesResponse500
from ...models.list_audiences_response_503 import ListAudiencesResponse503
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
        "url": "/v1/audiences",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListAudiencesResponse200
    | ListAudiencesResponse400
    | ListAudiencesResponse401
    | ListAudiencesResponse402
    | ListAudiencesResponse403
    | ListAudiencesResponse404
    | ListAudiencesResponse429
    | ListAudiencesResponse500
    | ListAudiencesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListAudiencesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListAudiencesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListAudiencesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListAudiencesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListAudiencesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListAudiencesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ListAudiencesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListAudiencesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListAudiencesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListAudiencesResponse200
    | ListAudiencesResponse400
    | ListAudiencesResponse401
    | ListAudiencesResponse402
    | ListAudiencesResponse403
    | ListAudiencesResponse404
    | ListAudiencesResponse429
    | ListAudiencesResponse500
    | ListAudiencesResponse503
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
    ListAudiencesResponse200
    | ListAudiencesResponse400
    | ListAudiencesResponse401
    | ListAudiencesResponse402
    | ListAudiencesResponse403
    | ListAudiencesResponse404
    | ListAudiencesResponse429
    | ListAudiencesResponse500
    | ListAudiencesResponse503
]:
    r"""List all audiences

     Lists all audiences for your organization. Returns basic info and counts for each audience. Only
    visible audiences are returned (hidden system audiences are excluded). Pass your apiKey in the query
    string.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAudiencesResponse200 | ListAudiencesResponse400 | ListAudiencesResponse401 | ListAudiencesResponse402 | ListAudiencesResponse403 | ListAudiencesResponse404 | ListAudiencesResponse429 | ListAudiencesResponse500 | ListAudiencesResponse503]
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
    ListAudiencesResponse200
    | ListAudiencesResponse400
    | ListAudiencesResponse401
    | ListAudiencesResponse402
    | ListAudiencesResponse403
    | ListAudiencesResponse404
    | ListAudiencesResponse429
    | ListAudiencesResponse500
    | ListAudiencesResponse503
    | None
):
    r"""List all audiences

     Lists all audiences for your organization. Returns basic info and counts for each audience. Only
    visible audiences are returned (hidden system audiences are excluded). Pass your apiKey in the query
    string.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAudiencesResponse200 | ListAudiencesResponse400 | ListAudiencesResponse401 | ListAudiencesResponse402 | ListAudiencesResponse403 | ListAudiencesResponse404 | ListAudiencesResponse429 | ListAudiencesResponse500 | ListAudiencesResponse503
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
    ListAudiencesResponse200
    | ListAudiencesResponse400
    | ListAudiencesResponse401
    | ListAudiencesResponse402
    | ListAudiencesResponse403
    | ListAudiencesResponse404
    | ListAudiencesResponse429
    | ListAudiencesResponse500
    | ListAudiencesResponse503
]:
    r"""List all audiences

     Lists all audiences for your organization. Returns basic info and counts for each audience. Only
    visible audiences are returned (hidden system audiences are excluded). Pass your apiKey in the query
    string.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAudiencesResponse200 | ListAudiencesResponse400 | ListAudiencesResponse401 | ListAudiencesResponse402 | ListAudiencesResponse403 | ListAudiencesResponse404 | ListAudiencesResponse429 | ListAudiencesResponse500 | ListAudiencesResponse503]
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
    ListAudiencesResponse200
    | ListAudiencesResponse400
    | ListAudiencesResponse401
    | ListAudiencesResponse402
    | ListAudiencesResponse403
    | ListAudiencesResponse404
    | ListAudiencesResponse429
    | ListAudiencesResponse500
    | ListAudiencesResponse503
    | None
):
    r"""List all audiences

     Lists all audiences for your organization. Returns basic info and counts for each audience. Only
    visible audiences are returned (hidden system audiences are excluded). Pass your apiKey in the query
    string.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAudiencesResponse200 | ListAudiencesResponse400 | ListAudiencesResponse401 | ListAudiencesResponse402 | ListAudiencesResponse403 | ListAudiencesResponse404 | ListAudiencesResponse429 | ListAudiencesResponse500 | ListAudiencesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
