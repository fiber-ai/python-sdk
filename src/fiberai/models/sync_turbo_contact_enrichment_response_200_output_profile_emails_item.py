from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_turbo_contact_enrichment_response_200_output_profile_emails_item_status_type_1 import (
    SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType1,
)
from ..models.sync_turbo_contact_enrichment_response_200_output_profile_emails_item_status_type_2_type_1 import (
    SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType2Type1,
)
from ..models.sync_turbo_contact_enrichment_response_200_output_profile_emails_item_status_type_3_type_1 import (
    SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncTurboContactEnrichmentResponse200OutputProfileEmailsItem")


@_attrs_define
class SyncTurboContactEnrichmentResponse200OutputProfileEmailsItem:
    """
    Attributes:
        email (str):
        type_ (str):
        status (None | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType1 |
            SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType2Type1 |
            SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType3Type1 | Unset):
    """

    email: str
    type_: str
    status: (
        None
        | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType1
        | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType2Type1
        | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType3Type1
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        type_ = self.type_

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType1):
            status = self.status.value
        elif isinstance(self.status, SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "type": type_,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        type_ = d.pop("type")

        def _parse_status(
            data: object,
        ) -> (
            None
            | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType1
            | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType2Type1
            | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType2Type1(
                    data
                )

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType3Type1(
                    data
                )

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType1
                | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType2Type1
                | SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType3Type1
                | Unset,
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        sync_turbo_contact_enrichment_response_200_output_profile_emails_item = cls(
            email=email,
            type_=type_,
            status=status,
        )

        sync_turbo_contact_enrichment_response_200_output_profile_emails_item.additional_properties = d
        return sync_turbo_contact_enrichment_response_200_output_profile_emails_item

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
