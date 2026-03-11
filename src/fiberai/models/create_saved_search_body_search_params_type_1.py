from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
    """companies

    Attributes:
        type_ (CreateSavedSearchBodySearchParamsType1Type): companies
        company_search_params (CreateSavedSearchBodySearchParamsType1CompanySearchParams): The company search params.
            This is same as our normal company search api.
        max_companies (int | None | Unset): Max companies to find. Defaults to 10000 if not provided. Default: 10000.
    """

    type_: CreateSavedSearchBodySearchParamsType1Type
    company_search_params: CreateSavedSearchBodySearchParamsType1CompanySearchParams
    max_companies: int | None | Unset = 10000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        company_search_params = self.company_search_params.to_dict()

        max_companies: int | None | Unset
        if isinstance(self.max_companies, Unset):
            max_companies = UNSET
        else:
            max_companies = self.max_companies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "companySearchParams": company_search_params,
            }
        )
        if max_companies is not UNSET:
            field_dict["maxCompanies"] = max_companies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParams,
        )

        d = dict(src_dict)
        type_ = CreateSavedSearchBodySearchParamsType1Type(d.pop("type"))

        company_search_params = CreateSavedSearchBodySearchParamsType1CompanySearchParams.from_dict(
            d.pop("companySearchParams")
        )

        def _parse_max_companies(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_companies = _parse_max_companies(d.pop("maxCompanies", UNSET))

        create_saved_search_body_search_params_type_1 = cls(
            type_=type_,
            company_search_params=company_search_params,
            max_companies=max_companies,
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
