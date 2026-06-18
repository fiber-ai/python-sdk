from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_batch_contact_details_body import CancelBatchContactDetailsBody
from ...models.cancel_batch_contact_details_response_200 import CancelBatchContactDetailsResponse200
from ...models.cancel_batch_contact_details_response_400 import CancelBatchContactDetailsResponse400
from ...models.cancel_batch_contact_details_response_401 import CancelBatchContactDetailsResponse401
from ...models.cancel_batch_contact_details_response_402 import CancelBatchContactDetailsResponse402
from ...models.cancel_batch_contact_details_response_403 import CancelBatchContactDetailsResponse403
from ...models.cancel_batch_contact_details_response_404 import CancelBatchContactDetailsResponse404
from ...models.cancel_batch_contact_details_response_422 import CancelBatchContactDetailsResponse422
from ...models.cancel_batch_contact_details_response_429 import CancelBatchContactDetailsResponse429
from ...models.cancel_batch_contact_details_response_500 import CancelBatchContactDetailsResponse500
from ...models.cancel_batch_contact_details_response_503 import CancelBatchContactDetailsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CancelBatchContactDetailsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/contact-details/batch/cancel",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CancelBatchContactDetailsResponse200
    | CancelBatchContactDetailsResponse400
    | CancelBatchContactDetailsResponse401
    | CancelBatchContactDetailsResponse402
    | CancelBatchContactDetailsResponse403
    | CancelBatchContactDetailsResponse404
    | CancelBatchContactDetailsResponse422
    | CancelBatchContactDetailsResponse429
    | CancelBatchContactDetailsResponse500
    | CancelBatchContactDetailsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CancelBatchContactDetailsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CancelBatchContactDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CancelBatchContactDetailsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CancelBatchContactDetailsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CancelBatchContactDetailsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CancelBatchContactDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = CancelBatchContactDetailsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = CancelBatchContactDetailsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CancelBatchContactDetailsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CancelBatchContactDetailsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CancelBatchContactDetailsResponse200
    | CancelBatchContactDetailsResponse400
    | CancelBatchContactDetailsResponse401
    | CancelBatchContactDetailsResponse402
    | CancelBatchContactDetailsResponse403
    | CancelBatchContactDetailsResponse404
    | CancelBatchContactDetailsResponse422
    | CancelBatchContactDetailsResponse429
    | CancelBatchContactDetailsResponse500
    | CancelBatchContactDetailsResponse503
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
    body: CancelBatchContactDetailsBody,
) -> Response[
    CancelBatchContactDetailsResponse200
    | CancelBatchContactDetailsResponse400
    | CancelBatchContactDetailsResponse401
    | CancelBatchContactDetailsResponse402
    | CancelBatchContactDetailsResponse403
    | CancelBatchContactDetailsResponse404
    | CancelBatchContactDetailsResponse422
    | CancelBatchContactDetailsResponse429
    | CancelBatchContactDetailsResponse500
    | CancelBatchContactDetailsResponse503
]:
    """Cancel batch contact details

     Cancels a batch contact details job that is in progress. Only unclaimed profiles will be cancelled.
    Profiles already processed will be charged for. Credits are refunded for cancelled profiles.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (CancelBatchContactDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelBatchContactDetailsResponse200 | CancelBatchContactDetailsResponse400 | CancelBatchContactDetailsResponse401 | CancelBatchContactDetailsResponse402 | CancelBatchContactDetailsResponse403 | CancelBatchContactDetailsResponse404 | CancelBatchContactDetailsResponse422 | CancelBatchContactDetailsResponse429 | CancelBatchContactDetailsResponse500 | CancelBatchContactDetailsResponse503]
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
    body: CancelBatchContactDetailsBody,
) -> (
    CancelBatchContactDetailsResponse200
    | CancelBatchContactDetailsResponse400
    | CancelBatchContactDetailsResponse401
    | CancelBatchContactDetailsResponse402
    | CancelBatchContactDetailsResponse403
    | CancelBatchContactDetailsResponse404
    | CancelBatchContactDetailsResponse422
    | CancelBatchContactDetailsResponse429
    | CancelBatchContactDetailsResponse500
    | CancelBatchContactDetailsResponse503
    | None
):
    """Cancel batch contact details

     Cancels a batch contact details job that is in progress. Only unclaimed profiles will be cancelled.
    Profiles already processed will be charged for. Credits are refunded for cancelled profiles.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (CancelBatchContactDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelBatchContactDetailsResponse200 | CancelBatchContactDetailsResponse400 | CancelBatchContactDetailsResponse401 | CancelBatchContactDetailsResponse402 | CancelBatchContactDetailsResponse403 | CancelBatchContactDetailsResponse404 | CancelBatchContactDetailsResponse422 | CancelBatchContactDetailsResponse429 | CancelBatchContactDetailsResponse500 | CancelBatchContactDetailsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CancelBatchContactDetailsBody,
) -> Response[
    CancelBatchContactDetailsResponse200
    | CancelBatchContactDetailsResponse400
    | CancelBatchContactDetailsResponse401
    | CancelBatchContactDetailsResponse402
    | CancelBatchContactDetailsResponse403
    | CancelBatchContactDetailsResponse404
    | CancelBatchContactDetailsResponse422
    | CancelBatchContactDetailsResponse429
    | CancelBatchContactDetailsResponse500
    | CancelBatchContactDetailsResponse503
]:
    """Cancel batch contact details

     Cancels a batch contact details job that is in progress. Only unclaimed profiles will be cancelled.
    Profiles already processed will be charged for. Credits are refunded for cancelled profiles.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (CancelBatchContactDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelBatchContactDetailsResponse200 | CancelBatchContactDetailsResponse400 | CancelBatchContactDetailsResponse401 | CancelBatchContactDetailsResponse402 | CancelBatchContactDetailsResponse403 | CancelBatchContactDetailsResponse404 | CancelBatchContactDetailsResponse422 | CancelBatchContactDetailsResponse429 | CancelBatchContactDetailsResponse500 | CancelBatchContactDetailsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CancelBatchContactDetailsBody,
) -> (
    CancelBatchContactDetailsResponse200
    | CancelBatchContactDetailsResponse400
    | CancelBatchContactDetailsResponse401
    | CancelBatchContactDetailsResponse402
    | CancelBatchContactDetailsResponse403
    | CancelBatchContactDetailsResponse404
    | CancelBatchContactDetailsResponse422
    | CancelBatchContactDetailsResponse429
    | CancelBatchContactDetailsResponse500
    | CancelBatchContactDetailsResponse503
    | None
):
    """Cancel batch contact details

     Cancels a batch contact details job that is in progress. Only unclaimed profiles will be cancelled.
    Profiles already processed will be charged for. Credits are refunded for cancelled profiles.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    Args:
        body (CancelBatchContactDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelBatchContactDetailsResponse200 | CancelBatchContactDetailsResponse400 | CancelBatchContactDetailsResponse401 | CancelBatchContactDetailsResponse402 | CancelBatchContactDetailsResponse403 | CancelBatchContactDetailsResponse404 | CancelBatchContactDetailsResponse422 | CancelBatchContactDetailsResponse429 | CancelBatchContactDetailsResponse500 | CancelBatchContactDetailsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
