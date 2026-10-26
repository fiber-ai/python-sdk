from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lookalikes_trigger_body import LookalikesTriggerBody
from ...models.lookalikes_trigger_response_200 import LookalikesTriggerResponse200
from ...models.lookalikes_trigger_response_400 import LookalikesTriggerResponse400
from ...models.lookalikes_trigger_response_401 import LookalikesTriggerResponse401
from ...models.lookalikes_trigger_response_402 import LookalikesTriggerResponse402
from ...models.lookalikes_trigger_response_403 import LookalikesTriggerResponse403
from ...models.lookalikes_trigger_response_404 import LookalikesTriggerResponse404
from ...models.lookalikes_trigger_response_422 import LookalikesTriggerResponse422
from ...models.lookalikes_trigger_response_429 import LookalikesTriggerResponse429
from ...models.lookalikes_trigger_response_500 import LookalikesTriggerResponse500
from ...models.lookalikes_trigger_response_503 import LookalikesTriggerResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: LookalikesTriggerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/lookalikes/trigger",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LookalikesTriggerResponse200
    | LookalikesTriggerResponse400
    | LookalikesTriggerResponse401
    | LookalikesTriggerResponse402
    | LookalikesTriggerResponse403
    | LookalikesTriggerResponse404
    | LookalikesTriggerResponse422
    | LookalikesTriggerResponse429
    | LookalikesTriggerResponse500
    | LookalikesTriggerResponse503
    | None
):
    if response.status_code == 200:
        response_200 = LookalikesTriggerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LookalikesTriggerResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LookalikesTriggerResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = LookalikesTriggerResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = LookalikesTriggerResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LookalikesTriggerResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = LookalikesTriggerResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = LookalikesTriggerResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = LookalikesTriggerResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = LookalikesTriggerResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LookalikesTriggerResponse200
    | LookalikesTriggerResponse400
    | LookalikesTriggerResponse401
    | LookalikesTriggerResponse402
    | LookalikesTriggerResponse403
    | LookalikesTriggerResponse404
    | LookalikesTriggerResponse422
    | LookalikesTriggerResponse429
    | LookalikesTriggerResponse500
    | LookalikesTriggerResponse503
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
    body: LookalikesTriggerBody,
) -> Response[
    LookalikesTriggerResponse200
    | LookalikesTriggerResponse400
    | LookalikesTriggerResponse401
    | LookalikesTriggerResponse402
    | LookalikesTriggerResponse403
    | LookalikesTriggerResponse404
    | LookalikesTriggerResponse422
    | LookalikesTriggerResponse429
    | LookalikesTriggerResponse500
    | LookalikesTriggerResponse503
]:
    """Start lookalike run

     Start an AI lookalike run: give it companies you like (by domain), and it finds and grades similar
    companies, grouped by the patterns in your list. Runs take a few minutes — poll for progress and
    results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookalikesTriggerResponse200 | LookalikesTriggerResponse400 | LookalikesTriggerResponse401 | LookalikesTriggerResponse402 | LookalikesTriggerResponse403 | LookalikesTriggerResponse404 | LookalikesTriggerResponse422 | LookalikesTriggerResponse429 | LookalikesTriggerResponse500 | LookalikesTriggerResponse503]
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
    body: LookalikesTriggerBody,
) -> (
    LookalikesTriggerResponse200
    | LookalikesTriggerResponse400
    | LookalikesTriggerResponse401
    | LookalikesTriggerResponse402
    | LookalikesTriggerResponse403
    | LookalikesTriggerResponse404
    | LookalikesTriggerResponse422
    | LookalikesTriggerResponse429
    | LookalikesTriggerResponse500
    | LookalikesTriggerResponse503
    | None
):
    """Start lookalike run

     Start an AI lookalike run: give it companies you like (by domain), and it finds and grades similar
    companies, grouped by the patterns in your list. Runs take a few minutes — poll for progress and
    results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookalikesTriggerResponse200 | LookalikesTriggerResponse400 | LookalikesTriggerResponse401 | LookalikesTriggerResponse402 | LookalikesTriggerResponse403 | LookalikesTriggerResponse404 | LookalikesTriggerResponse422 | LookalikesTriggerResponse429 | LookalikesTriggerResponse500 | LookalikesTriggerResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LookalikesTriggerBody,
) -> Response[
    LookalikesTriggerResponse200
    | LookalikesTriggerResponse400
    | LookalikesTriggerResponse401
    | LookalikesTriggerResponse402
    | LookalikesTriggerResponse403
    | LookalikesTriggerResponse404
    | LookalikesTriggerResponse422
    | LookalikesTriggerResponse429
    | LookalikesTriggerResponse500
    | LookalikesTriggerResponse503
]:
    """Start lookalike run

     Start an AI lookalike run: give it companies you like (by domain), and it finds and grades similar
    companies, grouped by the patterns in your list. Runs take a few minutes — poll for progress and
    results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookalikesTriggerResponse200 | LookalikesTriggerResponse400 | LookalikesTriggerResponse401 | LookalikesTriggerResponse402 | LookalikesTriggerResponse403 | LookalikesTriggerResponse404 | LookalikesTriggerResponse422 | LookalikesTriggerResponse429 | LookalikesTriggerResponse500 | LookalikesTriggerResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LookalikesTriggerBody,
) -> (
    LookalikesTriggerResponse200
    | LookalikesTriggerResponse400
    | LookalikesTriggerResponse401
    | LookalikesTriggerResponse402
    | LookalikesTriggerResponse403
    | LookalikesTriggerResponse404
    | LookalikesTriggerResponse422
    | LookalikesTriggerResponse429
    | LookalikesTriggerResponse500
    | LookalikesTriggerResponse503
    | None
):
    """Start lookalike run

     Start an AI lookalike run: give it companies you like (by domain), and it finds and grades similar
    companies, grouped by the patterns in your list. Runs take a few minutes — poll for progress and
    results.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesTriggerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookalikesTriggerResponse200 | LookalikesTriggerResponse400 | LookalikesTriggerResponse401 | LookalikesTriggerResponse402 | LookalikesTriggerResponse403 | LookalikesTriggerResponse404 | LookalikesTriggerResponse422 | LookalikesTriggerResponse429 | LookalikesTriggerResponse500 | LookalikesTriggerResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
