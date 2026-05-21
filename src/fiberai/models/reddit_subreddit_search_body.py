from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reddit_subreddit_search_body_sort import RedditSubredditSearchBodySort
from ..models.reddit_subreddit_search_body_timeframe import RedditSubredditSearchBodyTimeframe
from ..types import UNSET, Unset

T = TypeVar("T", bound="RedditSubredditSearchBody")


@_attrs_define
class RedditSubredditSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        subreddit (str): Subreddit name (e.g. 'AskReddit'), r/ prefix form (e.g. 'r/AskReddit'), or full subreddit URL.
        query (str): Search query.
        sort (RedditSubredditSearchBodySort | Unset): Sort order for subreddit search results. Default:
            RedditSubredditSearchBodySort.RELEVANCE.
        timeframe (RedditSubredditSearchBodyTimeframe | Unset): Time window for subreddit search filtering. Default:
            RedditSubredditSearchBodyTimeframe.ALL.
        next_page_token (None | str | Unset): Pagination token from a previous response to retrieve the next page. Omit
            for the first page.
    """

    api_key: str
    subreddit: str
    query: str
    sort: RedditSubredditSearchBodySort | Unset = RedditSubredditSearchBodySort.RELEVANCE
    timeframe: RedditSubredditSearchBodyTimeframe | Unset = RedditSubredditSearchBodyTimeframe.ALL
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        subreddit = self.subreddit

        query = self.query

        sort: str | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.value

        timeframe: str | Unset = UNSET
        if not isinstance(self.timeframe, Unset):
            timeframe = self.timeframe.value

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "subreddit": subreddit,
                "query": query,
            }
        )
        if sort is not UNSET:
            field_dict["sort"] = sort
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        subreddit = d.pop("subreddit")

        query = d.pop("query")

        _sort = d.pop("sort", UNSET)
        sort: RedditSubredditSearchBodySort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = RedditSubredditSearchBodySort(_sort)

        _timeframe = d.pop("timeframe", UNSET)
        timeframe: RedditSubredditSearchBodyTimeframe | Unset
        if isinstance(_timeframe, Unset):
            timeframe = UNSET
        else:
            timeframe = RedditSubredditSearchBodyTimeframe(_timeframe)

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        reddit_subreddit_search_body = cls(
            api_key=api_key,
            subreddit=subreddit,
            query=query,
            sort=sort,
            timeframe=timeframe,
            next_page_token=next_page_token,
        )

        reddit_subreddit_search_body.additional_properties = d
        return reddit_subreddit_search_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
