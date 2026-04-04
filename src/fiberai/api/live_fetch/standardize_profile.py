from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.standardize_profile_body import StandardizeProfileBody
from ...models.standardize_profile_response_200 import StandardizeProfileResponse200
from ...models.standardize_profile_response_400 import StandardizeProfileResponse400
from ...models.standardize_profile_response_401 import StandardizeProfileResponse401
from ...models.standardize_profile_response_402 import StandardizeProfileResponse402
from ...models.standardize_profile_response_403 import StandardizeProfileResponse403
from ...models.standardize_profile_response_404 import StandardizeProfileResponse404
from ...models.standardize_profile_response_429 import StandardizeProfileResponse429
from ...models.standardize_profile_response_500 import StandardizeProfileResponse500
from ...models.standardize_profile_response_503 import StandardizeProfileResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: StandardizeProfileBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/standardize/profile/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StandardizeProfileResponse200
    | StandardizeProfileResponse400
    | StandardizeProfileResponse401
    | StandardizeProfileResponse402
    | StandardizeProfileResponse403
    | StandardizeProfileResponse404
    | StandardizeProfileResponse429
    | StandardizeProfileResponse500
    | StandardizeProfileResponse503
    | None
):
    if response.status_code == 200:
        response_200 = StandardizeProfileResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StandardizeProfileResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StandardizeProfileResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = StandardizeProfileResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = StandardizeProfileResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StandardizeProfileResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = StandardizeProfileResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = StandardizeProfileResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = StandardizeProfileResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StandardizeProfileResponse200
    | StandardizeProfileResponse400
    | StandardizeProfileResponse401
    | StandardizeProfileResponse402
    | StandardizeProfileResponse403
    | StandardizeProfileResponse404
    | StandardizeProfileResponse429
    | StandardizeProfileResponse500
    | StandardizeProfileResponse503
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
    body: StandardizeProfileBody,
) -> Response[
    StandardizeProfileResponse200
    | StandardizeProfileResponse400
    | StandardizeProfileResponse401
    | StandardizeProfileResponse402
    | StandardizeProfileResponse403
    | StandardizeProfileResponse404
    | StandardizeProfileResponse429
    | StandardizeProfileResponse500
    | StandardizeProfileResponse503
]:
    r"""Standardize LinkedIn profile entity URN

     Resolves a LinkedIn entity URN to a proper LinkedIn profile URL. Supports a variety of URN formats
    from different LinkedIn sources (including ACoAA... and ACwAA... prefixes). Accepts either a raw
    entity URN or a full LinkedIn URL containing an entity URN in the slug position (e.g.,
    'https://www.linkedin.com/in/ACoAADVMtbkB...').

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per profile standardization&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (StandardizeProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StandardizeProfileResponse200 | StandardizeProfileResponse400 | StandardizeProfileResponse401 | StandardizeProfileResponse402 | StandardizeProfileResponse403 | StandardizeProfileResponse404 | StandardizeProfileResponse429 | StandardizeProfileResponse500 | StandardizeProfileResponse503]
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
    body: StandardizeProfileBody,
) -> (
    StandardizeProfileResponse200
    | StandardizeProfileResponse400
    | StandardizeProfileResponse401
    | StandardizeProfileResponse402
    | StandardizeProfileResponse403
    | StandardizeProfileResponse404
    | StandardizeProfileResponse429
    | StandardizeProfileResponse500
    | StandardizeProfileResponse503
    | None
):
    r"""Standardize LinkedIn profile entity URN

     Resolves a LinkedIn entity URN to a proper LinkedIn profile URL. Supports a variety of URN formats
    from different LinkedIn sources (including ACoAA... and ACwAA... prefixes). Accepts either a raw
    entity URN or a full LinkedIn URL containing an entity URN in the slug position (e.g.,
    'https://www.linkedin.com/in/ACoAADVMtbkB...').

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per profile standardization&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (StandardizeProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StandardizeProfileResponse200 | StandardizeProfileResponse400 | StandardizeProfileResponse401 | StandardizeProfileResponse402 | StandardizeProfileResponse403 | StandardizeProfileResponse404 | StandardizeProfileResponse429 | StandardizeProfileResponse500 | StandardizeProfileResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StandardizeProfileBody,
) -> Response[
    StandardizeProfileResponse200
    | StandardizeProfileResponse400
    | StandardizeProfileResponse401
    | StandardizeProfileResponse402
    | StandardizeProfileResponse403
    | StandardizeProfileResponse404
    | StandardizeProfileResponse429
    | StandardizeProfileResponse500
    | StandardizeProfileResponse503
]:
    r"""Standardize LinkedIn profile entity URN

     Resolves a LinkedIn entity URN to a proper LinkedIn profile URL. Supports a variety of URN formats
    from different LinkedIn sources (including ACoAA... and ACwAA... prefixes). Accepts either a raw
    entity URN or a full LinkedIn URL containing an entity URN in the slug position (e.g.,
    'https://www.linkedin.com/in/ACoAADVMtbkB...').

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per profile standardization&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (StandardizeProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StandardizeProfileResponse200 | StandardizeProfileResponse400 | StandardizeProfileResponse401 | StandardizeProfileResponse402 | StandardizeProfileResponse403 | StandardizeProfileResponse404 | StandardizeProfileResponse429 | StandardizeProfileResponse500 | StandardizeProfileResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StandardizeProfileBody,
) -> (
    StandardizeProfileResponse200
    | StandardizeProfileResponse400
    | StandardizeProfileResponse401
    | StandardizeProfileResponse402
    | StandardizeProfileResponse403
    | StandardizeProfileResponse404
    | StandardizeProfileResponse429
    | StandardizeProfileResponse500
    | StandardizeProfileResponse503
    | None
):
    r"""Standardize LinkedIn profile entity URN

     Resolves a LinkedIn entity URN to a proper LinkedIn profile URL. Supports a variety of URN formats
    from different LinkedIn sources (including ACoAA... and ACwAA... prefixes). Accepts either a raw
    entity URN or a full LinkedIn URL containing an entity URN in the slug position (e.g.,
    'https://www.linkedin.com/in/ACoAADVMtbkB...').

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per profile standardization&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (StandardizeProfileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StandardizeProfileResponse200 | StandardizeProfileResponse400 | StandardizeProfileResponse401 | StandardizeProfileResponse402 | StandardizeProfileResponse403 | StandardizeProfileResponse404 | StandardizeProfileResponse429 | StandardizeProfileResponse500 | StandardizeProfileResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
