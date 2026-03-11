from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_full_funding_rounds_type_0_item_investors_type_0_item import (
        GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyFullFundingRoundsType0ItemInvestorsType0Item,
    )


T = TypeVar("T", bound="GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyFullFundingRoundsType0Item")


@_attrs_define
class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyFullFundingRoundsType0Item:
    """
    Attributes:
        investors (list[GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyFullFundingRoundsType0ItemInvesto
            rsType0Item] | None | Unset):
        round_city (None | str | Unset):
        round_date (None | str | Unset):
        round_type (None | str | Unset):
        round_state (None | str | Unset):
        investor_count (float | None | Unset):
        round_raised_usd (float | None | Unset):
        round_country_code (None | str | Unset):
        round_valuation_usd (float | None | Unset):
    """

    investors: (
        list[
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyFullFundingRoundsType0ItemInvestorsType0Item
        ]
        | None
        | Unset
    ) = UNSET
    round_city: None | str | Unset = UNSET
    round_date: None | str | Unset = UNSET
    round_type: None | str | Unset = UNSET
    round_state: None | str | Unset = UNSET
    investor_count: float | None | Unset = UNSET
    round_raised_usd: float | None | Unset = UNSET
    round_country_code: None | str | Unset = UNSET
    round_valuation_usd: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investors: list[dict[str, Any]] | None | Unset
        if isinstance(self.investors, Unset):
            investors = UNSET
        elif isinstance(self.investors, list):
            investors = []
            for investors_type_0_item_data in self.investors:
                investors_type_0_item = investors_type_0_item_data.to_dict()
                investors.append(investors_type_0_item)

        else:
            investors = self.investors

        round_city: None | str | Unset
        if isinstance(self.round_city, Unset):
            round_city = UNSET
        else:
            round_city = self.round_city

        round_date: None | str | Unset
        if isinstance(self.round_date, Unset):
            round_date = UNSET
        else:
            round_date = self.round_date

        round_type: None | str | Unset
        if isinstance(self.round_type, Unset):
            round_type = UNSET
        else:
            round_type = self.round_type

        round_state: None | str | Unset
        if isinstance(self.round_state, Unset):
            round_state = UNSET
        else:
            round_state = self.round_state

        investor_count: float | None | Unset
        if isinstance(self.investor_count, Unset):
            investor_count = UNSET
        else:
            investor_count = self.investor_count

        round_raised_usd: float | None | Unset
        if isinstance(self.round_raised_usd, Unset):
            round_raised_usd = UNSET
        else:
            round_raised_usd = self.round_raised_usd

        round_country_code: None | str | Unset
        if isinstance(self.round_country_code, Unset):
            round_country_code = UNSET
        else:
            round_country_code = self.round_country_code

        round_valuation_usd: float | None | Unset
        if isinstance(self.round_valuation_usd, Unset):
            round_valuation_usd = UNSET
        else:
            round_valuation_usd = self.round_valuation_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if investors is not UNSET:
            field_dict["investors"] = investors
        if round_city is not UNSET:
            field_dict["round_city"] = round_city
        if round_date is not UNSET:
            field_dict["round_date"] = round_date
        if round_type is not UNSET:
            field_dict["round_type"] = round_type
        if round_state is not UNSET:
            field_dict["round_state"] = round_state
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count
        if round_raised_usd is not UNSET:
            field_dict["round_raised_usd"] = round_raised_usd
        if round_country_code is not UNSET:
            field_dict["round_country_code"] = round_country_code
        if round_valuation_usd is not UNSET:
            field_dict["round_valuation_usd"] = round_valuation_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_saved_search_run_companies_response_200_output_companies_item_company_full_funding_rounds_type_0_item_investors_type_0_item import (
            GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyFullFundingRoundsType0ItemInvestorsType0Item,
        )

        d = dict(src_dict)

        def _parse_investors(
            data: object,
        ) -> (
            list[
                GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyFullFundingRoundsType0ItemInvestorsType0Item
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
                investors_type_0 = []
                _investors_type_0 = data
                for investors_type_0_item_data in _investors_type_0:
                    investors_type_0_item = GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyFullFundingRoundsType0ItemInvestorsType0Item.from_dict(
                        investors_type_0_item_data
                    )

                    investors_type_0.append(investors_type_0_item)

                return investors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    GetSavedSearchRunCompaniesResponse200OutputCompaniesItemCompanyFullFundingRoundsType0ItemInvestorsType0Item
                ]
                | None
                | Unset,
                data,
            )

        investors = _parse_investors(d.pop("investors", UNSET))

        def _parse_round_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        round_city = _parse_round_city(d.pop("round_city", UNSET))

        def _parse_round_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        round_date = _parse_round_date(d.pop("round_date", UNSET))

        def _parse_round_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        round_type = _parse_round_type(d.pop("round_type", UNSET))

        def _parse_round_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        round_state = _parse_round_state(d.pop("round_state", UNSET))

        def _parse_investor_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        investor_count = _parse_investor_count(d.pop("investor_count", UNSET))

        def _parse_round_raised_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        round_raised_usd = _parse_round_raised_usd(d.pop("round_raised_usd", UNSET))

        def _parse_round_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        round_country_code = _parse_round_country_code(d.pop("round_country_code", UNSET))

        def _parse_round_valuation_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        round_valuation_usd = _parse_round_valuation_usd(d.pop("round_valuation_usd", UNSET))

        get_saved_search_run_companies_response_200_output_companies_item_company_full_funding_rounds_type_0_item = cls(
            investors=investors,
            round_city=round_city,
            round_date=round_date,
            round_type=round_type,
            round_state=round_state,
            investor_count=investor_count,
            round_raised_usd=round_raised_usd,
            round_country_code=round_country_code,
            round_valuation_usd=round_valuation_usd,
        )

        get_saved_search_run_companies_response_200_output_companies_item_company_full_funding_rounds_type_0_item.additional_properties = d
        return get_saved_search_run_companies_response_200_output_companies_item_company_full_funding_rounds_type_0_item

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
