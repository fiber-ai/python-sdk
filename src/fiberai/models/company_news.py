from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_news_sentiment_type_1 import CompanyNewsSentimentType1
from ..models.company_news_sentiment_type_2_type_1 import CompanyNewsSentimentType2Type1
from ..models.company_news_sentiment_type_3_type_1 import CompanyNewsSentimentType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyNews")


@_attrs_define
class CompanyNews:
    """
    Attributes:
        type_ (Literal['company_news']):
        entity_type (Literal['company']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        sentiment (CompanyNewsSentimentType1 | CompanyNewsSentimentType2Type1 | CompanyNewsSentimentType3Type1 | None |
            Unset): Only alert for news with this sentiment. Omit for any sentiment.
        min_articles (int | None | Unset): Only alert when at least this many articles are detected in a single check.
            Useful for filtering noise from single tangential mentions. Omit for any count.
    """

    type_: Literal["company_news"]
    entity_type: Literal["company"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    sentiment: (
        CompanyNewsSentimentType1 | CompanyNewsSentimentType2Type1 | CompanyNewsSentimentType3Type1 | None | Unset
    ) = UNSET
    min_articles: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        sentiment: None | str | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        elif isinstance(self.sentiment, CompanyNewsSentimentType1):
            sentiment = self.sentiment.value
        elif isinstance(self.sentiment, CompanyNewsSentimentType2Type1):
            sentiment = self.sentiment.value
        elif isinstance(self.sentiment, CompanyNewsSentimentType3Type1):
            sentiment = self.sentiment.value
        else:
            sentiment = self.sentiment

        min_articles: int | None | Unset
        if isinstance(self.min_articles, Unset):
            min_articles = UNSET
        else:
            min_articles = self.min_articles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if min_articles is not UNSET:
            field_dict["minArticles"] = min_articles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["company_news"], d.pop("type"))
        if type_ != "company_news":
            raise ValueError(f"type must match const 'company_news', got '{type_}'")

        entity_type = cast(Literal["company"], d.pop("entityType"))
        if entity_type != "company":
            raise ValueError(f"entityType must match const 'company', got '{entity_type}'")

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
        ) -> CompanyNewsSentimentType1 | CompanyNewsSentimentType2Type1 | CompanyNewsSentimentType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_type_1 = CompanyNewsSentimentType1(data)

                return sentiment_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_type_2_type_1 = CompanyNewsSentimentType2Type1(data)

                return sentiment_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_type_3_type_1 = CompanyNewsSentimentType3Type1(data)

                return sentiment_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanyNewsSentimentType1
                | CompanyNewsSentimentType2Type1
                | CompanyNewsSentimentType3Type1
                | None
                | Unset,
                data,
            )

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        def _parse_min_articles(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_articles = _parse_min_articles(d.pop("minArticles", UNSET))

        company_news = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            sentiment=sentiment,
            min_articles=min_articles,
        )

        company_news.additional_properties = d
        return company_news

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
