from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_2_profile_search_params_past_job_text_type_0_criteria_item_field import (
    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItemField,
)
from ..models.create_saved_search_body_search_params_type_2_profile_search_params_past_job_text_type_0_criteria_item_rule import (
    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItemRule,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItem")


@_attrs_define
class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItem:
    """
    Attributes:
        field (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItemField):
        rule (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItemRule):
        text (None | str | Unset):
    """

    field: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItemField
    rule: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItemRule
    text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field.value

        rule = self.rule.value

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "rule": rule,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItemField(
            d.pop("field")
        )

        rule = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsPastJobTextType0CriteriaItemRule(d.pop("rule"))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        create_saved_search_body_search_params_type_2_profile_search_params_past_job_text_type_0_criteria_item = cls(
            field=field,
            rule=rule,
            text=text,
        )

        create_saved_search_body_search_params_type_2_profile_search_params_past_job_text_type_0_criteria_item.additional_properties = d
        return create_saved_search_body_search_params_type_2_profile_search_params_past_job_text_type_0_criteria_item

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
