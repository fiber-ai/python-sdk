from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_billing_history_response_200 import GetBillingHistoryResponse200
from ...models.get_billing_history_response_400 import GetBillingHistoryResponse400
from ...models.get_billing_history_response_401 import GetBillingHistoryResponse401
from ...models.get_billing_history_response_402 import GetBillingHistoryResponse402
from ...models.get_billing_history_response_403 import GetBillingHistoryResponse403
from ...models.get_billing_history_response_404 import GetBillingHistoryResponse404
from ...models.get_billing_history_response_422 import GetBillingHistoryResponse422
from ...models.get_billing_history_response_429 import GetBillingHistoryResponse429
from ...models.get_billing_history_response_500 import GetBillingHistoryResponse500
from ...models.get_billing_history_response_503 import GetBillingHistoryResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    api_key: str,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["startDate"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["endDate"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing-history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetBillingHistoryResponse200
    | GetBillingHistoryResponse400
    | GetBillingHistoryResponse401
    | GetBillingHistoryResponse402
    | GetBillingHistoryResponse403
    | GetBillingHistoryResponse404
    | GetBillingHistoryResponse422
    | GetBillingHistoryResponse429
    | GetBillingHistoryResponse500
    | GetBillingHistoryResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetBillingHistoryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetBillingHistoryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetBillingHistoryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetBillingHistoryResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetBillingHistoryResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetBillingHistoryResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetBillingHistoryResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetBillingHistoryResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetBillingHistoryResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetBillingHistoryResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetBillingHistoryResponse200
    | GetBillingHistoryResponse400
    | GetBillingHistoryResponse401
    | GetBillingHistoryResponse402
    | GetBillingHistoryResponse403
    | GetBillingHistoryResponse404
    | GetBillingHistoryResponse422
    | GetBillingHistoryResponse429
    | GetBillingHistoryResponse500
    | GetBillingHistoryResponse503
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
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> Response[
    GetBillingHistoryResponse200
    | GetBillingHistoryResponse400
    | GetBillingHistoryResponse401
    | GetBillingHistoryResponse402
    | GetBillingHistoryResponse403
    | GetBillingHistoryResponse404
    | GetBillingHistoryResponse422
    | GetBillingHistoryResponse429
    | GetBillingHistoryResponse500
    | GetBillingHistoryResponse503
]:
    """Get purchase history

     Returns your purchase history — top-ups, auto top-ups, and subscription billing cycles — newest
    first. Each entry reports whether the purchase succeeded: completed entries include the credits
    added, the amount paid where available, and the payment IDs so you can reconcile against your own
    billing records; failed entries include the amount they attempted to charge and the failure reason.
    Use the optional date range to bound long histories; ranges are capped at two years per call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):
        start_date (None | str | Unset):
        end_date (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingHistoryResponse200 | GetBillingHistoryResponse400 | GetBillingHistoryResponse401 | GetBillingHistoryResponse402 | GetBillingHistoryResponse403 | GetBillingHistoryResponse404 | GetBillingHistoryResponse422 | GetBillingHistoryResponse429 | GetBillingHistoryResponse500 | GetBillingHistoryResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> (
    GetBillingHistoryResponse200
    | GetBillingHistoryResponse400
    | GetBillingHistoryResponse401
    | GetBillingHistoryResponse402
    | GetBillingHistoryResponse403
    | GetBillingHistoryResponse404
    | GetBillingHistoryResponse422
    | GetBillingHistoryResponse429
    | GetBillingHistoryResponse500
    | GetBillingHistoryResponse503
    | None
):
    """Get purchase history

     Returns your purchase history — top-ups, auto top-ups, and subscription billing cycles — newest
    first. Each entry reports whether the purchase succeeded: completed entries include the credits
    added, the amount paid where available, and the payment IDs so you can reconcile against your own
    billing records; failed entries include the amount they attempted to charge and the failure reason.
    Use the optional date range to bound long histories; ranges are capped at two years per call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):
        start_date (None | str | Unset):
        end_date (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingHistoryResponse200 | GetBillingHistoryResponse400 | GetBillingHistoryResponse401 | GetBillingHistoryResponse402 | GetBillingHistoryResponse403 | GetBillingHistoryResponse404 | GetBillingHistoryResponse422 | GetBillingHistoryResponse429 | GetBillingHistoryResponse500 | GetBillingHistoryResponse503
    """

    return sync_detailed(
        client=client,
        api_key=api_key,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> Response[
    GetBillingHistoryResponse200
    | GetBillingHistoryResponse400
    | GetBillingHistoryResponse401
    | GetBillingHistoryResponse402
    | GetBillingHistoryResponse403
    | GetBillingHistoryResponse404
    | GetBillingHistoryResponse422
    | GetBillingHistoryResponse429
    | GetBillingHistoryResponse500
    | GetBillingHistoryResponse503
]:
    """Get purchase history

     Returns your purchase history — top-ups, auto top-ups, and subscription billing cycles — newest
    first. Each entry reports whether the purchase succeeded: completed entries include the credits
    added, the amount paid where available, and the payment IDs so you can reconcile against your own
    billing records; failed entries include the amount they attempted to charge and the failure reason.
    Use the optional date range to bound long histories; ranges are capped at two years per call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):
        start_date (None | str | Unset):
        end_date (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingHistoryResponse200 | GetBillingHistoryResponse400 | GetBillingHistoryResponse401 | GetBillingHistoryResponse402 | GetBillingHistoryResponse403 | GetBillingHistoryResponse404 | GetBillingHistoryResponse422 | GetBillingHistoryResponse429 | GetBillingHistoryResponse500 | GetBillingHistoryResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> (
    GetBillingHistoryResponse200
    | GetBillingHistoryResponse400
    | GetBillingHistoryResponse401
    | GetBillingHistoryResponse402
    | GetBillingHistoryResponse403
    | GetBillingHistoryResponse404
    | GetBillingHistoryResponse422
    | GetBillingHistoryResponse429
    | GetBillingHistoryResponse500
    | GetBillingHistoryResponse503
    | None
):
    """Get purchase history

     Returns your purchase history — top-ups, auto top-ups, and subscription billing cycles — newest
    first. Each entry reports whether the purchase succeeded: completed entries include the credits
    added, the amount paid where available, and the payment IDs so you can reconcile against your own
    billing records; failed entries include the amount they attempted to charge and the failure reason.
    Use the optional date range to bound long histories; ranges are capped at two years per call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):
        start_date (None | str | Unset):
        end_date (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingHistoryResponse200 | GetBillingHistoryResponse400 | GetBillingHistoryResponse401 | GetBillingHistoryResponse402 | GetBillingHistoryResponse403 | GetBillingHistoryResponse404 | GetBillingHistoryResponse422 | GetBillingHistoryResponse429 | GetBillingHistoryResponse500 | GetBillingHistoryResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
