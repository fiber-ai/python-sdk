from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.create_saved_search_body_search_params_type_0 import CreateSavedSearchBodySearchParamsType0
  from ..models.create_saved_search_body_search_params_type_1 import CreateSavedSearchBodySearchParamsType1
  from ..models.create_saved_search_body_search_params_type_2 import CreateSavedSearchBodySearchParamsType2





T = TypeVar("T", bound="CreateSavedSearchBody")



@_attrs_define
class CreateSavedSearchBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            name (str): The name of the saved search
            search_params (Union['CreateSavedSearchBodySearchParamsType0', 'CreateSavedSearchBodySearchParamsType1',
                'CreateSavedSearchBodySearchParamsType2']):
            spawn_frequency_days (int): The frequency of the saved search in days.
     """

    api_key: str
    name: str
    search_params: Union['CreateSavedSearchBodySearchParamsType0', 'CreateSavedSearchBodySearchParamsType1', 'CreateSavedSearchBodySearchParamsType2']
    spawn_frequency_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0 import CreateSavedSearchBodySearchParamsType0
        from ..models.create_saved_search_body_search_params_type_1 import CreateSavedSearchBodySearchParamsType1
        from ..models.create_saved_search_body_search_params_type_2 import CreateSavedSearchBodySearchParamsType2
        api_key = self.api_key

        name = self.name

        search_params: dict[str, Any]
        if isinstance(self.search_params, CreateSavedSearchBodySearchParamsType0):
            search_params = self.search_params.to_dict()
        elif isinstance(self.search_params, CreateSavedSearchBodySearchParamsType1):
            search_params = self.search_params.to_dict()
        else:
            search_params = self.search_params.to_dict()


        spawn_frequency_days = self.spawn_frequency_days


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "name": name,
            "searchParams": search_params,
            "spawnFrequencyDays": spawn_frequency_days,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0 import CreateSavedSearchBodySearchParamsType0
        from ..models.create_saved_search_body_search_params_type_1 import CreateSavedSearchBodySearchParamsType1
        from ..models.create_saved_search_body_search_params_type_2 import CreateSavedSearchBodySearchParamsType2
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        name = d.pop("name")

        def _parse_search_params(data: object) -> Union['CreateSavedSearchBodySearchParamsType0', 'CreateSavedSearchBodySearchParamsType1', 'CreateSavedSearchBodySearchParamsType2']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_params_type_0 = CreateSavedSearchBodySearchParamsType0.from_dict(data)



                return search_params_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_params_type_1 = CreateSavedSearchBodySearchParamsType1.from_dict(data)



                return search_params_type_1
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            search_params_type_2 = CreateSavedSearchBodySearchParamsType2.from_dict(data)



            return search_params_type_2

        search_params = _parse_search_params(d.pop("searchParams"))


        spawn_frequency_days = d.pop("spawnFrequencyDays")

        create_saved_search_body = cls(
            api_key=api_key,
            name=name,
            search_params=search_params,
            spawn_frequency_days=spawn_frequency_days,
        )


        create_saved_search_body.additional_properties = d
        return create_saved_search_body

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
