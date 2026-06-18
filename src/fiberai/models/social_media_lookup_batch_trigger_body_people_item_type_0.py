from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_media_lookup_batch_trigger_body_people_item_type_0_input_type import (
    SocialMediaLookupBatchTriggerBodyPeopleItemType0InputType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialMediaLookupBatchTriggerBodyPeopleItemType0")


@_attrs_define
class SocialMediaLookupBatchTriggerBodyPeopleItemType0:
    """
    Attributes:
        input_type (SocialMediaLookupBatchTriggerBodyPeopleItemType0InputType):
        linkedin_url (str): LinkedIn profile URL, slug, or entity URN (e.g. https://www.linkedin.com/in/karpathy or just
            'karpathy').
        customer_provided_id (None | str | Unset): Your external ID for this person, echoed back in the response for
            joining results to your dataset.
    """

    input_type: SocialMediaLookupBatchTriggerBodyPeopleItemType0InputType
    linkedin_url: str
    customer_provided_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_type = self.input_type.value

        linkedin_url = self.linkedin_url

        customer_provided_id: None | str | Unset
        if isinstance(self.customer_provided_id, Unset):
            customer_provided_id = UNSET
        else:
            customer_provided_id = self.customer_provided_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputType": input_type,
                "linkedinUrl": linkedin_url,
            }
        )
        if customer_provided_id is not UNSET:
            field_dict["customerProvidedId"] = customer_provided_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_type = SocialMediaLookupBatchTriggerBodyPeopleItemType0InputType(d.pop("inputType"))

        linkedin_url = d.pop("linkedinUrl")

        def _parse_customer_provided_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId", UNSET))

        social_media_lookup_batch_trigger_body_people_item_type_0 = cls(
            input_type=input_type,
            linkedin_url=linkedin_url,
            customer_provided_id=customer_provided_id,
        )

        social_media_lookup_batch_trigger_body_people_item_type_0.additional_properties = d
        return social_media_lookup_batch_trigger_body_people_item_type_0

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
