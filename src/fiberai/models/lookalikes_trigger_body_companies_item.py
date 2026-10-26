from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LookalikesTriggerBodyCompaniesItem")


@_attrs_define
class LookalikesTriggerBodyCompaniesItem:
    """
    Attributes:
        domain (str): A company domain, like 'example.com'.
        importance_out_of_10 (int | None | Unset): How valuable this company is to you, from 1 (barely relevant) to 10
            (exactly your ideal customer). Higher values shape the lookalike groupings more strongly. Omit to weight all
            companies equally.
    """

    domain: str
    importance_out_of_10: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        importance_out_of_10: int | None | Unset
        if isinstance(self.importance_out_of_10, Unset):
            importance_out_of_10 = UNSET
        else:
            importance_out_of_10 = self.importance_out_of_10

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
            }
        )
        if importance_out_of_10 is not UNSET:
            field_dict["importanceOutOf10"] = importance_out_of_10

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        def _parse_importance_out_of_10(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        importance_out_of_10 = _parse_importance_out_of_10(d.pop("importanceOutOf10", UNSET))

        lookalikes_trigger_body_companies_item = cls(
            domain=domain,
            importance_out_of_10=importance_out_of_10,
        )

        lookalikes_trigger_body_companies_item.additional_properties = d
        return lookalikes_trigger_body_companies_item

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
