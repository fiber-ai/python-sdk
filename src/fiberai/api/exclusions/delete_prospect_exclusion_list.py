from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_prospect_exclusion_list_body import DeleteProspectExclusionListBody
from ...models.delete_prospect_exclusion_list_response_200 import DeleteProspectExclusionListResponse200
from ...models.delete_prospect_exclusion_list_response_400 import DeleteProspectExclusionListResponse400
from ...models.delete_prospect_exclusion_list_response_401 import DeleteProspectExclusionListResponse401
from ...models.delete_prospect_exclusion_list_response_402 import DeleteProspectExclusionListResponse402
from ...models.delete_prospect_exclusion_list_response_403 import DeleteProspectExclusionListResponse403
from ...models.delete_prospect_exclusion_list_response_404 import DeleteProspectExclusionListResponse404
from ...models.delete_prospect_exclusion_list_response_429 import DeleteProspectExclusionListResponse429
from ...models.delete_prospect_exclusion_list_response_500 import DeleteProspectExclusionListResponse500
from ...models.delete_prospect_exclusion_list_response_503 import DeleteProspectExclusionListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteProspectExclusionListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exclusions/prospects/delete-list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteProspectExclusionListResponse200
    | DeleteProspectExclusionListResponse400
    | DeleteProspectExclusionListResponse401
    | DeleteProspectExclusionListResponse402
    | DeleteProspectExclusionListResponse403
    | DeleteProspectExclusionListResponse404
    | DeleteProspectExclusionListResponse429
    | DeleteProspectExclusionListResponse500
    | DeleteProspectExclusionListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = DeleteProspectExclusionListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteProspectExclusionListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteProspectExclusionListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = DeleteProspectExclusionListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = DeleteProspectExclusionListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteProspectExclusionListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = DeleteProspectExclusionListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DeleteProspectExclusionListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteProspectExclusionListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteProspectExclusionListResponse200
    | DeleteProspectExclusionListResponse400
    | DeleteProspectExclusionListResponse401
    | DeleteProspectExclusionListResponse402
    | DeleteProspectExclusionListResponse403
    | DeleteProspectExclusionListResponse404
    | DeleteProspectExclusionListResponse429
    | DeleteProspectExclusionListResponse500
    | DeleteProspectExclusionListResponse503
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
    body: DeleteProspectExclusionListBody,
) -> Response[
    DeleteProspectExclusionListResponse200
    | DeleteProspectExclusionListResponse400
    | DeleteProspectExclusionListResponse401
    | DeleteProspectExclusionListResponse402
    | DeleteProspectExclusionListResponse403
    | DeleteProspectExclusionListResponse404
    | DeleteProspectExclusionListResponse429
    | DeleteProspectExclusionListResponse500
    | DeleteProspectExclusionListResponse503
]:
    r"""Delete prospect exclusion list

     Delete a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DeleteProspectExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProspectExclusionListResponse200 | DeleteProspectExclusionListResponse400 | DeleteProspectExclusionListResponse401 | DeleteProspectExclusionListResponse402 | DeleteProspectExclusionListResponse403 | DeleteProspectExclusionListResponse404 | DeleteProspectExclusionListResponse429 | DeleteProspectExclusionListResponse500 | DeleteProspectExclusionListResponse503]
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
    body: DeleteProspectExclusionListBody,
) -> (
    DeleteProspectExclusionListResponse200
    | DeleteProspectExclusionListResponse400
    | DeleteProspectExclusionListResponse401
    | DeleteProspectExclusionListResponse402
    | DeleteProspectExclusionListResponse403
    | DeleteProspectExclusionListResponse404
    | DeleteProspectExclusionListResponse429
    | DeleteProspectExclusionListResponse500
    | DeleteProspectExclusionListResponse503
    | None
):
    r"""Delete prospect exclusion list

     Delete a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DeleteProspectExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProspectExclusionListResponse200 | DeleteProspectExclusionListResponse400 | DeleteProspectExclusionListResponse401 | DeleteProspectExclusionListResponse402 | DeleteProspectExclusionListResponse403 | DeleteProspectExclusionListResponse404 | DeleteProspectExclusionListResponse429 | DeleteProspectExclusionListResponse500 | DeleteProspectExclusionListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteProspectExclusionListBody,
) -> Response[
    DeleteProspectExclusionListResponse200
    | DeleteProspectExclusionListResponse400
    | DeleteProspectExclusionListResponse401
    | DeleteProspectExclusionListResponse402
    | DeleteProspectExclusionListResponse403
    | DeleteProspectExclusionListResponse404
    | DeleteProspectExclusionListResponse429
    | DeleteProspectExclusionListResponse500
    | DeleteProspectExclusionListResponse503
]:
    r"""Delete prospect exclusion list

     Delete a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DeleteProspectExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProspectExclusionListResponse200 | DeleteProspectExclusionListResponse400 | DeleteProspectExclusionListResponse401 | DeleteProspectExclusionListResponse402 | DeleteProspectExclusionListResponse403 | DeleteProspectExclusionListResponse404 | DeleteProspectExclusionListResponse429 | DeleteProspectExclusionListResponse500 | DeleteProspectExclusionListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteProspectExclusionListBody,
) -> (
    DeleteProspectExclusionListResponse200
    | DeleteProspectExclusionListResponse400
    | DeleteProspectExclusionListResponse401
    | DeleteProspectExclusionListResponse402
    | DeleteProspectExclusionListResponse403
    | DeleteProspectExclusionListResponse404
    | DeleteProspectExclusionListResponse429
    | DeleteProspectExclusionListResponse500
    | DeleteProspectExclusionListResponse503
    | None
):
    r"""Delete prospect exclusion list

     Delete a prospect exclusion list

    <span>⚡ <strong>Rate limit:</strong> 50 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (DeleteProspectExclusionListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProspectExclusionListResponse200 | DeleteProspectExclusionListResponse400 | DeleteProspectExclusionListResponse401 | DeleteProspectExclusionListResponse402 | DeleteProspectExclusionListResponse403 | DeleteProspectExclusionListResponse404 | DeleteProspectExclusionListResponse429 | DeleteProspectExclusionListResponse500 | DeleteProspectExclusionListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
