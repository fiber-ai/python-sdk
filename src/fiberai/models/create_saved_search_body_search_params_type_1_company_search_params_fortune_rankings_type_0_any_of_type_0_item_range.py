from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType1CompanySearchParamsFortuneRankingsType0AnyOfType0ItemRange")



@_attrs_define
class CreateSavedSearchBodySearchParamsType1CompanySearchParamsFortuneRankingsType0AnyOfType0ItemRange:
    """ 
        Attributes:
            low (float):
            high (float):
            name (Union[None, Unset, str]):
     """

    low: float
    high: float
    name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        low = self.low

        high = self.high

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "low": low,
            "high": high,
        })
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        low = d.pop("low")

        high = d.pop("high")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        create_saved_search_body_search_params_type_1_company_search_params_fortune_rankings_type_0_any_of_type_0_item_range = cls(
            low=low,
            high=high,
            name=name,
        )


        create_saved_search_body_search_params_type_1_company_search_params_fortune_rankings_type_0_any_of_type_0_item_range.additional_properties = d
        return create_saved_search_body_search_params_type_1_company_search_params_fortune_rankings_type_0_any_of_type_0_item_range

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
