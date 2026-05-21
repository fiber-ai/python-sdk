from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_live_enrich_response_200_profile_found_and_enriched_profile_verifications_type_0_verification_types_type_0_item import (
        ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVerificationsType0VerificationTypesType0Item,
    )


T = TypeVar("T", bound="ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVerificationsType0")


@_attrs_define
class ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVerificationsType0:
    """
    Attributes:
        is_verified (bool | None | Unset):
        joined_date (None | str | Unset):
        verification_types
            (list[ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVerificationsType0VerificationTypesType0Item] |
            None | Unset):
    """

    is_verified: bool | None | Unset = UNSET
    joined_date: None | str | Unset = UNSET
    verification_types: (
        list[ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVerificationsType0VerificationTypesType0Item]
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_verified: bool | None | Unset
        if isinstance(self.is_verified, Unset):
            is_verified = UNSET
        else:
            is_verified = self.is_verified

        joined_date: None | str | Unset
        if isinstance(self.joined_date, Unset):
            joined_date = UNSET
        else:
            joined_date = self.joined_date

        verification_types: list[dict[str, Any]] | None | Unset
        if isinstance(self.verification_types, Unset):
            verification_types = UNSET
        elif isinstance(self.verification_types, list):
            verification_types = []
            for verification_types_type_0_item_data in self.verification_types:
                verification_types_type_0_item = verification_types_type_0_item_data.to_dict()
                verification_types.append(verification_types_type_0_item)

        else:
            verification_types = self.verification_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if joined_date is not UNSET:
            field_dict["joined_date"] = joined_date
        if verification_types is not UNSET:
            field_dict["verification_types"] = verification_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_live_enrich_response_200_profile_found_and_enriched_profile_verifications_type_0_verification_types_type_0_item import (
            ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVerificationsType0VerificationTypesType0Item,
        )

        d = dict(src_dict)

        def _parse_is_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_verified = _parse_is_verified(d.pop("is_verified", UNSET))

        def _parse_joined_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        joined_date = _parse_joined_date(d.pop("joined_date", UNSET))

        def _parse_verification_types(
            data: object,
        ) -> (
            list[ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVerificationsType0VerificationTypesType0Item]
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
                verification_types_type_0 = []
                _verification_types_type_0 = data
                for verification_types_type_0_item_data in _verification_types_type_0:
                    verification_types_type_0_item = ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVerificationsType0VerificationTypesType0Item.from_dict(
                        verification_types_type_0_item_data
                    )

                    verification_types_type_0.append(verification_types_type_0_item)

                return verification_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileVerificationsType0VerificationTypesType0Item
                ]
                | None
                | Unset,
                data,
            )

        verification_types = _parse_verification_types(d.pop("verification_types", UNSET))

        profile_live_enrich_response_200_profile_found_and_enriched_profile_verifications_type_0 = cls(
            is_verified=is_verified,
            joined_date=joined_date,
            verification_types=verification_types,
        )

        profile_live_enrich_response_200_profile_found_and_enriched_profile_verifications_type_0.additional_properties = d
        return profile_live_enrich_response_200_profile_found_and_enriched_profile_verifications_type_0

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
