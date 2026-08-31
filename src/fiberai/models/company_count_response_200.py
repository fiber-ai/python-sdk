from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_count_response_200_charge_info_type_0 import CompanyCountResponse200ChargeInfoType0
    from ..models.company_count_response_200_charge_info_type_1 import CompanyCountResponse200ChargeInfoType1
    from ..models.company_count_response_200_charge_info_type_2 import CompanyCountResponse200ChargeInfoType2
    from ..models.company_count_response_200_charge_info_type_3 import CompanyCountResponse200ChargeInfoType3
    from ..models.company_count_response_200_charge_info_type_4 import CompanyCountResponse200ChargeInfoType4
    from ..models.company_count_response_200_output import CompanyCountResponse200Output
    from ..models.company_count_response_200_warnings_type_0_item import CompanyCountResponse200WarningsType0Item


T = TypeVar("T", bound="CompanyCountResponse200")


@_attrs_define
class CompanyCountResponse200:
    """
    Attributes:
        output (CompanyCountResponse200Output):
        charge_info (CompanyCountResponse200ChargeInfoType0 | CompanyCountResponse200ChargeInfoType1 |
            CompanyCountResponse200ChargeInfoType2 | CompanyCountResponse200ChargeInfoType3 |
            CompanyCountResponse200ChargeInfoType4):
        warnings (list[CompanyCountResponse200WarningsType0Item] | None | Unset): Warnings about extraneous fields in
            request
        advice (list[str] | None | Unset): Tips, recommendations, and suggestions for using this API effectively.
    """

    output: CompanyCountResponse200Output
    charge_info: (
        CompanyCountResponse200ChargeInfoType0
        | CompanyCountResponse200ChargeInfoType1
        | CompanyCountResponse200ChargeInfoType2
        | CompanyCountResponse200ChargeInfoType3
        | CompanyCountResponse200ChargeInfoType4
    )
    warnings: list[CompanyCountResponse200WarningsType0Item] | None | Unset = UNSET
    advice: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_count_response_200_charge_info_type_0 import (
            CompanyCountResponse200ChargeInfoType0,  # noqa: PLC0415
        )
        from ..models.company_count_response_200_charge_info_type_1 import (
            CompanyCountResponse200ChargeInfoType1,  # noqa: PLC0415
        )
        from ..models.company_count_response_200_charge_info_type_2 import (
            CompanyCountResponse200ChargeInfoType2,  # noqa: PLC0415
        )
        from ..models.company_count_response_200_charge_info_type_3 import (
            CompanyCountResponse200ChargeInfoType3,  # noqa: PLC0415
        )

        output = self.output.to_dict()

        charge_info: dict[str, Any]
        if isinstance(self.charge_info, CompanyCountResponse200ChargeInfoType0):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, CompanyCountResponse200ChargeInfoType1):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, CompanyCountResponse200ChargeInfoType2):
            charge_info = self.charge_info.to_dict()
        elif isinstance(self.charge_info, CompanyCountResponse200ChargeInfoType3):
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

        advice: list[str] | None | Unset
        if isinstance(self.advice, Unset):
            advice = UNSET
        elif isinstance(self.advice, list):
            advice = self.advice

        else:
            advice = self.advice

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "output": output,
                "chargeInfo": charge_info,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if advice is not UNSET:
            field_dict["advice"] = advice

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_count_response_200_charge_info_type_0 import (
            CompanyCountResponse200ChargeInfoType0,  # noqa: PLC0415
        )
        from ..models.company_count_response_200_charge_info_type_1 import (
            CompanyCountResponse200ChargeInfoType1,  # noqa: PLC0415
        )
        from ..models.company_count_response_200_charge_info_type_2 import (
            CompanyCountResponse200ChargeInfoType2,  # noqa: PLC0415
        )
        from ..models.company_count_response_200_charge_info_type_3 import (
            CompanyCountResponse200ChargeInfoType3,  # noqa: PLC0415
        )
        from ..models.company_count_response_200_charge_info_type_4 import (
            CompanyCountResponse200ChargeInfoType4,  # noqa: PLC0415
        )
        from ..models.company_count_response_200_output import CompanyCountResponse200Output  # noqa: PLC0415
        from ..models.company_count_response_200_warnings_type_0_item import (
            CompanyCountResponse200WarningsType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)
        output = CompanyCountResponse200Output.from_dict(d.pop("output"))

        def _parse_charge_info(
            data: object,
        ) -> (
            CompanyCountResponse200ChargeInfoType0
            | CompanyCountResponse200ChargeInfoType1
            | CompanyCountResponse200ChargeInfoType2
            | CompanyCountResponse200ChargeInfoType3
            | CompanyCountResponse200ChargeInfoType4
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_0 = CompanyCountResponse200ChargeInfoType0.from_dict(data)

                return charge_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_1 = CompanyCountResponse200ChargeInfoType1.from_dict(data)

                return charge_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_2 = CompanyCountResponse200ChargeInfoType2.from_dict(data)

                return charge_info_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                charge_info_type_3 = CompanyCountResponse200ChargeInfoType3.from_dict(data)

                return charge_info_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            charge_info_type_4 = CompanyCountResponse200ChargeInfoType4.from_dict(data)

            return charge_info_type_4

        charge_info = _parse_charge_info(d.pop("chargeInfo"))

        def _parse_warnings(data: object) -> list[CompanyCountResponse200WarningsType0Item] | None | Unset:
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
                    warnings_type_0_item = CompanyCountResponse200WarningsType0Item.from_dict(warnings_type_0_item_data)

                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyCountResponse200WarningsType0Item] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        def _parse_advice(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                advice_type_0 = cast(list[str], data)

                return advice_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        advice = _parse_advice(d.pop("advice", UNSET))

        company_count_response_200 = cls(
            output=output,
            charge_info=charge_info,
            warnings=warnings,
            advice=advice,
        )

        return company_count_response_200
