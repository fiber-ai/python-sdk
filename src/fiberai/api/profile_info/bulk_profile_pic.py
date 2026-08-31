from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_profile_pic_body import BulkProfilePicBody
from ...models.bulk_profile_pic_response_200 import BulkProfilePicResponse200
from ...models.bulk_profile_pic_response_400 import BulkProfilePicResponse400
from ...models.bulk_profile_pic_response_401 import BulkProfilePicResponse401
from ...models.bulk_profile_pic_response_402 import BulkProfilePicResponse402
from ...models.bulk_profile_pic_response_403 import BulkProfilePicResponse403
from ...models.bulk_profile_pic_response_404 import BulkProfilePicResponse404
from ...models.bulk_profile_pic_response_422 import BulkProfilePicResponse422
from ...models.bulk_profile_pic_response_429 import BulkProfilePicResponse429
from ...models.bulk_profile_pic_response_500 import BulkProfilePicResponse500
from ...models.bulk_profile_pic_response_503 import BulkProfilePicResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: BulkProfilePicBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/profile-pic/bulk",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BulkProfilePicResponse200
    | BulkProfilePicResponse400
    | BulkProfilePicResponse401
    | BulkProfilePicResponse402
    | BulkProfilePicResponse403
    | BulkProfilePicResponse404
    | BulkProfilePicResponse422
    | BulkProfilePicResponse429
    | BulkProfilePicResponse500
    | BulkProfilePicResponse503
    | None
):
    if response.status_code == 200:
        response_200 = BulkProfilePicResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BulkProfilePicResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BulkProfilePicResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = BulkProfilePicResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = BulkProfilePicResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = BulkProfilePicResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = BulkProfilePicResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = BulkProfilePicResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = BulkProfilePicResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = BulkProfilePicResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BulkProfilePicResponse200
    | BulkProfilePicResponse400
    | BulkProfilePicResponse401
    | BulkProfilePicResponse402
    | BulkProfilePicResponse403
    | BulkProfilePicResponse404
    | BulkProfilePicResponse422
    | BulkProfilePicResponse429
    | BulkProfilePicResponse500
    | BulkProfilePicResponse503
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
    body: BulkProfilePicBody,
) -> Response[
    BulkProfilePicResponse200
    | BulkProfilePicResponse400
    | BulkProfilePicResponse401
    | BulkProfilePicResponse402
    | BulkProfilePicResponse403
    | BulkProfilePicResponse404
    | BulkProfilePicResponse422
    | BulkProfilePicResponse429
    | BulkProfilePicResponse500
    | BulkProfilePicResponse503
]:
    """Bulk profile pics

     Get profile pics for a list of profiles. Max 10,000 profiles can be looked up at a time.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per profile pic lookup&nbsp;<span title="Pricing shown
    is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BulkProfilePicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkProfilePicResponse200 | BulkProfilePicResponse400 | BulkProfilePicResponse401 | BulkProfilePicResponse402 | BulkProfilePicResponse403 | BulkProfilePicResponse404 | BulkProfilePicResponse422 | BulkProfilePicResponse429 | BulkProfilePicResponse500 | BulkProfilePicResponse503]
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
    body: BulkProfilePicBody,
) -> (
    BulkProfilePicResponse200
    | BulkProfilePicResponse400
    | BulkProfilePicResponse401
    | BulkProfilePicResponse402
    | BulkProfilePicResponse403
    | BulkProfilePicResponse404
    | BulkProfilePicResponse422
    | BulkProfilePicResponse429
    | BulkProfilePicResponse500
    | BulkProfilePicResponse503
    | None
):
    """Bulk profile pics

     Get profile pics for a list of profiles. Max 10,000 profiles can be looked up at a time.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per profile pic lookup&nbsp;<span title="Pricing shown
    is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BulkProfilePicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkProfilePicResponse200 | BulkProfilePicResponse400 | BulkProfilePicResponse401 | BulkProfilePicResponse402 | BulkProfilePicResponse403 | BulkProfilePicResponse404 | BulkProfilePicResponse422 | BulkProfilePicResponse429 | BulkProfilePicResponse500 | BulkProfilePicResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkProfilePicBody,
) -> Response[
    BulkProfilePicResponse200
    | BulkProfilePicResponse400
    | BulkProfilePicResponse401
    | BulkProfilePicResponse402
    | BulkProfilePicResponse403
    | BulkProfilePicResponse404
    | BulkProfilePicResponse422
    | BulkProfilePicResponse429
    | BulkProfilePicResponse500
    | BulkProfilePicResponse503
]:
    """Bulk profile pics

     Get profile pics for a list of profiles. Max 10,000 profiles can be looked up at a time.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per profile pic lookup&nbsp;<span title="Pricing shown
    is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BulkProfilePicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkProfilePicResponse200 | BulkProfilePicResponse400 | BulkProfilePicResponse401 | BulkProfilePicResponse402 | BulkProfilePicResponse403 | BulkProfilePicResponse404 | BulkProfilePicResponse422 | BulkProfilePicResponse429 | BulkProfilePicResponse500 | BulkProfilePicResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkProfilePicBody,
) -> (
    BulkProfilePicResponse200
    | BulkProfilePicResponse400
    | BulkProfilePicResponse401
    | BulkProfilePicResponse402
    | BulkProfilePicResponse403
    | BulkProfilePicResponse404
    | BulkProfilePicResponse422
    | BulkProfilePicResponse429
    | BulkProfilePicResponse500
    | BulkProfilePicResponse503
    | None
):
    """Bulk profile pics

     Get profile pics for a list of profiles. Max 10,000 profiles can be looked up at a time.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per profile pic lookup&nbsp;<span title="Pricing shown
    is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (BulkProfilePicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkProfilePicResponse200 | BulkProfilePicResponse400 | BulkProfilePicResponse401 | BulkProfilePicResponse402 | BulkProfilePicResponse403 | BulkProfilePicResponse404 | BulkProfilePicResponse422 | BulkProfilePicResponse429 | BulkProfilePicResponse500 | BulkProfilePicResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
