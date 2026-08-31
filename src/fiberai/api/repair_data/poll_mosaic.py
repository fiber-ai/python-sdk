from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.poll_mosaic_body import PollMosaicBody
from ...models.poll_mosaic_response_200 import PollMosaicResponse200
from ...models.poll_mosaic_response_400 import PollMosaicResponse400
from ...models.poll_mosaic_response_401 import PollMosaicResponse401
from ...models.poll_mosaic_response_402 import PollMosaicResponse402
from ...models.poll_mosaic_response_403 import PollMosaicResponse403
from ...models.poll_mosaic_response_404 import PollMosaicResponse404
from ...models.poll_mosaic_response_422 import PollMosaicResponse422
from ...models.poll_mosaic_response_429 import PollMosaicResponse429
from ...models.poll_mosaic_response_500 import PollMosaicResponse500
from ...models.poll_mosaic_response_503 import PollMosaicResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PollMosaicBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/mosaic/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PollMosaicResponse200
    | PollMosaicResponse400
    | PollMosaicResponse401
    | PollMosaicResponse402
    | PollMosaicResponse403
    | PollMosaicResponse404
    | PollMosaicResponse422
    | PollMosaicResponse429
    | PollMosaicResponse500
    | PollMosaicResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PollMosaicResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PollMosaicResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PollMosaicResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PollMosaicResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PollMosaicResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PollMosaicResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PollMosaicResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PollMosaicResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PollMosaicResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PollMosaicResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PollMosaicResponse200
    | PollMosaicResponse400
    | PollMosaicResponse401
    | PollMosaicResponse402
    | PollMosaicResponse403
    | PollMosaicResponse404
    | PollMosaicResponse422
    | PollMosaicResponse429
    | PollMosaicResponse500
    | PollMosaicResponse503
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
    body: PollMosaicBody,
) -> Response[
    PollMosaicResponse200
    | PollMosaicResponse400
    | PollMosaicResponse401
    | PollMosaicResponse402
    | PollMosaicResponse403
    | PollMosaicResponse404
    | PollMosaicResponse422
    | PollMosaicResponse429
    | PollMosaicResponse500
    | PollMosaicResponse503
]:
    """Poll Mosaic run status

     Retrieves the status of a Mosaic job started by `/mosaic/start`. When the run is done, the response
    includes temporary download links for the enriched CSV and the summary report.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (PollMosaicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollMosaicResponse200 | PollMosaicResponse400 | PollMosaicResponse401 | PollMosaicResponse402 | PollMosaicResponse403 | PollMosaicResponse404 | PollMosaicResponse422 | PollMosaicResponse429 | PollMosaicResponse500 | PollMosaicResponse503]
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
    body: PollMosaicBody,
) -> (
    PollMosaicResponse200
    | PollMosaicResponse400
    | PollMosaicResponse401
    | PollMosaicResponse402
    | PollMosaicResponse403
    | PollMosaicResponse404
    | PollMosaicResponse422
    | PollMosaicResponse429
    | PollMosaicResponse500
    | PollMosaicResponse503
    | None
):
    """Poll Mosaic run status

     Retrieves the status of a Mosaic job started by `/mosaic/start`. When the run is done, the response
    includes temporary download links for the enriched CSV and the summary report.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (PollMosaicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollMosaicResponse200 | PollMosaicResponse400 | PollMosaicResponse401 | PollMosaicResponse402 | PollMosaicResponse403 | PollMosaicResponse404 | PollMosaicResponse422 | PollMosaicResponse429 | PollMosaicResponse500 | PollMosaicResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PollMosaicBody,
) -> Response[
    PollMosaicResponse200
    | PollMosaicResponse400
    | PollMosaicResponse401
    | PollMosaicResponse402
    | PollMosaicResponse403
    | PollMosaicResponse404
    | PollMosaicResponse422
    | PollMosaicResponse429
    | PollMosaicResponse500
    | PollMosaicResponse503
]:
    """Poll Mosaic run status

     Retrieves the status of a Mosaic job started by `/mosaic/start`. When the run is done, the response
    includes temporary download links for the enriched CSV and the summary report.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (PollMosaicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PollMosaicResponse200 | PollMosaicResponse400 | PollMosaicResponse401 | PollMosaicResponse402 | PollMosaicResponse403 | PollMosaicResponse404 | PollMosaicResponse422 | PollMosaicResponse429 | PollMosaicResponse500 | PollMosaicResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PollMosaicBody,
) -> (
    PollMosaicResponse200
    | PollMosaicResponse400
    | PollMosaicResponse401
    | PollMosaicResponse402
    | PollMosaicResponse403
    | PollMosaicResponse404
    | PollMosaicResponse422
    | PollMosaicResponse429
    | PollMosaicResponse500
    | PollMosaicResponse503
    | None
):
    """Poll Mosaic run status

     Retrieves the status of a Mosaic job started by `/mosaic/start`. When the run is done, the response
    includes temporary download links for the enriched CSV and the summary report.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (PollMosaicBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PollMosaicResponse200 | PollMosaicResponse400 | PollMosaicResponse401 | PollMosaicResponse402 | PollMosaicResponse403 | PollMosaicResponse404 | PollMosaicResponse422 | PollMosaicResponse429 | PollMosaicResponse500 | PollMosaicResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
