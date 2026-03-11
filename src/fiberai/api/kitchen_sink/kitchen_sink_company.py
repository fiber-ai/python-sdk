from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.kitchen_sink_company_body import KitchenSinkCompanyBody
from ...models.kitchen_sink_company_response_200 import KitchenSinkCompanyResponse200
from ...models.kitchen_sink_company_response_400 import KitchenSinkCompanyResponse400
from ...models.kitchen_sink_company_response_401 import KitchenSinkCompanyResponse401
from ...models.kitchen_sink_company_response_402 import KitchenSinkCompanyResponse402
from ...models.kitchen_sink_company_response_403 import KitchenSinkCompanyResponse403
from ...models.kitchen_sink_company_response_404 import KitchenSinkCompanyResponse404
from ...models.kitchen_sink_company_response_429 import KitchenSinkCompanyResponse429
from ...models.kitchen_sink_company_response_500 import KitchenSinkCompanyResponse500
from ...models.kitchen_sink_company_response_503 import KitchenSinkCompanyResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: KitchenSinkCompanyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/kitchen-sink/company",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    KitchenSinkCompanyResponse200
    | KitchenSinkCompanyResponse400
    | KitchenSinkCompanyResponse401
    | KitchenSinkCompanyResponse402
    | KitchenSinkCompanyResponse403
    | KitchenSinkCompanyResponse404
    | KitchenSinkCompanyResponse429
    | KitchenSinkCompanyResponse500
    | KitchenSinkCompanyResponse503
    | None
):
    if response.status_code == 200:
        response_200 = KitchenSinkCompanyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = KitchenSinkCompanyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = KitchenSinkCompanyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = KitchenSinkCompanyResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = KitchenSinkCompanyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = KitchenSinkCompanyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = KitchenSinkCompanyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = KitchenSinkCompanyResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = KitchenSinkCompanyResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    KitchenSinkCompanyResponse200
    | KitchenSinkCompanyResponse400
    | KitchenSinkCompanyResponse401
    | KitchenSinkCompanyResponse402
    | KitchenSinkCompanyResponse403
    | KitchenSinkCompanyResponse404
    | KitchenSinkCompanyResponse429
    | KitchenSinkCompanyResponse500
    | KitchenSinkCompanyResponse503
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
    body: KitchenSinkCompanyBody,
) -> Response[
    KitchenSinkCompanyResponse200
    | KitchenSinkCompanyResponse400
    | KitchenSinkCompanyResponse401
    | KitchenSinkCompanyResponse402
    | KitchenSinkCompanyResponse403
    | KitchenSinkCompanyResponse404
    | KitchenSinkCompanyResponse429
    | KitchenSinkCompanyResponse500
    | KitchenSinkCompanyResponse503
]:
    r"""Kitchen sink company lookup

     Search for a company using a variety of parameters such as LinkedIn slug, LinkedIn URL, name, etc.
    Returns complete company data if found.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (KitchenSinkCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KitchenSinkCompanyResponse200 | KitchenSinkCompanyResponse400 | KitchenSinkCompanyResponse401 | KitchenSinkCompanyResponse402 | KitchenSinkCompanyResponse403 | KitchenSinkCompanyResponse404 | KitchenSinkCompanyResponse429 | KitchenSinkCompanyResponse500 | KitchenSinkCompanyResponse503]
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
    body: KitchenSinkCompanyBody,
) -> (
    KitchenSinkCompanyResponse200
    | KitchenSinkCompanyResponse400
    | KitchenSinkCompanyResponse401
    | KitchenSinkCompanyResponse402
    | KitchenSinkCompanyResponse403
    | KitchenSinkCompanyResponse404
    | KitchenSinkCompanyResponse429
    | KitchenSinkCompanyResponse500
    | KitchenSinkCompanyResponse503
    | None
):
    r"""Kitchen sink company lookup

     Search for a company using a variety of parameters such as LinkedIn slug, LinkedIn URL, name, etc.
    Returns complete company data if found.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (KitchenSinkCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KitchenSinkCompanyResponse200 | KitchenSinkCompanyResponse400 | KitchenSinkCompanyResponse401 | KitchenSinkCompanyResponse402 | KitchenSinkCompanyResponse403 | KitchenSinkCompanyResponse404 | KitchenSinkCompanyResponse429 | KitchenSinkCompanyResponse500 | KitchenSinkCompanyResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KitchenSinkCompanyBody,
) -> Response[
    KitchenSinkCompanyResponse200
    | KitchenSinkCompanyResponse400
    | KitchenSinkCompanyResponse401
    | KitchenSinkCompanyResponse402
    | KitchenSinkCompanyResponse403
    | KitchenSinkCompanyResponse404
    | KitchenSinkCompanyResponse429
    | KitchenSinkCompanyResponse500
    | KitchenSinkCompanyResponse503
]:
    r"""Kitchen sink company lookup

     Search for a company using a variety of parameters such as LinkedIn slug, LinkedIn URL, name, etc.
    Returns complete company data if found.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (KitchenSinkCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KitchenSinkCompanyResponse200 | KitchenSinkCompanyResponse400 | KitchenSinkCompanyResponse401 | KitchenSinkCompanyResponse402 | KitchenSinkCompanyResponse403 | KitchenSinkCompanyResponse404 | KitchenSinkCompanyResponse429 | KitchenSinkCompanyResponse500 | KitchenSinkCompanyResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: KitchenSinkCompanyBody,
) -> (
    KitchenSinkCompanyResponse200
    | KitchenSinkCompanyResponse400
    | KitchenSinkCompanyResponse401
    | KitchenSinkCompanyResponse402
    | KitchenSinkCompanyResponse403
    | KitchenSinkCompanyResponse404
    | KitchenSinkCompanyResponse429
    | KitchenSinkCompanyResponse500
    | KitchenSinkCompanyResponse503
    | None
):
    r"""Kitchen sink company lookup

     Search for a company using a variety of parameters such as LinkedIn slug, LinkedIn URL, name, etc.
    Returns complete company data if found.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per company lookup&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (KitchenSinkCompanyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KitchenSinkCompanyResponse200 | KitchenSinkCompanyResponse400 | KitchenSinkCompanyResponse401 | KitchenSinkCompanyResponse402 | KitchenSinkCompanyResponse403 | KitchenSinkCompanyResponse404 | KitchenSinkCompanyResponse429 | KitchenSinkCompanyResponse500 | KitchenSinkCompanyResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
