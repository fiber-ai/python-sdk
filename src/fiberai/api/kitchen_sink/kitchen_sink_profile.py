from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.kitchen_sink_profile_body import KitchenSinkProfileBody
from ...models.kitchen_sink_profile_response_200 import KitchenSinkProfileResponse200
from ...models.kitchen_sink_profile_response_400 import KitchenSinkProfileResponse400
from ...models.kitchen_sink_profile_response_401 import KitchenSinkProfileResponse401
from ...models.kitchen_sink_profile_response_402 import KitchenSinkProfileResponse402
from ...models.kitchen_sink_profile_response_403 import KitchenSinkProfileResponse403
from ...models.kitchen_sink_profile_response_404 import KitchenSinkProfileResponse404
from ...models.kitchen_sink_profile_response_429 import KitchenSinkProfileResponse429
from ...models.kitchen_sink_profile_response_500 import KitchenSinkProfileResponse500
from ...models.kitchen_sink_profile_response_503 import KitchenSinkProfileResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: KitchenSinkProfileBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/kitchen-sink/person",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    KitchenSinkProfileResponse200
    | KitchenSinkProfileResponse400
    | KitchenSinkProfileResponse401
    | KitchenSinkProfileResponse402
    | KitchenSinkProfileResponse403
    | KitchenSinkProfileResponse404
    | KitchenSinkProfileResponse429
    | KitchenSinkProfileResponse500
    | KitchenSinkProfileResponse503
    | None
):
    if response.status_code == 200:
        response_200 = KitchenSinkProfileResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = KitchenSinkProfileResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = KitchenSinkProfileResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = KitchenSinkProfileResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = KitchenSinkProfileResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = KitchenSinkProfileResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = KitchenSinkProfileResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = KitchenSinkProfileResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = KitchenSinkProfileResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    KitchenSinkProfileResponse200
    | KitchenSinkProfileResponse400
    | KitchenSinkProfileResponse401
    | KitchenSinkProfileResponse402
    | KitchenSinkProfileResponse403
    | KitchenSinkProfileResponse404
    | KitchenSinkProfileResponse429
    | KitchenSinkProfileResponse500
    | KitchenSinkProfileResponse503
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
    body: KitchenSinkProfileBody,
) -> Response[
    KitchenSinkProfileResponse200
    | KitchenSinkProfileResponse400
    | KitchenSinkProfileResponse401
    | KitchenSinkProfileResponse402
    | KitchenSinkProfileResponse403
    | KitchenSinkProfileResponse404
    | KitchenSinkProfileResponse429
    | KitchenSinkProfileResponse500
    | KitchenSinkProfileResponse503
]:
    r"""Kitchen sink person lookup

     Search for a person using a variety of parameters such as LinkedIn slug, LinkedIn URL, or their
    current company information. Returns profile data for the person if found.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay per person: 2 credits per lookup, plus 2 additional credits when
    the liveFetch flag is set.&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary. LinkedIn live fetch credits only apply when the liveFetch flag is set.\">ⓘ</span></span>

    Args:
        body (KitchenSinkProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KitchenSinkProfileResponse200 | KitchenSinkProfileResponse400 | KitchenSinkProfileResponse401 | KitchenSinkProfileResponse402 | KitchenSinkProfileResponse403 | KitchenSinkProfileResponse404 | KitchenSinkProfileResponse429 | KitchenSinkProfileResponse500 | KitchenSinkProfileResponse503]
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
    body: KitchenSinkProfileBody,
) -> (
    KitchenSinkProfileResponse200
    | KitchenSinkProfileResponse400
    | KitchenSinkProfileResponse401
    | KitchenSinkProfileResponse402
    | KitchenSinkProfileResponse403
    | KitchenSinkProfileResponse404
    | KitchenSinkProfileResponse429
    | KitchenSinkProfileResponse500
    | KitchenSinkProfileResponse503
    | None
):
    r"""Kitchen sink person lookup

     Search for a person using a variety of parameters such as LinkedIn slug, LinkedIn URL, or their
    current company information. Returns profile data for the person if found.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay per person: 2 credits per lookup, plus 2 additional credits when
    the liveFetch flag is set.&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary. LinkedIn live fetch credits only apply when the liveFetch flag is set.\">ⓘ</span></span>

    Args:
        body (KitchenSinkProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KitchenSinkProfileResponse200 | KitchenSinkProfileResponse400 | KitchenSinkProfileResponse401 | KitchenSinkProfileResponse402 | KitchenSinkProfileResponse403 | KitchenSinkProfileResponse404 | KitchenSinkProfileResponse429 | KitchenSinkProfileResponse500 | KitchenSinkProfileResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KitchenSinkProfileBody,
) -> Response[
    KitchenSinkProfileResponse200
    | KitchenSinkProfileResponse400
    | KitchenSinkProfileResponse401
    | KitchenSinkProfileResponse402
    | KitchenSinkProfileResponse403
    | KitchenSinkProfileResponse404
    | KitchenSinkProfileResponse429
    | KitchenSinkProfileResponse500
    | KitchenSinkProfileResponse503
]:
    r"""Kitchen sink person lookup

     Search for a person using a variety of parameters such as LinkedIn slug, LinkedIn URL, or their
    current company information. Returns profile data for the person if found.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay per person: 2 credits per lookup, plus 2 additional credits when
    the liveFetch flag is set.&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary. LinkedIn live fetch credits only apply when the liveFetch flag is set.\">ⓘ</span></span>

    Args:
        body (KitchenSinkProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KitchenSinkProfileResponse200 | KitchenSinkProfileResponse400 | KitchenSinkProfileResponse401 | KitchenSinkProfileResponse402 | KitchenSinkProfileResponse403 | KitchenSinkProfileResponse404 | KitchenSinkProfileResponse429 | KitchenSinkProfileResponse500 | KitchenSinkProfileResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: KitchenSinkProfileBody,
) -> (
    KitchenSinkProfileResponse200
    | KitchenSinkProfileResponse400
    | KitchenSinkProfileResponse401
    | KitchenSinkProfileResponse402
    | KitchenSinkProfileResponse403
    | KitchenSinkProfileResponse404
    | KitchenSinkProfileResponse429
    | KitchenSinkProfileResponse500
    | KitchenSinkProfileResponse503
    | None
):
    r"""Kitchen sink person lookup

     Search for a person using a variety of parameters such as LinkedIn slug, LinkedIn URL, or their
    current company information. Returns profile data for the person if found.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Pay per person: 2 credits per lookup, plus 2 additional credits when
    the liveFetch flag is set.&nbsp;<span title=\"Pricing shown is default pricing. Actual pricing may
    vary. LinkedIn live fetch credits only apply when the liveFetch flag is set.\">ⓘ</span></span>

    Args:
        body (KitchenSinkProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KitchenSinkProfileResponse200 | KitchenSinkProfileResponse400 | KitchenSinkProfileResponse401 | KitchenSinkProfileResponse402 | KitchenSinkProfileResponse403 | KitchenSinkProfileResponse404 | KitchenSinkProfileResponse429 | KitchenSinkProfileResponse500 | KitchenSinkProfileResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
