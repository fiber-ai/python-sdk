from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.people_search_body_search_params_keyword_search_options_type_0_fields_to_search_over_type_0 import PeopleSearchBodySearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0





T = TypeVar("T", bound="PeopleSearchBodySearchParamsKeywordSearchOptionsType0")



@_attrs_define
class PeopleSearchBodySearchParamsKeywordSearchOptionsType0:
    """ 
        Attributes:
            fields_to_search_over (Union['PeopleSearchBodySearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0',
                None, Unset]):
     """

    fields_to_search_over: Union['PeopleSearchBodySearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_body_search_params_keyword_search_options_type_0_fields_to_search_over_type_0 import PeopleSearchBodySearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0
        fields_to_search_over: Union[None, Unset, dict[str, Any]]
        if isinstance(self.fields_to_search_over, Unset):
            fields_to_search_over = UNSET
        elif isinstance(self.fields_to_search_over, PeopleSearchBodySearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0):
            fields_to_search_over = self.fields_to_search_over.to_dict()
        else:
            fields_to_search_over = self.fields_to_search_over


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields_to_search_over is not UNSET:
            field_dict["fieldsToSearchOver"] = fields_to_search_over

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_body_search_params_keyword_search_options_type_0_fields_to_search_over_type_0 import PeopleSearchBodySearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0
        d = dict(src_dict)
        def _parse_fields_to_search_over(data: object) -> Union['PeopleSearchBodySearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_to_search_over_type_0 = PeopleSearchBodySearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0.from_dict(data)



                return fields_to_search_over_type_0
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchBodySearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0', None, Unset], data)

        fields_to_search_over = _parse_fields_to_search_over(d.pop("fieldsToSearchOver", UNSET))


        people_search_body_search_params_keyword_search_options_type_0 = cls(
            fields_to_search_over=fields_to_search_over,
        )


        people_search_body_search_params_keyword_search_options_type_0.additional_properties = d
        return people_search_body_search_params_keyword_search_options_type_0

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
