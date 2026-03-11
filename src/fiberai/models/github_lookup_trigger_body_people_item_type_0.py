from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_lookup_trigger_body_people_item_type_0_input_type import (
    GithubLookupTriggerBodyPeopleItemType0InputType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubLookupTriggerBodyPeopleItemType0")


@_attrs_define
class GithubLookupTriggerBodyPeopleItemType0:
    """
    Attributes:
        input_type (GithubLookupTriggerBodyPeopleItemType0InputType):
        linkedin_url (str): LinkedIn URL, slug, or entity URN
        external_id (None | str | Unset): Your own ID to join results back
    """

    input_type: GithubLookupTriggerBodyPeopleItemType0InputType
    linkedin_url: str
    external_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_type = self.input_type.value

        linkedin_url = self.linkedin_url

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputType": input_type,
                "linkedinUrl": linkedin_url,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_type = GithubLookupTriggerBodyPeopleItemType0InputType(d.pop("inputType"))

        linkedin_url = d.pop("linkedinUrl")

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        github_lookup_trigger_body_people_item_type_0 = cls(
            input_type=input_type,
            linkedin_url=linkedin_url,
            external_id=external_id,
        )

        github_lookup_trigger_body_people_item_type_0.additional_properties = d
        return github_lookup_trigger_body_people_item_type_0

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
