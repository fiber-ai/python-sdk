from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_salary_levels_type_0_item_levels_item import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemLevelsItem,
    )
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_salary_levels_type_0_item_titles_item import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemTitlesItem,
    )


T = TypeVar("T", bound="GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0Item")


@_attrs_define
class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0Item:
    """
    Attributes:
        name (str):
        slug (str):
        titles (list[GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemTitlesItem]):
        levels (list[GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemLevelsItem]):
        median_total_compensation_usd (float | None | Unset):
        submissions_last_24_months (int | None | Unset):
        min_level_total_compensation_usd (float | None | Unset):
        max_level_total_compensation_usd (float | None | Unset):
    """

    name: str
    slug: str
    titles: list[GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemTitlesItem]
    levels: list[GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemLevelsItem]
    median_total_compensation_usd: float | None | Unset = UNSET
    submissions_last_24_months: int | None | Unset = UNSET
    min_level_total_compensation_usd: float | None | Unset = UNSET
    max_level_total_compensation_usd: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        titles = []
        for titles_item_data in self.titles:
            titles_item = titles_item_data.to_dict()
            titles.append(titles_item)

        levels = []
        for levels_item_data in self.levels:
            levels_item = levels_item_data.to_dict()
            levels.append(levels_item)

        median_total_compensation_usd: float | None | Unset
        if isinstance(self.median_total_compensation_usd, Unset):
            median_total_compensation_usd = UNSET
        else:
            median_total_compensation_usd = self.median_total_compensation_usd

        submissions_last_24_months: int | None | Unset
        if isinstance(self.submissions_last_24_months, Unset):
            submissions_last_24_months = UNSET
        else:
            submissions_last_24_months = self.submissions_last_24_months

        min_level_total_compensation_usd: float | None | Unset
        if isinstance(self.min_level_total_compensation_usd, Unset):
            min_level_total_compensation_usd = UNSET
        else:
            min_level_total_compensation_usd = self.min_level_total_compensation_usd

        max_level_total_compensation_usd: float | None | Unset
        if isinstance(self.max_level_total_compensation_usd, Unset):
            max_level_total_compensation_usd = UNSET
        else:
            max_level_total_compensation_usd = self.max_level_total_compensation_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "titles": titles,
                "levels": levels,
            }
        )
        if median_total_compensation_usd is not UNSET:
            field_dict["median_total_compensation_usd"] = median_total_compensation_usd
        if submissions_last_24_months is not UNSET:
            field_dict["submissions_last_24_months"] = submissions_last_24_months
        if min_level_total_compensation_usd is not UNSET:
            field_dict["min_level_total_compensation_usd"] = min_level_total_compensation_usd
        if max_level_total_compensation_usd is not UNSET:
            field_dict["max_level_total_compensation_usd"] = max_level_total_compensation_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_salary_levels_type_0_item_levels_item import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemLevelsItem,  # noqa: PLC0415
        )
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_salary_levels_type_0_item_titles_item import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemTitlesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        titles = []
        _titles = d.pop("titles")
        for titles_item_data in _titles:
            titles_item = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemTitlesItem.from_dict(
                titles_item_data
            )

            titles.append(titles_item)

        levels = []
        _levels = d.pop("levels")
        for levels_item_data in _levels:
            levels_item = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanySalaryLevelsType0ItemLevelsItem.from_dict(
                levels_item_data
            )

            levels.append(levels_item)

        def _parse_median_total_compensation_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        median_total_compensation_usd = _parse_median_total_compensation_usd(
            d.pop("median_total_compensation_usd", UNSET)
        )

        def _parse_submissions_last_24_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        submissions_last_24_months = _parse_submissions_last_24_months(d.pop("submissions_last_24_months", UNSET))

        def _parse_min_level_total_compensation_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_level_total_compensation_usd = _parse_min_level_total_compensation_usd(
            d.pop("min_level_total_compensation_usd", UNSET)
        )

        def _parse_max_level_total_compensation_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_level_total_compensation_usd = _parse_max_level_total_compensation_usd(
            d.pop("max_level_total_compensation_usd", UNSET)
        )

        get_saved_search_run_companies_response_200_output_companies_item_company_salary_levels_type_0_item = cls(
            name=name,
            slug=slug,
            titles=titles,
            levels=levels,
            median_total_compensation_usd=median_total_compensation_usd,
            submissions_last_24_months=submissions_last_24_months,
            min_level_total_compensation_usd=min_level_total_compensation_usd,
            max_level_total_compensation_usd=max_level_total_compensation_usd,
        )

        get_saved_search_run_companies_response_200_output_companies_item_company_salary_levels_type_0_item.additional_properties = d
        return get_saved_search_run_companies_response_200_output_companies_item_company_salary_levels_type_0_item

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
