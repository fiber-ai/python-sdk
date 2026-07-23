from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_logo_body import CompanyLogoBody
from ...models.company_logo_response_200 import CompanyLogoResponse200
from ...models.company_logo_response_400 import CompanyLogoResponse400
from ...models.company_logo_response_401 import CompanyLogoResponse401
from ...models.company_logo_response_402 import CompanyLogoResponse402
from ...models.company_logo_response_403 import CompanyLogoResponse403
from ...models.company_logo_response_404 import CompanyLogoResponse404
from ...models.company_logo_response_422 import CompanyLogoResponse422
from ...models.company_logo_response_429 import CompanyLogoResponse429
from ...models.company_logo_response_500 import CompanyLogoResponse500
from ...models.company_logo_response_503 import CompanyLogoResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CompanyLogoBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/company-logos/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CompanyLogoResponse200
    | CompanyLogoResponse400
    | CompanyLogoResponse401
    | CompanyLogoResponse402
    | CompanyLogoResponse403
    | CompanyLogoResponse404
    | CompanyLogoResponse422
    | CompanyLogoResponse429
    | CompanyLogoResponse500
    | CompanyLogoResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CompanyLogoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CompanyLogoResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CompanyLogoResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CompanyLogoResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CompanyLogoResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CompanyLogoResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = CompanyLogoResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = CompanyLogoResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CompanyLogoResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CompanyLogoResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CompanyLogoResponse200
    | CompanyLogoResponse400
    | CompanyLogoResponse401
    | CompanyLogoResponse402
    | CompanyLogoResponse403
    | CompanyLogoResponse404
    | CompanyLogoResponse422
    | CompanyLogoResponse429
    | CompanyLogoResponse500
    | CompanyLogoResponse503
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
    body: CompanyLogoBody,
) -> Response[
    CompanyLogoResponse200
    | CompanyLogoResponse400
    | CompanyLogoResponse401
    | CompanyLogoResponse402
    | CompanyLogoResponse403
    | CompanyLogoResponse404
    | CompanyLogoResponse422
    | CompanyLogoResponse429
    | CompanyLogoResponse500
    | CompanyLogoResponse503
]:
    r"""Company logo

     Get the logo for a single company. Accepts a LinkedIn company URL, slug, numeric organization ID, or
    domain — the format is auto-detected.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per company logo lookup&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (CompanyLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyLogoResponse200 | CompanyLogoResponse400 | CompanyLogoResponse401 | CompanyLogoResponse402 | CompanyLogoResponse403 | CompanyLogoResponse404 | CompanyLogoResponse422 | CompanyLogoResponse429 | CompanyLogoResponse500 | CompanyLogoResponse503]
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
    body: CompanyLogoBody,
) -> (
    CompanyLogoResponse200
    | CompanyLogoResponse400
    | CompanyLogoResponse401
    | CompanyLogoResponse402
    | CompanyLogoResponse403
    | CompanyLogoResponse404
    | CompanyLogoResponse422
    | CompanyLogoResponse429
    | CompanyLogoResponse500
    | CompanyLogoResponse503
    | None
):
    r"""Company logo

     Get the logo for a single company. Accepts a LinkedIn company URL, slug, numeric organization ID, or
    domain — the format is auto-detected.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per company logo lookup&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (CompanyLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyLogoResponse200 | CompanyLogoResponse400 | CompanyLogoResponse401 | CompanyLogoResponse402 | CompanyLogoResponse403 | CompanyLogoResponse404 | CompanyLogoResponse422 | CompanyLogoResponse429 | CompanyLogoResponse500 | CompanyLogoResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompanyLogoBody,
) -> Response[
    CompanyLogoResponse200
    | CompanyLogoResponse400
    | CompanyLogoResponse401
    | CompanyLogoResponse402
    | CompanyLogoResponse403
    | CompanyLogoResponse404
    | CompanyLogoResponse422
    | CompanyLogoResponse429
    | CompanyLogoResponse500
    | CompanyLogoResponse503
]:
    r"""Company logo

     Get the logo for a single company. Accepts a LinkedIn company URL, slug, numeric organization ID, or
    domain — the format is auto-detected.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per company logo lookup&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (CompanyLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyLogoResponse200 | CompanyLogoResponse400 | CompanyLogoResponse401 | CompanyLogoResponse402 | CompanyLogoResponse403 | CompanyLogoResponse404 | CompanyLogoResponse422 | CompanyLogoResponse429 | CompanyLogoResponse500 | CompanyLogoResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CompanyLogoBody,
) -> (
    CompanyLogoResponse200
    | CompanyLogoResponse400
    | CompanyLogoResponse401
    | CompanyLogoResponse402
    | CompanyLogoResponse403
    | CompanyLogoResponse404
    | CompanyLogoResponse422
    | CompanyLogoResponse429
    | CompanyLogoResponse500
    | CompanyLogoResponse503
    | None
):
    r"""Company logo

     Get the logo for a single company. Accepts a LinkedIn company URL, slug, numeric organization ID, or
    domain — the format is auto-detected.

    <span>⚡ <strong>Rate limit:</strong> 600 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 0.33 credits per company logo lookup&nbsp;<span title=\"Pricing shown
    is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (CompanyLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyLogoResponse200 | CompanyLogoResponse400 | CompanyLogoResponse401 | CompanyLogoResponse402 | CompanyLogoResponse403 | CompanyLogoResponse404 | CompanyLogoResponse422 | CompanyLogoResponse429 | CompanyLogoResponse500 | CompanyLogoResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
