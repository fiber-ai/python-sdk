from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nlp_search_parse_body import NlpSearchParseBody
from ...models.nlp_search_parse_response_400 import NlpSearchParseResponse400
from ...models.nlp_search_parse_response_401 import NlpSearchParseResponse401
from ...models.nlp_search_parse_response_402 import NlpSearchParseResponse402
from ...models.nlp_search_parse_response_403 import NlpSearchParseResponse403
from ...models.nlp_search_parse_response_404 import NlpSearchParseResponse404
from ...models.nlp_search_parse_response_429 import NlpSearchParseResponse429
from ...models.nlp_search_parse_response_500 import NlpSearchParseResponse500
from ...models.nlp_search_parse_response_503 import NlpSearchParseResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: NlpSearchParseBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/nlp-search/parse",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    NlpSearchParseResponse400
    | NlpSearchParseResponse401
    | NlpSearchParseResponse402
    | NlpSearchParseResponse403
    | NlpSearchParseResponse404
    | NlpSearchParseResponse429
    | NlpSearchParseResponse500
    | NlpSearchParseResponse503
    | None
):
    if response.status_code == 400:
        response_400 = NlpSearchParseResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = NlpSearchParseResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = NlpSearchParseResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = NlpSearchParseResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = NlpSearchParseResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = NlpSearchParseResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = NlpSearchParseResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = NlpSearchParseResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    NlpSearchParseResponse400
    | NlpSearchParseResponse401
    | NlpSearchParseResponse402
    | NlpSearchParseResponse403
    | NlpSearchParseResponse404
    | NlpSearchParseResponse429
    | NlpSearchParseResponse500
    | NlpSearchParseResponse503
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
    body: NlpSearchParseBody,
) -> Response[
    NlpSearchParseResponse400
    | NlpSearchParseResponse401
    | NlpSearchParseResponse402
    | NlpSearchParseResponse403
    | NlpSearchParseResponse404
    | NlpSearchParseResponse429
    | NlpSearchParseResponse500
    | NlpSearchParseResponse503
]:
    r"""Parse natural language to search params

     Parses a natural language query into structured search parameters without executing the search.

    Use the returned `suggestedAction` to determine your next step:
    - `combinedSearch`: pass `parsedParams.companySearchParams` and `parsedParams.profileSearchParams`
    to POST /v1/combined-search/paginated
    - `companySearch`: pass `parsedParams.companySearchParams` to POST /v1/company-search
    - `profileSearch`: pass `parsedParams.profileSearchParams` to POST /v1/combined-search/paginated
    (with only profileConfig)
    - `personLookup`: use the `parsedParams.persons` array with POST /v1/person-lookup/enrich (one call
    per person)
    - `companyLookup`: use the `parsedParams.companies` array with POST /v1/company-lookup/enrich (one
    call per company)
    - `none`: query could not be interpreted

    Alternatively, use POST /v1/nlp-search/run to parse and execute in a single call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (NlpSearchParseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NlpSearchParseResponse400 | NlpSearchParseResponse401 | NlpSearchParseResponse402 | NlpSearchParseResponse403 | NlpSearchParseResponse404 | NlpSearchParseResponse429 | NlpSearchParseResponse500 | NlpSearchParseResponse503]
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
    body: NlpSearchParseBody,
) -> (
    NlpSearchParseResponse400
    | NlpSearchParseResponse401
    | NlpSearchParseResponse402
    | NlpSearchParseResponse403
    | NlpSearchParseResponse404
    | NlpSearchParseResponse429
    | NlpSearchParseResponse500
    | NlpSearchParseResponse503
    | None
):
    r"""Parse natural language to search params

     Parses a natural language query into structured search parameters without executing the search.

    Use the returned `suggestedAction` to determine your next step:
    - `combinedSearch`: pass `parsedParams.companySearchParams` and `parsedParams.profileSearchParams`
    to POST /v1/combined-search/paginated
    - `companySearch`: pass `parsedParams.companySearchParams` to POST /v1/company-search
    - `profileSearch`: pass `parsedParams.profileSearchParams` to POST /v1/combined-search/paginated
    (with only profileConfig)
    - `personLookup`: use the `parsedParams.persons` array with POST /v1/person-lookup/enrich (one call
    per person)
    - `companyLookup`: use the `parsedParams.companies` array with POST /v1/company-lookup/enrich (one
    call per company)
    - `none`: query could not be interpreted

    Alternatively, use POST /v1/nlp-search/run to parse and execute in a single call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (NlpSearchParseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NlpSearchParseResponse400 | NlpSearchParseResponse401 | NlpSearchParseResponse402 | NlpSearchParseResponse403 | NlpSearchParseResponse404 | NlpSearchParseResponse429 | NlpSearchParseResponse500 | NlpSearchParseResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NlpSearchParseBody,
) -> Response[
    NlpSearchParseResponse400
    | NlpSearchParseResponse401
    | NlpSearchParseResponse402
    | NlpSearchParseResponse403
    | NlpSearchParseResponse404
    | NlpSearchParseResponse429
    | NlpSearchParseResponse500
    | NlpSearchParseResponse503
]:
    r"""Parse natural language to search params

     Parses a natural language query into structured search parameters without executing the search.

    Use the returned `suggestedAction` to determine your next step:
    - `combinedSearch`: pass `parsedParams.companySearchParams` and `parsedParams.profileSearchParams`
    to POST /v1/combined-search/paginated
    - `companySearch`: pass `parsedParams.companySearchParams` to POST /v1/company-search
    - `profileSearch`: pass `parsedParams.profileSearchParams` to POST /v1/combined-search/paginated
    (with only profileConfig)
    - `personLookup`: use the `parsedParams.persons` array with POST /v1/person-lookup/enrich (one call
    per person)
    - `companyLookup`: use the `parsedParams.companies` array with POST /v1/company-lookup/enrich (one
    call per company)
    - `none`: query could not be interpreted

    Alternatively, use POST /v1/nlp-search/run to parse and execute in a single call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (NlpSearchParseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NlpSearchParseResponse400 | NlpSearchParseResponse401 | NlpSearchParseResponse402 | NlpSearchParseResponse403 | NlpSearchParseResponse404 | NlpSearchParseResponse429 | NlpSearchParseResponse500 | NlpSearchParseResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NlpSearchParseBody,
) -> (
    NlpSearchParseResponse400
    | NlpSearchParseResponse401
    | NlpSearchParseResponse402
    | NlpSearchParseResponse403
    | NlpSearchParseResponse404
    | NlpSearchParseResponse429
    | NlpSearchParseResponse500
    | NlpSearchParseResponse503
    | None
):
    r"""Parse natural language to search params

     Parses a natural language query into structured search parameters without executing the search.

    Use the returned `suggestedAction` to determine your next step:
    - `combinedSearch`: pass `parsedParams.companySearchParams` and `parsedParams.profileSearchParams`
    to POST /v1/combined-search/paginated
    - `companySearch`: pass `parsedParams.companySearchParams` to POST /v1/company-search
    - `profileSearch`: pass `parsedParams.profileSearchParams` to POST /v1/combined-search/paginated
    (with only profileConfig)
    - `personLookup`: use the `parsedParams.persons` array with POST /v1/person-lookup/enrich (one call
    per person)
    - `companyLookup`: use the `parsedParams.companies` array with POST /v1/company-lookup/enrich (one
    call per company)
    - `none`: query could not be interpreted

    Alternatively, use POST /v1/nlp-search/run to parse and execute in a single call.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (NlpSearchParseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NlpSearchParseResponse400 | NlpSearchParseResponse401 | NlpSearchParseResponse402 | NlpSearchParseResponse403 | NlpSearchParseResponse404 | NlpSearchParseResponse429 | NlpSearchParseResponse500 | NlpSearchParseResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
