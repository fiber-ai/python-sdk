from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputDataCompaniesItemStockInfoConsensusType0")



@_attrs_define
class TextToCombinedSearchResponse200OutputDataCompaniesItemStockInfoConsensusType0:
    """ 
        Attributes:
            ticker (Union[None, Unset, str]):
            exchange (Union[None, Unset, str]):
     """

    ticker: Union[None, Unset, str] = UNSET
    exchange: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ticker: Union[None, Unset, str]
        if isinstance(self.ticker, Unset):
            ticker = UNSET
        else:
            ticker = self.ticker

        exchange: Union[None, Unset, str]
        if isinstance(self.exchange, Unset):
            exchange = UNSET
        else:
            exchange = self.exchange


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if exchange is not UNSET:
            field_dict["exchange"] = exchange

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_ticker(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ticker = _parse_ticker(d.pop("ticker", UNSET))


        def _parse_exchange(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        exchange = _parse_exchange(d.pop("exchange", UNSET))


        text_to_combined_search_response_200_output_data_companies_item_stock_info_consensus_type_0 = cls(
            ticker=ticker,
            exchange=exchange,
        )


        text_to_combined_search_response_200_output_data_companies_item_stock_info_consensus_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_data_companies_item_stock_info_consensus_type_0

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
