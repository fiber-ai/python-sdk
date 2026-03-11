from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_profile_search_params_response_200_output_search_params_past_jobs_type_0_any_of_type_0_item_company_type_0 import (
        TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0ItemCompanyType0,
    )


T = TypeVar("T", bound="TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0Item")


@_attrs_define
class TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0Item:
    """
    Attributes:
        job_title (list[str] | None | Unset):
        company (None | TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0ItemCompanyType0 |
            Unset):
    """

    job_title: list[str] | None | Unset = UNSET
    company: (
        None | TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0ItemCompanyType0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_profile_search_params_response_200_output_search_params_past_jobs_type_0_any_of_type_0_item_company_type_0 import (
            TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0ItemCompanyType0,
        )

        job_title: list[str] | None | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, list):
            job_title = self.job_title

        else:
            job_title = self.job_title

        company: dict[str, Any] | None | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        elif isinstance(
            self.company, TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0ItemCompanyType0
        ):
            company = self.company.to_dict()
        else:
            company = self.company

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if company is not UNSET:
            field_dict["company"] = company

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_profile_search_params_response_200_output_search_params_past_jobs_type_0_any_of_type_0_item_company_type_0 import (
            TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0ItemCompanyType0,
        )

        d = dict(src_dict)

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

        def _parse_company(
            data: object,
        ) -> (
            None | TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0ItemCompanyType0 | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0ItemCompanyType0.from_dict(
                    data
                )

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToProfileSearchParamsResponse200OutputSearchParamsPastJobsType0AnyOfType0ItemCompanyType0
                | Unset,
                data,
            )

        company = _parse_company(d.pop("company", UNSET))

        text_to_profile_search_params_response_200_output_search_params_past_jobs_type_0_any_of_type_0_item = cls(
            job_title=job_title,
            company=company,
        )

        text_to_profile_search_params_response_200_output_search_params_past_jobs_type_0_any_of_type_0_item.additional_properties = d
        return text_to_profile_search_params_response_200_output_search_params_past_jobs_type_0_any_of_type_0_item

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
