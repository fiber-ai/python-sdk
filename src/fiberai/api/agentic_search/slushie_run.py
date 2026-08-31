from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.slushie_run_body import SlushieRunBody
from ...models.slushie_run_response_400 import SlushieRunResponse400
from ...models.slushie_run_response_401 import SlushieRunResponse401
from ...models.slushie_run_response_402 import SlushieRunResponse402
from ...models.slushie_run_response_403 import SlushieRunResponse403
from ...models.slushie_run_response_404 import SlushieRunResponse404
from ...models.slushie_run_response_422 import SlushieRunResponse422
from ...models.slushie_run_response_429 import SlushieRunResponse429
from ...models.slushie_run_response_500 import SlushieRunResponse500
from ...models.slushie_run_response_503 import SlushieRunResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SlushieRunBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/nlp-search/run",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SlushieRunResponse400
    | SlushieRunResponse401
    | SlushieRunResponse402
    | SlushieRunResponse403
    | SlushieRunResponse404
    | SlushieRunResponse422
    | SlushieRunResponse429
    | SlushieRunResponse500
    | SlushieRunResponse503
    | None
):
    if response.status_code == 400:
        response_400 = SlushieRunResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SlushieRunResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SlushieRunResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SlushieRunResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SlushieRunResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = SlushieRunResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = SlushieRunResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SlushieRunResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SlushieRunResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SlushieRunResponse400
    | SlushieRunResponse401
    | SlushieRunResponse402
    | SlushieRunResponse403
    | SlushieRunResponse404
    | SlushieRunResponse422
    | SlushieRunResponse429
    | SlushieRunResponse500
    | SlushieRunResponse503
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
    body: SlushieRunBody,
) -> Response[
    SlushieRunResponse400
    | SlushieRunResponse401
    | SlushieRunResponse402
    | SlushieRunResponse403
    | SlushieRunResponse404
    | SlushieRunResponse422
    | SlushieRunResponse429
    | SlushieRunResponse500
    | SlushieRunResponse503
]:
    """Natural language search

     Takes free-form text (e.g., 'Senior Product Managers at Series A FinTech startups in New York') and
    returns matching companies or people. The API determines the result type based on query
    interpretation — company-specific queries return companies, everything else returns people. Supports
    cursor-based pagination via a single pageToken.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request (first page only):<br />• 2 credits for AI
    search interpretation<br /><br />Variable costs per result:<br />• 1 credits per company returned<br
    />• 1 credits per profile returned&nbsp;<span title="Pricing shown is default pricing. Actual
    pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (SlushieRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlushieRunResponse400 | SlushieRunResponse401 | SlushieRunResponse402 | SlushieRunResponse403 | SlushieRunResponse404 | SlushieRunResponse422 | SlushieRunResponse429 | SlushieRunResponse500 | SlushieRunResponse503]
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
    body: SlushieRunBody,
) -> (
    SlushieRunResponse400
    | SlushieRunResponse401
    | SlushieRunResponse402
    | SlushieRunResponse403
    | SlushieRunResponse404
    | SlushieRunResponse422
    | SlushieRunResponse429
    | SlushieRunResponse500
    | SlushieRunResponse503
    | None
):
    """Natural language search

     Takes free-form text (e.g., 'Senior Product Managers at Series A FinTech startups in New York') and
    returns matching companies or people. The API determines the result type based on query
    interpretation — company-specific queries return companies, everything else returns people. Supports
    cursor-based pagination via a single pageToken.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request (first page only):<br />• 2 credits for AI
    search interpretation<br /><br />Variable costs per result:<br />• 1 credits per company returned<br
    />• 1 credits per profile returned&nbsp;<span title="Pricing shown is default pricing. Actual
    pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (SlushieRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlushieRunResponse400 | SlushieRunResponse401 | SlushieRunResponse402 | SlushieRunResponse403 | SlushieRunResponse404 | SlushieRunResponse422 | SlushieRunResponse429 | SlushieRunResponse500 | SlushieRunResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlushieRunBody,
) -> Response[
    SlushieRunResponse400
    | SlushieRunResponse401
    | SlushieRunResponse402
    | SlushieRunResponse403
    | SlushieRunResponse404
    | SlushieRunResponse422
    | SlushieRunResponse429
    | SlushieRunResponse500
    | SlushieRunResponse503
]:
    """Natural language search

     Takes free-form text (e.g., 'Senior Product Managers at Series A FinTech startups in New York') and
    returns matching companies or people. The API determines the result type based on query
    interpretation — company-specific queries return companies, everything else returns people. Supports
    cursor-based pagination via a single pageToken.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request (first page only):<br />• 2 credits for AI
    search interpretation<br /><br />Variable costs per result:<br />• 1 credits per company returned<br
    />• 1 credits per profile returned&nbsp;<span title="Pricing shown is default pricing. Actual
    pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (SlushieRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SlushieRunResponse400 | SlushieRunResponse401 | SlushieRunResponse402 | SlushieRunResponse403 | SlushieRunResponse404 | SlushieRunResponse422 | SlushieRunResponse429 | SlushieRunResponse500 | SlushieRunResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SlushieRunBody,
) -> (
    SlushieRunResponse400
    | SlushieRunResponse401
    | SlushieRunResponse402
    | SlushieRunResponse403
    | SlushieRunResponse404
    | SlushieRunResponse422
    | SlushieRunResponse429
    | SlushieRunResponse500
    | SlushieRunResponse503
    | None
):
    """Natural language search

     Takes free-form text (e.g., 'Senior Product Managers at Series A FinTech startups in New York') and
    returns matching companies or people. The API determines the result type based on query
    interpretation — company-specific queries return companies, everything else returns people. Supports
    cursor-based pagination via a single pageToken.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> Fixed costs per request (first page only):<br />• 2 credits for AI
    search interpretation<br /><br />Variable costs per result:<br />• 1 credits per company returned<br
    />• 1 credits per profile returned&nbsp;<span title="Pricing shown is default pricing. Actual
    pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.">ⓘ</span></span>

    Args:
        body (SlushieRunBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SlushieRunResponse400 | SlushieRunResponse401 | SlushieRunResponse402 | SlushieRunResponse403 | SlushieRunResponse404 | SlushieRunResponse422 | SlushieRunResponse429 | SlushieRunResponse500 | SlushieRunResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
