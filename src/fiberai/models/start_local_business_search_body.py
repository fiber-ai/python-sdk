from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.start_local_business_search_body_companies_item import StartLocalBusinessSearchBodyCompaniesItem
    from ..models.start_local_business_search_body_contact_preferences import (
        StartLocalBusinessSearchBodyContactPreferences,
    )


T = TypeVar("T", bound="StartLocalBusinessSearchBody")


@_attrs_define
class StartLocalBusinessSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        companies (list[StartLocalBusinessSearchBodyCompaniesItem]): The companies to search for.
        job_titles (list[str] | None | Unset): Job titles to search for at each company (e.g. ['CEO', 'Owner']). Omit or
            null to skip person search.
        strict_job_title_match (bool | Unset): If true, only match the same role with different wording (e.g. CEO =
            Chief Executive Officer). Rejects different roles even if senior/similar (e.g. CEO ≠ Chairman). Default: False.
        contact_preferences (StartLocalBusinessSearchBodyContactPreferences | Unset): Controls which contact data to
            fetch for all companies in this payload.
    """

    api_key: str
    companies: list[StartLocalBusinessSearchBodyCompaniesItem]
    job_titles: list[str] | None | Unset = UNSET
    strict_job_title_match: bool | Unset = False
    contact_preferences: StartLocalBusinessSearchBodyContactPreferences | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        job_titles: list[str] | None | Unset
        if isinstance(self.job_titles, Unset):
            job_titles = UNSET
        elif isinstance(self.job_titles, list):
            job_titles = self.job_titles

        else:
            job_titles = self.job_titles

        strict_job_title_match = self.strict_job_title_match

        contact_preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_preferences, Unset):
            contact_preferences = self.contact_preferences.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "companies": companies,
            }
        )
        if job_titles is not UNSET:
            field_dict["jobTitles"] = job_titles
        if strict_job_title_match is not UNSET:
            field_dict["strictJobTitleMatch"] = strict_job_title_match
        if contact_preferences is not UNSET:
            field_dict["contactPreferences"] = contact_preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_local_business_search_body_companies_item import StartLocalBusinessSearchBodyCompaniesItem
        from ..models.start_local_business_search_body_contact_preferences import (
            StartLocalBusinessSearchBodyContactPreferences,
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = StartLocalBusinessSearchBodyCompaniesItem.from_dict(companies_item_data)

            companies.append(companies_item)

        def _parse_job_titles(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_titles_type_0 = cast(list[str], data)

                return job_titles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        job_titles = _parse_job_titles(d.pop("jobTitles", UNSET))

        strict_job_title_match = d.pop("strictJobTitleMatch", UNSET)

        _contact_preferences = d.pop("contactPreferences", UNSET)
        contact_preferences: StartLocalBusinessSearchBodyContactPreferences | Unset
        if isinstance(_contact_preferences, Unset):
            contact_preferences = UNSET
        else:
            contact_preferences = StartLocalBusinessSearchBodyContactPreferences.from_dict(_contact_preferences)

        start_local_business_search_body = cls(
            api_key=api_key,
            companies=companies,
            job_titles=job_titles,
            strict_job_title_match=strict_job_title_match,
            contact_preferences=contact_preferences,
        )

        start_local_business_search_body.additional_properties = d
        return start_local_business_search_body

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
