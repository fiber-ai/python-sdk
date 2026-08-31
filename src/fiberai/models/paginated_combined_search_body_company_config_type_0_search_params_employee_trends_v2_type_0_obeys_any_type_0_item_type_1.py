from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_type import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1Type,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_window_months_type_0 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType0,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_window_months_type_1 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType1,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_window_months_type_2 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType2,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_window_months_type_3 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType3,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_window_months_type_4 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType4,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_window_months_type_5 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType5,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_window_months_type_6 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType6,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_window_months_type_7 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType7,
)

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_change import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1Change,
    )


T = TypeVar(
    "T", bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1"
)


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1:
    """
    Attributes:
        type_
            (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1Type):
        window_months (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemTy
            pe1WindowMonthsType0 | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyTyp
            e0ItemType1WindowMonthsType1 | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0Obe
            ysAnyType0ItemType1WindowMonthsType2 | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2
            Type0ObeysAnyType0ItemType1WindowMonthsType3 | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployee
            TrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType4 | PaginatedCombinedSearchBodyCompanyConfigType0SearchParams
            EmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType5 | PaginatedCombinedSearchBodyCompanyConfigType0Sear
            chParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType6 | PaginatedCombinedSearchBodyCompanyConfigT
            ype0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType7):
        change
            (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1Change):
    """

    type_: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1Type
    window_months: (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType0
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType1
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType2
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType3
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType4
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType5
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType6
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType7
    )
    change: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1Change
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        window_months: int
        if isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType0,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType1,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType2,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType3,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType4,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType5,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType6,
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
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1_change import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1Change,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1Type(
                d.pop("type")
            )
        )

        def _parse_window_months(
            data: object,
        ) -> (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType0
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType1
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType2
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType3
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType4
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType5
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType6
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType7
        ):
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType0(
                    data
                )

                return window_months_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_1 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType1(
                    data
                )

                return window_months_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_2 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType2(
                    data
                )

                return window_months_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_3 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType3(
                    data
                )

                return window_months_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_4 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType4(
                    data
                )

                return window_months_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_5 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType5(
                    data
                )

                return window_months_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_6 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType6(
                    data
                )

                return window_months_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            window_months_type_7 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1WindowMonthsType7(
                data
            )

            return window_months_type_7

        window_months = _parse_window_months(d.pop("windowMonths"))

        change = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysAnyType0ItemType1Change.from_dict(
            d.pop("change")
        )

        paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1 = cls(
            type_=type_,
            window_months=window_months,
            change=change,
        )

        paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_any_type_0_item_type_1

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
