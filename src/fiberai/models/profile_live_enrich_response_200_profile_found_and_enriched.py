from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_live_enrich_response_200_profile_found_and_enriched_profile import (
        ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfile,
    )


T = TypeVar("T", bound="ProfileLiveEnrichResponse200ProfileFoundAndEnriched")


@_attrs_define
class ProfileLiveEnrichResponse200ProfileFoundAndEnriched:
    """The profile was found and enriched

    Attributes:
        found (bool):
        profile (ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfile):
        is_cached_404 (bool | None | Unset): True when the profile is not found but we have the cached data in our
            database. In this case, you won't be charged.
    """

    found: bool
    profile: ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfile
    is_cached_404: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        found = self.found

        profile = self.profile.to_dict()

        is_cached_404: bool | None | Unset
        if isinstance(self.is_cached_404, Unset):
            is_cached_404 = UNSET
        else:
            is_cached_404 = self.is_cached_404

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "found": found,
                "profile": profile,
            }
        )
        if is_cached_404 is not UNSET:
            field_dict["isCached404"] = is_cached_404

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_live_enrich_response_200_profile_found_and_enriched_profile import (
            ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfile,
        )

        d = dict(src_dict)
        found = d.pop("found")

        profile = ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfile.from_dict(d.pop("profile"))

        def _parse_is_cached_404(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_cached_404 = _parse_is_cached_404(d.pop("isCached404", UNSET))

        profile_live_enrich_response_200_profile_found_and_enriched = cls(
            found=found,
            profile=profile,
            is_cached_404=is_cached_404,
        )

        profile_live_enrich_response_200_profile_found_and_enriched.additional_properties = d
        return profile_live_enrich_response_200_profile_found_and_enriched

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
