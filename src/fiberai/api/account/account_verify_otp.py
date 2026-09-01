from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_verify_otp_body import AccountVerifyOtpBody
from ...models.account_verify_otp_response_200 import AccountVerifyOtpResponse200
from ...models.account_verify_otp_response_400 import AccountVerifyOtpResponse400
from ...models.account_verify_otp_response_401 import AccountVerifyOtpResponse401
from ...models.account_verify_otp_response_402 import AccountVerifyOtpResponse402
from ...models.account_verify_otp_response_403 import AccountVerifyOtpResponse403
from ...models.account_verify_otp_response_404 import AccountVerifyOtpResponse404
from ...models.account_verify_otp_response_409 import AccountVerifyOtpResponse409
from ...models.account_verify_otp_response_410 import AccountVerifyOtpResponse410
from ...models.account_verify_otp_response_422 import AccountVerifyOtpResponse422
from ...models.account_verify_otp_response_429 import AccountVerifyOtpResponse429
from ...models.account_verify_otp_response_500 import AccountVerifyOtpResponse500
from ...models.account_verify_otp_response_503 import AccountVerifyOtpResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: AccountVerifyOtpBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/account/verify-otp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AccountVerifyOtpResponse200
    | AccountVerifyOtpResponse400
    | AccountVerifyOtpResponse401
    | AccountVerifyOtpResponse402
    | AccountVerifyOtpResponse403
    | AccountVerifyOtpResponse404
    | AccountVerifyOtpResponse409
    | AccountVerifyOtpResponse410
    | AccountVerifyOtpResponse422
    | AccountVerifyOtpResponse429
    | AccountVerifyOtpResponse500
    | AccountVerifyOtpResponse503
    | None
):
    if response.status_code == 200:
        response_200 = AccountVerifyOtpResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AccountVerifyOtpResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AccountVerifyOtpResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = AccountVerifyOtpResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = AccountVerifyOtpResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AccountVerifyOtpResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = AccountVerifyOtpResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = AccountVerifyOtpResponse410.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = AccountVerifyOtpResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = AccountVerifyOtpResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AccountVerifyOtpResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AccountVerifyOtpResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AccountVerifyOtpResponse200
    | AccountVerifyOtpResponse400
    | AccountVerifyOtpResponse401
    | AccountVerifyOtpResponse402
    | AccountVerifyOtpResponse403
    | AccountVerifyOtpResponse404
    | AccountVerifyOtpResponse409
    | AccountVerifyOtpResponse410
    | AccountVerifyOtpResponse422
    | AccountVerifyOtpResponse429
    | AccountVerifyOtpResponse500
    | AccountVerifyOtpResponse503
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
    body: AccountVerifyOtpBody,
) -> Response[
    AccountVerifyOtpResponse200
    | AccountVerifyOtpResponse400
    | AccountVerifyOtpResponse401
    | AccountVerifyOtpResponse402
    | AccountVerifyOtpResponse403
    | AccountVerifyOtpResponse404
    | AccountVerifyOtpResponse409
    | AccountVerifyOtpResponse410
    | AccountVerifyOtpResponse422
    | AccountVerifyOtpResponse429
    | AccountVerifyOtpResponse500
    | AccountVerifyOtpResponse503
]:
    """Complete signup (verify OTP)

     Step 2 of signup. Completes the flow started by POST /v1/account/send-otp. Pass the verificationId
    from that response and the one-time code from email. On success this creates the trial account and
    returns a live API key (sk_live_...) plus a companion sandbox API key (sk_test_...) when one was
    minted. Store both securely — they cannot be retrieved later. First-time users without a key yet
    must start at send-otp; existing users create extra sandbox keys via POST /v1/api-keys/create-
    sandbox.

    <span>⚡ <strong>Rate limit:</strong> 12 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (AccountVerifyOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountVerifyOtpResponse200 | AccountVerifyOtpResponse400 | AccountVerifyOtpResponse401 | AccountVerifyOtpResponse402 | AccountVerifyOtpResponse403 | AccountVerifyOtpResponse404 | AccountVerifyOtpResponse409 | AccountVerifyOtpResponse410 | AccountVerifyOtpResponse422 | AccountVerifyOtpResponse429 | AccountVerifyOtpResponse500 | AccountVerifyOtpResponse503]
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
    body: AccountVerifyOtpBody,
) -> (
    AccountVerifyOtpResponse200
    | AccountVerifyOtpResponse400
    | AccountVerifyOtpResponse401
    | AccountVerifyOtpResponse402
    | AccountVerifyOtpResponse403
    | AccountVerifyOtpResponse404
    | AccountVerifyOtpResponse409
    | AccountVerifyOtpResponse410
    | AccountVerifyOtpResponse422
    | AccountVerifyOtpResponse429
    | AccountVerifyOtpResponse500
    | AccountVerifyOtpResponse503
    | None
):
    """Complete signup (verify OTP)

     Step 2 of signup. Completes the flow started by POST /v1/account/send-otp. Pass the verificationId
    from that response and the one-time code from email. On success this creates the trial account and
    returns a live API key (sk_live_...) plus a companion sandbox API key (sk_test_...) when one was
    minted. Store both securely — they cannot be retrieved later. First-time users without a key yet
    must start at send-otp; existing users create extra sandbox keys via POST /v1/api-keys/create-
    sandbox.

    <span>⚡ <strong>Rate limit:</strong> 12 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (AccountVerifyOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountVerifyOtpResponse200 | AccountVerifyOtpResponse400 | AccountVerifyOtpResponse401 | AccountVerifyOtpResponse402 | AccountVerifyOtpResponse403 | AccountVerifyOtpResponse404 | AccountVerifyOtpResponse409 | AccountVerifyOtpResponse410 | AccountVerifyOtpResponse422 | AccountVerifyOtpResponse429 | AccountVerifyOtpResponse500 | AccountVerifyOtpResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AccountVerifyOtpBody,
) -> Response[
    AccountVerifyOtpResponse200
    | AccountVerifyOtpResponse400
    | AccountVerifyOtpResponse401
    | AccountVerifyOtpResponse402
    | AccountVerifyOtpResponse403
    | AccountVerifyOtpResponse404
    | AccountVerifyOtpResponse409
    | AccountVerifyOtpResponse410
    | AccountVerifyOtpResponse422
    | AccountVerifyOtpResponse429
    | AccountVerifyOtpResponse500
    | AccountVerifyOtpResponse503
]:
    """Complete signup (verify OTP)

     Step 2 of signup. Completes the flow started by POST /v1/account/send-otp. Pass the verificationId
    from that response and the one-time code from email. On success this creates the trial account and
    returns a live API key (sk_live_...) plus a companion sandbox API key (sk_test_...) when one was
    minted. Store both securely — they cannot be retrieved later. First-time users without a key yet
    must start at send-otp; existing users create extra sandbox keys via POST /v1/api-keys/create-
    sandbox.

    <span>⚡ <strong>Rate limit:</strong> 12 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (AccountVerifyOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountVerifyOtpResponse200 | AccountVerifyOtpResponse400 | AccountVerifyOtpResponse401 | AccountVerifyOtpResponse402 | AccountVerifyOtpResponse403 | AccountVerifyOtpResponse404 | AccountVerifyOtpResponse409 | AccountVerifyOtpResponse410 | AccountVerifyOtpResponse422 | AccountVerifyOtpResponse429 | AccountVerifyOtpResponse500 | AccountVerifyOtpResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AccountVerifyOtpBody,
) -> (
    AccountVerifyOtpResponse200
    | AccountVerifyOtpResponse400
    | AccountVerifyOtpResponse401
    | AccountVerifyOtpResponse402
    | AccountVerifyOtpResponse403
    | AccountVerifyOtpResponse404
    | AccountVerifyOtpResponse409
    | AccountVerifyOtpResponse410
    | AccountVerifyOtpResponse422
    | AccountVerifyOtpResponse429
    | AccountVerifyOtpResponse500
    | AccountVerifyOtpResponse503
    | None
):
    """Complete signup (verify OTP)

     Step 2 of signup. Completes the flow started by POST /v1/account/send-otp. Pass the verificationId
    from that response and the one-time code from email. On success this creates the trial account and
    returns a live API key (sk_live_...) plus a companion sandbox API key (sk_test_...) when one was
    minted. Store both securely — they cannot be retrieved later. First-time users without a key yet
    must start at send-otp; existing users create extra sandbox keys via POST /v1/api-keys/create-
    sandbox.

    <span>⚡ <strong>Rate limit:</strong> 12 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (AccountVerifyOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountVerifyOtpResponse200 | AccountVerifyOtpResponse400 | AccountVerifyOtpResponse401 | AccountVerifyOtpResponse402 | AccountVerifyOtpResponse403 | AccountVerifyOtpResponse404 | AccountVerifyOtpResponse409 | AccountVerifyOtpResponse410 | AccountVerifyOtpResponse422 | AccountVerifyOtpResponse429 | AccountVerifyOtpResponse500 | AccountVerifyOtpResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
