from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.text_to_profile_search_params_body import TextToProfileSearchParamsBody
from ...models.text_to_profile_search_params_response_200 import TextToProfileSearchParamsResponse200
from ...models.text_to_profile_search_params_response_400 import TextToProfileSearchParamsResponse400
from ...models.text_to_profile_search_params_response_401 import TextToProfileSearchParamsResponse401
from ...models.text_to_profile_search_params_response_402 import TextToProfileSearchParamsResponse402
from ...models.text_to_profile_search_params_response_403 import TextToProfileSearchParamsResponse403
from ...models.text_to_profile_search_params_response_404 import TextToProfileSearchParamsResponse404
from ...models.text_to_profile_search_params_response_429 import TextToProfileSearchParamsResponse429
from ...models.text_to_profile_search_params_response_500 import TextToProfileSearchParamsResponse500
from ...models.text_to_profile_search_params_response_503 import TextToProfileSearchParamsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: TextToProfileSearchParamsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/text-to-search-params/profiles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TextToProfileSearchParamsResponse200
    | TextToProfileSearchParamsResponse400
    | TextToProfileSearchParamsResponse401
    | TextToProfileSearchParamsResponse402
    | TextToProfileSearchParamsResponse403
    | TextToProfileSearchParamsResponse404
    | TextToProfileSearchParamsResponse429
    | TextToProfileSearchParamsResponse500
    | TextToProfileSearchParamsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = TextToProfileSearchParamsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TextToProfileSearchParamsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TextToProfileSearchParamsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = TextToProfileSearchParamsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = TextToProfileSearchParamsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TextToProfileSearchParamsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = TextToProfileSearchParamsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = TextToProfileSearchParamsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = TextToProfileSearchParamsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TextToProfileSearchParamsResponse200
    | TextToProfileSearchParamsResponse400
    | TextToProfileSearchParamsResponse401
    | TextToProfileSearchParamsResponse402
    | TextToProfileSearchParamsResponse403
    | TextToProfileSearchParamsResponse404
    | TextToProfileSearchParamsResponse429
    | TextToProfileSearchParamsResponse500
    | TextToProfileSearchParamsResponse503
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
    body: TextToProfileSearchParamsBody,
) -> Response[
    TextToProfileSearchParamsResponse200
    | TextToProfileSearchParamsResponse400
    | TextToProfileSearchParamsResponse401
    | TextToProfileSearchParamsResponse402
    | TextToProfileSearchParamsResponse403
    | TextToProfileSearchParamsResponse404
    | TextToProfileSearchParamsResponse429
    | TextToProfileSearchParamsResponse500
    | TextToProfileSearchParamsResponse503
]:
    r"""Convert text into profile search filters

     Takes free-form text (e.g., 'Software engineers in US with 5+ years of experience') and converts it
    into a structured set of filters for profile search.           This endpoint helps transform natural
    language queries into standardized search parameters such as job titles, skills, seniority,
    locations, past experiences, education, languages, and more.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToProfileSearchParamsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TextToProfileSearchParamsResponse200 | TextToProfileSearchParamsResponse400 | TextToProfileSearchParamsResponse401 | TextToProfileSearchParamsResponse402 | TextToProfileSearchParamsResponse403 | TextToProfileSearchParamsResponse404 | TextToProfileSearchParamsResponse429 | TextToProfileSearchParamsResponse500 | TextToProfileSearchParamsResponse503]
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
    body: TextToProfileSearchParamsBody,
) -> (
    TextToProfileSearchParamsResponse200
    | TextToProfileSearchParamsResponse400
    | TextToProfileSearchParamsResponse401
    | TextToProfileSearchParamsResponse402
    | TextToProfileSearchParamsResponse403
    | TextToProfileSearchParamsResponse404
    | TextToProfileSearchParamsResponse429
    | TextToProfileSearchParamsResponse500
    | TextToProfileSearchParamsResponse503
    | None
):
    r"""Convert text into profile search filters

     Takes free-form text (e.g., 'Software engineers in US with 5+ years of experience') and converts it
    into a structured set of filters for profile search.           This endpoint helps transform natural
    language queries into standardized search parameters such as job titles, skills, seniority,
    locations, past experiences, education, languages, and more.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToProfileSearchParamsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TextToProfileSearchParamsResponse200 | TextToProfileSearchParamsResponse400 | TextToProfileSearchParamsResponse401 | TextToProfileSearchParamsResponse402 | TextToProfileSearchParamsResponse403 | TextToProfileSearchParamsResponse404 | TextToProfileSearchParamsResponse429 | TextToProfileSearchParamsResponse500 | TextToProfileSearchParamsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TextToProfileSearchParamsBody,
) -> Response[
    TextToProfileSearchParamsResponse200
    | TextToProfileSearchParamsResponse400
    | TextToProfileSearchParamsResponse401
    | TextToProfileSearchParamsResponse402
    | TextToProfileSearchParamsResponse403
    | TextToProfileSearchParamsResponse404
    | TextToProfileSearchParamsResponse429
    | TextToProfileSearchParamsResponse500
    | TextToProfileSearchParamsResponse503
]:
    r"""Convert text into profile search filters

     Takes free-form text (e.g., 'Software engineers in US with 5+ years of experience') and converts it
    into a structured set of filters for profile search.           This endpoint helps transform natural
    language queries into standardized search parameters such as job titles, skills, seniority,
    locations, past experiences, education, languages, and more.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToProfileSearchParamsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TextToProfileSearchParamsResponse200 | TextToProfileSearchParamsResponse400 | TextToProfileSearchParamsResponse401 | TextToProfileSearchParamsResponse402 | TextToProfileSearchParamsResponse403 | TextToProfileSearchParamsResponse404 | TextToProfileSearchParamsResponse429 | TextToProfileSearchParamsResponse500 | TextToProfileSearchParamsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TextToProfileSearchParamsBody,
) -> (
    TextToProfileSearchParamsResponse200
    | TextToProfileSearchParamsResponse400
    | TextToProfileSearchParamsResponse401
    | TextToProfileSearchParamsResponse402
    | TextToProfileSearchParamsResponse403
    | TextToProfileSearchParamsResponse404
    | TextToProfileSearchParamsResponse429
    | TextToProfileSearchParamsResponse500
    | TextToProfileSearchParamsResponse503
    | None
):
    r"""Convert text into profile search filters

     Takes free-form text (e.g., 'Software engineers in US with 5+ years of experience') and converts it
    into a structured set of filters for profile search.           This endpoint helps transform natural
    language queries into standardized search parameters such as job titles, skills, seniority,
    locations, past experiences, education, languages, and more.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (TextToProfileSearchParamsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TextToProfileSearchParamsResponse200 | TextToProfileSearchParamsResponse400 | TextToProfileSearchParamsResponse401 | TextToProfileSearchParamsResponse402 | TextToProfileSearchParamsResponse403 | TextToProfileSearchParamsResponse404 | TextToProfileSearchParamsResponse429 | TextToProfileSearchParamsResponse500 | TextToProfileSearchParamsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
