from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_1_type import CreateSavedSearchBodySearchParamsType1Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_1_company_search_params import (
        CreateSavedSearchBodySearchParamsType1CompanySearchParams,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType1")


@_attrs_define
class CreateSavedSearchBodySearchParamsType1:
    """A company-only search.

    Attributes:
        type_ (CreateSavedSearchBodySearchParamsType1Type): The search type: companies only.
        company_search_params (CreateSavedSearchBodySearchParamsType1CompanySearchParams): The company search
            parameters. Uses the same schema as the company search endpoint.
        max_new_companies_per_run (int | Unset): Maximum number of new companies to charge for per run. Default: 1000.
    """

    type_: CreateSavedSearchBodySearchParamsType1Type
    company_search_params: CreateSavedSearchBodySearchParamsType1CompanySearchParams
    max_new_companies_per_run: int | Unset = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        company_search_params = self.company_search_params.to_dict()

        max_new_companies_per_run = self.max_new_companies_per_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "companySearchParams": company_search_params,
            }
        )
        if max_new_companies_per_run is not UNSET:
            field_dict["maxNewCompaniesPerRun"] = max_new_companies_per_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParams,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = CreateSavedSearchBodySearchParamsType1Type(d.pop("type"))

        company_search_params = CreateSavedSearchBodySearchParamsType1CompanySearchParams.from_dict(
            d.pop("companySearchParams")
        )

        max_new_companies_per_run = d.pop("maxNewCompaniesPerRun", UNSET)

        create_saved_search_body_search_params_type_1 = cls(
            type_=type_,
            company_search_params=company_search_params,
            max_new_companies_per_run=max_new_companies_per_run,
        )

        create_saved_search_body_search_params_type_1.additional_properties = d
        return create_saved_search_body_search_params_type_1

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
