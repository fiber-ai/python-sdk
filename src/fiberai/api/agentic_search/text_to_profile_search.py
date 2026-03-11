from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.text_to_profile_search_body import TextToProfileSearchBody
from ...models.text_to_profile_search_response_200 import TextToProfileSearchResponse200
from ...models.text_to_profile_search_response_400 import TextToProfileSearchResponse400
from ...models.text_to_profile_search_response_401 import TextToProfileSearchResponse401
from ...models.text_to_profile_search_response_402 import TextToProfileSearchResponse402
from ...models.text_to_profile_search_response_403 import TextToProfileSearchResponse403
from ...models.text_to_profile_search_response_404 import TextToProfileSearchResponse404
from ...models.text_to_profile_search_response_429 import TextToProfileSearchResponse429
from ...models.text_to_profile_search_response_500 import TextToProfileSearchResponse500
from ...models.text_to_profile_search_response_503 import TextToProfileSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TextToProfileSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/natural-language-search/profiles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TextToProfileSearchResponse200
    | TextToProfileSearchResponse400
    | TextToProfileSearchResponse401
    | TextToProfileSearchResponse402
    | TextToProfileSearchResponse403
    | TextToProfileSearchResponse404
    | TextToProfileSearchResponse429
    | TextToProfileSearchResponse500
    | TextToProfileSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TextToProfileSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TextToProfileSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TextToProfileSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TextToProfileSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TextToProfileSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TextToProfileSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TextToProfileSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TextToProfileSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TextToProfileSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TextToProfileSearchResponse200
    | TextToProfileSearchResponse400
    | TextToProfileSearchResponse401
    | TextToProfileSearchResponse402
    | TextToProfileSearchResponse403
    | TextToProfileSearchResponse404
    | TextToProfileSearchResponse429
    | TextToProfileSearchResponse500
    | TextToProfileSearchResponse503
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
    body: TextToProfileSearchBody,
) -> Response[
    TextToProfileSearchResponse200
    | TextToProfileSearchResponse400
    | TextToProfileSearchResponse401
    | TextToProfileSearchResponse402
    | TextToProfileSearchResponse403
    | TextToProfileSearchResponse404
    | TextToProfileSearchResponse429
    | TextToProfileSearchResponse500
    | TextToProfileSearchResponse503
]:
    r"""Search profiles from text

     Takes free-form text (e.g., 'Software engineers in US with 5+ years of experience') and returns a
    list of matching profiles.             The endpoint interprets natural language queries and applies
    structured filters such as job titles, seniority, skills, locations, past jobs, education, and
    languages to identify relevant people.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per profile found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToProfileSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TextToProfileSearchResponse200 | TextToProfileSearchResponse400 | TextToProfileSearchResponse401 | TextToProfileSearchResponse402 | TextToProfileSearchResponse403 | TextToProfileSearchResponse404 | TextToProfileSearchResponse429 | TextToProfileSearchResponse500 | TextToProfileSearchResponse503]
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
    body: TextToProfileSearchBody,
) -> (
    TextToProfileSearchResponse200
    | TextToProfileSearchResponse400
    | TextToProfileSearchResponse401
    | TextToProfileSearchResponse402
    | TextToProfileSearchResponse403
    | TextToProfileSearchResponse404
    | TextToProfileSearchResponse429
    | TextToProfileSearchResponse500
    | TextToProfileSearchResponse503
    | None
):
    r"""Search profiles from text

     Takes free-form text (e.g., 'Software engineers in US with 5+ years of experience') and returns a
    list of matching profiles.             The endpoint interprets natural language queries and applies
    structured filters such as job titles, seniority, skills, locations, past jobs, education, and
    languages to identify relevant people.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per profile found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToProfileSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TextToProfileSearchResponse200 | TextToProfileSearchResponse400 | TextToProfileSearchResponse401 | TextToProfileSearchResponse402 | TextToProfileSearchResponse403 | TextToProfileSearchResponse404 | TextToProfileSearchResponse429 | TextToProfileSearchResponse500 | TextToProfileSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TextToProfileSearchBody,
) -> Response[
    TextToProfileSearchResponse200
    | TextToProfileSearchResponse400
    | TextToProfileSearchResponse401
    | TextToProfileSearchResponse402
    | TextToProfileSearchResponse403
    | TextToProfileSearchResponse404
    | TextToProfileSearchResponse429
    | TextToProfileSearchResponse500
    | TextToProfileSearchResponse503
]:
    r"""Search profiles from text

     Takes free-form text (e.g., 'Software engineers in US with 5+ years of experience') and returns a
    list of matching profiles.             The endpoint interprets natural language queries and applies
    structured filters such as job titles, seniority, skills, locations, past jobs, education, and
    languages to identify relevant people.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per profile found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToProfileSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TextToProfileSearchResponse200 | TextToProfileSearchResponse400 | TextToProfileSearchResponse401 | TextToProfileSearchResponse402 | TextToProfileSearchResponse403 | TextToProfileSearchResponse404 | TextToProfileSearchResponse429 | TextToProfileSearchResponse500 | TextToProfileSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TextToProfileSearchBody,
) -> (
    TextToProfileSearchResponse200
    | TextToProfileSearchResponse400
    | TextToProfileSearchResponse401
    | TextToProfileSearchResponse402
    | TextToProfileSearchResponse403
    | TextToProfileSearchResponse404
    | TextToProfileSearchResponse429
    | TextToProfileSearchResponse500
    | TextToProfileSearchResponse503
    | None
):
    r"""Search profiles from text

     Takes free-form text (e.g., 'Software engineers in US with 5+ years of experience') and returns a
    list of matching profiles.             The endpoint interprets natural language queries and applies
    structured filters such as job titles, seniority, skills, locations, past jobs, education, and
    languages to identify relevant people.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per profile found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToProfileSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TextToProfileSearchResponse200 | TextToProfileSearchResponse400 | TextToProfileSearchResponse401 | TextToProfileSearchResponse402 | TextToProfileSearchResponse403 | TextToProfileSearchResponse404 | TextToProfileSearchResponse429 | TextToProfileSearchResponse500 | TextToProfileSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
