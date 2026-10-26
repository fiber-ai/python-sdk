from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookalikes_trigger_body_companies_item import LookalikesTriggerBodyCompaniesItem
    from ..models.lookalikes_trigger_body_filters_type_0 import LookalikesTriggerBodyFiltersType0


T = TypeVar("T", bound="LookalikesTriggerBody")


@_attrs_define
class LookalikesTriggerBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        companies (list[LookalikesTriggerBodyCompaniesItem]): The companies to find lookalikes for, identified by
            domain. Lists longer than 100 companies are grouped from a 100-company sample (your highest-importance companies
            first); every company you submit is still excluded from the results.
        max_buckets (int | Unset): Maximum number of company groupings (buckets) to build from your list. Default: 5.
        company_exclusion_list_i_ds (list[str] | None | Unset): IDs of your company exclusion lists, up to 20. Companies
            in these lists, and in your organization-wide exclusion lists, are never returned — for example your existing
            customers. Create and fill lists with the company exclusion list endpoints.
        filters (LookalikesTriggerBodyFiltersType0 | None | Unset): Only return lookalikes that match these company
            search filters — the same object company search takes, so you can reuse your company search filters as-is.
            Filters that pick specific companies and employee-based filters are not accepted; use exclusion lists to leave
            companies out. A filter you set replaces that part of each grouping's own search (lists you exclude are added to
            it). Omit to return lookalikes of any kind.
    """

    api_key: str
    companies: list[LookalikesTriggerBodyCompaniesItem]
    max_buckets: int | Unset = 5
    company_exclusion_list_i_ds: list[str] | None | Unset = UNSET
    filters: LookalikesTriggerBodyFiltersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lookalikes_trigger_body_filters_type_0 import LookalikesTriggerBodyFiltersType0  # noqa: PLC0415

        api_key = self.api_key

        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        max_buckets = self.max_buckets

        company_exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.company_exclusion_list_i_ds, Unset):
            company_exclusion_list_i_ds = UNSET
        elif isinstance(self.company_exclusion_list_i_ds, list):
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        else:
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, LookalikesTriggerBodyFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "companies": companies,
            }
        )
        if max_buckets is not UNSET:
            field_dict["maxBuckets"] = max_buckets
        if company_exclusion_list_i_ds is not UNSET:
            field_dict["companyExclusionListIDs"] = company_exclusion_list_i_ds
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookalikes_trigger_body_companies_item import LookalikesTriggerBodyCompaniesItem  # noqa: PLC0415
        from ..models.lookalikes_trigger_body_filters_type_0 import LookalikesTriggerBodyFiltersType0  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = LookalikesTriggerBodyCompaniesItem.from_dict(companies_item_data)

            companies.append(companies_item)

        max_buckets = d.pop("maxBuckets", UNSET)

        def _parse_company_exclusion_list_i_ds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                company_exclusion_list_i_ds_type_0 = cast(list[str], data)

                return company_exclusion_list_i_ds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        company_exclusion_list_i_ds = _parse_company_exclusion_list_i_ds(d.pop("companyExclusionListIDs", UNSET))

        def _parse_filters(data: object) -> LookalikesTriggerBodyFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = LookalikesTriggerBodyFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesTriggerBodyFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        lookalikes_trigger_body = cls(
            api_key=api_key,
            companies=companies,
            max_buckets=max_buckets,
            company_exclusion_list_i_ds=company_exclusion_list_i_ds,
            filters=filters,
        )

        lookalikes_trigger_body.additional_properties = d
        return lookalikes_trigger_body

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
