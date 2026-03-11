from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_status import (
    TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_entered_stealth_at_type_0 import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType0,
    )
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_entered_stealth_at_type_1 import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType1,
    )
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_left_stealth_at_type_0 import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType0,
    )
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_left_stealth_at_type_1 import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType1,
    )
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0 import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0,
    )


T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1")


@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1:
    """
    Attributes:
        status (TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1Status):
        left_stealth_at (None |
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType0 |
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType1 | Unset):
        entered_stealth_at (None |
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType0 |
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType1 | Unset):
        stealth_duration (None |
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0 | Unset):
    """

    status: TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1Status
    left_stealth_at: (
        None
        | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType0
        | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType1
        | Unset
    ) = UNSET
    entered_stealth_at: (
        None
        | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType0
        | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType1
        | Unset
    ) = UNSET
    stealth_duration: (
        None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_entered_stealth_at_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType0,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_entered_stealth_at_type_1 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType1,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_left_stealth_at_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType0,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_left_stealth_at_type_1 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType1,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0,
        )

        status = self.status.value

        left_stealth_at: dict[str, Any] | None | Unset
        if isinstance(self.left_stealth_at, Unset):
            left_stealth_at = UNSET
        elif isinstance(
            self.left_stealth_at,
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType0,
        ):
            left_stealth_at = self.left_stealth_at.to_dict()
        elif isinstance(
            self.left_stealth_at,
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType1,
        ):
            left_stealth_at = self.left_stealth_at.to_dict()
        else:
            left_stealth_at = self.left_stealth_at

        entered_stealth_at: dict[str, Any] | None | Unset
        if isinstance(self.entered_stealth_at, Unset):
            entered_stealth_at = UNSET
        elif isinstance(
            self.entered_stealth_at,
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType0,
        ):
            entered_stealth_at = self.entered_stealth_at.to_dict()
        elif isinstance(
            self.entered_stealth_at,
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType1,
        ):
            entered_stealth_at = self.entered_stealth_at.to_dict()
        else:
            entered_stealth_at = self.entered_stealth_at

        stealth_duration: dict[str, Any] | None | Unset
        if isinstance(self.stealth_duration, Unset):
            stealth_duration = UNSET
        elif isinstance(
            self.stealth_duration,
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0,
        ):
            stealth_duration = self.stealth_duration.to_dict()
        else:
            stealth_duration = self.stealth_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if left_stealth_at is not UNSET:
            field_dict["leftStealthAt"] = left_stealth_at
        if entered_stealth_at is not UNSET:
            field_dict["enteredStealthAt"] = entered_stealth_at
        if stealth_duration is not UNSET:
            field_dict["stealthDuration"] = stealth_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_entered_stealth_at_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType0,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_entered_stealth_at_type_1 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType1,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_left_stealth_at_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType0,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_left_stealth_at_type_1 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType1,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1_stealth_duration_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0,
        )

        d = dict(src_dict)
        status = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1Status(d.pop("status"))

        def _parse_left_stealth_at(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType0
            | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_stealth_at_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType0.from_dict(
                    data
                )

                return left_stealth_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_stealth_at_type_1 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType1.from_dict(
                    data
                )

                return left_stealth_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType0
                | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1LeftStealthAtType1
                | Unset,
                data,
            )

        left_stealth_at = _parse_left_stealth_at(d.pop("leftStealthAt", UNSET))

        def _parse_entered_stealth_at(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType0
            | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entered_stealth_at_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType0.from_dict(
                    data
                )

                return entered_stealth_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entered_stealth_at_type_1 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType1.from_dict(
                    data
                )

                return entered_stealth_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType0
                | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1EnteredStealthAtType1
                | Unset,
                data,
            )

        entered_stealth_at = _parse_entered_stealth_at(d.pop("enteredStealthAt", UNSET))

        def _parse_stealth_duration(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stealth_duration_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0.from_dict(
                    data
                )

                return stealth_duration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputProfileSearchParamsType0StealthV2Type1StealthDurationType0
                | Unset,
                data,
            )

        stealth_duration = _parse_stealth_duration(d.pop("stealthDuration", UNSET))

        text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1 = cls(
            status=status,
            left_stealth_at=left_stealth_at,
            entered_stealth_at=entered_stealth_at,
            stealth_duration=stealth_duration,
        )

        text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_stealth_v2_type_1

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
