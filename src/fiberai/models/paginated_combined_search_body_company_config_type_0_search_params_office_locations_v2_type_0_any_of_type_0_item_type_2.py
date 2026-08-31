from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_type import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2Type,
)

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_1 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_3 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3,
    )


T = TypeVar(
    "T", bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2"
)


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2:
    """
    Attributes:
        type_ (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2Type):
        location
            (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0
            |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1
            |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType
            3):
    """

    type_: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2Type
    location: (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2,  # noqa: PLC0415
        )

        type_ = self.type_.value

        location: dict[str, Any]
        if isinstance(
            self.location,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0,
        ):
            location = self.location.to_dict()
        elif isinstance(
            self.location,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1,
        ):
            location = self.location.to_dict()
        elif isinstance(
            self.location,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2,
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
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_2 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2_location_type_3 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2Type(
            d.pop("type")
        )

        def _parse_location(
            data: object,
        ) -> (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType0.from_dict(
                    data
                )

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_1 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType1.from_dict(
                    data
                )

                return location_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_2 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType2.from_dict(
                    data
                )

                return location_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            location_type_3 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsOfficeLocationsV2Type0AnyOfType0ItemType2LocationType3.from_dict(
                data
            )

            return location_type_3

        location = _parse_location(d.pop("location"))

        paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2 = cls(
            type_=type_,
            location=location,
        )

        paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_office_locations_v2_type_0_any_of_type_0_item_type_2

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
