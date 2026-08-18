from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialInstrumentLookupResponse200OutputCompanyInfoType0")


@_attrs_define
class FinancialInstrumentLookupResponse200OutputCompanyInfoType0:
    """Company information when available — description, leadership, sector, headquarters, etc.

    Attributes:
        description (None | str | Unset): Short company or fund description.
        description_url (None | str | Unset): URL for the full company description.
        ceo_name (None | str | Unset): Chief executive officer name.
        employee_count (int | None | Unset): Number of employees.
        founded_date (None | str | Unset): ISO 8601 founding date: full 'YYYY-MM-DD' when the day is known, otherwise
            just 'YYYY'.
        headquarters (None | str | Unset): Headquarters location.
        sector (None | str | Unset): Sector or industry classification.
        website_url (None | str | Unset): Company website URL.
    """

    description: None | str | Unset = UNSET
    description_url: None | str | Unset = UNSET
    ceo_name: None | str | Unset = UNSET
    employee_count: int | None | Unset = UNSET
    founded_date: None | str | Unset = UNSET
    headquarters: None | str | Unset = UNSET
    sector: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        description_url: None | str | Unset
        if isinstance(self.description_url, Unset):
            description_url = UNSET
        else:
            description_url = self.description_url

        ceo_name: None | str | Unset
        if isinstance(self.ceo_name, Unset):
            ceo_name = UNSET
        else:
            ceo_name = self.ceo_name

        employee_count: int | None | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        founded_date: None | str | Unset
        if isinstance(self.founded_date, Unset):
            founded_date = UNSET
        else:
            founded_date = self.founded_date

        headquarters: None | str | Unset
        if isinstance(self.headquarters, Unset):
            headquarters = UNSET
        else:
            headquarters = self.headquarters

        sector: None | str | Unset
        if isinstance(self.sector, Unset):
            sector = UNSET
        else:
            sector = self.sector

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if description_url is not UNSET:
            field_dict["descriptionUrl"] = description_url
        if ceo_name is not UNSET:
            field_dict["ceoName"] = ceo_name
        if employee_count is not UNSET:
            field_dict["employeeCount"] = employee_count
        if founded_date is not UNSET:
            field_dict["foundedDate"] = founded_date
        if headquarters is not UNSET:
            field_dict["headquarters"] = headquarters
        if sector is not UNSET:
            field_dict["sector"] = sector
        if website_url is not UNSET:
            field_dict["websiteUrl"] = website_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_description_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description_url = _parse_description_url(d.pop("descriptionUrl", UNSET))

        def _parse_ceo_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ceo_name = _parse_ceo_name(d.pop("ceoName", UNSET))

        def _parse_employee_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        employee_count = _parse_employee_count(d.pop("employeeCount", UNSET))

        def _parse_founded_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        founded_date = _parse_founded_date(d.pop("foundedDate", UNSET))

        def _parse_headquarters(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headquarters = _parse_headquarters(d.pop("headquarters", UNSET))

        def _parse_sector(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sector = _parse_sector(d.pop("sector", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("websiteUrl", UNSET))

        financial_instrument_lookup_response_200_output_company_info_type_0 = cls(
            description=description,
            description_url=description_url,
            ceo_name=ceo_name,
            employee_count=employee_count,
            founded_date=founded_date,
            headquarters=headquarters,
            sector=sector,
            website_url=website_url,
        )

        financial_instrument_lookup_response_200_output_company_info_type_0.additional_properties = d
        return financial_instrument_lookup_response_200_output_company_info_type_0

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
