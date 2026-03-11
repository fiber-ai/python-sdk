from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.text_to_company_search_body import TextToCompanySearchBody
from ...models.text_to_company_search_response_200 import TextToCompanySearchResponse200
from ...models.text_to_company_search_response_400 import TextToCompanySearchResponse400
from ...models.text_to_company_search_response_401 import TextToCompanySearchResponse401
from ...models.text_to_company_search_response_402 import TextToCompanySearchResponse402
from ...models.text_to_company_search_response_403 import TextToCompanySearchResponse403
from ...models.text_to_company_search_response_404 import TextToCompanySearchResponse404
from ...models.text_to_company_search_response_429 import TextToCompanySearchResponse429
from ...models.text_to_company_search_response_500 import TextToCompanySearchResponse500
from ...models.text_to_company_search_response_503 import TextToCompanySearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TextToCompanySearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/natural-language-search/companies",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TextToCompanySearchResponse200
    | TextToCompanySearchResponse400
    | TextToCompanySearchResponse401
    | TextToCompanySearchResponse402
    | TextToCompanySearchResponse403
    | TextToCompanySearchResponse404
    | TextToCompanySearchResponse429
    | TextToCompanySearchResponse500
    | TextToCompanySearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TextToCompanySearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TextToCompanySearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TextToCompanySearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TextToCompanySearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TextToCompanySearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TextToCompanySearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TextToCompanySearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TextToCompanySearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TextToCompanySearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TextToCompanySearchResponse200
    | TextToCompanySearchResponse400
    | TextToCompanySearchResponse401
    | TextToCompanySearchResponse402
    | TextToCompanySearchResponse403
    | TextToCompanySearchResponse404
    | TextToCompanySearchResponse429
    | TextToCompanySearchResponse500
    | TextToCompanySearchResponse503
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
    body: TextToCompanySearchBody,
) -> Response[
    TextToCompanySearchResponse200
    | TextToCompanySearchResponse400
    | TextToCompanySearchResponse401
    | TextToCompanySearchResponse402
    | TextToCompanySearchResponse403
    | TextToCompanySearchResponse404
    | TextToCompanySearchResponse429
    | TextToCompanySearchResponse500
    | TextToCompanySearchResponse503
]:
    r"""Search companies from text

     Takes free-form text (e.g., 'Series A startups in USA with 50–200 employees') and returns a list of
    matching companies.           The endpoint interprets natural language queries and applies
    structured filters such as industries, funding stages, headcount ranges, and locations to identify
    relevant companies.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per company found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCompanySearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TextToCompanySearchResponse200 | TextToCompanySearchResponse400 | TextToCompanySearchResponse401 | TextToCompanySearchResponse402 | TextToCompanySearchResponse403 | TextToCompanySearchResponse404 | TextToCompanySearchResponse429 | TextToCompanySearchResponse500 | TextToCompanySearchResponse503]
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
    body: TextToCompanySearchBody,
) -> (
    TextToCompanySearchResponse200
    | TextToCompanySearchResponse400
    | TextToCompanySearchResponse401
    | TextToCompanySearchResponse402
    | TextToCompanySearchResponse403
    | TextToCompanySearchResponse404
    | TextToCompanySearchResponse429
    | TextToCompanySearchResponse500
    | TextToCompanySearchResponse503
    | None
):
    r"""Search companies from text

     Takes free-form text (e.g., 'Series A startups in USA with 50–200 employees') and returns a list of
    matching companies.           The endpoint interprets natural language queries and applies
    structured filters such as industries, funding stages, headcount ranges, and locations to identify
    relevant companies.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per company found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCompanySearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TextToCompanySearchResponse200 | TextToCompanySearchResponse400 | TextToCompanySearchResponse401 | TextToCompanySearchResponse402 | TextToCompanySearchResponse403 | TextToCompanySearchResponse404 | TextToCompanySearchResponse429 | TextToCompanySearchResponse500 | TextToCompanySearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TextToCompanySearchBody,
) -> Response[
    TextToCompanySearchResponse200
    | TextToCompanySearchResponse400
    | TextToCompanySearchResponse401
    | TextToCompanySearchResponse402
    | TextToCompanySearchResponse403
    | TextToCompanySearchResponse404
    | TextToCompanySearchResponse429
    | TextToCompanySearchResponse500
    | TextToCompanySearchResponse503
]:
    r"""Search companies from text

     Takes free-form text (e.g., 'Series A startups in USA with 50–200 employees') and returns a list of
    matching companies.           The endpoint interprets natural language queries and applies
    structured filters such as industries, funding stages, headcount ranges, and locations to identify
    relevant companies.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per company found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCompanySearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TextToCompanySearchResponse200 | TextToCompanySearchResponse400 | TextToCompanySearchResponse401 | TextToCompanySearchResponse402 | TextToCompanySearchResponse403 | TextToCompanySearchResponse404 | TextToCompanySearchResponse429 | TextToCompanySearchResponse500 | TextToCompanySearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TextToCompanySearchBody,
) -> (
    TextToCompanySearchResponse200
    | TextToCompanySearchResponse400
    | TextToCompanySearchResponse401
    | TextToCompanySearchResponse402
    | TextToCompanySearchResponse403
    | TextToCompanySearchResponse404
    | TextToCompanySearchResponse429
    | TextToCompanySearchResponse500
    | TextToCompanySearchResponse503
    | None
):
    r"""Search companies from text

     Takes free-form text (e.g., 'Series A startups in USA with 50–200 employees') and returns a list of
    matching companies.           The endpoint interprets natural language queries and applies
    structured filters such as industries, funding stages, headcount ranges, and locations to identify
    relevant companies.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per company found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToCompanySearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TextToCompanySearchResponse200 | TextToCompanySearchResponse400 | TextToCompanySearchResponse401 | TextToCompanySearchResponse402 | TextToCompanySearchResponse403 | TextToCompanySearchResponse404 | TextToCompanySearchResponse429 | TextToCompanySearchResponse500 | TextToCompanySearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
