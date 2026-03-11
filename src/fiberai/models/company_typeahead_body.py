from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_typeahead_body_org_type_type_1 import CompanyTypeaheadBodyOrgTypeType1
from ..models.company_typeahead_body_org_type_type_2_type_1 import CompanyTypeaheadBodyOrgTypeType2Type1
from ..models.company_typeahead_body_org_type_type_3_type_1 import CompanyTypeaheadBodyOrgTypeType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyTypeaheadBody")


@_attrs_define
class CompanyTypeaheadBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        starts_with (str):
        org_type (CompanyTypeaheadBodyOrgTypeType1 | CompanyTypeaheadBodyOrgTypeType2Type1 |
            CompanyTypeaheadBodyOrgTypeType3Type1 | None | Unset): The input schema for the typeahead. Keep orgType as
            investor, school or null if not sure
    """

    api_key: str
    starts_with: str
    org_type: (
        CompanyTypeaheadBodyOrgTypeType1
        | CompanyTypeaheadBodyOrgTypeType2Type1
        | CompanyTypeaheadBodyOrgTypeType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        starts_with = self.starts_with

        org_type: None | str | Unset
        if isinstance(self.org_type, Unset):
            org_type = UNSET
        elif isinstance(self.org_type, CompanyTypeaheadBodyOrgTypeType1):
            org_type = self.org_type.value
        elif isinstance(self.org_type, CompanyTypeaheadBodyOrgTypeType2Type1):
            org_type = self.org_type.value
        elif isinstance(self.org_type, CompanyTypeaheadBodyOrgTypeType3Type1):
            org_type = self.org_type.value
        else:
            org_type = self.org_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "startsWith": starts_with,
            }
        )
        if org_type is not UNSET:
            field_dict["orgType"] = org_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        starts_with = d.pop("startsWith")

        def _parse_org_type(
            data: object,
        ) -> (
            CompanyTypeaheadBodyOrgTypeType1
            | CompanyTypeaheadBodyOrgTypeType2Type1
            | CompanyTypeaheadBodyOrgTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_type_type_1 = CompanyTypeaheadBodyOrgTypeType1(data)

                return org_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_type_type_2_type_1 = CompanyTypeaheadBodyOrgTypeType2Type1(data)

                return org_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_type_type_3_type_1 = CompanyTypeaheadBodyOrgTypeType3Type1(data)

                return org_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanyTypeaheadBodyOrgTypeType1
                | CompanyTypeaheadBodyOrgTypeType2Type1
                | CompanyTypeaheadBodyOrgTypeType3Type1
                | None
                | Unset,
                data,
            )

        org_type = _parse_org_type(d.pop("orgType", UNSET))

        company_typeahead_body = cls(
            api_key=api_key,
            starts_with=starts_with,
            org_type=org_type,
        )

        company_typeahead_body.additional_properties = d
        return company_typeahead_body

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
