from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_tracker_companies_body import RemoveTrackerCompaniesBody
from ...models.remove_tracker_companies_response_200 import RemoveTrackerCompaniesResponse200
from ...models.remove_tracker_companies_response_400 import RemoveTrackerCompaniesResponse400
from ...models.remove_tracker_companies_response_401 import RemoveTrackerCompaniesResponse401
from ...models.remove_tracker_companies_response_402 import RemoveTrackerCompaniesResponse402
from ...models.remove_tracker_companies_response_403 import RemoveTrackerCompaniesResponse403
from ...models.remove_tracker_companies_response_404 import RemoveTrackerCompaniesResponse404
from ...models.remove_tracker_companies_response_422 import RemoveTrackerCompaniesResponse422
from ...models.remove_tracker_companies_response_429 import RemoveTrackerCompaniesResponse429
from ...models.remove_tracker_companies_response_500 import RemoveTrackerCompaniesResponse500
from ...models.remove_tracker_companies_response_503 import RemoveTrackerCompaniesResponse503
from ...types import UNSET, Response


def _get_kwargs(
    list_id: str,
    *,
    body: RemoveTrackerCompaniesBody,
    api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/tracker/company-lists/{list_id}/companies".format(
            list_id=quote(str(list_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RemoveTrackerCompaniesResponse200
    | RemoveTrackerCompaniesResponse400
    | RemoveTrackerCompaniesResponse401
    | RemoveTrackerCompaniesResponse402
    | RemoveTrackerCompaniesResponse403
    | RemoveTrackerCompaniesResponse404
    | RemoveTrackerCompaniesResponse422
    | RemoveTrackerCompaniesResponse429
    | RemoveTrackerCompaniesResponse500
    | RemoveTrackerCompaniesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RemoveTrackerCompaniesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RemoveTrackerCompaniesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RemoveTrackerCompaniesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RemoveTrackerCompaniesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RemoveTrackerCompaniesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveTrackerCompaniesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = RemoveTrackerCompaniesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = RemoveTrackerCompaniesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RemoveTrackerCompaniesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RemoveTrackerCompaniesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RemoveTrackerCompaniesResponse200
    | RemoveTrackerCompaniesResponse400
    | RemoveTrackerCompaniesResponse401
    | RemoveTrackerCompaniesResponse402
    | RemoveTrackerCompaniesResponse403
    | RemoveTrackerCompaniesResponse404
    | RemoveTrackerCompaniesResponse422
    | RemoveTrackerCompaniesResponse429
    | RemoveTrackerCompaniesResponse500
    | RemoveTrackerCompaniesResponse503
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
    body: RemoveTrackerCompaniesBody,
    api_key: str,
) -> Response[
    RemoveTrackerCompaniesResponse200
    | RemoveTrackerCompaniesResponse400
    | RemoveTrackerCompaniesResponse401
    | RemoveTrackerCompaniesResponse402
    | RemoveTrackerCompaniesResponse403
    | RemoveTrackerCompaniesResponse404
    | RemoveTrackerCompaniesResponse422
    | RemoveTrackerCompaniesResponse429
    | RemoveTrackerCompaniesResponse500
    | RemoveTrackerCompaniesResponse503
]:
    r"""Remove companies from tracker list

     Remove companies from a company tracker list. Deactivates them so they are no longer monitored, but
    preserves their signal history. Uses the same identifier format as add-companies.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        body (RemoveTrackerCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveTrackerCompaniesResponse200 | RemoveTrackerCompaniesResponse400 | RemoveTrackerCompaniesResponse401 | RemoveTrackerCompaniesResponse402 | RemoveTrackerCompaniesResponse403 | RemoveTrackerCompaniesResponse404 | RemoveTrackerCompaniesResponse422 | RemoveTrackerCompaniesResponse429 | RemoveTrackerCompaniesResponse500 | RemoveTrackerCompaniesResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
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
    body: RemoveTrackerCompaniesBody,
    api_key: str,
) -> (
    RemoveTrackerCompaniesResponse200
    | RemoveTrackerCompaniesResponse400
    | RemoveTrackerCompaniesResponse401
    | RemoveTrackerCompaniesResponse402
    | RemoveTrackerCompaniesResponse403
    | RemoveTrackerCompaniesResponse404
    | RemoveTrackerCompaniesResponse422
    | RemoveTrackerCompaniesResponse429
    | RemoveTrackerCompaniesResponse500
    | RemoveTrackerCompaniesResponse503
    | None
):
    r"""Remove companies from tracker list

     Remove companies from a company tracker list. Deactivates them so they are no longer monitored, but
    preserves their signal history. Uses the same identifier format as add-companies.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        body (RemoveTrackerCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveTrackerCompaniesResponse200 | RemoveTrackerCompaniesResponse400 | RemoveTrackerCompaniesResponse401 | RemoveTrackerCompaniesResponse402 | RemoveTrackerCompaniesResponse403 | RemoveTrackerCompaniesResponse404 | RemoveTrackerCompaniesResponse422 | RemoveTrackerCompaniesResponse429 | RemoveTrackerCompaniesResponse500 | RemoveTrackerCompaniesResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        body=body,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveTrackerCompaniesBody,
    api_key: str,
) -> Response[
    RemoveTrackerCompaniesResponse200
    | RemoveTrackerCompaniesResponse400
    | RemoveTrackerCompaniesResponse401
    | RemoveTrackerCompaniesResponse402
    | RemoveTrackerCompaniesResponse403
    | RemoveTrackerCompaniesResponse404
    | RemoveTrackerCompaniesResponse422
    | RemoveTrackerCompaniesResponse429
    | RemoveTrackerCompaniesResponse500
    | RemoveTrackerCompaniesResponse503
]:
    r"""Remove companies from tracker list

     Remove companies from a company tracker list. Deactivates them so they are no longer monitored, but
    preserves their signal history. Uses the same identifier format as add-companies.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        body (RemoveTrackerCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveTrackerCompaniesResponse200 | RemoveTrackerCompaniesResponse400 | RemoveTrackerCompaniesResponse401 | RemoveTrackerCompaniesResponse402 | RemoveTrackerCompaniesResponse403 | RemoveTrackerCompaniesResponse404 | RemoveTrackerCompaniesResponse422 | RemoveTrackerCompaniesResponse429 | RemoveTrackerCompaniesResponse500 | RemoveTrackerCompaniesResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveTrackerCompaniesBody,
    api_key: str,
) -> (
    RemoveTrackerCompaniesResponse200
    | RemoveTrackerCompaniesResponse400
    | RemoveTrackerCompaniesResponse401
    | RemoveTrackerCompaniesResponse402
    | RemoveTrackerCompaniesResponse403
    | RemoveTrackerCompaniesResponse404
    | RemoveTrackerCompaniesResponse422
    | RemoveTrackerCompaniesResponse429
    | RemoveTrackerCompaniesResponse500
    | RemoveTrackerCompaniesResponse503
    | None
):
    r"""Remove companies from tracker list

     Remove companies from a company tracker list. Deactivates them so they are no longer monitored, but
    preserves their signal history. Uses the same identifier format as add-companies.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        body (RemoveTrackerCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveTrackerCompaniesResponse200 | RemoveTrackerCompaniesResponse400 | RemoveTrackerCompaniesResponse401 | RemoveTrackerCompaniesResponse402 | RemoveTrackerCompaniesResponse403 | RemoveTrackerCompaniesResponse404 | RemoveTrackerCompaniesResponse422 | RemoveTrackerCompaniesResponse429 | RemoveTrackerCompaniesResponse500 | RemoveTrackerCompaniesResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
            api_key=api_key,
        )
    ).parsed
