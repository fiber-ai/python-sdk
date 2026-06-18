from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.skills_typeahead_body import SkillsTypeaheadBody
from ...models.skills_typeahead_response_200 import SkillsTypeaheadResponse200
from ...models.skills_typeahead_response_400 import SkillsTypeaheadResponse400
from ...models.skills_typeahead_response_401 import SkillsTypeaheadResponse401
from ...models.skills_typeahead_response_402 import SkillsTypeaheadResponse402
from ...models.skills_typeahead_response_403 import SkillsTypeaheadResponse403
from ...models.skills_typeahead_response_404 import SkillsTypeaheadResponse404
from ...models.skills_typeahead_response_422 import SkillsTypeaheadResponse422
from ...models.skills_typeahead_response_429 import SkillsTypeaheadResponse429
from ...models.skills_typeahead_response_500 import SkillsTypeaheadResponse500
from ...models.skills_typeahead_response_503 import SkillsTypeaheadResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: SkillsTypeaheadBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/typeahead/skills",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SkillsTypeaheadResponse200
    | SkillsTypeaheadResponse400
    | SkillsTypeaheadResponse401
    | SkillsTypeaheadResponse402
    | SkillsTypeaheadResponse403
    | SkillsTypeaheadResponse404
    | SkillsTypeaheadResponse422
    | SkillsTypeaheadResponse429
    | SkillsTypeaheadResponse500
    | SkillsTypeaheadResponse503
    | None
):
    if response.status_code == 200:
        response_200 = SkillsTypeaheadResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SkillsTypeaheadResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SkillsTypeaheadResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SkillsTypeaheadResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = SkillsTypeaheadResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SkillsTypeaheadResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = SkillsTypeaheadResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = SkillsTypeaheadResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SkillsTypeaheadResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = SkillsTypeaheadResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SkillsTypeaheadResponse200
    | SkillsTypeaheadResponse400
    | SkillsTypeaheadResponse401
    | SkillsTypeaheadResponse402
    | SkillsTypeaheadResponse403
    | SkillsTypeaheadResponse404
    | SkillsTypeaheadResponse422
    | SkillsTypeaheadResponse429
    | SkillsTypeaheadResponse500
    | SkillsTypeaheadResponse503
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
    body: SkillsTypeaheadBody,
) -> Response[
    SkillsTypeaheadResponse200
    | SkillsTypeaheadResponse400
    | SkillsTypeaheadResponse401
    | SkillsTypeaheadResponse402
    | SkillsTypeaheadResponse403
    | SkillsTypeaheadResponse404
    | SkillsTypeaheadResponse422
    | SkillsTypeaheadResponse429
    | SkillsTypeaheadResponse500
    | SkillsTypeaheadResponse503
]:
    r"""Skills Typeahead

     Search for professional skills by name. Supports prefix and partial matches with relevance-based
    ranking. Useful for building autocomplete in search UIs.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SkillsTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SkillsTypeaheadResponse200 | SkillsTypeaheadResponse400 | SkillsTypeaheadResponse401 | SkillsTypeaheadResponse402 | SkillsTypeaheadResponse403 | SkillsTypeaheadResponse404 | SkillsTypeaheadResponse422 | SkillsTypeaheadResponse429 | SkillsTypeaheadResponse500 | SkillsTypeaheadResponse503]
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
    body: SkillsTypeaheadBody,
) -> (
    SkillsTypeaheadResponse200
    | SkillsTypeaheadResponse400
    | SkillsTypeaheadResponse401
    | SkillsTypeaheadResponse402
    | SkillsTypeaheadResponse403
    | SkillsTypeaheadResponse404
    | SkillsTypeaheadResponse422
    | SkillsTypeaheadResponse429
    | SkillsTypeaheadResponse500
    | SkillsTypeaheadResponse503
    | None
):
    r"""Skills Typeahead

     Search for professional skills by name. Supports prefix and partial matches with relevance-based
    ranking. Useful for building autocomplete in search UIs.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SkillsTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SkillsTypeaheadResponse200 | SkillsTypeaheadResponse400 | SkillsTypeaheadResponse401 | SkillsTypeaheadResponse402 | SkillsTypeaheadResponse403 | SkillsTypeaheadResponse404 | SkillsTypeaheadResponse422 | SkillsTypeaheadResponse429 | SkillsTypeaheadResponse500 | SkillsTypeaheadResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SkillsTypeaheadBody,
) -> Response[
    SkillsTypeaheadResponse200
    | SkillsTypeaheadResponse400
    | SkillsTypeaheadResponse401
    | SkillsTypeaheadResponse402
    | SkillsTypeaheadResponse403
    | SkillsTypeaheadResponse404
    | SkillsTypeaheadResponse422
    | SkillsTypeaheadResponse429
    | SkillsTypeaheadResponse500
    | SkillsTypeaheadResponse503
]:
    r"""Skills Typeahead

     Search for professional skills by name. Supports prefix and partial matches with relevance-based
    ranking. Useful for building autocomplete in search UIs.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SkillsTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SkillsTypeaheadResponse200 | SkillsTypeaheadResponse400 | SkillsTypeaheadResponse401 | SkillsTypeaheadResponse402 | SkillsTypeaheadResponse403 | SkillsTypeaheadResponse404 | SkillsTypeaheadResponse422 | SkillsTypeaheadResponse429 | SkillsTypeaheadResponse500 | SkillsTypeaheadResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SkillsTypeaheadBody,
) -> (
    SkillsTypeaheadResponse200
    | SkillsTypeaheadResponse400
    | SkillsTypeaheadResponse401
    | SkillsTypeaheadResponse402
    | SkillsTypeaheadResponse403
    | SkillsTypeaheadResponse404
    | SkillsTypeaheadResponse422
    | SkillsTypeaheadResponse429
    | SkillsTypeaheadResponse500
    | SkillsTypeaheadResponse503
    | None
):
    r"""Skills Typeahead

     Search for professional skills by name. Supports prefix and partial matches with relevance-based
    ranking. Useful for building autocomplete in search UIs.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (SkillsTypeaheadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SkillsTypeaheadResponse200 | SkillsTypeaheadResponse400 | SkillsTypeaheadResponse401 | SkillsTypeaheadResponse402 | SkillsTypeaheadResponse403 | SkillsTypeaheadResponse404 | SkillsTypeaheadResponse422 | SkillsTypeaheadResponse429 | SkillsTypeaheadResponse500 | SkillsTypeaheadResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
