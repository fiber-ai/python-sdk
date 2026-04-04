from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkProfilePicResponse200OutputDataItem")


@_attrs_define
class BulkProfilePicResponse200OutputDataItem:
    """
    Attributes:
        linkedin_url (str): The linkedin URL of the profile
        profile_pic_found (bool):
        profile_pic (None | str): The profile pic of the profile
    """

    linkedin_url: str
    profile_pic_found: bool
    profile_pic: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url = self.linkedin_url

        profile_pic_found = self.profile_pic_found

        profile_pic: None | str
        profile_pic = self.profile_pic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinUrl": linkedin_url,
                "profilePicFound": profile_pic_found,
                "profilePic": profile_pic,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linkedin_url = d.pop("linkedinUrl")

        profile_pic_found = d.pop("profilePicFound")

        def _parse_profile_pic(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_pic = _parse_profile_pic(d.pop("profilePic"))

        bulk_profile_pic_response_200_output_data_item = cls(
            linkedin_url=linkedin_url,
            profile_pic_found=profile_pic_found,
            profile_pic=profile_pic,
        )

        bulk_profile_pic_response_200_output_data_item.additional_properties = d
        return bulk_profile_pic_response_200_output_data_item

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
