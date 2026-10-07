from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollExhaustiveContactEnrichmentResultResponse200OutputProfileFoundOtherTypesType0")


@_attrs_define
class PollExhaustiveContactEnrichmentResultResponse200OutputProfileFoundOtherTypesType0:
    """Counts of contact details discovered but not returned because they were not part of the requested enrichmentType
    set. Only present when at least one unrequested type was found; request the corresponding enrichment types and run
    the task again to receive them.

        Attributes:
            work_emails (int):
            personal_emails (int):
            phone_numbers (int):
    """

    work_emails: int
    personal_emails: int
    phone_numbers: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_emails = self.work_emails

        personal_emails = self.personal_emails

        phone_numbers = self.phone_numbers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workEmails": work_emails,
                "personalEmails": personal_emails,
                "phoneNumbers": phone_numbers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        work_emails = d.pop("workEmails")

        personal_emails = d.pop("personalEmails")

        phone_numbers = d.pop("phoneNumbers")

        poll_exhaustive_contact_enrichment_result_response_200_output_profile_found_other_types_type_0 = cls(
            work_emails=work_emails,
            personal_emails=personal_emails,
            phone_numbers=phone_numbers,
        )

        poll_exhaustive_contact_enrichment_result_response_200_output_profile_found_other_types_type_0.additional_properties = d
        return poll_exhaustive_contact_enrichment_result_response_200_output_profile_found_other_types_type_0

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
