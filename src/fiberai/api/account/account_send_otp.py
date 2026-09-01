from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_send_otp_body import AccountSendOtpBody
from ...models.account_send_otp_response_200 import AccountSendOtpResponse200
from ...models.account_send_otp_response_400 import AccountSendOtpResponse400
from ...models.account_send_otp_response_401 import AccountSendOtpResponse401
from ...models.account_send_otp_response_402 import AccountSendOtpResponse402
from ...models.account_send_otp_response_403 import AccountSendOtpResponse403
from ...models.account_send_otp_response_404 import AccountSendOtpResponse404
from ...models.account_send_otp_response_409 import AccountSendOtpResponse409
from ...models.account_send_otp_response_410 import AccountSendOtpResponse410
from ...models.account_send_otp_response_422 import AccountSendOtpResponse422
from ...models.account_send_otp_response_429 import AccountSendOtpResponse429
from ...models.account_send_otp_response_500 import AccountSendOtpResponse500
from ...models.account_send_otp_response_503 import AccountSendOtpResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: AccountSendOtpBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/account/send-otp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AccountSendOtpResponse200
    | AccountSendOtpResponse400
    | AccountSendOtpResponse401
    | AccountSendOtpResponse402
    | AccountSendOtpResponse403
    | AccountSendOtpResponse404
    | AccountSendOtpResponse409
    | AccountSendOtpResponse410
    | AccountSendOtpResponse422
    | AccountSendOtpResponse429
    | AccountSendOtpResponse500
    | AccountSendOtpResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AccountSendOtpResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AccountSendOtpResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AccountSendOtpResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = AccountSendOtpResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = AccountSendOtpResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AccountSendOtpResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = AccountSendOtpResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = AccountSendOtpResponse410.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = AccountSendOtpResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = AccountSendOtpResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AccountSendOtpResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AccountSendOtpResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AccountSendOtpResponse200
    | AccountSendOtpResponse400
    | AccountSendOtpResponse401
    | AccountSendOtpResponse402
    | AccountSendOtpResponse403
    | AccountSendOtpResponse404
    | AccountSendOtpResponse409
    | AccountSendOtpResponse410
    | AccountSendOtpResponse422
    | AccountSendOtpResponse429
    | AccountSendOtpResponse500
    | AccountSendOtpResponse503
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
    body: AccountSendOtpBody,
) -> Response[
    AccountSendOtpResponse200
    | AccountSendOtpResponse400
    | AccountSendOtpResponse401
    | AccountSendOtpResponse402
    | AccountSendOtpResponse403
    | AccountSendOtpResponse404
    | AccountSendOtpResponse409
    | AccountSendOtpResponse410
    | AccountSendOtpResponse422
    | AccountSendOtpResponse429
    | AccountSendOtpResponse500
    | AccountSendOtpResponse503
]:
    """Start signup (send OTP)

     Step 1 of signup. No API key is required. Send a one-time verification code to a work email to start
    a Fiber API trial. Optional firstName, lastName, and companyName are stored and used when the
    account is created. After the code arrives, call POST /v1/account/verify-otp with the returned
    verificationId and the code from email. That completes signup and returns your live API key (and a
    sandbox key when minted).

    <span>⚡ <strong>Rate limit:</strong> 6 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (AccountSendOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountSendOtpResponse200 | AccountSendOtpResponse400 | AccountSendOtpResponse401 | AccountSendOtpResponse402 | AccountSendOtpResponse403 | AccountSendOtpResponse404 | AccountSendOtpResponse409 | AccountSendOtpResponse410 | AccountSendOtpResponse422 | AccountSendOtpResponse429 | AccountSendOtpResponse500 | AccountSendOtpResponse503]
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
    body: AccountSendOtpBody,
) -> (
    AccountSendOtpResponse200
    | AccountSendOtpResponse400
    | AccountSendOtpResponse401
    | AccountSendOtpResponse402
    | AccountSendOtpResponse403
    | AccountSendOtpResponse404
    | AccountSendOtpResponse409
    | AccountSendOtpResponse410
    | AccountSendOtpResponse422
    | AccountSendOtpResponse429
    | AccountSendOtpResponse500
    | AccountSendOtpResponse503
    | None
):
    """Start signup (send OTP)

     Step 1 of signup. No API key is required. Send a one-time verification code to a work email to start
    a Fiber API trial. Optional firstName, lastName, and companyName are stored and used when the
    account is created. After the code arrives, call POST /v1/account/verify-otp with the returned
    verificationId and the code from email. That completes signup and returns your live API key (and a
    sandbox key when minted).

    <span>⚡ <strong>Rate limit:</strong> 6 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (AccountSendOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountSendOtpResponse200 | AccountSendOtpResponse400 | AccountSendOtpResponse401 | AccountSendOtpResponse402 | AccountSendOtpResponse403 | AccountSendOtpResponse404 | AccountSendOtpResponse409 | AccountSendOtpResponse410 | AccountSendOtpResponse422 | AccountSendOtpResponse429 | AccountSendOtpResponse500 | AccountSendOtpResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AccountSendOtpBody,
) -> Response[
    AccountSendOtpResponse200
    | AccountSendOtpResponse400
    | AccountSendOtpResponse401
    | AccountSendOtpResponse402
    | AccountSendOtpResponse403
    | AccountSendOtpResponse404
    | AccountSendOtpResponse409
    | AccountSendOtpResponse410
    | AccountSendOtpResponse422
    | AccountSendOtpResponse429
    | AccountSendOtpResponse500
    | AccountSendOtpResponse503
]:
    """Start signup (send OTP)

     Step 1 of signup. No API key is required. Send a one-time verification code to a work email to start
    a Fiber API trial. Optional firstName, lastName, and companyName are stored and used when the
    account is created. After the code arrives, call POST /v1/account/verify-otp with the returned
    verificationId and the code from email. That completes signup and returns your live API key (and a
    sandbox key when minted).

    <span>⚡ <strong>Rate limit:</strong> 6 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (AccountSendOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountSendOtpResponse200 | AccountSendOtpResponse400 | AccountSendOtpResponse401 | AccountSendOtpResponse402 | AccountSendOtpResponse403 | AccountSendOtpResponse404 | AccountSendOtpResponse409 | AccountSendOtpResponse410 | AccountSendOtpResponse422 | AccountSendOtpResponse429 | AccountSendOtpResponse500 | AccountSendOtpResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AccountSendOtpBody,
) -> (
    AccountSendOtpResponse200
    | AccountSendOtpResponse400
    | AccountSendOtpResponse401
    | AccountSendOtpResponse402
    | AccountSendOtpResponse403
    | AccountSendOtpResponse404
    | AccountSendOtpResponse409
    | AccountSendOtpResponse410
    | AccountSendOtpResponse422
    | AccountSendOtpResponse429
    | AccountSendOtpResponse500
    | AccountSendOtpResponse503
    | None
):
    """Start signup (send OTP)

     Step 1 of signup. No API key is required. Send a one-time verification code to a work email to start
    a Fiber API trial. Optional firstName, lastName, and companyName are stored and used when the
    account is created. After the code arrives, call POST /v1/account/verify-otp with the returned
    verificationId and the code from email. That completes signup and returns your live API key (and a
    sandbox key when minted).

    <span>⚡ <strong>Rate limit:</strong> 6 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (AccountSendOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountSendOtpResponse200 | AccountSendOtpResponse400 | AccountSendOtpResponse401 | AccountSendOtpResponse402 | AccountSendOtpResponse403 | AccountSendOtpResponse404 | AccountSendOtpResponse409 | AccountSendOtpResponse410 | AccountSendOtpResponse422 | AccountSendOtpResponse429 | AccountSendOtpResponse500 | AccountSendOtpResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
