from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlushieRunBody")


@_attrs_define
class SlushieRunBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        query (None | str | Unset): Natural language search query. Required on the first request. Ignored when pageToken
            is provided.
        page_size (int | Unset): Number of results per page (1-1000). Applied to whichever result type is returned.
            Default: 25.
        company_exclusion_list_i_ds (list[str] | None | Unset): IDs of exclusion lists to filter out companies. Applied
            when returning companies, or to narrow company-based profile filtering.
        people_exclusion_list_i_ds (list[str] | None | Unset): IDs of exclusion lists to filter out people.
        page_token (None | str | Unset): Pagination token from a previous response. Pass the value of nextPageToken from
            the prior response.
        get_detailed_education (bool | None | Unset): Whether to include deep details about each educational item, like
            the school's LinkedIn URL, website, location, etc. That'll be put in the detailedEducation array. This slows
            down the API call, so only enable this if you need it. Only applies when the result type is people; ignored for
            company results.
        get_detailed_work_experience (bool | None | Unset): Whether to include deep details about each work experience
            item, like the company's LinkedIn URL, website, location, etc. That'll be put in the detailedWorkExperience
            array. This slows down the API call, so only enable this if you need it. Only applies when the result type is
            people; ignored for company results.
    """

    api_key: str
    query: None | str | Unset = UNSET
    page_size: int | Unset = 25
    company_exclusion_list_i_ds: list[str] | None | Unset = UNSET
    people_exclusion_list_i_ds: list[str] | None | Unset = UNSET
    page_token: None | str | Unset = UNSET
    get_detailed_education: bool | None | Unset = UNSET
    get_detailed_work_experience: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        page_size = self.page_size

        company_exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.company_exclusion_list_i_ds, Unset):
            company_exclusion_list_i_ds = UNSET
        elif isinstance(self.company_exclusion_list_i_ds, list):
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        else:
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        people_exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.people_exclusion_list_i_ds, Unset):
            people_exclusion_list_i_ds = UNSET
        elif isinstance(self.people_exclusion_list_i_ds, list):
            people_exclusion_list_i_ds = self.people_exclusion_list_i_ds

        else:
            people_exclusion_list_i_ds = self.people_exclusion_list_i_ds

        page_token: None | str | Unset
        if isinstance(self.page_token, Unset):
            page_token = UNSET
        else:
            page_token = self.page_token

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
            }
        )
        if query is not UNSET:
            field_dict["query"] = query
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if company_exclusion_list_i_ds is not UNSET:
            field_dict["companyExclusionListIDs"] = company_exclusion_list_i_ds
        if people_exclusion_list_i_ds is not UNSET:
            field_dict["peopleExclusionListIDs"] = people_exclusion_list_i_ds
        if page_token is not UNSET:
            field_dict["pageToken"] = page_token
        if get_detailed_education is not UNSET:
            field_dict["getDetailedEducation"] = get_detailed_education
        if get_detailed_work_experience is not UNSET:
            field_dict["getDetailedWorkExperience"] = get_detailed_work_experience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        page_size = d.pop("pageSize", UNSET)

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

        def _parse_people_exclusion_list_i_ds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                people_exclusion_list_i_ds_type_0 = cast(list[str], data)

                return people_exclusion_list_i_ds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        people_exclusion_list_i_ds = _parse_people_exclusion_list_i_ds(d.pop("peopleExclusionListIDs", UNSET))

        def _parse_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_token = _parse_page_token(d.pop("pageToken", UNSET))

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

        slushie_run_body = cls(
            api_key=api_key,
            query=query,
            page_size=page_size,
            company_exclusion_list_i_ds=company_exclusion_list_i_ds,
            people_exclusion_list_i_ds=people_exclusion_list_i_ds,
            page_token=page_token,
            get_detailed_education=get_detailed_education,
            get_detailed_work_experience=get_detailed_work_experience,
        )

        slushie_run_body.additional_properties = d
        return slushie_run_body

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
