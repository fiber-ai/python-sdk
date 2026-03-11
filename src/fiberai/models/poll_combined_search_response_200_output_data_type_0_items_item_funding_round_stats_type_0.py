from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_funding_round_stats_type_0_individual_investor_stats_type_0_item import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemFundingRoundStatsType0IndividualInvestorStatsType0Item,
    )


T = TypeVar("T", bound="PollCombinedSearchResponse200OutputDataType0ItemsItemFundingRoundStatsType0")


@_attrs_define
class PollCombinedSearchResponse200OutputDataType0ItemsItemFundingRoundStatsType0:
    """
    Attributes:
        round_count (float | None | Unset):
        total_raised_usd (float | None | Unset):
        peak_valuation_usd (float | None | Unset):
        unique_investor_count (float | None | Unset):
        individual_investor_stats (list[PollCombinedSearchResponse200OutputDataType0ItemsItemFundingRoundStatsType0Indiv
            idualInvestorStatsType0Item] | None | Unset):
        unique_personal_investor_count (float | None | Unset):
        unique_organizational_investor_count (float | None | Unset):
    """

    round_count: float | None | Unset = UNSET
    total_raised_usd: float | None | Unset = UNSET
    peak_valuation_usd: float | None | Unset = UNSET
    unique_investor_count: float | None | Unset = UNSET
    individual_investor_stats: (
        list[
            PollCombinedSearchResponse200OutputDataType0ItemsItemFundingRoundStatsType0IndividualInvestorStatsType0Item
        ]
        | None
        | Unset
    ) = UNSET
    unique_personal_investor_count: float | None | Unset = UNSET
    unique_organizational_investor_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        round_count: float | None | Unset
        if isinstance(self.round_count, Unset):
            round_count = UNSET
        else:
            round_count = self.round_count

        total_raised_usd: float | None | Unset
        if isinstance(self.total_raised_usd, Unset):
            total_raised_usd = UNSET
        else:
            total_raised_usd = self.total_raised_usd

        peak_valuation_usd: float | None | Unset
        if isinstance(self.peak_valuation_usd, Unset):
            peak_valuation_usd = UNSET
        else:
            peak_valuation_usd = self.peak_valuation_usd

        unique_investor_count: float | None | Unset
        if isinstance(self.unique_investor_count, Unset):
            unique_investor_count = UNSET
        else:
            unique_investor_count = self.unique_investor_count

        individual_investor_stats: list[dict[str, Any]] | None | Unset
        if isinstance(self.individual_investor_stats, Unset):
            individual_investor_stats = UNSET
        elif isinstance(self.individual_investor_stats, list):
            individual_investor_stats = []
            for individual_investor_stats_type_0_item_data in self.individual_investor_stats:
                individual_investor_stats_type_0_item = individual_investor_stats_type_0_item_data.to_dict()
                individual_investor_stats.append(individual_investor_stats_type_0_item)

        else:
            individual_investor_stats = self.individual_investor_stats

        unique_personal_investor_count: float | None | Unset
        if isinstance(self.unique_personal_investor_count, Unset):
            unique_personal_investor_count = UNSET
        else:
            unique_personal_investor_count = self.unique_personal_investor_count

        unique_organizational_investor_count: float | None | Unset
        if isinstance(self.unique_organizational_investor_count, Unset):
            unique_organizational_investor_count = UNSET
        else:
            unique_organizational_investor_count = self.unique_organizational_investor_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if round_count is not UNSET:
            field_dict["round_count"] = round_count
        if total_raised_usd is not UNSET:
            field_dict["total_raised_usd"] = total_raised_usd
        if peak_valuation_usd is not UNSET:
            field_dict["peak_valuation_usd"] = peak_valuation_usd
        if unique_investor_count is not UNSET:
            field_dict["unique_investor_count"] = unique_investor_count
        if individual_investor_stats is not UNSET:
            field_dict["individual_investor_stats"] = individual_investor_stats
        if unique_personal_investor_count is not UNSET:
            field_dict["unique_personal_investor_count"] = unique_personal_investor_count
        if unique_organizational_investor_count is not UNSET:
            field_dict["unique_organizational_investor_count"] = unique_organizational_investor_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_funding_round_stats_type_0_individual_investor_stats_type_0_item import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemFundingRoundStatsType0IndividualInvestorStatsType0Item,
        )

        d = dict(src_dict)

        def _parse_round_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        round_count = _parse_round_count(d.pop("round_count", UNSET))

        def _parse_total_raised_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_raised_usd = _parse_total_raised_usd(d.pop("total_raised_usd", UNSET))

        def _parse_peak_valuation_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        peak_valuation_usd = _parse_peak_valuation_usd(d.pop("peak_valuation_usd", UNSET))

        def _parse_unique_investor_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unique_investor_count = _parse_unique_investor_count(d.pop("unique_investor_count", UNSET))

        def _parse_individual_investor_stats(
            data: object,
        ) -> (
            list[
                PollCombinedSearchResponse200OutputDataType0ItemsItemFundingRoundStatsType0IndividualInvestorStatsType0Item
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                individual_investor_stats_type_0 = []
                _individual_investor_stats_type_0 = data
                for individual_investor_stats_type_0_item_data in _individual_investor_stats_type_0:
                    individual_investor_stats_type_0_item = PollCombinedSearchResponse200OutputDataType0ItemsItemFundingRoundStatsType0IndividualInvestorStatsType0Item.from_dict(
                        individual_investor_stats_type_0_item_data
                    )

                    individual_investor_stats_type_0.append(individual_investor_stats_type_0_item)

                return individual_investor_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    PollCombinedSearchResponse200OutputDataType0ItemsItemFundingRoundStatsType0IndividualInvestorStatsType0Item
                ]
                | None
                | Unset,
                data,
            )

        individual_investor_stats = _parse_individual_investor_stats(d.pop("individual_investor_stats", UNSET))

        def _parse_unique_personal_investor_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unique_personal_investor_count = _parse_unique_personal_investor_count(
            d.pop("unique_personal_investor_count", UNSET)
        )

        def _parse_unique_organizational_investor_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unique_organizational_investor_count = _parse_unique_organizational_investor_count(
            d.pop("unique_organizational_investor_count", UNSET)
        )

        poll_combined_search_response_200_output_data_type_0_items_item_funding_round_stats_type_0 = cls(
            round_count=round_count,
            total_raised_usd=total_raised_usd,
            peak_valuation_usd=peak_valuation_usd,
            unique_investor_count=unique_investor_count,
            individual_investor_stats=individual_investor_stats,
            unique_personal_investor_count=unique_personal_investor_count,
            unique_organizational_investor_count=unique_organizational_investor_count,
        )

        poll_combined_search_response_200_output_data_type_0_items_item_funding_round_stats_type_0.additional_properties = d
        return poll_combined_search_response_200_output_data_type_0_items_item_funding_round_stats_type_0

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
