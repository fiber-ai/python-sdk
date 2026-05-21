from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reddit_subreddit_details_response_200_output_subreddit import (
        RedditSubredditDetailsResponse200OutputSubreddit,
    )


T = TypeVar("T", bound="RedditSubredditDetailsResponse200Output")


@_attrs_define
class RedditSubredditDetailsResponse200Output:
    """
    Attributes:
        subreddit (RedditSubredditDetailsResponse200OutputSubreddit): Subreddit metadata.
    """

    subreddit: RedditSubredditDetailsResponse200OutputSubreddit
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subreddit = self.subreddit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subreddit": subreddit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reddit_subreddit_details_response_200_output_subreddit import (
            RedditSubredditDetailsResponse200OutputSubreddit,
        )

        d = dict(src_dict)
        subreddit = RedditSubredditDetailsResponse200OutputSubreddit.from_dict(d.pop("subreddit"))

        reddit_subreddit_details_response_200_output = cls(
            subreddit=subreddit,
        )

        reddit_subreddit_details_response_200_output.additional_properties = d
        return reddit_subreddit_details_response_200_output

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
