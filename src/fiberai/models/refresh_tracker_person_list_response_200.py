from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.refresh_tracker_person_list_response_200_charge_info_type_0 import (
        RefreshTrackerPersonListResponse200ChargeInfoType0,
    )
    from ..models.refresh_tracker_person_list_response_200_charge_info_type_1 import (
        RefreshTrackerPersonListResponse200ChargeInfoType1,
    )
    from ..models.refresh_tracker_person_list_response_200_charge_info_type_2 import (
        RefreshTrackerPersonListResponse200ChargeInfoType2,
    )
    from ..models.refresh_tracker_person_list_response_200_charge_info_type_3 import (
        RefreshTrackerPersonListResponse200ChargeInfoType3,
    )
    from ..models.refresh_tracker_person_list_response_200_charge_info_type_4 import (
        RefreshTrackerPersonListResponse200ChargeInfoType4,
    )
    from ..models.refresh_tracker_person_list_response_200_output import RefreshTrackerPersonListResponse200Output
    from ..models.refresh_tracker_person_list_response_200_warnings_type_0_item import (
        RefreshTrackerPersonListResponse200WarningsType0Item,
    )


T = TypeVar("T", bound="RefreshTrackerPersonListResponse200")


@_attrs_define
class RefreshTrackerPersonListResponse200:
    """
    Attributes:
        output (RefreshTrackerPersonListResponse200Output):
        charge_info (RefreshTrackerPersonListResponse200ChargeInfoType0 |
            RefreshTrackerPersonListResponse200ChargeInfoType1 | RefreshTrackerPersonListResponse200ChargeInfoType2 |
            RefreshTrackerPersonListResponse200ChargeInfoType3 | RefreshTrackerPersonListResponse200ChargeInfoType4):
        advice (list[str]): Tips, recommendations, and suggestions for using this API effectively.
        warnings (list[RefreshTrackerPersonListResponse200WarningsType0Item] | None | Unset): Warnings about extraneous
            fields in request
    """

    output: RefreshTrackerPersonListResponse200Output
    charge_info: (
        RefreshTrackerPersonListResponse200ChargeInfoType0
        | RefreshTrackerPersonListResponse200ChargeInfoType1
        | RefreshTrackerPersonListResponse200ChargeInfoType2
        | RefreshTrackerPersonListResponse200ChargeInfoType3
        | RefreshTrackerPersonListResponse200ChargeInfoType4
    )
    advice: list[str]
    warnings: list[RefreshTrackerPersonListResponse200WarningsType0Item] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.refresh_tracker_person_list_response_200_charge_info_type_0 import (
            RefreshTrackerPersonListResponse200ChargeInfoType0,
        )
        from ..models.refresh_tracker_person_list_response_200_charge_info_type_1 import (
            RefreshTrackerPersonListResponse200ChargeInfoType1,
        )
        from ..models.refresh_tracker_person_list_response_200_charge_info_type_2 import (
            RefreshTrackerPersonListResponse200ChargeInfoType2,
        )
        from ..models.refresh_tracker_person_list_response_200_charge_info_type_3 import (
            RefreshTrackerPersonListResponse200ChargeInfoType3,
        )

        output = self.output.to_dict()

        charge_info: dict[str, Any]
        if isinstance(self.charge_info, RefreshTrackerPersonListResponse200ChargeInfoType0):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, RefreshTrackerPersonListResponse200ChargeInfoType1):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, RefreshTrackerPersonListResponse200ChargeInfoType2):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, RefreshTrackerPersonListResponse200ChargeInfoType3):
            charge_info = self.charge_info.to_dict()
        else:
            charge_info = self.charge_info.to_dict()

        advice = self.advice

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
                "advice": advice,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refresh_tracker_person_list_response_200_charge_info_type_0 import (
            RefreshTrackerPersonListResponse200ChargeInfoType0,
        )
        from ..models.refresh_tracker_person_list_response_200_charge_info_type_1 import (
            RefreshTrackerPersonListResponse200ChargeInfoType1,
        )
        from ..models.refresh_tracker_person_list_response_200_charge_info_type_2 import (
            RefreshTrackerPersonListResponse200ChargeInfoType2,
        )
        from ..models.refresh_tracker_person_list_response_200_charge_info_type_3 import (
            RefreshTrackerPersonListResponse200ChargeInfoType3,
        )
        from ..models.refresh_tracker_person_list_response_200_charge_info_type_4 import (
            RefreshTrackerPersonListResponse200ChargeInfoType4,
        )
        from ..models.refresh_tracker_person_list_response_200_output import RefreshTrackerPersonListResponse200Output
        from ..models.refresh_tracker_person_list_response_200_warnings_type_0_item import (
            RefreshTrackerPersonListResponse200WarningsType0Item,
        )

        d = dict(src_dict)
        output = RefreshTrackerPersonListResponse200Output.from_dict(d.pop("output"))

        def _parse_charge_info(
            data: object,
        ) -> (
            RefreshTrackerPersonListResponse200ChargeInfoType0
            | RefreshTrackerPersonListResponse200ChargeInfoType1
            | RefreshTrackerPersonListResponse200ChargeInfoType2
            | RefreshTrackerPersonListResponse200ChargeInfoType3
            | RefreshTrackerPersonListResponse200ChargeInfoType4
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_0 = RefreshTrackerPersonListResponse200ChargeInfoType0.from_dict(data)

                return charge_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_1 = RefreshTrackerPersonListResponse200ChargeInfoType1.from_dict(data)

                return charge_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_2 = RefreshTrackerPersonListResponse200ChargeInfoType2.from_dict(data)

                return charge_info_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_3 = RefreshTrackerPersonListResponse200ChargeInfoType3.from_dict(data)

                return charge_info_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            charge_info_type_4 = RefreshTrackerPersonListResponse200ChargeInfoType4.from_dict(data)

            return charge_info_type_4

        charge_info = _parse_charge_info(d.pop("chargeInfo"))

        advice = cast(list[str], d.pop("advice"))

        def _parse_warnings(data: object) -> list[RefreshTrackerPersonListResponse200WarningsType0Item] | None | Unset:
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
                    warnings_type_0_item = RefreshTrackerPersonListResponse200WarningsType0Item.from_dict(
                        warnings_type_0_item_data
                    )

                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RefreshTrackerPersonListResponse200WarningsType0Item] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        refresh_tracker_person_list_response_200 = cls(
            output=output,
            charge_info=charge_info,
            advice=advice,
            warnings=warnings,
        )

        return refresh_tracker_person_list_response_200
