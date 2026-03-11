from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.profile_live_enrich_body import ProfileLiveEnrichBody
from ...models.profile_live_enrich_response_200 import ProfileLiveEnrichResponse200
from ...models.profile_live_enrich_response_400 import ProfileLiveEnrichResponse400
from ...models.profile_live_enrich_response_401 import ProfileLiveEnrichResponse401
from ...models.profile_live_enrich_response_402 import ProfileLiveEnrichResponse402
from ...models.profile_live_enrich_response_403 import ProfileLiveEnrichResponse403
from ...models.profile_live_enrich_response_404 import ProfileLiveEnrichResponse404
from ...models.profile_live_enrich_response_429 import ProfileLiveEnrichResponse429
from ...models.profile_live_enrich_response_500 import ProfileLiveEnrichResponse500
from ...models.profile_live_enrich_response_503 import ProfileLiveEnrichResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ProfileLiveEnrichBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/profile/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProfileLiveEnrichResponse200
    | ProfileLiveEnrichResponse400
    | ProfileLiveEnrichResponse401
    | ProfileLiveEnrichResponse402
    | ProfileLiveEnrichResponse403
    | ProfileLiveEnrichResponse404
    | ProfileLiveEnrichResponse429
    | ProfileLiveEnrichResponse500
    | ProfileLiveEnrichResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ProfileLiveEnrichResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProfileLiveEnrichResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfileLiveEnrichResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ProfileLiveEnrichResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ProfileLiveEnrichResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProfileLiveEnrichResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ProfileLiveEnrichResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ProfileLiveEnrichResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ProfileLiveEnrichResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProfileLiveEnrichResponse200
    | ProfileLiveEnrichResponse400
    | ProfileLiveEnrichResponse401
    | ProfileLiveEnrichResponse402
    | ProfileLiveEnrichResponse403
    | ProfileLiveEnrichResponse404
    | ProfileLiveEnrichResponse429
    | ProfileLiveEnrichResponse500
    | ProfileLiveEnrichResponse503
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
    body: ProfileLiveEnrichBody,
) -> Response[
    ProfileLiveEnrichResponse200
    | ProfileLiveEnrichResponse400
    | ProfileLiveEnrichResponse401
    | ProfileLiveEnrichResponse402
    | ProfileLiveEnrichResponse403
    | ProfileLiveEnrichResponse404
    | ProfileLiveEnrichResponse429
    | ProfileLiveEnrichResponse500
    | ProfileLiveEnrichResponse503
]:
    r"""Live fetch LinkedIn profile

     Returns an enriched profile with details for a given LinkedIn profile identifier

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 second</span>

    <span>💰 <strong>Cost:</strong> 2 credits per profile live fetch&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileLiveEnrichResponse200 | ProfileLiveEnrichResponse400 | ProfileLiveEnrichResponse401 | ProfileLiveEnrichResponse402 | ProfileLiveEnrichResponse403 | ProfileLiveEnrichResponse404 | ProfileLiveEnrichResponse429 | ProfileLiveEnrichResponse500 | ProfileLiveEnrichResponse503]
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
    body: ProfileLiveEnrichBody,
) -> (
    ProfileLiveEnrichResponse200
    | ProfileLiveEnrichResponse400
    | ProfileLiveEnrichResponse401
    | ProfileLiveEnrichResponse402
    | ProfileLiveEnrichResponse403
    | ProfileLiveEnrichResponse404
    | ProfileLiveEnrichResponse429
    | ProfileLiveEnrichResponse500
    | ProfileLiveEnrichResponse503
    | None
):
    r"""Live fetch LinkedIn profile

     Returns an enriched profile with details for a given LinkedIn profile identifier

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 second</span>

    <span>💰 <strong>Cost:</strong> 2 credits per profile live fetch&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileLiveEnrichResponse200 | ProfileLiveEnrichResponse400 | ProfileLiveEnrichResponse401 | ProfileLiveEnrichResponse402 | ProfileLiveEnrichResponse403 | ProfileLiveEnrichResponse404 | ProfileLiveEnrichResponse429 | ProfileLiveEnrichResponse500 | ProfileLiveEnrichResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProfileLiveEnrichBody,
) -> Response[
    ProfileLiveEnrichResponse200
    | ProfileLiveEnrichResponse400
    | ProfileLiveEnrichResponse401
    | ProfileLiveEnrichResponse402
    | ProfileLiveEnrichResponse403
    | ProfileLiveEnrichResponse404
    | ProfileLiveEnrichResponse429
    | ProfileLiveEnrichResponse500
    | ProfileLiveEnrichResponse503
]:
    r"""Live fetch LinkedIn profile

     Returns an enriched profile with details for a given LinkedIn profile identifier

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 second</span>

    <span>💰 <strong>Cost:</strong> 2 credits per profile live fetch&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileLiveEnrichResponse200 | ProfileLiveEnrichResponse400 | ProfileLiveEnrichResponse401 | ProfileLiveEnrichResponse402 | ProfileLiveEnrichResponse403 | ProfileLiveEnrichResponse404 | ProfileLiveEnrichResponse429 | ProfileLiveEnrichResponse500 | ProfileLiveEnrichResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ProfileLiveEnrichBody,
) -> (
    ProfileLiveEnrichResponse200
    | ProfileLiveEnrichResponse400
    | ProfileLiveEnrichResponse401
    | ProfileLiveEnrichResponse402
    | ProfileLiveEnrichResponse403
    | ProfileLiveEnrichResponse404
    | ProfileLiveEnrichResponse429
    | ProfileLiveEnrichResponse500
    | ProfileLiveEnrichResponse503
    | None
):
    r"""Live fetch LinkedIn profile

     Returns an enriched profile with details for a given LinkedIn profile identifier

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 second</span>

    <span>💰 <strong>Cost:</strong> 2 credits per profile live fetch&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ProfileLiveEnrichBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileLiveEnrichResponse200 | ProfileLiveEnrichResponse400 | ProfileLiveEnrichResponse401 | ProfileLiveEnrichResponse402 | ProfileLiveEnrichResponse403 | ProfileLiveEnrichResponse404 | ProfileLiveEnrichResponse429 | ProfileLiveEnrichResponse500 | ProfileLiveEnrichResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
