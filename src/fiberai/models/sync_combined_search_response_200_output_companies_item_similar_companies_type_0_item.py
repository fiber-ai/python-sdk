from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="SyncCombinedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item")



@_attrs_define
class SyncCombinedSearchResponse200OutputCompaniesItemSimilarCompaniesType0Item:
    """ 
        Attributes:
            name (Union[None, Unset, str]):
            industries (Union[None, Unset, list[str]]):
            employee_count (Union[None, Unset, float]):
            revenue (Union[None, Unset, float]):
            logo_url (Union[None, Unset, str]):
     """

    name: Union[None, Unset, str] = UNSET
    industries: Union[None, Unset, list[str]] = UNSET
    employee_count: Union[None, Unset, float] = UNSET
    revenue: Union[None, Unset, float] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        industries: Union[None, Unset, list[str]]
        if isinstance(self.industries, Unset):
            industries = UNSET
        elif isinstance(self.industries, list):
            industries = self.industries


        else:
            industries = self.industries

        employee_count: Union[None, Unset, float]
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        revenue: Union[None, Unset, float]
        if isinstance(self.revenue, Unset):
            revenue = UNSET
        else:
            revenue = self.revenue

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if industries is not UNSET:
            field_dict["industries"] = industries
        if employee_count is not UNSET:
            field_dict["employee_count"] = employee_count
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_industries(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                industries_type_0 = cast(list[str], data)

                return industries_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        industries = _parse_industries(d.pop("industries", UNSET))


        def _parse_employee_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        employee_count = _parse_employee_count(d.pop("employee_count", UNSET))


        def _parse_revenue(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        revenue = _parse_revenue(d.pop("revenue", UNSET))


        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))


        sync_combined_search_response_200_output_companies_item_similar_companies_type_0_item = cls(
            name=name,
            industries=industries,
            employee_count=employee_count,
            revenue=revenue,
            logo_url=logo_url,
        )


        sync_combined_search_response_200_output_companies_item_similar_companies_type_0_item.additional_properties = d
        return sync_combined_search_response_200_output_companies_item_similar_companies_type_0_item

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
