from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookalikes_single_body_filters_type_0 import LookalikesSingleBodyFiltersType0


T = TypeVar("T", bound="LookalikesSingleBody")


@_attrs_define
class LookalikesSingleBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        domain (str): The company to find lookalikes for, identified by its domain, like 'example.com'.
        limit (int | Unset): How many lookalike companies to return. The best matches come first, with scores and a
            reason; the companies after them are ranked by similarity and have no scores. You are charged only for the
            companies returned. Default: 100.
        filters (LookalikesSingleBodyFiltersType0 | None | Unset): Only return lookalikes that match these company
            search filters — the same object company search takes, so you can reuse your company search filters as-is.
            Filters that pick specific companies and employee-based filters are not accepted; use exclusion lists to leave
            companies out. A filter you set replaces our own criteria for that field (lists you exclude are added to them).
            Omit to return lookalikes of any kind.
        company_exclusion_list_i_ds (list[str] | None | Unset): IDs of your company exclusion lists, up to 20. Companies
            in these lists, and in your organization-wide exclusion lists, are never returned — for example your existing
            customers. Create and fill lists with the company exclusion list endpoints.
    """

    api_key: str
    domain: str
    limit: int | Unset = 100
    filters: LookalikesSingleBodyFiltersType0 | None | Unset = UNSET
    company_exclusion_list_i_ds: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lookalikes_single_body_filters_type_0 import LookalikesSingleBodyFiltersType0  # noqa: PLC0415

        api_key = self.api_key

        domain = self.domain

        limit = self.limit

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, LookalikesSingleBodyFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        company_exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.company_exclusion_list_i_ds, Unset):
            company_exclusion_list_i_ds = UNSET
        elif isinstance(self.company_exclusion_list_i_ds, list):
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        else:
            company_exclusion_list_i_ds = self.company_exclusion_list_i_ds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "domain": domain,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if filters is not UNSET:
            field_dict["filters"] = filters
        if company_exclusion_list_i_ds is not UNSET:
            field_dict["companyExclusionListIDs"] = company_exclusion_list_i_ds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookalikes_single_body_filters_type_0 import LookalikesSingleBodyFiltersType0  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        domain = d.pop("domain")

        limit = d.pop("limit", UNSET)

        def _parse_filters(data: object) -> LookalikesSingleBodyFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = LookalikesSingleBodyFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LookalikesSingleBodyFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

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

        lookalikes_single_body = cls(
            api_key=api_key,
            domain=domain,
            limit=limit,
            filters=filters,
            company_exclusion_list_i_ds=company_exclusion_list_i_ds,
        )

        lookalikes_single_body.additional_properties = d
        return lookalikes_single_body

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
