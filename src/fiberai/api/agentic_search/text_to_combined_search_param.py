from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.text_to_combined_search_param_body import TextToCombinedSearchParamBody
from ...models.text_to_combined_search_param_response_200 import TextToCombinedSearchParamResponse200
from ...models.text_to_combined_search_param_response_400 import TextToCombinedSearchParamResponse400
from ...models.text_to_combined_search_param_response_401 import TextToCombinedSearchParamResponse401
from ...models.text_to_combined_search_param_response_402 import TextToCombinedSearchParamResponse402
from ...models.text_to_combined_search_param_response_403 import TextToCombinedSearchParamResponse403
from ...models.text_to_combined_search_param_response_404 import TextToCombinedSearchParamResponse404
from ...models.text_to_combined_search_param_response_429 import TextToCombinedSearchParamResponse429
from ...models.text_to_combined_search_param_response_500 import TextToCombinedSearchParamResponse500
from ...models.text_to_combined_search_param_response_503 import TextToCombinedSearchParamResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TextToCombinedSearchParamBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/natural-language-search/combined-search-param",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TextToCombinedSearchParamResponse200
    | TextToCombinedSearchParamResponse400
    | TextToCombinedSearchParamResponse401
    | TextToCombinedSearchParamResponse402
    | TextToCombinedSearchParamResponse403
    | TextToCombinedSearchParamResponse404
    | TextToCombinedSearchParamResponse429
    | TextToCombinedSearchParamResponse500
    | TextToCombinedSearchParamResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TextToCombinedSearchParamResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TextToCombinedSearchParamResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TextToCombinedSearchParamResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TextToCombinedSearchParamResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TextToCombinedSearchParamResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TextToCombinedSearchParamResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TextToCombinedSearchParamResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TextToCombinedSearchParamResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TextToCombinedSearchParamResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TextToCombinedSearchParamResponse200
    | TextToCombinedSearchParamResponse400
    | TextToCombinedSearchParamResponse401
    | TextToCombinedSearchParamResponse402
    | TextToCombinedSearchParamResponse403
    | TextToCombinedSearchParamResponse404
    | TextToCombinedSearchParamResponse429
    | TextToCombinedSearchParamResponse500
    | TextToCombinedSearchParamResponse503
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
    body: TextToCombinedSearchParamBody,
) -> Response[
    TextToCombinedSearchParamResponse200
    | TextToCombinedSearchParamResponse400
    | TextToCombinedSearchParamResponse401
    | TextToCombinedSearchParamResponse402
    | TextToCombinedSearchParamResponse403
    | TextToCombinedSearchParamResponse404
    | TextToCombinedSearchParamResponse429
    | TextToCombinedSearchParamResponse500
    | TextToCombinedSearchParamResponse503
]:
    r"""Converts text to companies and prospects search params

     Takes free-form text (e.g., 'Senior Product Managers from Series A to C FinTech startups in New
    York') and produces standardized filters (industries, funding stages, headcount ranges, locations,
    titles, seniorities, etc.). When limits are provided, executes the search and returns matching
    companies and people in a single synchronous call. When referencing specific companies, provide the
    identifier in one of these forms: plain name (e.g. 'Apple'), domain (e.g. 'apple.com'), or LinkedIn
    slug (e.g. 'company/banco-santander').Note: This is not optimized for job descriptions. If you have
    a JD, use the Search profiles from a job description endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request:<br />• 2 credits for company search params
    generation based on prompt, if required<br />• 2 credits for profile search params generation based
    on prompt, if required&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary.\">ⓘ</span></span>

    Args:
        body (TextToCombinedSearchParamBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TextToCombinedSearchParamResponse200 | TextToCombinedSearchParamResponse400 | TextToCombinedSearchParamResponse401 | TextToCombinedSearchParamResponse402 | TextToCombinedSearchParamResponse403 | TextToCombinedSearchParamResponse404 | TextToCombinedSearchParamResponse429 | TextToCombinedSearchParamResponse500 | TextToCombinedSearchParamResponse503]
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
    body: TextToCombinedSearchParamBody,
) -> (
    TextToCombinedSearchParamResponse200
    | TextToCombinedSearchParamResponse400
    | TextToCombinedSearchParamResponse401
    | TextToCombinedSearchParamResponse402
    | TextToCombinedSearchParamResponse403
    | TextToCombinedSearchParamResponse404
    | TextToCombinedSearchParamResponse429
    | TextToCombinedSearchParamResponse500
    | TextToCombinedSearchParamResponse503
    | None
):
    r"""Converts text to companies and prospects search params

     Takes free-form text (e.g., 'Senior Product Managers from Series A to C FinTech startups in New
    York') and produces standardized filters (industries, funding stages, headcount ranges, locations,
    titles, seniorities, etc.). When limits are provided, executes the search and returns matching
    companies and people in a single synchronous call. When referencing specific companies, provide the
    identifier in one of these forms: plain name (e.g. 'Apple'), domain (e.g. 'apple.com'), or LinkedIn
    slug (e.g. 'company/banco-santander').Note: This is not optimized for job descriptions. If you have
    a JD, use the Search profiles from a job description endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request:<br />• 2 credits for company search params
    generation based on prompt, if required<br />• 2 credits for profile search params generation based
    on prompt, if required&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary.\">ⓘ</span></span>

    Args:
        body (TextToCombinedSearchParamBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TextToCombinedSearchParamResponse200 | TextToCombinedSearchParamResponse400 | TextToCombinedSearchParamResponse401 | TextToCombinedSearchParamResponse402 | TextToCombinedSearchParamResponse403 | TextToCombinedSearchParamResponse404 | TextToCombinedSearchParamResponse429 | TextToCombinedSearchParamResponse500 | TextToCombinedSearchParamResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TextToCombinedSearchParamBody,
) -> Response[
    TextToCombinedSearchParamResponse200
    | TextToCombinedSearchParamResponse400
    | TextToCombinedSearchParamResponse401
    | TextToCombinedSearchParamResponse402
    | TextToCombinedSearchParamResponse403
    | TextToCombinedSearchParamResponse404
    | TextToCombinedSearchParamResponse429
    | TextToCombinedSearchParamResponse500
    | TextToCombinedSearchParamResponse503
]:
    r"""Converts text to companies and prospects search params

     Takes free-form text (e.g., 'Senior Product Managers from Series A to C FinTech startups in New
    York') and produces standardized filters (industries, funding stages, headcount ranges, locations,
    titles, seniorities, etc.). When limits are provided, executes the search and returns matching
    companies and people in a single synchronous call. When referencing specific companies, provide the
    identifier in one of these forms: plain name (e.g. 'Apple'), domain (e.g. 'apple.com'), or LinkedIn
    slug (e.g. 'company/banco-santander').Note: This is not optimized for job descriptions. If you have
    a JD, use the Search profiles from a job description endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request:<br />• 2 credits for company search params
    generation based on prompt, if required<br />• 2 credits for profile search params generation based
    on prompt, if required&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary.\">ⓘ</span></span>

    Args:
        body (TextToCombinedSearchParamBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TextToCombinedSearchParamResponse200 | TextToCombinedSearchParamResponse400 | TextToCombinedSearchParamResponse401 | TextToCombinedSearchParamResponse402 | TextToCombinedSearchParamResponse403 | TextToCombinedSearchParamResponse404 | TextToCombinedSearchParamResponse429 | TextToCombinedSearchParamResponse500 | TextToCombinedSearchParamResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TextToCombinedSearchParamBody,
) -> (
    TextToCombinedSearchParamResponse200
    | TextToCombinedSearchParamResponse400
    | TextToCombinedSearchParamResponse401
    | TextToCombinedSearchParamResponse402
    | TextToCombinedSearchParamResponse403
    | TextToCombinedSearchParamResponse404
    | TextToCombinedSearchParamResponse429
    | TextToCombinedSearchParamResponse500
    | TextToCombinedSearchParamResponse503
    | None
):
    r"""Converts text to companies and prospects search params

     Takes free-form text (e.g., 'Senior Product Managers from Series A to C FinTech startups in New
    York') and produces standardized filters (industries, funding stages, headcount ranges, locations,
    titles, seniorities, etc.). When limits are provided, executes the search and returns matching
    companies and people in a single synchronous call. When referencing specific companies, provide the
    identifier in one of these forms: plain name (e.g. 'Apple'), domain (e.g. 'apple.com'), or LinkedIn
    slug (e.g. 'company/banco-santander').Note: This is not optimized for job descriptions. If you have
    a JD, use the Search profiles from a job description endpoint instead.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request:<br />• 2 credits for company search params
    generation based on prompt, if required<br />• 2 credits for profile search params generation based
    on prompt, if required&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary.\">ⓘ</span></span>

    Args:
        body (TextToCombinedSearchParamBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TextToCombinedSearchParamResponse200 | TextToCombinedSearchParamResponse400 | TextToCombinedSearchParamResponse401 | TextToCombinedSearchParamResponse402 | TextToCombinedSearchParamResponse403 | TextToCombinedSearchParamResponse404 | TextToCombinedSearchParamResponse429 | TextToCombinedSearchParamResponse500 | TextToCombinedSearchParamResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
