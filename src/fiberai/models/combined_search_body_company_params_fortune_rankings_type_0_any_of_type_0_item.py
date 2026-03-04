from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item_list import CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemList
from typing import cast

if TYPE_CHECKING:
  from ..models.combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item_range import CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemRange





T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0Item")



@_attrs_define
class CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0Item:
    """ 
        Attributes:
            list_ (CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemList):
            range_ (CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemRange):
            year (float):
     """

    list_: CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemList
    range_: 'CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemRange'
    year: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item_range import CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemRange
        list_ = self.list_.value

        range_ = self.range_.to_dict()

        year = self.year


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "list": list_,
            "range": range_,
            "year": year,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item_range import CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemRange
        d = dict(src_dict)
        list_ = CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemList(d.pop("list"))




        range_ = CombinedSearchBodyCompanyParamsFortuneRankingsType0AnyOfType0ItemRange.from_dict(d.pop("range"))




        year = d.pop("year")

        combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item = cls(
            list_=list_,
            range_=range_,
            year=year,
        )


        combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item.additional_properties = d
        return combined_search_body_company_params_fortune_rankings_type_0_any_of_type_0_item

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
