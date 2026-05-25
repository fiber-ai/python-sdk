from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonChangedCompany")


@_attrs_define
class PersonChangedCompany:
    """
    Attributes:
        type_ (Literal['person_changed_company']):
        entity_type (Literal['person']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        to_companies (list[str] | None | Unset): Only alert if they moved TO one of these companies (domains or slugs).
            Omit for any.
        from_companies (list[str] | None | Unset): Only alert if they moved FROM one of these companies. Omit for any.
    """

    type_: Literal["person_changed_company"]
    entity_type: Literal["person"]
    lookback_days: int | None | Unset = UNSET
    to_companies: list[str] | None | Unset = UNSET
    from_companies: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        to_companies: list[str] | None | Unset
        if isinstance(self.to_companies, Unset):
            to_companies = UNSET
        elif isinstance(self.to_companies, list):
            to_companies = self.to_companies

        else:
            to_companies = self.to_companies

        from_companies: list[str] | None | Unset
        if isinstance(self.from_companies, Unset):
            from_companies = UNSET
        elif isinstance(self.from_companies, list):
            from_companies = self.from_companies

        else:
            from_companies = self.from_companies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if to_companies is not UNSET:
            field_dict["toCompanies"] = to_companies
        if from_companies is not UNSET:
            field_dict["fromCompanies"] = from_companies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["person_changed_company"], d.pop("type"))
        if type_ != "person_changed_company":
            raise ValueError(f"type must match const 'person_changed_company', got '{type_}'")

        entity_type = cast(Literal["person"], d.pop("entityType"))
        if entity_type != "person":
            raise ValueError(f"entityType must match const 'person', got '{entity_type}'")

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        def _parse_to_companies(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_companies_type_0 = cast(list[str], data)

                return to_companies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        to_companies = _parse_to_companies(d.pop("toCompanies", UNSET))

        def _parse_from_companies(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                from_companies_type_0 = cast(list[str], data)

                return from_companies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        from_companies = _parse_from_companies(d.pop("fromCompanies", UNSET))

        person_changed_company = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            to_companies=to_companies,
            from_companies=from_companies,
        )

        person_changed_company.additional_properties = d
        return person_changed_company

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
