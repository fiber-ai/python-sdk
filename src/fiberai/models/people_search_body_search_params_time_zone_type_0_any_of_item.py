from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.people_search_body_search_params_time_zone_type_0_any_of_item_strategy_type_0 import PeopleSearchBodySearchParamsTimeZoneType0AnyOfItemStrategyType0





T = TypeVar("T", bound="PeopleSearchBodySearchParamsTimeZoneType0AnyOfItem")



@_attrs_define
class PeopleSearchBodySearchParamsTimeZoneType0AnyOfItem:
    """ 
        Attributes:
            strategy ('PeopleSearchBodySearchParamsTimeZoneType0AnyOfItemStrategyType0'):
     """

    strategy: 'PeopleSearchBodySearchParamsTimeZoneType0AnyOfItemStrategyType0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_body_search_params_time_zone_type_0_any_of_item_strategy_type_0 import PeopleSearchBodySearchParamsTimeZoneType0AnyOfItemStrategyType0
        strategy: dict[str, Any]
        if isinstance(self.strategy, PeopleSearchBodySearchParamsTimeZoneType0AnyOfItemStrategyType0):
            strategy = self.strategy.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "strategy": strategy,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_body_search_params_time_zone_type_0_any_of_item_strategy_type_0 import PeopleSearchBodySearchParamsTimeZoneType0AnyOfItemStrategyType0
        d = dict(src_dict)
        def _parse_strategy(data: object) -> 'PeopleSearchBodySearchParamsTimeZoneType0AnyOfItemStrategyType0':
            if not isinstance(data, dict):
                raise TypeError()
            strategy_type_0 = PeopleSearchBodySearchParamsTimeZoneType0AnyOfItemStrategyType0.from_dict(data)



            return strategy_type_0

        strategy = _parse_strategy(d.pop("strategy"))


        people_search_body_search_params_time_zone_type_0_any_of_item = cls(
            strategy=strategy,
        )


        people_search_body_search_params_time_zone_type_0_any_of_item.additional_properties = d
        return people_search_body_search_params_time_zone_type_0_any_of_item

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
