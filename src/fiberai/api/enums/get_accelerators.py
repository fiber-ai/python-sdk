from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_accelerators_response_200 import GetAcceleratorsResponse200
from ...models.get_accelerators_response_400 import GetAcceleratorsResponse400
from ...models.get_accelerators_response_401 import GetAcceleratorsResponse401
from ...models.get_accelerators_response_402 import GetAcceleratorsResponse402
from ...models.get_accelerators_response_403 import GetAcceleratorsResponse403
from ...models.get_accelerators_response_404 import GetAcceleratorsResponse404
from ...models.get_accelerators_response_429 import GetAcceleratorsResponse429
from ...models.get_accelerators_response_500 import GetAcceleratorsResponse500
from ...models.get_accelerators_response_503 import GetAcceleratorsResponse503
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
        "url": "/v1/enums/accelerators",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAcceleratorsResponse200
    | GetAcceleratorsResponse400
    | GetAcceleratorsResponse401
    | GetAcceleratorsResponse402
    | GetAcceleratorsResponse403
    | GetAcceleratorsResponse404
    | GetAcceleratorsResponse429
    | GetAcceleratorsResponse500
    | GetAcceleratorsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetAcceleratorsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAcceleratorsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAcceleratorsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetAcceleratorsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetAcceleratorsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAcceleratorsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetAcceleratorsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAcceleratorsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAcceleratorsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAcceleratorsResponse200
    | GetAcceleratorsResponse400
    | GetAcceleratorsResponse401
    | GetAcceleratorsResponse402
    | GetAcceleratorsResponse403
    | GetAcceleratorsResponse404
    | GetAcceleratorsResponse429
    | GetAcceleratorsResponse500
    | GetAcceleratorsResponse503
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
    GetAcceleratorsResponse200
    | GetAcceleratorsResponse400
    | GetAcceleratorsResponse401
    | GetAcceleratorsResponse402
    | GetAcceleratorsResponse403
    | GetAcceleratorsResponse404
    | GetAcceleratorsResponse429
    | GetAcceleratorsResponse500
    | GetAcceleratorsResponse503
]:
    r"""List accelerators

     Get a list of all accelerators with their metadata, total company counts, and statistics broken down
    by batch and year. Useful for filtering accelerator data in search APIs.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAcceleratorsResponse200 | GetAcceleratorsResponse400 | GetAcceleratorsResponse401 | GetAcceleratorsResponse402 | GetAcceleratorsResponse403 | GetAcceleratorsResponse404 | GetAcceleratorsResponse429 | GetAcceleratorsResponse500 | GetAcceleratorsResponse503]
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
    GetAcceleratorsResponse200
    | GetAcceleratorsResponse400
    | GetAcceleratorsResponse401
    | GetAcceleratorsResponse402
    | GetAcceleratorsResponse403
    | GetAcceleratorsResponse404
    | GetAcceleratorsResponse429
    | GetAcceleratorsResponse500
    | GetAcceleratorsResponse503
    | None
):
    r"""List accelerators

     Get a list of all accelerators with their metadata, total company counts, and statistics broken down
    by batch and year. Useful for filtering accelerator data in search APIs.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAcceleratorsResponse200 | GetAcceleratorsResponse400 | GetAcceleratorsResponse401 | GetAcceleratorsResponse402 | GetAcceleratorsResponse403 | GetAcceleratorsResponse404 | GetAcceleratorsResponse429 | GetAcceleratorsResponse500 | GetAcceleratorsResponse503
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
    GetAcceleratorsResponse200
    | GetAcceleratorsResponse400
    | GetAcceleratorsResponse401
    | GetAcceleratorsResponse402
    | GetAcceleratorsResponse403
    | GetAcceleratorsResponse404
    | GetAcceleratorsResponse429
    | GetAcceleratorsResponse500
    | GetAcceleratorsResponse503
]:
    r"""List accelerators

     Get a list of all accelerators with their metadata, total company counts, and statistics broken down
    by batch and year. Useful for filtering accelerator data in search APIs.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAcceleratorsResponse200 | GetAcceleratorsResponse400 | GetAcceleratorsResponse401 | GetAcceleratorsResponse402 | GetAcceleratorsResponse403 | GetAcceleratorsResponse404 | GetAcceleratorsResponse429 | GetAcceleratorsResponse500 | GetAcceleratorsResponse503]
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
    GetAcceleratorsResponse200
    | GetAcceleratorsResponse400
    | GetAcceleratorsResponse401
    | GetAcceleratorsResponse402
    | GetAcceleratorsResponse403
    | GetAcceleratorsResponse404
    | GetAcceleratorsResponse429
    | GetAcceleratorsResponse500
    | GetAcceleratorsResponse503
    | None
):
    r"""List accelerators

     Get a list of all accelerators with their metadata, total company counts, and statistics broken down
    by batch and year. Useful for filtering accelerator data in search APIs.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAcceleratorsResponse200 | GetAcceleratorsResponse400 | GetAcceleratorsResponse401 | GetAcceleratorsResponse402 | GetAcceleratorsResponse403 | GetAcceleratorsResponse404 | GetAcceleratorsResponse429 | GetAcceleratorsResponse500 | GetAcceleratorsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
