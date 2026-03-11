from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.people_search_body import PeopleSearchBody
from ...models.people_search_response_200 import PeopleSearchResponse200
from ...models.people_search_response_400 import PeopleSearchResponse400
from ...models.people_search_response_401 import PeopleSearchResponse401
from ...models.people_search_response_402 import PeopleSearchResponse402
from ...models.people_search_response_403 import PeopleSearchResponse403
from ...models.people_search_response_404 import PeopleSearchResponse404
from ...models.people_search_response_429 import PeopleSearchResponse429
from ...models.people_search_response_500 import PeopleSearchResponse500
from ...models.people_search_response_503 import PeopleSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PeopleSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/people-search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PeopleSearchResponse200
    | PeopleSearchResponse400
    | PeopleSearchResponse401
    | PeopleSearchResponse402
    | PeopleSearchResponse403
    | PeopleSearchResponse404
    | PeopleSearchResponse429
    | PeopleSearchResponse500
    | PeopleSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PeopleSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PeopleSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PeopleSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PeopleSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PeopleSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PeopleSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PeopleSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PeopleSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PeopleSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PeopleSearchResponse200
    | PeopleSearchResponse400
    | PeopleSearchResponse401
    | PeopleSearchResponse402
    | PeopleSearchResponse403
    | PeopleSearchResponse404
    | PeopleSearchResponse429
    | PeopleSearchResponse500
    | PeopleSearchResponse503
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
    body: PeopleSearchBody,
) -> Response[
    PeopleSearchResponse200
    | PeopleSearchResponse400
    | PeopleSearchResponse401
    | PeopleSearchResponse402
    | PeopleSearchResponse403
    | PeopleSearchResponse404
    | PeopleSearchResponse429
    | PeopleSearchResponse500
    | PeopleSearchResponse503
]:
    r"""People search

     Search for people using filters

    <span>⚡ <strong>Rate limit:</strong> 180 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per profile found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PeopleSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PeopleSearchResponse200 | PeopleSearchResponse400 | PeopleSearchResponse401 | PeopleSearchResponse402 | PeopleSearchResponse403 | PeopleSearchResponse404 | PeopleSearchResponse429 | PeopleSearchResponse500 | PeopleSearchResponse503]
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
    body: PeopleSearchBody,
) -> (
    PeopleSearchResponse200
    | PeopleSearchResponse400
    | PeopleSearchResponse401
    | PeopleSearchResponse402
    | PeopleSearchResponse403
    | PeopleSearchResponse404
    | PeopleSearchResponse429
    | PeopleSearchResponse500
    | PeopleSearchResponse503
    | None
):
    r"""People search

     Search for people using filters

    <span>⚡ <strong>Rate limit:</strong> 180 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per profile found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PeopleSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PeopleSearchResponse200 | PeopleSearchResponse400 | PeopleSearchResponse401 | PeopleSearchResponse402 | PeopleSearchResponse403 | PeopleSearchResponse404 | PeopleSearchResponse429 | PeopleSearchResponse500 | PeopleSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PeopleSearchBody,
) -> Response[
    PeopleSearchResponse200
    | PeopleSearchResponse400
    | PeopleSearchResponse401
    | PeopleSearchResponse402
    | PeopleSearchResponse403
    | PeopleSearchResponse404
    | PeopleSearchResponse429
    | PeopleSearchResponse500
    | PeopleSearchResponse503
]:
    r"""People search

     Search for people using filters

    <span>⚡ <strong>Rate limit:</strong> 180 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per profile found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PeopleSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PeopleSearchResponse200 | PeopleSearchResponse400 | PeopleSearchResponse401 | PeopleSearchResponse402 | PeopleSearchResponse403 | PeopleSearchResponse404 | PeopleSearchResponse429 | PeopleSearchResponse500 | PeopleSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PeopleSearchBody,
) -> (
    PeopleSearchResponse200
    | PeopleSearchResponse400
    | PeopleSearchResponse401
    | PeopleSearchResponse402
    | PeopleSearchResponse403
    | PeopleSearchResponse404
    | PeopleSearchResponse429
    | PeopleSearchResponse500
    | PeopleSearchResponse503
    | None
):
    r"""People search

     Search for people using filters

    <span>⚡ <strong>Rate limit:</strong> 180 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per profile found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (PeopleSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PeopleSearchResponse200 | PeopleSearchResponse400 | PeopleSearchResponse401 | PeopleSearchResponse402 | PeopleSearchResponse403 | PeopleSearchResponse404 | PeopleSearchResponse429 | PeopleSearchResponse500 | PeopleSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
