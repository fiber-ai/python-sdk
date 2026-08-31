from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_response_200_output_companies_item_revenue_estimate_type_0_value_usd import (
        PaginatedCombinedSearchResponse200OutputCompaniesItemRevenueEstimateType0ValueUsd,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchResponse200OutputCompaniesItemRevenueEstimateType0")


@_attrs_define
class PaginatedCombinedSearchResponse200OutputCompaniesItemRevenueEstimateType0:
    """
    Attributes:
        value_usd (PaginatedCombinedSearchResponse200OutputCompaniesItemRevenueEstimateType0ValueUsd):
        sources (list[str] | None | Unset):
        fiscal_year (int | None | Unset):
    """

    value_usd: PaginatedCombinedSearchResponse200OutputCompaniesItemRevenueEstimateType0ValueUsd
    sources: list[str] | None | Unset = UNSET
    fiscal_year: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_usd = self.value_usd.to_dict()

        sources: list[str] | None | Unset
        if isinstance(self.sources, Unset):
            sources = UNSET
        elif isinstance(self.sources, list):
            sources = self.sources

        else:
            sources = self.sources

        fiscal_year: int | None | Unset
        if isinstance(self.fiscal_year, Unset):
            fiscal_year = UNSET
        else:
            fiscal_year = self.fiscal_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value_usd": value_usd,
            }
        )
        if sources is not UNSET:
            field_dict["sources"] = sources
        if fiscal_year is not UNSET:
            field_dict["fiscal_year"] = fiscal_year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_response_200_output_companies_item_revenue_estimate_type_0_value_usd import (
            PaginatedCombinedSearchResponse200OutputCompaniesItemRevenueEstimateType0ValueUsd,  # noqa: PLC0415
        )

        d = dict(src_dict)
        value_usd = PaginatedCombinedSearchResponse200OutputCompaniesItemRevenueEstimateType0ValueUsd.from_dict(
            d.pop("value_usd")
        )

        def _parse_sources(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = cast(list[str], data)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        sources = _parse_sources(d.pop("sources", UNSET))

        def _parse_fiscal_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fiscal_year = _parse_fiscal_year(d.pop("fiscal_year", UNSET))

        paginated_combined_search_response_200_output_companies_item_revenue_estimate_type_0 = cls(
            value_usd=value_usd,
            sources=sources,
            fiscal_year=fiscal_year,
        )

        paginated_combined_search_response_200_output_companies_item_revenue_estimate_type_0.additional_properties = d
        return paginated_combined_search_response_200_output_companies_item_revenue_estimate_type_0

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
