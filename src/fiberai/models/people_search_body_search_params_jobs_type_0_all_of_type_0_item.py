from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_status import (
    PeopleSearchBodySearchParamsJobsType0AllOfType0ItemStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_0 import (
        PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType0,
    )
    from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_1 import (
        PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType1,
    )
    from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_2 import (
        PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType2,
    )
    from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_3 import (
        PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType3,
    )
    from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_job_title_type_0 import (
        PeopleSearchBodySearchParamsJobsType0AllOfType0ItemJobTitleType0,
    )


T = TypeVar("T", bound="PeopleSearchBodySearchParamsJobsType0AllOfType0Item")


@_attrs_define
class PeopleSearchBodySearchParamsJobsType0AllOfType0Item:
    """
    Attributes:
        status (PeopleSearchBodySearchParamsJobsType0AllOfType0ItemStatus):
        company (None | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType0 |
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType1 |
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType2 |
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType3 | Unset): Company to match. Identify by LinkedIn
            org ID, LinkedIn URL, LinkedIn slug, or website domain.
        job_title (None | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemJobTitleType0 | Unset):
    """

    status: PeopleSearchBodySearchParamsJobsType0AllOfType0ItemStatus
    company: (
        None
        | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType0
        | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType1
        | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType2
        | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType3
        | Unset
    ) = UNSET
    job_title: None | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemJobTitleType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_0 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType0,
        )
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_1 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType1,
        )
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_2 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType2,
        )
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_3 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType3,
        )
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_job_title_type_0 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemJobTitleType0,
        )

        status = self.status.value

        company: dict[str, Any] | None | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        elif isinstance(self.company, PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType0):
            company = self.company.to_dict()
        elif isinstance(self.company, PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType1):
            company = self.company.to_dict()
        elif isinstance(self.company, PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType2):
            company = self.company.to_dict()
        elif isinstance(self.company, PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType3):
            company = self.company.to_dict()
        else:
            company = self.company

        job_title: dict[str, Any] | None | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, PeopleSearchBodySearchParamsJobsType0AllOfType0ItemJobTitleType0):
            job_title = self.job_title.to_dict()
        else:
            job_title = self.job_title

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_0 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType0,
        )
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_1 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType1,
        )
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_2 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType2,
        )
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_company_type_3 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType3,
        )
        from ..models.people_search_body_search_params_jobs_type_0_all_of_type_0_item_job_title_type_0 import (
            PeopleSearchBodySearchParamsJobsType0AllOfType0ItemJobTitleType0,
        )

        d = dict(src_dict)
        status = PeopleSearchBodySearchParamsJobsType0AllOfType0ItemStatus(d.pop("status"))

        def _parse_company(
            data: object,
        ) -> (
            None
            | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType0
            | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType1
            | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType2
            | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType3
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_1 = PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType1.from_dict(data)

                return company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_2 = PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType2.from_dict(data)

                return company_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_3 = PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType3.from_dict(data)

                return company_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType0
                | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType1
                | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType2
                | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemCompanyType3
                | Unset,
                data,
            )

        company = _parse_company(d.pop("company", UNSET))

        def _parse_job_title(
            data: object,
        ) -> None | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemJobTitleType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_type_0 = PeopleSearchBodySearchParamsJobsType0AllOfType0ItemJobTitleType0.from_dict(data)

                return job_title_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsJobsType0AllOfType0ItemJobTitleType0 | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        people_search_body_search_params_jobs_type_0_all_of_type_0_item = cls(
            status=status,
            company=company,
            job_title=job_title,
        )

        people_search_body_search_params_jobs_type_0_all_of_type_0_item.additional_properties = d
        return people_search_body_search_params_jobs_type_0_all_of_type_0_item

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
