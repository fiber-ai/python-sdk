from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_saved_search_run_companies_response_200_output_companies_item_movement_type import (
    GetSavedSearchRunCompaniesResponse200OutputCompaniesItemMovementType,
)

if TYPE_CHECKING:
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompany,
    )


T = TypeVar("T", bound="GetSavedSearchRunCompaniesResponse200OutputCompaniesItem")


@_attrs_define
class GetSavedSearchRunCompaniesResponse200OutputCompaniesItem:
    """
    Attributes:
        company (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompany):
        movement_type (GetSavedSearchRunCompaniesResponse200OutputCompaniesItemMovementType):
    """

    company: GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompany
    movement_type: GetSavedSearchRunCompaniesResponse200OutputCompaniesItemMovementType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company.to_dict()

        movement_type = self.movement_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
                "movementType": movement_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompany,
        )

        d = dict(src_dict)
        company = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompany.from_dict(d.pop("company"))

        movement_type = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemMovementType(d.pop("movementType"))

        get_saved_search_run_companies_response_200_output_companies_item = cls(
            company=company,
            movement_type=movement_type,
        )

        get_saved_search_run_companies_response_200_output_companies_item.additional_properties = d
        return get_saved_search_run_companies_response_200_output_companies_item

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
