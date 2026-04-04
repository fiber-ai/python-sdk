from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.multi_source_search_body_search_type_0 import MultiSourceSearchBodySearchType0
    from ..models.multi_source_search_body_search_type_1 import MultiSourceSearchBodySearchType1


T = TypeVar("T", bound="MultiSourceSearchBody")


@_attrs_define
class MultiSourceSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        search (MultiSourceSearchBodySearchType0 | MultiSourceSearchBodySearchType1):
    """

    api_key: str
    search: MultiSourceSearchBodySearchType0 | MultiSourceSearchBodySearchType1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.multi_source_search_body_search_type_0 import MultiSourceSearchBodySearchType0

        api_key = self.api_key

        search: dict[str, Any]
        if isinstance(self.search, MultiSourceSearchBodySearchType0):
            search = self.search.to_dict()
        else:
            search = self.search.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "search": search,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multi_source_search_body_search_type_0 import MultiSourceSearchBodySearchType0
        from ..models.multi_source_search_body_search_type_1 import MultiSourceSearchBodySearchType1

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_search(data: object) -> MultiSourceSearchBodySearchType0 | MultiSourceSearchBodySearchType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_type_0 = MultiSourceSearchBodySearchType0.from_dict(data)

                return search_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            search_type_1 = MultiSourceSearchBodySearchType1.from_dict(data)

            return search_type_1

        search = _parse_search(d.pop("search"))

        multi_source_search_body = cls(
            api_key=api_key,
            search=search,
        )

        multi_source_search_body.additional_properties = d
        return multi_source_search_body

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
