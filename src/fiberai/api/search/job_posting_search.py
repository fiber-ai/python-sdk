from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.job_posting_search_body import JobPostingSearchBody
from ...models.job_posting_search_response_200 import JobPostingSearchResponse200
from ...models.job_posting_search_response_400 import JobPostingSearchResponse400
from ...models.job_posting_search_response_401 import JobPostingSearchResponse401
from ...models.job_posting_search_response_402 import JobPostingSearchResponse402
from ...models.job_posting_search_response_403 import JobPostingSearchResponse403
from ...models.job_posting_search_response_404 import JobPostingSearchResponse404
from ...models.job_posting_search_response_429 import JobPostingSearchResponse429
from ...models.job_posting_search_response_500 import JobPostingSearchResponse500
from typing import cast



def _get_kwargs(
    *,
    body: JobPostingSearchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/job-search",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]]:
    if response.status_code == 200:
        response_200 = JobPostingSearchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = JobPostingSearchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = JobPostingSearchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = JobPostingSearchResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = JobPostingSearchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = JobPostingSearchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = JobPostingSearchResponse429.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = JobPostingSearchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: JobPostingSearchBody,

) -> Response[Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]]:
    r""" Job postings search

     Search for job postings with flexible filtering capabilities

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per job posting found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JobPostingSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]]
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
    body: JobPostingSearchBody,

) -> Optional[Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]]:
    r""" Job postings search

     Search for job postings with flexible filtering capabilities

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per job posting found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JobPostingSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: JobPostingSearchBody,

) -> Response[Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]]:
    r""" Job postings search

     Search for job postings with flexible filtering capabilities

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per job posting found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JobPostingSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]]
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
    body: JobPostingSearchBody,

) -> Optional[Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]]:
    r""" Job postings search

     Search for job postings with flexible filtering capabilities

    <span>⚡ <strong>Rate limit:</strong> 20 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 1 credit per job posting found&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    Args:
        body (JobPostingSearchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[JobPostingSearchResponse200, JobPostingSearchResponse400, JobPostingSearchResponse401, JobPostingSearchResponse402, JobPostingSearchResponse403, JobPostingSearchResponse404, JobPostingSearchResponse429, JobPostingSearchResponse500]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
