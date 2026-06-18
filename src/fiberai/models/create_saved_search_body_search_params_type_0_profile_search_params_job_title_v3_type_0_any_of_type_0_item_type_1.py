from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_title_v3_type_0_any_of_type_0_item_type_1_seniority_item import (
    CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1SeniorityItem,
)
from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_title_v3_type_0_any_of_type_0_item_type_1_type import (
    CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1Type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1")


@_attrs_define
class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1:
    """
    Attributes:
        type_ (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1Type):
        seniority (list[CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1Senio
            rityItem]):
        keywords (list[str] | None | Unset):
    """

    type_: CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1Type
    seniority: list[
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1SeniorityItem
    ]
    keywords: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        seniority = []
        for seniority_item_data in self.seniority:
            seniority_item = seniority_item_data.value
            seniority.append(seniority_item)

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "seniority": seniority,
            }
        )
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1Type(
            d.pop("type")
        )

        seniority = []
        _seniority = d.pop("seniority")
        for seniority_item_data in _seniority:
            seniority_item = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobTitleV3Type0AnyOfType0ItemType1SeniorityItem(
                seniority_item_data
            )

            seniority.append(seniority_item)

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        create_saved_search_body_search_params_type_0_profile_search_params_job_title_v3_type_0_any_of_type_0_item_type_1 = cls(
            type_=type_,
            seniority=seniority,
            keywords=keywords,
        )

        create_saved_search_body_search_params_type_0_profile_search_params_job_title_v3_type_0_any_of_type_0_item_type_1.additional_properties = d
        return create_saved_search_body_search_params_type_0_profile_search_params_job_title_v3_type_0_any_of_type_0_item_type_1

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
