from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_post_comments_body import FacebookPostCommentsBody
from ...models.facebook_post_comments_response_200 import FacebookPostCommentsResponse200
from ...models.facebook_post_comments_response_400 import FacebookPostCommentsResponse400
from ...models.facebook_post_comments_response_401 import FacebookPostCommentsResponse401
from ...models.facebook_post_comments_response_402 import FacebookPostCommentsResponse402
from ...models.facebook_post_comments_response_403 import FacebookPostCommentsResponse403
from ...models.facebook_post_comments_response_404 import FacebookPostCommentsResponse404
from ...models.facebook_post_comments_response_422 import FacebookPostCommentsResponse422
from ...models.facebook_post_comments_response_429 import FacebookPostCommentsResponse429
from ...models.facebook_post_comments_response_500 import FacebookPostCommentsResponse500
from ...models.facebook_post_comments_response_503 import FacebookPostCommentsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookPostCommentsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/post/comments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookPostCommentsResponse200
    | FacebookPostCommentsResponse400
    | FacebookPostCommentsResponse401
    | FacebookPostCommentsResponse402
    | FacebookPostCommentsResponse403
    | FacebookPostCommentsResponse404
    | FacebookPostCommentsResponse422
    | FacebookPostCommentsResponse429
    | FacebookPostCommentsResponse500
    | FacebookPostCommentsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookPostCommentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookPostCommentsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookPostCommentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookPostCommentsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookPostCommentsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookPostCommentsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookPostCommentsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookPostCommentsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookPostCommentsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookPostCommentsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookPostCommentsResponse200
    | FacebookPostCommentsResponse400
    | FacebookPostCommentsResponse401
    | FacebookPostCommentsResponse402
    | FacebookPostCommentsResponse403
    | FacebookPostCommentsResponse404
    | FacebookPostCommentsResponse422
    | FacebookPostCommentsResponse429
    | FacebookPostCommentsResponse500
    | FacebookPostCommentsResponse503
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
    body: FacebookPostCommentsBody,
) -> Response[
    FacebookPostCommentsResponse200
    | FacebookPostCommentsResponse400
    | FacebookPostCommentsResponse401
    | FacebookPostCommentsResponse402
    | FacebookPostCommentsResponse403
    | FacebookPostCommentsResponse404
    | FacebookPostCommentsResponse422
    | FacebookPostCommentsResponse429
    | FacebookPostCommentsResponse500
    | FacebookPostCommentsResponse503
]:
    """Fetch Facebook post comments

     Fetches a page of comments on a public Facebook post or Reel. Each comment includes the feedback ID
    and expansion token needed to fetch its replies. Use the response's `nextPageToken` to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookPostCommentsResponse200 | FacebookPostCommentsResponse400 | FacebookPostCommentsResponse401 | FacebookPostCommentsResponse402 | FacebookPostCommentsResponse403 | FacebookPostCommentsResponse404 | FacebookPostCommentsResponse422 | FacebookPostCommentsResponse429 | FacebookPostCommentsResponse500 | FacebookPostCommentsResponse503]
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
    body: FacebookPostCommentsBody,
) -> (
    FacebookPostCommentsResponse200
    | FacebookPostCommentsResponse400
    | FacebookPostCommentsResponse401
    | FacebookPostCommentsResponse402
    | FacebookPostCommentsResponse403
    | FacebookPostCommentsResponse404
    | FacebookPostCommentsResponse422
    | FacebookPostCommentsResponse429
    | FacebookPostCommentsResponse500
    | FacebookPostCommentsResponse503
    | None
):
    """Fetch Facebook post comments

     Fetches a page of comments on a public Facebook post or Reel. Each comment includes the feedback ID
    and expansion token needed to fetch its replies. Use the response's `nextPageToken` to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookPostCommentsResponse200 | FacebookPostCommentsResponse400 | FacebookPostCommentsResponse401 | FacebookPostCommentsResponse402 | FacebookPostCommentsResponse403 | FacebookPostCommentsResponse404 | FacebookPostCommentsResponse422 | FacebookPostCommentsResponse429 | FacebookPostCommentsResponse500 | FacebookPostCommentsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookPostCommentsBody,
) -> Response[
    FacebookPostCommentsResponse200
    | FacebookPostCommentsResponse400
    | FacebookPostCommentsResponse401
    | FacebookPostCommentsResponse402
    | FacebookPostCommentsResponse403
    | FacebookPostCommentsResponse404
    | FacebookPostCommentsResponse422
    | FacebookPostCommentsResponse429
    | FacebookPostCommentsResponse500
    | FacebookPostCommentsResponse503
]:
    """Fetch Facebook post comments

     Fetches a page of comments on a public Facebook post or Reel. Each comment includes the feedback ID
    and expansion token needed to fetch its replies. Use the response's `nextPageToken` to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookPostCommentsResponse200 | FacebookPostCommentsResponse400 | FacebookPostCommentsResponse401 | FacebookPostCommentsResponse402 | FacebookPostCommentsResponse403 | FacebookPostCommentsResponse404 | FacebookPostCommentsResponse422 | FacebookPostCommentsResponse429 | FacebookPostCommentsResponse500 | FacebookPostCommentsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookPostCommentsBody,
) -> (
    FacebookPostCommentsResponse200
    | FacebookPostCommentsResponse400
    | FacebookPostCommentsResponse401
    | FacebookPostCommentsResponse402
    | FacebookPostCommentsResponse403
    | FacebookPostCommentsResponse404
    | FacebookPostCommentsResponse422
    | FacebookPostCommentsResponse429
    | FacebookPostCommentsResponse500
    | FacebookPostCommentsResponse503
    | None
):
    """Fetch Facebook post comments

     Fetches a page of comments on a public Facebook post or Reel. Each comment includes the feedback ID
    and expansion token needed to fetch its replies. Use the response's `nextPageToken` to retrieve
    subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookPostCommentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookPostCommentsResponse200 | FacebookPostCommentsResponse400 | FacebookPostCommentsResponse401 | FacebookPostCommentsResponse402 | FacebookPostCommentsResponse403 | FacebookPostCommentsResponse404 | FacebookPostCommentsResponse422 | FacebookPostCommentsResponse429 | FacebookPostCommentsResponse500 | FacebookPostCommentsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
