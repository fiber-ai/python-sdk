from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_lookup_trigger_body_people_item_type_1_input_type import (
    GithubLookupTriggerBodyPeopleItemType1InputType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubLookupTriggerBodyPeopleItemType1")


@_attrs_define
class GithubLookupTriggerBodyPeopleItemType1:
    """
    Attributes:
        input_type (GithubLookupTriggerBodyPeopleItemType1InputType):
        linkedin_user_id (str): LinkedIn numeric user ID
        external_id (None | str | Unset): Your own ID to join results back
    """

    input_type: GithubLookupTriggerBodyPeopleItemType1InputType
    linkedin_user_id: str
    external_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_type = self.input_type.value

        linkedin_user_id = self.linkedin_user_id

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
                "linkedinUserId": linkedin_user_id,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_type = GithubLookupTriggerBodyPeopleItemType1InputType(d.pop("inputType"))

        linkedin_user_id = d.pop("linkedinUserId")

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        github_lookup_trigger_body_people_item_type_1 = cls(
            input_type=input_type,
            linkedin_user_id=linkedin_user_id,
            external_id=external_id,
        )

        github_lookup_trigger_body_people_item_type_1.additional_properties = d
        return github_lookup_trigger_body_people_item_type_1

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
