from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.instant_contact_reveal_response_200_output_profile_emails_item_type_type_1 import (
    InstantContactRevealResponse200OutputProfileEmailsItemTypeType1,
)
from ..models.instant_contact_reveal_response_200_output_profile_emails_item_type_type_2_type_1 import (
    InstantContactRevealResponse200OutputProfileEmailsItemTypeType2Type1,
)
from ..models.instant_contact_reveal_response_200_output_profile_emails_item_type_type_3_type_1 import (
    InstantContactRevealResponse200OutputProfileEmailsItemTypeType3Type1,
)
from ..models.instant_contact_reveal_response_200_output_profile_emails_item_validation_status_type_1 import (
    InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType1,
)
from ..models.instant_contact_reveal_response_200_output_profile_emails_item_validation_status_type_2_type_1 import (
    InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType2Type1,
)
from ..models.instant_contact_reveal_response_200_output_profile_emails_item_validation_status_type_3_type_1 import (
    InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantContactRevealResponse200OutputProfileEmailsItem")


@_attrs_define
class InstantContactRevealResponse200OutputProfileEmailsItem:
    """
    Attributes:
        email_address (None | str | Unset): Email address for the person.
        type_ (InstantContactRevealResponse200OutputProfileEmailsItemTypeType1 |
            InstantContactRevealResponse200OutputProfileEmailsItemTypeType2Type1 |
            InstantContactRevealResponse200OutputProfileEmailsItemTypeType3Type1 | None | Unset): Classification of the
            email address.
        validation_status (InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType1 |
            InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType2Type1 |
            InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType3Type1 | None | Unset): Email
            verification result.
        deliverability_score (float | None | Unset): Confidence score ranking deliverability for this email. Higher
            values indicate higher likelihood of delivery.
        is_catch_all (bool | None | Unset): Whether the domain accepts email to any address (catch-all). Catch-all
            domains make individual address verification unreliable — the address may appear valid but not actually be
            monitored.
    """

    email_address: None | str | Unset = UNSET
    type_: (
        InstantContactRevealResponse200OutputProfileEmailsItemTypeType1
        | InstantContactRevealResponse200OutputProfileEmailsItemTypeType2Type1
        | InstantContactRevealResponse200OutputProfileEmailsItemTypeType3Type1
        | None
        | Unset
    ) = UNSET
    validation_status: (
        InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType1
        | InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType2Type1
        | InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType3Type1
        | None
        | Unset
    ) = UNSET
    deliverability_score: float | None | Unset = UNSET
    is_catch_all: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, InstantContactRevealResponse200OutputProfileEmailsItemTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, InstantContactRevealResponse200OutputProfileEmailsItemTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, InstantContactRevealResponse200OutputProfileEmailsItemTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        validation_status: None | str | Unset
        if isinstance(self.validation_status, Unset):
            validation_status = UNSET
        elif isinstance(
            self.validation_status, InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType1
        ):
            validation_status = self.validation_status.value
        elif isinstance(
            self.validation_status, InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType2Type1
        ):
            validation_status = self.validation_status.value
        elif isinstance(
            self.validation_status, InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType3Type1
        ):
            validation_status = self.validation_status.value
        else:
            validation_status = self.validation_status

        deliverability_score: float | None | Unset
        if isinstance(self.deliverability_score, Unset):
            deliverability_score = UNSET
        else:
            deliverability_score = self.deliverability_score

        is_catch_all: bool | None | Unset
        if isinstance(self.is_catch_all, Unset):
            is_catch_all = UNSET
        else:
            is_catch_all = self.is_catch_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if type_ is not UNSET:
            field_dict["type"] = type_
        if validation_status is not UNSET:
            field_dict["validationStatus"] = validation_status
        if deliverability_score is not UNSET:
            field_dict["deliverabilityScore"] = deliverability_score
        if is_catch_all is not UNSET:
            field_dict["isCatchAll"] = is_catch_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("emailAddress", UNSET))

        def _parse_type_(
            data: object,
        ) -> (
            InstantContactRevealResponse200OutputProfileEmailsItemTypeType1
            | InstantContactRevealResponse200OutputProfileEmailsItemTypeType2Type1
            | InstantContactRevealResponse200OutputProfileEmailsItemTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = InstantContactRevealResponse200OutputProfileEmailsItemTypeType1(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = InstantContactRevealResponse200OutputProfileEmailsItemTypeType2Type1(data)

                return type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = InstantContactRevealResponse200OutputProfileEmailsItemTypeType3Type1(data)

                return type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InstantContactRevealResponse200OutputProfileEmailsItemTypeType1
                | InstantContactRevealResponse200OutputProfileEmailsItemTypeType2Type1
                | InstantContactRevealResponse200OutputProfileEmailsItemTypeType3Type1
                | None
                | Unset,
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_validation_status(
            data: object,
        ) -> (
            InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType1
            | InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType2Type1
            | InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                validation_status_type_1 = InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType1(
                    data
                )

                return validation_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                validation_status_type_2_type_1 = (
                    InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType2Type1(data)
                )

                return validation_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                validation_status_type_3_type_1 = (
                    InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType3Type1(data)
                )

                return validation_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType1
                | InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType2Type1
                | InstantContactRevealResponse200OutputProfileEmailsItemValidationStatusType3Type1
                | None
                | Unset,
                data,
            )

        validation_status = _parse_validation_status(d.pop("validationStatus", UNSET))

        def _parse_deliverability_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        deliverability_score = _parse_deliverability_score(d.pop("deliverabilityScore", UNSET))

        def _parse_is_catch_all(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_catch_all = _parse_is_catch_all(d.pop("isCatchAll", UNSET))

        instant_contact_reveal_response_200_output_profile_emails_item = cls(
            email_address=email_address,
            type_=type_,
            validation_status=validation_status,
            deliverability_score=deliverability_score,
            is_catch_all=is_catch_all,
        )

        instant_contact_reveal_response_200_output_profile_emails_item.additional_properties = d
        return instant_contact_reveal_response_200_output_profile_emails_item

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
