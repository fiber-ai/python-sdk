from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_prospects_body import ExportProspectsBody
from ...models.export_prospects_response_200 import ExportProspectsResponse200
from ...models.export_prospects_response_400 import ExportProspectsResponse400
from ...models.export_prospects_response_401 import ExportProspectsResponse401
from ...models.export_prospects_response_402 import ExportProspectsResponse402
from ...models.export_prospects_response_403 import ExportProspectsResponse403
from ...models.export_prospects_response_404 import ExportProspectsResponse404
from ...models.export_prospects_response_429 import ExportProspectsResponse429
from ...models.export_prospects_response_500 import ExportProspectsResponse500
from ...models.export_prospects_response_503 import ExportProspectsResponse503
from ...types import Response


def _get_kwargs(
    audience_id: str,
    *,
    body: ExportProspectsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/audiences/{audience_id}/export/prospects".format(
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
    ExportProspectsResponse200
    | ExportProspectsResponse400
    | ExportProspectsResponse401
    | ExportProspectsResponse402
    | ExportProspectsResponse403
    | ExportProspectsResponse404
    | ExportProspectsResponse429
    | ExportProspectsResponse500
    | ExportProspectsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ExportProspectsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ExportProspectsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ExportProspectsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ExportProspectsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ExportProspectsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ExportProspectsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ExportProspectsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ExportProspectsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ExportProspectsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ExportProspectsResponse200
    | ExportProspectsResponse400
    | ExportProspectsResponse401
    | ExportProspectsResponse402
    | ExportProspectsResponse403
    | ExportProspectsResponse404
    | ExportProspectsResponse429
    | ExportProspectsResponse500
    | ExportProspectsResponse503
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
    body: ExportProspectsBody,
) -> Response[
    ExportProspectsResponse200
    | ExportProspectsResponse400
    | ExportProspectsResponse401
    | ExportProspectsResponse402
    | ExportProspectsResponse403
    | ExportProspectsResponse404
    | ExportProspectsResponse429
    | ExportProspectsResponse500
    | ExportProspectsResponse503
]:
    r"""Export audience prospects to CSV

     Triggers CSV export of prospects (people) in an audience. The export runs asynchronously - CSV links
    will be sent to the provided email address (if userEmail is provided) or returned in the API
    response. Export quota limits apply per usage period. Optionally filter to only export prospects
    with verified emails or phones.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (ExportProspectsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportProspectsResponse200 | ExportProspectsResponse400 | ExportProspectsResponse401 | ExportProspectsResponse402 | ExportProspectsResponse403 | ExportProspectsResponse404 | ExportProspectsResponse429 | ExportProspectsResponse500 | ExportProspectsResponse503]
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
    body: ExportProspectsBody,
) -> (
    ExportProspectsResponse200
    | ExportProspectsResponse400
    | ExportProspectsResponse401
    | ExportProspectsResponse402
    | ExportProspectsResponse403
    | ExportProspectsResponse404
    | ExportProspectsResponse429
    | ExportProspectsResponse500
    | ExportProspectsResponse503
    | None
):
    r"""Export audience prospects to CSV

     Triggers CSV export of prospects (people) in an audience. The export runs asynchronously - CSV links
    will be sent to the provided email address (if userEmail is provided) or returned in the API
    response. Export quota limits apply per usage period. Optionally filter to only export prospects
    with verified emails or phones.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (ExportProspectsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportProspectsResponse200 | ExportProspectsResponse400 | ExportProspectsResponse401 | ExportProspectsResponse402 | ExportProspectsResponse403 | ExportProspectsResponse404 | ExportProspectsResponse429 | ExportProspectsResponse500 | ExportProspectsResponse503
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
    body: ExportProspectsBody,
) -> Response[
    ExportProspectsResponse200
    | ExportProspectsResponse400
    | ExportProspectsResponse401
    | ExportProspectsResponse402
    | ExportProspectsResponse403
    | ExportProspectsResponse404
    | ExportProspectsResponse429
    | ExportProspectsResponse500
    | ExportProspectsResponse503
]:
    r"""Export audience prospects to CSV

     Triggers CSV export of prospects (people) in an audience. The export runs asynchronously - CSV links
    will be sent to the provided email address (if userEmail is provided) or returned in the API
    response. Export quota limits apply per usage period. Optionally filter to only export prospects
    with verified emails or phones.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (ExportProspectsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportProspectsResponse200 | ExportProspectsResponse400 | ExportProspectsResponse401 | ExportProspectsResponse402 | ExportProspectsResponse403 | ExportProspectsResponse404 | ExportProspectsResponse429 | ExportProspectsResponse500 | ExportProspectsResponse503]
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
    body: ExportProspectsBody,
) -> (
    ExportProspectsResponse200
    | ExportProspectsResponse400
    | ExportProspectsResponse401
    | ExportProspectsResponse402
    | ExportProspectsResponse403
    | ExportProspectsResponse404
    | ExportProspectsResponse429
    | ExportProspectsResponse500
    | ExportProspectsResponse503
    | None
):
    r"""Export audience prospects to CSV

     Triggers CSV export of prospects (people) in an audience. The export runs asynchronously - CSV links
    will be sent to the provided email address (if userEmail is provided) or returned in the API
    response. Export quota limits apply per usage period. Optionally filter to only export prospects
    with verified emails or phones.

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        audience_id (str):
        body (ExportProspectsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportProspectsResponse200 | ExportProspectsResponse400 | ExportProspectsResponse401 | ExportProspectsResponse402 | ExportProspectsResponse403 | ExportProspectsResponse404 | ExportProspectsResponse429 | ExportProspectsResponse500 | ExportProspectsResponse503
    """

    return (
        await asyncio_detailed(
            audience_id=audience_id,
            client=client,
            body=body,
        )
    ).parsed
