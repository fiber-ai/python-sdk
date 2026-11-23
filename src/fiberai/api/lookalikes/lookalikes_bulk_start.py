from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lookalikes_bulk_start_body import LookalikesBulkStartBody
from ...models.lookalikes_bulk_start_response_200 import LookalikesBulkStartResponse200
from ...models.lookalikes_bulk_start_response_400 import LookalikesBulkStartResponse400
from ...models.lookalikes_bulk_start_response_401 import LookalikesBulkStartResponse401
from ...models.lookalikes_bulk_start_response_402 import LookalikesBulkStartResponse402
from ...models.lookalikes_bulk_start_response_403 import LookalikesBulkStartResponse403
from ...models.lookalikes_bulk_start_response_404 import LookalikesBulkStartResponse404
from ...models.lookalikes_bulk_start_response_422 import LookalikesBulkStartResponse422
from ...models.lookalikes_bulk_start_response_429 import LookalikesBulkStartResponse429
from ...models.lookalikes_bulk_start_response_500 import LookalikesBulkStartResponse500
from ...models.lookalikes_bulk_start_response_503 import LookalikesBulkStartResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: LookalikesBulkStartBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/lookalikes/bulk/start",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LookalikesBulkStartResponse200
    | LookalikesBulkStartResponse400
    | LookalikesBulkStartResponse401
    | LookalikesBulkStartResponse402
    | LookalikesBulkStartResponse403
    | LookalikesBulkStartResponse404
    | LookalikesBulkStartResponse422
    | LookalikesBulkStartResponse429
    | LookalikesBulkStartResponse500
    | LookalikesBulkStartResponse503
    | None
):
    if response.status_code == 200:
        response_200 = LookalikesBulkStartResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LookalikesBulkStartResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LookalikesBulkStartResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = LookalikesBulkStartResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = LookalikesBulkStartResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LookalikesBulkStartResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = LookalikesBulkStartResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = LookalikesBulkStartResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = LookalikesBulkStartResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = LookalikesBulkStartResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LookalikesBulkStartResponse200
    | LookalikesBulkStartResponse400
    | LookalikesBulkStartResponse401
    | LookalikesBulkStartResponse402
    | LookalikesBulkStartResponse403
    | LookalikesBulkStartResponse404
    | LookalikesBulkStartResponse422
    | LookalikesBulkStartResponse429
    | LookalikesBulkStartResponse500
    | LookalikesBulkStartResponse503
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
    body: LookalikesBulkStartBody,
) -> Response[
    LookalikesBulkStartResponse200
    | LookalikesBulkStartResponse400
    | LookalikesBulkStartResponse401
    | LookalikesBulkStartResponse402
    | LookalikesBulkStartResponse403
    | LookalikesBulkStartResponse404
    | LookalikesBulkStartResponse422
    | LookalikesBulkStartResponse429
    | LookalikesBulkStartResponse500
    | LookalikesBulkStartResponse503
]:
    """Start lookalike run

     Find companies similar to the ones you list, grouped by the patterns in it. Runs take a few minutes
    — poll /lookalikes/bulk/poll for progress and results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesBulkStartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookalikesBulkStartResponse200 | LookalikesBulkStartResponse400 | LookalikesBulkStartResponse401 | LookalikesBulkStartResponse402 | LookalikesBulkStartResponse403 | LookalikesBulkStartResponse404 | LookalikesBulkStartResponse422 | LookalikesBulkStartResponse429 | LookalikesBulkStartResponse500 | LookalikesBulkStartResponse503]
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
    body: LookalikesBulkStartBody,
) -> (
    LookalikesBulkStartResponse200
    | LookalikesBulkStartResponse400
    | LookalikesBulkStartResponse401
    | LookalikesBulkStartResponse402
    | LookalikesBulkStartResponse403
    | LookalikesBulkStartResponse404
    | LookalikesBulkStartResponse422
    | LookalikesBulkStartResponse429
    | LookalikesBulkStartResponse500
    | LookalikesBulkStartResponse503
    | None
):
    """Start lookalike run

     Find companies similar to the ones you list, grouped by the patterns in it. Runs take a few minutes
    — poll /lookalikes/bulk/poll for progress and results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesBulkStartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookalikesBulkStartResponse200 | LookalikesBulkStartResponse400 | LookalikesBulkStartResponse401 | LookalikesBulkStartResponse402 | LookalikesBulkStartResponse403 | LookalikesBulkStartResponse404 | LookalikesBulkStartResponse422 | LookalikesBulkStartResponse429 | LookalikesBulkStartResponse500 | LookalikesBulkStartResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LookalikesBulkStartBody,
) -> Response[
    LookalikesBulkStartResponse200
    | LookalikesBulkStartResponse400
    | LookalikesBulkStartResponse401
    | LookalikesBulkStartResponse402
    | LookalikesBulkStartResponse403
    | LookalikesBulkStartResponse404
    | LookalikesBulkStartResponse422
    | LookalikesBulkStartResponse429
    | LookalikesBulkStartResponse500
    | LookalikesBulkStartResponse503
]:
    """Start lookalike run

     Find companies similar to the ones you list, grouped by the patterns in it. Runs take a few minutes
    — poll /lookalikes/bulk/poll for progress and results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesBulkStartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookalikesBulkStartResponse200 | LookalikesBulkStartResponse400 | LookalikesBulkStartResponse401 | LookalikesBulkStartResponse402 | LookalikesBulkStartResponse403 | LookalikesBulkStartResponse404 | LookalikesBulkStartResponse422 | LookalikesBulkStartResponse429 | LookalikesBulkStartResponse500 | LookalikesBulkStartResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LookalikesBulkStartBody,
) -> (
    LookalikesBulkStartResponse200
    | LookalikesBulkStartResponse400
    | LookalikesBulkStartResponse401
    | LookalikesBulkStartResponse402
    | LookalikesBulkStartResponse403
    | LookalikesBulkStartResponse404
    | LookalikesBulkStartResponse422
    | LookalikesBulkStartResponse429
    | LookalikesBulkStartResponse500
    | LookalikesBulkStartResponse503
    | None
):
    """Start lookalike run

     Find companies similar to the ones you list, grouped by the patterns in it. Runs take a few minutes
    — poll /lookalikes/bulk/poll for progress and results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesBulkStartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookalikesBulkStartResponse200 | LookalikesBulkStartResponse400 | LookalikesBulkStartResponse401 | LookalikesBulkStartResponse402 | LookalikesBulkStartResponse403 | LookalikesBulkStartResponse404 | LookalikesBulkStartResponse422 | LookalikesBulkStartResponse429 | LookalikesBulkStartResponse500 | LookalikesBulkStartResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
