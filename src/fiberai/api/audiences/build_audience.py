from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.build_audience_body import BuildAudienceBody
from ...models.build_audience_response_200 import BuildAudienceResponse200
from ...models.build_audience_response_400 import BuildAudienceResponse400
from ...models.build_audience_response_401 import BuildAudienceResponse401
from ...models.build_audience_response_402 import BuildAudienceResponse402
from ...models.build_audience_response_403 import BuildAudienceResponse403
from ...models.build_audience_response_404 import BuildAudienceResponse404
from ...models.build_audience_response_429 import BuildAudienceResponse429
from ...models.build_audience_response_500 import BuildAudienceResponse500
from ...models.build_audience_response_503 import BuildAudienceResponse503
from ...types import Response


def _get_kwargs(
    audience_id: str,
    *,
    body: BuildAudienceBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/audiences/{audience_id}/build".format(
            audience_id=quote(str(audience_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BuildAudienceResponse200
    | BuildAudienceResponse400
    | BuildAudienceResponse401
    | BuildAudienceResponse402
    | BuildAudienceResponse403
    | BuildAudienceResponse404
    | BuildAudienceResponse429
    | BuildAudienceResponse500
    | BuildAudienceResponse503
    | None
):
    if response.status_code == 200:
        response_200 = BuildAudienceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BuildAudienceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BuildAudienceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = BuildAudienceResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = BuildAudienceResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = BuildAudienceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = BuildAudienceResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = BuildAudienceResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = BuildAudienceResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BuildAudienceResponse200
    | BuildAudienceResponse400
    | BuildAudienceResponse401
    | BuildAudienceResponse402
    | BuildAudienceResponse403
    | BuildAudienceResponse404
    | BuildAudienceResponse429
    | BuildAudienceResponse500
    | BuildAudienceResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BuildAudienceBody,
) -> Response[
    BuildAudienceResponse200
    | BuildAudienceResponse400
    | BuildAudienceResponse401
    | BuildAudienceResponse402
    | BuildAudienceResponse403
    | BuildAudienceResponse404
    | BuildAudienceResponse429
    | BuildAudienceResponse500
    | BuildAudienceResponse503
]:
    r"""Build audience from search parameters

     Triggers the audience building process. This runs a company and prospect search based on the
    configured search parameters and saves results to the database. The build runs asynchronously - use
    the get-audience-status endpoint to poll for completion. Status transitions: DRAFT → BUILDING →
    NORMAL (success) or FAILED (error).

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the build completes based on results: 1
    credits per company and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary. Your total charge will vary based on the number of companies and
    profiles in your audience.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (BuildAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuildAudienceResponse200 | BuildAudienceResponse400 | BuildAudienceResponse401 | BuildAudienceResponse402 | BuildAudienceResponse403 | BuildAudienceResponse404 | BuildAudienceResponse429 | BuildAudienceResponse500 | BuildAudienceResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BuildAudienceBody,
) -> (
    BuildAudienceResponse200
    | BuildAudienceResponse400
    | BuildAudienceResponse401
    | BuildAudienceResponse402
    | BuildAudienceResponse403
    | BuildAudienceResponse404
    | BuildAudienceResponse429
    | BuildAudienceResponse500
    | BuildAudienceResponse503
    | None
):
    r"""Build audience from search parameters

     Triggers the audience building process. This runs a company and prospect search based on the
    configured search parameters and saves results to the database. The build runs asynchronously - use
    the get-audience-status endpoint to poll for completion. Status transitions: DRAFT → BUILDING →
    NORMAL (success) or FAILED (error).

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the build completes based on results: 1
    credits per company and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary. Your total charge will vary based on the number of companies and
    profiles in your audience.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (BuildAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuildAudienceResponse200 | BuildAudienceResponse400 | BuildAudienceResponse401 | BuildAudienceResponse402 | BuildAudienceResponse403 | BuildAudienceResponse404 | BuildAudienceResponse429 | BuildAudienceResponse500 | BuildAudienceResponse503
    """

    return sync_detailed(
        audience_id=audience_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BuildAudienceBody,
) -> Response[
    BuildAudienceResponse200
    | BuildAudienceResponse400
    | BuildAudienceResponse401
    | BuildAudienceResponse402
    | BuildAudienceResponse403
    | BuildAudienceResponse404
    | BuildAudienceResponse429
    | BuildAudienceResponse500
    | BuildAudienceResponse503
]:
    r"""Build audience from search parameters

     Triggers the audience building process. This runs a company and prospect search based on the
    configured search parameters and saves results to the database. The build runs asynchronously - use
    the get-audience-status endpoint to poll for completion. Status transitions: DRAFT → BUILDING →
    NORMAL (success) or FAILED (error).

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the build completes based on results: 1
    credits per company and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary. Your total charge will vary based on the number of companies and
    profiles in your audience.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (BuildAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuildAudienceResponse200 | BuildAudienceResponse400 | BuildAudienceResponse401 | BuildAudienceResponse402 | BuildAudienceResponse403 | BuildAudienceResponse404 | BuildAudienceResponse429 | BuildAudienceResponse500 | BuildAudienceResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BuildAudienceBody,
) -> (
    BuildAudienceResponse200
    | BuildAudienceResponse400
    | BuildAudienceResponse401
    | BuildAudienceResponse402
    | BuildAudienceResponse403
    | BuildAudienceResponse404
    | BuildAudienceResponse429
    | BuildAudienceResponse500
    | BuildAudienceResponse503
    | None
):
    r"""Build audience from search parameters

     Triggers the audience building process. This runs a company and prospect search based on the
    configured search parameters and saves results to the database. The build runs asynchronously - use
    the get-audience-status endpoint to poll for completion. Status transitions: DRAFT → BUILDING →
    NORMAL (success) or FAILED (error).

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Credits are charged after the build completes based on results: 1
    credits per company and 1 credits per profile found.&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary. Your total charge will vary based on the number of companies and
    profiles in your audience.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (BuildAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuildAudienceResponse200 | BuildAudienceResponse400 | BuildAudienceResponse401 | BuildAudienceResponse402 | BuildAudienceResponse403 | BuildAudienceResponse404 | BuildAudienceResponse429 | BuildAudienceResponse500 | BuildAudienceResponse503
    """

    return (
        await asyncio_detailed(
            audience_id=audience_id,
            client=client,
            body=body,
        )
    ).parsed
