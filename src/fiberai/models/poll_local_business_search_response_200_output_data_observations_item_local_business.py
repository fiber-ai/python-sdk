from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PollLocalBusinessSearchResponse200OutputDataObservationsItemLocalBusiness")


@_attrs_define
class PollLocalBusinessSearchResponse200OutputDataObservationsItemLocalBusiness:
    """
    Attributes:
        company_name (str):
        domain (None | str | Unset):
        city (None | str | Unset):
        state (None | str | Unset):
        state_code (None | str | Unset):
        country_name (None | str | Unset):
        country_3_letter_code (None | str | Unset):
        address (None | str | Unset):
        context (None | str | Unset):
    """

    company_name: str
    domain: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    state_code: None | str | Unset = UNSET
    country_name: None | str | Unset = UNSET
    country_3_letter_code: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    context: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        state_code: None | str | Unset
        if isinstance(self.state_code, Unset):
            state_code = UNSET
        else:
            state_code = self.state_code

        country_name: None | str | Unset
        if isinstance(self.country_name, Unset):
            country_name = UNSET
        else:
            country_name = self.country_name

        country_3_letter_code: None | str | Unset
        if isinstance(self.country_3_letter_code, Unset):
            country_3_letter_code = UNSET
        else:
            country_3_letter_code = self.country_3_letter_code

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyName": company_name,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code
        if country_name is not UNSET:
            field_dict["countryName"] = country_name
        if country_3_letter_code is not UNSET:
            field_dict["country3LetterCode"] = country_3_letter_code
        if address is not UNSET:
            field_dict["address"] = address
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_name = d.pop("companyName")

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_state_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_code = _parse_state_code(d.pop("stateCode", UNSET))

        def _parse_country_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_name = _parse_country_name(d.pop("countryName", UNSET))

        def _parse_country_3_letter_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_3_letter_code = _parse_country_3_letter_code(d.pop("country3LetterCode", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        poll_local_business_search_response_200_output_data_observations_item_local_business = cls(
            company_name=company_name,
            domain=domain,
            city=city,
            state=state,
            state_code=state_code,
            country_name=country_name,
            country_3_letter_code=country_3_letter_code,
            address=address,
            context=context,
        )

        poll_local_business_search_response_200_output_data_observations_item_local_business.additional_properties = d
        return poll_local_business_search_response_200_output_data_observations_item_local_business

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
