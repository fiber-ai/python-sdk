from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_people_item_start_date_precision_type_1 import (
    CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType1,
)
from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_people_item_start_date_precision_type_2_type_1 import (
    CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType2Type1,
)
from ..models.company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_people_item_start_date_precision_type_3_type_1 import (
    CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItem")


@_attrs_define
class CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItem:
    """A person who satisfied an employees rule.

    Attributes:
        linkedin_url (None | str | Unset): LinkedIn profile URL of the person.
        name (None | str | Unset): Full name of the person.
        title (None | str | Unset): Title of the person's matching role at this company.
        start_date (None | str | Unset): When the person's matching role at this company started.
        start_date_precision
            (CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType1 |
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType2Type1 |
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType3Type1 |
            None | Unset): How precise `start_date` is. "month" means the month and year are known. "year" means only the
            year is known, so `start_date` is set to January 1 of that year. Null if unknown.
    """

    linkedin_url: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    start_date: None | str | Unset = UNSET
    start_date_precision: (
        CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType1
        | CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType2Type1
        | CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        start_date_precision: None | str | Unset
        if isinstance(self.start_date_precision, Unset):
            start_date_precision = UNSET
        elif isinstance(
            self.start_date_precision,
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType1,
        ):
            start_date_precision = self.start_date_precision.value
        elif isinstance(
            self.start_date_precision,
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType2Type1,
        ):
            start_date_precision = self.start_date_precision.value
        elif isinstance(
            self.start_date_precision,
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType3Type1,
        ):
            start_date_precision = self.start_date_precision.value
        else:
            start_date_precision = self.start_date_precision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_url is not UNSET:
            field_dict["linkedin_url"] = linkedin_url
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if start_date_precision is not UNSET:
            field_dict["start_date_precision"] = start_date_precision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedin_url", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_start_date_precision(
            data: object,
        ) -> (
            CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType1
            | CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType2Type1
            | CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType3Type1
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
                start_date_precision_type_1 = CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType1(
                    data
                )

                return start_date_precision_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_precision_type_2_type_1 = CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType2Type1(
                    data
                )

                return start_date_precision_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_precision_type_3_type_1 = CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType3Type1(
                    data
                )

                return start_date_precision_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType1
                | CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType2Type1
                | CompanySearchResponse200OutputDataItemMatchesType0EmployeeRulesType0ItemPeopleItemStartDatePrecisionType3Type1
                | None
                | Unset,
                data,
            )

        start_date_precision = _parse_start_date_precision(d.pop("start_date_precision", UNSET))

        company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_people_item = cls(
            linkedin_url=linkedin_url,
            name=name,
            title=title,
            start_date=start_date,
            start_date_precision=start_date_precision,
        )

        company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_people_item.additional_properties = d
        return company_search_response_200_output_data_item_matches_type_0_employee_rules_type_0_item_people_item

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
