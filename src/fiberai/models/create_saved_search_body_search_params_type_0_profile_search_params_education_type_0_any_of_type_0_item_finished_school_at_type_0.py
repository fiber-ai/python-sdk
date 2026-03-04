from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0_strategy import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0Strategy
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0_range_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0RangeType0





T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0")



@_attrs_define
class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0:
    """ 
        Attributes:
            strategy (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtT
                ype0Strategy):
            range_ (Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedScho
                olAtType0RangeType0', None, Unset]):
     """

    strategy: CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0Strategy
    range_: Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0RangeType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0_range_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0RangeType0
        strategy = self.strategy.value

        range_: Union[None, Unset, dict[str, Any]]
        if isinstance(self.range_, Unset):
            range_ = UNSET
        elif isinstance(self.range_, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0RangeType0):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "strategy": strategy,
        })
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0_range_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0RangeType0
        d = dict(src_dict)
        strategy = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0Strategy(d.pop("strategy"))




        def _parse_range_(data: object) -> Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0RangeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0RangeType0.from_dict(data)



                return range_type_0
            except: # noqa: E722
                pass
            return cast(Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0RangeType0', None, Unset], data)

        range_ = _parse_range_(d.pop("range", UNSET))


        create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0 = cls(
            strategy=strategy,
            range_=range_,
        )


        create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0

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
