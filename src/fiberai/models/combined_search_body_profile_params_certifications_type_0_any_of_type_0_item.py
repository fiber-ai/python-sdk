from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_search_body_profile_params_certifications_type_0_any_of_type_0_item_keywords_type_0 import (
        CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0ItemKeywordsType0,
    )


T = TypeVar("T", bound="CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0Item")


@_attrs_define
class CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0Item:
    """
    Attributes:
        keywords (CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0ItemKeywordsType0 | None | Unset):
    """

    keywords: CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0ItemKeywordsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_body_profile_params_certifications_type_0_any_of_type_0_item_keywords_type_0 import (
            CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0ItemKeywordsType0,
        )

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0ItemKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_search_body_profile_params_certifications_type_0_any_of_type_0_item_keywords_type_0 import (
            CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0ItemKeywordsType0,
        )

        d = dict(src_dict)

        def _parse_keywords(
            data: object,
        ) -> CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0ItemKeywordsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = (
                    CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0ItemKeywordsType0.from_dict(data)
                )

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CombinedSearchBodyProfileParamsCertificationsType0AnyOfType0ItemKeywordsType0 | None | Unset, data
            )

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        combined_search_body_profile_params_certifications_type_0_any_of_type_0_item = cls(
            keywords=keywords,
        )

        combined_search_body_profile_params_certifications_type_0_any_of_type_0_item.additional_properties = d
        return combined_search_body_profile_params_certifications_type_0_any_of_type_0_item

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
