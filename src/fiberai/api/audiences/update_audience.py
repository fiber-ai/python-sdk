from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_audience_body import UpdateAudienceBody
from ...models.update_audience_response_200 import UpdateAudienceResponse200
from ...models.update_audience_response_400 import UpdateAudienceResponse400
from ...models.update_audience_response_401 import UpdateAudienceResponse401
from ...models.update_audience_response_402 import UpdateAudienceResponse402
from ...models.update_audience_response_403 import UpdateAudienceResponse403
from ...models.update_audience_response_404 import UpdateAudienceResponse404
from ...models.update_audience_response_422 import UpdateAudienceResponse422
from ...models.update_audience_response_429 import UpdateAudienceResponse429
from ...models.update_audience_response_500 import UpdateAudienceResponse500
from ...models.update_audience_response_503 import UpdateAudienceResponse503
from ...types import Response


def _get_kwargs(
    audience_id: str,
    *,
    body: UpdateAudienceBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/audiences/{audience_id}".format(
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
    UpdateAudienceResponse200
    | UpdateAudienceResponse400
    | UpdateAudienceResponse401
    | UpdateAudienceResponse402
    | UpdateAudienceResponse403
    | UpdateAudienceResponse404
    | UpdateAudienceResponse422
    | UpdateAudienceResponse429
    | UpdateAudienceResponse500
    | UpdateAudienceResponse503
    | None
):
    if response.status_code == 200:
        response_200 = UpdateAudienceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateAudienceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateAudienceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = UpdateAudienceResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = UpdateAudienceResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateAudienceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = UpdateAudienceResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = UpdateAudienceResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UpdateAudienceResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = UpdateAudienceResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateAudienceResponse200
    | UpdateAudienceResponse400
    | UpdateAudienceResponse401
    | UpdateAudienceResponse402
    | UpdateAudienceResponse403
    | UpdateAudienceResponse404
    | UpdateAudienceResponse422
    | UpdateAudienceResponse429
    | UpdateAudienceResponse500
    | UpdateAudienceResponse503
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
    body: UpdateAudienceBody,
) -> Response[
    UpdateAudienceResponse200
    | UpdateAudienceResponse400
    | UpdateAudienceResponse401
    | UpdateAudienceResponse402
    | UpdateAudienceResponse403
    | UpdateAudienceResponse404
    | UpdateAudienceResponse422
    | UpdateAudienceResponse429
    | UpdateAudienceResponse500
    | UpdateAudienceResponse503
]:
    """Rename an audience

     Renames an audience. The audience can be renamed in any status, and renaming does not change its
    search parameters, companies, or prospects. Returns the audience ID, its new name, and when it was
    updated.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        audience_id (str):
        body (UpdateAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAudienceResponse200 | UpdateAudienceResponse400 | UpdateAudienceResponse401 | UpdateAudienceResponse402 | UpdateAudienceResponse403 | UpdateAudienceResponse404 | UpdateAudienceResponse422 | UpdateAudienceResponse429 | UpdateAudienceResponse500 | UpdateAudienceResponse503]
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
    body: UpdateAudienceBody,
) -> (
    UpdateAudienceResponse200
    | UpdateAudienceResponse400
    | UpdateAudienceResponse401
    | UpdateAudienceResponse402
    | UpdateAudienceResponse403
    | UpdateAudienceResponse404
    | UpdateAudienceResponse422
    | UpdateAudienceResponse429
    | UpdateAudienceResponse500
    | UpdateAudienceResponse503
    | None
):
    """Rename an audience

     Renames an audience. The audience can be renamed in any status, and renaming does not change its
    search parameters, companies, or prospects. Returns the audience ID, its new name, and when it was
    updated.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        audience_id (str):
        body (UpdateAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAudienceResponse200 | UpdateAudienceResponse400 | UpdateAudienceResponse401 | UpdateAudienceResponse402 | UpdateAudienceResponse403 | UpdateAudienceResponse404 | UpdateAudienceResponse422 | UpdateAudienceResponse429 | UpdateAudienceResponse500 | UpdateAudienceResponse503
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
    body: UpdateAudienceBody,
) -> Response[
    UpdateAudienceResponse200
    | UpdateAudienceResponse400
    | UpdateAudienceResponse401
    | UpdateAudienceResponse402
    | UpdateAudienceResponse403
    | UpdateAudienceResponse404
    | UpdateAudienceResponse422
    | UpdateAudienceResponse429
    | UpdateAudienceResponse500
    | UpdateAudienceResponse503
]:
    """Rename an audience

     Renames an audience. The audience can be renamed in any status, and renaming does not change its
    search parameters, companies, or prospects. Returns the audience ID, its new name, and when it was
    updated.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        audience_id (str):
        body (UpdateAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAudienceResponse200 | UpdateAudienceResponse400 | UpdateAudienceResponse401 | UpdateAudienceResponse402 | UpdateAudienceResponse403 | UpdateAudienceResponse404 | UpdateAudienceResponse422 | UpdateAudienceResponse429 | UpdateAudienceResponse500 | UpdateAudienceResponse503]
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
    body: UpdateAudienceBody,
) -> (
    UpdateAudienceResponse200
    | UpdateAudienceResponse400
    | UpdateAudienceResponse401
    | UpdateAudienceResponse402
    | UpdateAudienceResponse403
    | UpdateAudienceResponse404
    | UpdateAudienceResponse422
    | UpdateAudienceResponse429
    | UpdateAudienceResponse500
    | UpdateAudienceResponse503
    | None
):
    """Rename an audience

     Renames an audience. The audience can be renamed in any status, and renaming does not change its
    search parameters, companies, or prospects. Returns the audience ID, its new name, and when it was
    updated.

    <span>⚡ <strong>Rate limit:</strong> 120 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        audience_id (str):
        body (UpdateAudienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAudienceResponse200 | UpdateAudienceResponse400 | UpdateAudienceResponse401 | UpdateAudienceResponse402 | UpdateAudienceResponse403 | UpdateAudienceResponse404 | UpdateAudienceResponse422 | UpdateAudienceResponse429 | UpdateAudienceResponse500 | UpdateAudienceResponse503
    """

    return (
        await asyncio_detailed(
            audience_id=audience_id,
            client=client,
            body=body,
        )
    ).parsed
