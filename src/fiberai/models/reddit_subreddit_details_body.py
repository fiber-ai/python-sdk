from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RedditSubredditDetailsBody")


@_attrs_define
class RedditSubredditDetailsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        subreddit (str): Subreddit name (e.g. 'AskReddit'), r/ prefix form (e.g. 'r/AskReddit'), or full subreddit URL.
    """

    api_key: str
    subreddit: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        subreddit = self.subreddit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "subreddit": subreddit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        subreddit = d.pop("subreddit")

        reddit_subreddit_details_body = cls(
            api_key=api_key,
            subreddit=subreddit,
        )

        reddit_subreddit_details_body.additional_properties = d
        return reddit_subreddit_details_body

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
