from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.twitter_search_body import TwitterSearchBody
from ...models.twitter_search_response_200 import TwitterSearchResponse200
from ...models.twitter_search_response_400 import TwitterSearchResponse400
from ...models.twitter_search_response_401 import TwitterSearchResponse401
from ...models.twitter_search_response_402 import TwitterSearchResponse402
from ...models.twitter_search_response_403 import TwitterSearchResponse403
from ...models.twitter_search_response_404 import TwitterSearchResponse404
from ...models.twitter_search_response_422 import TwitterSearchResponse422
from ...models.twitter_search_response_429 import TwitterSearchResponse429
from ...models.twitter_search_response_500 import TwitterSearchResponse500
from ...models.twitter_search_response_503 import TwitterSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TwitterSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/twitter/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TwitterSearchResponse200
    | TwitterSearchResponse400
    | TwitterSearchResponse401
    | TwitterSearchResponse402
    | TwitterSearchResponse403
    | TwitterSearchResponse404
    | TwitterSearchResponse422
    | TwitterSearchResponse429
    | TwitterSearchResponse500
    | TwitterSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TwitterSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TwitterSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TwitterSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TwitterSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TwitterSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TwitterSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = TwitterSearchResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = TwitterSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TwitterSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TwitterSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TwitterSearchResponse200
    | TwitterSearchResponse400
    | TwitterSearchResponse401
    | TwitterSearchResponse402
    | TwitterSearchResponse403
    | TwitterSearchResponse404
    | TwitterSearchResponse422
    | TwitterSearchResponse429
    | TwitterSearchResponse500
    | TwitterSearchResponse503
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
    body: TwitterSearchBody,
) -> Response[
    TwitterSearchResponse200
    | TwitterSearchResponse400
    | TwitterSearchResponse401
    | TwitterSearchResponse402
    | TwitterSearchResponse403
    | TwitterSearchResponse404
    | TwitterSearchResponse422
    | TwitterSearchResponse429
    | TwitterSearchResponse500
    | TwitterSearchResponse503
]:
    r"""Search Twitter/X tweets

     Searches for tweets matching a query. Supports standard Twitter search operators (e.g. 'TypeScript
    from:elonmusk lang:en'). Returns a paginated list of matching tweets. Use the `cursor` field from
    the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterSearchResponse200 | TwitterSearchResponse400 | TwitterSearchResponse401 | TwitterSearchResponse402 | TwitterSearchResponse403 | TwitterSearchResponse404 | TwitterSearchResponse422 | TwitterSearchResponse429 | TwitterSearchResponse500 | TwitterSearchResponse503]
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
    body: TwitterSearchBody,
) -> (
    TwitterSearchResponse200
    | TwitterSearchResponse400
    | TwitterSearchResponse401
    | TwitterSearchResponse402
    | TwitterSearchResponse403
    | TwitterSearchResponse404
    | TwitterSearchResponse422
    | TwitterSearchResponse429
    | TwitterSearchResponse500
    | TwitterSearchResponse503
    | None
):
    r"""Search Twitter/X tweets

     Searches for tweets matching a query. Supports standard Twitter search operators (e.g. 'TypeScript
    from:elonmusk lang:en'). Returns a paginated list of matching tweets. Use the `cursor` field from
    the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterSearchResponse200 | TwitterSearchResponse400 | TwitterSearchResponse401 | TwitterSearchResponse402 | TwitterSearchResponse403 | TwitterSearchResponse404 | TwitterSearchResponse422 | TwitterSearchResponse429 | TwitterSearchResponse500 | TwitterSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterSearchBody,
) -> Response[
    TwitterSearchResponse200
    | TwitterSearchResponse400
    | TwitterSearchResponse401
    | TwitterSearchResponse402
    | TwitterSearchResponse403
    | TwitterSearchResponse404
    | TwitterSearchResponse422
    | TwitterSearchResponse429
    | TwitterSearchResponse500
    | TwitterSearchResponse503
]:
    r"""Search Twitter/X tweets

     Searches for tweets matching a query. Supports standard Twitter search operators (e.g. 'TypeScript
    from:elonmusk lang:en'). Returns a paginated list of matching tweets. Use the `cursor` field from
    the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwitterSearchResponse200 | TwitterSearchResponse400 | TwitterSearchResponse401 | TwitterSearchResponse402 | TwitterSearchResponse403 | TwitterSearchResponse404 | TwitterSearchResponse422 | TwitterSearchResponse429 | TwitterSearchResponse500 | TwitterSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TwitterSearchBody,
) -> (
    TwitterSearchResponse200
    | TwitterSearchResponse400
    | TwitterSearchResponse401
    | TwitterSearchResponse402
    | TwitterSearchResponse403
    | TwitterSearchResponse404
    | TwitterSearchResponse422
    | TwitterSearchResponse429
    | TwitterSearchResponse500
    | TwitterSearchResponse503
    | None
):
    r"""Search Twitter/X tweets

     Searches for tweets matching a query. Supports standard Twitter search operators (e.g. 'TypeScript
    from:elonmusk lang:en'). Returns a paginated list of matching tweets. Use the `cursor` field from
    the response to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TwitterSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwitterSearchResponse200 | TwitterSearchResponse400 | TwitterSearchResponse401 | TwitterSearchResponse402 | TwitterSearchResponse403 | TwitterSearchResponse404 | TwitterSearchResponse422 | TwitterSearchResponse429 | TwitterSearchResponse500 | TwitterSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
