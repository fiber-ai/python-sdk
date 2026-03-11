from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.remove_company_from_exclusion_list_body_excluded_company_details import (
        RemoveCompanyFromExclusionListBodyExcludedCompanyDetails,
    )


T = TypeVar("T", bound="RemoveCompanyFromExclusionListBody")


@_attrs_define
class RemoveCompanyFromExclusionListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        list_id (str): Id of the company exclusion lists to remove the company from
        excluded_company_details (RemoveCompanyFromExclusionListBodyExcludedCompanyDetails): Details of the companies to
            remove from the exclusion list
    """

    api_key: str
    list_id: str
    excluded_company_details: RemoveCompanyFromExclusionListBodyExcludedCompanyDetails
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        list_id = self.list_id

        excluded_company_details = self.excluded_company_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "listId": list_id,
                "excludedCompanyDetails": excluded_company_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remove_company_from_exclusion_list_body_excluded_company_details import (
            RemoveCompanyFromExclusionListBodyExcludedCompanyDetails,
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        list_id = d.pop("listId")

        excluded_company_details = RemoveCompanyFromExclusionListBodyExcludedCompanyDetails.from_dict(
            d.pop("excludedCompanyDetails")
        )

        remove_company_from_exclusion_list_body = cls(
            api_key=api_key,
            list_id=list_id,
            excluded_company_details=excluded_company_details,
        )

        remove_company_from_exclusion_list_body.additional_properties = d
        return remove_company_from_exclusion_list_body

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
