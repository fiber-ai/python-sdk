from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_skills_response_200 import GetSkillsResponse200
from ...models.get_skills_response_400 import GetSkillsResponse400
from ...models.get_skills_response_401 import GetSkillsResponse401
from ...models.get_skills_response_402 import GetSkillsResponse402
from ...models.get_skills_response_403 import GetSkillsResponse403
from ...models.get_skills_response_404 import GetSkillsResponse404
from ...models.get_skills_response_422 import GetSkillsResponse422
from ...models.get_skills_response_429 import GetSkillsResponse429
from ...models.get_skills_response_500 import GetSkillsResponse500
from ...models.get_skills_response_503 import GetSkillsResponse503
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
        "url": "/v1/enums/skills",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSkillsResponse200
    | GetSkillsResponse400
    | GetSkillsResponse401
    | GetSkillsResponse402
    | GetSkillsResponse403
    | GetSkillsResponse404
    | GetSkillsResponse422
    | GetSkillsResponse429
    | GetSkillsResponse500
    | GetSkillsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetSkillsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSkillsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSkillsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetSkillsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetSkillsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSkillsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetSkillsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetSkillsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetSkillsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSkillsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSkillsResponse200
    | GetSkillsResponse400
    | GetSkillsResponse401
    | GetSkillsResponse402
    | GetSkillsResponse403
    | GetSkillsResponse404
    | GetSkillsResponse422
    | GetSkillsResponse429
    | GetSkillsResponse500
    | GetSkillsResponse503
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
    GetSkillsResponse200
    | GetSkillsResponse400
    | GetSkillsResponse401
    | GetSkillsResponse402
    | GetSkillsResponse403
    | GetSkillsResponse404
    | GetSkillsResponse422
    | GetSkillsResponse429
    | GetSkillsResponse500
    | GetSkillsResponse503
]:
    r"""List skills

     Get the most common professional skills across profiles. Returns up to 1,000 skill names sorted by
    popularity. Useful for building skill-based search filters.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSkillsResponse200 | GetSkillsResponse400 | GetSkillsResponse401 | GetSkillsResponse402 | GetSkillsResponse403 | GetSkillsResponse404 | GetSkillsResponse422 | GetSkillsResponse429 | GetSkillsResponse500 | GetSkillsResponse503]
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
    GetSkillsResponse200
    | GetSkillsResponse400
    | GetSkillsResponse401
    | GetSkillsResponse402
    | GetSkillsResponse403
    | GetSkillsResponse404
    | GetSkillsResponse422
    | GetSkillsResponse429
    | GetSkillsResponse500
    | GetSkillsResponse503
    | None
):
    r"""List skills

     Get the most common professional skills across profiles. Returns up to 1,000 skill names sorted by
    popularity. Useful for building skill-based search filters.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSkillsResponse200 | GetSkillsResponse400 | GetSkillsResponse401 | GetSkillsResponse402 | GetSkillsResponse403 | GetSkillsResponse404 | GetSkillsResponse422 | GetSkillsResponse429 | GetSkillsResponse500 | GetSkillsResponse503
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
    GetSkillsResponse200
    | GetSkillsResponse400
    | GetSkillsResponse401
    | GetSkillsResponse402
    | GetSkillsResponse403
    | GetSkillsResponse404
    | GetSkillsResponse422
    | GetSkillsResponse429
    | GetSkillsResponse500
    | GetSkillsResponse503
]:
    r"""List skills

     Get the most common professional skills across profiles. Returns up to 1,000 skill names sorted by
    popularity. Useful for building skill-based search filters.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSkillsResponse200 | GetSkillsResponse400 | GetSkillsResponse401 | GetSkillsResponse402 | GetSkillsResponse403 | GetSkillsResponse404 | GetSkillsResponse422 | GetSkillsResponse429 | GetSkillsResponse500 | GetSkillsResponse503]
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
    GetSkillsResponse200
    | GetSkillsResponse400
    | GetSkillsResponse401
    | GetSkillsResponse402
    | GetSkillsResponse403
    | GetSkillsResponse404
    | GetSkillsResponse422
    | GetSkillsResponse429
    | GetSkillsResponse500
    | GetSkillsResponse503
    | None
):
    r"""List skills

     Get the most common professional skills across profiles. Returns up to 1,000 skill names sorted by
    popularity. Useful for building skill-based search filters.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSkillsResponse200 | GetSkillsResponse400 | GetSkillsResponse401 | GetSkillsResponse402 | GetSkillsResponse403 | GetSkillsResponse404 | GetSkillsResponse422 | GetSkillsResponse429 | GetSkillsResponse500 | GetSkillsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
