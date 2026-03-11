from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_phone_number_response_200_output_is_reachable import (
    ValidatePhoneNumberResponse200OutputIsReachable,
)
from ..models.validate_phone_number_response_200_output_validation_status import (
    ValidatePhoneNumberResponse200OutputValidationStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validate_phone_number_response_200_output_current_carrier_type_0 import (
        ValidatePhoneNumberResponse200OutputCurrentCarrierType0,
    )
    from ..models.validate_phone_number_response_200_output_original_carrier_type_0 import (
        ValidatePhoneNumberResponse200OutputOriginalCarrierType0,
    )


T = TypeVar("T", bound="ValidatePhoneNumberResponse200Output")


@_attrs_define
class ValidatePhoneNumberResponse200Output:
    """
    Attributes:
        is_valid (bool): Whether the phone number is valid
        is_reachable (ValidatePhoneNumberResponse200OutputIsReachable): Whether the phone number is currently reachable
            (alive/active status)
        is_ported (bool): Whether the number has been ported to a different carrier
        is_roaming (bool): Whether the number is currently roaming
        validation_score (int): Validation score from 0-10 (10 = valid and reachable, 6 = valid but not reachable, 2 =
            unknown, 0 = invalid)
        validation_status (ValidatePhoneNumberResponse200OutputValidationStatus): Overall validation status
        formatted_number (None | str | Unset): Phone number in international format (e.g., +1 234 567 8900)
        national_format (None | str | Unset): Phone number in national format
        country_calling_code (None | str | Unset): Country calling code with plus prefix (e.g. '+1', '+44'), derived
            from validation result; not used as request input.
        country_iso_code (None | str | Unset): ISO 3166-1 alpha-2 country code (e.g. 'US', 'GB'), derived from
            validation result; not used as request input.
        country_name (None | str | Unset): Full country name (e.g. 'United States'), derived from validation result.
        current_carrier (None | Unset | ValidatePhoneNumberResponse200OutputCurrentCarrierType0): Information about the
            current carrier
        original_carrier (None | Unset | ValidatePhoneNumberResponse200OutputOriginalCarrierType0): Information about
            the original carrier that issued the number
        caller_id_name (None | str | Unset): The name associated with this phone number (what shows up on caller ID)
    """

    is_valid: bool
    is_reachable: ValidatePhoneNumberResponse200OutputIsReachable
    is_ported: bool
    is_roaming: bool
    validation_score: int
    validation_status: ValidatePhoneNumberResponse200OutputValidationStatus
    formatted_number: None | str | Unset = UNSET
    national_format: None | str | Unset = UNSET
    country_calling_code: None | str | Unset = UNSET
    country_iso_code: None | str | Unset = UNSET
    country_name: None | str | Unset = UNSET
    current_carrier: None | Unset | ValidatePhoneNumberResponse200OutputCurrentCarrierType0 = UNSET
    original_carrier: None | Unset | ValidatePhoneNumberResponse200OutputOriginalCarrierType0 = UNSET
    caller_id_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.validate_phone_number_response_200_output_current_carrier_type_0 import (
            ValidatePhoneNumberResponse200OutputCurrentCarrierType0,
        )
        from ..models.validate_phone_number_response_200_output_original_carrier_type_0 import (
            ValidatePhoneNumberResponse200OutputOriginalCarrierType0,
        )

        is_valid = self.is_valid

        is_reachable = self.is_reachable.value

        is_ported = self.is_ported

        is_roaming = self.is_roaming

        validation_score = self.validation_score

        validation_status = self.validation_status.value

        formatted_number: None | str | Unset
        if isinstance(self.formatted_number, Unset):
            formatted_number = UNSET
        else:
            formatted_number = self.formatted_number

        national_format: None | str | Unset
        if isinstance(self.national_format, Unset):
            national_format = UNSET
        else:
            national_format = self.national_format

        country_calling_code: None | str | Unset
        if isinstance(self.country_calling_code, Unset):
            country_calling_code = UNSET
        else:
            country_calling_code = self.country_calling_code

        country_iso_code: None | str | Unset
        if isinstance(self.country_iso_code, Unset):
            country_iso_code = UNSET
        else:
            country_iso_code = self.country_iso_code

        country_name: None | str | Unset
        if isinstance(self.country_name, Unset):
            country_name = UNSET
        else:
            country_name = self.country_name

        current_carrier: dict[str, Any] | None | Unset
        if isinstance(self.current_carrier, Unset):
            current_carrier = UNSET
        elif isinstance(self.current_carrier, ValidatePhoneNumberResponse200OutputCurrentCarrierType0):
            current_carrier = self.current_carrier.to_dict()
        else:
            current_carrier = self.current_carrier

        original_carrier: dict[str, Any] | None | Unset
        if isinstance(self.original_carrier, Unset):
            original_carrier = UNSET
        elif isinstance(self.original_carrier, ValidatePhoneNumberResponse200OutputOriginalCarrierType0):
            original_carrier = self.original_carrier.to_dict()
        else:
            original_carrier = self.original_carrier

        caller_id_name: None | str | Unset
        if isinstance(self.caller_id_name, Unset):
            caller_id_name = UNSET
        else:
            caller_id_name = self.caller_id_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isValid": is_valid,
                "isReachable": is_reachable,
                "isPorted": is_ported,
                "isRoaming": is_roaming,
                "validationScore": validation_score,
                "validationStatus": validation_status,
            }
        )
        if formatted_number is not UNSET:
            field_dict["formattedNumber"] = formatted_number
        if national_format is not UNSET:
            field_dict["nationalFormat"] = national_format
        if country_calling_code is not UNSET:
            field_dict["countryCallingCode"] = country_calling_code
        if country_iso_code is not UNSET:
            field_dict["countryIsoCode"] = country_iso_code
        if country_name is not UNSET:
            field_dict["countryName"] = country_name
        if current_carrier is not UNSET:
            field_dict["currentCarrier"] = current_carrier
        if original_carrier is not UNSET:
            field_dict["originalCarrier"] = original_carrier
        if caller_id_name is not UNSET:
            field_dict["callerIdName"] = caller_id_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validate_phone_number_response_200_output_current_carrier_type_0 import (
            ValidatePhoneNumberResponse200OutputCurrentCarrierType0,
        )
        from ..models.validate_phone_number_response_200_output_original_carrier_type_0 import (
            ValidatePhoneNumberResponse200OutputOriginalCarrierType0,
        )

        d = dict(src_dict)
        is_valid = d.pop("isValid")

        is_reachable = ValidatePhoneNumberResponse200OutputIsReachable(d.pop("isReachable"))

        is_ported = d.pop("isPorted")

        is_roaming = d.pop("isRoaming")

        validation_score = d.pop("validationScore")

        validation_status = ValidatePhoneNumberResponse200OutputValidationStatus(d.pop("validationStatus"))

        def _parse_formatted_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formatted_number = _parse_formatted_number(d.pop("formattedNumber", UNSET))

        def _parse_national_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        national_format = _parse_national_format(d.pop("nationalFormat", UNSET))

        def _parse_country_calling_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_calling_code = _parse_country_calling_code(d.pop("countryCallingCode", UNSET))

        def _parse_country_iso_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_iso_code = _parse_country_iso_code(d.pop("countryIsoCode", UNSET))

        def _parse_country_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_name = _parse_country_name(d.pop("countryName", UNSET))

        def _parse_current_carrier(
            data: object,
        ) -> None | Unset | ValidatePhoneNumberResponse200OutputCurrentCarrierType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_carrier_type_0 = ValidatePhoneNumberResponse200OutputCurrentCarrierType0.from_dict(data)

                return current_carrier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ValidatePhoneNumberResponse200OutputCurrentCarrierType0, data)

        current_carrier = _parse_current_carrier(d.pop("currentCarrier", UNSET))

        def _parse_original_carrier(
            data: object,
        ) -> None | Unset | ValidatePhoneNumberResponse200OutputOriginalCarrierType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                original_carrier_type_0 = ValidatePhoneNumberResponse200OutputOriginalCarrierType0.from_dict(data)

                return original_carrier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ValidatePhoneNumberResponse200OutputOriginalCarrierType0, data)

        original_carrier = _parse_original_carrier(d.pop("originalCarrier", UNSET))

        def _parse_caller_id_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caller_id_name = _parse_caller_id_name(d.pop("callerIdName", UNSET))

        validate_phone_number_response_200_output = cls(
            is_valid=is_valid,
            is_reachable=is_reachable,
            is_ported=is_ported,
            is_roaming=is_roaming,
            validation_score=validation_score,
            validation_status=validation_status,
            formatted_number=formatted_number,
            national_format=national_format,
            country_calling_code=country_calling_code,
            country_iso_code=country_iso_code,
            country_name=country_name,
            current_carrier=current_carrier,
            original_carrier=original_carrier,
            caller_id_name=caller_id_name,
        )

        validate_phone_number_response_200_output.additional_properties = d
        return validate_phone_number_response_200_output

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
