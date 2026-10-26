from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lookalikes_poll_body import LookalikesPollBody
from ...models.lookalikes_poll_response_200 import LookalikesPollResponse200
from ...models.lookalikes_poll_response_400 import LookalikesPollResponse400
from ...models.lookalikes_poll_response_401 import LookalikesPollResponse401
from ...models.lookalikes_poll_response_402 import LookalikesPollResponse402
from ...models.lookalikes_poll_response_403 import LookalikesPollResponse403
from ...models.lookalikes_poll_response_404 import LookalikesPollResponse404
from ...models.lookalikes_poll_response_422 import LookalikesPollResponse422
from ...models.lookalikes_poll_response_429 import LookalikesPollResponse429
from ...models.lookalikes_poll_response_500 import LookalikesPollResponse500
from ...models.lookalikes_poll_response_503 import LookalikesPollResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: LookalikesPollBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/lookalikes/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LookalikesPollResponse200
    | LookalikesPollResponse400
    | LookalikesPollResponse401
    | LookalikesPollResponse402
    | LookalikesPollResponse403
    | LookalikesPollResponse404
    | LookalikesPollResponse422
    | LookalikesPollResponse429
    | LookalikesPollResponse500
    | LookalikesPollResponse503
    | None
):
    if response.status_code == 200:
        response_200 = LookalikesPollResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LookalikesPollResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LookalikesPollResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = LookalikesPollResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = LookalikesPollResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LookalikesPollResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = LookalikesPollResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = LookalikesPollResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = LookalikesPollResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = LookalikesPollResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LookalikesPollResponse200
    | LookalikesPollResponse400
    | LookalikesPollResponse401
    | LookalikesPollResponse402
    | LookalikesPollResponse403
    | LookalikesPollResponse404
    | LookalikesPollResponse422
    | LookalikesPollResponse429
    | LookalikesPollResponse500
    | LookalikesPollResponse503
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
    body: LookalikesPollBody,
) -> Response[
    LookalikesPollResponse200
    | LookalikesPollResponse400
    | LookalikesPollResponse401
    | LookalikesPollResponse402
    | LookalikesPollResponse403
    | LookalikesPollResponse404
    | LookalikesPollResponse422
    | LookalikesPollResponse429
    | LookalikesPollResponse500
    | LookalikesPollResponse503
]:
    """Poll lookalike run

     Poll a lookalike run for progress. Graded results appear when the run completes; poll until status
    is 'done' or 'failed'.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookalikesPollResponse200 | LookalikesPollResponse400 | LookalikesPollResponse401 | LookalikesPollResponse402 | LookalikesPollResponse403 | LookalikesPollResponse404 | LookalikesPollResponse422 | LookalikesPollResponse429 | LookalikesPollResponse500 | LookalikesPollResponse503]
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
    body: LookalikesPollBody,
) -> (
    LookalikesPollResponse200
    | LookalikesPollResponse400
    | LookalikesPollResponse401
    | LookalikesPollResponse402
    | LookalikesPollResponse403
    | LookalikesPollResponse404
    | LookalikesPollResponse422
    | LookalikesPollResponse429
    | LookalikesPollResponse500
    | LookalikesPollResponse503
    | None
):
    """Poll lookalike run

     Poll a lookalike run for progress. Graded results appear when the run completes; poll until status
    is 'done' or 'failed'.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookalikesPollResponse200 | LookalikesPollResponse400 | LookalikesPollResponse401 | LookalikesPollResponse402 | LookalikesPollResponse403 | LookalikesPollResponse404 | LookalikesPollResponse422 | LookalikesPollResponse429 | LookalikesPollResponse500 | LookalikesPollResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LookalikesPollBody,
) -> Response[
    LookalikesPollResponse200
    | LookalikesPollResponse400
    | LookalikesPollResponse401
    | LookalikesPollResponse402
    | LookalikesPollResponse403
    | LookalikesPollResponse404
    | LookalikesPollResponse422
    | LookalikesPollResponse429
    | LookalikesPollResponse500
    | LookalikesPollResponse503
]:
    """Poll lookalike run

     Poll a lookalike run for progress. Graded results appear when the run completes; poll until status
    is 'done' or 'failed'.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookalikesPollResponse200 | LookalikesPollResponse400 | LookalikesPollResponse401 | LookalikesPollResponse402 | LookalikesPollResponse403 | LookalikesPollResponse404 | LookalikesPollResponse422 | LookalikesPollResponse429 | LookalikesPollResponse500 | LookalikesPollResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LookalikesPollBody,
) -> (
    LookalikesPollResponse200
    | LookalikesPollResponse400
    | LookalikesPollResponse401
    | LookalikesPollResponse402
    | LookalikesPollResponse403
    | LookalikesPollResponse404
    | LookalikesPollResponse422
    | LookalikesPollResponse429
    | LookalikesPollResponse500
    | LookalikesPollResponse503
    | None
):
    """Poll lookalike run

     Poll a lookalike run for progress. Graded results appear when the run completes; poll until status
    is 'done' or 'failed'.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookalikesPollResponse200 | LookalikesPollResponse400 | LookalikesPollResponse401 | LookalikesPollResponse402 | LookalikesPollResponse403 | LookalikesPollResponse404 | LookalikesPollResponse422 | LookalikesPollResponse429 | LookalikesPollResponse500 | LookalikesPollResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
