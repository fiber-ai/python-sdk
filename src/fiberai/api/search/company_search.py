from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_search_body import CompanySearchBody
from ...models.company_search_response_200 import CompanySearchResponse200
from ...models.company_search_response_400 import CompanySearchResponse400
from ...models.company_search_response_401 import CompanySearchResponse401
from ...models.company_search_response_402 import CompanySearchResponse402
from ...models.company_search_response_403 import CompanySearchResponse403
from ...models.company_search_response_404 import CompanySearchResponse404
from ...models.company_search_response_429 import CompanySearchResponse429
from ...models.company_search_response_500 import CompanySearchResponse500
from ...models.company_search_response_503 import CompanySearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CompanySearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/company-search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CompanySearchResponse200
    | CompanySearchResponse400
    | CompanySearchResponse401
    | CompanySearchResponse402
    | CompanySearchResponse403
    | CompanySearchResponse404
    | CompanySearchResponse429
    | CompanySearchResponse500
    | CompanySearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CompanySearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CompanySearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CompanySearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CompanySearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CompanySearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CompanySearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CompanySearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CompanySearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CompanySearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CompanySearchResponse200
    | CompanySearchResponse400
    | CompanySearchResponse401
    | CompanySearchResponse402
    | CompanySearchResponse403
    | CompanySearchResponse404
    | CompanySearchResponse429
    | CompanySearchResponse500
    | CompanySearchResponse503
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
    body: CompanySearchBody,
) -> Response[
    CompanySearchResponse200
    | CompanySearchResponse400
    | CompanySearchResponse401
    | CompanySearchResponse402
    | CompanySearchResponse403
    | CompanySearchResponse404
    | CompanySearchResponse429
    | CompanySearchResponse500
    | CompanySearchResponse503
]:
    r"""Company search

     Search for companies using filters

    <span>⚡ <strong>Rate limit:</strong> 180 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanySearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanySearchResponse200 | CompanySearchResponse400 | CompanySearchResponse401 | CompanySearchResponse402 | CompanySearchResponse403 | CompanySearchResponse404 | CompanySearchResponse429 | CompanySearchResponse500 | CompanySearchResponse503]
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
    body: CompanySearchBody,
) -> (
    CompanySearchResponse200
    | CompanySearchResponse400
    | CompanySearchResponse401
    | CompanySearchResponse402
    | CompanySearchResponse403
    | CompanySearchResponse404
    | CompanySearchResponse429
    | CompanySearchResponse500
    | CompanySearchResponse503
    | None
):
    r"""Company search

     Search for companies using filters

    <span>⚡ <strong>Rate limit:</strong> 180 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanySearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanySearchResponse200 | CompanySearchResponse400 | CompanySearchResponse401 | CompanySearchResponse402 | CompanySearchResponse403 | CompanySearchResponse404 | CompanySearchResponse429 | CompanySearchResponse500 | CompanySearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompanySearchBody,
) -> Response[
    CompanySearchResponse200
    | CompanySearchResponse400
    | CompanySearchResponse401
    | CompanySearchResponse402
    | CompanySearchResponse403
    | CompanySearchResponse404
    | CompanySearchResponse429
    | CompanySearchResponse500
    | CompanySearchResponse503
]:
    r"""Company search

     Search for companies using filters

    <span>⚡ <strong>Rate limit:</strong> 180 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanySearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanySearchResponse200 | CompanySearchResponse400 | CompanySearchResponse401 | CompanySearchResponse402 | CompanySearchResponse403 | CompanySearchResponse404 | CompanySearchResponse429 | CompanySearchResponse500 | CompanySearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CompanySearchBody,
) -> (
    CompanySearchResponse200
    | CompanySearchResponse400
    | CompanySearchResponse401
    | CompanySearchResponse402
    | CompanySearchResponse403
    | CompanySearchResponse404
    | CompanySearchResponse429
    | CompanySearchResponse500
    | CompanySearchResponse503
    | None
):
    r"""Company search

     Search for companies using filters

    <span>⚡ <strong>Rate limit:</strong> 180 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per company found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanySearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanySearchResponse200 | CompanySearchResponse400 | CompanySearchResponse401 | CompanySearchResponse402 | CompanySearchResponse403 | CompanySearchResponse404 | CompanySearchResponse429 | CompanySearchResponse500 | CompanySearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
