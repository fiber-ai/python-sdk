from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_local_business_search_body import StartLocalBusinessSearchBody
from ...models.start_local_business_search_response_200 import StartLocalBusinessSearchResponse200
from ...models.start_local_business_search_response_400 import StartLocalBusinessSearchResponse400
from ...models.start_local_business_search_response_401 import StartLocalBusinessSearchResponse401
from ...models.start_local_business_search_response_402 import StartLocalBusinessSearchResponse402
from ...models.start_local_business_search_response_403 import StartLocalBusinessSearchResponse403
from ...models.start_local_business_search_response_404 import StartLocalBusinessSearchResponse404
from ...models.start_local_business_search_response_429 import StartLocalBusinessSearchResponse429
from ...models.start_local_business_search_response_500 import StartLocalBusinessSearchResponse500
from ...models.start_local_business_search_response_503 import StartLocalBusinessSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: StartLocalBusinessSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/local-business-search/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StartLocalBusinessSearchResponse200
    | StartLocalBusinessSearchResponse400
    | StartLocalBusinessSearchResponse401
    | StartLocalBusinessSearchResponse402
    | StartLocalBusinessSearchResponse403
    | StartLocalBusinessSearchResponse404
    | StartLocalBusinessSearchResponse429
    | StartLocalBusinessSearchResponse500
    | StartLocalBusinessSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = StartLocalBusinessSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StartLocalBusinessSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StartLocalBusinessSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = StartLocalBusinessSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = StartLocalBusinessSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StartLocalBusinessSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = StartLocalBusinessSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = StartLocalBusinessSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = StartLocalBusinessSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StartLocalBusinessSearchResponse200
    | StartLocalBusinessSearchResponse400
    | StartLocalBusinessSearchResponse401
    | StartLocalBusinessSearchResponse402
    | StartLocalBusinessSearchResponse403
    | StartLocalBusinessSearchResponse404
    | StartLocalBusinessSearchResponse429
    | StartLocalBusinessSearchResponse500
    | StartLocalBusinessSearchResponse503
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
    body: StartLocalBusinessSearchBody,
) -> Response[
    StartLocalBusinessSearchResponse200
    | StartLocalBusinessSearchResponse400
    | StartLocalBusinessSearchResponse401
    | StartLocalBusinessSearchResponse402
    | StartLocalBusinessSearchResponse403
    | StartLocalBusinessSearchResponse404
    | StartLocalBusinessSearchResponse429
    | StartLocalBusinessSearchResponse500
    | StartLocalBusinessSearchResponse503
]:
    r"""Start local business search

     Coming Soon! Start a local business search task

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (StartLocalBusinessSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartLocalBusinessSearchResponse200 | StartLocalBusinessSearchResponse400 | StartLocalBusinessSearchResponse401 | StartLocalBusinessSearchResponse402 | StartLocalBusinessSearchResponse403 | StartLocalBusinessSearchResponse404 | StartLocalBusinessSearchResponse429 | StartLocalBusinessSearchResponse500 | StartLocalBusinessSearchResponse503]
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
    body: StartLocalBusinessSearchBody,
) -> (
    StartLocalBusinessSearchResponse200
    | StartLocalBusinessSearchResponse400
    | StartLocalBusinessSearchResponse401
    | StartLocalBusinessSearchResponse402
    | StartLocalBusinessSearchResponse403
    | StartLocalBusinessSearchResponse404
    | StartLocalBusinessSearchResponse429
    | StartLocalBusinessSearchResponse500
    | StartLocalBusinessSearchResponse503
    | None
):
    r"""Start local business search

     Coming Soon! Start a local business search task

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (StartLocalBusinessSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartLocalBusinessSearchResponse200 | StartLocalBusinessSearchResponse400 | StartLocalBusinessSearchResponse401 | StartLocalBusinessSearchResponse402 | StartLocalBusinessSearchResponse403 | StartLocalBusinessSearchResponse404 | StartLocalBusinessSearchResponse429 | StartLocalBusinessSearchResponse500 | StartLocalBusinessSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartLocalBusinessSearchBody,
) -> Response[
    StartLocalBusinessSearchResponse200
    | StartLocalBusinessSearchResponse400
    | StartLocalBusinessSearchResponse401
    | StartLocalBusinessSearchResponse402
    | StartLocalBusinessSearchResponse403
    | StartLocalBusinessSearchResponse404
    | StartLocalBusinessSearchResponse429
    | StartLocalBusinessSearchResponse500
    | StartLocalBusinessSearchResponse503
]:
    r"""Start local business search

     Coming Soon! Start a local business search task

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (StartLocalBusinessSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartLocalBusinessSearchResponse200 | StartLocalBusinessSearchResponse400 | StartLocalBusinessSearchResponse401 | StartLocalBusinessSearchResponse402 | StartLocalBusinessSearchResponse403 | StartLocalBusinessSearchResponse404 | StartLocalBusinessSearchResponse429 | StartLocalBusinessSearchResponse500 | StartLocalBusinessSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StartLocalBusinessSearchBody,
) -> (
    StartLocalBusinessSearchResponse200
    | StartLocalBusinessSearchResponse400
    | StartLocalBusinessSearchResponse401
    | StartLocalBusinessSearchResponse402
    | StartLocalBusinessSearchResponse403
    | StartLocalBusinessSearchResponse404
    | StartLocalBusinessSearchResponse429
    | StartLocalBusinessSearchResponse500
    | StartLocalBusinessSearchResponse503
    | None
):
    r"""Start local business search

     Coming Soon! Start a local business search task

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per company&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (StartLocalBusinessSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartLocalBusinessSearchResponse200 | StartLocalBusinessSearchResponse400 | StartLocalBusinessSearchResponse401 | StartLocalBusinessSearchResponse402 | StartLocalBusinessSearchResponse403 | StartLocalBusinessSearchResponse404 | StartLocalBusinessSearchResponse429 | StartLocalBusinessSearchResponse500 | StartLocalBusinessSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
