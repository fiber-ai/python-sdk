from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.refresh_tracker_company_list_body import RefreshTrackerCompanyListBody
from ...models.refresh_tracker_company_list_response_200 import RefreshTrackerCompanyListResponse200
from ...models.refresh_tracker_company_list_response_400 import RefreshTrackerCompanyListResponse400
from ...models.refresh_tracker_company_list_response_401 import RefreshTrackerCompanyListResponse401
from ...models.refresh_tracker_company_list_response_402 import RefreshTrackerCompanyListResponse402
from ...models.refresh_tracker_company_list_response_403 import RefreshTrackerCompanyListResponse403
from ...models.refresh_tracker_company_list_response_404 import RefreshTrackerCompanyListResponse404
from ...models.refresh_tracker_company_list_response_422 import RefreshTrackerCompanyListResponse422
from ...models.refresh_tracker_company_list_response_429 import RefreshTrackerCompanyListResponse429
from ...models.refresh_tracker_company_list_response_500 import RefreshTrackerCompanyListResponse500
from ...models.refresh_tracker_company_list_response_503 import RefreshTrackerCompanyListResponse503
from ...types import Response


def _get_kwargs(
    list_id: str,
    *,
    body: RefreshTrackerCompanyListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tracker/company-lists/{list_id}/refresh".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RefreshTrackerCompanyListResponse200
    | RefreshTrackerCompanyListResponse400
    | RefreshTrackerCompanyListResponse401
    | RefreshTrackerCompanyListResponse402
    | RefreshTrackerCompanyListResponse403
    | RefreshTrackerCompanyListResponse404
    | RefreshTrackerCompanyListResponse422
    | RefreshTrackerCompanyListResponse429
    | RefreshTrackerCompanyListResponse500
    | RefreshTrackerCompanyListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RefreshTrackerCompanyListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RefreshTrackerCompanyListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RefreshTrackerCompanyListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RefreshTrackerCompanyListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RefreshTrackerCompanyListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RefreshTrackerCompanyListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = RefreshTrackerCompanyListResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = RefreshTrackerCompanyListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RefreshTrackerCompanyListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RefreshTrackerCompanyListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RefreshTrackerCompanyListResponse200
    | RefreshTrackerCompanyListResponse400
    | RefreshTrackerCompanyListResponse401
    | RefreshTrackerCompanyListResponse402
    | RefreshTrackerCompanyListResponse403
    | RefreshTrackerCompanyListResponse404
    | RefreshTrackerCompanyListResponse422
    | RefreshTrackerCompanyListResponse429
    | RefreshTrackerCompanyListResponse500
    | RefreshTrackerCompanyListResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RefreshTrackerCompanyListBody,
) -> Response[
    RefreshTrackerCompanyListResponse200
    | RefreshTrackerCompanyListResponse400
    | RefreshTrackerCompanyListResponse401
    | RefreshTrackerCompanyListResponse402
    | RefreshTrackerCompanyListResponse403
    | RefreshTrackerCompanyListResponse404
    | RefreshTrackerCompanyListResponse422
    | RefreshTrackerCompanyListResponse429
    | RefreshTrackerCompanyListResponse500
    | RefreshTrackerCompanyListResponse503
]:
    """Refresh company tracker list

     Initiate an immediate refresh of all tracked companies in this list. Each entity is checked for
    changes against its current monitoring rules. Credits are charged per entity processed.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits charged per entity processed (silver/gold tier based on org
    volume).&nbsp;<span title="Pricing shown is default pricing. Actual pricing may
    vary.">ⓘ</span></span>

    Args:
        list_id (str):
        body (RefreshTrackerCompanyListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshTrackerCompanyListResponse200 | RefreshTrackerCompanyListResponse400 | RefreshTrackerCompanyListResponse401 | RefreshTrackerCompanyListResponse402 | RefreshTrackerCompanyListResponse403 | RefreshTrackerCompanyListResponse404 | RefreshTrackerCompanyListResponse422 | RefreshTrackerCompanyListResponse429 | RefreshTrackerCompanyListResponse500 | RefreshTrackerCompanyListResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RefreshTrackerCompanyListBody,
) -> (
    RefreshTrackerCompanyListResponse200
    | RefreshTrackerCompanyListResponse400
    | RefreshTrackerCompanyListResponse401
    | RefreshTrackerCompanyListResponse402
    | RefreshTrackerCompanyListResponse403
    | RefreshTrackerCompanyListResponse404
    | RefreshTrackerCompanyListResponse422
    | RefreshTrackerCompanyListResponse429
    | RefreshTrackerCompanyListResponse500
    | RefreshTrackerCompanyListResponse503
    | None
):
    """Refresh company tracker list

     Initiate an immediate refresh of all tracked companies in this list. Each entity is checked for
    changes against its current monitoring rules. Credits are charged per entity processed.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits charged per entity processed (silver/gold tier based on org
    volume).&nbsp;<span title="Pricing shown is default pricing. Actual pricing may
    vary.">ⓘ</span></span>

    Args:
        list_id (str):
        body (RefreshTrackerCompanyListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshTrackerCompanyListResponse200 | RefreshTrackerCompanyListResponse400 | RefreshTrackerCompanyListResponse401 | RefreshTrackerCompanyListResponse402 | RefreshTrackerCompanyListResponse403 | RefreshTrackerCompanyListResponse404 | RefreshTrackerCompanyListResponse422 | RefreshTrackerCompanyListResponse429 | RefreshTrackerCompanyListResponse500 | RefreshTrackerCompanyListResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RefreshTrackerCompanyListBody,
) -> Response[
    RefreshTrackerCompanyListResponse200
    | RefreshTrackerCompanyListResponse400
    | RefreshTrackerCompanyListResponse401
    | RefreshTrackerCompanyListResponse402
    | RefreshTrackerCompanyListResponse403
    | RefreshTrackerCompanyListResponse404
    | RefreshTrackerCompanyListResponse422
    | RefreshTrackerCompanyListResponse429
    | RefreshTrackerCompanyListResponse500
    | RefreshTrackerCompanyListResponse503
]:
    """Refresh company tracker list

     Initiate an immediate refresh of all tracked companies in this list. Each entity is checked for
    changes against its current monitoring rules. Credits are charged per entity processed.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits charged per entity processed (silver/gold tier based on org
    volume).&nbsp;<span title="Pricing shown is default pricing. Actual pricing may
    vary.">ⓘ</span></span>

    Args:
        list_id (str):
        body (RefreshTrackerCompanyListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshTrackerCompanyListResponse200 | RefreshTrackerCompanyListResponse400 | RefreshTrackerCompanyListResponse401 | RefreshTrackerCompanyListResponse402 | RefreshTrackerCompanyListResponse403 | RefreshTrackerCompanyListResponse404 | RefreshTrackerCompanyListResponse422 | RefreshTrackerCompanyListResponse429 | RefreshTrackerCompanyListResponse500 | RefreshTrackerCompanyListResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RefreshTrackerCompanyListBody,
) -> (
    RefreshTrackerCompanyListResponse200
    | RefreshTrackerCompanyListResponse400
    | RefreshTrackerCompanyListResponse401
    | RefreshTrackerCompanyListResponse402
    | RefreshTrackerCompanyListResponse403
    | RefreshTrackerCompanyListResponse404
    | RefreshTrackerCompanyListResponse422
    | RefreshTrackerCompanyListResponse429
    | RefreshTrackerCompanyListResponse500
    | RefreshTrackerCompanyListResponse503
    | None
):
    """Refresh company tracker list

     Initiate an immediate refresh of all tracked companies in this list. Each entity is checked for
    changes against its current monitoring rules. Credits are charged per entity processed.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits charged per entity processed (silver/gold tier based on org
    volume).&nbsp;<span title="Pricing shown is default pricing. Actual pricing may
    vary.">ⓘ</span></span>

    Args:
        list_id (str):
        body (RefreshTrackerCompanyListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshTrackerCompanyListResponse200 | RefreshTrackerCompanyListResponse400 | RefreshTrackerCompanyListResponse401 | RefreshTrackerCompanyListResponse402 | RefreshTrackerCompanyListResponse403 | RefreshTrackerCompanyListResponse404 | RefreshTrackerCompanyListResponse422 | RefreshTrackerCompanyListResponse429 | RefreshTrackerCompanyListResponse500 | RefreshTrackerCompanyListResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
