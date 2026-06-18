from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_tracker_company_list_response_200 import DeleteTrackerCompanyListResponse200
from ...models.delete_tracker_company_list_response_400 import DeleteTrackerCompanyListResponse400
from ...models.delete_tracker_company_list_response_401 import DeleteTrackerCompanyListResponse401
from ...models.delete_tracker_company_list_response_402 import DeleteTrackerCompanyListResponse402
from ...models.delete_tracker_company_list_response_403 import DeleteTrackerCompanyListResponse403
from ...models.delete_tracker_company_list_response_404 import DeleteTrackerCompanyListResponse404
from ...models.delete_tracker_company_list_response_422 import DeleteTrackerCompanyListResponse422
from ...models.delete_tracker_company_list_response_429 import DeleteTrackerCompanyListResponse429
from ...models.delete_tracker_company_list_response_500 import DeleteTrackerCompanyListResponse500
from ...models.delete_tracker_company_list_response_503 import DeleteTrackerCompanyListResponse503
from ...types import UNSET, Response


def _get_kwargs(
    list_id: str,
    *,
    api_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/tracker/company-lists/{list_id}".format(
            list_id=quote(str(list_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteTrackerCompanyListResponse200
    | DeleteTrackerCompanyListResponse400
    | DeleteTrackerCompanyListResponse401
    | DeleteTrackerCompanyListResponse402
    | DeleteTrackerCompanyListResponse403
    | DeleteTrackerCompanyListResponse404
    | DeleteTrackerCompanyListResponse422
    | DeleteTrackerCompanyListResponse429
    | DeleteTrackerCompanyListResponse500
    | DeleteTrackerCompanyListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = DeleteTrackerCompanyListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteTrackerCompanyListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteTrackerCompanyListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = DeleteTrackerCompanyListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = DeleteTrackerCompanyListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteTrackerCompanyListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = DeleteTrackerCompanyListResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = DeleteTrackerCompanyListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteTrackerCompanyListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteTrackerCompanyListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteTrackerCompanyListResponse200
    | DeleteTrackerCompanyListResponse400
    | DeleteTrackerCompanyListResponse401
    | DeleteTrackerCompanyListResponse402
    | DeleteTrackerCompanyListResponse403
    | DeleteTrackerCompanyListResponse404
    | DeleteTrackerCompanyListResponse422
    | DeleteTrackerCompanyListResponse429
    | DeleteTrackerCompanyListResponse500
    | DeleteTrackerCompanyListResponse503
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
    api_key: str,
) -> Response[
    DeleteTrackerCompanyListResponse200
    | DeleteTrackerCompanyListResponse400
    | DeleteTrackerCompanyListResponse401
    | DeleteTrackerCompanyListResponse402
    | DeleteTrackerCompanyListResponse403
    | DeleteTrackerCompanyListResponse404
    | DeleteTrackerCompanyListResponse422
    | DeleteTrackerCompanyListResponse429
    | DeleteTrackerCompanyListResponse500
    | DeleteTrackerCompanyListResponse503
]:
    r"""Archive company tracker list

     Archive a company tracker list. Stops all monitoring and deactivates all tracked companies and rules
    on the list. Signal history is preserved for audit purposes.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTrackerCompanyListResponse200 | DeleteTrackerCompanyListResponse400 | DeleteTrackerCompanyListResponse401 | DeleteTrackerCompanyListResponse402 | DeleteTrackerCompanyListResponse403 | DeleteTrackerCompanyListResponse404 | DeleteTrackerCompanyListResponse422 | DeleteTrackerCompanyListResponse429 | DeleteTrackerCompanyListResponse500 | DeleteTrackerCompanyListResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    DeleteTrackerCompanyListResponse200
    | DeleteTrackerCompanyListResponse400
    | DeleteTrackerCompanyListResponse401
    | DeleteTrackerCompanyListResponse402
    | DeleteTrackerCompanyListResponse403
    | DeleteTrackerCompanyListResponse404
    | DeleteTrackerCompanyListResponse422
    | DeleteTrackerCompanyListResponse429
    | DeleteTrackerCompanyListResponse500
    | DeleteTrackerCompanyListResponse503
    | None
):
    r"""Archive company tracker list

     Archive a company tracker list. Stops all monitoring and deactivates all tracked companies and rules
    on the list. Signal history is preserved for audit purposes.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTrackerCompanyListResponse200 | DeleteTrackerCompanyListResponse400 | DeleteTrackerCompanyListResponse401 | DeleteTrackerCompanyListResponse402 | DeleteTrackerCompanyListResponse403 | DeleteTrackerCompanyListResponse404 | DeleteTrackerCompanyListResponse422 | DeleteTrackerCompanyListResponse429 | DeleteTrackerCompanyListResponse500 | DeleteTrackerCompanyListResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> Response[
    DeleteTrackerCompanyListResponse200
    | DeleteTrackerCompanyListResponse400
    | DeleteTrackerCompanyListResponse401
    | DeleteTrackerCompanyListResponse402
    | DeleteTrackerCompanyListResponse403
    | DeleteTrackerCompanyListResponse404
    | DeleteTrackerCompanyListResponse422
    | DeleteTrackerCompanyListResponse429
    | DeleteTrackerCompanyListResponse500
    | DeleteTrackerCompanyListResponse503
]:
    r"""Archive company tracker list

     Archive a company tracker list. Stops all monitoring and deactivates all tracked companies and rules
    on the list. Signal history is preserved for audit purposes.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTrackerCompanyListResponse200 | DeleteTrackerCompanyListResponse400 | DeleteTrackerCompanyListResponse401 | DeleteTrackerCompanyListResponse402 | DeleteTrackerCompanyListResponse403 | DeleteTrackerCompanyListResponse404 | DeleteTrackerCompanyListResponse422 | DeleteTrackerCompanyListResponse429 | DeleteTrackerCompanyListResponse500 | DeleteTrackerCompanyListResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
) -> (
    DeleteTrackerCompanyListResponse200
    | DeleteTrackerCompanyListResponse400
    | DeleteTrackerCompanyListResponse401
    | DeleteTrackerCompanyListResponse402
    | DeleteTrackerCompanyListResponse403
    | DeleteTrackerCompanyListResponse404
    | DeleteTrackerCompanyListResponse422
    | DeleteTrackerCompanyListResponse429
    | DeleteTrackerCompanyListResponse500
    | DeleteTrackerCompanyListResponse503
    | None
):
    r"""Archive company tracker list

     Archive a company tracker list. Stops all monitoring and deactivates all tracked companies and rules
    on the list. Signal history is preserved for audit purposes.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTrackerCompanyListResponse200 | DeleteTrackerCompanyListResponse400 | DeleteTrackerCompanyListResponse401 | DeleteTrackerCompanyListResponse402 | DeleteTrackerCompanyListResponse403 | DeleteTrackerCompanyListResponse404 | DeleteTrackerCompanyListResponse422 | DeleteTrackerCompanyListResponse429 | DeleteTrackerCompanyListResponse500 | DeleteTrackerCompanyListResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            api_key=api_key,
        )
    ).parsed
