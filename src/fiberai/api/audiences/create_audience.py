from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_audience_body import CreateAudienceBody
from ...models.create_audience_response_200 import CreateAudienceResponse200
from ...models.create_audience_response_400 import CreateAudienceResponse400
from ...models.create_audience_response_401 import CreateAudienceResponse401
from ...models.create_audience_response_402 import CreateAudienceResponse402
from ...models.create_audience_response_403 import CreateAudienceResponse403
from ...models.create_audience_response_404 import CreateAudienceResponse404
from ...models.create_audience_response_429 import CreateAudienceResponse429
from ...models.create_audience_response_500 import CreateAudienceResponse500
from ...models.create_audience_response_503 import CreateAudienceResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAudienceBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/audiences/create",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateAudienceResponse200
    | CreateAudienceResponse400
    | CreateAudienceResponse401
    | CreateAudienceResponse402
    | CreateAudienceResponse403
    | CreateAudienceResponse404
    | CreateAudienceResponse429
    | CreateAudienceResponse500
    | CreateAudienceResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CreateAudienceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateAudienceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateAudienceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CreateAudienceResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CreateAudienceResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateAudienceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CreateAudienceResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateAudienceResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreateAudienceResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateAudienceResponse200
    | CreateAudienceResponse400
    | CreateAudienceResponse401
    | CreateAudienceResponse402
    | CreateAudienceResponse403
    | CreateAudienceResponse404
    | CreateAudienceResponse429
    | CreateAudienceResponse500
    | CreateAudienceResponse503
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
    body: CreateAudienceBody,
) -> Response[
    CreateAudienceResponse200
    | CreateAudienceResponse400
    | CreateAudienceResponse401
    | CreateAudienceResponse402
    | CreateAudienceResponse403
    | CreateAudienceResponse404
    | CreateAudienceResponse429
    | CreateAudienceResponse500
    | CreateAudienceResponse503
]:
    r"""Create a new audience

     Creates a new audience in DRAFT status. After creation, use the update-search-params endpoint to set
    filters, then use the build endpoint to populate the audience with companies and prospects from
    Elasticsearch.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAudienceResponse200 | CreateAudienceResponse400 | CreateAudienceResponse401 | CreateAudienceResponse402 | CreateAudienceResponse403 | CreateAudienceResponse404 | CreateAudienceResponse429 | CreateAudienceResponse500 | CreateAudienceResponse503]
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
    body: CreateAudienceBody,
) -> (
    CreateAudienceResponse200
    | CreateAudienceResponse400
    | CreateAudienceResponse401
    | CreateAudienceResponse402
    | CreateAudienceResponse403
    | CreateAudienceResponse404
    | CreateAudienceResponse429
    | CreateAudienceResponse500
    | CreateAudienceResponse503
    | None
):
    r"""Create a new audience

     Creates a new audience in DRAFT status. After creation, use the update-search-params endpoint to set
    filters, then use the build endpoint to populate the audience with companies and prospects from
    Elasticsearch.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAudienceResponse200 | CreateAudienceResponse400 | CreateAudienceResponse401 | CreateAudienceResponse402 | CreateAudienceResponse403 | CreateAudienceResponse404 | CreateAudienceResponse429 | CreateAudienceResponse500 | CreateAudienceResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAudienceBody,
) -> Response[
    CreateAudienceResponse200
    | CreateAudienceResponse400
    | CreateAudienceResponse401
    | CreateAudienceResponse402
    | CreateAudienceResponse403
    | CreateAudienceResponse404
    | CreateAudienceResponse429
    | CreateAudienceResponse500
    | CreateAudienceResponse503
]:
    r"""Create a new audience

     Creates a new audience in DRAFT status. After creation, use the update-search-params endpoint to set
    filters, then use the build endpoint to populate the audience with companies and prospects from
    Elasticsearch.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAudienceResponse200 | CreateAudienceResponse400 | CreateAudienceResponse401 | CreateAudienceResponse402 | CreateAudienceResponse403 | CreateAudienceResponse404 | CreateAudienceResponse429 | CreateAudienceResponse500 | CreateAudienceResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAudienceBody,
) -> (
    CreateAudienceResponse200
    | CreateAudienceResponse400
    | CreateAudienceResponse401
    | CreateAudienceResponse402
    | CreateAudienceResponse403
    | CreateAudienceResponse404
    | CreateAudienceResponse429
    | CreateAudienceResponse500
    | CreateAudienceResponse503
    | None
):
    r"""Create a new audience

     Creates a new audience in DRAFT status. After creation, use the update-search-params endpoint to set
    filters, then use the build endpoint to populate the audience with companies and prospects from
    Elasticsearch.

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CreateAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAudienceResponse200 | CreateAudienceResponse400 | CreateAudienceResponse401 | CreateAudienceResponse402 | CreateAudienceResponse403 | CreateAudienceResponse404 | CreateAudienceResponse429 | CreateAudienceResponse500 | CreateAudienceResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
