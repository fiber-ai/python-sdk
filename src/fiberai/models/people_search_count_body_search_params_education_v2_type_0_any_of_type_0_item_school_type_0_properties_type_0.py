from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_school_type_0_properties_type_0_country_type_0 import (
        PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0CountryType0,
    )


T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0")


@_attrs_define
class PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0:
    """
    Attributes:
        country (None |
            PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0CountryType0 | Unset):
    """

    country: (
        None
        | PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0CountryType0
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_school_type_0_properties_type_0_country_type_0 import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0CountryType0,
        )

        country: dict[str, Any] | None | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(
            self.country,
            PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0CountryType0,
        ):
            country = self.country.to_dict()
        else:
            country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_school_type_0_properties_type_0_country_type_0 import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0CountryType0,
        )

        d = dict(src_dict)

        def _parse_country(
            data: object,
        ) -> (
            None
            | PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0CountryType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_type_0 = PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0CountryType0.from_dict(
                    data
                )

                return country_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemSchoolType0PropertiesType0CountryType0
                | Unset,
                data,
            )

        country = _parse_country(d.pop("country", UNSET))

        people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_school_type_0_properties_type_0 = cls(
            country=country,
        )

        people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_school_type_0_properties_type_0.additional_properties = d
        return people_search_count_body_search_params_education_v2_type_0_any_of_type_0_item_school_type_0_properties_type_0

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
