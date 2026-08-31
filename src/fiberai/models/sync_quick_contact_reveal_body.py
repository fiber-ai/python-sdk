from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_quick_contact_reveal_body_patience_type_1 import SyncQuickContactRevealBodyPatienceType1
from ..models.sync_quick_contact_reveal_body_patience_type_2_type_1 import SyncQuickContactRevealBodyPatienceType2Type1
from ..models.sync_quick_contact_reveal_body_patience_type_3_type_1 import SyncQuickContactRevealBodyPatienceType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_quick_contact_reveal_body_enrichment_type import SyncQuickContactRevealBodyEnrichmentType


T = TypeVar("T", bound="SyncQuickContactRevealBody")


@_attrs_define
class SyncQuickContactRevealBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        linkedin_url (str): The person's LinkedIn identifier. Accepts a full LinkedIn profile URL (e.g.
            'https://www.linkedin.com/in/williamhgates/'), a bare slug (e.g. 'williamhgates'), a Sales Navigator URN (e.g.
            'ACwAAA-001MBbIvJon'), or a numeric LinkedIn user ID (e.g. '443105112').
        enrichment_type (SyncQuickContactRevealBodyEnrichmentType | Unset): The enrichment types to request. Credits are
            charged per selected type.
        patience (None | SyncQuickContactRevealBodyPatienceType1 | SyncQuickContactRevealBodyPatienceType2Type1 |
            SyncQuickContactRevealBodyPatienceType3Type1 | Unset): How long to wait for email deliverability validation
            after a contact is found. Higher patience increases average response time but improves deliverability accuracy.
            MINIMUM is the least thorough bounce-detection option.
        validate_emails (bool | None | Unset): Deprecated — use `patience` instead. When false, maps to patience:
            MINIMUM. Ignored if `patience` is also provided.
    """

    api_key: str
    linkedin_url: str
    enrichment_type: SyncQuickContactRevealBodyEnrichmentType | Unset = UNSET
    patience: (
        None
        | SyncQuickContactRevealBodyPatienceType1
        | SyncQuickContactRevealBodyPatienceType2Type1
        | SyncQuickContactRevealBodyPatienceType3Type1
        | Unset
    ) = UNSET
    validate_emails: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        linkedin_url = self.linkedin_url

        enrichment_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enrichment_type, Unset):
            enrichment_type = self.enrichment_type.to_dict()

        patience: None | str | Unset
        if isinstance(self.patience, Unset):
            patience = UNSET
        elif isinstance(self.patience, SyncQuickContactRevealBodyPatienceType1):
            patience = self.patience.value
        elif isinstance(self.patience, SyncQuickContactRevealBodyPatienceType2Type1):
            patience = self.patience.value
        elif isinstance(self.patience, SyncQuickContactRevealBodyPatienceType3Type1):
            patience = self.patience.value
        else:
            patience = self.patience

        validate_emails: bool | None | Unset
        if isinstance(self.validate_emails, Unset):
            validate_emails = UNSET
        else:
            validate_emails = self.validate_emails

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "linkedinUrl": linkedin_url,
            }
        )
        if enrichment_type is not UNSET:
            field_dict["enrichmentType"] = enrichment_type
        if patience is not UNSET:
            field_dict["patience"] = patience
        if validate_emails is not UNSET:
            field_dict["validateEmails"] = validate_emails

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_quick_contact_reveal_body_enrichment_type import (
            SyncQuickContactRevealBodyEnrichmentType,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        linkedin_url = d.pop("linkedinUrl")

        _enrichment_type = d.pop("enrichmentType", UNSET)
        enrichment_type: SyncQuickContactRevealBodyEnrichmentType | Unset
        if isinstance(_enrichment_type, Unset):
            enrichment_type = UNSET
        else:
            enrichment_type = SyncQuickContactRevealBodyEnrichmentType.from_dict(_enrichment_type)

        def _parse_patience(
            data: object,
        ) -> (
            None
            | SyncQuickContactRevealBodyPatienceType1
            | SyncQuickContactRevealBodyPatienceType2Type1
            | SyncQuickContactRevealBodyPatienceType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_1 = SyncQuickContactRevealBodyPatienceType1(data)

                return patience_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_2_type_1 = SyncQuickContactRevealBodyPatienceType2Type1(data)

                return patience_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_3_type_1 = SyncQuickContactRevealBodyPatienceType3Type1(data)

                return patience_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SyncQuickContactRevealBodyPatienceType1
                | SyncQuickContactRevealBodyPatienceType2Type1
                | SyncQuickContactRevealBodyPatienceType3Type1
                | Unset,
                data,
            )

        patience = _parse_patience(d.pop("patience", UNSET))

        def _parse_validate_emails(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        validate_emails = _parse_validate_emails(d.pop("validateEmails", UNSET))

        sync_quick_contact_reveal_body = cls(
            api_key=api_key,
            linkedin_url=linkedin_url,
            enrichment_type=enrichment_type,
            patience=patience,
            validate_emails=validate_emails,
        )

        sync_quick_contact_reveal_body.additional_properties = d
        return sync_quick_contact_reveal_body

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
