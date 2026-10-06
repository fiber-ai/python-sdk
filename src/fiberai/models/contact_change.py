from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_change_to_employment_types_type_0_item import ContactChangeToEmploymentTypesType0Item
from ..models.contact_change_to_seniority_levels_type_0_item import ContactChangeToSeniorityLevelsType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactChange")


@_attrs_define
class ContactChange:
    """
    Attributes:
        entity_type (Literal['person']):
        type_ (Literal['person_contact_change']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        to_companies (list[str] | None | Unset): Only alert if they moved TO one of these companies (domains or slugs).
            Omit for any.
        from_companies (list[str] | None | Unset): Only alert if they moved FROM one of these companies. Omit for any.
        to_title_keywords (list[str] | None | Unset): Only alert if their title at the new company contains one of these
            keywords.
        to_seniority_levels (list[ContactChangeToSeniorityLevelsType0Item] | None | Unset): Only alert if their
            seniority at the new company is one of these levels.
        to_employment_types (list[ContactChangeToEmploymentTypesType0Item] | None | Unset): Only alert for these
            employment types at the new company. Omit for any.
    """

    entity_type: Literal["person"]
    type_: Literal["person_contact_change"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    to_companies: list[str] | None | Unset = UNSET
    from_companies: list[str] | None | Unset = UNSET
    to_title_keywords: list[str] | None | Unset = UNSET
    to_seniority_levels: list[ContactChangeToSeniorityLevelsType0Item] | None | Unset = UNSET
    to_employment_types: list[ContactChangeToEmploymentTypesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type

        type_ = self.type_

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

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

        to_title_keywords: list[str] | None | Unset
        if isinstance(self.to_title_keywords, Unset):
            to_title_keywords = UNSET
        elif isinstance(self.to_title_keywords, list):
            to_title_keywords = self.to_title_keywords

        else:
            to_title_keywords = self.to_title_keywords

        to_seniority_levels: list[str] | None | Unset
        if isinstance(self.to_seniority_levels, Unset):
            to_seniority_levels = UNSET
        elif isinstance(self.to_seniority_levels, list):
            to_seniority_levels = []
            for to_seniority_levels_type_0_item_data in self.to_seniority_levels:
                to_seniority_levels_type_0_item = to_seniority_levels_type_0_item_data.value
                to_seniority_levels.append(to_seniority_levels_type_0_item)

        else:
            to_seniority_levels = self.to_seniority_levels

        to_employment_types: list[str] | None | Unset
        if isinstance(self.to_employment_types, Unset):
            to_employment_types = UNSET
        elif isinstance(self.to_employment_types, list):
            to_employment_types = []
            for to_employment_types_type_0_item_data in self.to_employment_types:
                to_employment_types_type_0_item = to_employment_types_type_0_item_data.value
                to_employment_types.append(to_employment_types_type_0_item)

        else:
            to_employment_types = self.to_employment_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityType": entity_type,
                "type": type_,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if to_companies is not UNSET:
            field_dict["toCompanies"] = to_companies
        if from_companies is not UNSET:
            field_dict["fromCompanies"] = from_companies
        if to_title_keywords is not UNSET:
            field_dict["toTitleKeywords"] = to_title_keywords
        if to_seniority_levels is not UNSET:
            field_dict["toSeniorityLevels"] = to_seniority_levels
        if to_employment_types is not UNSET:
            field_dict["toEmploymentTypes"] = to_employment_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_type = cast(Literal["person"], d.pop("entityType"))
        if entity_type != "person":
            raise ValueError(f"entityType must match const 'person', got '{entity_type}'")

        type_ = cast(Literal["person_contact_change"], d.pop("type"))
        if type_ != "person_contact_change":
            raise ValueError(f"type must match const 'person_contact_change', got '{type_}'")

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

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

        def _parse_to_title_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_title_keywords_type_0 = cast(list[str], data)

                return to_title_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        to_title_keywords = _parse_to_title_keywords(d.pop("toTitleKeywords", UNSET))

        def _parse_to_seniority_levels(data: object) -> list[ContactChangeToSeniorityLevelsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_seniority_levels_type_0 = []
                _to_seniority_levels_type_0 = data
                for to_seniority_levels_type_0_item_data in _to_seniority_levels_type_0:
                    to_seniority_levels_type_0_item = ContactChangeToSeniorityLevelsType0Item(
                        to_seniority_levels_type_0_item_data
                    )

                    to_seniority_levels_type_0.append(to_seniority_levels_type_0_item)

                return to_seniority_levels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContactChangeToSeniorityLevelsType0Item] | None | Unset, data)

        to_seniority_levels = _parse_to_seniority_levels(d.pop("toSeniorityLevels", UNSET))

        def _parse_to_employment_types(data: object) -> list[ContactChangeToEmploymentTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_employment_types_type_0 = []
                _to_employment_types_type_0 = data
                for to_employment_types_type_0_item_data in _to_employment_types_type_0:
                    to_employment_types_type_0_item = ContactChangeToEmploymentTypesType0Item(
                        to_employment_types_type_0_item_data
                    )

                    to_employment_types_type_0.append(to_employment_types_type_0_item)

                return to_employment_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContactChangeToEmploymentTypesType0Item] | None | Unset, data)

        to_employment_types = _parse_to_employment_types(d.pop("toEmploymentTypes", UNSET))

        contact_change = cls(
            entity_type=entity_type,
            type_=type_,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            to_companies=to_companies,
            from_companies=from_companies,
            to_title_keywords=to_title_keywords,
            to_seniority_levels=to_seniority_levels,
            to_employment_types=to_employment_types,
        )

        contact_change.additional_properties = d
        return contact_change

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
