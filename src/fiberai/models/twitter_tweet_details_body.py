from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TwitterTweetDetailsBody")


@_attrs_define
class TwitterTweetDetailsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        tweet_id (str): Numeric tweet ID to fetch (e.g. '1234567890123456789'). Must contain only digits.
    """

    api_key: str
    tweet_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        tweet_id = self.tweet_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "tweetId": tweet_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        tweet_id = d.pop("tweetId")

        twitter_tweet_details_body = cls(
            api_key=api_key,
            tweet_id=tweet_id,
        )

        twitter_tweet_details_body.additional_properties = d
        return twitter_tweet_details_body

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
