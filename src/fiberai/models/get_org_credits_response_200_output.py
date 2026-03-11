from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_org_credits_response_200_output_credits_per_operation_type_0 import (
        GetOrgCreditsResponse200OutputCreditsPerOperationType0,
    )


T = TypeVar("T", bound="GetOrgCreditsResponse200Output")


@_attrs_define
class GetOrgCreditsResponse200Output:
    """
    Attributes:
        organization_id (str):
        max_ (float):
        used (float):
        available (float):
        usage_period_resets_on (str):
        credits_per_operation (GetOrgCreditsResponse200OutputCreditsPerOperationType0 | None | Unset):
    """

    organization_id: str
    max_: float
    used: float
    available: float
    usage_period_resets_on: str
    credits_per_operation: GetOrgCreditsResponse200OutputCreditsPerOperationType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0 import (
            GetOrgCreditsResponse200OutputCreditsPerOperationType0,
        )

        organization_id = self.organization_id

        max_ = self.max_

        used = self.used

        available = self.available

        usage_period_resets_on = self.usage_period_resets_on

        credits_per_operation: dict[str, Any] | None | Unset
        if isinstance(self.credits_per_operation, Unset):
            credits_per_operation = UNSET
        elif isinstance(self.credits_per_operation, GetOrgCreditsResponse200OutputCreditsPerOperationType0):
            credits_per_operation = self.credits_per_operation.to_dict()
        else:
            credits_per_operation = self.credits_per_operation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationId": organization_id,
                "max": max_,
                "used": used,
                "available": available,
                "usagePeriodResetsOn": usage_period_resets_on,
            }
        )
        if credits_per_operation is not UNSET:
            field_dict["creditsPerOperation"] = credits_per_operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0 import (
            GetOrgCreditsResponse200OutputCreditsPerOperationType0,
        )

        d = dict(src_dict)
        organization_id = d.pop("organizationId")

        max_ = d.pop("max")

        used = d.pop("used")

        available = d.pop("available")

        usage_period_resets_on = d.pop("usagePeriodResetsOn")

        def _parse_credits_per_operation(
            data: object,
        ) -> GetOrgCreditsResponse200OutputCreditsPerOperationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credits_per_operation_type_0 = GetOrgCreditsResponse200OutputCreditsPerOperationType0.from_dict(data)

                return credits_per_operation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetOrgCreditsResponse200OutputCreditsPerOperationType0 | None | Unset, data)

        credits_per_operation = _parse_credits_per_operation(d.pop("creditsPerOperation", UNSET))

        get_org_credits_response_200_output = cls(
            organization_id=organization_id,
            max_=max_,
            used=used,
            available=available,
            usage_period_resets_on=usage_period_resets_on,
            credits_per_operation=credits_per_operation,
        )

        get_org_credits_response_200_output.additional_properties = d
        return get_org_credits_response_200_output

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
