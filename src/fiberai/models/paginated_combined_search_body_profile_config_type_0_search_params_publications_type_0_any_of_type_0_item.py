from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_publications_type_0_any_of_type_0_item_keywords_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0ItemKeywordsType0,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0Item")


@_attrs_define
class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0Item:
    """
    Attributes:
        keywords (None |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0ItemKeywordsType0 | Unset):
    """

    keywords: (
        None
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0ItemKeywordsType0
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_publications_type_0_any_of_type_0_item_keywords_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0ItemKeywordsType0,  # noqa: PLC0415
        )

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(
            self.keywords,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0ItemKeywordsType0,
        ):
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
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_publications_type_0_any_of_type_0_item_keywords_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0ItemKeywordsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_keywords(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0ItemKeywordsType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0ItemKeywordsType0.from_dict(
                    data
                )

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPublicationsType0AnyOfType0ItemKeywordsType0
                | Unset,
                data,
            )

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        paginated_combined_search_body_profile_config_type_0_search_params_publications_type_0_any_of_type_0_item = cls(
            keywords=keywords,
        )

        paginated_combined_search_body_profile_config_type_0_search_params_publications_type_0_any_of_type_0_item.additional_properties = d
        return paginated_combined_search_body_profile_config_type_0_search_params_publications_type_0_any_of_type_0_item

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
