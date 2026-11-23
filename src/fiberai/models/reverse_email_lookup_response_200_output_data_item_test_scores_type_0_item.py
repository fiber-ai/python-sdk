from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReverseEmailLookupResponse200OutputDataItemTestScoresType0Item")


@_attrs_define
class ReverseEmailLookupResponse200OutputDataItemTestScoresType0Item:
    """
    Attributes:
        test_date (None | str | Unset):
        test_description (None | str | Unset):
        test_name (None | str | Unset):
        test_score (None | str | Unset):
    """

    test_date: None | str | Unset = UNSET
    test_description: None | str | Unset = UNSET
    test_name: None | str | Unset = UNSET
    test_score: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_date: None | str | Unset
        if isinstance(self.test_date, Unset):
            test_date = UNSET
        else:
            test_date = self.test_date

        test_description: None | str | Unset
        if isinstance(self.test_description, Unset):
            test_description = UNSET
        else:
            test_description = self.test_description

        test_name: None | str | Unset
        if isinstance(self.test_name, Unset):
            test_name = UNSET
        else:
            test_name = self.test_name

        test_score: None | str | Unset
        if isinstance(self.test_score, Unset):
            test_score = UNSET
        else:
            test_score = self.test_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if test_date is not UNSET:
            field_dict["test_date"] = test_date
        if test_description is not UNSET:
            field_dict["test_description"] = test_description
        if test_name is not UNSET:
            field_dict["test_name"] = test_name
        if test_score is not UNSET:
            field_dict["test_score"] = test_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_test_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_date = _parse_test_date(d.pop("test_date", UNSET))

        def _parse_test_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_description = _parse_test_description(d.pop("test_description", UNSET))

        def _parse_test_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_name = _parse_test_name(d.pop("test_name", UNSET))

        def _parse_test_score(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        test_score = _parse_test_score(d.pop("test_score", UNSET))

        reverse_email_lookup_response_200_output_data_item_test_scores_type_0_item = cls(
            test_date=test_date,
            test_description=test_description,
            test_name=test_name,
            test_score=test_score,
        )

        reverse_email_lookup_response_200_output_data_item_test_scores_type_0_item.additional_properties = d
        return reverse_email_lookup_response_200_output_data_item_test_scores_type_0_item

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
