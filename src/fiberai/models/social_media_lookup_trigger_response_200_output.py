from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SocialMediaLookupTriggerResponse200Output")


@_attrs_define
class SocialMediaLookupTriggerResponse200Output:
    """
    Attributes:
        social_media_finder_run_id (str): The ID of the social media finder run. Provide this to the polling endpoint to
            get results.
    """

    social_media_finder_run_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        social_media_finder_run_id = self.social_media_finder_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "socialMediaFinderRunId": social_media_finder_run_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        social_media_finder_run_id = d.pop("socialMediaFinderRunId")

        social_media_lookup_trigger_response_200_output = cls(
            social_media_finder_run_id=social_media_finder_run_id,
        )

        social_media_lookup_trigger_response_200_output.additional_properties = d
        return social_media_lookup_trigger_response_200_output

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
