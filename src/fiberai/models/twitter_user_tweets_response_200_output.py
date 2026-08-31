from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.twitter_user_tweets_response_200_output_tweets_item import (
        TwitterUserTweetsResponse200OutputTweetsItem,
    )


T = TypeVar("T", bound="TwitterUserTweetsResponse200Output")


@_attrs_define
class TwitterUserTweetsResponse200Output:
    """
    Attributes:
        tweets (list[TwitterUserTweetsResponse200OutputTweetsItem]): List of tweets for this page.
        next_cursor (None | str | Unset): Cursor to retrieve the next page of tweets. Pass as `cursor` in the next
            request. Null if there are no more pages.
    """

    tweets: list[TwitterUserTweetsResponse200OutputTweetsItem]
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tweets = []
        for tweets_item_data in self.tweets:
            tweets_item = tweets_item_data.to_dict()
            tweets.append(tweets_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tweets": tweets,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.twitter_user_tweets_response_200_output_tweets_item import (
            TwitterUserTweetsResponse200OutputTweetsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        tweets = []
        _tweets = d.pop("tweets")
        for tweets_item_data in _tweets:
            tweets_item = TwitterUserTweetsResponse200OutputTweetsItem.from_dict(tweets_item_data)

            tweets.append(tweets_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        twitter_user_tweets_response_200_output = cls(
            tweets=tweets,
            next_cursor=next_cursor,
        )

        twitter_user_tweets_response_200_output.additional_properties = d
        return twitter_user_tweets_response_200_output

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
