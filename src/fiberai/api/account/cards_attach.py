from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cards_attach_body import CardsAttachBody
from ...models.cards_attach_response_200 import CardsAttachResponse200
from ...models.cards_attach_response_400_type_0 import CardsAttachResponse400Type0
from ...models.cards_attach_response_400_type_1 import CardsAttachResponse400Type1
from ...models.cards_attach_response_401 import CardsAttachResponse401
from ...models.cards_attach_response_402 import CardsAttachResponse402
from ...models.cards_attach_response_403 import CardsAttachResponse403
from ...models.cards_attach_response_404 import CardsAttachResponse404
from ...models.cards_attach_response_409 import CardsAttachResponse409
from ...models.cards_attach_response_422 import CardsAttachResponse422
from ...models.cards_attach_response_429_type_0 import CardsAttachResponse429Type0
from ...models.cards_attach_response_429_type_1 import CardsAttachResponse429Type1
from ...models.cards_attach_response_500_type_0 import CardsAttachResponse500Type0
from ...models.cards_attach_response_500_type_1 import CardsAttachResponse500Type1
from ...models.cards_attach_response_503 import CardsAttachResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: CardsAttachBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/cards/attach",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CardsAttachResponse200
    | CardsAttachResponse400Type0
    | CardsAttachResponse400Type1
    | CardsAttachResponse401
    | CardsAttachResponse402
    | CardsAttachResponse403
    | CardsAttachResponse404
    | CardsAttachResponse409
    | CardsAttachResponse422
    | CardsAttachResponse429Type0
    | CardsAttachResponse429Type1
    | CardsAttachResponse500Type0
    | CardsAttachResponse500Type1
    | CardsAttachResponse503
    | None
):
    if response.status_code == 200:
        response_200 = CardsAttachResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> CardsAttachResponse400Type0 | CardsAttachResponse400Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = CardsAttachResponse400Type0.from_dict(data)

                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_1 = CardsAttachResponse400Type1.from_dict(data)

            return response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CardsAttachResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CardsAttachResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CardsAttachResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CardsAttachResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CardsAttachResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CardsAttachResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:

        def _parse_response_429(data: object) -> CardsAttachResponse429Type0 | CardsAttachResponse429Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_429_type_0 = CardsAttachResponse429Type0.from_dict(data)

                return response_429_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_429_type_1 = CardsAttachResponse429Type1.from_dict(data)

            return response_429_type_1

        response_429 = _parse_response_429(response.json())

        return response_429

    if response.status_code == 500:

        def _parse_response_500(data: object) -> CardsAttachResponse500Type0 | CardsAttachResponse500Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_0 = CardsAttachResponse500Type0.from_dict(data)

                return response_500_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_500_type_1 = CardsAttachResponse500Type1.from_dict(data)

            return response_500_type_1

        response_500 = _parse_response_500(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CardsAttachResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CardsAttachResponse200
    | CardsAttachResponse400Type0
    | CardsAttachResponse400Type1
    | CardsAttachResponse401
    | CardsAttachResponse402
    | CardsAttachResponse403
    | CardsAttachResponse404
    | CardsAttachResponse409
    | CardsAttachResponse422
    | CardsAttachResponse429Type0
    | CardsAttachResponse429Type1
    | CardsAttachResponse500Type0
    | CardsAttachResponse500Type1
    | CardsAttachResponse503
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
    body: CardsAttachBody,
) -> Response[
    CardsAttachResponse200
    | CardsAttachResponse400Type0
    | CardsAttachResponse400Type1
    | CardsAttachResponse401
    | CardsAttachResponse402
    | CardsAttachResponse403
    | CardsAttachResponse404
    | CardsAttachResponse409
    | CardsAttachResponse422
    | CardsAttachResponse429Type0
    | CardsAttachResponse429Type1
    | CardsAttachResponse500Type0
    | CardsAttachResponse500Type1
    | CardsAttachResponse503
]:
    r"""Attach card to trial account

     Attach a payment card to a cardless trial organization using a single-use Stripe shared payment
    token. The card is verified with a temporary $1 authorization that is refunded immediately (net cost
    $0), and the organization's free-credit ceiling is raised. The verified card is not saved for future
    charges — every future paid top-up requires a freshly-minted shared payment token.

    <span>⚡ <strong>Rate limit:</strong> 3 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CardsAttachBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CardsAttachResponse200 | CardsAttachResponse400Type0 | CardsAttachResponse400Type1 | CardsAttachResponse401 | CardsAttachResponse402 | CardsAttachResponse403 | CardsAttachResponse404 | CardsAttachResponse409 | CardsAttachResponse422 | CardsAttachResponse429Type0 | CardsAttachResponse429Type1 | CardsAttachResponse500Type0 | CardsAttachResponse500Type1 | CardsAttachResponse503]
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
    body: CardsAttachBody,
) -> (
    CardsAttachResponse200
    | CardsAttachResponse400Type0
    | CardsAttachResponse400Type1
    | CardsAttachResponse401
    | CardsAttachResponse402
    | CardsAttachResponse403
    | CardsAttachResponse404
    | CardsAttachResponse409
    | CardsAttachResponse422
    | CardsAttachResponse429Type0
    | CardsAttachResponse429Type1
    | CardsAttachResponse500Type0
    | CardsAttachResponse500Type1
    | CardsAttachResponse503
    | None
):
    r"""Attach card to trial account

     Attach a payment card to a cardless trial organization using a single-use Stripe shared payment
    token. The card is verified with a temporary $1 authorization that is refunded immediately (net cost
    $0), and the organization's free-credit ceiling is raised. The verified card is not saved for future
    charges — every future paid top-up requires a freshly-minted shared payment token.

    <span>⚡ <strong>Rate limit:</strong> 3 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CardsAttachBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CardsAttachResponse200 | CardsAttachResponse400Type0 | CardsAttachResponse400Type1 | CardsAttachResponse401 | CardsAttachResponse402 | CardsAttachResponse403 | CardsAttachResponse404 | CardsAttachResponse409 | CardsAttachResponse422 | CardsAttachResponse429Type0 | CardsAttachResponse429Type1 | CardsAttachResponse500Type0 | CardsAttachResponse500Type1 | CardsAttachResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CardsAttachBody,
) -> Response[
    CardsAttachResponse200
    | CardsAttachResponse400Type0
    | CardsAttachResponse400Type1
    | CardsAttachResponse401
    | CardsAttachResponse402
    | CardsAttachResponse403
    | CardsAttachResponse404
    | CardsAttachResponse409
    | CardsAttachResponse422
    | CardsAttachResponse429Type0
    | CardsAttachResponse429Type1
    | CardsAttachResponse500Type0
    | CardsAttachResponse500Type1
    | CardsAttachResponse503
]:
    r"""Attach card to trial account

     Attach a payment card to a cardless trial organization using a single-use Stripe shared payment
    token. The card is verified with a temporary $1 authorization that is refunded immediately (net cost
    $0), and the organization's free-credit ceiling is raised. The verified card is not saved for future
    charges — every future paid top-up requires a freshly-minted shared payment token.

    <span>⚡ <strong>Rate limit:</strong> 3 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CardsAttachBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CardsAttachResponse200 | CardsAttachResponse400Type0 | CardsAttachResponse400Type1 | CardsAttachResponse401 | CardsAttachResponse402 | CardsAttachResponse403 | CardsAttachResponse404 | CardsAttachResponse409 | CardsAttachResponse422 | CardsAttachResponse429Type0 | CardsAttachResponse429Type1 | CardsAttachResponse500Type0 | CardsAttachResponse500Type1 | CardsAttachResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CardsAttachBody,
) -> (
    CardsAttachResponse200
    | CardsAttachResponse400Type0
    | CardsAttachResponse400Type1
    | CardsAttachResponse401
    | CardsAttachResponse402
    | CardsAttachResponse403
    | CardsAttachResponse404
    | CardsAttachResponse409
    | CardsAttachResponse422
    | CardsAttachResponse429Type0
    | CardsAttachResponse429Type1
    | CardsAttachResponse500Type0
    | CardsAttachResponse500Type1
    | CardsAttachResponse503
    | None
):
    r"""Attach card to trial account

     Attach a payment card to a cardless trial organization using a single-use Stripe shared payment
    token. The card is verified with a temporary $1 authorization that is refunded immediately (net cost
    $0), and the organization's free-credit ceiling is raised. The verified card is not saved for future
    charges — every future paid top-up requires a freshly-minted shared payment token.

    <span>⚡ <strong>Rate limit:</strong> 3 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (CardsAttachBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CardsAttachResponse200 | CardsAttachResponse400Type0 | CardsAttachResponse400Type1 | CardsAttachResponse401 | CardsAttachResponse402 | CardsAttachResponse403 | CardsAttachResponse404 | CardsAttachResponse409 | CardsAttachResponse422 | CardsAttachResponse429Type0 | CardsAttachResponse429Type1 | CardsAttachResponse500Type0 | CardsAttachResponse500Type1 | CardsAttachResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
