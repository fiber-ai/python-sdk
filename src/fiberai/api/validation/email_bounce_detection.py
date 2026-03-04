from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.email_bounce_detection_body import EmailBounceDetectionBody
from ...models.email_bounce_detection_response_200 import EmailBounceDetectionResponse200
from ...models.email_bounce_detection_response_400 import EmailBounceDetectionResponse400
from ...models.email_bounce_detection_response_401 import EmailBounceDetectionResponse401
from ...models.email_bounce_detection_response_402 import EmailBounceDetectionResponse402
from ...models.email_bounce_detection_response_403 import EmailBounceDetectionResponse403
from ...models.email_bounce_detection_response_404 import EmailBounceDetectionResponse404
from ...models.email_bounce_detection_response_429 import EmailBounceDetectionResponse429
from ...models.email_bounce_detection_response_500 import EmailBounceDetectionResponse500
from typing import cast



def _get_kwargs(
    *,
    body: EmailBounceDetectionBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/validate-email/single",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]]:
    if response.status_code == 200:
        response_200 = EmailBounceDetectionResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = EmailBounceDetectionResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = EmailBounceDetectionResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = EmailBounceDetectionResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = EmailBounceDetectionResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = EmailBounceDetectionResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = EmailBounceDetectionResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = EmailBounceDetectionResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmailBounceDetectionBody,

) -> Response[Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]]:
    r""" Validate a single email

     Checks if a given email is likely to bounce using a waterfall of strategies. Works for catch-all
    email addresses, which are increasingly common yet hard for other APIs to validate.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per email validation&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (EmailBounceDetectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]]
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
    client: Union[AuthenticatedClient, Client],
    body: EmailBounceDetectionBody,

) -> Optional[Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]]:
    r""" Validate a single email

     Checks if a given email is likely to bounce using a waterfall of strategies. Works for catch-all
    email addresses, which are increasingly common yet hard for other APIs to validate.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per email validation&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (EmailBounceDetectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmailBounceDetectionBody,

) -> Response[Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]]:
    r""" Validate a single email

     Checks if a given email is likely to bounce using a waterfall of strategies. Works for catch-all
    email addresses, which are increasingly common yet hard for other APIs to validate.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per email validation&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (EmailBounceDetectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmailBounceDetectionBody,

) -> Optional[Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]]:
    r""" Validate a single email

     Checks if a given email is likely to bounce using a waterfall of strategies. Works for catch-all
    email addresses, which are increasingly common yet hard for other APIs to validate.

    <span>⚡ <strong>Rate limit:</strong> 10 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per email validation&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (EmailBounceDetectionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EmailBounceDetectionResponse200, EmailBounceDetectionResponse400, EmailBounceDetectionResponse401, EmailBounceDetectionResponse402, EmailBounceDetectionResponse403, EmailBounceDetectionResponse404, EmailBounceDetectionResponse429, EmailBounceDetectionResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
