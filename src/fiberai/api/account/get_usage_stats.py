from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_usage_stats_granularity import GetUsageStatsGranularity
from ...models.get_usage_stats_group_by import GetUsageStatsGroupBy
from ...models.get_usage_stats_response_200 import GetUsageStatsResponse200
from ...models.get_usage_stats_response_400 import GetUsageStatsResponse400
from ...models.get_usage_stats_response_401 import GetUsageStatsResponse401
from ...models.get_usage_stats_response_402 import GetUsageStatsResponse402
from ...models.get_usage_stats_response_403 import GetUsageStatsResponse403
from ...models.get_usage_stats_response_404 import GetUsageStatsResponse404
from ...models.get_usage_stats_response_422 import GetUsageStatsResponse422
from ...models.get_usage_stats_response_429 import GetUsageStatsResponse429
from ...models.get_usage_stats_response_500 import GetUsageStatsResponse500
from ...models.get_usage_stats_response_503 import GetUsageStatsResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    api_key: str,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    granularity: GetUsageStatsGranularity | Unset = GetUsageStatsGranularity.DAY,
    group_by: GetUsageStatsGroupBy | Unset = GetUsageStatsGroupBy.TOTAL,
    api_key_hash: None | str | Unset = UNSET,
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

    json_granularity: str | Unset = UNSET
    if not isinstance(granularity, Unset):
        json_granularity = granularity.value

    params["granularity"] = json_granularity

    json_group_by: str | Unset = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = group_by.value

    params["groupBy"] = json_group_by

    json_api_key_hash: None | str | Unset
    if isinstance(api_key_hash, Unset):
        json_api_key_hash = UNSET
    else:
        json_api_key_hash = api_key_hash
    params["apiKeyHash"] = json_api_key_hash

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage-stats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUsageStatsResponse200
    | GetUsageStatsResponse400
    | GetUsageStatsResponse401
    | GetUsageStatsResponse402
    | GetUsageStatsResponse403
    | GetUsageStatsResponse404
    | GetUsageStatsResponse422
    | GetUsageStatsResponse429
    | GetUsageStatsResponse500
    | GetUsageStatsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = GetUsageStatsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetUsageStatsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetUsageStatsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = GetUsageStatsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = GetUsageStatsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUsageStatsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = GetUsageStatsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = GetUsageStatsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetUsageStatsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetUsageStatsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUsageStatsResponse200
    | GetUsageStatsResponse400
    | GetUsageStatsResponse401
    | GetUsageStatsResponse402
    | GetUsageStatsResponse403
    | GetUsageStatsResponse404
    | GetUsageStatsResponse422
    | GetUsageStatsResponse429
    | GetUsageStatsResponse500
    | GetUsageStatsResponse503
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
    granularity: GetUsageStatsGranularity | Unset = GetUsageStatsGranularity.DAY,
    group_by: GetUsageStatsGroupBy | Unset = GetUsageStatsGroupBy.TOTAL,
    api_key_hash: None | str | Unset = UNSET,
) -> Response[
    GetUsageStatsResponse200
    | GetUsageStatsResponse400
    | GetUsageStatsResponse401
    | GetUsageStatsResponse402
    | GetUsageStatsResponse403
    | GetUsageStatsResponse404
    | GetUsageStatsResponse422
    | GetUsageStatsResponse429
    | GetUsageStatsResponse500
    | GetUsageStatsResponse503
]:
    """Get usage breakdown

     Returns your credit usage broken down into time buckets, in ascending order, with the credits
    charged, the credits refunded, and the number of API calls in each bucket. Split each bucket per API
    key with `groupBy`, or scope to one key with `apiKeyHash`. All timestamps and bucket boundaries are
    UTC.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        granularity (GetUsageStatsGranularity | Unset):  Default: GetUsageStatsGranularity.DAY.
        group_by (GetUsageStatsGroupBy | Unset):  Default: GetUsageStatsGroupBy.TOTAL.
        api_key_hash (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsageStatsResponse200 | GetUsageStatsResponse400 | GetUsageStatsResponse401 | GetUsageStatsResponse402 | GetUsageStatsResponse403 | GetUsageStatsResponse404 | GetUsageStatsResponse422 | GetUsageStatsResponse429 | GetUsageStatsResponse500 | GetUsageStatsResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        start_date=start_date,
        end_date=end_date,
        granularity=granularity,
        group_by=group_by,
        api_key_hash=api_key_hash,
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
    granularity: GetUsageStatsGranularity | Unset = GetUsageStatsGranularity.DAY,
    group_by: GetUsageStatsGroupBy | Unset = GetUsageStatsGroupBy.TOTAL,
    api_key_hash: None | str | Unset = UNSET,
) -> (
    GetUsageStatsResponse200
    | GetUsageStatsResponse400
    | GetUsageStatsResponse401
    | GetUsageStatsResponse402
    | GetUsageStatsResponse403
    | GetUsageStatsResponse404
    | GetUsageStatsResponse422
    | GetUsageStatsResponse429
    | GetUsageStatsResponse500
    | GetUsageStatsResponse503
    | None
):
    """Get usage breakdown

     Returns your credit usage broken down into time buckets, in ascending order, with the credits
    charged, the credits refunded, and the number of API calls in each bucket. Split each bucket per API
    key with `groupBy`, or scope to one key with `apiKeyHash`. All timestamps and bucket boundaries are
    UTC.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        granularity (GetUsageStatsGranularity | Unset):  Default: GetUsageStatsGranularity.DAY.
        group_by (GetUsageStatsGroupBy | Unset):  Default: GetUsageStatsGroupBy.TOTAL.
        api_key_hash (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsageStatsResponse200 | GetUsageStatsResponse400 | GetUsageStatsResponse401 | GetUsageStatsResponse402 | GetUsageStatsResponse403 | GetUsageStatsResponse404 | GetUsageStatsResponse422 | GetUsageStatsResponse429 | GetUsageStatsResponse500 | GetUsageStatsResponse503
    """

    return sync_detailed(
        client=client,
        api_key=api_key,
        start_date=start_date,
        end_date=end_date,
        granularity=granularity,
        group_by=group_by,
        api_key_hash=api_key_hash,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    granularity: GetUsageStatsGranularity | Unset = GetUsageStatsGranularity.DAY,
    group_by: GetUsageStatsGroupBy | Unset = GetUsageStatsGroupBy.TOTAL,
    api_key_hash: None | str | Unset = UNSET,
) -> Response[
    GetUsageStatsResponse200
    | GetUsageStatsResponse400
    | GetUsageStatsResponse401
    | GetUsageStatsResponse402
    | GetUsageStatsResponse403
    | GetUsageStatsResponse404
    | GetUsageStatsResponse422
    | GetUsageStatsResponse429
    | GetUsageStatsResponse500
    | GetUsageStatsResponse503
]:
    """Get usage breakdown

     Returns your credit usage broken down into time buckets, in ascending order, with the credits
    charged, the credits refunded, and the number of API calls in each bucket. Split each bucket per API
    key with `groupBy`, or scope to one key with `apiKeyHash`. All timestamps and bucket boundaries are
    UTC.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        granularity (GetUsageStatsGranularity | Unset):  Default: GetUsageStatsGranularity.DAY.
        group_by (GetUsageStatsGroupBy | Unset):  Default: GetUsageStatsGroupBy.TOTAL.
        api_key_hash (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsageStatsResponse200 | GetUsageStatsResponse400 | GetUsageStatsResponse401 | GetUsageStatsResponse402 | GetUsageStatsResponse403 | GetUsageStatsResponse404 | GetUsageStatsResponse422 | GetUsageStatsResponse429 | GetUsageStatsResponse500 | GetUsageStatsResponse503]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        start_date=start_date,
        end_date=end_date,
        granularity=granularity,
        group_by=group_by,
        api_key_hash=api_key_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    api_key: str,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    granularity: GetUsageStatsGranularity | Unset = GetUsageStatsGranularity.DAY,
    group_by: GetUsageStatsGroupBy | Unset = GetUsageStatsGroupBy.TOTAL,
    api_key_hash: None | str | Unset = UNSET,
) -> (
    GetUsageStatsResponse200
    | GetUsageStatsResponse400
    | GetUsageStatsResponse401
    | GetUsageStatsResponse402
    | GetUsageStatsResponse403
    | GetUsageStatsResponse404
    | GetUsageStatsResponse422
    | GetUsageStatsResponse429
    | GetUsageStatsResponse500
    | GetUsageStatsResponse503
    | None
):
    """Get usage breakdown

     Returns your credit usage broken down into time buckets, in ascending order, with the credits
    charged, the credits refunded, and the number of API calls in each bucket. Split each bucket per API
    key with `groupBy`, or scope to one key with `apiKeyHash`. All timestamps and bucket boundaries are
    UTC.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        api_key (str):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        granularity (GetUsageStatsGranularity | Unset):  Default: GetUsageStatsGranularity.DAY.
        group_by (GetUsageStatsGroupBy | Unset):  Default: GetUsageStatsGroupBy.TOTAL.
        api_key_hash (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsageStatsResponse200 | GetUsageStatsResponse400 | GetUsageStatsResponse401 | GetUsageStatsResponse402 | GetUsageStatsResponse403 | GetUsageStatsResponse404 | GetUsageStatsResponse422 | GetUsageStatsResponse429 | GetUsageStatsResponse500 | GetUsageStatsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
            start_date=start_date,
            end_date=end_date,
            granularity=granularity,
            group_by=group_by,
            api_key_hash=api_key_hash,
        )
    ).parsed
