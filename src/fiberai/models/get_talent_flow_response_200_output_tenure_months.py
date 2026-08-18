from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTalentFlowResponse200OutputTenureMonths")


@_attrs_define
class GetTalentFlowResponse200OutputTenureMonths:
    """Tenure at the analyzed company, in months.

    Attributes:
        count (int): Number of data points.
        median (float | None | Unset): Median value.
        mean (float | None | Unset): Mean (average) value.
        std_dev (float | None | Unset): Standard deviation.
        p25 (float | None | Unset): 25th percentile.
        p75 (float | None | Unset): 75th percentile.
        min_ (float | None | Unset): Minimum value.
        max_ (float | None | Unset): Maximum value.
    """

    count: int
    median: float | None | Unset = UNSET
    mean: float | None | Unset = UNSET
    std_dev: float | None | Unset = UNSET
    p25: float | None | Unset = UNSET
    p75: float | None | Unset = UNSET
    min_: float | None | Unset = UNSET
    max_: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        median: float | None | Unset
        if isinstance(self.median, Unset):
            median = UNSET
        else:
            median = self.median

        mean: float | None | Unset
        if isinstance(self.mean, Unset):
            mean = UNSET
        else:
            mean = self.mean

        std_dev: float | None | Unset
        if isinstance(self.std_dev, Unset):
            std_dev = UNSET
        else:
            std_dev = self.std_dev

        p25: float | None | Unset
        if isinstance(self.p25, Unset):
            p25 = UNSET
        else:
            p25 = self.p25

        p75: float | None | Unset
        if isinstance(self.p75, Unset):
            p75 = UNSET
        else:
            p75 = self.p75

        min_: float | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        max_: float | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
            }
        )
        if median is not UNSET:
            field_dict["median"] = median
        if mean is not UNSET:
            field_dict["mean"] = mean
        if std_dev is not UNSET:
            field_dict["stdDev"] = std_dev
        if p25 is not UNSET:
            field_dict["p25"] = p25
        if p75 is not UNSET:
            field_dict["p75"] = p75
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        def _parse_median(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        median = _parse_median(d.pop("median", UNSET))

        def _parse_mean(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mean = _parse_mean(d.pop("mean", UNSET))

        def _parse_std_dev(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        std_dev = _parse_std_dev(d.pop("stdDev", UNSET))

        def _parse_p25(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        p25 = _parse_p25(d.pop("p25", UNSET))

        def _parse_p75(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        p75 = _parse_p75(d.pop("p75", UNSET))

        def _parse_min_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        def _parse_max_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        get_talent_flow_response_200_output_tenure_months = cls(
            count=count,
            median=median,
            mean=mean,
            std_dev=std_dev,
            p25=p25,
            p75=p75,
            min_=min_,
            max_=max_,
        )

        get_talent_flow_response_200_output_tenure_months.additional_properties = d
        return get_talent_flow_response_200_output_tenure_months

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
