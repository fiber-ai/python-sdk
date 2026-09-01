from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_api_requests_body import ListApiRequestsBody
from ...models.list_api_requests_response_200 import ListApiRequestsResponse200
from ...models.list_api_requests_response_400 import ListApiRequestsResponse400
from ...models.list_api_requests_response_401 import ListApiRequestsResponse401
from ...models.list_api_requests_response_402 import ListApiRequestsResponse402
from ...models.list_api_requests_response_403 import ListApiRequestsResponse403
from ...models.list_api_requests_response_404 import ListApiRequestsResponse404
from ...models.list_api_requests_response_422 import ListApiRequestsResponse422
from ...models.list_api_requests_response_429 import ListApiRequestsResponse429
from ...models.list_api_requests_response_500 import ListApiRequestsResponse500
from ...models.list_api_requests_response_503 import ListApiRequestsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: ListApiRequestsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api-requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListApiRequestsResponse200
    | ListApiRequestsResponse400
    | ListApiRequestsResponse401
    | ListApiRequestsResponse402
    | ListApiRequestsResponse403
    | ListApiRequestsResponse404
    | ListApiRequestsResponse422
    | ListApiRequestsResponse429
    | ListApiRequestsResponse500
    | ListApiRequestsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = ListApiRequestsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListApiRequestsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListApiRequestsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ListApiRequestsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ListApiRequestsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListApiRequestsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ListApiRequestsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ListApiRequestsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListApiRequestsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ListApiRequestsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListApiRequestsResponse200
    | ListApiRequestsResponse400
    | ListApiRequestsResponse401
    | ListApiRequestsResponse402
    | ListApiRequestsResponse403
    | ListApiRequestsResponse404
    | ListApiRequestsResponse422
    | ListApiRequestsResponse429
    | ListApiRequestsResponse500
    | ListApiRequestsResponse503
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
    body: ListApiRequestsBody,
) -> Response[
    ListApiRequestsResponse200
    | ListApiRequestsResponse400
    | ListApiRequestsResponse401
    | ListApiRequestsResponse402
    | ListApiRequestsResponse403
    | ListApiRequestsResponse404
    | ListApiRequestsResponse422
    | ListApiRequestsResponse429
    | ListApiRequestsResponse500
    | ListApiRequestsResponse503
]:
    """List your past API requests

     List the API requests your organization has made, newest first, with the parameters you sent and how
    each call turned out. Use it to answer 'what did my agent actually run?' — debugging a failed run,
    auditing usage, or quoting an `errorCode` in a support request. Filter by time range, route, method,
    status code, or error code, and page through results with `cursor`. History is retained for 7 days;
    anything older has been purged. Response bodies are not returned — only the request side of each
    call.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListApiRequestsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListApiRequestsResponse200 | ListApiRequestsResponse400 | ListApiRequestsResponse401 | ListApiRequestsResponse402 | ListApiRequestsResponse403 | ListApiRequestsResponse404 | ListApiRequestsResponse422 | ListApiRequestsResponse429 | ListApiRequestsResponse500 | ListApiRequestsResponse503]
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
    body: ListApiRequestsBody,
) -> (
    ListApiRequestsResponse200
    | ListApiRequestsResponse400
    | ListApiRequestsResponse401
    | ListApiRequestsResponse402
    | ListApiRequestsResponse403
    | ListApiRequestsResponse404
    | ListApiRequestsResponse422
    | ListApiRequestsResponse429
    | ListApiRequestsResponse500
    | ListApiRequestsResponse503
    | None
):
    """List your past API requests

     List the API requests your organization has made, newest first, with the parameters you sent and how
    each call turned out. Use it to answer 'what did my agent actually run?' — debugging a failed run,
    auditing usage, or quoting an `errorCode` in a support request. Filter by time range, route, method,
    status code, or error code, and page through results with `cursor`. History is retained for 7 days;
    anything older has been purged. Response bodies are not returned — only the request side of each
    call.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListApiRequestsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListApiRequestsResponse200 | ListApiRequestsResponse400 | ListApiRequestsResponse401 | ListApiRequestsResponse402 | ListApiRequestsResponse403 | ListApiRequestsResponse404 | ListApiRequestsResponse422 | ListApiRequestsResponse429 | ListApiRequestsResponse500 | ListApiRequestsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListApiRequestsBody,
) -> Response[
    ListApiRequestsResponse200
    | ListApiRequestsResponse400
    | ListApiRequestsResponse401
    | ListApiRequestsResponse402
    | ListApiRequestsResponse403
    | ListApiRequestsResponse404
    | ListApiRequestsResponse422
    | ListApiRequestsResponse429
    | ListApiRequestsResponse500
    | ListApiRequestsResponse503
]:
    """List your past API requests

     List the API requests your organization has made, newest first, with the parameters you sent and how
    each call turned out. Use it to answer 'what did my agent actually run?' — debugging a failed run,
    auditing usage, or quoting an `errorCode` in a support request. Filter by time range, route, method,
    status code, or error code, and page through results with `cursor`. History is retained for 7 days;
    anything older has been purged. Response bodies are not returned — only the request side of each
    call.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListApiRequestsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListApiRequestsResponse200 | ListApiRequestsResponse400 | ListApiRequestsResponse401 | ListApiRequestsResponse402 | ListApiRequestsResponse403 | ListApiRequestsResponse404 | ListApiRequestsResponse422 | ListApiRequestsResponse429 | ListApiRequestsResponse500 | ListApiRequestsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListApiRequestsBody,
) -> (
    ListApiRequestsResponse200
    | ListApiRequestsResponse400
    | ListApiRequestsResponse401
    | ListApiRequestsResponse402
    | ListApiRequestsResponse403
    | ListApiRequestsResponse404
    | ListApiRequestsResponse422
    | ListApiRequestsResponse429
    | ListApiRequestsResponse500
    | ListApiRequestsResponse503
    | None
):
    """List your past API requests

     List the API requests your organization has made, newest first, with the parameters you sent and how
    each call turned out. Use it to answer 'what did my agent actually run?' — debugging a failed run,
    auditing usage, or quoting an `errorCode` in a support request. Filter by time range, route, method,
    status code, or error code, and page through results with `cursor`. History is retained for 7 days;
    anything older has been purged. Response bodies are not returned — only the request side of each
    call.

    <span>⚡ <strong>Rate limit:</strong> 30 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title="Pricing
    shown is default pricing. Actual pricing may vary.">ⓘ</span></span>

    Args:
        body (ListApiRequestsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListApiRequestsResponse200 | ListApiRequestsResponse400 | ListApiRequestsResponse401 | ListApiRequestsResponse402 | ListApiRequestsResponse403 | ListApiRequestsResponse404 | ListApiRequestsResponse422 | ListApiRequestsResponse429 | ListApiRequestsResponse500 | ListApiRequestsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
