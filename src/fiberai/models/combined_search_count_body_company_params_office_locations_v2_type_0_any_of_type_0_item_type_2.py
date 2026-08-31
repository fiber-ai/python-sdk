from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_type import (
    CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2Type,
)

if TYPE_CHECKING:
    from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_0 import (
        CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0,
    )
    from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_1 import (
        CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1,
    )
    from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2 import (
        CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2,
    )
    from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_3 import (
        CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3,
    )


T = TypeVar("T", bound="CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2")


@_attrs_define
class CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2:
    """
    Attributes:
        type_ (CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2Type):
        location (CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0 |
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1 |
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2 |
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3):
    """

    type_: CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2Type
    location: (
        CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0
        | CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1
        | CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2
        | CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_0 import (
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0,  # noqa: PLC0415
        )
        from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_1 import (
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1,  # noqa: PLC0415
        )
        from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2 import (
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2,  # noqa: PLC0415
        )

        type_ = self.type_.value

        location: dict[str, Any]
        if isinstance(
            self.location, CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0
        ):
            location = self.location.to_dict()
        elif isinstance(
            self.location, CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1
        ):
            location = self.location.to_dict()
        elif isinstance(
            self.location, CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2
        ):
            location = self.location.to_dict()
        else:
            location = self.location.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "location": location,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_0 import (
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0,  # noqa: PLC0415
        )
        from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_1 import (
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1,  # noqa: PLC0415
        )
        from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2 import (
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2,  # noqa: PLC0415
        )
        from ..models.combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_3 import (
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2Type(d.pop("type"))

        def _parse_location(
            data: object,
        ) -> (
            CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0
            | CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1
            | CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2
            | CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0.from_dict(
                    data
                )

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_1 = CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1.from_dict(
                    data
                )

                return location_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_2 = CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2.from_dict(
                    data
                )

                return location_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            location_type_3 = (
                CombinedSearchCountBodyCompanyParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3.from_dict(
                    data
                )
            )

            return location_type_3

        location = _parse_location(d.pop("location"))

        combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2 = cls(
            type_=type_,
            location=location,
        )

        combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2.additional_properties = d
        return combined_search_count_body_company_params_office_locations_v2_type_0_any_of_type_0_item_type_2

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
