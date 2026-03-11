from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_lookup_polling_body import DomainLookupPollingBody
from ...models.domain_lookup_polling_response_200 import DomainLookupPollingResponse200
from ...models.domain_lookup_polling_response_400 import DomainLookupPollingResponse400
from ...models.domain_lookup_polling_response_401 import DomainLookupPollingResponse401
from ...models.domain_lookup_polling_response_402 import DomainLookupPollingResponse402
from ...models.domain_lookup_polling_response_403 import DomainLookupPollingResponse403
from ...models.domain_lookup_polling_response_404 import DomainLookupPollingResponse404
from ...models.domain_lookup_polling_response_429 import DomainLookupPollingResponse429
from ...models.domain_lookup_polling_response_500 import DomainLookupPollingResponse500
from ...models.domain_lookup_polling_response_503 import DomainLookupPollingResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: DomainLookupPollingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/domain-lookup/polling",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DomainLookupPollingResponse200
    | DomainLookupPollingResponse400
    | DomainLookupPollingResponse401
    | DomainLookupPollingResponse402
    | DomainLookupPollingResponse403
    | DomainLookupPollingResponse404
    | DomainLookupPollingResponse429
    | DomainLookupPollingResponse500
    | DomainLookupPollingResponse503
    | None
):
    if response.status_code == 200:
        response_200 = DomainLookupPollingResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DomainLookupPollingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DomainLookupPollingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = DomainLookupPollingResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = DomainLookupPollingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DomainLookupPollingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = DomainLookupPollingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DomainLookupPollingResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DomainLookupPollingResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DomainLookupPollingResponse200
    | DomainLookupPollingResponse400
    | DomainLookupPollingResponse401
    | DomainLookupPollingResponse402
    | DomainLookupPollingResponse403
    | DomainLookupPollingResponse404
    | DomainLookupPollingResponse429
    | DomainLookupPollingResponse500
    | DomainLookupPollingResponse503
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
    body: DomainLookupPollingBody,
) -> Response[
    DomainLookupPollingResponse200
    | DomainLookupPollingResponse400
    | DomainLookupPollingResponse401
    | DomainLookupPollingResponse402
    | DomainLookupPollingResponse403
    | DomainLookupPollingResponse404
    | DomainLookupPollingResponse429
    | DomainLookupPollingResponse500
    | DomainLookupPollingResponse503
]:
    """Poll Domain lookup

     Poll for the results of a domain lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (DomainLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainLookupPollingResponse200 | DomainLookupPollingResponse400 | DomainLookupPollingResponse401 | DomainLookupPollingResponse402 | DomainLookupPollingResponse403 | DomainLookupPollingResponse404 | DomainLookupPollingResponse429 | DomainLookupPollingResponse500 | DomainLookupPollingResponse503]
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
    body: DomainLookupPollingBody,
) -> (
    DomainLookupPollingResponse200
    | DomainLookupPollingResponse400
    | DomainLookupPollingResponse401
    | DomainLookupPollingResponse402
    | DomainLookupPollingResponse403
    | DomainLookupPollingResponse404
    | DomainLookupPollingResponse429
    | DomainLookupPollingResponse500
    | DomainLookupPollingResponse503
    | None
):
    """Poll Domain lookup

     Poll for the results of a domain lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (DomainLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainLookupPollingResponse200 | DomainLookupPollingResponse400 | DomainLookupPollingResponse401 | DomainLookupPollingResponse402 | DomainLookupPollingResponse403 | DomainLookupPollingResponse404 | DomainLookupPollingResponse429 | DomainLookupPollingResponse500 | DomainLookupPollingResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DomainLookupPollingBody,
) -> Response[
    DomainLookupPollingResponse200
    | DomainLookupPollingResponse400
    | DomainLookupPollingResponse401
    | DomainLookupPollingResponse402
    | DomainLookupPollingResponse403
    | DomainLookupPollingResponse404
    | DomainLookupPollingResponse429
    | DomainLookupPollingResponse500
    | DomainLookupPollingResponse503
]:
    """Poll Domain lookup

     Poll for the results of a domain lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (DomainLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainLookupPollingResponse200 | DomainLookupPollingResponse400 | DomainLookupPollingResponse401 | DomainLookupPollingResponse402 | DomainLookupPollingResponse403 | DomainLookupPollingResponse404 | DomainLookupPollingResponse429 | DomainLookupPollingResponse500 | DomainLookupPollingResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DomainLookupPollingBody,
) -> (
    DomainLookupPollingResponse200
    | DomainLookupPollingResponse400
    | DomainLookupPollingResponse401
    | DomainLookupPollingResponse402
    | DomainLookupPollingResponse403
    | DomainLookupPollingResponse404
    | DomainLookupPollingResponse429
    | DomainLookupPollingResponse500
    | DomainLookupPollingResponse503
    | None
):
    """Poll Domain lookup

     Poll for the results of a domain lookup task.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    Args:
        body (DomainLookupPollingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainLookupPollingResponse200 | DomainLookupPollingResponse400 | DomainLookupPollingResponse401 | DomainLookupPollingResponse402 | DomainLookupPollingResponse403 | DomainLookupPollingResponse404 | DomainLookupPollingResponse429 | DomainLookupPollingResponse500 | DomainLookupPollingResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
