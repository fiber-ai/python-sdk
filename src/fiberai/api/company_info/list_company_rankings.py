from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_company_rankings_body import ListCompanyRankingsBody
from ...models.list_company_rankings_response_200 import ListCompanyRankingsResponse200
from ...models.list_company_rankings_response_400 import ListCompanyRankingsResponse400
from ...models.list_company_rankings_response_401 import ListCompanyRankingsResponse401
from ...models.list_company_rankings_response_402 import ListCompanyRankingsResponse402
from ...models.list_company_rankings_response_403 import ListCompanyRankingsResponse403
from ...models.list_company_rankings_response_404 import ListCompanyRankingsResponse404
from ...models.list_company_rankings_response_422 import ListCompanyRankingsResponse422
from ...models.list_company_rankings_response_429 import ListCompanyRankingsResponse429
from ...models.list_company_rankings_response_500 import ListCompanyRankingsResponse500
from ...models.list_company_rankings_response_503 import ListCompanyRankingsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ListCompanyRankingsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/company-rankings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListCompanyRankingsResponse200
    | ListCompanyRankingsResponse400
    | ListCompanyRankingsResponse401
    | ListCompanyRankingsResponse402
    | ListCompanyRankingsResponse403
    | ListCompanyRankingsResponse404
    | ListCompanyRankingsResponse422
    | ListCompanyRankingsResponse429
    | ListCompanyRankingsResponse500
    | ListCompanyRankingsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListCompanyRankingsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListCompanyRankingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListCompanyRankingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListCompanyRankingsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListCompanyRankingsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListCompanyRankingsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ListCompanyRankingsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ListCompanyRankingsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListCompanyRankingsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListCompanyRankingsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListCompanyRankingsResponse200
    | ListCompanyRankingsResponse400
    | ListCompanyRankingsResponse401
    | ListCompanyRankingsResponse402
    | ListCompanyRankingsResponse403
    | ListCompanyRankingsResponse404
    | ListCompanyRankingsResponse422
    | ListCompanyRankingsResponse429
    | ListCompanyRankingsResponse500
    | ListCompanyRankingsResponse503
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
    body: ListCompanyRankingsBody,
) -> Response[
    ListCompanyRankingsResponse200
    | ListCompanyRankingsResponse400
    | ListCompanyRankingsResponse401
    | ListCompanyRankingsResponse402
    | ListCompanyRankingsResponse403
    | ListCompanyRankingsResponse404
    | ListCompanyRankingsResponse422
    | ListCompanyRankingsResponse429
    | ListCompanyRankingsResponse500
    | ListCompanyRankingsResponse503
]:
    """Download a ranked company list

     Download a ranked company list edition (for example the most recent Fortune 500), including rank,
    domain, financials, and headcount for every company. Optionally restrict the download to an
    inclusive rank range.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company returned&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListCompanyRankingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCompanyRankingsResponse200 | ListCompanyRankingsResponse400 | ListCompanyRankingsResponse401 | ListCompanyRankingsResponse402 | ListCompanyRankingsResponse403 | ListCompanyRankingsResponse404 | ListCompanyRankingsResponse422 | ListCompanyRankingsResponse429 | ListCompanyRankingsResponse500 | ListCompanyRankingsResponse503]
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
    body: ListCompanyRankingsBody,
) -> (
    ListCompanyRankingsResponse200
    | ListCompanyRankingsResponse400
    | ListCompanyRankingsResponse401
    | ListCompanyRankingsResponse402
    | ListCompanyRankingsResponse403
    | ListCompanyRankingsResponse404
    | ListCompanyRankingsResponse422
    | ListCompanyRankingsResponse429
    | ListCompanyRankingsResponse500
    | ListCompanyRankingsResponse503
    | None
):
    """Download a ranked company list

     Download a ranked company list edition (for example the most recent Fortune 500), including rank,
    domain, financials, and headcount for every company. Optionally restrict the download to an
    inclusive rank range.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company returned&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListCompanyRankingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCompanyRankingsResponse200 | ListCompanyRankingsResponse400 | ListCompanyRankingsResponse401 | ListCompanyRankingsResponse402 | ListCompanyRankingsResponse403 | ListCompanyRankingsResponse404 | ListCompanyRankingsResponse422 | ListCompanyRankingsResponse429 | ListCompanyRankingsResponse500 | ListCompanyRankingsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListCompanyRankingsBody,
) -> Response[
    ListCompanyRankingsResponse200
    | ListCompanyRankingsResponse400
    | ListCompanyRankingsResponse401
    | ListCompanyRankingsResponse402
    | ListCompanyRankingsResponse403
    | ListCompanyRankingsResponse404
    | ListCompanyRankingsResponse422
    | ListCompanyRankingsResponse429
    | ListCompanyRankingsResponse500
    | ListCompanyRankingsResponse503
]:
    """Download a ranked company list

     Download a ranked company list edition (for example the most recent Fortune 500), including rank,
    domain, financials, and headcount for every company. Optionally restrict the download to an
    inclusive rank range.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company returned&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListCompanyRankingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCompanyRankingsResponse200 | ListCompanyRankingsResponse400 | ListCompanyRankingsResponse401 | ListCompanyRankingsResponse402 | ListCompanyRankingsResponse403 | ListCompanyRankingsResponse404 | ListCompanyRankingsResponse422 | ListCompanyRankingsResponse429 | ListCompanyRankingsResponse500 | ListCompanyRankingsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListCompanyRankingsBody,
) -> (
    ListCompanyRankingsResponse200
    | ListCompanyRankingsResponse400
    | ListCompanyRankingsResponse401
    | ListCompanyRankingsResponse402
    | ListCompanyRankingsResponse403
    | ListCompanyRankingsResponse404
    | ListCompanyRankingsResponse422
    | ListCompanyRankingsResponse429
    | ListCompanyRankingsResponse500
    | ListCompanyRankingsResponse503
    | None
):
    """Download a ranked company list

     Download a ranked company list edition (for example the most recent Fortune 500), including rank,
    domain, financials, and headcount for every company. Optionally restrict the download to an
    inclusive rank range.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company returned&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListCompanyRankingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCompanyRankingsResponse200 | ListCompanyRankingsResponse400 | ListCompanyRankingsResponse401 | ListCompanyRankingsResponse402 | ListCompanyRankingsResponse403 | ListCompanyRankingsResponse404 | ListCompanyRankingsResponse422 | ListCompanyRankingsResponse429 | ListCompanyRankingsResponse500 | ListCompanyRankingsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
