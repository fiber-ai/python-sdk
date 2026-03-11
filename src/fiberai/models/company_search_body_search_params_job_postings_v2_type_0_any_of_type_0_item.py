from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_country_or_region_code_type_0_item import (
    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemCountryOrRegionCodeType0Item,
)
from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_employment_type_type_0_item import (
    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemEmploymentTypeType0Item,
)
from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_industry_type_0_item import (
    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemIndustryType0Item,
)
from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_job_function_type_0_item import (
    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobFunctionType0Item,
)
from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_job_location_type_type_0_item import (
    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobLocationTypeType0Item,
)
from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_job_posting_status_type_1 import (
    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType1,
)
from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_job_posting_status_type_2_type_1 import (
    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType2Type1,
)
from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_job_posting_status_type_3_type_1 import (
    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType3Type1,
)
from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_seniority_type_0_item import (
    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemSeniorityType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_annual_pay_usd_type_0 import (
        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemAnnualPayUSDType0,
    )
    from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_geo_location_type_0 import (
        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemGeoLocationType0,
    )
    from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_num_applicants_type_0 import (
        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemNumApplicantsType0,
    )
    from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_0 import (
        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType0,
    )
    from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1 import (
        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1,
    )
    from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_years_of_experience_type_0 import (
        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemYearsOfExperienceType0,
    )


T = TypeVar("T", bound="CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0Item")


@_attrs_define
class CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0Item:
    """
    Attributes:
        job_posting_status (CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType1 |
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType2Type1 |
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType3Type1 | None | Unset):
        job_title (list[str] | None | Unset):
        keywords (list[str] | None | Unset):
        posted_at (CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType0 |
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1 | None | Unset):
        num_applicants (CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemNumApplicantsType0 | None | Unset):
        annual_pay_usd (CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemAnnualPayUSDType0 | None | Unset):
        years_of_experience (CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemYearsOfExperienceType0 | None
            | Unset):
        geo_location (CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemGeoLocationType0 | None | Unset):
        country_or_region_code
            (list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemCountryOrRegionCodeType0Item] | None |
            Unset):
        seniority (list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemSeniorityType0Item] | None |
            Unset):
        employment_type (list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemEmploymentTypeType0Item] |
            None | Unset):
        job_function (list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobFunctionType0Item] | None |
            Unset):
        industry (list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemIndustryType0Item] | None | Unset):
        job_location_type (list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobLocationTypeType0Item] |
            None | Unset):
    """

    job_posting_status: (
        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType1
        | CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType2Type1
        | CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType3Type1
        | None
        | Unset
    ) = UNSET
    job_title: list[str] | None | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    posted_at: (
        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType0
        | CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1
        | None
        | Unset
    ) = UNSET
    num_applicants: CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemNumApplicantsType0 | None | Unset = (
        UNSET
    )
    annual_pay_usd: CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemAnnualPayUSDType0 | None | Unset = (
        UNSET
    )
    years_of_experience: (
        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemYearsOfExperienceType0 | None | Unset
    ) = UNSET
    geo_location: CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemGeoLocationType0 | None | Unset = UNSET
    country_or_region_code: (
        list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemCountryOrRegionCodeType0Item] | None | Unset
    ) = UNSET
    seniority: list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemSeniorityType0Item] | None | Unset = (
        UNSET
    )
    employment_type: (
        list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemEmploymentTypeType0Item] | None | Unset
    ) = UNSET
    job_function: (
        list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobFunctionType0Item] | None | Unset
    ) = UNSET
    industry: list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemIndustryType0Item] | None | Unset = (
        UNSET
    )
    job_location_type: (
        list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobLocationTypeType0Item] | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_annual_pay_usd_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemAnnualPayUSDType0,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_geo_location_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemGeoLocationType0,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_num_applicants_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemNumApplicantsType0,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType0,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_years_of_experience_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemYearsOfExperienceType0,
        )

        job_posting_status: None | str | Unset
        if isinstance(self.job_posting_status, Unset):
            job_posting_status = UNSET
        elif isinstance(
            self.job_posting_status, CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType1
        ):
            job_posting_status = self.job_posting_status.value
        elif isinstance(
            self.job_posting_status,
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType2Type1,
        ):
            job_posting_status = self.job_posting_status.value
        elif isinstance(
            self.job_posting_status,
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType3Type1,
        ):
            job_posting_status = self.job_posting_status.value
        else:
            job_posting_status = self.job_posting_status

        job_title: list[str] | None | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, list):
            job_title = self.job_title

        else:
            job_title = self.job_title

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        posted_at: dict[str, Any] | None | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        elif isinstance(self.posted_at, CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType0):
            posted_at = self.posted_at.to_dict()
        elif isinstance(self.posted_at, CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1):
            posted_at = self.posted_at.to_dict()
        else:
            posted_at = self.posted_at

        num_applicants: dict[str, Any] | None | Unset
        if isinstance(self.num_applicants, Unset):
            num_applicants = UNSET
        elif isinstance(
            self.num_applicants, CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemNumApplicantsType0
        ):
            num_applicants = self.num_applicants.to_dict()
        else:
            num_applicants = self.num_applicants

        annual_pay_usd: dict[str, Any] | None | Unset
        if isinstance(self.annual_pay_usd, Unset):
            annual_pay_usd = UNSET
        elif isinstance(
            self.annual_pay_usd, CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemAnnualPayUSDType0
        ):
            annual_pay_usd = self.annual_pay_usd.to_dict()
        else:
            annual_pay_usd = self.annual_pay_usd

        years_of_experience: dict[str, Any] | None | Unset
        if isinstance(self.years_of_experience, Unset):
            years_of_experience = UNSET
        elif isinstance(
            self.years_of_experience,
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemYearsOfExperienceType0,
        ):
            years_of_experience = self.years_of_experience.to_dict()
        else:
            years_of_experience = self.years_of_experience

        geo_location: dict[str, Any] | None | Unset
        if isinstance(self.geo_location, Unset):
            geo_location = UNSET
        elif isinstance(
            self.geo_location, CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemGeoLocationType0
        ):
            geo_location = self.geo_location.to_dict()
        else:
            geo_location = self.geo_location

        country_or_region_code: list[str] | None | Unset
        if isinstance(self.country_or_region_code, Unset):
            country_or_region_code = UNSET
        elif isinstance(self.country_or_region_code, list):
            country_or_region_code = []
            for country_or_region_code_type_0_item_data in self.country_or_region_code:
                country_or_region_code_type_0_item = country_or_region_code_type_0_item_data.value
                country_or_region_code.append(country_or_region_code_type_0_item)

        else:
            country_or_region_code = self.country_or_region_code

        seniority: list[str] | None | Unset
        if isinstance(self.seniority, Unset):
            seniority = UNSET
        elif isinstance(self.seniority, list):
            seniority = []
            for seniority_type_0_item_data in self.seniority:
                seniority_type_0_item = seniority_type_0_item_data.value
                seniority.append(seniority_type_0_item)

        else:
            seniority = self.seniority

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

        industry: list[str] | None | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        elif isinstance(self.industry, list):
            industry = []
            for industry_type_0_item_data in self.industry:
                industry_type_0_item = industry_type_0_item_data.value
                industry.append(industry_type_0_item)

        else:
            industry = self.industry

        job_location_type: list[str] | None | Unset
        if isinstance(self.job_location_type, Unset):
            job_location_type = UNSET
        elif isinstance(self.job_location_type, list):
            job_location_type = []
            for job_location_type_type_0_item_data in self.job_location_type:
                job_location_type_type_0_item = job_location_type_type_0_item_data.value
                job_location_type.append(job_location_type_type_0_item)

        else:
            job_location_type = self.job_location_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_posting_status is not UNSET:
            field_dict["jobPostingStatus"] = job_posting_status
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if posted_at is not UNSET:
            field_dict["postedAt"] = posted_at
        if num_applicants is not UNSET:
            field_dict["numApplicants"] = num_applicants
        if annual_pay_usd is not UNSET:
            field_dict["annualPayUSD"] = annual_pay_usd
        if years_of_experience is not UNSET:
            field_dict["yearsOfExperience"] = years_of_experience
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location
        if country_or_region_code is not UNSET:
            field_dict["countryOrRegionCode"] = country_or_region_code
        if seniority is not UNSET:
            field_dict["seniority"] = seniority
        if employment_type is not UNSET:
            field_dict["employmentType"] = employment_type
        if job_function is not UNSET:
            field_dict["jobFunction"] = job_function
        if industry is not UNSET:
            field_dict["industry"] = industry
        if job_location_type is not UNSET:
            field_dict["jobLocationType"] = job_location_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_annual_pay_usd_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemAnnualPayUSDType0,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_geo_location_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemGeoLocationType0,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_num_applicants_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemNumApplicantsType0,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType0,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1,
        )
        from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_years_of_experience_type_0 import (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemYearsOfExperienceType0,
        )

        d = dict(src_dict)

        def _parse_job_posting_status(
            data: object,
        ) -> (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType1
            | CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType2Type1
            | CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType3Type1
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
                job_posting_status_type_1 = (
                    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType1(data)
                )

                return job_posting_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_posting_status_type_2_type_1 = (
                    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType2Type1(data)
                )

                return job_posting_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_posting_status_type_3_type_1 = (
                    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType3Type1(data)
                )

                return job_posting_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType1
                | CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType2Type1
                | CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobPostingStatusType3Type1
                | None
                | Unset,
                data,
            )

        job_posting_status = _parse_job_posting_status(d.pop("jobPostingStatus", UNSET))

        def _parse_job_title(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_title_type_0 = cast(list[str], data)

                return job_title_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_posted_at(
            data: object,
        ) -> (
            CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType0
            | CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                posted_at_type_0 = CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType0.from_dict(
                    data
                )

                return posted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                posted_at_type_1 = CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1.from_dict(
                    data
                )

                return posted_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType0
                | CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1
                | None
                | Unset,
                data,
            )

        posted_at = _parse_posted_at(d.pop("postedAt", UNSET))

        def _parse_num_applicants(
            data: object,
        ) -> CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemNumApplicantsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_applicants_type_0 = (
                    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemNumApplicantsType0.from_dict(data)
                )

                return num_applicants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemNumApplicantsType0 | None | Unset, data
            )

        num_applicants = _parse_num_applicants(d.pop("numApplicants", UNSET))

        def _parse_annual_pay_usd(
            data: object,
        ) -> CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemAnnualPayUSDType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                annual_pay_usd_type_0 = (
                    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemAnnualPayUSDType0.from_dict(data)
                )

                return annual_pay_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemAnnualPayUSDType0 | None | Unset, data
            )

        annual_pay_usd = _parse_annual_pay_usd(d.pop("annualPayUSD", UNSET))

        def _parse_years_of_experience(
            data: object,
        ) -> CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemYearsOfExperienceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_of_experience_type_0 = (
                    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemYearsOfExperienceType0.from_dict(data)
                )

                return years_of_experience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemYearsOfExperienceType0 | None | Unset, data
            )

        years_of_experience = _parse_years_of_experience(d.pop("yearsOfExperience", UNSET))

        def _parse_geo_location(
            data: object,
        ) -> CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemGeoLocationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geo_location_type_0 = (
                    CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemGeoLocationType0.from_dict(data)
                )

                return geo_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemGeoLocationType0 | None | Unset, data
            )

        geo_location = _parse_geo_location(d.pop("geoLocation", UNSET))

        def _parse_country_or_region_code(
            data: object,
        ) -> (
            list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemCountryOrRegionCodeType0Item]
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
                country_or_region_code_type_0 = []
                _country_or_region_code_type_0 = data
                for country_or_region_code_type_0_item_data in _country_or_region_code_type_0:
                    country_or_region_code_type_0_item = (
                        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemCountryOrRegionCodeType0Item(
                            country_or_region_code_type_0_item_data
                        )
                    )

                    country_or_region_code_type_0.append(country_or_region_code_type_0_item)

                return country_or_region_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemCountryOrRegionCodeType0Item]
                | None
                | Unset,
                data,
            )

        country_or_region_code = _parse_country_or_region_code(d.pop("countryOrRegionCode", UNSET))

        def _parse_seniority(
            data: object,
        ) -> list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemSeniorityType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                seniority_type_0 = []
                _seniority_type_0 = data
                for seniority_type_0_item_data in _seniority_type_0:
                    seniority_type_0_item = (
                        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemSeniorityType0Item(
                            seniority_type_0_item_data
                        )
                    )

                    seniority_type_0.append(seniority_type_0_item)

                return seniority_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemSeniorityType0Item] | None | Unset,
                data,
            )

        seniority = _parse_seniority(d.pop("seniority", UNSET))

        def _parse_employment_type(
            data: object,
        ) -> list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemEmploymentTypeType0Item] | None | Unset:
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
                        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemEmploymentTypeType0Item(
                            employment_type_type_0_item_data
                        )
                    )

                    employment_type_type_0.append(employment_type_type_0_item)

                return employment_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemEmploymentTypeType0Item]
                | None
                | Unset,
                data,
            )

        employment_type = _parse_employment_type(d.pop("employmentType", UNSET))

        def _parse_job_function(
            data: object,
        ) -> list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobFunctionType0Item] | None | Unset:
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
                        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobFunctionType0Item(
                            job_function_type_0_item_data
                        )
                    )

                    job_function_type_0.append(job_function_type_0_item)

                return job_function_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobFunctionType0Item] | None | Unset,
                data,
            )

        job_function = _parse_job_function(d.pop("jobFunction", UNSET))

        def _parse_industry(
            data: object,
        ) -> list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemIndustryType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                industry_type_0 = []
                _industry_type_0 = data
                for industry_type_0_item_data in _industry_type_0:
                    industry_type_0_item = (
                        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemIndustryType0Item(
                            industry_type_0_item_data
                        )
                    )

                    industry_type_0.append(industry_type_0_item)

                return industry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemIndustryType0Item] | None | Unset,
                data,
            )

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_job_location_type(
            data: object,
        ) -> list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobLocationTypeType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_location_type_type_0 = []
                _job_location_type_type_0 = data
                for job_location_type_type_0_item_data in _job_location_type_type_0:
                    job_location_type_type_0_item = (
                        CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobLocationTypeType0Item(
                            job_location_type_type_0_item_data
                        )
                    )

                    job_location_type_type_0.append(job_location_type_type_0_item)

                return job_location_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobLocationTypeType0Item]
                | None
                | Unset,
                data,
            )

        job_location_type = _parse_job_location_type(d.pop("jobLocationType", UNSET))

        company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item = cls(
            job_posting_status=job_posting_status,
            job_title=job_title,
            keywords=keywords,
            posted_at=posted_at,
            num_applicants=num_applicants,
            annual_pay_usd=annual_pay_usd,
            years_of_experience=years_of_experience,
            geo_location=geo_location,
            country_or_region_code=country_or_region_code,
            seniority=seniority,
            employment_type=employment_type,
            job_function=job_function,
            industry=industry,
            job_location_type=job_location_type,
        )

        company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item.additional_properties = d
        return company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item

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
