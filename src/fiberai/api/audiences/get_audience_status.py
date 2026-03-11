from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_audience_status_response_200 import GetAudienceStatusResponse200
from ...models.get_audience_status_response_400 import GetAudienceStatusResponse400
from ...models.get_audience_status_response_401 import GetAudienceStatusResponse401
from ...models.get_audience_status_response_402 import GetAudienceStatusResponse402
from ...models.get_audience_status_response_403 import GetAudienceStatusResponse403
from ...models.get_audience_status_response_404 import GetAudienceStatusResponse404
from ...models.get_audience_status_response_429 import GetAudienceStatusResponse429
from ...models.get_audience_status_response_500 import GetAudienceStatusResponse500
from ...models.get_audience_status_response_503 import GetAudienceStatusResponse503
from ...types import UNSET, Response


def _get_kwargs(
    audience_id: str,
    *,
    api_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audiences/{audience_id}".format(
            audience_id=quote(str(audience_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetAudienceStatusResponse200
    | GetAudienceStatusResponse400
    | GetAudienceStatusResponse401
    | GetAudienceStatusResponse402
    | GetAudienceStatusResponse403
    | GetAudienceStatusResponse404
    | GetAudienceStatusResponse429
    | GetAudienceStatusResponse500
    | GetAudienceStatusResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetAudienceStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAudienceStatusResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAudienceStatusResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetAudienceStatusResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetAudienceStatusResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAudienceStatusResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetAudienceStatusResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetAudienceStatusResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetAudienceStatusResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetAudienceStatusResponse200
    | GetAudienceStatusResponse400
    | GetAudienceStatusResponse401
    | GetAudienceStatusResponse402
    | GetAudienceStatusResponse403
    | GetAudienceStatusResponse404
    | GetAudienceStatusResponse429
    | GetAudienceStatusResponse500
    | GetAudienceStatusResponse503
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
) -> Response[
    GetAudienceStatusResponse200
    | GetAudienceStatusResponse400
    | GetAudienceStatusResponse401
    | GetAudienceStatusResponse402
    | GetAudienceStatusResponse403
    | GetAudienceStatusResponse404
    | GetAudienceStatusResponse429
    | GetAudienceStatusResponse500
    | GetAudienceStatusResponse503
]:
    r"""Get audience status

     Gets the status and basic statistics of an audience. Use this to poll for build completion after
    triggering a build. Status values: DRAFT (waiting for configuration), BUILDING (search in progress),
    NORMAL (ready to use), FAILED (build failed). Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAudienceStatusResponse200 | GetAudienceStatusResponse400 | GetAudienceStatusResponse401 | GetAudienceStatusResponse402 | GetAudienceStatusResponse403 | GetAudienceStatusResponse404 | GetAudienceStatusResponse429 | GetAudienceStatusResponse500 | GetAudienceStatusResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        api_key=api_key,
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
) -> (
    GetAudienceStatusResponse200
    | GetAudienceStatusResponse400
    | GetAudienceStatusResponse401
    | GetAudienceStatusResponse402
    | GetAudienceStatusResponse403
    | GetAudienceStatusResponse404
    | GetAudienceStatusResponse429
    | GetAudienceStatusResponse500
    | GetAudienceStatusResponse503
    | None
):
    r"""Get audience status

     Gets the status and basic statistics of an audience. Use this to poll for build completion after
    triggering a build. Status values: DRAFT (waiting for configuration), BUILDING (search in progress),
    NORMAL (ready to use), FAILED (build failed). Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAudienceStatusResponse200 | GetAudienceStatusResponse400 | GetAudienceStatusResponse401 | GetAudienceStatusResponse402 | GetAudienceStatusResponse403 | GetAudienceStatusResponse404 | GetAudienceStatusResponse429 | GetAudienceStatusResponse500 | GetAudienceStatusResponse503
    """

    return sync_detailed(
        audience_id=audience_id,
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    GetAudienceStatusResponse200
    | GetAudienceStatusResponse400
    | GetAudienceStatusResponse401
    | GetAudienceStatusResponse402
    | GetAudienceStatusResponse403
    | GetAudienceStatusResponse404
    | GetAudienceStatusResponse429
    | GetAudienceStatusResponse500
    | GetAudienceStatusResponse503
]:
    r"""Get audience status

     Gets the status and basic statistics of an audience. Use this to poll for build completion after
    triggering a build. Status values: DRAFT (waiting for configuration), BUILDING (search in progress),
    NORMAL (ready to use), FAILED (build failed). Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAudienceStatusResponse200 | GetAudienceStatusResponse400 | GetAudienceStatusResponse401 | GetAudienceStatusResponse402 | GetAudienceStatusResponse403 | GetAudienceStatusResponse404 | GetAudienceStatusResponse429 | GetAudienceStatusResponse500 | GetAudienceStatusResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    GetAudienceStatusResponse200
    | GetAudienceStatusResponse400
    | GetAudienceStatusResponse401
    | GetAudienceStatusResponse402
    | GetAudienceStatusResponse403
    | GetAudienceStatusResponse404
    | GetAudienceStatusResponse429
    | GetAudienceStatusResponse500
    | GetAudienceStatusResponse503
    | None
):
    r"""Get audience status

     Gets the status and basic statistics of an audience. Use this to poll for build completion after
    triggering a build. Status values: DRAFT (waiting for configuration), BUILDING (search in progress),
    NORMAL (ready to use), FAILED (build failed). Pass your apiKey in the query string.

    <span>⚡ <strong>Rate limit:</strong> 100 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAudienceStatusResponse200 | GetAudienceStatusResponse400 | GetAudienceStatusResponse401 | GetAudienceStatusResponse402 | GetAudienceStatusResponse403 | GetAudienceStatusResponse404 | GetAudienceStatusResponse429 | GetAudienceStatusResponse500 | GetAudienceStatusResponse503
    """

    return (
        await asyncio_detailed(
            audience_id=audience_id,
            client=client,
            api_key=api_key,
        )
    ).parsed
