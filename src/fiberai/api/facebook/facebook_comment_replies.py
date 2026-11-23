from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_comment_replies_body import FacebookCommentRepliesBody
from ...models.facebook_comment_replies_response_200 import FacebookCommentRepliesResponse200
from ...models.facebook_comment_replies_response_400 import FacebookCommentRepliesResponse400
from ...models.facebook_comment_replies_response_401 import FacebookCommentRepliesResponse401
from ...models.facebook_comment_replies_response_402 import FacebookCommentRepliesResponse402
from ...models.facebook_comment_replies_response_403 import FacebookCommentRepliesResponse403
from ...models.facebook_comment_replies_response_404 import FacebookCommentRepliesResponse404
from ...models.facebook_comment_replies_response_422 import FacebookCommentRepliesResponse422
from ...models.facebook_comment_replies_response_429 import FacebookCommentRepliesResponse429
from ...models.facebook_comment_replies_response_500 import FacebookCommentRepliesResponse500
from ...models.facebook_comment_replies_response_503 import FacebookCommentRepliesResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookCommentRepliesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/post/comment-replies",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookCommentRepliesResponse200
    | FacebookCommentRepliesResponse400
    | FacebookCommentRepliesResponse401
    | FacebookCommentRepliesResponse402
    | FacebookCommentRepliesResponse403
    | FacebookCommentRepliesResponse404
    | FacebookCommentRepliesResponse422
    | FacebookCommentRepliesResponse429
    | FacebookCommentRepliesResponse500
    | FacebookCommentRepliesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookCommentRepliesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookCommentRepliesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookCommentRepliesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookCommentRepliesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookCommentRepliesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookCommentRepliesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookCommentRepliesResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookCommentRepliesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookCommentRepliesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookCommentRepliesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookCommentRepliesResponse200
    | FacebookCommentRepliesResponse400
    | FacebookCommentRepliesResponse401
    | FacebookCommentRepliesResponse402
    | FacebookCommentRepliesResponse403
    | FacebookCommentRepliesResponse404
    | FacebookCommentRepliesResponse422
    | FacebookCommentRepliesResponse429
    | FacebookCommentRepliesResponse500
    | FacebookCommentRepliesResponse503
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
    body: FacebookCommentRepliesBody,
) -> Response[
    FacebookCommentRepliesResponse200
    | FacebookCommentRepliesResponse400
    | FacebookCommentRepliesResponse401
    | FacebookCommentRepliesResponse402
    | FacebookCommentRepliesResponse403
    | FacebookCommentRepliesResponse404
    | FacebookCommentRepliesResponse422
    | FacebookCommentRepliesResponse429
    | FacebookCommentRepliesResponse500
    | FacebookCommentRepliesResponse503
]:
    """Fetch Facebook comment replies

     Fetches a page of replies to a comment on a Facebook post. Use the feedback ID and expansion token
    from the post comments response. Use the response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookCommentRepliesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookCommentRepliesResponse200 | FacebookCommentRepliesResponse400 | FacebookCommentRepliesResponse401 | FacebookCommentRepliesResponse402 | FacebookCommentRepliesResponse403 | FacebookCommentRepliesResponse404 | FacebookCommentRepliesResponse422 | FacebookCommentRepliesResponse429 | FacebookCommentRepliesResponse500 | FacebookCommentRepliesResponse503]
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
    body: FacebookCommentRepliesBody,
) -> (
    FacebookCommentRepliesResponse200
    | FacebookCommentRepliesResponse400
    | FacebookCommentRepliesResponse401
    | FacebookCommentRepliesResponse402
    | FacebookCommentRepliesResponse403
    | FacebookCommentRepliesResponse404
    | FacebookCommentRepliesResponse422
    | FacebookCommentRepliesResponse429
    | FacebookCommentRepliesResponse500
    | FacebookCommentRepliesResponse503
    | None
):
    """Fetch Facebook comment replies

     Fetches a page of replies to a comment on a Facebook post. Use the feedback ID and expansion token
    from the post comments response. Use the response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookCommentRepliesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookCommentRepliesResponse200 | FacebookCommentRepliesResponse400 | FacebookCommentRepliesResponse401 | FacebookCommentRepliesResponse402 | FacebookCommentRepliesResponse403 | FacebookCommentRepliesResponse404 | FacebookCommentRepliesResponse422 | FacebookCommentRepliesResponse429 | FacebookCommentRepliesResponse500 | FacebookCommentRepliesResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookCommentRepliesBody,
) -> Response[
    FacebookCommentRepliesResponse200
    | FacebookCommentRepliesResponse400
    | FacebookCommentRepliesResponse401
    | FacebookCommentRepliesResponse402
    | FacebookCommentRepliesResponse403
    | FacebookCommentRepliesResponse404
    | FacebookCommentRepliesResponse422
    | FacebookCommentRepliesResponse429
    | FacebookCommentRepliesResponse500
    | FacebookCommentRepliesResponse503
]:
    """Fetch Facebook comment replies

     Fetches a page of replies to a comment on a Facebook post. Use the feedback ID and expansion token
    from the post comments response. Use the response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookCommentRepliesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookCommentRepliesResponse200 | FacebookCommentRepliesResponse400 | FacebookCommentRepliesResponse401 | FacebookCommentRepliesResponse402 | FacebookCommentRepliesResponse403 | FacebookCommentRepliesResponse404 | FacebookCommentRepliesResponse422 | FacebookCommentRepliesResponse429 | FacebookCommentRepliesResponse500 | FacebookCommentRepliesResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookCommentRepliesBody,
) -> (
    FacebookCommentRepliesResponse200
    | FacebookCommentRepliesResponse400
    | FacebookCommentRepliesResponse401
    | FacebookCommentRepliesResponse402
    | FacebookCommentRepliesResponse403
    | FacebookCommentRepliesResponse404
    | FacebookCommentRepliesResponse422
    | FacebookCommentRepliesResponse429
    | FacebookCommentRepliesResponse500
    | FacebookCommentRepliesResponse503
    | None
):
    """Fetch Facebook comment replies

     Fetches a page of replies to a comment on a Facebook post. Use the feedback ID and expansion token
    from the post comments response. Use the response's `nextPageToken` to retrieve subsequent pages.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookCommentRepliesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookCommentRepliesResponse200 | FacebookCommentRepliesResponse400 | FacebookCommentRepliesResponse401 | FacebookCommentRepliesResponse402 | FacebookCommentRepliesResponse403 | FacebookCommentRepliesResponse404 | FacebookCommentRepliesResponse422 | FacebookCommentRepliesResponse429 | FacebookCommentRepliesResponse500 | FacebookCommentRepliesResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
