from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facebook_group_details_body import FacebookGroupDetailsBody
from ...models.facebook_group_details_response_200 import FacebookGroupDetailsResponse200
from ...models.facebook_group_details_response_400 import FacebookGroupDetailsResponse400
from ...models.facebook_group_details_response_401 import FacebookGroupDetailsResponse401
from ...models.facebook_group_details_response_402 import FacebookGroupDetailsResponse402
from ...models.facebook_group_details_response_403 import FacebookGroupDetailsResponse403
from ...models.facebook_group_details_response_404 import FacebookGroupDetailsResponse404
from ...models.facebook_group_details_response_422 import FacebookGroupDetailsResponse422
from ...models.facebook_group_details_response_429 import FacebookGroupDetailsResponse429
from ...models.facebook_group_details_response_500 import FacebookGroupDetailsResponse500
from ...models.facebook_group_details_response_503 import FacebookGroupDetailsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: FacebookGroupDetailsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/facebook/group/details",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FacebookGroupDetailsResponse200
    | FacebookGroupDetailsResponse400
    | FacebookGroupDetailsResponse401
    | FacebookGroupDetailsResponse402
    | FacebookGroupDetailsResponse403
    | FacebookGroupDetailsResponse404
    | FacebookGroupDetailsResponse422
    | FacebookGroupDetailsResponse429
    | FacebookGroupDetailsResponse500
    | FacebookGroupDetailsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = FacebookGroupDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FacebookGroupDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FacebookGroupDetailsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FacebookGroupDetailsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = FacebookGroupDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = FacebookGroupDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = FacebookGroupDetailsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FacebookGroupDetailsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FacebookGroupDetailsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = FacebookGroupDetailsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FacebookGroupDetailsResponse200
    | FacebookGroupDetailsResponse400
    | FacebookGroupDetailsResponse401
    | FacebookGroupDetailsResponse402
    | FacebookGroupDetailsResponse403
    | FacebookGroupDetailsResponse404
    | FacebookGroupDetailsResponse422
    | FacebookGroupDetailsResponse429
    | FacebookGroupDetailsResponse500
    | FacebookGroupDetailsResponse503
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
    body: FacebookGroupDetailsBody,
) -> Response[
    FacebookGroupDetailsResponse200
    | FacebookGroupDetailsResponse400
    | FacebookGroupDetailsResponse401
    | FacebookGroupDetailsResponse402
    | FacebookGroupDetailsResponse403
    | FacebookGroupDetailsResponse404
    | FacebookGroupDetailsResponse422
    | FacebookGroupDetailsResponse429
    | FacebookGroupDetailsResponse500
    | FacebookGroupDetailsResponse503
]:
    """Fetch Facebook group

     Fetches the public About-page info for a Facebook group, such as its name, description, privacy, and
    member count.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookGroupDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookGroupDetailsResponse200 | FacebookGroupDetailsResponse400 | FacebookGroupDetailsResponse401 | FacebookGroupDetailsResponse402 | FacebookGroupDetailsResponse403 | FacebookGroupDetailsResponse404 | FacebookGroupDetailsResponse422 | FacebookGroupDetailsResponse429 | FacebookGroupDetailsResponse500 | FacebookGroupDetailsResponse503]
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
    body: FacebookGroupDetailsBody,
) -> (
    FacebookGroupDetailsResponse200
    | FacebookGroupDetailsResponse400
    | FacebookGroupDetailsResponse401
    | FacebookGroupDetailsResponse402
    | FacebookGroupDetailsResponse403
    | FacebookGroupDetailsResponse404
    | FacebookGroupDetailsResponse422
    | FacebookGroupDetailsResponse429
    | FacebookGroupDetailsResponse500
    | FacebookGroupDetailsResponse503
    | None
):
    """Fetch Facebook group

     Fetches the public About-page info for a Facebook group, such as its name, description, privacy, and
    member count.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookGroupDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookGroupDetailsResponse200 | FacebookGroupDetailsResponse400 | FacebookGroupDetailsResponse401 | FacebookGroupDetailsResponse402 | FacebookGroupDetailsResponse403 | FacebookGroupDetailsResponse404 | FacebookGroupDetailsResponse422 | FacebookGroupDetailsResponse429 | FacebookGroupDetailsResponse500 | FacebookGroupDetailsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookGroupDetailsBody,
) -> Response[
    FacebookGroupDetailsResponse200
    | FacebookGroupDetailsResponse400
    | FacebookGroupDetailsResponse401
    | FacebookGroupDetailsResponse402
    | FacebookGroupDetailsResponse403
    | FacebookGroupDetailsResponse404
    | FacebookGroupDetailsResponse422
    | FacebookGroupDetailsResponse429
    | FacebookGroupDetailsResponse500
    | FacebookGroupDetailsResponse503
]:
    """Fetch Facebook group

     Fetches the public About-page info for a Facebook group, such as its name, description, privacy, and
    member count.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookGroupDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FacebookGroupDetailsResponse200 | FacebookGroupDetailsResponse400 | FacebookGroupDetailsResponse401 | FacebookGroupDetailsResponse402 | FacebookGroupDetailsResponse403 | FacebookGroupDetailsResponse404 | FacebookGroupDetailsResponse422 | FacebookGroupDetailsResponse429 | FacebookGroupDetailsResponse500 | FacebookGroupDetailsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FacebookGroupDetailsBody,
) -> (
    FacebookGroupDetailsResponse200
    | FacebookGroupDetailsResponse400
    | FacebookGroupDetailsResponse401
    | FacebookGroupDetailsResponse402
    | FacebookGroupDetailsResponse403
    | FacebookGroupDetailsResponse404
    | FacebookGroupDetailsResponse422
    | FacebookGroupDetailsResponse429
    | FacebookGroupDetailsResponse500
    | FacebookGroupDetailsResponse503
    | None
):
    """Fetch Facebook group

     Fetches the public About-page info for a Facebook group, such as its name, description, privacy, and
    member count.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title="Pricing shown is default
    pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (FacebookGroupDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FacebookGroupDetailsResponse200 | FacebookGroupDetailsResponse400 | FacebookGroupDetailsResponse401 | FacebookGroupDetailsResponse402 | FacebookGroupDetailsResponse403 | FacebookGroupDetailsResponse404 | FacebookGroupDetailsResponse422 | FacebookGroupDetailsResponse429 | FacebookGroupDetailsResponse500 | FacebookGroupDetailsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
