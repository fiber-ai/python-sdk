from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.jd_to_profile_search_body import JdToProfileSearchBody
from ...models.jd_to_profile_search_response_200 import JdToProfileSearchResponse200
from ...models.jd_to_profile_search_response_400 import JdToProfileSearchResponse400
from ...models.jd_to_profile_search_response_401 import JdToProfileSearchResponse401
from ...models.jd_to_profile_search_response_402 import JdToProfileSearchResponse402
from ...models.jd_to_profile_search_response_403 import JdToProfileSearchResponse403
from ...models.jd_to_profile_search_response_404 import JdToProfileSearchResponse404
from ...models.jd_to_profile_search_response_429 import JdToProfileSearchResponse429
from ...models.jd_to_profile_search_response_500 import JdToProfileSearchResponse500
from ...models.jd_to_profile_search_response_503 import JdToProfileSearchResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: JdToProfileSearchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/natural-language-search/job-description-search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    JdToProfileSearchResponse200
    | JdToProfileSearchResponse400
    | JdToProfileSearchResponse401
    | JdToProfileSearchResponse402
    | JdToProfileSearchResponse403
    | JdToProfileSearchResponse404
    | JdToProfileSearchResponse429
    | JdToProfileSearchResponse500
    | JdToProfileSearchResponse503
    | None
):
    if response.status_code == 200:
        response_200 = JdToProfileSearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = JdToProfileSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = JdToProfileSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = JdToProfileSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = JdToProfileSearchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = JdToProfileSearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = JdToProfileSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = JdToProfileSearchResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = JdToProfileSearchResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    JdToProfileSearchResponse200
    | JdToProfileSearchResponse400
    | JdToProfileSearchResponse401
    | JdToProfileSearchResponse402
    | JdToProfileSearchResponse403
    | JdToProfileSearchResponse404
    | JdToProfileSearchResponse429
    | JdToProfileSearchResponse500
    | JdToProfileSearchResponse503
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
    body: JdToProfileSearchBody,
) -> Response[
    JdToProfileSearchResponse200
    | JdToProfileSearchResponse400
    | JdToProfileSearchResponse401
    | JdToProfileSearchResponse402
    | JdToProfileSearchResponse403
    | JdToProfileSearchResponse404
    | JdToProfileSearchResponse429
    | JdToProfileSearchResponse500
    | JdToProfileSearchResponse503
]:
    r"""Search profiles from a job description

     Accepts a raw job description and returns a list of matching LinkedIn profiles. Optionally returns
    detailed work experience and education history. Results are paginated via cursor. Credits are
    charged per request and per profile returned.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per profile found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JdToProfileSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JdToProfileSearchResponse200 | JdToProfileSearchResponse400 | JdToProfileSearchResponse401 | JdToProfileSearchResponse402 | JdToProfileSearchResponse403 | JdToProfileSearchResponse404 | JdToProfileSearchResponse429 | JdToProfileSearchResponse500 | JdToProfileSearchResponse503]
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
    body: JdToProfileSearchBody,
) -> (
    JdToProfileSearchResponse200
    | JdToProfileSearchResponse400
    | JdToProfileSearchResponse401
    | JdToProfileSearchResponse402
    | JdToProfileSearchResponse403
    | JdToProfileSearchResponse404
    | JdToProfileSearchResponse429
    | JdToProfileSearchResponse500
    | JdToProfileSearchResponse503
    | None
):
    r"""Search profiles from a job description

     Accepts a raw job description and returns a list of matching LinkedIn profiles. Optionally returns
    detailed work experience and education history. Results are paginated via cursor. Credits are
    charged per request and per profile returned.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per profile found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JdToProfileSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JdToProfileSearchResponse200 | JdToProfileSearchResponse400 | JdToProfileSearchResponse401 | JdToProfileSearchResponse402 | JdToProfileSearchResponse403 | JdToProfileSearchResponse404 | JdToProfileSearchResponse429 | JdToProfileSearchResponse500 | JdToProfileSearchResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JdToProfileSearchBody,
) -> Response[
    JdToProfileSearchResponse200
    | JdToProfileSearchResponse400
    | JdToProfileSearchResponse401
    | JdToProfileSearchResponse402
    | JdToProfileSearchResponse403
    | JdToProfileSearchResponse404
    | JdToProfileSearchResponse429
    | JdToProfileSearchResponse500
    | JdToProfileSearchResponse503
]:
    r"""Search profiles from a job description

     Accepts a raw job description and returns a list of matching LinkedIn profiles. Optionally returns
    detailed work experience and education history. Results are paginated via cursor. Credits are
    charged per request and per profile returned.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per profile found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JdToProfileSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JdToProfileSearchResponse200 | JdToProfileSearchResponse400 | JdToProfileSearchResponse401 | JdToProfileSearchResponse402 | JdToProfileSearchResponse403 | JdToProfileSearchResponse404 | JdToProfileSearchResponse429 | JdToProfileSearchResponse500 | JdToProfileSearchResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: JdToProfileSearchBody,
) -> (
    JdToProfileSearchResponse200
    | JdToProfileSearchResponse400
    | JdToProfileSearchResponse401
    | JdToProfileSearchResponse402
    | JdToProfileSearchResponse403
    | JdToProfileSearchResponse404
    | JdToProfileSearchResponse429
    | JdToProfileSearchResponse500
    | JdToProfileSearchResponse503
    | None
):
    r"""Search profiles from a job description

     Accepts a raw job description and returns a list of matching LinkedIn profiles. Optionally returns
    detailed work experience and education history. Results are paginated via cursor. Credits are
    charged per request and per profile returned.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per request + 1 credit per profile found&nbsp;<span
    title=\"Pricing shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JdToProfileSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JdToProfileSearchResponse200 | JdToProfileSearchResponse400 | JdToProfileSearchResponse401 | JdToProfileSearchResponse402 | JdToProfileSearchResponse403 | JdToProfileSearchResponse404 | JdToProfileSearchResponse429 | JdToProfileSearchResponse500 | JdToProfileSearchResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
