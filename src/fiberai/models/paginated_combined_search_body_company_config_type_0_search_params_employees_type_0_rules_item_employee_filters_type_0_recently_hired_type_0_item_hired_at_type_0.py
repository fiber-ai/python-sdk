from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0_strategy import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0Strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0_range_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0RangeType0,
    )


T = TypeVar(
    "T",
    bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0",
)


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0:
    """
    Attributes:
        strategy (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0Re
            centlyHiredType0ItemHiredAtType0Strategy):
        range_ (None | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersTy
            pe0RecentlyHiredType0ItemHiredAtType0RangeType0 | Unset):
    """

    strategy: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0Strategy
    range_: (
        None
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0RangeType0
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0_range_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0RangeType0,  # noqa: PLC0415
        )

        strategy = self.strategy.value

        range_: dict[str, Any] | None | Unset
        if isinstance(self.range_, Unset):
            range_ = UNSET
        elif isinstance(
            self.range_,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0RangeType0,
        ):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
            }
        )
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0_range_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0RangeType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        strategy = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0Strategy(
            d.pop("strategy")
        )

        def _parse_range_(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0RangeType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0RangeType0.from_dict(
                    data
                )

                return range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsEmployeesType0RulesItemEmployeeFiltersType0RecentlyHiredType0ItemHiredAtType0RangeType0
                | Unset,
                data,
            )

        range_ = _parse_range_(d.pop("range", UNSET))

        paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0 = cls(
            strategy=strategy,
            range_=range_,
        )

        paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_employees_type_0_rules_item_employee_filters_type_0_recently_hired_type_0_item_hired_at_type_0

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
