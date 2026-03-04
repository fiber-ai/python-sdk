from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="KitchenSinkBulkCompanyResponse200OutputDataItemItemEmployeeTrendsType0ItemChangesType0Item")



@_attrs_define
class KitchenSinkBulkCompanyResponse200OutputDataItemItemEmployeeTrendsType0ItemChangesType0Item:
    """ 
        Attributes:
            count_end (Union[None, Unset, float]):
            count_start (Union[None, Unset, float]):
            months_back (Union[None, Unset, float]):
            end_of_period (Union[None, Unset, str]):
            numeric_change (Union[None, Unset, float]):
            percent_change (Union[None, Unset, float]):
            start_of_period (Union[None, Unset, str]):
     """

    count_end: Union[None, Unset, float] = UNSET
    count_start: Union[None, Unset, float] = UNSET
    months_back: Union[None, Unset, float] = UNSET
    end_of_period: Union[None, Unset, str] = UNSET
    numeric_change: Union[None, Unset, float] = UNSET
    percent_change: Union[None, Unset, float] = UNSET
    start_of_period: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        count_end: Union[None, Unset, float]
        if isinstance(self.count_end, Unset):
            count_end = UNSET
        else:
            count_end = self.count_end

        count_start: Union[None, Unset, float]
        if isinstance(self.count_start, Unset):
            count_start = UNSET
        else:
            count_start = self.count_start

        months_back: Union[None, Unset, float]
        if isinstance(self.months_back, Unset):
            months_back = UNSET
        else:
            months_back = self.months_back

        end_of_period: Union[None, Unset, str]
        if isinstance(self.end_of_period, Unset):
            end_of_period = UNSET
        else:
            end_of_period = self.end_of_period

        numeric_change: Union[None, Unset, float]
        if isinstance(self.numeric_change, Unset):
            numeric_change = UNSET
        else:
            numeric_change = self.numeric_change

        percent_change: Union[None, Unset, float]
        if isinstance(self.percent_change, Unset):
            percent_change = UNSET
        else:
            percent_change = self.percent_change

        start_of_period: Union[None, Unset, str]
        if isinstance(self.start_of_period, Unset):
            start_of_period = UNSET
        else:
            start_of_period = self.start_of_period


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count_end is not UNSET:
            field_dict["count_end"] = count_end
        if count_start is not UNSET:
            field_dict["count_start"] = count_start
        if months_back is not UNSET:
            field_dict["months_back"] = months_back
        if end_of_period is not UNSET:
            field_dict["end_of_period"] = end_of_period
        if numeric_change is not UNSET:
            field_dict["numeric_change"] = numeric_change
        if percent_change is not UNSET:
            field_dict["percent_change"] = percent_change
        if start_of_period is not UNSET:
            field_dict["start_of_period"] = start_of_period

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_count_end(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        count_end = _parse_count_end(d.pop("count_end", UNSET))


        def _parse_count_start(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        count_start = _parse_count_start(d.pop("count_start", UNSET))


        def _parse_months_back(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        months_back = _parse_months_back(d.pop("months_back", UNSET))


        def _parse_end_of_period(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_of_period = _parse_end_of_period(d.pop("end_of_period", UNSET))


        def _parse_numeric_change(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        numeric_change = _parse_numeric_change(d.pop("numeric_change", UNSET))


        def _parse_percent_change(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        percent_change = _parse_percent_change(d.pop("percent_change", UNSET))


        def _parse_start_of_period(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_of_period = _parse_start_of_period(d.pop("start_of_period", UNSET))


        kitchen_sink_bulk_company_response_200_output_data_item_item_employee_trends_type_0_item_changes_type_0_item = cls(
            count_end=count_end,
            count_start=count_start,
            months_back=months_back,
            end_of_period=end_of_period,
            numeric_change=numeric_change,
            percent_change=percent_change,
            start_of_period=start_of_period,
        )


        kitchen_sink_bulk_company_response_200_output_data_item_item_employee_trends_type_0_item_changes_type_0_item.additional_properties = d
        return kitchen_sink_bulk_company_response_200_output_data_item_item_employee_trends_type_0_item_changes_type_0_item

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
