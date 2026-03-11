from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_saved_search_body import ListSavedSearchBody
from ...models.list_saved_search_response_200 import ListSavedSearchResponse200
from ...models.list_saved_search_response_400 import ListSavedSearchResponse400
from ...models.list_saved_search_response_401 import ListSavedSearchResponse401
from ...models.list_saved_search_response_402 import ListSavedSearchResponse402
from ...models.list_saved_search_response_403 import ListSavedSearchResponse403
from ...models.list_saved_search_response_404 import ListSavedSearchResponse404
from ...models.list_saved_search_response_429 import ListSavedSearchResponse429
from ...models.list_saved_search_response_500 import ListSavedSearchResponse500
from ...models.list_saved_search_response_503 import ListSavedSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ListSavedSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/saved-search/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListSavedSearchResponse200
    | ListSavedSearchResponse400
    | ListSavedSearchResponse401
    | ListSavedSearchResponse402
    | ListSavedSearchResponse403
    | ListSavedSearchResponse404
    | ListSavedSearchResponse429
    | ListSavedSearchResponse500
    | ListSavedSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListSavedSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListSavedSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListSavedSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListSavedSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListSavedSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListSavedSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ListSavedSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListSavedSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListSavedSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListSavedSearchResponse200
    | ListSavedSearchResponse400
    | ListSavedSearchResponse401
    | ListSavedSearchResponse402
    | ListSavedSearchResponse403
    | ListSavedSearchResponse404
    | ListSavedSearchResponse429
    | ListSavedSearchResponse500
    | ListSavedSearchResponse503
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
    body: ListSavedSearchBody,
) -> Response[
    ListSavedSearchResponse200
    | ListSavedSearchResponse400
    | ListSavedSearchResponse401
    | ListSavedSearchResponse402
    | ListSavedSearchResponse403
    | ListSavedSearchResponse404
    | ListSavedSearchResponse429
    | ListSavedSearchResponse500
    | ListSavedSearchResponse503
]:
    r"""List saved searches

     List saved searches

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSavedSearchResponse200 | ListSavedSearchResponse400 | ListSavedSearchResponse401 | ListSavedSearchResponse402 | ListSavedSearchResponse403 | ListSavedSearchResponse404 | ListSavedSearchResponse429 | ListSavedSearchResponse500 | ListSavedSearchResponse503]
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
    body: ListSavedSearchBody,
) -> (
    ListSavedSearchResponse200
    | ListSavedSearchResponse400
    | ListSavedSearchResponse401
    | ListSavedSearchResponse402
    | ListSavedSearchResponse403
    | ListSavedSearchResponse404
    | ListSavedSearchResponse429
    | ListSavedSearchResponse500
    | ListSavedSearchResponse503
    | None
):
    r"""List saved searches

     List saved searches

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSavedSearchResponse200 | ListSavedSearchResponse400 | ListSavedSearchResponse401 | ListSavedSearchResponse402 | ListSavedSearchResponse403 | ListSavedSearchResponse404 | ListSavedSearchResponse429 | ListSavedSearchResponse500 | ListSavedSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListSavedSearchBody,
) -> Response[
    ListSavedSearchResponse200
    | ListSavedSearchResponse400
    | ListSavedSearchResponse401
    | ListSavedSearchResponse402
    | ListSavedSearchResponse403
    | ListSavedSearchResponse404
    | ListSavedSearchResponse429
    | ListSavedSearchResponse500
    | ListSavedSearchResponse503
]:
    r"""List saved searches

     List saved searches

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSavedSearchResponse200 | ListSavedSearchResponse400 | ListSavedSearchResponse401 | ListSavedSearchResponse402 | ListSavedSearchResponse403 | ListSavedSearchResponse404 | ListSavedSearchResponse429 | ListSavedSearchResponse500 | ListSavedSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListSavedSearchBody,
) -> (
    ListSavedSearchResponse200
    | ListSavedSearchResponse400
    | ListSavedSearchResponse401
    | ListSavedSearchResponse402
    | ListSavedSearchResponse403
    | ListSavedSearchResponse404
    | ListSavedSearchResponse429
    | ListSavedSearchResponse500
    | ListSavedSearchResponse503
    | None
):
    r"""List saved searches

     List saved searches

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ListSavedSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSavedSearchResponse200 | ListSavedSearchResponse400 | ListSavedSearchResponse401 | ListSavedSearchResponse402 | ListSavedSearchResponse403 | ListSavedSearchResponse404 | ListSavedSearchResponse429 | ListSavedSearchResponse500 | ListSavedSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
