from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_search_by_keywords_body_recency_type_1 import PostSearchByKeywordsBodyRecencyType1
from ..models.post_search_by_keywords_body_recency_type_2_type_1 import PostSearchByKeywordsBodyRecencyType2Type1
from ..models.post_search_by_keywords_body_recency_type_3_type_1 import PostSearchByKeywordsBodyRecencyType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSearchByKeywordsBody")


@_attrs_define
class PostSearchByKeywordsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        keywords (str): Keywords to search for in LinkedIn posts (comma-separated)
        recency (None | PostSearchByKeywordsBodyRecencyType1 | PostSearchByKeywordsBodyRecencyType2Type1 |
            PostSearchByKeywordsBodyRecencyType3Type1 | Unset): Filter by post age. Options: Day, Week, Month, Quarter,
            HalfYear, Year. Defaults to all time if omitted.
        cursor (None | str | Unset): Pagination cursor for fetching additional pages of posts
    """

    api_key: str
    keywords: str
    recency: (
        None
        | PostSearchByKeywordsBodyRecencyType1
        | PostSearchByKeywordsBodyRecencyType2Type1
        | PostSearchByKeywordsBodyRecencyType3Type1
        | Unset
    ) = UNSET
    cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        keywords = self.keywords

        recency: None | str | Unset
        if isinstance(self.recency, Unset):
            recency = UNSET
        elif isinstance(self.recency, PostSearchByKeywordsBodyRecencyType1):
            recency = self.recency.value
        elif isinstance(self.recency, PostSearchByKeywordsBodyRecencyType2Type1):
            recency = self.recency.value
        elif isinstance(self.recency, PostSearchByKeywordsBodyRecencyType3Type1):
            recency = self.recency.value
        else:
            recency = self.recency

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "keywords": keywords,
            }
        )
        if recency is not UNSET:
            field_dict["recency"] = recency
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        keywords = d.pop("keywords")

        def _parse_recency(
            data: object,
        ) -> (
            None
            | PostSearchByKeywordsBodyRecencyType1
            | PostSearchByKeywordsBodyRecencyType2Type1
            | PostSearchByKeywordsBodyRecencyType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recency_type_1 = PostSearchByKeywordsBodyRecencyType1(data)

                return recency_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recency_type_2_type_1 = PostSearchByKeywordsBodyRecencyType2Type1(data)

                return recency_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recency_type_3_type_1 = PostSearchByKeywordsBodyRecencyType3Type1(data)

                return recency_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PostSearchByKeywordsBodyRecencyType1
                | PostSearchByKeywordsBodyRecencyType2Type1
                | PostSearchByKeywordsBodyRecencyType3Type1
                | Unset,
                data,
            )

        recency = _parse_recency(d.pop("recency", UNSET))

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        post_search_by_keywords_body = cls(
            api_key=api_key,
            keywords=keywords,
            recency=recency,
            cursor=cursor,
        )

        post_search_by_keywords_body.additional_properties = d
        return post_search_by_keywords_body

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
