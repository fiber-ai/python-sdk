from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_lookup_trigger_response_200_charge_info_type_0 import (
        GithubLookupTriggerResponse200ChargeInfoType0,
    )
    from ..models.github_lookup_trigger_response_200_charge_info_type_1 import (
        GithubLookupTriggerResponse200ChargeInfoType1,
    )
    from ..models.github_lookup_trigger_response_200_charge_info_type_2 import (
        GithubLookupTriggerResponse200ChargeInfoType2,
    )
    from ..models.github_lookup_trigger_response_200_charge_info_type_3 import (
        GithubLookupTriggerResponse200ChargeInfoType3,
    )
    from ..models.github_lookup_trigger_response_200_output import GithubLookupTriggerResponse200Output
    from ..models.github_lookup_trigger_response_200_warnings_type_0_item import (
        GithubLookupTriggerResponse200WarningsType0Item,
    )


T = TypeVar("T", bound="GithubLookupTriggerResponse200")


@_attrs_define
class GithubLookupTriggerResponse200:
    """
    Attributes:
        output (GithubLookupTriggerResponse200Output):
        charge_info (GithubLookupTriggerResponse200ChargeInfoType0 | GithubLookupTriggerResponse200ChargeInfoType1 |
            GithubLookupTriggerResponse200ChargeInfoType2 | GithubLookupTriggerResponse200ChargeInfoType3):
        warnings (list[GithubLookupTriggerResponse200WarningsType0Item] | None | Unset): Warnings about extraneous
            fields in request
    """

    output: GithubLookupTriggerResponse200Output
    charge_info: (
        GithubLookupTriggerResponse200ChargeInfoType0
        | GithubLookupTriggerResponse200ChargeInfoType1
        | GithubLookupTriggerResponse200ChargeInfoType2
        | GithubLookupTriggerResponse200ChargeInfoType3
    )
    warnings: list[GithubLookupTriggerResponse200WarningsType0Item] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.github_lookup_trigger_response_200_charge_info_type_0 import (
            GithubLookupTriggerResponse200ChargeInfoType0,
        )
        from ..models.github_lookup_trigger_response_200_charge_info_type_1 import (
            GithubLookupTriggerResponse200ChargeInfoType1,
        )
        from ..models.github_lookup_trigger_response_200_charge_info_type_2 import (
            GithubLookupTriggerResponse200ChargeInfoType2,
        )

        output = self.output.to_dict()

        charge_info: dict[str, Any]
        if isinstance(self.charge_info, GithubLookupTriggerResponse200ChargeInfoType0):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, GithubLookupTriggerResponse200ChargeInfoType1):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, GithubLookupTriggerResponse200ChargeInfoType2):
            charge_info = self.charge_info.to_dict()
        else:
            charge_info = self.charge_info.to_dict()

        warnings: list[dict[str, Any]] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = []
            for warnings_type_0_item_data in self.warnings:
                warnings_type_0_item = warnings_type_0_item_data.to_dict()
                warnings.append(warnings_type_0_item)

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "output": output,
                "chargeInfo": charge_info,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_lookup_trigger_response_200_charge_info_type_0 import (
            GithubLookupTriggerResponse200ChargeInfoType0,
        )
        from ..models.github_lookup_trigger_response_200_charge_info_type_1 import (
            GithubLookupTriggerResponse200ChargeInfoType1,
        )
        from ..models.github_lookup_trigger_response_200_charge_info_type_2 import (
            GithubLookupTriggerResponse200ChargeInfoType2,
        )
        from ..models.github_lookup_trigger_response_200_charge_info_type_3 import (
            GithubLookupTriggerResponse200ChargeInfoType3,
        )
        from ..models.github_lookup_trigger_response_200_output import GithubLookupTriggerResponse200Output
        from ..models.github_lookup_trigger_response_200_warnings_type_0_item import (
            GithubLookupTriggerResponse200WarningsType0Item,
        )

        d = dict(src_dict)
        output = GithubLookupTriggerResponse200Output.from_dict(d.pop("output"))

        def _parse_charge_info(
            data: object,
        ) -> (
            GithubLookupTriggerResponse200ChargeInfoType0
            | GithubLookupTriggerResponse200ChargeInfoType1
            | GithubLookupTriggerResponse200ChargeInfoType2
            | GithubLookupTriggerResponse200ChargeInfoType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_0 = GithubLookupTriggerResponse200ChargeInfoType0.from_dict(data)

                return charge_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_1 = GithubLookupTriggerResponse200ChargeInfoType1.from_dict(data)

                return charge_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_2 = GithubLookupTriggerResponse200ChargeInfoType2.from_dict(data)

                return charge_info_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            charge_info_type_3 = GithubLookupTriggerResponse200ChargeInfoType3.from_dict(data)

            return charge_info_type_3

        charge_info = _parse_charge_info(d.pop("chargeInfo"))

        def _parse_warnings(data: object) -> list[GithubLookupTriggerResponse200WarningsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = []
                _warnings_type_0 = data
                for warnings_type_0_item_data in _warnings_type_0:
                    warnings_type_0_item = GithubLookupTriggerResponse200WarningsType0Item.from_dict(
                        warnings_type_0_item_data
                    )

                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GithubLookupTriggerResponse200WarningsType0Item] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        github_lookup_trigger_response_200 = cls(
            output=output,
            charge_info=charge_info,
            warnings=warnings,
        )

        return github_lookup_trigger_response_200
