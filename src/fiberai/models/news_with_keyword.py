from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.news_with_keyword_sentiment_type_1 import NewsWithKeywordSentimentType1
from ..models.news_with_keyword_sentiment_type_2_type_1 import NewsWithKeywordSentimentType2Type1
from ..models.news_with_keyword_sentiment_type_3_type_1 import NewsWithKeywordSentimentType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsWithKeyword")


@_attrs_define
class NewsWithKeyword:
    """
    Attributes:
        type_ (Literal['news_with_keyword']):
        entity_type (Literal['company']):
        keywords (list[str]): Alert when a news article title or summary matches any keyword
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        sentiment (NewsWithKeywordSentimentType1 | NewsWithKeywordSentimentType2Type1 |
            NewsWithKeywordSentimentType3Type1 | None | Unset): Only alert for news with this sentiment. Omit for any
            sentiment.
    """

    type_: Literal["news_with_keyword"]
    entity_type: Literal["company"]
    keywords: list[str]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    sentiment: (
        NewsWithKeywordSentimentType1
        | NewsWithKeywordSentimentType2Type1
        | NewsWithKeywordSentimentType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        keywords = self.keywords

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        sentiment: None | str | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        elif isinstance(self.sentiment, NewsWithKeywordSentimentType1):
            sentiment = self.sentiment.value
        elif isinstance(self.sentiment, NewsWithKeywordSentimentType2Type1):
            sentiment = self.sentiment.value
        elif isinstance(self.sentiment, NewsWithKeywordSentimentType3Type1):
            sentiment = self.sentiment.value
        else:
            sentiment = self.sentiment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
                "keywords": keywords,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["news_with_keyword"], d.pop("type"))
        if type_ != "news_with_keyword":
            raise ValueError(f"type must match const 'news_with_keyword', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

        keywords = cast(list[str], d.pop("keywords"))

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_sentiment(
            data: object,
        ) -> (
            NewsWithKeywordSentimentType1
            | NewsWithKeywordSentimentType2Type1
            | NewsWithKeywordSentimentType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_type_1 = NewsWithKeywordSentimentType1(data)

                return sentiment_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_type_2_type_1 = NewsWithKeywordSentimentType2Type1(data)

                return sentiment_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_type_3_type_1 = NewsWithKeywordSentimentType3Type1(data)

                return sentiment_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                NewsWithKeywordSentimentType1
                | NewsWithKeywordSentimentType2Type1
                | NewsWithKeywordSentimentType3Type1
                | None
                | Unset,
                data,
            )

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        news_with_keyword = cls(
            type_=type_,
            entity_type=entity_type,
            keywords=keywords,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            sentiment=sentiment,
        )

        news_with_keyword.additional_properties = d
        return news_with_keyword

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
