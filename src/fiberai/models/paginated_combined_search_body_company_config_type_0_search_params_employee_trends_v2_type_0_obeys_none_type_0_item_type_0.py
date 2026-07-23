from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_type import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0Type,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_window_months_type_0 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType0,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_window_months_type_1 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType1,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_window_months_type_2 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType2,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_window_months_type_3 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType3,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_window_months_type_4 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType4,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_window_months_type_5 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType5,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_window_months_type_6 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType6,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_window_months_type_7 import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType7,
)

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_change import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0Change,
    )


T = TypeVar(
    "T", bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0"
)


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0:
    """
    Attributes:
        type_
            (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0Type):
        window_months (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemT
            ype0WindowMonthsType0 | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneT
            ype0ItemType0WindowMonthsType1 | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0O
            beysNoneType0ItemType0WindowMonthsType2 | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrend
            sV2Type0ObeysNoneType0ItemType0WindowMonthsType3 | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmpl
            oyeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType4 | PaginatedCombinedSearchBodyCompanyConfigType0SearchP
            aramsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType5 | PaginatedCombinedSearchBodyCompanyConfigTyp
            e0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType6 | PaginatedCombinedSearchBodyCompany
            ConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType7):
        change
            (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0Change):
    """

    type_: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0Type
    window_months: (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType0
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType1
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType2
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType3
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType4
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType5
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType6
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType7
    )
    change: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0Change
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        window_months: int
        if isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType0,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType1,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType2,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType3,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType4,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType5,
        ):
            window_months = self.window_months.value
        elif isinstance(
            self.window_months,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType6,
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
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0_change import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0Change,
        )

        d = dict(src_dict)
        type_ = (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0Type(
                d.pop("type")
            )
        )

        def _parse_window_months(
            data: object,
        ) -> (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType0
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType1
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType2
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType3
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType4
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType5
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType6
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType7
        ):
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType0(
                    data
                )

                return window_months_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_1 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType1(
                    data
                )

                return window_months_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_2 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType2(
                    data
                )

                return window_months_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_3 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType3(
                    data
                )

                return window_months_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_4 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType4(
                    data
                )

                return window_months_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_5 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType5(
                    data
                )

                return window_months_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                window_months_type_6 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType6(
                    data
                )

                return window_months_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            window_months_type_7 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0WindowMonthsType7(
                data
            )

            return window_months_type_7

        window_months = _parse_window_months(d.pop("windowMonths"))

        change = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeeTrendsV2Type0ObeysNoneType0ItemType0Change.from_dict(
            d.pop("change")
        )

        paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0 = cls(
            type_=type_,
            window_months=window_months,
            change=change,
        )

        paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_employee_trends_v2_type_0_obeys_none_type_0_item_type_0

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
