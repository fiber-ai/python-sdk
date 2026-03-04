from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.investment_search_response_200_output_investments_item import InvestmentSearchResponse200OutputInvestmentsItem





T = TypeVar("T", bound="InvestmentSearchResponse200Output")



@_attrs_define
class InvestmentSearchResponse200Output:
    """ 
        Attributes:
            investments (list['InvestmentSearchResponse200OutputInvestmentsItem']): Array of investment results
            next_cursor (Union[None, str]): Pagination cursor for the next page. Null if there are no more results.
     """

    investments: list['InvestmentSearchResponse200OutputInvestmentsItem']
    next_cursor: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.investment_search_response_200_output_investments_item import InvestmentSearchResponse200OutputInvestmentsItem
        investments = []
        for investments_item_data in self.investments:
            investments_item = investments_item_data.to_dict()
            investments.append(investments_item)



        next_cursor: Union[None, str]
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "investments": investments,
            "nextCursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_search_response_200_output_investments_item import InvestmentSearchResponse200OutputInvestmentsItem
        d = dict(src_dict)
        investments = []
        _investments = d.pop("investments")
        for investments_item_data in (_investments):
            investments_item = InvestmentSearchResponse200OutputInvestmentsItem.from_dict(investments_item_data)



            investments.append(investments_item)


        def _parse_next_cursor(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))


        investment_search_response_200_output = cls(
            investments=investments,
            next_cursor=next_cursor,
        )


        investment_search_response_200_output.additional_properties = d
        return investment_search_response_200_output

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
