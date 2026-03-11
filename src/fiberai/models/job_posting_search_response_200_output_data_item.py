from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_posting_search_response_200_output_data_item_job_function_type_0_item import (
    JobPostingSearchResponse200OutputDataItemJobFunctionType0Item,
)
from ..models.job_posting_search_response_200_output_data_item_job_location_type_type_1 import (
    JobPostingSearchResponse200OutputDataItemJobLocationTypeType1,
)
from ..models.job_posting_search_response_200_output_data_item_job_location_type_type_2_type_1 import (
    JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1,
)
from ..models.job_posting_search_response_200_output_data_item_job_location_type_type_3_type_1 import (
    JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1,
)
from ..models.job_posting_search_response_200_output_data_item_standard_industries_type_0_item import (
    JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item,
)
from ..models.job_posting_search_response_200_output_data_item_status import (
    JobPostingSearchResponse200OutputDataItemStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_posting_search_response_200_output_data_item_annual_salary_usd_type_0 import (
        JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0,
    )
    from ..models.job_posting_search_response_200_output_data_item_applicant_range_type_0 import (
        JobPostingSearchResponse200OutputDataItemApplicantRangeType0,
    )
    from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0 import (
        JobPostingSearchResponse200OutputDataItemCompensationRangeType0,
    )
    from ..models.job_posting_search_response_200_output_data_item_standardized_location_type_0 import (
        JobPostingSearchResponse200OutputDataItemStandardizedLocationType0,
    )
    from ..models.job_posting_search_response_200_output_data_item_years_of_experience_type_0 import (
        JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0,
    )


T = TypeVar("T", bound="JobPostingSearchResponse200OutputDataItem")


@_attrs_define
class JobPostingSearchResponse200OutputDataItem:
    """
    Attributes:
        job_id (str): Unique job identifier
        status (JobPostingSearchResponse200OutputDataItemStatus): Job status
        title (None | str | Unset): Job title/position
        company_name (None | str | Unset): Company name
        company_logo_url (None | str | Unset): Company logo URL
        posted_at (None | str | Unset): When the job was posted
        job_url (None | str | Unset): LinkedIn job URL
        applicant_range (JobPostingSearchResponse200OutputDataItemApplicantRangeType0 | None | Unset): Applicant count
            range
        description (None | str | Unset): Job description text
        seniority_level (None | str | Unset): Seniority level (e.g., 'Entry level', 'Senior level')
        employment_type (None | str | Unset): Employment type (e.g., 'Full-time', 'Part-time')
        job_function (list[JobPostingSearchResponse200OutputDataItemJobFunctionType0Item] | None | Unset): Job function
            categories
        raw_industries (None | str | Unset): Raw industries string from LinkedIn
        standard_industries (list[JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item] | None | Unset):
            Standardized industry categories
        compensation_range (JobPostingSearchResponse200OutputDataItemCompensationRangeType0 | None | Unset): Structured
            compensation range with currency and period
        annual_salary_usd (JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0 | None | Unset): Annual salary
            approximation in USD
        years_of_experience (JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0 | None | Unset): Years of
            experience required
        standardized_location (JobPostingSearchResponse200OutputDataItemStandardizedLocationType0 | None | Unset):
            Standardized location with geo data including lat/lon
        job_location_type (JobPostingSearchResponse200OutputDataItemJobLocationTypeType1 |
            JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1 |
            JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1 | None | Unset): Work location type
    """

    job_id: str
    status: JobPostingSearchResponse200OutputDataItemStatus
    title: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    company_logo_url: None | str | Unset = UNSET
    posted_at: None | str | Unset = UNSET
    job_url: None | str | Unset = UNSET
    applicant_range: JobPostingSearchResponse200OutputDataItemApplicantRangeType0 | None | Unset = UNSET
    description: None | str | Unset = UNSET
    seniority_level: None | str | Unset = UNSET
    employment_type: None | str | Unset = UNSET
    job_function: list[JobPostingSearchResponse200OutputDataItemJobFunctionType0Item] | None | Unset = UNSET
    raw_industries: None | str | Unset = UNSET
    standard_industries: list[JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item] | None | Unset = (
        UNSET
    )
    compensation_range: JobPostingSearchResponse200OutputDataItemCompensationRangeType0 | None | Unset = UNSET
    annual_salary_usd: JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0 | None | Unset = UNSET
    years_of_experience: JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0 | None | Unset = UNSET
    standardized_location: JobPostingSearchResponse200OutputDataItemStandardizedLocationType0 | None | Unset = UNSET
    job_location_type: (
        JobPostingSearchResponse200OutputDataItemJobLocationTypeType1
        | JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1
        | JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.job_posting_search_response_200_output_data_item_annual_salary_usd_type_0 import (
            JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0,
        )
        from ..models.job_posting_search_response_200_output_data_item_applicant_range_type_0 import (
            JobPostingSearchResponse200OutputDataItemApplicantRangeType0,
        )
        from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0 import (
            JobPostingSearchResponse200OutputDataItemCompensationRangeType0,
        )
        from ..models.job_posting_search_response_200_output_data_item_standardized_location_type_0 import (
            JobPostingSearchResponse200OutputDataItemStandardizedLocationType0,
        )
        from ..models.job_posting_search_response_200_output_data_item_years_of_experience_type_0 import (
            JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0,
        )

        job_id = self.job_id

        status = self.status.value

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_logo_url: None | str | Unset
        if isinstance(self.company_logo_url, Unset):
            company_logo_url = UNSET
        else:
            company_logo_url = self.company_logo_url

        posted_at: None | str | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        else:
            posted_at = self.posted_at

        job_url: None | str | Unset
        if isinstance(self.job_url, Unset):
            job_url = UNSET
        else:
            job_url = self.job_url

        applicant_range: dict[str, Any] | None | Unset
        if isinstance(self.applicant_range, Unset):
            applicant_range = UNSET
        elif isinstance(self.applicant_range, JobPostingSearchResponse200OutputDataItemApplicantRangeType0):
            applicant_range = self.applicant_range.to_dict()
        else:
            applicant_range = self.applicant_range

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        seniority_level: None | str | Unset
        if isinstance(self.seniority_level, Unset):
            seniority_level = UNSET
        else:
            seniority_level = self.seniority_level

        employment_type: None | str | Unset
        if isinstance(self.employment_type, Unset):
            employment_type = UNSET
        else:
            employment_type = self.employment_type

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

        raw_industries: None | str | Unset
        if isinstance(self.raw_industries, Unset):
            raw_industries = UNSET
        else:
            raw_industries = self.raw_industries

        standard_industries: list[str] | None | Unset
        if isinstance(self.standard_industries, Unset):
            standard_industries = UNSET
        elif isinstance(self.standard_industries, list):
            standard_industries = []
            for standard_industries_type_0_item_data in self.standard_industries:
                standard_industries_type_0_item = standard_industries_type_0_item_data.value
                standard_industries.append(standard_industries_type_0_item)

        else:
            standard_industries = self.standard_industries

        compensation_range: dict[str, Any] | None | Unset
        if isinstance(self.compensation_range, Unset):
            compensation_range = UNSET
        elif isinstance(self.compensation_range, JobPostingSearchResponse200OutputDataItemCompensationRangeType0):
            compensation_range = self.compensation_range.to_dict()
        else:
            compensation_range = self.compensation_range

        annual_salary_usd: dict[str, Any] | None | Unset
        if isinstance(self.annual_salary_usd, Unset):
            annual_salary_usd = UNSET
        elif isinstance(self.annual_salary_usd, JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0):
            annual_salary_usd = self.annual_salary_usd.to_dict()
        else:
            annual_salary_usd = self.annual_salary_usd

        years_of_experience: dict[str, Any] | None | Unset
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(self.years_of_experience, JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        standardized_location: dict[str, Any] | None | Unset
        if isinstance(self.standardized_location, Unset):
            standardized_location = UNSET
        elif isinstance(self.standardized_location, JobPostingSearchResponse200OutputDataItemStandardizedLocationType0):
            standardized_location = self.standardized_location.to_dict()
        else:
            standardized_location = self.standardized_location

        job_location_type: None | str | Unset
        if isinstance(self.job_location_type, Unset):
            job_location_type = UNSET
        elif isinstance(self.job_location_type, JobPostingSearchResponse200OutputDataItemJobLocationTypeType1):
            job_location_type = self.job_location_type.value
        elif isinstance(self.job_location_type, JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1):
            job_location_type = self.job_location_type.value
        elif isinstance(self.job_location_type, JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1):
            job_location_type = self.job_location_type.value
        else:
            job_location_type = self.job_location_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "status": status,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_logo_url is not UNSET:
            field_dict["company_logo_url"] = company_logo_url
        if posted_at is not UNSET:
            field_dict["posted_at"] = posted_at
        if job_url is not UNSET:
            field_dict["job_url"] = job_url
        if applicant_range is not UNSET:
            field_dict["applicant_range"] = applicant_range
        if description is not UNSET:
            field_dict["description"] = description
        if seniority_level is not UNSET:
            field_dict["seniority_level"] = seniority_level
        if employment_type is not UNSET:
            field_dict["employment_type"] = employment_type
        if job_function is not UNSET:
            field_dict["job_function"] = job_function
        if raw_industries is not UNSET:
            field_dict["raw_industries"] = raw_industries
        if standard_industries is not UNSET:
            field_dict["standard_industries"] = standard_industries
        if compensation_range is not UNSET:
            field_dict["compensation_range"] = compensation_range
        if annual_salary_usd is not UNSET:
            field_dict["annual_salary_usd"] = annual_salary_usd
        if years_of_experience is not UNSET:
            field_dict["years_of_experience"] = years_of_experience
        if standardized_location is not UNSET:
            field_dict["standardized_location"] = standardized_location
        if job_location_type is not UNSET:
            field_dict["job_location_type"] = job_location_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_posting_search_response_200_output_data_item_annual_salary_usd_type_0 import (
            JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0,
        )
        from ..models.job_posting_search_response_200_output_data_item_applicant_range_type_0 import (
            JobPostingSearchResponse200OutputDataItemApplicantRangeType0,
        )
        from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0 import (
            JobPostingSearchResponse200OutputDataItemCompensationRangeType0,
        )
        from ..models.job_posting_search_response_200_output_data_item_standardized_location_type_0 import (
            JobPostingSearchResponse200OutputDataItemStandardizedLocationType0,
        )
        from ..models.job_posting_search_response_200_output_data_item_years_of_experience_type_0 import (
            JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0,
        )

        d = dict(src_dict)
        job_id = d.pop("job_id")

        status = JobPostingSearchResponse200OutputDataItemStatus(d.pop("status"))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_company_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_logo_url = _parse_company_logo_url(d.pop("company_logo_url", UNSET))

        def _parse_posted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        posted_at = _parse_posted_at(d.pop("posted_at", UNSET))

        def _parse_job_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_url = _parse_job_url(d.pop("job_url", UNSET))

        def _parse_applicant_range(
            data: object,
        ) -> JobPostingSearchResponse200OutputDataItemApplicantRangeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                applicant_range_type_0 = JobPostingSearchResponse200OutputDataItemApplicantRangeType0.from_dict(data)

                return applicant_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobPostingSearchResponse200OutputDataItemApplicantRangeType0 | None | Unset, data)

        applicant_range = _parse_applicant_range(d.pop("applicant_range", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_seniority_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seniority_level = _parse_seniority_level(d.pop("seniority_level", UNSET))

        def _parse_employment_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employment_type = _parse_employment_type(d.pop("employment_type", UNSET))

        def _parse_job_function(
            data: object,
        ) -> list[JobPostingSearchResponse200OutputDataItemJobFunctionType0Item] | None | Unset:
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
                    job_function_type_0_item = JobPostingSearchResponse200OutputDataItemJobFunctionType0Item(
                        job_function_type_0_item_data
                    )

                    job_function_type_0.append(job_function_type_0_item)

                return job_function_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobPostingSearchResponse200OutputDataItemJobFunctionType0Item] | None | Unset, data)

        job_function = _parse_job_function(d.pop("job_function", UNSET))

        def _parse_raw_industries(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        raw_industries = _parse_raw_industries(d.pop("raw_industries", UNSET))

        def _parse_standard_industries(
            data: object,
        ) -> list[JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                standard_industries_type_0 = []
                _standard_industries_type_0 = data
                for standard_industries_type_0_item_data in _standard_industries_type_0:
                    standard_industries_type_0_item = (
                        JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item(
                            standard_industries_type_0_item_data
                        )
                    )

                    standard_industries_type_0.append(standard_industries_type_0_item)

                return standard_industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobPostingSearchResponse200OutputDataItemStandardIndustriesType0Item] | None | Unset, data)

        standard_industries = _parse_standard_industries(d.pop("standard_industries", UNSET))

        def _parse_compensation_range(
            data: object,
        ) -> JobPostingSearchResponse200OutputDataItemCompensationRangeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                compensation_range_type_0 = JobPostingSearchResponse200OutputDataItemCompensationRangeType0.from_dict(
                    data
                )

                return compensation_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobPostingSearchResponse200OutputDataItemCompensationRangeType0 | None | Unset, data)

        compensation_range = _parse_compensation_range(d.pop("compensation_range", UNSET))

        def _parse_annual_salary_usd(
            data: object,
        ) -> JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                annual_salary_usd_type_0 = JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0.from_dict(data)

                return annual_salary_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobPostingSearchResponse200OutputDataItemAnnualSalaryUsdType0 | None | Unset, data)

        annual_salary_usd = _parse_annual_salary_usd(d.pop("annual_salary_usd", UNSET))

        def _parse_years_of_experience(
            data: object,
        ) -> JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0.from_dict(
                    data
                )

                return years_of_experience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobPostingSearchResponse200OutputDataItemYearsOfExperienceType0 | None | Unset, data)

        years_of_experience = _parse_years_of_experience(d.pop("years_of_experience", UNSET))

        def _parse_standardized_location(
            data: object,
        ) -> JobPostingSearchResponse200OutputDataItemStandardizedLocationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                standardized_location_type_0 = (
                    JobPostingSearchResponse200OutputDataItemStandardizedLocationType0.from_dict(data)
                )

                return standardized_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobPostingSearchResponse200OutputDataItemStandardizedLocationType0 | None | Unset, data)

        standardized_location = _parse_standardized_location(d.pop("standardized_location", UNSET))

        def _parse_job_location_type(
            data: object,
        ) -> (
            JobPostingSearchResponse200OutputDataItemJobLocationTypeType1
            | JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1
            | JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1
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
                job_location_type_type_1 = JobPostingSearchResponse200OutputDataItemJobLocationTypeType1(data)

                return job_location_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_location_type_type_2_type_1 = JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1(
                    data
                )

                return job_location_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_location_type_type_3_type_1 = JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1(
                    data
                )

                return job_location_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                JobPostingSearchResponse200OutputDataItemJobLocationTypeType1
                | JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1
                | JobPostingSearchResponse200OutputDataItemJobLocationTypeType3Type1
                | None
                | Unset,
                data,
            )

        job_location_type = _parse_job_location_type(d.pop("job_location_type", UNSET))

        job_posting_search_response_200_output_data_item = cls(
            job_id=job_id,
            status=status,
            title=title,
            company_name=company_name,
            company_logo_url=company_logo_url,
            posted_at=posted_at,
            job_url=job_url,
            applicant_range=applicant_range,
            description=description,
            seniority_level=seniority_level,
            employment_type=employment_type,
            job_function=job_function,
            raw_industries=raw_industries,
            standard_industries=standard_industries,
            compensation_range=compensation_range,
            annual_salary_usd=annual_salary_usd,
            years_of_experience=years_of_experience,
            standardized_location=standardized_location,
            job_location_type=job_location_type,
        )

        job_posting_search_response_200_output_data_item.additional_properties = d
        return job_posting_search_response_200_output_data_item

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
