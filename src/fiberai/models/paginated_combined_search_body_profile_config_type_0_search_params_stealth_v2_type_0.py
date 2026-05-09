from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0_status import (
    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0_entered_stealth_at_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0_entered_stealth_at_type_1 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0")


@_attrs_define
class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0:
    """
    Attributes:
        status (PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0Status):
        entered_stealth_at (None |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType0 |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1 | Unset):
    """

    status: PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0Status
    entered_stealth_at: (
        None
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType0
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0_entered_stealth_at_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0_entered_stealth_at_type_1 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1,
        )

        status = self.status.value

        entered_stealth_at: dict[str, Any] | None | Unset
        if isinstance(self.entered_stealth_at, Unset):
            entered_stealth_at = UNSET
        elif isinstance(
            self.entered_stealth_at,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType0,
        ):
            entered_stealth_at = self.entered_stealth_at.to_dict()
        elif isinstance(
            self.entered_stealth_at,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1,
        ):
            entered_stealth_at = self.entered_stealth_at.to_dict()
        else:
            entered_stealth_at = self.entered_stealth_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if entered_stealth_at is not UNSET:
            field_dict["enteredStealthAt"] = entered_stealth_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0_entered_stealth_at_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0_entered_stealth_at_type_1 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1,
        )

        d = dict(src_dict)
        status = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0Status(d.pop("status"))

        def _parse_entered_stealth_at(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType0
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entered_stealth_at_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType0.from_dict(
                    data
                )

                return entered_stealth_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entered_stealth_at_type_1 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1.from_dict(
                    data
                )

                return entered_stealth_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType0
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStealthV2Type0EnteredStealthAtType1
                | Unset,
                data,
            )

        entered_stealth_at = _parse_entered_stealth_at(d.pop("enteredStealthAt", UNSET))

        paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0 = cls(
            status=status,
            entered_stealth_at=entered_stealth_at,
        )

        paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0.additional_properties = d
        return paginated_combined_search_body_profile_config_type_0_search_params_stealth_v2_type_0

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
