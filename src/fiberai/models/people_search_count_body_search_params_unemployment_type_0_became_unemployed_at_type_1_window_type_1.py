from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.people_search_count_body_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1_method import (
    PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Method,
)
from ..models.people_search_count_body_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1_period import (
    PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Period,
)
from ..models.people_search_count_body_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1_which import (
    PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which,
)

T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1")


@_attrs_define
class PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1:
    """
    Attributes:
        method (PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Method):
        which (PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which):
        period (PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Period):
    """

    method: PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Method
    which: PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which
    period: PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Period
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        which = self.which.value

        period = self.period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "which": which,
                "period": period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Method(
            d.pop("method")
        )

        which = PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which(
            d.pop("which")
        )

        period = PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Period(
            d.pop("period")
        )

        people_search_count_body_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1 = cls(
            method=method,
            which=which,
            period=period,
        )

        people_search_count_body_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1.additional_properties = d
        return people_search_count_body_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1

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
