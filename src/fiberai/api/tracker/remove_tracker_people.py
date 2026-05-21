from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_tracker_people_body import RemoveTrackerPeopleBody
from ...models.remove_tracker_people_response_200 import RemoveTrackerPeopleResponse200
from ...models.remove_tracker_people_response_400 import RemoveTrackerPeopleResponse400
from ...models.remove_tracker_people_response_401 import RemoveTrackerPeopleResponse401
from ...models.remove_tracker_people_response_402 import RemoveTrackerPeopleResponse402
from ...models.remove_tracker_people_response_403 import RemoveTrackerPeopleResponse403
from ...models.remove_tracker_people_response_404 import RemoveTrackerPeopleResponse404
from ...models.remove_tracker_people_response_429 import RemoveTrackerPeopleResponse429
from ...models.remove_tracker_people_response_500 import RemoveTrackerPeopleResponse500
from ...models.remove_tracker_people_response_503 import RemoveTrackerPeopleResponse503
from ...types import UNSET, Response


def _get_kwargs(
    list_id: str,
    *,
    body: RemoveTrackerPeopleBody,
    api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["apiKey"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/tracker/person-lists/{list_id}/people".format(
            list_id=quote(str(list_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RemoveTrackerPeopleResponse200
    | RemoveTrackerPeopleResponse400
    | RemoveTrackerPeopleResponse401
    | RemoveTrackerPeopleResponse402
    | RemoveTrackerPeopleResponse403
    | RemoveTrackerPeopleResponse404
    | RemoveTrackerPeopleResponse429
    | RemoveTrackerPeopleResponse500
    | RemoveTrackerPeopleResponse503
    | None
):
    if response.status_code == 200:
        response_200 = RemoveTrackerPeopleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RemoveTrackerPeopleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RemoveTrackerPeopleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RemoveTrackerPeopleResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = RemoveTrackerPeopleResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveTrackerPeopleResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = RemoveTrackerPeopleResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RemoveTrackerPeopleResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = RemoveTrackerPeopleResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RemoveTrackerPeopleResponse200
    | RemoveTrackerPeopleResponse400
    | RemoveTrackerPeopleResponse401
    | RemoveTrackerPeopleResponse402
    | RemoveTrackerPeopleResponse403
    | RemoveTrackerPeopleResponse404
    | RemoveTrackerPeopleResponse429
    | RemoveTrackerPeopleResponse500
    | RemoveTrackerPeopleResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveTrackerPeopleBody,
    api_key: str,
) -> Response[
    RemoveTrackerPeopleResponse200
    | RemoveTrackerPeopleResponse400
    | RemoveTrackerPeopleResponse401
    | RemoveTrackerPeopleResponse402
    | RemoveTrackerPeopleResponse403
    | RemoveTrackerPeopleResponse404
    | RemoveTrackerPeopleResponse429
    | RemoveTrackerPeopleResponse500
    | RemoveTrackerPeopleResponse503
]:
    r"""Remove people from tracker list

     Remove people from a person tracker list. Deactivates them so they are no longer monitored, but
    preserves their signal history. Uses the same identifier format as add-people.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        body (RemoveTrackerPeopleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveTrackerPeopleResponse200 | RemoveTrackerPeopleResponse400 | RemoveTrackerPeopleResponse401 | RemoveTrackerPeopleResponse402 | RemoveTrackerPeopleResponse403 | RemoveTrackerPeopleResponse404 | RemoveTrackerPeopleResponse429 | RemoveTrackerPeopleResponse500 | RemoveTrackerPeopleResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveTrackerPeopleBody,
    api_key: str,
) -> (
    RemoveTrackerPeopleResponse200
    | RemoveTrackerPeopleResponse400
    | RemoveTrackerPeopleResponse401
    | RemoveTrackerPeopleResponse402
    | RemoveTrackerPeopleResponse403
    | RemoveTrackerPeopleResponse404
    | RemoveTrackerPeopleResponse429
    | RemoveTrackerPeopleResponse500
    | RemoveTrackerPeopleResponse503
    | None
):
    r"""Remove people from tracker list

     Remove people from a person tracker list. Deactivates them so they are no longer monitored, but
    preserves their signal history. Uses the same identifier format as add-people.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        body (RemoveTrackerPeopleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveTrackerPeopleResponse200 | RemoveTrackerPeopleResponse400 | RemoveTrackerPeopleResponse401 | RemoveTrackerPeopleResponse402 | RemoveTrackerPeopleResponse403 | RemoveTrackerPeopleResponse404 | RemoveTrackerPeopleResponse429 | RemoveTrackerPeopleResponse500 | RemoveTrackerPeopleResponse503
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        body=body,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveTrackerPeopleBody,
    api_key: str,
) -> Response[
    RemoveTrackerPeopleResponse200
    | RemoveTrackerPeopleResponse400
    | RemoveTrackerPeopleResponse401
    | RemoveTrackerPeopleResponse402
    | RemoveTrackerPeopleResponse403
    | RemoveTrackerPeopleResponse404
    | RemoveTrackerPeopleResponse429
    | RemoveTrackerPeopleResponse500
    | RemoveTrackerPeopleResponse503
]:
    r"""Remove people from tracker list

     Remove people from a person tracker list. Deactivates them so they are no longer monitored, but
    preserves their signal history. Uses the same identifier format as add-people.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        body (RemoveTrackerPeopleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveTrackerPeopleResponse200 | RemoveTrackerPeopleResponse400 | RemoveTrackerPeopleResponse401 | RemoveTrackerPeopleResponse402 | RemoveTrackerPeopleResponse403 | RemoveTrackerPeopleResponse404 | RemoveTrackerPeopleResponse429 | RemoveTrackerPeopleResponse500 | RemoveTrackerPeopleResponse503]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveTrackerPeopleBody,
    api_key: str,
) -> (
    RemoveTrackerPeopleResponse200
    | RemoveTrackerPeopleResponse400
    | RemoveTrackerPeopleResponse401
    | RemoveTrackerPeopleResponse402
    | RemoveTrackerPeopleResponse403
    | RemoveTrackerPeopleResponse404
    | RemoveTrackerPeopleResponse429
    | RemoveTrackerPeopleResponse500
    | RemoveTrackerPeopleResponse503
    | None
):
    r"""Remove people from tracker list

     Remove people from a person tracker list. Deactivates them so they are no longer monitored, but
    preserves their signal history. Uses the same identifier format as add-people.

    <span>⚡ <strong>Rate limit:</strong> 60 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> FREE! No credits are charged for this API.&nbsp;<span title=\"Pricing
    shown is default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        list_id (str):
        api_key (str):
        body (RemoveTrackerPeopleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveTrackerPeopleResponse200 | RemoveTrackerPeopleResponse400 | RemoveTrackerPeopleResponse401 | RemoveTrackerPeopleResponse402 | RemoveTrackerPeopleResponse403 | RemoveTrackerPeopleResponse404 | RemoveTrackerPeopleResponse429 | RemoveTrackerPeopleResponse500 | RemoveTrackerPeopleResponse503
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
            api_key=api_key,
        )
    ).parsed
