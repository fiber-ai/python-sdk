from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.news_article_change_sentiment_type_1 import NewsArticleChangeSentimentType1
from ..models.news_article_change_sentiment_type_2_type_1 import NewsArticleChangeSentimentType2Type1
from ..models.news_article_change_sentiment_type_3_type_1 import NewsArticleChangeSentimentType3Type1

T = TypeVar("T", bound="NewsArticleChange")


@_attrs_define
class NewsArticleChange:
    """
    Attributes:
        url (str): Article URL
        title (str): Article title
        published_at (None | str): ISO date published
        publisher_name (None | str): Publisher name
        summary (None | str): Article summary
        sentiment (NewsArticleChangeSentimentType1 | NewsArticleChangeSentimentType2Type1 |
            NewsArticleChangeSentimentType3Type1 | None): Sentiment of the article. Null if not classified.
    """

    url: str
    title: str
    published_at: None | str
    publisher_name: None | str
    summary: None | str
    sentiment: (
        NewsArticleChangeSentimentType1
        | NewsArticleChangeSentimentType2Type1
        | NewsArticleChangeSentimentType3Type1
        | None
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        title = self.title

        published_at: None | str
        published_at = self.published_at

        publisher_name: None | str
        publisher_name = self.publisher_name

        summary: None | str
        summary = self.summary

        sentiment: None | str
        if isinstance(self.sentiment, NewsArticleChangeSentimentType1):
            sentiment = self.sentiment.value
        elif isinstance(self.sentiment, NewsArticleChangeSentimentType2Type1):
            sentiment = self.sentiment.value
        elif isinstance(self.sentiment, NewsArticleChangeSentimentType3Type1):
            sentiment = self.sentiment.value
        else:
            sentiment = self.sentiment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "title": title,
                "publishedAt": published_at,
                "publisherName": publisher_name,
                "summary": summary,
                "sentiment": sentiment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        title = d.pop("title")

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("publishedAt"))

        def _parse_publisher_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        publisher_name = _parse_publisher_name(d.pop("publisherName"))

        def _parse_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        summary = _parse_summary(d.pop("summary"))

        def _parse_sentiment(
            data: object,
        ) -> (
            NewsArticleChangeSentimentType1
            | NewsArticleChangeSentimentType2Type1
            | NewsArticleChangeSentimentType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_type_1 = NewsArticleChangeSentimentType1(data)

                return sentiment_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_type_2_type_1 = NewsArticleChangeSentimentType2Type1(data)

                return sentiment_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_type_3_type_1 = NewsArticleChangeSentimentType3Type1(data)

                return sentiment_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                NewsArticleChangeSentimentType1
                | NewsArticleChangeSentimentType2Type1
                | NewsArticleChangeSentimentType3Type1
                | None,
                data,
            )

        sentiment = _parse_sentiment(d.pop("sentiment"))

        news_article_change = cls(
            url=url,
            title=title,
            published_at=published_at,
            publisher_name=publisher_name,
            summary=summary,
            sentiment=sentiment,
        )

        news_article_change.additional_properties = d
        return news_article_change

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
