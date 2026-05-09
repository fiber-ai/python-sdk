from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.twitter_handle_to_linkedin_url_response_200_output_x_profile_type_0 import (
        TwitterHandleToLinkedinUrlResponse200OutputXProfileType0,
    )


T = TypeVar("T", bound="TwitterHandleToLinkedinUrlResponse200Output")


@_attrs_define
class TwitterHandleToLinkedinUrlResponse200Output:
    """
    Attributes:
        confidence_out_of_10 (int): Match confidence on a 0-10 scale. 0 means no confident match was found; higher
            values indicate stronger evidence.
        linked_in_url (None | str | Unset): LinkedIn profile URL if a match was found, else null.
        rationale (None | str | Unset): Short explanation of why this LinkedIn profile was matched. Null for high-
            confidence direct matches and when no match was found.
        x_profile (None | TwitterHandleToLinkedinUrlResponse200OutputXProfileType0 | Unset): Public snapshot of the X
            profile that was used for matching (null if the X profile could not be fetched).
    """

    confidence_out_of_10: int
    linked_in_url: None | str | Unset = UNSET
    rationale: None | str | Unset = UNSET
    x_profile: None | TwitterHandleToLinkedinUrlResponse200OutputXProfileType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.twitter_handle_to_linkedin_url_response_200_output_x_profile_type_0 import (
            TwitterHandleToLinkedinUrlResponse200OutputXProfileType0,
        )

        confidence_out_of_10 = self.confidence_out_of_10

        linked_in_url: None | str | Unset
        if isinstance(self.linked_in_url, Unset):
            linked_in_url = UNSET
        else:
            linked_in_url = self.linked_in_url

        rationale: None | str | Unset
        if isinstance(self.rationale, Unset):
            rationale = UNSET
        else:
            rationale = self.rationale

        x_profile: dict[str, Any] | None | Unset
        if isinstance(self.x_profile, Unset):
            x_profile = UNSET
        elif isinstance(self.x_profile, TwitterHandleToLinkedinUrlResponse200OutputXProfileType0):
            x_profile = self.x_profile.to_dict()
        else:
            x_profile = self.x_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidenceOutOf10": confidence_out_of_10,
            }
        )
        if linked_in_url is not UNSET:
            field_dict["linkedInUrl"] = linked_in_url
        if rationale is not UNSET:
            field_dict["rationale"] = rationale
        if x_profile is not UNSET:
            field_dict["xProfile"] = x_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.twitter_handle_to_linkedin_url_response_200_output_x_profile_type_0 import (
            TwitterHandleToLinkedinUrlResponse200OutputXProfileType0,
        )

        d = dict(src_dict)
        confidence_out_of_10 = d.pop("confidenceOutOf10")

        def _parse_linked_in_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linked_in_url = _parse_linked_in_url(d.pop("linkedInUrl", UNSET))

        def _parse_rationale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rationale = _parse_rationale(d.pop("rationale", UNSET))

        def _parse_x_profile(data: object) -> None | TwitterHandleToLinkedinUrlResponse200OutputXProfileType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                x_profile_type_0 = TwitterHandleToLinkedinUrlResponse200OutputXProfileType0.from_dict(data)

                return x_profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TwitterHandleToLinkedinUrlResponse200OutputXProfileType0 | Unset, data)

        x_profile = _parse_x_profile(d.pop("xProfile", UNSET))

        twitter_handle_to_linkedin_url_response_200_output = cls(
            confidence_out_of_10=confidence_out_of_10,
            linked_in_url=linked_in_url,
            rationale=rationale,
            x_profile=x_profile,
        )

        twitter_handle_to_linkedin_url_response_200_output.additional_properties = d
        return twitter_handle_to_linkedin_url_response_200_output

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
