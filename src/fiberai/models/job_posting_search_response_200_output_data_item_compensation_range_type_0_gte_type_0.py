from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0_gte_type_0_period import (
    JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0Period,
)

T = TypeVar("T", bound="JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0")


@_attrs_define
class JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0:
    """
    Attributes:
        currency_unit (str): These are just currency symbols, like CA$ or £
        number (float):
        period (JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0Period):
    """

    currency_unit: str
    number: float
    period: JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0Period
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_unit = self.currency_unit

        number = self.number

        period = self.period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyUnit": currency_unit,
                "number": number,
                "period": period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_unit = d.pop("currencyUnit")

        number = d.pop("number")

        period = JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0Period(d.pop("period"))

        job_posting_search_response_200_output_data_item_compensation_range_type_0_gte_type_0 = cls(
            currency_unit=currency_unit,
            number=number,
            period=period,
        )

        job_posting_search_response_200_output_data_item_compensation_range_type_0_gte_type_0.additional_properties = d
        return job_posting_search_response_200_output_data_item_compensation_range_type_0_gte_type_0

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
