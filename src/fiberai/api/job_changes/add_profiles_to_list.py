from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_profiles_to_list_body import AddProfilesToListBody
from ...models.add_profiles_to_list_response_200 import AddProfilesToListResponse200
from ...models.add_profiles_to_list_response_400 import AddProfilesToListResponse400
from ...models.add_profiles_to_list_response_401 import AddProfilesToListResponse401
from ...models.add_profiles_to_list_response_402 import AddProfilesToListResponse402
from ...models.add_profiles_to_list_response_403 import AddProfilesToListResponse403
from ...models.add_profiles_to_list_response_404 import AddProfilesToListResponse404
from ...models.add_profiles_to_list_response_422 import AddProfilesToListResponse422
from ...models.add_profiles_to_list_response_429 import AddProfilesToListResponse429
from ...models.add_profiles_to_list_response_500 import AddProfilesToListResponse500
from ...models.add_profiles_to_list_response_503 import AddProfilesToListResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: AddProfilesToListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job-changes/add-profiles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddProfilesToListResponse200
    | AddProfilesToListResponse400
    | AddProfilesToListResponse401
    | AddProfilesToListResponse402
    | AddProfilesToListResponse403
    | AddProfilesToListResponse404
    | AddProfilesToListResponse422
    | AddProfilesToListResponse429
    | AddProfilesToListResponse500
    | AddProfilesToListResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AddProfilesToListResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddProfilesToListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddProfilesToListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = AddProfilesToListResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = AddProfilesToListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddProfilesToListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = AddProfilesToListResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = AddProfilesToListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AddProfilesToListResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AddProfilesToListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddProfilesToListResponse200
    | AddProfilesToListResponse400
    | AddProfilesToListResponse401
    | AddProfilesToListResponse402
    | AddProfilesToListResponse403
    | AddProfilesToListResponse404
    | AddProfilesToListResponse422
    | AddProfilesToListResponse429
    | AddProfilesToListResponse500
    | AddProfilesToListResponse503
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
    body: AddProfilesToListBody,
) -> Response[
    AddProfilesToListResponse200
    | AddProfilesToListResponse400
    | AddProfilesToListResponse401
    | AddProfilesToListResponse402
    | AddProfilesToListResponse403
    | AddProfilesToListResponse404
    | AddProfilesToListResponse422
    | AddProfilesToListResponse429
    | AddProfilesToListResponse500
    | AddProfilesToListResponse503
]:
    r"""Add profiles to the job change list

     Add profiles to the job change list whose job changes you want to track. Note: we automatically
    remove 404 profiles from the list. Once the upload starts, you can use /job-changes/get-list to
    track the upload progress.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per per profile tracked&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddProfilesToListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddProfilesToListResponse200 | AddProfilesToListResponse400 | AddProfilesToListResponse401 | AddProfilesToListResponse402 | AddProfilesToListResponse403 | AddProfilesToListResponse404 | AddProfilesToListResponse422 | AddProfilesToListResponse429 | AddProfilesToListResponse500 | AddProfilesToListResponse503]
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
    body: AddProfilesToListBody,
) -> (
    AddProfilesToListResponse200
    | AddProfilesToListResponse400
    | AddProfilesToListResponse401
    | AddProfilesToListResponse402
    | AddProfilesToListResponse403
    | AddProfilesToListResponse404
    | AddProfilesToListResponse422
    | AddProfilesToListResponse429
    | AddProfilesToListResponse500
    | AddProfilesToListResponse503
    | None
):
    r"""Add profiles to the job change list

     Add profiles to the job change list whose job changes you want to track. Note: we automatically
    remove 404 profiles from the list. Once the upload starts, you can use /job-changes/get-list to
    track the upload progress.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per per profile tracked&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddProfilesToListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddProfilesToListResponse200 | AddProfilesToListResponse400 | AddProfilesToListResponse401 | AddProfilesToListResponse402 | AddProfilesToListResponse403 | AddProfilesToListResponse404 | AddProfilesToListResponse422 | AddProfilesToListResponse429 | AddProfilesToListResponse500 | AddProfilesToListResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddProfilesToListBody,
) -> Response[
    AddProfilesToListResponse200
    | AddProfilesToListResponse400
    | AddProfilesToListResponse401
    | AddProfilesToListResponse402
    | AddProfilesToListResponse403
    | AddProfilesToListResponse404
    | AddProfilesToListResponse422
    | AddProfilesToListResponse429
    | AddProfilesToListResponse500
    | AddProfilesToListResponse503
]:
    r"""Add profiles to the job change list

     Add profiles to the job change list whose job changes you want to track. Note: we automatically
    remove 404 profiles from the list. Once the upload starts, you can use /job-changes/get-list to
    track the upload progress.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per per profile tracked&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddProfilesToListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddProfilesToListResponse200 | AddProfilesToListResponse400 | AddProfilesToListResponse401 | AddProfilesToListResponse402 | AddProfilesToListResponse403 | AddProfilesToListResponse404 | AddProfilesToListResponse422 | AddProfilesToListResponse429 | AddProfilesToListResponse500 | AddProfilesToListResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AddProfilesToListBody,
) -> (
    AddProfilesToListResponse200
    | AddProfilesToListResponse400
    | AddProfilesToListResponse401
    | AddProfilesToListResponse402
    | AddProfilesToListResponse403
    | AddProfilesToListResponse404
    | AddProfilesToListResponse422
    | AddProfilesToListResponse429
    | AddProfilesToListResponse500
    | AddProfilesToListResponse503
    | None
):
    r"""Add profiles to the job change list

     Add profiles to the job change list whose job changes you want to track. Note: we automatically
    remove 404 profiles from the list. Once the upload starts, you can use /job-changes/get-list to
    track the upload progress.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per per profile tracked&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (AddProfilesToListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddProfilesToListResponse200 | AddProfilesToListResponse400 | AddProfilesToListResponse401 | AddProfilesToListResponse402 | AddProfilesToListResponse403 | AddProfilesToListResponse404 | AddProfilesToListResponse422 | AddProfilesToListResponse429 | AddProfilesToListResponse500 | AddProfilesToListResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
