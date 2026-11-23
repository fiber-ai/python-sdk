from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lookalikes_single_body import LookalikesSingleBody
from ...models.lookalikes_single_response_200 import LookalikesSingleResponse200
from ...models.lookalikes_single_response_400 import LookalikesSingleResponse400
from ...models.lookalikes_single_response_401 import LookalikesSingleResponse401
from ...models.lookalikes_single_response_402 import LookalikesSingleResponse402
from ...models.lookalikes_single_response_403 import LookalikesSingleResponse403
from ...models.lookalikes_single_response_404 import LookalikesSingleResponse404
from ...models.lookalikes_single_response_422 import LookalikesSingleResponse422
from ...models.lookalikes_single_response_429 import LookalikesSingleResponse429
from ...models.lookalikes_single_response_500 import LookalikesSingleResponse500
from ...models.lookalikes_single_response_503 import LookalikesSingleResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: LookalikesSingleBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/lookalikes/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LookalikesSingleResponse200
    | LookalikesSingleResponse400
    | LookalikesSingleResponse401
    | LookalikesSingleResponse402
    | LookalikesSingleResponse403
    | LookalikesSingleResponse404
    | LookalikesSingleResponse422
    | LookalikesSingleResponse429
    | LookalikesSingleResponse500
    | LookalikesSingleResponse503
    | None
):
    if response.status_code == 200:
        response_200 = LookalikesSingleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LookalikesSingleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LookalikesSingleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = LookalikesSingleResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = LookalikesSingleResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LookalikesSingleResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = LookalikesSingleResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = LookalikesSingleResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = LookalikesSingleResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = LookalikesSingleResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LookalikesSingleResponse200
    | LookalikesSingleResponse400
    | LookalikesSingleResponse401
    | LookalikesSingleResponse402
    | LookalikesSingleResponse403
    | LookalikesSingleResponse404
    | LookalikesSingleResponse422
    | LookalikesSingleResponse429
    | LookalikesSingleResponse500
    | LookalikesSingleResponse503
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
    body: LookalikesSingleBody,
) -> Response[
    LookalikesSingleResponse200
    | LookalikesSingleResponse400
    | LookalikesSingleResponse401
    | LookalikesSingleResponse402
    | LookalikesSingleResponse403
    | LookalikesSingleResponse404
    | LookalikesSingleResponse422
    | LookalikesSingleResponse429
    | LookalikesSingleResponse500
    | LookalikesSingleResponse503
]:
    """Find similar companies

     Find companies similar to one company, in a single request: give it a domain and get back similar
    companies, best first. Built for per-row use, such as an enrichment column in a spreadsheet tool:
    send `{"domain": "example.com"}` and read `output.results`, or pass `limit` for fewer companies. The
    best matches come first, with scores and a reason. You are charged only for the companies returned.
    For a whole list of companies, grouped by the patterns in it, start a lookalike run instead.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookalikesSingleResponse200 | LookalikesSingleResponse400 | LookalikesSingleResponse401 | LookalikesSingleResponse402 | LookalikesSingleResponse403 | LookalikesSingleResponse404 | LookalikesSingleResponse422 | LookalikesSingleResponse429 | LookalikesSingleResponse500 | LookalikesSingleResponse503]
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
    body: LookalikesSingleBody,
) -> (
    LookalikesSingleResponse200
    | LookalikesSingleResponse400
    | LookalikesSingleResponse401
    | LookalikesSingleResponse402
    | LookalikesSingleResponse403
    | LookalikesSingleResponse404
    | LookalikesSingleResponse422
    | LookalikesSingleResponse429
    | LookalikesSingleResponse500
    | LookalikesSingleResponse503
    | None
):
    """Find similar companies

     Find companies similar to one company, in a single request: give it a domain and get back similar
    companies, best first. Built for per-row use, such as an enrichment column in a spreadsheet tool:
    send `{"domain": "example.com"}` and read `output.results`, or pass `limit` for fewer companies. The
    best matches come first, with scores and a reason. You are charged only for the companies returned.
    For a whole list of companies, grouped by the patterns in it, start a lookalike run instead.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookalikesSingleResponse200 | LookalikesSingleResponse400 | LookalikesSingleResponse401 | LookalikesSingleResponse402 | LookalikesSingleResponse403 | LookalikesSingleResponse404 | LookalikesSingleResponse422 | LookalikesSingleResponse429 | LookalikesSingleResponse500 | LookalikesSingleResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LookalikesSingleBody,
) -> Response[
    LookalikesSingleResponse200
    | LookalikesSingleResponse400
    | LookalikesSingleResponse401
    | LookalikesSingleResponse402
    | LookalikesSingleResponse403
    | LookalikesSingleResponse404
    | LookalikesSingleResponse422
    | LookalikesSingleResponse429
    | LookalikesSingleResponse500
    | LookalikesSingleResponse503
]:
    """Find similar companies

     Find companies similar to one company, in a single request: give it a domain and get back similar
    companies, best first. Built for per-row use, such as an enrichment column in a spreadsheet tool:
    send `{"domain": "example.com"}` and read `output.results`, or pass `limit` for fewer companies. The
    best matches come first, with scores and a reason. You are charged only for the companies returned.
    For a whole list of companies, grouped by the patterns in it, start a lookalike run instead.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LookalikesSingleResponse200 | LookalikesSingleResponse400 | LookalikesSingleResponse401 | LookalikesSingleResponse402 | LookalikesSingleResponse403 | LookalikesSingleResponse404 | LookalikesSingleResponse422 | LookalikesSingleResponse429 | LookalikesSingleResponse500 | LookalikesSingleResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LookalikesSingleBody,
) -> (
    LookalikesSingleResponse200
    | LookalikesSingleResponse400
    | LookalikesSingleResponse401
    | LookalikesSingleResponse402
    | LookalikesSingleResponse403
    | LookalikesSingleResponse404
    | LookalikesSingleResponse422
    | LookalikesSingleResponse429
    | LookalikesSingleResponse500
    | LookalikesSingleResponse503
    | None
):
    """Find similar companies

     Find companies similar to one company, in a single request: give it a domain and get back similar
    companies, best first. Built for per-row use, such as an enrichment column in a spreadsheet tool:
    send `{"domain": "example.com"}` and read `output.results`, or pass `limit` for fewer companies. The
    best matches come first, with scores and a reason. You are charged only for the companies returned.
    For a whole list of companies, grouped by the patterns in it, start a lookalike run instead.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.2 credits per lookalike found&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (LookalikesSingleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LookalikesSingleResponse200 | LookalikesSingleResponse400 | LookalikesSingleResponse401 | LookalikesSingleResponse402 | LookalikesSingleResponse403 | LookalikesSingleResponse404 | LookalikesSingleResponse422 | LookalikesSingleResponse429 | LookalikesSingleResponse500 | LookalikesSingleResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
