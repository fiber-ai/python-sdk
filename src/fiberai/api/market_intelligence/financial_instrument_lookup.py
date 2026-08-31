from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.financial_instrument_lookup_body import FinancialInstrumentLookupBody
from ...models.financial_instrument_lookup_response_200 import FinancialInstrumentLookupResponse200
from ...models.financial_instrument_lookup_response_400 import FinancialInstrumentLookupResponse400
from ...models.financial_instrument_lookup_response_401 import FinancialInstrumentLookupResponse401
from ...models.financial_instrument_lookup_response_402 import FinancialInstrumentLookupResponse402
from ...models.financial_instrument_lookup_response_403 import FinancialInstrumentLookupResponse403
from ...models.financial_instrument_lookup_response_404 import FinancialInstrumentLookupResponse404
from ...models.financial_instrument_lookup_response_422 import FinancialInstrumentLookupResponse422
from ...models.financial_instrument_lookup_response_429 import FinancialInstrumentLookupResponse429
from ...models.financial_instrument_lookup_response_500 import FinancialInstrumentLookupResponse500
from ...models.financial_instrument_lookup_response_503 import FinancialInstrumentLookupResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FinancialInstrumentLookupBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/finance/instrument",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FinancialInstrumentLookupResponse200
    | FinancialInstrumentLookupResponse400
    | FinancialInstrumentLookupResponse401
    | FinancialInstrumentLookupResponse402
    | FinancialInstrumentLookupResponse403
    | FinancialInstrumentLookupResponse404
    | FinancialInstrumentLookupResponse422
    | FinancialInstrumentLookupResponse429
    | FinancialInstrumentLookupResponse500
    | FinancialInstrumentLookupResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FinancialInstrumentLookupResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FinancialInstrumentLookupResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FinancialInstrumentLookupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FinancialInstrumentLookupResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FinancialInstrumentLookupResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FinancialInstrumentLookupResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FinancialInstrumentLookupResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FinancialInstrumentLookupResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FinancialInstrumentLookupResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FinancialInstrumentLookupResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FinancialInstrumentLookupResponse200
    | FinancialInstrumentLookupResponse400
    | FinancialInstrumentLookupResponse401
    | FinancialInstrumentLookupResponse402
    | FinancialInstrumentLookupResponse403
    | FinancialInstrumentLookupResponse404
    | FinancialInstrumentLookupResponse422
    | FinancialInstrumentLookupResponse429
    | FinancialInstrumentLookupResponse500
    | FinancialInstrumentLookupResponse503
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
    body: FinancialInstrumentLookupBody,
) -> Response[
    FinancialInstrumentLookupResponse200
    | FinancialInstrumentLookupResponse400
    | FinancialInstrumentLookupResponse401
    | FinancialInstrumentLookupResponse402
    | FinancialInstrumentLookupResponse403
    | FinancialInstrumentLookupResponse404
    | FinancialInstrumentLookupResponse422
    | FinancialInstrumentLookupResponse429
    | FinancialInstrumentLookupResponse500
    | FinancialInstrumentLookupResponse503
]:
    """Look up a financial instrument

     Returns live market data for a stock, index, currency pair, or fund, including the headline quote,
    price movement, company facts, financial statements, related news, and a price history series.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per financial instrument lookup&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FinancialInstrumentLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinancialInstrumentLookupResponse200 | FinancialInstrumentLookupResponse400 | FinancialInstrumentLookupResponse401 | FinancialInstrumentLookupResponse402 | FinancialInstrumentLookupResponse403 | FinancialInstrumentLookupResponse404 | FinancialInstrumentLookupResponse422 | FinancialInstrumentLookupResponse429 | FinancialInstrumentLookupResponse500 | FinancialInstrumentLookupResponse503]
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
    body: FinancialInstrumentLookupBody,
) -> (
    FinancialInstrumentLookupResponse200
    | FinancialInstrumentLookupResponse400
    | FinancialInstrumentLookupResponse401
    | FinancialInstrumentLookupResponse402
    | FinancialInstrumentLookupResponse403
    | FinancialInstrumentLookupResponse404
    | FinancialInstrumentLookupResponse422
    | FinancialInstrumentLookupResponse429
    | FinancialInstrumentLookupResponse500
    | FinancialInstrumentLookupResponse503
    | None
):
    """Look up a financial instrument

     Returns live market data for a stock, index, currency pair, or fund, including the headline quote,
    price movement, company facts, financial statements, related news, and a price history series.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per financial instrument lookup&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FinancialInstrumentLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinancialInstrumentLookupResponse200 | FinancialInstrumentLookupResponse400 | FinancialInstrumentLookupResponse401 | FinancialInstrumentLookupResponse402 | FinancialInstrumentLookupResponse403 | FinancialInstrumentLookupResponse404 | FinancialInstrumentLookupResponse422 | FinancialInstrumentLookupResponse429 | FinancialInstrumentLookupResponse500 | FinancialInstrumentLookupResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinancialInstrumentLookupBody,
) -> Response[
    FinancialInstrumentLookupResponse200
    | FinancialInstrumentLookupResponse400
    | FinancialInstrumentLookupResponse401
    | FinancialInstrumentLookupResponse402
    | FinancialInstrumentLookupResponse403
    | FinancialInstrumentLookupResponse404
    | FinancialInstrumentLookupResponse422
    | FinancialInstrumentLookupResponse429
    | FinancialInstrumentLookupResponse500
    | FinancialInstrumentLookupResponse503
]:
    """Look up a financial instrument

     Returns live market data for a stock, index, currency pair, or fund, including the headline quote,
    price movement, company facts, financial statements, related news, and a price history series.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per financial instrument lookup&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FinancialInstrumentLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinancialInstrumentLookupResponse200 | FinancialInstrumentLookupResponse400 | FinancialInstrumentLookupResponse401 | FinancialInstrumentLookupResponse402 | FinancialInstrumentLookupResponse403 | FinancialInstrumentLookupResponse404 | FinancialInstrumentLookupResponse422 | FinancialInstrumentLookupResponse429 | FinancialInstrumentLookupResponse500 | FinancialInstrumentLookupResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FinancialInstrumentLookupBody,
) -> (
    FinancialInstrumentLookupResponse200
    | FinancialInstrumentLookupResponse400
    | FinancialInstrumentLookupResponse401
    | FinancialInstrumentLookupResponse402
    | FinancialInstrumentLookupResponse403
    | FinancialInstrumentLookupResponse404
    | FinancialInstrumentLookupResponse422
    | FinancialInstrumentLookupResponse429
    | FinancialInstrumentLookupResponse500
    | FinancialInstrumentLookupResponse503
    | None
):
    """Look up a financial instrument

     Returns live market data for a stock, index, currency pair, or fund, including the headline quote,
    price movement, company facts, financial statements, related news, and a price history series.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per financial instrument lookup&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FinancialInstrumentLookupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinancialInstrumentLookupResponse200 | FinancialInstrumentLookupResponse400 | FinancialInstrumentLookupResponse401 | FinancialInstrumentLookupResponse402 | FinancialInstrumentLookupResponse403 | FinancialInstrumentLookupResponse404 | FinancialInstrumentLookupResponse422 | FinancialInstrumentLookupResponse429 | FinancialInstrumentLookupResponse500 | FinancialInstrumentLookupResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
