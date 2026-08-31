from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_type import (
    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Type,
)
from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_0 import (
    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0,
)
from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_1 import (
    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1,
)
from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_2 import (
    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2,
)
from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_3 import (
    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3,
)
from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_4 import (
    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4,
)
from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_5 import (
    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5,
)
from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_6 import (
    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6,
)
from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_7 import (
    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7,
)

if TYPE_CHECKING:
    from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_change import (
        CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change,
    )


T = TypeVar("T", bound="CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1")


@_attrs_define
class CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1:
    """
    Attributes:
        type_ (CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Type):
        window_months (CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0 |
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1 |
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2 |
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3 |
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4 |
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5 |
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6 |
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7):
        change (CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change):
    """

    type_: CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Type
    window_months: (
        CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0
        | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1
        | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2
        | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3
        | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4
        | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5
        | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6
        | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7
    )
    change: CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        window_months: int
        if isinstance(
            self.window_months,
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6,
        ):
            window_months = self.window_months.value
        else:
            window_months = self.window_months.value

        change = self.change.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "windowMonths": window_months,
                "change": change,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_change import (
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Type(d.pop("type"))

        def _parse_window_months(
            data: object,
        ) -> (
            CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0
            | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1
            | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2
            | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3
            | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4
            | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5
            | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6
            | CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7
        ):
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_0 = (
                    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0(data)
                )

                return window_months_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_1 = (
                    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1(data)
                )

                return window_months_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_2 = (
                    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2(data)
                )

                return window_months_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_3 = (
                    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3(data)
                )

                return window_months_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_4 = (
                    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4(data)
                )

                return window_months_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_5 = (
                    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5(data)
                )

                return window_months_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_6 = (
                    CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6(data)
                )

                return window_months_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            window_months_type_7 = (
                CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7(data)
            )

            return window_months_type_7

        window_months = _parse_window_months(d.pop("windowMonths"))

        change = CompanySearchBodySearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change.from_dict(
            d.pop("change")
        )

        company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1 = cls(
            type_=type_,
            window_months=window_months,
            change=change,
        )

        company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1.additional_properties = d
        return company_search_body_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1

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
