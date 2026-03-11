from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_typeahead_body import CompanyTypeaheadBody
from ...models.company_typeahead_response_200 import CompanyTypeaheadResponse200
from ...models.company_typeahead_response_400 import CompanyTypeaheadResponse400
from ...models.company_typeahead_response_401 import CompanyTypeaheadResponse401
from ...models.company_typeahead_response_402 import CompanyTypeaheadResponse402
from ...models.company_typeahead_response_403 import CompanyTypeaheadResponse403
from ...models.company_typeahead_response_404 import CompanyTypeaheadResponse404
from ...models.company_typeahead_response_429 import CompanyTypeaheadResponse429
from ...models.company_typeahead_response_500 import CompanyTypeaheadResponse500
from ...models.company_typeahead_response_503 import CompanyTypeaheadResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CompanyTypeaheadBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/typeahead/company",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CompanyTypeaheadResponse200
    | CompanyTypeaheadResponse400
    | CompanyTypeaheadResponse401
    | CompanyTypeaheadResponse402
    | CompanyTypeaheadResponse403
    | CompanyTypeaheadResponse404
    | CompanyTypeaheadResponse429
    | CompanyTypeaheadResponse500
    | CompanyTypeaheadResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CompanyTypeaheadResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CompanyTypeaheadResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CompanyTypeaheadResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CompanyTypeaheadResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CompanyTypeaheadResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CompanyTypeaheadResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CompanyTypeaheadResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CompanyTypeaheadResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CompanyTypeaheadResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CompanyTypeaheadResponse200
    | CompanyTypeaheadResponse400
    | CompanyTypeaheadResponse401
    | CompanyTypeaheadResponse402
    | CompanyTypeaheadResponse403
    | CompanyTypeaheadResponse404
    | CompanyTypeaheadResponse429
    | CompanyTypeaheadResponse500
    | CompanyTypeaheadResponse503
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
    body: CompanyTypeaheadBody,
) -> Response[
    CompanyTypeaheadResponse200
    | CompanyTypeaheadResponse400
    | CompanyTypeaheadResponse401
    | CompanyTypeaheadResponse402
    | CompanyTypeaheadResponse403
    | CompanyTypeaheadResponse404
    | CompanyTypeaheadResponse429
    | CompanyTypeaheadResponse500
    | CompanyTypeaheadResponse503
]:
    r"""Company/School/Investor Typeahead

     Search for companies, schools/universities, and investors by name. Supports partial inputs, which
    can enable typeaheads in your UI.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyTypeaheadResponse200 | CompanyTypeaheadResponse400 | CompanyTypeaheadResponse401 | CompanyTypeaheadResponse402 | CompanyTypeaheadResponse403 | CompanyTypeaheadResponse404 | CompanyTypeaheadResponse429 | CompanyTypeaheadResponse500 | CompanyTypeaheadResponse503]
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
    body: CompanyTypeaheadBody,
) -> (
    CompanyTypeaheadResponse200
    | CompanyTypeaheadResponse400
    | CompanyTypeaheadResponse401
    | CompanyTypeaheadResponse402
    | CompanyTypeaheadResponse403
    | CompanyTypeaheadResponse404
    | CompanyTypeaheadResponse429
    | CompanyTypeaheadResponse500
    | CompanyTypeaheadResponse503
    | None
):
    r"""Company/School/Investor Typeahead

     Search for companies, schools/universities, and investors by name. Supports partial inputs, which
    can enable typeaheads in your UI.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyTypeaheadResponse200 | CompanyTypeaheadResponse400 | CompanyTypeaheadResponse401 | CompanyTypeaheadResponse402 | CompanyTypeaheadResponse403 | CompanyTypeaheadResponse404 | CompanyTypeaheadResponse429 | CompanyTypeaheadResponse500 | CompanyTypeaheadResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompanyTypeaheadBody,
) -> Response[
    CompanyTypeaheadResponse200
    | CompanyTypeaheadResponse400
    | CompanyTypeaheadResponse401
    | CompanyTypeaheadResponse402
    | CompanyTypeaheadResponse403
    | CompanyTypeaheadResponse404
    | CompanyTypeaheadResponse429
    | CompanyTypeaheadResponse500
    | CompanyTypeaheadResponse503
]:
    r"""Company/School/Investor Typeahead

     Search for companies, schools/universities, and investors by name. Supports partial inputs, which
    can enable typeaheads in your UI.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyTypeaheadResponse200 | CompanyTypeaheadResponse400 | CompanyTypeaheadResponse401 | CompanyTypeaheadResponse402 | CompanyTypeaheadResponse403 | CompanyTypeaheadResponse404 | CompanyTypeaheadResponse429 | CompanyTypeaheadResponse500 | CompanyTypeaheadResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CompanyTypeaheadBody,
) -> (
    CompanyTypeaheadResponse200
    | CompanyTypeaheadResponse400
    | CompanyTypeaheadResponse401
    | CompanyTypeaheadResponse402
    | CompanyTypeaheadResponse403
    | CompanyTypeaheadResponse404
    | CompanyTypeaheadResponse429
    | CompanyTypeaheadResponse500
    | CompanyTypeaheadResponse503
    | None
):
    r"""Company/School/Investor Typeahead

     Search for companies, schools/universities, and investors by name. Supports partial inputs, which
    can enable typeaheads in your UI.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CompanyTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyTypeaheadResponse200 | CompanyTypeaheadResponse400 | CompanyTypeaheadResponse401 | CompanyTypeaheadResponse402 | CompanyTypeaheadResponse403 | CompanyTypeaheadResponse404 | CompanyTypeaheadResponse429 | CompanyTypeaheadResponse500 | CompanyTypeaheadResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
