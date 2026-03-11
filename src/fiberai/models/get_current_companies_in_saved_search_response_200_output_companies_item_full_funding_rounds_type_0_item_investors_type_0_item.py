from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0ItemInvestorsType0Item",
)


@_attrs_define
class GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemFullFundingRoundsType0ItemInvestorsType0Item:
    """
    Attributes:
        is_lead (bool | None | Unset):
        investor_name (None | str | Unset):
        investor_type (None | str | Unset):
        investor_domain (None | str | Unset):
        investor_categories (list[str] | None | Unset):
        investor_linkedin_url (None | str | Unset):
        investor_linkedin_org_id (None | str | Unset):
    """

    is_lead: bool | None | Unset = UNSET
    investor_name: None | str | Unset = UNSET
    investor_type: None | str | Unset = UNSET
    investor_domain: None | str | Unset = UNSET
    investor_categories: list[str] | None | Unset = UNSET
    investor_linkedin_url: None | str | Unset = UNSET
    investor_linkedin_org_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_lead: bool | None | Unset
        if isinstance(self.is_lead, Unset):
            is_lead = UNSET
        else:
            is_lead = self.is_lead

        investor_name: None | str | Unset
        if isinstance(self.investor_name, Unset):
            investor_name = UNSET
        else:
            investor_name = self.investor_name

        investor_type: None | str | Unset
        if isinstance(self.investor_type, Unset):
            investor_type = UNSET
        else:
            investor_type = self.investor_type

        investor_domain: None | str | Unset
        if isinstance(self.investor_domain, Unset):
            investor_domain = UNSET
        else:
            investor_domain = self.investor_domain

        investor_categories: list[str] | None | Unset
        if isinstance(self.investor_categories, Unset):
            investor_categories = UNSET
        elif isinstance(self.investor_categories, list):
            investor_categories = self.investor_categories

        else:
            investor_categories = self.investor_categories

        investor_linkedin_url: None | str | Unset
        if isinstance(self.investor_linkedin_url, Unset):
            investor_linkedin_url = UNSET
        else:
            investor_linkedin_url = self.investor_linkedin_url

        investor_linkedin_org_id: None | str | Unset
        if isinstance(self.investor_linkedin_org_id, Unset):
            investor_linkedin_org_id = UNSET
        else:
            investor_linkedin_org_id = self.investor_linkedin_org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_lead is not UNSET:
            field_dict["is_lead"] = is_lead
        if investor_name is not UNSET:
            field_dict["investor_name"] = investor_name
        if investor_type is not UNSET:
            field_dict["investor_type"] = investor_type
        if investor_domain is not UNSET:
            field_dict["investor_domain"] = investor_domain
        if investor_categories is not UNSET:
            field_dict["investor_categories"] = investor_categories
        if investor_linkedin_url is not UNSET:
            field_dict["investor_linkedin_url"] = investor_linkedin_url
        if investor_linkedin_org_id is not UNSET:
            field_dict["investor_linkedin_org_id"] = investor_linkedin_org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_is_lead(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_lead = _parse_is_lead(d.pop("is_lead", UNSET))

        def _parse_investor_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_name = _parse_investor_name(d.pop("investor_name", UNSET))

        def _parse_investor_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_type = _parse_investor_type(d.pop("investor_type", UNSET))

        def _parse_investor_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_domain = _parse_investor_domain(d.pop("investor_domain", UNSET))

        def _parse_investor_categories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investor_categories_type_0 = cast(list[str], data)

                return investor_categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        investor_categories = _parse_investor_categories(d.pop("investor_categories", UNSET))

        def _parse_investor_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_linkedin_url = _parse_investor_linkedin_url(d.pop("investor_linkedin_url", UNSET))

        def _parse_investor_linkedin_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_linkedin_org_id = _parse_investor_linkedin_org_id(d.pop("investor_linkedin_org_id", UNSET))

        get_current_companies_in_saved_search_response_200_output_companies_item_full_funding_rounds_type_0_item_investors_type_0_item = cls(
            is_lead=is_lead,
            investor_name=investor_name,
            investor_type=investor_type,
            investor_domain=investor_domain,
            investor_categories=investor_categories,
            investor_linkedin_url=investor_linkedin_url,
            investor_linkedin_org_id=investor_linkedin_org_id,
        )

        get_current_companies_in_saved_search_response_200_output_companies_item_full_funding_rounds_type_0_item_investors_type_0_item.additional_properties = d
        return get_current_companies_in_saved_search_response_200_output_companies_item_full_funding_rounds_type_0_item_investors_type_0_item

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
