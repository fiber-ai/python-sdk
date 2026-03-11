from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_0_type import (
    SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0Type,
)

if TYPE_CHECKING:
    from ..models.sync_combined_search_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_0_range import (
        SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0Range,
    )


T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0")


@_attrs_define
class SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0:
    """
    Attributes:
        type_ (SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0Type):
        range_ (SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0Range):
    """

    type_: SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0Type
    range_: SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0Range
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        range_ = self.range_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "range": range_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_0_range import (
            SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0Range,
        )

        d = dict(src_dict)
        type_ = SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0Type(d.pop("type"))

        range_ = SyncCombinedSearchBodyCompanyParamsOfficeLocationsV2Type0NoneOfType0ItemType0Range.from_dict(
            d.pop("range")
        )

        sync_combined_search_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_0 = cls(
            type_=type_,
            range_=range_,
        )

        sync_combined_search_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_0.additional_properties = d
        return sync_combined_search_body_company_params_office_locations_v2_type_0_none_of_type_0_item_type_0

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
