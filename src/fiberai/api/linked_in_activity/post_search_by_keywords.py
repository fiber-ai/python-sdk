from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_search_by_keywords_body import PostSearchByKeywordsBody
from ...models.post_search_by_keywords_response_200 import PostSearchByKeywordsResponse200
from ...models.post_search_by_keywords_response_400 import PostSearchByKeywordsResponse400
from ...models.post_search_by_keywords_response_401 import PostSearchByKeywordsResponse401
from ...models.post_search_by_keywords_response_402 import PostSearchByKeywordsResponse402
from ...models.post_search_by_keywords_response_403 import PostSearchByKeywordsResponse403
from ...models.post_search_by_keywords_response_404 import PostSearchByKeywordsResponse404
from ...models.post_search_by_keywords_response_422 import PostSearchByKeywordsResponse422
from ...models.post_search_by_keywords_response_429 import PostSearchByKeywordsResponse429
from ...models.post_search_by_keywords_response_500 import PostSearchByKeywordsResponse500
from ...models.post_search_by_keywords_response_503 import PostSearchByKeywordsResponse503
from ...types import Response


def _get_kwargs(
    *,
    body: PostSearchByKeywordsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/linkedin-live-fetch/posts/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSearchByKeywordsResponse200
    | PostSearchByKeywordsResponse400
    | PostSearchByKeywordsResponse401
    | PostSearchByKeywordsResponse402
    | PostSearchByKeywordsResponse403
    | PostSearchByKeywordsResponse404
    | PostSearchByKeywordsResponse422
    | PostSearchByKeywordsResponse429
    | PostSearchByKeywordsResponse500
    | PostSearchByKeywordsResponse503
    | None
):
    if response.status_code == 200:
        response_200 = PostSearchByKeywordsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostSearchByKeywordsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSearchByKeywordsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PostSearchByKeywordsResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = PostSearchByKeywordsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSearchByKeywordsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PostSearchByKeywordsResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = PostSearchByKeywordsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostSearchByKeywordsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSearchByKeywordsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSearchByKeywordsResponse200
    | PostSearchByKeywordsResponse400
    | PostSearchByKeywordsResponse401
    | PostSearchByKeywordsResponse402
    | PostSearchByKeywordsResponse403
    | PostSearchByKeywordsResponse404
    | PostSearchByKeywordsResponse422
    | PostSearchByKeywordsResponse429
    | PostSearchByKeywordsResponse500
    | PostSearchByKeywordsResponse503
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
    body: PostSearchByKeywordsBody,
) -> Response[
    PostSearchByKeywordsResponse200
    | PostSearchByKeywordsResponse400
    | PostSearchByKeywordsResponse401
    | PostSearchByKeywordsResponse402
    | PostSearchByKeywordsResponse403
    | PostSearchByKeywordsResponse404
    | PostSearchByKeywordsResponse422
    | PostSearchByKeywordsResponse429
    | PostSearchByKeywordsResponse500
    | PostSearchByKeywordsResponse503
]:
    r"""Search LinkedIn posts by keywords

     Search LinkedIn posts using keyword-based queries. Returns a paginated list of posts matching the
    search criteria, up to 50 per page.

    **Keyword Search Syntax:**
    - **Exact phrase:** Wrap keywords in quotes for exact phrase matching. \"head of sales\" matches the
    exact phrase, not the individual words.
    - **AND:** Use **AND** between keywords to require both terms. sales **AND** engineering matches
    posts containing both words.
    - **OR:** Use **OR** between keywords to match posts containing any of the terms. sales **OR**
    marketing matches posts with either word.
    - **NOT:** Use **NOT** before a keyword to exclude posts containing that term. sales **NOT**
    recruiter matches posts with \"sales\" but without \"recruiter\".
    - **Parentheses:** Group terms to control operator precedence. (sales **OR** marketing) **AND**
    \"series A\" finds posts about either sales or marketing that also mention \"series A\".

    **Order of precedence:**
    1. **Quotes (\" \"):** Exact phrase match. Phrase matching occurs before any Boolean logic is
    applied.
    2. **Parentheses (()):** Used to explicitly group Boolean logic. Grouped expressions are evaluated
    before ungrouped logic.
    3. **NOT:** Applied after any parentheses or quoted phrases are resolved.
    4. **AND:** Evaluated after **NOT** but before **OR**.
    5. **OR:** Lowest precedence among Boolean operators.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PostSearchByKeywordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSearchByKeywordsResponse200 | PostSearchByKeywordsResponse400 | PostSearchByKeywordsResponse401 | PostSearchByKeywordsResponse402 | PostSearchByKeywordsResponse403 | PostSearchByKeywordsResponse404 | PostSearchByKeywordsResponse422 | PostSearchByKeywordsResponse429 | PostSearchByKeywordsResponse500 | PostSearchByKeywordsResponse503]
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
    body: PostSearchByKeywordsBody,
) -> (
    PostSearchByKeywordsResponse200
    | PostSearchByKeywordsResponse400
    | PostSearchByKeywordsResponse401
    | PostSearchByKeywordsResponse402
    | PostSearchByKeywordsResponse403
    | PostSearchByKeywordsResponse404
    | PostSearchByKeywordsResponse422
    | PostSearchByKeywordsResponse429
    | PostSearchByKeywordsResponse500
    | PostSearchByKeywordsResponse503
    | None
):
    r"""Search LinkedIn posts by keywords

     Search LinkedIn posts using keyword-based queries. Returns a paginated list of posts matching the
    search criteria, up to 50 per page.

    **Keyword Search Syntax:**
    - **Exact phrase:** Wrap keywords in quotes for exact phrase matching. \"head of sales\" matches the
    exact phrase, not the individual words.
    - **AND:** Use **AND** between keywords to require both terms. sales **AND** engineering matches
    posts containing both words.
    - **OR:** Use **OR** between keywords to match posts containing any of the terms. sales **OR**
    marketing matches posts with either word.
    - **NOT:** Use **NOT** before a keyword to exclude posts containing that term. sales **NOT**
    recruiter matches posts with \"sales\" but without \"recruiter\".
    - **Parentheses:** Group terms to control operator precedence. (sales **OR** marketing) **AND**
    \"series A\" finds posts about either sales or marketing that also mention \"series A\".

    **Order of precedence:**
    1. **Quotes (\" \"):** Exact phrase match. Phrase matching occurs before any Boolean logic is
    applied.
    2. **Parentheses (()):** Used to explicitly group Boolean logic. Grouped expressions are evaluated
    before ungrouped logic.
    3. **NOT:** Applied after any parentheses or quoted phrases are resolved.
    4. **AND:** Evaluated after **NOT** but before **OR**.
    5. **OR:** Lowest precedence among Boolean operators.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PostSearchByKeywordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSearchByKeywordsResponse200 | PostSearchByKeywordsResponse400 | PostSearchByKeywordsResponse401 | PostSearchByKeywordsResponse402 | PostSearchByKeywordsResponse403 | PostSearchByKeywordsResponse404 | PostSearchByKeywordsResponse422 | PostSearchByKeywordsResponse429 | PostSearchByKeywordsResponse500 | PostSearchByKeywordsResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSearchByKeywordsBody,
) -> Response[
    PostSearchByKeywordsResponse200
    | PostSearchByKeywordsResponse400
    | PostSearchByKeywordsResponse401
    | PostSearchByKeywordsResponse402
    | PostSearchByKeywordsResponse403
    | PostSearchByKeywordsResponse404
    | PostSearchByKeywordsResponse422
    | PostSearchByKeywordsResponse429
    | PostSearchByKeywordsResponse500
    | PostSearchByKeywordsResponse503
]:
    r"""Search LinkedIn posts by keywords

     Search LinkedIn posts using keyword-based queries. Returns a paginated list of posts matching the
    search criteria, up to 50 per page.

    **Keyword Search Syntax:**
    - **Exact phrase:** Wrap keywords in quotes for exact phrase matching. \"head of sales\" matches the
    exact phrase, not the individual words.
    - **AND:** Use **AND** between keywords to require both terms. sales **AND** engineering matches
    posts containing both words.
    - **OR:** Use **OR** between keywords to match posts containing any of the terms. sales **OR**
    marketing matches posts with either word.
    - **NOT:** Use **NOT** before a keyword to exclude posts containing that term. sales **NOT**
    recruiter matches posts with \"sales\" but without \"recruiter\".
    - **Parentheses:** Group terms to control operator precedence. (sales **OR** marketing) **AND**
    \"series A\" finds posts about either sales or marketing that also mention \"series A\".

    **Order of precedence:**
    1. **Quotes (\" \"):** Exact phrase match. Phrase matching occurs before any Boolean logic is
    applied.
    2. **Parentheses (()):** Used to explicitly group Boolean logic. Grouped expressions are evaluated
    before ungrouped logic.
    3. **NOT:** Applied after any parentheses or quoted phrases are resolved.
    4. **AND:** Evaluated after **NOT** but before **OR**.
    5. **OR:** Lowest precedence among Boolean operators.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PostSearchByKeywordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSearchByKeywordsResponse200 | PostSearchByKeywordsResponse400 | PostSearchByKeywordsResponse401 | PostSearchByKeywordsResponse402 | PostSearchByKeywordsResponse403 | PostSearchByKeywordsResponse404 | PostSearchByKeywordsResponse422 | PostSearchByKeywordsResponse429 | PostSearchByKeywordsResponse500 | PostSearchByKeywordsResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSearchByKeywordsBody,
) -> (
    PostSearchByKeywordsResponse200
    | PostSearchByKeywordsResponse400
    | PostSearchByKeywordsResponse401
    | PostSearchByKeywordsResponse402
    | PostSearchByKeywordsResponse403
    | PostSearchByKeywordsResponse404
    | PostSearchByKeywordsResponse422
    | PostSearchByKeywordsResponse429
    | PostSearchByKeywordsResponse500
    | PostSearchByKeywordsResponse503
    | None
):
    r"""Search LinkedIn posts by keywords

     Search LinkedIn posts using keyword-based queries. Returns a paginated list of posts matching the
    search criteria, up to 50 per page.

    **Keyword Search Syntax:**
    - **Exact phrase:** Wrap keywords in quotes for exact phrase matching. \"head of sales\" matches the
    exact phrase, not the individual words.
    - **AND:** Use **AND** between keywords to require both terms. sales **AND** engineering matches
    posts containing both words.
    - **OR:** Use **OR** between keywords to match posts containing any of the terms. sales **OR**
    marketing matches posts with either word.
    - **NOT:** Use **NOT** before a keyword to exclude posts containing that term. sales **NOT**
    recruiter matches posts with \"sales\" but without \"recruiter\".
    - **Parentheses:** Group terms to control operator precedence. (sales **OR** marketing) **AND**
    \"series A\" finds posts about either sales or marketing that also mention \"series A\".

    **Order of precedence:**
    1. **Quotes (\" \"):** Exact phrase match. Phrase matching occurs before any Boolean logic is
    applied.
    2. **Parentheses (()):** Used to explicitly group Boolean logic. Grouped expressions are evaluated
    before ungrouped logic.
    3. **NOT:** Applied after any parentheses or quoted phrases are resolved.
    4. **AND:** Evaluated after **NOT** but before **OR**.
    5. **OR:** Lowest precedence among Boolean operators.

    <span>⚡ <strong>Rate limit:</strong> 300 requests per 1 minute</span>

    <span>💰 <strong>Cost:</strong> 2 credits per page of results&nbsp;<span title=\"Pricing shown is
    default pricing. Actual pricing may vary.\">ⓘ</span></span>

    <span>⏱ <strong>Recommended timeout:</strong> 1 minute&nbsp;<span title=\"Recommended timeout: set
    your HTTP client timeout to at least 1 minute for this endpoint.\">ⓘ</span></span>

    Args:
        body (PostSearchByKeywordsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSearchByKeywordsResponse200 | PostSearchByKeywordsResponse400 | PostSearchByKeywordsResponse401 | PostSearchByKeywordsResponse402 | PostSearchByKeywordsResponse403 | PostSearchByKeywordsResponse404 | PostSearchByKeywordsResponse422 | PostSearchByKeywordsResponse429 | PostSearchByKeywordsResponse500 | PostSearchByKeywordsResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
