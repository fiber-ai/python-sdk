from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KitchenSinkBulkCompanyResponse200OutputDataItemItemSalaryLevelsType0ItemTitlesItem")


@_attrs_define
class KitchenSinkBulkCompanyResponse200OutputDataItemItemSalaryLevelsType0ItemTitlesItem:
    """
    Attributes:
        name (str):
        slug (None | str | Unset):
        total_compensation_usd (float | None | Unset):
        submission_count (int | None | Unset):
    """

    name: str
    slug: None | str | Unset = UNSET
    total_compensation_usd: float | None | Unset = UNSET
    submission_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        total_compensation_usd: float | None | Unset
        if isinstance(self.total_compensation_usd, Unset):
            total_compensation_usd = UNSET
        else:
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
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if total_compensation_usd is not UNSET:
            field_dict["total_compensation_usd"] = total_compensation_usd
        if submission_count is not UNSET:
            field_dict["submission_count"] = submission_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_total_compensation_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_compensation_usd = _parse_total_compensation_usd(d.pop("total_compensation_usd", UNSET))

        def _parse_submission_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        submission_count = _parse_submission_count(d.pop("submission_count", UNSET))

        kitchen_sink_bulk_company_response_200_output_data_item_item_salary_levels_type_0_item_titles_item = cls(
            name=name,
            slug=slug,
            total_compensation_usd=total_compensation_usd,
            submission_count=submission_count,
        )

        kitchen_sink_bulk_company_response_200_output_data_item_item_salary_levels_type_0_item_titles_item.additional_properties = d
        return kitchen_sink_bulk_company_response_200_output_data_item_item_salary_levels_type_0_item_titles_item

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
