from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_saved_search_body_search_params_type_0_company_search_params_revenue_usd_type_0_max_type_0_suffix_type_1 import CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType1
from ..models.create_saved_search_body_search_params_type_0_company_search_params_revenue_usd_type_0_max_type_0_suffix_type_2_type_1 import CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType2Type1
from ..models.create_saved_search_body_search_params_type_0_company_search_params_revenue_usd_type_0_max_type_0_suffix_type_3_type_1 import CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType3Type1
from typing import cast, Union






T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0")



@_attrs_define
class CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0:
    """ 
        Attributes:
            quantity (float):
            suffix (Union[CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType1,
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType2Type1,
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType3Type1, None]):
     """

    quantity: float
    suffix: Union[CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType1, CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType2Type1, CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType3Type1, None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        suffix: Union[None, str]
        if isinstance(self.suffix, CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType1):
            suffix = self.suffix.value
        elif isinstance(self.suffix, CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType2Type1):
            suffix = self.suffix.value
        elif isinstance(self.suffix, CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType3Type1):
            suffix = self.suffix.value
        else:
            suffix = self.suffix


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "quantity": quantity,
            "suffix": suffix,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        def _parse_suffix(data: object) -> Union[CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType1, CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType2Type1, CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType3Type1, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suffix_type_1 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType1(data)



                return suffix_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suffix_type_2_type_1 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType2Type1(data)



                return suffix_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suffix_type_3_type_1 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType3Type1(data)



                return suffix_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType1, CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType2Type1, CreateSavedSearchBodySearchParamsType0CompanySearchParamsRevenueUSDType0MaxType0SuffixType3Type1, None], data)

        suffix = _parse_suffix(d.pop("suffix"))


        create_saved_search_body_search_params_type_0_company_search_params_revenue_usd_type_0_max_type_0 = cls(
            quantity=quantity,
            suffix=suffix,
        )


        create_saved_search_body_search_params_type_0_company_search_params_revenue_usd_type_0_max_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_0_company_search_params_revenue_usd_type_0_max_type_0

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
