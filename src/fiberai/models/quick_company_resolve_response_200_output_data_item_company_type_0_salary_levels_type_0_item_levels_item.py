from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuickCompanyResolveResponse200OutputDataItemCompanyType0SalaryLevelsType0ItemLevelsItem")


@_attrs_define
class QuickCompanyResolveResponse200OutputDataItemCompanyType0SalaryLevelsType0ItemLevelsItem:
    """
    Attributes:
        name (str):
        slug (str):
        order (int):
        total_compensation_usd (float):
        submission_count (int | None | Unset):
    """

    name: str
    slug: str
    order: int
    total_compensation_usd: float
    submission_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        order = self.order

        total_compensation_usd = self.total_compensation_usd

        submission_count: int | None | Unset
        if isinstance(self.submission_count, Unset):
            submission_count = UNSET
        else:
            submission_count = self.submission_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "order": order,
                "total_compensation_usd": total_compensation_usd,
            }
        )
        if submission_count is not UNSET:
            field_dict["submission_count"] = submission_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        order = d.pop("order")

        total_compensation_usd = d.pop("total_compensation_usd")

        def _parse_submission_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        submission_count = _parse_submission_count(d.pop("submission_count", UNSET))

        quick_company_resolve_response_200_output_data_item_company_type_0_salary_levels_type_0_item_levels_item = cls(
            name=name,
            slug=slug,
            order=order,
            total_compensation_usd=total_compensation_usd,
            submission_count=submission_count,
        )

        quick_company_resolve_response_200_output_data_item_company_type_0_salary_levels_type_0_item_levels_item.additional_properties = d
        return quick_company_resolve_response_200_output_data_item_company_type_0_salary_levels_type_0_item_levels_item

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
