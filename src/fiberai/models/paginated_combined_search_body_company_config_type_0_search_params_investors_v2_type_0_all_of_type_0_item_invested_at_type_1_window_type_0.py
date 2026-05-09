from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0_all_of_type_0_item_invested_at_type_1_window_type_0_method import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType0Method,
)
from ..models.paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0_all_of_type_0_item_invested_at_type_1_window_type_0_period import (
    PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType0Period,
)

T = TypeVar(
    "T",
    bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType0",
)


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType0:
    """
    Attributes:
        method (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1Wi
            ndowType0Method):
        period (PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1Wi
            ndowType0Period):
        quantity (float):
    """

    method: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType0Method
    period: PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType0Period
    quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        period = self.period.value

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "period": period,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType0Method(
            d.pop("method")
        )

        period = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType0Period(
            d.pop("period")
        )

        quantity = d.pop("quantity")

        paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0_all_of_type_0_item_invested_at_type_1_window_type_0 = cls(
            method=method,
            period=period,
            quantity=quantity,
        )

        paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0_all_of_type_0_item_invested_at_type_1_window_type_0.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_investors_v2_type_0_all_of_type_0_item_invested_at_type_1_window_type_0

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
