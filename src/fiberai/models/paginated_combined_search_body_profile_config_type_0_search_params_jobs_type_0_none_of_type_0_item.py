from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_status import (
    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_1 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType1,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_2 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType2,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_3 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType3,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_4 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType4,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_job_categories_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobCategoriesType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_job_function_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobFunctionType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_job_title_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobTitleType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_seniority_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemSeniorityType0,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0Item")


@_attrs_define
class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0Item:
    """
    Attributes:
        status (PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemStatus):
        company (None | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType0 |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType1 |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType2 |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType3 |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType4 | Unset): Company
            to match. Identify by LinkedIn org ID, LinkedIn URL, LinkedIn slug, website domain, or company name.
        job_title (None | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobTitleType0
            | Unset):
        job_function (None |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobFunctionType0 | Unset):
        job_categories (None |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobCategoriesType0 | Unset):
        seniority (None |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemSeniorityType0 | Unset):
    """

    status: PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemStatus
    company: (
        None
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType0
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType1
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType2
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType3
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType4
        | Unset
    ) = UNSET
    job_title: (
        None | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobTitleType0 | Unset
    ) = UNSET
    job_function: (
        None | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobFunctionType0 | Unset
    ) = UNSET
    job_categories: (
        None
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobCategoriesType0
        | Unset
    ) = UNSET
    seniority: (
        None | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemSeniorityType0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_1 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType1,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_2 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType2,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_3 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType3,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_4 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType4,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_job_categories_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobCategoriesType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_job_function_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobFunctionType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_job_title_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobTitleType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_seniority_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemSeniorityType0,  # noqa: PLC0415
        )

        status = self.status.value

        company: dict[str, Any] | None | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        elif isinstance(
            self.company, PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType0
        ):
            company = self.company.to_dict()
        elif isinstance(
            self.company, PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType1
        ):
            company = self.company.to_dict()
        elif isinstance(
            self.company, PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType2
        ):
            company = self.company.to_dict()
        elif isinstance(
            self.company, PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType3
        ):
            company = self.company.to_dict()
        elif isinstance(
            self.company, PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType4
        ):
            company = self.company.to_dict()
        else:
            company = self.company

        job_title: dict[str, Any] | None | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(
            self.job_title,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobTitleType0,
        ):
            job_title = self.job_title.to_dict()
        else:
            job_title = self.job_title

        job_function: dict[str, Any] | None | Unset
        if isinstance(self.job_function, Unset):
            job_function = UNSET
        elif isinstance(
            self.job_function,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobFunctionType0,
        ):
            job_function = self.job_function.to_dict()
        else:
            job_function = self.job_function

        job_categories: dict[str, Any] | None | Unset
        if isinstance(self.job_categories, Unset):
            job_categories = UNSET
        elif isinstance(
            self.job_categories,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobCategoriesType0,
        ):
            job_categories = self.job_categories.to_dict()
        else:
            job_categories = self.job_categories

        seniority: dict[str, Any] | None | Unset
        if isinstance(self.seniority, Unset):
            seniority = UNSET
        elif isinstance(
            self.seniority,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemSeniorityType0,
        ):
            seniority = self.seniority.to_dict()
        else:
            seniority = self.seniority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if company is not UNSET:
            field_dict["company"] = company
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if job_function is not UNSET:
            field_dict["jobFunction"] = job_function
        if job_categories is not UNSET:
            field_dict["jobCategories"] = job_categories
        if seniority is not UNSET:
            field_dict["seniority"] = seniority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_1 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType1,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_2 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType2,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_3 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType3,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_company_type_4 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType4,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_job_categories_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobCategoriesType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_job_function_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobFunctionType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_job_title_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobTitleType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item_seniority_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemSeniorityType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemStatus(
            d.pop("status")
        )

        def _parse_company(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType0
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType1
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType2
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType3
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType4
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType0.from_dict(
                    data
                )

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_1 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType1.from_dict(
                    data
                )

                return company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_2 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType2.from_dict(
                    data
                )

                return company_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_3 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType3.from_dict(
                    data
                )

                return company_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_4 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType4.from_dict(
                    data
                )

                return company_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType0
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType1
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType2
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType3
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemCompanyType4
                | Unset,
                data,
            )

        company = _parse_company(d.pop("company", UNSET))

        def _parse_job_title(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobTitleType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobTitleType0.from_dict(
                    data
                )

                return job_title_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobTitleType0
                | Unset,
                data,
            )

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_job_function(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobFunctionType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_function_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobFunctionType0.from_dict(
                    data
                )

                return job_function_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobFunctionType0
                | Unset,
                data,
            )

        job_function = _parse_job_function(d.pop("jobFunction", UNSET))

        def _parse_job_categories(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobCategoriesType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_categories_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobCategoriesType0.from_dict(
                    data
                )

                return job_categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemJobCategoriesType0
                | Unset,
                data,
            )

        job_categories = _parse_job_categories(d.pop("jobCategories", UNSET))

        def _parse_seniority(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemSeniorityType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                seniority_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemSeniorityType0.from_dict(
                    data
                )

                return seniority_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0NoneOfType0ItemSeniorityType0
                | Unset,
                data,
            )

        seniority = _parse_seniority(d.pop("seniority", UNSET))

        paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item = cls(
            status=status,
            company=company,
            job_title=job_title,
            job_function=job_function,
            job_categories=job_categories,
            seniority=seniority,
        )

        paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item.additional_properties = d
        return paginated_combined_search_body_profile_config_type_0_search_params_jobs_type_0_none_of_type_0_item

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
