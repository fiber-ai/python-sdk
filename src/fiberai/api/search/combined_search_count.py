from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.combined_search_count_body import CombinedSearchCountBody
from ...models.combined_search_count_response_200 import CombinedSearchCountResponse200
from ...models.combined_search_count_response_400 import CombinedSearchCountResponse400
from ...models.combined_search_count_response_401 import CombinedSearchCountResponse401
from ...models.combined_search_count_response_402 import CombinedSearchCountResponse402
from ...models.combined_search_count_response_403 import CombinedSearchCountResponse403
from ...models.combined_search_count_response_404 import CombinedSearchCountResponse404
from ...models.combined_search_count_response_429 import CombinedSearchCountResponse429
from ...models.combined_search_count_response_500 import CombinedSearchCountResponse500
from ...models.combined_search_count_response_503 import CombinedSearchCountResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CombinedSearchCountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/combined-search/count",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CombinedSearchCountResponse200
    | CombinedSearchCountResponse400
    | CombinedSearchCountResponse401
    | CombinedSearchCountResponse402
    | CombinedSearchCountResponse403
    | CombinedSearchCountResponse404
    | CombinedSearchCountResponse429
    | CombinedSearchCountResponse500
    | CombinedSearchCountResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CombinedSearchCountResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CombinedSearchCountResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CombinedSearchCountResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CombinedSearchCountResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CombinedSearchCountResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CombinedSearchCountResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CombinedSearchCountResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CombinedSearchCountResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CombinedSearchCountResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CombinedSearchCountResponse200
    | CombinedSearchCountResponse400
    | CombinedSearchCountResponse401
    | CombinedSearchCountResponse402
    | CombinedSearchCountResponse403
    | CombinedSearchCountResponse404
    | CombinedSearchCountResponse429
    | CombinedSearchCountResponse500
    | CombinedSearchCountResponse503
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
    body: CombinedSearchCountBody,
) -> Response[
    CombinedSearchCountResponse200
    | CombinedSearchCountResponse400
    | CombinedSearchCountResponse401
    | CombinedSearchCountResponse402
    | CombinedSearchCountResponse403
    | CombinedSearchCountResponse404
    | CombinedSearchCountResponse429
    | CombinedSearchCountResponse500
    | CombinedSearchCountResponse503
]:
    r"""Combined search count

     Get the total count of companies and people matching the provided search filters. People counts are
    scoped to those currently or previously working (based on the job status filter) at companies that
    satisfy the company search filters.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Flat charge for the company count (1 credit) and profile count (1
    credit)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Flat
    charge\">ⓘ</span></span>

    Args:
        body (CombinedSearchCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CombinedSearchCountResponse200 | CombinedSearchCountResponse400 | CombinedSearchCountResponse401 | CombinedSearchCountResponse402 | CombinedSearchCountResponse403 | CombinedSearchCountResponse404 | CombinedSearchCountResponse429 | CombinedSearchCountResponse500 | CombinedSearchCountResponse503]
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
    body: CombinedSearchCountBody,
) -> (
    CombinedSearchCountResponse200
    | CombinedSearchCountResponse400
    | CombinedSearchCountResponse401
    | CombinedSearchCountResponse402
    | CombinedSearchCountResponse403
    | CombinedSearchCountResponse404
    | CombinedSearchCountResponse429
    | CombinedSearchCountResponse500
    | CombinedSearchCountResponse503
    | None
):
    r"""Combined search count

     Get the total count of companies and people matching the provided search filters. People counts are
    scoped to those currently or previously working (based on the job status filter) at companies that
    satisfy the company search filters.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Flat charge for the company count (1 credit) and profile count (1
    credit)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Flat
    charge\">ⓘ</span></span>

    Args:
        body (CombinedSearchCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CombinedSearchCountResponse200 | CombinedSearchCountResponse400 | CombinedSearchCountResponse401 | CombinedSearchCountResponse402 | CombinedSearchCountResponse403 | CombinedSearchCountResponse404 | CombinedSearchCountResponse429 | CombinedSearchCountResponse500 | CombinedSearchCountResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CombinedSearchCountBody,
) -> Response[
    CombinedSearchCountResponse200
    | CombinedSearchCountResponse400
    | CombinedSearchCountResponse401
    | CombinedSearchCountResponse402
    | CombinedSearchCountResponse403
    | CombinedSearchCountResponse404
    | CombinedSearchCountResponse429
    | CombinedSearchCountResponse500
    | CombinedSearchCountResponse503
]:
    r"""Combined search count

     Get the total count of companies and people matching the provided search filters. People counts are
    scoped to those currently or previously working (based on the job status filter) at companies that
    satisfy the company search filters.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Flat charge for the company count (1 credit) and profile count (1
    credit)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Flat
    charge\">ⓘ</span></span>

    Args:
        body (CombinedSearchCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CombinedSearchCountResponse200 | CombinedSearchCountResponse400 | CombinedSearchCountResponse401 | CombinedSearchCountResponse402 | CombinedSearchCountResponse403 | CombinedSearchCountResponse404 | CombinedSearchCountResponse429 | CombinedSearchCountResponse500 | CombinedSearchCountResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CombinedSearchCountBody,
) -> (
    CombinedSearchCountResponse200
    | CombinedSearchCountResponse400
    | CombinedSearchCountResponse401
    | CombinedSearchCountResponse402
    | CombinedSearchCountResponse403
    | CombinedSearchCountResponse404
    | CombinedSearchCountResponse429
    | CombinedSearchCountResponse500
    | CombinedSearchCountResponse503
    | None
):
    r"""Combined search count

     Get the total count of companies and people matching the provided search filters. People counts are
    scoped to those currently or previously working (based on the job status filter) at companies that
    satisfy the company search filters.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Flat charge for the company count (1 credit) and profile count (1
    credit)&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may vary. Flat
    charge\">ⓘ</span></span>

    Args:
        body (CombinedSearchCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CombinedSearchCountResponse200 | CombinedSearchCountResponse400 | CombinedSearchCountResponse401 | CombinedSearchCountResponse402 | CombinedSearchCountResponse403 | CombinedSearchCountResponse404 | CombinedSearchCountResponse429 | CombinedSearchCountResponse500 | CombinedSearchCountResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
