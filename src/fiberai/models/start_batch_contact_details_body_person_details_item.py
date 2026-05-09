from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.start_batch_contact_details_body_person_details_item_linkedin_url import (
        StartBatchContactDetailsBodyPersonDetailsItemLinkedinUrl,
    )


T = TypeVar("T", bound="StartBatchContactDetailsBodyPersonDetailsItem")


@_attrs_define
class StartBatchContactDetailsBodyPersonDetailsItem:
    """
    Attributes:
        linkedin_url (StartBatchContactDetailsBodyPersonDetailsItemLinkedinUrl):
    """

    linkedin_url: StartBatchContactDetailsBodyPersonDetailsItemLinkedinUrl
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkedin_url = self.linkedin_url.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkedinUrl": linkedin_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_batch_contact_details_body_person_details_item_linkedin_url import (
            StartBatchContactDetailsBodyPersonDetailsItemLinkedinUrl,
        )

        d = dict(src_dict)
        linkedin_url = StartBatchContactDetailsBodyPersonDetailsItemLinkedinUrl.from_dict(d.pop("linkedinUrl"))

        start_batch_contact_details_body_person_details_item = cls(
            linkedin_url=linkedin_url,
        )

        start_batch_contact_details_body_person_details_item.additional_properties = d
        return start_batch_contact_details_body_person_details_item

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
