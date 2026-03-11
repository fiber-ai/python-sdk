from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_response_200 import GetTagsResponse200
from ...models.get_tags_response_400 import GetTagsResponse400
from ...models.get_tags_response_401 import GetTagsResponse401
from ...models.get_tags_response_402 import GetTagsResponse402
from ...models.get_tags_response_403 import GetTagsResponse403
from ...models.get_tags_response_404 import GetTagsResponse404
from ...models.get_tags_response_429 import GetTagsResponse429
from ...models.get_tags_response_500 import GetTagsResponse500
from ...models.get_tags_response_503 import GetTagsResponse503
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
        "url": "/v1/enums/tags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetTagsResponse200
    | GetTagsResponse400
    | GetTagsResponse401
    | GetTagsResponse402
    | GetTagsResponse403
    | GetTagsResponse404
    | GetTagsResponse429
    | GetTagsResponse500
    | GetTagsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetTagsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetTagsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetTagsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetTagsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetTagsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetTagsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetTagsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetTagsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetTagsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetTagsResponse200
    | GetTagsResponse400
    | GetTagsResponse401
    | GetTagsResponse402
    | GetTagsResponse403
    | GetTagsResponse404
    | GetTagsResponse429
    | GetTagsResponse500
    | GetTagsResponse503
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
    GetTagsResponse200
    | GetTagsResponse400
    | GetTagsResponse401
    | GetTagsResponse402
    | GetTagsResponse403
    | GetTagsResponse404
    | GetTagsResponse429
    | GetTagsResponse500
    | GetTagsResponse503
]:
    r"""List profile and company tags

     Get a list of all profile and company tags that you can use to filter searches in our API, along
    with their descriptions.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsResponse200 | GetTagsResponse400 | GetTagsResponse401 | GetTagsResponse402 | GetTagsResponse403 | GetTagsResponse404 | GetTagsResponse429 | GetTagsResponse500 | GetTagsResponse503]
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
    GetTagsResponse200
    | GetTagsResponse400
    | GetTagsResponse401
    | GetTagsResponse402
    | GetTagsResponse403
    | GetTagsResponse404
    | GetTagsResponse429
    | GetTagsResponse500
    | GetTagsResponse503
    | None
):
    r"""List profile and company tags

     Get a list of all profile and company tags that you can use to filter searches in our API, along
    with their descriptions.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsResponse200 | GetTagsResponse400 | GetTagsResponse401 | GetTagsResponse402 | GetTagsResponse403 | GetTagsResponse404 | GetTagsResponse429 | GetTagsResponse500 | GetTagsResponse503
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
    GetTagsResponse200
    | GetTagsResponse400
    | GetTagsResponse401
    | GetTagsResponse402
    | GetTagsResponse403
    | GetTagsResponse404
    | GetTagsResponse429
    | GetTagsResponse500
    | GetTagsResponse503
]:
    r"""List profile and company tags

     Get a list of all profile and company tags that you can use to filter searches in our API, along
    with their descriptions.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsResponse200 | GetTagsResponse400 | GetTagsResponse401 | GetTagsResponse402 | GetTagsResponse403 | GetTagsResponse404 | GetTagsResponse429 | GetTagsResponse500 | GetTagsResponse503]
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
    GetTagsResponse200
    | GetTagsResponse400
    | GetTagsResponse401
    | GetTagsResponse402
    | GetTagsResponse403
    | GetTagsResponse404
    | GetTagsResponse429
    | GetTagsResponse500
    | GetTagsResponse503
    | None
):
    r"""List profile and company tags

     Get a list of all profile and company tags that you can use to filter searches in our API, along
    with their descriptions.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsResponse200 | GetTagsResponse400 | GetTagsResponse401 | GetTagsResponse402 | GetTagsResponse403 | GetTagsResponse404 | GetTagsResponse429 | GetTagsResponse500 | GetTagsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
