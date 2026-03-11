from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_audience_companies_response_200 import GetAudienceCompaniesResponse200
from ...models.get_audience_companies_response_400 import GetAudienceCompaniesResponse400
from ...models.get_audience_companies_response_401 import GetAudienceCompaniesResponse401
from ...models.get_audience_companies_response_402 import GetAudienceCompaniesResponse402
from ...models.get_audience_companies_response_403 import GetAudienceCompaniesResponse403
from ...models.get_audience_companies_response_404 import GetAudienceCompaniesResponse404
from ...models.get_audience_companies_response_429 import GetAudienceCompaniesResponse429
from ...models.get_audience_companies_response_500 import GetAudienceCompaniesResponse500
from ...models.get_audience_companies_response_503 import GetAudienceCompaniesResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    audience_id: str,
    *,
    api_key: str,
    page_size: int | Unset = 100,
    cursor: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params["pageSize"] = page_size

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audiences/{audience_id}/companies".format(
            audience_id=quote(str(audience_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAudienceCompaniesResponse200
    | GetAudienceCompaniesResponse400
    | GetAudienceCompaniesResponse401
    | GetAudienceCompaniesResponse402
    | GetAudienceCompaniesResponse403
    | GetAudienceCompaniesResponse404
    | GetAudienceCompaniesResponse429
    | GetAudienceCompaniesResponse500
    | GetAudienceCompaniesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetAudienceCompaniesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAudienceCompaniesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAudienceCompaniesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetAudienceCompaniesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetAudienceCompaniesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAudienceCompaniesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetAudienceCompaniesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAudienceCompaniesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAudienceCompaniesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAudienceCompaniesResponse200
    | GetAudienceCompaniesResponse400
    | GetAudienceCompaniesResponse401
    | GetAudienceCompaniesResponse402
    | GetAudienceCompaniesResponse403
    | GetAudienceCompaniesResponse404
    | GetAudienceCompaniesResponse429
    | GetAudienceCompaniesResponse500
    | GetAudienceCompaniesResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    page_size: int | Unset = 100,
    cursor: None | str | Unset = UNSET,
) -> Response[
    GetAudienceCompaniesResponse200
    | GetAudienceCompaniesResponse400
    | GetAudienceCompaniesResponse401
    | GetAudienceCompaniesResponse402
    | GetAudienceCompaniesResponse403
    | GetAudienceCompaniesResponse404
    | GetAudienceCompaniesResponse429
    | GetAudienceCompaniesResponse500
    | GetAudienceCompaniesResponse503
]:
    r"""Get companies in an audience

     Gets the companies in an audience with pagination. Use the nextCursor from the response to fetch the
    next page. Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):
        page_size (int | Unset):  Default: 100.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAudienceCompaniesResponse200 | GetAudienceCompaniesResponse400 | GetAudienceCompaniesResponse401 | GetAudienceCompaniesResponse402 | GetAudienceCompaniesResponse403 | GetAudienceCompaniesResponse404 | GetAudienceCompaniesResponse429 | GetAudienceCompaniesResponse500 | GetAudienceCompaniesResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        api_key=api_key,
        page_size=page_size,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    page_size: int | Unset = 100,
    cursor: None | str | Unset = UNSET,
) -> (
    GetAudienceCompaniesResponse200
    | GetAudienceCompaniesResponse400
    | GetAudienceCompaniesResponse401
    | GetAudienceCompaniesResponse402
    | GetAudienceCompaniesResponse403
    | GetAudienceCompaniesResponse404
    | GetAudienceCompaniesResponse429
    | GetAudienceCompaniesResponse500
    | GetAudienceCompaniesResponse503
    | None
):
    r"""Get companies in an audience

     Gets the companies in an audience with pagination. Use the nextCursor from the response to fetch the
    next page. Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):
        page_size (int | Unset):  Default: 100.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAudienceCompaniesResponse200 | GetAudienceCompaniesResponse400 | GetAudienceCompaniesResponse401 | GetAudienceCompaniesResponse402 | GetAudienceCompaniesResponse403 | GetAudienceCompaniesResponse404 | GetAudienceCompaniesResponse429 | GetAudienceCompaniesResponse500 | GetAudienceCompaniesResponse503
    """

    return sync_detailed(
        audience_id=audience_id,
        client=client,
        api_key=api_key,
        page_size=page_size,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    page_size: int | Unset = 100,
    cursor: None | str | Unset = UNSET,
) -> Response[
    GetAudienceCompaniesResponse200
    | GetAudienceCompaniesResponse400
    | GetAudienceCompaniesResponse401
    | GetAudienceCompaniesResponse402
    | GetAudienceCompaniesResponse403
    | GetAudienceCompaniesResponse404
    | GetAudienceCompaniesResponse429
    | GetAudienceCompaniesResponse500
    | GetAudienceCompaniesResponse503
]:
    r"""Get companies in an audience

     Gets the companies in an audience with pagination. Use the nextCursor from the response to fetch the
    next page. Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):
        page_size (int | Unset):  Default: 100.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAudienceCompaniesResponse200 | GetAudienceCompaniesResponse400 | GetAudienceCompaniesResponse401 | GetAudienceCompaniesResponse402 | GetAudienceCompaniesResponse403 | GetAudienceCompaniesResponse404 | GetAudienceCompaniesResponse429 | GetAudienceCompaniesResponse500 | GetAudienceCompaniesResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        api_key=api_key,
        page_size=page_size,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    page_size: int | Unset = 100,
    cursor: None | str | Unset = UNSET,
) -> (
    GetAudienceCompaniesResponse200
    | GetAudienceCompaniesResponse400
    | GetAudienceCompaniesResponse401
    | GetAudienceCompaniesResponse402
    | GetAudienceCompaniesResponse403
    | GetAudienceCompaniesResponse404
    | GetAudienceCompaniesResponse429
    | GetAudienceCompaniesResponse500
    | GetAudienceCompaniesResponse503
    | None
):
    r"""Get companies in an audience

     Gets the companies in an audience with pagination. Use the nextCursor from the response to fetch the
    next page. Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):
        page_size (int | Unset):  Default: 100.
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAudienceCompaniesResponse200 | GetAudienceCompaniesResponse400 | GetAudienceCompaniesResponse401 | GetAudienceCompaniesResponse402 | GetAudienceCompaniesResponse403 | GetAudienceCompaniesResponse404 | GetAudienceCompaniesResponse429 | GetAudienceCompaniesResponse500 | GetAudienceCompaniesResponse503
    """

    return (
        await asyncio_detailed(
            audience_id=audience_id,
            client=client,
            api_key=api_key,
            page_size=page_size,
            cursor=cursor,
        )
    ).parsed
