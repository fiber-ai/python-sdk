from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TwitterTweetRepliesResponse200OutputTweetsItem")


@_attrs_define
class TwitterTweetRepliesResponse200OutputTweetsItem:
    """
    Attributes:
        id (None | str | Unset): Numeric tweet ID.
        text (None | str | Unset): Full tweet text.
        created_at (None | str | Unset): When the tweet was created.
        like_count (float | None | Unset): Number of likes.
        reply_count (float | None | Unset): Number of replies.
        retweet_count (float | None | Unset): Number of retweets.
        quote_count (float | None | Unset): Number of quote tweets.
        view_count (float | None | Unset): Number of views.
        bookmark_count (float | None | Unset): Number of bookmarks.
        is_retweet (bool | None | Unset): Whether this tweet is a retweet.
        is_reply (bool | None | Unset): Whether this tweet is a reply to another tweet.
        lang (None | str | Unset): BCP-47 language code detected for the tweet (e.g. 'en' for English, 'es' for
            Spanish).
    """

    id: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    created_at: None | str | Unset = UNSET
    like_count: float | None | Unset = UNSET
    reply_count: float | None | Unset = UNSET
    retweet_count: float | None | Unset = UNSET
    quote_count: float | None | Unset = UNSET
    view_count: float | None | Unset = UNSET
    bookmark_count: float | None | Unset = UNSET
    is_retweet: bool | None | Unset = UNSET
    is_reply: bool | None | Unset = UNSET
    lang: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        like_count: float | None | Unset
        if isinstance(self.like_count, Unset):
            like_count = UNSET
        else:
            like_count = self.like_count

        reply_count: float | None | Unset
        if isinstance(self.reply_count, Unset):
            reply_count = UNSET
        else:
            reply_count = self.reply_count

        retweet_count: float | None | Unset
        if isinstance(self.retweet_count, Unset):
            retweet_count = UNSET
        else:
            retweet_count = self.retweet_count

        quote_count: float | None | Unset
        if isinstance(self.quote_count, Unset):
            quote_count = UNSET
        else:
            quote_count = self.quote_count

        view_count: float | None | Unset
        if isinstance(self.view_count, Unset):
            view_count = UNSET
        else:
            view_count = self.view_count

        bookmark_count: float | None | Unset
        if isinstance(self.bookmark_count, Unset):
            bookmark_count = UNSET
        else:
            bookmark_count = self.bookmark_count

        is_retweet: bool | None | Unset
        if isinstance(self.is_retweet, Unset):
            is_retweet = UNSET
        else:
            is_retweet = self.is_retweet

        is_reply: bool | None | Unset
        if isinstance(self.is_reply, Unset):
            is_reply = UNSET
        else:
            is_reply = self.is_reply

        lang: None | str | Unset
        if isinstance(self.lang, Unset):
            lang = UNSET
        else:
            lang = self.lang

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if like_count is not UNSET:
            field_dict["likeCount"] = like_count
        if reply_count is not UNSET:
            field_dict["replyCount"] = reply_count
        if retweet_count is not UNSET:
            field_dict["retweetCount"] = retweet_count
        if quote_count is not UNSET:
            field_dict["quoteCount"] = quote_count
        if view_count is not UNSET:
            field_dict["viewCount"] = view_count
        if bookmark_count is not UNSET:
            field_dict["bookmarkCount"] = bookmark_count
        if is_retweet is not UNSET:
            field_dict["isRetweet"] = is_retweet
        if is_reply is not UNSET:
            field_dict["isReply"] = is_reply
        if lang is not UNSET:
            field_dict["lang"] = lang

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_like_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        like_count = _parse_like_count(d.pop("likeCount", UNSET))

        def _parse_reply_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        reply_count = _parse_reply_count(d.pop("replyCount", UNSET))

        def _parse_retweet_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        retweet_count = _parse_retweet_count(d.pop("retweetCount", UNSET))

        def _parse_quote_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quote_count = _parse_quote_count(d.pop("quoteCount", UNSET))

        def _parse_view_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        view_count = _parse_view_count(d.pop("viewCount", UNSET))

        def _parse_bookmark_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bookmark_count = _parse_bookmark_count(d.pop("bookmarkCount", UNSET))

        def _parse_is_retweet(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_retweet = _parse_is_retweet(d.pop("isRetweet", UNSET))

        def _parse_is_reply(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_reply = _parse_is_reply(d.pop("isReply", UNSET))

        def _parse_lang(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lang = _parse_lang(d.pop("lang", UNSET))

        twitter_tweet_replies_response_200_output_tweets_item = cls(
            id=id,
            text=text,
            created_at=created_at,
            like_count=like_count,
            reply_count=reply_count,
            retweet_count=retweet_count,
            quote_count=quote_count,
            view_count=view_count,
            bookmark_count=bookmark_count,
            is_retweet=is_retweet,
            is_reply=is_reply,
            lang=lang,
        )

        twitter_tweet_replies_response_200_output_tweets_item.additional_properties = d
        return twitter_tweet_replies_response_200_output_tweets_item

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
