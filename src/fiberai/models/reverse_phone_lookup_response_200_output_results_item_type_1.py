from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reverse_phone_lookup_response_200_output_results_item_type_1_type import (
    ReversePhoneLookupResponse200OutputResultsItemType1Type,
)

if TYPE_CHECKING:
    from ..models.reverse_phone_lookup_response_200_output_results_item_type_1_company import (
        ReversePhoneLookupResponse200OutputResultsItemType1Company,
    )


T = TypeVar("T", bound="ReversePhoneLookupResponse200OutputResultsItemType1")


@_attrs_define
class ReversePhoneLookupResponse200OutputResultsItemType1:
    """
    Attributes:
        type_ (ReversePhoneLookupResponse200OutputResultsItemType1Type):
        company (ReversePhoneLookupResponse200OutputResultsItemType1Company):
    """

    type_: ReversePhoneLookupResponse200OutputResultsItemType1Type
    company: ReversePhoneLookupResponse200OutputResultsItemType1Company
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        company = self.company.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "company": company,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reverse_phone_lookup_response_200_output_results_item_type_1_company import (
            ReversePhoneLookupResponse200OutputResultsItemType1Company,
        )

        d = dict(src_dict)
        type_ = ReversePhoneLookupResponse200OutputResultsItemType1Type(d.pop("type"))

        company = ReversePhoneLookupResponse200OutputResultsItemType1Company.from_dict(d.pop("company"))

        reverse_phone_lookup_response_200_output_results_item_type_1 = cls(
            type_=type_,
            company=company,
        )

        reverse_phone_lookup_response_200_output_results_item_type_1.additional_properties = d
        return reverse_phone_lookup_response_200_output_results_item_type_1

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
