from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_budgeted_contact_reveal_response_200_output_profile import (
        SyncBudgetedContactRevealResponse200OutputProfile,
    )


T = TypeVar("T", bound="SyncBudgetedContactRevealResponse200Output")


@_attrs_define
class SyncBudgetedContactRevealResponse200Output:
    """
    Attributes:
        profile (SyncBudgetedContactRevealResponse200OutputProfile):
    """

    profile: SyncBudgetedContactRevealResponse200OutputProfile
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile = self.profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profile": profile,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_budgeted_contact_reveal_response_200_output_profile import (
            SyncBudgetedContactRevealResponse200OutputProfile,  # noqa: PLC0415
        )

        d = dict(src_dict)
        profile = SyncBudgetedContactRevealResponse200OutputProfile.from_dict(d.pop("profile"))

        sync_budgeted_contact_reveal_response_200_output = cls(
            profile=profile,
        )

        sync_budgeted_contact_reveal_response_200_output.additional_properties = d
        return sync_budgeted_contact_reveal_response_200_output

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
