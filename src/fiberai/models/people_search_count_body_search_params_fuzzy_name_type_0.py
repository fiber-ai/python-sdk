from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.people_search_count_body_search_params_fuzzy_name_type_0_any_of_item import PeopleSearchCountBodySearchParamsFuzzyNameType0AnyOfItem





T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsFuzzyNameType0")



@_attrs_define
class PeopleSearchCountBodySearchParamsFuzzyNameType0:
    """ 
        Attributes:
            any_of (list['PeopleSearchCountBodySearchParamsFuzzyNameType0AnyOfItem']):
     """

    any_of: list['PeopleSearchCountBodySearchParamsFuzzyNameType0AnyOfItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_count_body_search_params_fuzzy_name_type_0_any_of_item import PeopleSearchCountBodySearchParamsFuzzyNameType0AnyOfItem
        any_of = []
        for any_of_item_data in self.any_of:
            any_of_item = any_of_item_data.to_dict()
            any_of.append(any_of_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "anyOf": any_of,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_count_body_search_params_fuzzy_name_type_0_any_of_item import PeopleSearchCountBodySearchParamsFuzzyNameType0AnyOfItem
        d = dict(src_dict)
        any_of = []
        _any_of = d.pop("anyOf")
        for any_of_item_data in (_any_of):
            any_of_item = PeopleSearchCountBodySearchParamsFuzzyNameType0AnyOfItem.from_dict(any_of_item_data)



            any_of.append(any_of_item)


        people_search_count_body_search_params_fuzzy_name_type_0 = cls(
            any_of=any_of,
        )


        people_search_count_body_search_params_fuzzy_name_type_0.additional_properties = d
        return people_search_count_body_search_params_fuzzy_name_type_0

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
