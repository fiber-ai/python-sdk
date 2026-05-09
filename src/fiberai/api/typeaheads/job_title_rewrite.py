from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_title_rewrite_body import JobTitleRewriteBody
from ...models.job_title_rewrite_response_200 import JobTitleRewriteResponse200
from ...models.job_title_rewrite_response_400 import JobTitleRewriteResponse400
from ...models.job_title_rewrite_response_401 import JobTitleRewriteResponse401
from ...models.job_title_rewrite_response_402 import JobTitleRewriteResponse402
from ...models.job_title_rewrite_response_403 import JobTitleRewriteResponse403
from ...models.job_title_rewrite_response_404 import JobTitleRewriteResponse404
from ...models.job_title_rewrite_response_429 import JobTitleRewriteResponse429
from ...models.job_title_rewrite_response_500 import JobTitleRewriteResponse500
from ...models.job_title_rewrite_response_503 import JobTitleRewriteResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: JobTitleRewriteBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/typeahead/job-title",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    JobTitleRewriteResponse200
    | JobTitleRewriteResponse400
    | JobTitleRewriteResponse401
    | JobTitleRewriteResponse402
    | JobTitleRewriteResponse403
    | JobTitleRewriteResponse404
    | JobTitleRewriteResponse429
    | JobTitleRewriteResponse500
    | JobTitleRewriteResponse503
    | None
):
    if response.status_code == 200:
        response_200 = JobTitleRewriteResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = JobTitleRewriteResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = JobTitleRewriteResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = JobTitleRewriteResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = JobTitleRewriteResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = JobTitleRewriteResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = JobTitleRewriteResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = JobTitleRewriteResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = JobTitleRewriteResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    JobTitleRewriteResponse200
    | JobTitleRewriteResponse400
    | JobTitleRewriteResponse401
    | JobTitleRewriteResponse402
    | JobTitleRewriteResponse403
    | JobTitleRewriteResponse404
    | JobTitleRewriteResponse429
    | JobTitleRewriteResponse500
    | JobTitleRewriteResponse503
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
    body: JobTitleRewriteBody,
) -> Response[
    JobTitleRewriteResponse200
    | JobTitleRewriteResponse400
    | JobTitleRewriteResponse401
    | JobTitleRewriteResponse402
    | JobTitleRewriteResponse403
    | JobTitleRewriteResponse404
    | JobTitleRewriteResponse429
    | JobTitleRewriteResponse500
    | JobTitleRewriteResponse503
]:
    r"""Job Title Synonym Expansion

     Expand a job title into synonyms and related variations. Useful for broadening job title searches to
    improve yield.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JobTitleRewriteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobTitleRewriteResponse200 | JobTitleRewriteResponse400 | JobTitleRewriteResponse401 | JobTitleRewriteResponse402 | JobTitleRewriteResponse403 | JobTitleRewriteResponse404 | JobTitleRewriteResponse429 | JobTitleRewriteResponse500 | JobTitleRewriteResponse503]
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
    body: JobTitleRewriteBody,
) -> (
    JobTitleRewriteResponse200
    | JobTitleRewriteResponse400
    | JobTitleRewriteResponse401
    | JobTitleRewriteResponse402
    | JobTitleRewriteResponse403
    | JobTitleRewriteResponse404
    | JobTitleRewriteResponse429
    | JobTitleRewriteResponse500
    | JobTitleRewriteResponse503
    | None
):
    r"""Job Title Synonym Expansion

     Expand a job title into synonyms and related variations. Useful for broadening job title searches to
    improve yield.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JobTitleRewriteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobTitleRewriteResponse200 | JobTitleRewriteResponse400 | JobTitleRewriteResponse401 | JobTitleRewriteResponse402 | JobTitleRewriteResponse403 | JobTitleRewriteResponse404 | JobTitleRewriteResponse429 | JobTitleRewriteResponse500 | JobTitleRewriteResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobTitleRewriteBody,
) -> Response[
    JobTitleRewriteResponse200
    | JobTitleRewriteResponse400
    | JobTitleRewriteResponse401
    | JobTitleRewriteResponse402
    | JobTitleRewriteResponse403
    | JobTitleRewriteResponse404
    | JobTitleRewriteResponse429
    | JobTitleRewriteResponse500
    | JobTitleRewriteResponse503
]:
    r"""Job Title Synonym Expansion

     Expand a job title into synonyms and related variations. Useful for broadening job title searches to
    improve yield.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JobTitleRewriteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobTitleRewriteResponse200 | JobTitleRewriteResponse400 | JobTitleRewriteResponse401 | JobTitleRewriteResponse402 | JobTitleRewriteResponse403 | JobTitleRewriteResponse404 | JobTitleRewriteResponse429 | JobTitleRewriteResponse500 | JobTitleRewriteResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: JobTitleRewriteBody,
) -> (
    JobTitleRewriteResponse200
    | JobTitleRewriteResponse400
    | JobTitleRewriteResponse401
    | JobTitleRewriteResponse402
    | JobTitleRewriteResponse403
    | JobTitleRewriteResponse404
    | JobTitleRewriteResponse429
    | JobTitleRewriteResponse500
    | JobTitleRewriteResponse503
    | None
):
    r"""Job Title Synonym Expansion

     Expand a job title into synonyms and related variations. Useful for broadening job title searches to
    improve yield.

    <span>⚡ <strong>Rate limit:</strong> 240 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per request&nbsp;<span title=\"Pricing shown is default
    pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JobTitleRewriteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobTitleRewriteResponse200 | JobTitleRewriteResponse400 | JobTitleRewriteResponse401 | JobTitleRewriteResponse402 | JobTitleRewriteResponse403 | JobTitleRewriteResponse404 | JobTitleRewriteResponse429 | JobTitleRewriteResponse500 | JobTitleRewriteResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
