from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.basic_work_email_reveal_body import BasicWorkEmailRevealBody
from ...models.basic_work_email_reveal_response_200 import BasicWorkEmailRevealResponse200
from ...models.basic_work_email_reveal_response_400 import BasicWorkEmailRevealResponse400
from ...models.basic_work_email_reveal_response_401 import BasicWorkEmailRevealResponse401
from ...models.basic_work_email_reveal_response_402 import BasicWorkEmailRevealResponse402
from ...models.basic_work_email_reveal_response_403 import BasicWorkEmailRevealResponse403
from ...models.basic_work_email_reveal_response_404 import BasicWorkEmailRevealResponse404
from ...models.basic_work_email_reveal_response_422 import BasicWorkEmailRevealResponse422
from ...models.basic_work_email_reveal_response_429 import BasicWorkEmailRevealResponse429
from ...models.basic_work_email_reveal_response_500 import BasicWorkEmailRevealResponse500
from ...models.basic_work_email_reveal_response_503 import BasicWorkEmailRevealResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: BasicWorkEmailRevealBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/basic-work-email",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BasicWorkEmailRevealResponse200
    | BasicWorkEmailRevealResponse400
    | BasicWorkEmailRevealResponse401
    | BasicWorkEmailRevealResponse402
    | BasicWorkEmailRevealResponse403
    | BasicWorkEmailRevealResponse404
    | BasicWorkEmailRevealResponse422
    | BasicWorkEmailRevealResponse429
    | BasicWorkEmailRevealResponse500
    | BasicWorkEmailRevealResponse503
    | None
):
    if response.status_code == 200:
        response_200 = BasicWorkEmailRevealResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BasicWorkEmailRevealResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BasicWorkEmailRevealResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = BasicWorkEmailRevealResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = BasicWorkEmailRevealResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = BasicWorkEmailRevealResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = BasicWorkEmailRevealResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = BasicWorkEmailRevealResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = BasicWorkEmailRevealResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = BasicWorkEmailRevealResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BasicWorkEmailRevealResponse200
    | BasicWorkEmailRevealResponse400
    | BasicWorkEmailRevealResponse401
    | BasicWorkEmailRevealResponse402
    | BasicWorkEmailRevealResponse403
    | BasicWorkEmailRevealResponse404
    | BasicWorkEmailRevealResponse422
    | BasicWorkEmailRevealResponse429
    | BasicWorkEmailRevealResponse500
    | BasicWorkEmailRevealResponse503
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
    body: BasicWorkEmailRevealBody,
) -> Response[
    BasicWorkEmailRevealResponse200
    | BasicWorkEmailRevealResponse400
    | BasicWorkEmailRevealResponse401
    | BasicWorkEmailRevealResponse402
    | BasicWorkEmailRevealResponse403
    | BasicWorkEmailRevealResponse404
    | BasicWorkEmailRevealResponse422
    | BasicWorkEmailRevealResponse429
    | BasicWorkEmailRevealResponse500
    | BasicWorkEmailRevealResponse503
]:
    """Find work email from name and company (no LinkedIn required)

     Finds a work email from a person's name and company information without requiring a LinkedIn
    profile. Useful when the person is not on LinkedIn.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per lite email reveal&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 4 minutes&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 4 minutes for this endpoint.">ⓘ</span></span>

    Args:
        body (BasicWorkEmailRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BasicWorkEmailRevealResponse200 | BasicWorkEmailRevealResponse400 | BasicWorkEmailRevealResponse401 | BasicWorkEmailRevealResponse402 | BasicWorkEmailRevealResponse403 | BasicWorkEmailRevealResponse404 | BasicWorkEmailRevealResponse422 | BasicWorkEmailRevealResponse429 | BasicWorkEmailRevealResponse500 | BasicWorkEmailRevealResponse503]
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
    body: BasicWorkEmailRevealBody,
) -> (
    BasicWorkEmailRevealResponse200
    | BasicWorkEmailRevealResponse400
    | BasicWorkEmailRevealResponse401
    | BasicWorkEmailRevealResponse402
    | BasicWorkEmailRevealResponse403
    | BasicWorkEmailRevealResponse404
    | BasicWorkEmailRevealResponse422
    | BasicWorkEmailRevealResponse429
    | BasicWorkEmailRevealResponse500
    | BasicWorkEmailRevealResponse503
    | None
):
    """Find work email from name and company (no LinkedIn required)

     Finds a work email from a person's name and company information without requiring a LinkedIn
    profile. Useful when the person is not on LinkedIn.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per lite email reveal&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 4 minutes&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 4 minutes for this endpoint.">ⓘ</span></span>

    Args:
        body (BasicWorkEmailRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BasicWorkEmailRevealResponse200 | BasicWorkEmailRevealResponse400 | BasicWorkEmailRevealResponse401 | BasicWorkEmailRevealResponse402 | BasicWorkEmailRevealResponse403 | BasicWorkEmailRevealResponse404 | BasicWorkEmailRevealResponse422 | BasicWorkEmailRevealResponse429 | BasicWorkEmailRevealResponse500 | BasicWorkEmailRevealResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BasicWorkEmailRevealBody,
) -> Response[
    BasicWorkEmailRevealResponse200
    | BasicWorkEmailRevealResponse400
    | BasicWorkEmailRevealResponse401
    | BasicWorkEmailRevealResponse402
    | BasicWorkEmailRevealResponse403
    | BasicWorkEmailRevealResponse404
    | BasicWorkEmailRevealResponse422
    | BasicWorkEmailRevealResponse429
    | BasicWorkEmailRevealResponse500
    | BasicWorkEmailRevealResponse503
]:
    """Find work email from name and company (no LinkedIn required)

     Finds a work email from a person's name and company information without requiring a LinkedIn
    profile. Useful when the person is not on LinkedIn.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per lite email reveal&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 4 minutes&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 4 minutes for this endpoint.">ⓘ</span></span>

    Args:
        body (BasicWorkEmailRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BasicWorkEmailRevealResponse200 | BasicWorkEmailRevealResponse400 | BasicWorkEmailRevealResponse401 | BasicWorkEmailRevealResponse402 | BasicWorkEmailRevealResponse403 | BasicWorkEmailRevealResponse404 | BasicWorkEmailRevealResponse422 | BasicWorkEmailRevealResponse429 | BasicWorkEmailRevealResponse500 | BasicWorkEmailRevealResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BasicWorkEmailRevealBody,
) -> (
    BasicWorkEmailRevealResponse200
    | BasicWorkEmailRevealResponse400
    | BasicWorkEmailRevealResponse401
    | BasicWorkEmailRevealResponse402
    | BasicWorkEmailRevealResponse403
    | BasicWorkEmailRevealResponse404
    | BasicWorkEmailRevealResponse422
    | BasicWorkEmailRevealResponse429
    | BasicWorkEmailRevealResponse500
    | BasicWorkEmailRevealResponse503
    | None
):
    """Find work email from name and company (no LinkedIn required)

     Finds a work email from a person's name and company information without requiring a LinkedIn
    profile. Useful when the person is not on LinkedIn.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per lite email reveal&nbsp;<span title="Pricing shown is
    default pricing. Actual pricing may vary.">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 4 minutes&nbsp;<span title="Recommended timeout: set
    your HTTP client timeout to at least 4 minutes for this endpoint.">ⓘ</span></span>

    Args:
        body (BasicWorkEmailRevealBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BasicWorkEmailRevealResponse200 | BasicWorkEmailRevealResponse400 | BasicWorkEmailRevealResponse401 | BasicWorkEmailRevealResponse402 | BasicWorkEmailRevealResponse403 | BasicWorkEmailRevealResponse404 | BasicWorkEmailRevealResponse422 | BasicWorkEmailRevealResponse429 | BasicWorkEmailRevealResponse500 | BasicWorkEmailRevealResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
