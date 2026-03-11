from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validate_phone_number_body import ValidatePhoneNumberBody
from ...models.validate_phone_number_response_200 import ValidatePhoneNumberResponse200
from ...models.validate_phone_number_response_400 import ValidatePhoneNumberResponse400
from ...models.validate_phone_number_response_401 import ValidatePhoneNumberResponse401
from ...models.validate_phone_number_response_402 import ValidatePhoneNumberResponse402
from ...models.validate_phone_number_response_403 import ValidatePhoneNumberResponse403
from ...models.validate_phone_number_response_404 import ValidatePhoneNumberResponse404
from ...models.validate_phone_number_response_429 import ValidatePhoneNumberResponse429
from ...models.validate_phone_number_response_500 import ValidatePhoneNumberResponse500
from ...models.validate_phone_number_response_503 import ValidatePhoneNumberResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ValidatePhoneNumberBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/validate-phone/single",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ValidatePhoneNumberResponse200
    | ValidatePhoneNumberResponse400
    | ValidatePhoneNumberResponse401
    | ValidatePhoneNumberResponse402
    | ValidatePhoneNumberResponse403
    | ValidatePhoneNumberResponse404
    | ValidatePhoneNumberResponse429
    | ValidatePhoneNumberResponse500
    | ValidatePhoneNumberResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ValidatePhoneNumberResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ValidatePhoneNumberResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ValidatePhoneNumberResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ValidatePhoneNumberResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ValidatePhoneNumberResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ValidatePhoneNumberResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ValidatePhoneNumberResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ValidatePhoneNumberResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ValidatePhoneNumberResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ValidatePhoneNumberResponse200
    | ValidatePhoneNumberResponse400
    | ValidatePhoneNumberResponse401
    | ValidatePhoneNumberResponse402
    | ValidatePhoneNumberResponse403
    | ValidatePhoneNumberResponse404
    | ValidatePhoneNumberResponse429
    | ValidatePhoneNumberResponse500
    | ValidatePhoneNumberResponse503
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
    body: ValidatePhoneNumberBody,
) -> Response[
    ValidatePhoneNumberResponse200
    | ValidatePhoneNumberResponse400
    | ValidatePhoneNumberResponse401
    | ValidatePhoneNumberResponse402
    | ValidatePhoneNumberResponse403
    | ValidatePhoneNumberResponse404
    | ValidatePhoneNumberResponse429
    | ValidatePhoneNumberResponse500
    | ValidatePhoneNumberResponse503
]:
    r"""Validate a single phone number

     Validates a phone number and returns detailed information including whether it's valid, reachable
    (active/alive), carrier information, and the caller ID name associated with the number.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per phone validation&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ValidatePhoneNumberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidatePhoneNumberResponse200 | ValidatePhoneNumberResponse400 | ValidatePhoneNumberResponse401 | ValidatePhoneNumberResponse402 | ValidatePhoneNumberResponse403 | ValidatePhoneNumberResponse404 | ValidatePhoneNumberResponse429 | ValidatePhoneNumberResponse500 | ValidatePhoneNumberResponse503]
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
    body: ValidatePhoneNumberBody,
) -> (
    ValidatePhoneNumberResponse200
    | ValidatePhoneNumberResponse400
    | ValidatePhoneNumberResponse401
    | ValidatePhoneNumberResponse402
    | ValidatePhoneNumberResponse403
    | ValidatePhoneNumberResponse404
    | ValidatePhoneNumberResponse429
    | ValidatePhoneNumberResponse500
    | ValidatePhoneNumberResponse503
    | None
):
    r"""Validate a single phone number

     Validates a phone number and returns detailed information including whether it's valid, reachable
    (active/alive), carrier information, and the caller ID name associated with the number.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per phone validation&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ValidatePhoneNumberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidatePhoneNumberResponse200 | ValidatePhoneNumberResponse400 | ValidatePhoneNumberResponse401 | ValidatePhoneNumberResponse402 | ValidatePhoneNumberResponse403 | ValidatePhoneNumberResponse404 | ValidatePhoneNumberResponse429 | ValidatePhoneNumberResponse500 | ValidatePhoneNumberResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ValidatePhoneNumberBody,
) -> Response[
    ValidatePhoneNumberResponse200
    | ValidatePhoneNumberResponse400
    | ValidatePhoneNumberResponse401
    | ValidatePhoneNumberResponse402
    | ValidatePhoneNumberResponse403
    | ValidatePhoneNumberResponse404
    | ValidatePhoneNumberResponse429
    | ValidatePhoneNumberResponse500
    | ValidatePhoneNumberResponse503
]:
    r"""Validate a single phone number

     Validates a phone number and returns detailed information including whether it's valid, reachable
    (active/alive), carrier information, and the caller ID name associated with the number.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per phone validation&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ValidatePhoneNumberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidatePhoneNumberResponse200 | ValidatePhoneNumberResponse400 | ValidatePhoneNumberResponse401 | ValidatePhoneNumberResponse402 | ValidatePhoneNumberResponse403 | ValidatePhoneNumberResponse404 | ValidatePhoneNumberResponse429 | ValidatePhoneNumberResponse500 | ValidatePhoneNumberResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ValidatePhoneNumberBody,
) -> (
    ValidatePhoneNumberResponse200
    | ValidatePhoneNumberResponse400
    | ValidatePhoneNumberResponse401
    | ValidatePhoneNumberResponse402
    | ValidatePhoneNumberResponse403
    | ValidatePhoneNumberResponse404
    | ValidatePhoneNumberResponse429
    | ValidatePhoneNumberResponse500
    | ValidatePhoneNumberResponse503
    | None
):
    r"""Validate a single phone number

     Validates a phone number and returns detailed information including whether it's valid, reachable
    (active/alive), carrier information, and the caller ID name associated with the number.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 3 credits per phone validation&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (ValidatePhoneNumberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidatePhoneNumberResponse200 | ValidatePhoneNumberResponse400 | ValidatePhoneNumberResponse401 | ValidatePhoneNumberResponse402 | ValidatePhoneNumberResponse403 | ValidatePhoneNumberResponse404 | ValidatePhoneNumberResponse429 | ValidatePhoneNumberResponse500 | ValidatePhoneNumberResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
