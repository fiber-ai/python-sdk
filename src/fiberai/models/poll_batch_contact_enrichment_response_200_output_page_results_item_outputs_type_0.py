from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_emails_item import (
        PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItem,
    )
    from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_phone_numbers_item import (
        PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItem,
    )


T = TypeVar("T", bound="PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0")


@_attrs_define
class PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0:
    """The reveal result for this person

    Attributes:
        emails (list[PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItem]):
        phone_numbers (list[PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItem]):
        exhaustive (bool | None | Unset):
    """

    emails: list[PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItem]
    phone_numbers: list[PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItem]
    exhaustive: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()
            emails.append(emails_item)

        phone_numbers = []
        for phone_numbers_item_data in self.phone_numbers:
            phone_numbers_item = phone_numbers_item_data.to_dict()
            phone_numbers.append(phone_numbers_item)

        exhaustive: bool | None | Unset
        if isinstance(self.exhaustive, Unset):
            exhaustive = UNSET
        else:
            exhaustive = self.exhaustive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
                "phoneNumbers": phone_numbers,
            }
        )
        if exhaustive is not UNSET:
            field_dict["exhaustive"] = exhaustive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_emails_item import (
            PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItem,
        )
        from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_phone_numbers_item import (
            PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItem,
        )

        d = dict(src_dict)
        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItem.from_dict(
                emails_item_data
            )

            emails.append(emails_item)

        phone_numbers = []
        _phone_numbers = d.pop("phoneNumbers")
        for phone_numbers_item_data in _phone_numbers:
            phone_numbers_item = (
                PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItem.from_dict(
                    phone_numbers_item_data
                )
            )

            phone_numbers.append(phone_numbers_item)

        def _parse_exhaustive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exhaustive = _parse_exhaustive(d.pop("exhaustive", UNSET))

        poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0 = cls(
            emails=emails,
            phone_numbers=phone_numbers,
            exhaustive=exhaustive,
        )

        poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0.additional_properties = d
        return poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0

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
