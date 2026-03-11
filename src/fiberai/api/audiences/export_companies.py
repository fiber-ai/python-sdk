from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_companies_body import ExportCompaniesBody
from ...models.export_companies_response_200 import ExportCompaniesResponse200
from ...models.export_companies_response_400 import ExportCompaniesResponse400
from ...models.export_companies_response_401 import ExportCompaniesResponse401
from ...models.export_companies_response_402 import ExportCompaniesResponse402
from ...models.export_companies_response_403 import ExportCompaniesResponse403
from ...models.export_companies_response_404 import ExportCompaniesResponse404
from ...models.export_companies_response_429 import ExportCompaniesResponse429
from ...models.export_companies_response_500 import ExportCompaniesResponse500
from ...models.export_companies_response_503 import ExportCompaniesResponse503
from ...types import Response


def _get_kwargs(
    audience_id: str,
    *,
    body: ExportCompaniesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/audiences/{audience_id}/export/companies".format(
            audience_id=quote(str(audience_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ExportCompaniesResponse200
    | ExportCompaniesResponse400
    | ExportCompaniesResponse401
    | ExportCompaniesResponse402
    | ExportCompaniesResponse403
    | ExportCompaniesResponse404
    | ExportCompaniesResponse429
    | ExportCompaniesResponse500
    | ExportCompaniesResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ExportCompaniesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ExportCompaniesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ExportCompaniesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ExportCompaniesResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ExportCompaniesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ExportCompaniesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ExportCompaniesResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ExportCompaniesResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ExportCompaniesResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ExportCompaniesResponse200
    | ExportCompaniesResponse400
    | ExportCompaniesResponse401
    | ExportCompaniesResponse402
    | ExportCompaniesResponse403
    | ExportCompaniesResponse404
    | ExportCompaniesResponse429
    | ExportCompaniesResponse500
    | ExportCompaniesResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExportCompaniesBody,
) -> Response[
    ExportCompaniesResponse200
    | ExportCompaniesResponse400
    | ExportCompaniesResponse401
    | ExportCompaniesResponse402
    | ExportCompaniesResponse403
    | ExportCompaniesResponse404
    | ExportCompaniesResponse429
    | ExportCompaniesResponse500
    | ExportCompaniesResponse503
]:
    r"""Export audience companies to CSV

     Triggers CSV export of companies in an audience. The export runs asynchronously - CSV links will be
    sent to the provided email address (if userEmail is provided) or returned in the API response.
    Export quota limits apply per usage period.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (ExportCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportCompaniesResponse200 | ExportCompaniesResponse400 | ExportCompaniesResponse401 | ExportCompaniesResponse402 | ExportCompaniesResponse403 | ExportCompaniesResponse404 | ExportCompaniesResponse429 | ExportCompaniesResponse500 | ExportCompaniesResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExportCompaniesBody,
) -> (
    ExportCompaniesResponse200
    | ExportCompaniesResponse400
    | ExportCompaniesResponse401
    | ExportCompaniesResponse402
    | ExportCompaniesResponse403
    | ExportCompaniesResponse404
    | ExportCompaniesResponse429
    | ExportCompaniesResponse500
    | ExportCompaniesResponse503
    | None
):
    r"""Export audience companies to CSV

     Triggers CSV export of companies in an audience. The export runs asynchronously - CSV links will be
    sent to the provided email address (if userEmail is provided) or returned in the API response.
    Export quota limits apply per usage period.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (ExportCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportCompaniesResponse200 | ExportCompaniesResponse400 | ExportCompaniesResponse401 | ExportCompaniesResponse402 | ExportCompaniesResponse403 | ExportCompaniesResponse404 | ExportCompaniesResponse429 | ExportCompaniesResponse500 | ExportCompaniesResponse503
    """

    return sync_detailed(
        audience_id=audience_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExportCompaniesBody,
) -> Response[
    ExportCompaniesResponse200
    | ExportCompaniesResponse400
    | ExportCompaniesResponse401
    | ExportCompaniesResponse402
    | ExportCompaniesResponse403
    | ExportCompaniesResponse404
    | ExportCompaniesResponse429
    | ExportCompaniesResponse500
    | ExportCompaniesResponse503
]:
    r"""Export audience companies to CSV

     Triggers CSV export of companies in an audience. The export runs asynchronously - CSV links will be
    sent to the provided email address (if userEmail is provided) or returned in the API response.
    Export quota limits apply per usage period.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (ExportCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportCompaniesResponse200 | ExportCompaniesResponse400 | ExportCompaniesResponse401 | ExportCompaniesResponse402 | ExportCompaniesResponse403 | ExportCompaniesResponse404 | ExportCompaniesResponse429 | ExportCompaniesResponse500 | ExportCompaniesResponse503]
    """

    kwargs = _get_kwargs(
        audience_id=audience_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audience_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExportCompaniesBody,
) -> (
    ExportCompaniesResponse200
    | ExportCompaniesResponse400
    | ExportCompaniesResponse401
    | ExportCompaniesResponse402
    | ExportCompaniesResponse403
    | ExportCompaniesResponse404
    | ExportCompaniesResponse429
    | ExportCompaniesResponse500
    | ExportCompaniesResponse503
    | None
):
    r"""Export audience companies to CSV

     Triggers CSV export of companies in an audience. The export runs asynchronously - CSV links will be
    sent to the provided email address (if userEmail is provided) or returned in the API response.
    Export quota limits apply per usage period.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (ExportCompaniesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportCompaniesResponse200 | ExportCompaniesResponse400 | ExportCompaniesResponse401 | ExportCompaniesResponse402 | ExportCompaniesResponse403 | ExportCompaniesResponse404 | ExportCompaniesResponse429 | ExportCompaniesResponse500 | ExportCompaniesResponse503
    """

    return (
        await asyncio_detailed(
            audience_id=audience_id,
            client=client,
            body=body,
        )
    ).parsed
