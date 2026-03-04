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
  from ..models.investor_search_response_200_output_investors_item import InvestorSearchResponse200OutputInvestorsItem





T = TypeVar("T", bound="InvestorSearchResponse200Output")



@_attrs_define
class InvestorSearchResponse200Output:
    """ 
        Attributes:
            investors (list['InvestorSearchResponse200OutputInvestorsItem']): Array of investors matching the search
                criteria
            next_cursor (Union[None, Unset, str]): Cursor for fetching the next page of results. Null if no more results
                available
     """

    investors: list['InvestorSearchResponse200OutputInvestorsItem']
    next_cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.investor_search_response_200_output_investors_item import InvestorSearchResponse200OutputInvestorsItem
        investors = []
        for investors_item_data in self.investors:
            investors_item = investors_item_data.to_dict()
            investors.append(investors_item)



        next_cursor: Union[None, Unset, str]
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "investors": investors,
        })
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investor_search_response_200_output_investors_item import InvestorSearchResponse200OutputInvestorsItem
        d = dict(src_dict)
        investors = []
        _investors = d.pop("investors")
        for investors_item_data in (_investors):
            investors_item = InvestorSearchResponse200OutputInvestorsItem.from_dict(investors_item_data)



            investors.append(investors_item)


        def _parse_next_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))


        investor_search_response_200_output = cls(
            investors=investors,
            next_cursor=next_cursor,
        )


        investor_search_response_200_output.additional_properties = d
        return investor_search_response_200_output

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
