from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_journeyman_list_body import GetJourneymanListBody
from ...models.get_journeyman_list_response_200 import GetJourneymanListResponse200
from ...models.get_journeyman_list_response_400 import GetJourneymanListResponse400
from ...models.get_journeyman_list_response_401 import GetJourneymanListResponse401
from ...models.get_journeyman_list_response_402 import GetJourneymanListResponse402
from ...models.get_journeyman_list_response_403 import GetJourneymanListResponse403
from ...models.get_journeyman_list_response_404 import GetJourneymanListResponse404
from ...models.get_journeyman_list_response_429 import GetJourneymanListResponse429
from ...models.get_journeyman_list_response_500 import GetJourneymanListResponse500
from ...models.get_journeyman_list_response_503 import GetJourneymanListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: GetJourneymanListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job-changes/get-list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetJourneymanListResponse200
    | GetJourneymanListResponse400
    | GetJourneymanListResponse401
    | GetJourneymanListResponse402
    | GetJourneymanListResponse403
    | GetJourneymanListResponse404
    | GetJourneymanListResponse429
    | GetJourneymanListResponse500
    | GetJourneymanListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetJourneymanListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetJourneymanListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetJourneymanListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetJourneymanListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetJourneymanListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetJourneymanListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetJourneymanListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetJourneymanListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetJourneymanListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetJourneymanListResponse200
    | GetJourneymanListResponse400
    | GetJourneymanListResponse401
    | GetJourneymanListResponse402
    | GetJourneymanListResponse403
    | GetJourneymanListResponse404
    | GetJourneymanListResponse429
    | GetJourneymanListResponse500
    | GetJourneymanListResponse503
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
    body: GetJourneymanListBody,
) -> Response[
    GetJourneymanListResponse200
    | GetJourneymanListResponse400
    | GetJourneymanListResponse401
    | GetJourneymanListResponse402
    | GetJourneymanListResponse403
    | GetJourneymanListResponse404
    | GetJourneymanListResponse429
    | GetJourneymanListResponse500
    | GetJourneymanListResponse503
]:
    r"""Get a job changes list

     Get a job changes list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetJourneymanListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJourneymanListResponse200 | GetJourneymanListResponse400 | GetJourneymanListResponse401 | GetJourneymanListResponse402 | GetJourneymanListResponse403 | GetJourneymanListResponse404 | GetJourneymanListResponse429 | GetJourneymanListResponse500 | GetJourneymanListResponse503]
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
    body: GetJourneymanListBody,
) -> (
    GetJourneymanListResponse200
    | GetJourneymanListResponse400
    | GetJourneymanListResponse401
    | GetJourneymanListResponse402
    | GetJourneymanListResponse403
    | GetJourneymanListResponse404
    | GetJourneymanListResponse429
    | GetJourneymanListResponse500
    | GetJourneymanListResponse503
    | None
):
    r"""Get a job changes list

     Get a job changes list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetJourneymanListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJourneymanListResponse200 | GetJourneymanListResponse400 | GetJourneymanListResponse401 | GetJourneymanListResponse402 | GetJourneymanListResponse403 | GetJourneymanListResponse404 | GetJourneymanListResponse429 | GetJourneymanListResponse500 | GetJourneymanListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetJourneymanListBody,
) -> Response[
    GetJourneymanListResponse200
    | GetJourneymanListResponse400
    | GetJourneymanListResponse401
    | GetJourneymanListResponse402
    | GetJourneymanListResponse403
    | GetJourneymanListResponse404
    | GetJourneymanListResponse429
    | GetJourneymanListResponse500
    | GetJourneymanListResponse503
]:
    r"""Get a job changes list

     Get a job changes list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetJourneymanListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJourneymanListResponse200 | GetJourneymanListResponse400 | GetJourneymanListResponse401 | GetJourneymanListResponse402 | GetJourneymanListResponse403 | GetJourneymanListResponse404 | GetJourneymanListResponse429 | GetJourneymanListResponse500 | GetJourneymanListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetJourneymanListBody,
) -> (
    GetJourneymanListResponse200
    | GetJourneymanListResponse400
    | GetJourneymanListResponse401
    | GetJourneymanListResponse402
    | GetJourneymanListResponse403
    | GetJourneymanListResponse404
    | GetJourneymanListResponse429
    | GetJourneymanListResponse500
    | GetJourneymanListResponse503
    | None
):
    r"""Get a job changes list

     Get a job changes list.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (GetJourneymanListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJourneymanListResponse200 | GetJourneymanListResponse400 | GetJourneymanListResponse401 | GetJourneymanListResponse402 | GetJourneymanListResponse403 | GetJourneymanListResponse404 | GetJourneymanListResponse429 | GetJourneymanListResponse500 | GetJourneymanListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
