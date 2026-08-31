from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.quick_person_resolve_body import QuickPersonResolveBody
from ...models.quick_person_resolve_response_200 import QuickPersonResolveResponse200
from ...models.quick_person_resolve_response_400 import QuickPersonResolveResponse400
from ...models.quick_person_resolve_response_401 import QuickPersonResolveResponse401
from ...models.quick_person_resolve_response_402 import QuickPersonResolveResponse402
from ...models.quick_person_resolve_response_403 import QuickPersonResolveResponse403
from ...models.quick_person_resolve_response_404 import QuickPersonResolveResponse404
from ...models.quick_person_resolve_response_422 import QuickPersonResolveResponse422
from ...models.quick_person_resolve_response_429 import QuickPersonResolveResponse429
from ...models.quick_person_resolve_response_500 import QuickPersonResolveResponse500
from ...models.quick_person_resolve_response_503 import QuickPersonResolveResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: QuickPersonResolveBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/person-resolve",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    QuickPersonResolveResponse200
    | QuickPersonResolveResponse400
    | QuickPersonResolveResponse401
    | QuickPersonResolveResponse402
    | QuickPersonResolveResponse403
    | QuickPersonResolveResponse404
    | QuickPersonResolveResponse422
    | QuickPersonResolveResponse429
    | QuickPersonResolveResponse500
    | QuickPersonResolveResponse503
    | None
):
    if response.status_code == 200:
        response_200 = QuickPersonResolveResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = QuickPersonResolveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = QuickPersonResolveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = QuickPersonResolveResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = QuickPersonResolveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = QuickPersonResolveResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = QuickPersonResolveResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = QuickPersonResolveResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = QuickPersonResolveResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = QuickPersonResolveResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    QuickPersonResolveResponse200
    | QuickPersonResolveResponse400
    | QuickPersonResolveResponse401
    | QuickPersonResolveResponse402
    | QuickPersonResolveResponse403
    | QuickPersonResolveResponse404
    | QuickPersonResolveResponse422
    | QuickPersonResolveResponse429
    | QuickPersonResolveResponse500
    | QuickPersonResolveResponse503
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
    body: QuickPersonResolveBody,
) -> Response[
    QuickPersonResolveResponse200
    | QuickPersonResolveResponse400
    | QuickPersonResolveResponse401
    | QuickPersonResolveResponse402
    | QuickPersonResolveResponse403
    | QuickPersonResolveResponse404
    | QuickPersonResolveResponse422
    | QuickPersonResolveResponse429
    | QuickPersonResolveResponse500
    | QuickPersonResolveResponse503
]:
    """Quickly resolve person identifiers

     Resolves many person identifiers — LinkedIn slug, numeric LinkedIn user ID, LinkedIn profile URL, or
    LinkedIn entity URN — to full profile records in a single request.

    <span>⚡ <strong>Rate limit:</strong> 1500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per person resolved&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (QuickPersonResolveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QuickPersonResolveResponse200 | QuickPersonResolveResponse400 | QuickPersonResolveResponse401 | QuickPersonResolveResponse402 | QuickPersonResolveResponse403 | QuickPersonResolveResponse404 | QuickPersonResolveResponse422 | QuickPersonResolveResponse429 | QuickPersonResolveResponse500 | QuickPersonResolveResponse503]
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
    body: QuickPersonResolveBody,
) -> (
    QuickPersonResolveResponse200
    | QuickPersonResolveResponse400
    | QuickPersonResolveResponse401
    | QuickPersonResolveResponse402
    | QuickPersonResolveResponse403
    | QuickPersonResolveResponse404
    | QuickPersonResolveResponse422
    | QuickPersonResolveResponse429
    | QuickPersonResolveResponse500
    | QuickPersonResolveResponse503
    | None
):
    """Quickly resolve person identifiers

     Resolves many person identifiers — LinkedIn slug, numeric LinkedIn user ID, LinkedIn profile URL, or
    LinkedIn entity URN — to full profile records in a single request.

    <span>⚡ <strong>Rate limit:</strong> 1500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per person resolved&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (QuickPersonResolveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QuickPersonResolveResponse200 | QuickPersonResolveResponse400 | QuickPersonResolveResponse401 | QuickPersonResolveResponse402 | QuickPersonResolveResponse403 | QuickPersonResolveResponse404 | QuickPersonResolveResponse422 | QuickPersonResolveResponse429 | QuickPersonResolveResponse500 | QuickPersonResolveResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QuickPersonResolveBody,
) -> Response[
    QuickPersonResolveResponse200
    | QuickPersonResolveResponse400
    | QuickPersonResolveResponse401
    | QuickPersonResolveResponse402
    | QuickPersonResolveResponse403
    | QuickPersonResolveResponse404
    | QuickPersonResolveResponse422
    | QuickPersonResolveResponse429
    | QuickPersonResolveResponse500
    | QuickPersonResolveResponse503
]:
    """Quickly resolve person identifiers

     Resolves many person identifiers — LinkedIn slug, numeric LinkedIn user ID, LinkedIn profile URL, or
    LinkedIn entity URN — to full profile records in a single request.

    <span>⚡ <strong>Rate limit:</strong> 1500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per person resolved&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (QuickPersonResolveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QuickPersonResolveResponse200 | QuickPersonResolveResponse400 | QuickPersonResolveResponse401 | QuickPersonResolveResponse402 | QuickPersonResolveResponse403 | QuickPersonResolveResponse404 | QuickPersonResolveResponse422 | QuickPersonResolveResponse429 | QuickPersonResolveResponse500 | QuickPersonResolveResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QuickPersonResolveBody,
) -> (
    QuickPersonResolveResponse200
    | QuickPersonResolveResponse400
    | QuickPersonResolveResponse401
    | QuickPersonResolveResponse402
    | QuickPersonResolveResponse403
    | QuickPersonResolveResponse404
    | QuickPersonResolveResponse422
    | QuickPersonResolveResponse429
    | QuickPersonResolveResponse500
    | QuickPersonResolveResponse503
    | None
):
    """Quickly resolve person identifiers

     Resolves many person identifiers — LinkedIn slug, numeric LinkedIn user ID, LinkedIn profile URL, or
    LinkedIn entity URN — to full profile records in a single request.

    <span>⚡ <strong>Rate limit:</strong> 1500 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per person resolved&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (QuickPersonResolveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QuickPersonResolveResponse200 | QuickPersonResolveResponse400 | QuickPersonResolveResponse401 | QuickPersonResolveResponse402 | QuickPersonResolveResponse403 | QuickPersonResolveResponse404 | QuickPersonResolveResponse422 | QuickPersonResolveResponse429 | QuickPersonResolveResponse500 | QuickPersonResolveResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
