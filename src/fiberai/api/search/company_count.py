from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_count_body import CompanyCountBody
from ...models.company_count_response_200 import CompanyCountResponse200
from ...models.company_count_response_400 import CompanyCountResponse400
from ...models.company_count_response_401 import CompanyCountResponse401
from ...models.company_count_response_402 import CompanyCountResponse402
from ...models.company_count_response_403 import CompanyCountResponse403
from ...models.company_count_response_404 import CompanyCountResponse404
from ...models.company_count_response_429 import CompanyCountResponse429
from ...models.company_count_response_500 import CompanyCountResponse500
from ...models.company_count_response_503 import CompanyCountResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CompanyCountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/company-count",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CompanyCountResponse200
    | CompanyCountResponse400
    | CompanyCountResponse401
    | CompanyCountResponse402
    | CompanyCountResponse403
    | CompanyCountResponse404
    | CompanyCountResponse429
    | CompanyCountResponse500
    | CompanyCountResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CompanyCountResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CompanyCountResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CompanyCountResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CompanyCountResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CompanyCountResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CompanyCountResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CompanyCountResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CompanyCountResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CompanyCountResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CompanyCountResponse200
    | CompanyCountResponse400
    | CompanyCountResponse401
    | CompanyCountResponse402
    | CompanyCountResponse403
    | CompanyCountResponse404
    | CompanyCountResponse429
    | CompanyCountResponse500
    | CompanyCountResponse503
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
    body: CompanyCountBody,
) -> Response[
    CompanyCountResponse200
    | CompanyCountResponse400
    | CompanyCountResponse401
    | CompanyCountResponse402
    | CompanyCountResponse403
    | CompanyCountResponse404
    | CompanyCountResponse429
    | CompanyCountResponse500
    | CompanyCountResponse503
]:
    r"""Company count

     Get count of companies matching search filters

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyCountResponse200 | CompanyCountResponse400 | CompanyCountResponse401 | CompanyCountResponse402 | CompanyCountResponse403 | CompanyCountResponse404 | CompanyCountResponse429 | CompanyCountResponse500 | CompanyCountResponse503]
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
    body: CompanyCountBody,
) -> (
    CompanyCountResponse200
    | CompanyCountResponse400
    | CompanyCountResponse401
    | CompanyCountResponse402
    | CompanyCountResponse403
    | CompanyCountResponse404
    | CompanyCountResponse429
    | CompanyCountResponse500
    | CompanyCountResponse503
    | None
):
    r"""Company count

     Get count of companies matching search filters

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyCountResponse200 | CompanyCountResponse400 | CompanyCountResponse401 | CompanyCountResponse402 | CompanyCountResponse403 | CompanyCountResponse404 | CompanyCountResponse429 | CompanyCountResponse500 | CompanyCountResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompanyCountBody,
) -> Response[
    CompanyCountResponse200
    | CompanyCountResponse400
    | CompanyCountResponse401
    | CompanyCountResponse402
    | CompanyCountResponse403
    | CompanyCountResponse404
    | CompanyCountResponse429
    | CompanyCountResponse500
    | CompanyCountResponse503
]:
    r"""Company count

     Get count of companies matching search filters

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyCountResponse200 | CompanyCountResponse400 | CompanyCountResponse401 | CompanyCountResponse402 | CompanyCountResponse403 | CompanyCountResponse404 | CompanyCountResponse429 | CompanyCountResponse500 | CompanyCountResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CompanyCountBody,
) -> (
    CompanyCountResponse200
    | CompanyCountResponse400
    | CompanyCountResponse401
    | CompanyCountResponse402
    | CompanyCountResponse403
    | CompanyCountResponse404
    | CompanyCountResponse429
    | CompanyCountResponse500
    | CompanyCountResponse503
    | None
):
    r"""Company count

     Get count of companies matching search filters

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyCountResponse200 | CompanyCountResponse400 | CompanyCountResponse401 | CompanyCountResponse402 | CompanyCountResponse403 | CompanyCountResponse404 | CompanyCountResponse429 | CompanyCountResponse500 | CompanyCountResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
