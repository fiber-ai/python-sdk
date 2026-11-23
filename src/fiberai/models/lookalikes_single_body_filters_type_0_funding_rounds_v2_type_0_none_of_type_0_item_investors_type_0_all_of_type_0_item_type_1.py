from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lookalikes_single_body_filters_type_0_funding_rounds_v2_type_0_none_of_type_0_item_investors_type_0_all_of_type_0_item_type_1_type import (
    LookalikesSingleBodyFiltersType0FundingRoundsV2Type0NoneOfType0ItemInvestorsType0AllOfType0ItemType1Type,
)

T = TypeVar(
    "T", bound="LookalikesSingleBodyFiltersType0FundingRoundsV2Type0NoneOfType0ItemInvestorsType0AllOfType0ItemType1"
)


@_attrs_define
class LookalikesSingleBodyFiltersType0FundingRoundsV2Type0NoneOfType0ItemInvestorsType0AllOfType0ItemType1:
    """
    Attributes:
        type_
            (LookalikesSingleBodyFiltersType0FundingRoundsV2Type0NoneOfType0ItemInvestorsType0AllOfType0ItemType1Type):
        linkedin_url (str):
    """

    type_: LookalikesSingleBodyFiltersType0FundingRoundsV2Type0NoneOfType0ItemInvestorsType0AllOfType0ItemType1Type
    linkedin_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        linkedin_url = self.linkedin_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "linkedin_url": linkedin_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = (
            LookalikesSingleBodyFiltersType0FundingRoundsV2Type0NoneOfType0ItemInvestorsType0AllOfType0ItemType1Type(
                d.pop("type")
            )
        )

        linkedin_url = d.pop("linkedin_url")

        lookalikes_single_body_filters_type_0_funding_rounds_v2_type_0_none_of_type_0_item_investors_type_0_all_of_type_0_item_type_1 = cls(
            type_=type_,
            linkedin_url=linkedin_url,
        )

        lookalikes_single_body_filters_type_0_funding_rounds_v2_type_0_none_of_type_0_item_investors_type_0_all_of_type_0_item_type_1.additional_properties = d
        return lookalikes_single_body_filters_type_0_funding_rounds_v2_type_0_none_of_type_0_item_investors_type_0_all_of_type_0_item_type_1

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
