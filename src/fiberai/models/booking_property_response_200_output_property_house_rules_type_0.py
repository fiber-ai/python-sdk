from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookingPropertyResponse200OutputPropertyHouseRulesType0")


@_attrs_define
class BookingPropertyResponse200OutputPropertyHouseRulesType0:
    """Published house rules for the property.

    Attributes:
        payment_methods (list[str]): Accepted payment methods.
        age_restriction (None | str | Unset): Age restriction policy, when published.
        children_policy (None | str | Unset): Children policy, when published.
        pets_policy (None | str | Unset): Pets policy, when published.
        smoking_policy (None | str | Unset): Smoking policy, when published.
        parties_policy (None | str | Unset): Parties and events policy, when published.
        group_policy (None | str | Unset): Group booking policy, when published.
        is_cash_accepted (bool | None | Unset): True when the property accepts cash.
    """

    payment_methods: list[str]
    age_restriction: None | str | Unset = UNSET
    children_policy: None | str | Unset = UNSET
    pets_policy: None | str | Unset = UNSET
    smoking_policy: None | str | Unset = UNSET
    parties_policy: None | str | Unset = UNSET
    group_policy: None | str | Unset = UNSET
    is_cash_accepted: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_methods = self.payment_methods

        age_restriction: None | str | Unset
        if isinstance(self.age_restriction, Unset):
            age_restriction = UNSET
        else:
            age_restriction = self.age_restriction

        children_policy: None | str | Unset
        if isinstance(self.children_policy, Unset):
            children_policy = UNSET
        else:
            children_policy = self.children_policy

        pets_policy: None | str | Unset
        if isinstance(self.pets_policy, Unset):
            pets_policy = UNSET
        else:
            pets_policy = self.pets_policy

        smoking_policy: None | str | Unset
        if isinstance(self.smoking_policy, Unset):
            smoking_policy = UNSET
        else:
            smoking_policy = self.smoking_policy

        parties_policy: None | str | Unset
        if isinstance(self.parties_policy, Unset):
            parties_policy = UNSET
        else:
            parties_policy = self.parties_policy

        group_policy: None | str | Unset
        if isinstance(self.group_policy, Unset):
            group_policy = UNSET
        else:
            group_policy = self.group_policy

        is_cash_accepted: bool | None | Unset
        if isinstance(self.is_cash_accepted, Unset):
            is_cash_accepted = UNSET
        else:
            is_cash_accepted = self.is_cash_accepted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentMethods": payment_methods,
            }
        )
        if age_restriction is not UNSET:
            field_dict["ageRestriction"] = age_restriction
        if children_policy is not UNSET:
            field_dict["childrenPolicy"] = children_policy
        if pets_policy is not UNSET:
            field_dict["petsPolicy"] = pets_policy
        if smoking_policy is not UNSET:
            field_dict["smokingPolicy"] = smoking_policy
        if parties_policy is not UNSET:
            field_dict["partiesPolicy"] = parties_policy
        if group_policy is not UNSET:
            field_dict["groupPolicy"] = group_policy
        if is_cash_accepted is not UNSET:
            field_dict["isCashAccepted"] = is_cash_accepted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_methods = cast(list[str], d.pop("paymentMethods"))

        def _parse_age_restriction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        age_restriction = _parse_age_restriction(d.pop("ageRestriction", UNSET))

        def _parse_children_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        children_policy = _parse_children_policy(d.pop("childrenPolicy", UNSET))

        def _parse_pets_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pets_policy = _parse_pets_policy(d.pop("petsPolicy", UNSET))

        def _parse_smoking_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        smoking_policy = _parse_smoking_policy(d.pop("smokingPolicy", UNSET))

        def _parse_parties_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parties_policy = _parse_parties_policy(d.pop("partiesPolicy", UNSET))

        def _parse_group_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_policy = _parse_group_policy(d.pop("groupPolicy", UNSET))

        def _parse_is_cash_accepted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_cash_accepted = _parse_is_cash_accepted(d.pop("isCashAccepted", UNSET))

        booking_property_response_200_output_property_house_rules_type_0 = cls(
            payment_methods=payment_methods,
            age_restriction=age_restriction,
            children_policy=children_policy,
            pets_policy=pets_policy,
            smoking_policy=smoking_policy,
            parties_policy=parties_policy,
            group_policy=group_policy,
            is_cash_accepted=is_cash_accepted,
        )

        booking_property_response_200_output_property_house_rules_type_0.additional_properties = d
        return booking_property_response_200_output_property_house_rules_type_0

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
