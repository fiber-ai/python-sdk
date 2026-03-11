from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_response_200_output_profiles_item_current_job_type_0_academic_qualification_type_0_item import (
    SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0AcademicQualificationType0Item,
)
from ..models.sync_combined_search_response_200_output_profiles_item_current_job_type_0_employment_type_type_0_item import (
    SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0EmploymentTypeType0Item,
)
from ..models.sync_combined_search_response_200_output_profiles_item_current_job_type_0_job_function_type_0_item import (
    SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0JobFunctionType0Item,
)
from ..models.sync_combined_search_response_200_output_profiles_item_current_job_type_0_seniority_type_1 import (
    SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType1,
)
from ..models.sync_combined_search_response_200_output_profiles_item_current_job_type_0_seniority_type_2_type_1 import (
    SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType2Type1,
)
from ..models.sync_combined_search_response_200_output_profiles_item_current_job_type_0_seniority_type_3_type_1 import (
    SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0")


@_attrs_define
class SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0:
    """
    Attributes:
        linkedin_company_id (None | str | Unset):
        is_current (bool | None | Unset):
        company_name (None | str | Unset):
        locality (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        summary (None | str | Unset):
        title (None | str | Unset):
        seniority (None | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType1 |
            SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType2Type1 |
            SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType3Type1 | Unset):
        job_function (list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0JobFunctionType0Item] | None |
            Unset):
        employment_type (list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0EmploymentTypeType0Item] |
            None | Unset):
        academic_qualification
            (list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0AcademicQualificationType0Item] | None |
            Unset):
        company_start_date (None | str | Unset):
        company_end_date (None | str | Unset):
    """

    linkedin_company_id: None | str | Unset = UNSET
    is_current: bool | None | Unset = UNSET
    company_name: None | str | Unset = UNSET
    locality: None | str | Unset = UNSET
    start_date: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    seniority: (
        None
        | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType1
        | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType2Type1
        | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType3Type1
        | Unset
    ) = UNSET
    job_function: (
        list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0JobFunctionType0Item] | None | Unset
    ) = UNSET
    employment_type: (
        list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0EmploymentTypeType0Item] | None | Unset
    ) = UNSET
    academic_qualification: (
        list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0AcademicQualificationType0Item]
        | None
        | Unset
    ) = UNSET
    company_start_date: None | str | Unset = UNSET
    company_end_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_company_id: None | str | Unset
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        is_current: bool | None | Unset
        if isinstance(self.is_current, Unset):
            is_current = UNSET
        else:
            is_current = self.is_current

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        locality: None | str | Unset
        if isinstance(self.locality, Unset):
            locality = UNSET
        else:
            locality = self.locality

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        seniority: None | str | Unset
        if isinstance(self.seniority, Unset):
            seniority = UNSET
        elif isinstance(self.seniority, SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType1):
            seniority = self.seniority.value
        elif isinstance(
            self.seniority, SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType2Type1
        ):
            seniority = self.seniority.value
        elif isinstance(
            self.seniority, SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType3Type1
        ):
            seniority = self.seniority.value
        else:
            seniority = self.seniority

        job_function: list[str] | None | Unset
        if isinstance(self.job_function, Unset):
            job_function = UNSET
        elif isinstance(self.job_function, list):
            job_function = []
            for job_function_type_0_item_data in self.job_function:
                job_function_type_0_item = job_function_type_0_item_data.value
                job_function.append(job_function_type_0_item)

        else:
            job_function = self.job_function

        employment_type: list[str] | None | Unset
        if isinstance(self.employment_type, Unset):
            employment_type = UNSET
        elif isinstance(self.employment_type, list):
            employment_type = []
            for employment_type_type_0_item_data in self.employment_type:
                employment_type_type_0_item = employment_type_type_0_item_data.value
                employment_type.append(employment_type_type_0_item)

        else:
            employment_type = self.employment_type

        academic_qualification: list[str] | None | Unset
        if isinstance(self.academic_qualification, Unset):
            academic_qualification = UNSET
        elif isinstance(self.academic_qualification, list):
            academic_qualification = []
            for academic_qualification_type_0_item_data in self.academic_qualification:
                academic_qualification_type_0_item = academic_qualification_type_0_item_data.value
                academic_qualification.append(academic_qualification_type_0_item)

        else:
            academic_qualification = self.academic_qualification

        company_start_date: None | str | Unset
        if isinstance(self.company_start_date, Unset):
            company_start_date = UNSET
        else:
            company_start_date = self.company_start_date

        company_end_date: None | str | Unset
        if isinstance(self.company_end_date, Unset):
            company_end_date = UNSET
        else:
            company_end_date = self.company_end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_company_id is not UNSET:
            field_dict["linkedin_company_id"] = linkedin_company_id
        if is_current is not UNSET:
            field_dict["is_current"] = is_current
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if locality is not UNSET:
            field_dict["locality"] = locality
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if seniority is not UNSET:
            field_dict["seniority"] = seniority
        if job_function is not UNSET:
            field_dict["job_function"] = job_function
        if employment_type is not UNSET:
            field_dict["employment_type"] = employment_type
        if academic_qualification is not UNSET:
            field_dict["academic_qualification"] = academic_qualification
        if company_start_date is not UNSET:
            field_dict["company_start_date"] = company_start_date
        if company_end_date is not UNSET:
            field_dict["company_end_date"] = company_end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_linkedin_company_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedin_company_id", UNSET))

        def _parse_is_current(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_current = _parse_is_current(d.pop("is_current", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_locality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locality = _parse_locality(d.pop("locality", UNSET))

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_seniority(
            data: object,
        ) -> (
            None
            | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType1
            | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType2Type1
            | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                seniority_type_1 = SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType1(data)

                return seniority_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                seniority_type_2_type_1 = (
                    SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType2Type1(data)
                )

                return seniority_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                seniority_type_3_type_1 = (
                    SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType3Type1(data)
                )

                return seniority_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType1
                | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType2Type1
                | SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0SeniorityType3Type1
                | Unset,
                data,
            )

        seniority = _parse_seniority(d.pop("seniority", UNSET))

        def _parse_job_function(
            data: object,
        ) -> list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0JobFunctionType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_function_type_0 = []
                _job_function_type_0 = data
                for job_function_type_0_item_data in _job_function_type_0:
                    job_function_type_0_item = (
                        SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0JobFunctionType0Item(
                            job_function_type_0_item_data
                        )
                    )

                    job_function_type_0.append(job_function_type_0_item)

                return job_function_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0JobFunctionType0Item] | None | Unset,
                data,
            )

        job_function = _parse_job_function(d.pop("job_function", UNSET))

        def _parse_employment_type(
            data: object,
        ) -> list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0EmploymentTypeType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                employment_type_type_0 = []
                _employment_type_type_0 = data
                for employment_type_type_0_item_data in _employment_type_type_0:
                    employment_type_type_0_item = (
                        SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0EmploymentTypeType0Item(
                            employment_type_type_0_item_data
                        )
                    )

                    employment_type_type_0.append(employment_type_type_0_item)

                return employment_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0EmploymentTypeType0Item]
                | None
                | Unset,
                data,
            )

        employment_type = _parse_employment_type(d.pop("employment_type", UNSET))

        def _parse_academic_qualification(
            data: object,
        ) -> (
            list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0AcademicQualificationType0Item]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                academic_qualification_type_0 = []
                _academic_qualification_type_0 = data
                for academic_qualification_type_0_item_data in _academic_qualification_type_0:
                    academic_qualification_type_0_item = (
                        SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0AcademicQualificationType0Item(
                            academic_qualification_type_0_item_data
                        )
                    )

                    academic_qualification_type_0.append(academic_qualification_type_0_item)

                return academic_qualification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SyncCombinedSearchResponse200OutputProfilesItemCurrentJobType0AcademicQualificationType0Item]
                | None
                | Unset,
                data,
            )

        academic_qualification = _parse_academic_qualification(d.pop("academic_qualification", UNSET))

        def _parse_company_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_start_date = _parse_company_start_date(d.pop("company_start_date", UNSET))

        def _parse_company_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_end_date = _parse_company_end_date(d.pop("company_end_date", UNSET))

        sync_combined_search_response_200_output_profiles_item_current_job_type_0 = cls(
            linkedin_company_id=linkedin_company_id,
            is_current=is_current,
            company_name=company_name,
            locality=locality,
            start_date=start_date,
            end_date=end_date,
            summary=summary,
            title=title,
            seniority=seniority,
            job_function=job_function,
            employment_type=employment_type,
            academic_qualification=academic_qualification,
            company_start_date=company_start_date,
            company_end_date=company_end_date,
        )

        sync_combined_search_response_200_output_profiles_item_current_job_type_0.additional_properties = d
        return sync_combined_search_response_200_output_profiles_item_current_job_type_0

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
