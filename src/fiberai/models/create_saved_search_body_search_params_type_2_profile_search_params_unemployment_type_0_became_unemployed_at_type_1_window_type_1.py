from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_2_profile_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1_method import (
    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Method,
)
from ..models.create_saved_search_body_search_params_type_2_profile_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1_period import (
    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Period,
)
from ..models.create_saved_search_body_search_params_type_2_profile_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1_which import (
    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which,
)

T = TypeVar(
    "T",
    bound="CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1",
)


@_attrs_define
class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1:
    """
    Attributes:
        method (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowT
            ype1Method):
        which (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowTy
            pe1Which):
        period (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowT
            ype1Period):
    """

    method: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Method
    which: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which
    period: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Period
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
        method = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Method(
            d.pop("method")
        )

        which = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which(
            d.pop("which")
        )

        period = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Period(
            d.pop("period")
        )

        create_saved_search_body_search_params_type_2_profile_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1 = cls(
            method=method,
            which=which,
            period=period,
        )

        create_saved_search_body_search_params_type_2_profile_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1.additional_properties = d
        return create_saved_search_body_search_params_type_2_profile_search_params_unemployment_type_0_became_unemployed_at_type_1_window_type_1

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
