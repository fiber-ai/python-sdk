from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_job_categories_response_200 import GetJobCategoriesResponse200
from ...models.get_job_categories_response_400 import GetJobCategoriesResponse400
from ...models.get_job_categories_response_401 import GetJobCategoriesResponse401
from ...models.get_job_categories_response_402 import GetJobCategoriesResponse402
from ...models.get_job_categories_response_403 import GetJobCategoriesResponse403
from ...models.get_job_categories_response_404 import GetJobCategoriesResponse404
from ...models.get_job_categories_response_422 import GetJobCategoriesResponse422
from ...models.get_job_categories_response_429 import GetJobCategoriesResponse429
from ...models.get_job_categories_response_500 import GetJobCategoriesResponse500
from ...models.get_job_categories_response_503 import GetJobCategoriesResponse503
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
        "url": "/v1/enums/job-categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetJobCategoriesResponse200
    | GetJobCategoriesResponse400
    | GetJobCategoriesResponse401
    | GetJobCategoriesResponse402
    | GetJobCategoriesResponse403
    | GetJobCategoriesResponse404
    | GetJobCategoriesResponse422
    | GetJobCategoriesResponse429
    | GetJobCategoriesResponse500
    | GetJobCategoriesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetJobCategoriesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetJobCategoriesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetJobCategoriesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetJobCategoriesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetJobCategoriesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetJobCategoriesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetJobCategoriesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetJobCategoriesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetJobCategoriesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetJobCategoriesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetJobCategoriesResponse200
    | GetJobCategoriesResponse400
    | GetJobCategoriesResponse401
    | GetJobCategoriesResponse402
    | GetJobCategoriesResponse403
    | GetJobCategoriesResponse404
    | GetJobCategoriesResponse422
    | GetJobCategoriesResponse429
    | GetJobCategoriesResponse500
    | GetJobCategoriesResponse503
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
    GetJobCategoriesResponse200
    | GetJobCategoriesResponse400
    | GetJobCategoriesResponse401
    | GetJobCategoriesResponse402
    | GetJobCategoriesResponse403
    | GetJobCategoriesResponse404
    | GetJobCategoriesResponse422
    | GetJobCategoriesResponse429
    | GetJobCategoriesResponse500
    | GetJobCategoriesResponse503
]:
    """List job functions, specialties, and seniorities

     Get the job-function and specialty taxonomy behind the `jobCategories` people-search filter, plus
    every value the `seniority` filter accepts. Each function lists the specialties nested under it, and
    either tier can be used in `jobCategories.anyOf` and `jobCategories.noneOf`.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobCategoriesResponse200 | GetJobCategoriesResponse400 | GetJobCategoriesResponse401 | GetJobCategoriesResponse402 | GetJobCategoriesResponse403 | GetJobCategoriesResponse404 | GetJobCategoriesResponse422 | GetJobCategoriesResponse429 | GetJobCategoriesResponse500 | GetJobCategoriesResponse503]
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
    GetJobCategoriesResponse200
    | GetJobCategoriesResponse400
    | GetJobCategoriesResponse401
    | GetJobCategoriesResponse402
    | GetJobCategoriesResponse403
    | GetJobCategoriesResponse404
    | GetJobCategoriesResponse422
    | GetJobCategoriesResponse429
    | GetJobCategoriesResponse500
    | GetJobCategoriesResponse503
    | None
):
    """List job functions, specialties, and seniorities

     Get the job-function and specialty taxonomy behind the `jobCategories` people-search filter, plus
    every value the `seniority` filter accepts. Each function lists the specialties nested under it, and
    either tier can be used in `jobCategories.anyOf` and `jobCategories.noneOf`.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobCategoriesResponse200 | GetJobCategoriesResponse400 | GetJobCategoriesResponse401 | GetJobCategoriesResponse402 | GetJobCategoriesResponse403 | GetJobCategoriesResponse404 | GetJobCategoriesResponse422 | GetJobCategoriesResponse429 | GetJobCategoriesResponse500 | GetJobCategoriesResponse503
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
    GetJobCategoriesResponse200
    | GetJobCategoriesResponse400
    | GetJobCategoriesResponse401
    | GetJobCategoriesResponse402
    | GetJobCategoriesResponse403
    | GetJobCategoriesResponse404
    | GetJobCategoriesResponse422
    | GetJobCategoriesResponse429
    | GetJobCategoriesResponse500
    | GetJobCategoriesResponse503
]:
    """List job functions, specialties, and seniorities

     Get the job-function and specialty taxonomy behind the `jobCategories` people-search filter, plus
    every value the `seniority` filter accepts. Each function lists the specialties nested under it, and
    either tier can be used in `jobCategories.anyOf` and `jobCategories.noneOf`.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobCategoriesResponse200 | GetJobCategoriesResponse400 | GetJobCategoriesResponse401 | GetJobCategoriesResponse402 | GetJobCategoriesResponse403 | GetJobCategoriesResponse404 | GetJobCategoriesResponse422 | GetJobCategoriesResponse429 | GetJobCategoriesResponse500 | GetJobCategoriesResponse503]
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
    GetJobCategoriesResponse200
    | GetJobCategoriesResponse400
    | GetJobCategoriesResponse401
    | GetJobCategoriesResponse402
    | GetJobCategoriesResponse403
    | GetJobCategoriesResponse404
    | GetJobCategoriesResponse422
    | GetJobCategoriesResponse429
    | GetJobCategoriesResponse500
    | GetJobCategoriesResponse503
    | None
):
    """List job functions, specialties, and seniorities

     Get the job-function and specialty taxonomy behind the `jobCategories` people-search filter, plus
    every value the `seniority` filter accepts. Each function lists the specialties nested under it, and
    either tier can be used in `jobCategories.anyOf` and `jobCategories.noneOf`.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobCategoriesResponse200 | GetJobCategoriesResponse400 | GetJobCategoriesResponse401 | GetJobCategoriesResponse402 | GetJobCategoriesResponse403 | GetJobCategoriesResponse404 | GetJobCategoriesResponse422 | GetJobCategoriesResponse429 | GetJobCategoriesResponse500 | GetJobCategoriesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
        )
    ).parsed
