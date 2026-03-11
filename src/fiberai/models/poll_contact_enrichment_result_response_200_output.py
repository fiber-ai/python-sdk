from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.poll_contact_enrichment_result_response_200_output_profile import (
        PollContactEnrichmentResultResponse200OutputProfile,
    )


T = TypeVar("T", bound="PollContactEnrichmentResultResponse200Output")


@_attrs_define
class PollContactEnrichmentResultResponse200Output:
    """
    Attributes:
        profile (PollContactEnrichmentResultResponse200OutputProfile):
        done (bool): Whether the enrichment is completed or not.
    """

    profile: PollContactEnrichmentResultResponse200OutputProfile
    done: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile = self.profile.to_dict()

        done = self.done

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profile": profile,
                "done": done,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_contact_enrichment_result_response_200_output_profile import (
            PollContactEnrichmentResultResponse200OutputProfile,
        )

        d = dict(src_dict)
        profile = PollContactEnrichmentResultResponse200OutputProfile.from_dict(d.pop("profile"))

        done = d.pop("done")

        poll_contact_enrichment_result_response_200_output = cls(
            profile=profile,
            done=done,
        )

        poll_contact_enrichment_result_response_200_output.additional_properties = d
        return poll_contact_enrichment_result_response_200_output

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
