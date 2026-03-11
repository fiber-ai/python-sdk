from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextToCombinedSearchBody")


@_attrs_define
class TextToCombinedSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        query (str): Describe what you’re looking for — for example: I want Senior Product Managers from Series A to C
            FinTech startups located in New York.
        profile_item_limit (float): The number of profiles to return.
        company_item_limit (float | None | Unset): The number of companies to return. If not provided, no companies will
            be returned. But, regardless of the value you give here, we'll find all prospects (based on the query) who work
            at companies that satisfy the companyParams.
        company_exclusion_list_i_ds (list[str] | None | Unset): Filter out companies which belong to the given company
            exclusion lists. You can create company exclusion lists via our API
        prospect_exclusion_list_i_ds (list[str] | None | Unset): Filter out people which belong to the given prospect
            exclusion lists. You can create prospect exclusion lists via our API
        get_detailed_education (bool | None | Unset): Whether to include deep details about each educational item, like
            the school's LinkedIn URL, website, location, etc. That'll be put in the detailedEducation array. This slows
            down the API call, so only enable this if you need it. Default: False.
        get_detailed_work_experience (bool | None | Unset): Whether to include deep details about each work experience
            item, like the company's LinkedIn URL, website, location, etc. That'll be put in the detailedWorkExperience
            array. This slows down the API call, so only enable this if you need it. Default: False.
    """

    api_key: str
    query: str
    profile_item_limit: float
    company_item_limit: float | None | Unset = UNSET
    company_exclusion_list_i_ds: list[str] | None | Unset = UNSET
    prospect_exclusion_list_i_ds: list[str] | None | Unset = UNSET
    get_detailed_education: bool | None | Unset = False
    get_detailed_work_experience: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        query = self.query

        profile_item_limit = self.profile_item_limit

        company_item_limit: float | None | Unset
        if isinstance(self.company_item_limit, Unset):
            company_item_limit = UNSET
        else:
            company_item_limit = self.company_item_limit

        company_exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.company_exclusion_list_i_ds, Unset):
            company_exclusion_list_i_ds = UNSET
        elif isinstance(self.company_exclusion_list_i_ds, list):
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        else:
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        prospect_exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.prospect_exclusion_list_i_ds, Unset):
            prospect_exclusion_list_i_ds = UNSET
        elif isinstance(self.prospect_exclusion_list_i_ds, list):
            prospect_exclusion_list_i_ds = self.prospect_exclusion_list_i_ds

        else:
            prospect_exclusion_list_i_ds = self.prospect_exclusion_list_i_ds

        get_detailed_education: bool | None | Unset
        if isinstance(self.get_detailed_education, Unset):
            get_detailed_education = UNSET
        else:
            get_detailed_education = self.get_detailed_education

        get_detailed_work_experience: bool | None | Unset
        if isinstance(self.get_detailed_work_experience, Unset):
            get_detailed_work_experience = UNSET
        else:
            get_detailed_work_experience = self.get_detailed_work_experience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "query": query,
                "profileItemLimit": profile_item_limit,
            }
        )
        if company_item_limit is not UNSET:
            field_dict["companyItemLimit"] = company_item_limit
        if company_exclusion_list_i_ds is not UNSET:
            field_dict["companyExclusionListIDs"] = company_exclusion_list_i_ds
        if prospect_exclusion_list_i_ds is not UNSET:
            field_dict["prospectExclusionListIDs"] = prospect_exclusion_list_i_ds
        if get_detailed_education is not UNSET:
            field_dict["getDetailedEducation"] = get_detailed_education
        if get_detailed_work_experience is not UNSET:
            field_dict["getDetailedWorkExperience"] = get_detailed_work_experience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        query = d.pop("query")

        profile_item_limit = d.pop("profileItemLimit")

        def _parse_company_item_limit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        company_item_limit = _parse_company_item_limit(d.pop("companyItemLimit", UNSET))

        def _parse_company_exclusion_list_i_ds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                company_exclusion_list_i_ds_type_0 = cast(list[str], data)

                return company_exclusion_list_i_ds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        company_exclusion_list_i_ds = _parse_company_exclusion_list_i_ds(d.pop("companyExclusionListIDs", UNSET))

        def _parse_prospect_exclusion_list_i_ds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prospect_exclusion_list_i_ds_type_0 = cast(list[str], data)

                return prospect_exclusion_list_i_ds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        prospect_exclusion_list_i_ds = _parse_prospect_exclusion_list_i_ds(d.pop("prospectExclusionListIDs", UNSET))

        def _parse_get_detailed_education(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_education = _parse_get_detailed_education(d.pop("getDetailedEducation", UNSET))

        def _parse_get_detailed_work_experience(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_work_experience = _parse_get_detailed_work_experience(d.pop("getDetailedWorkExperience", UNSET))

        text_to_combined_search_body = cls(
            api_key=api_key,
            query=query,
            profile_item_limit=profile_item_limit,
            company_item_limit=company_item_limit,
            company_exclusion_list_i_ds=company_exclusion_list_i_ds,
            prospect_exclusion_list_i_ds=prospect_exclusion_list_i_ds,
            get_detailed_education=get_detailed_education,
            get_detailed_work_experience=get_detailed_work_experience,
        )

        text_to_combined_search_body.additional_properties = d
        return text_to_combined_search_body

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
