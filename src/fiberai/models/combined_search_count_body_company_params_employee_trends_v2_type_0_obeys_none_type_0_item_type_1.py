from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_type import (
    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Type,
)
from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_0 import (
    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0,
)
from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_1 import (
    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1,
)
from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_2 import (
    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2,
)
from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_3 import (
    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3,
)
from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_4 import (
    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4,
)
from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_5 import (
    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5,
)
from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_6 import (
    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6,
)
from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_window_months_type_7 import (
    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7,
)

if TYPE_CHECKING:
    from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_change import (
        CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change,
    )


T = TypeVar("T", bound="CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1")


@_attrs_define
class CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1:
    """
    Attributes:
        type_ (CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Type):
        window_months (CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0
            | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1 |
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2 |
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3 |
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4 |
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5 |
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6 |
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7):
        change (CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change):
    """

    type_: CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Type
    window_months: (
        CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0
        | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1
        | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2
        | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3
        | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4
        | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5
        | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6
        | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7
    )
    change: CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        window_months: int
        if isinstance(
            self.window_months,
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6,
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
        from ..models.combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1_change import (
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Type(d.pop("type"))

        def _parse_window_months(
            data: object,
        ) -> (
            CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0
            | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1
            | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2
            | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3
            | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4
            | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5
            | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6
            | CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7
        ):
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_0 = (
                    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType0(
                        data
                    )
                )

                return window_months_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_1 = (
                    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType1(
                        data
                    )
                )

                return window_months_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_2 = (
                    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType2(
                        data
                    )
                )

                return window_months_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_3 = (
                    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType3(
                        data
                    )
                )

                return window_months_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_4 = (
                    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType4(
                        data
                    )
                )

                return window_months_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_5 = (
                    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType5(
                        data
                    )
                )

                return window_months_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_6 = (
                    CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType6(
                        data
                    )
                )

                return window_months_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            window_months_type_7 = (
                CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1WindowMonthsType7(data)
            )

            return window_months_type_7

        window_months = _parse_window_months(d.pop("windowMonths"))

        change = CombinedSearchCountBodyCompanyParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType1Change.from_dict(
            d.pop("change")
        )

        combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1 = cls(
            type_=type_,
            window_months=window_months,
            change=change,
        )

        combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1.additional_properties = d
        return combined_search_count_body_company_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_1

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
