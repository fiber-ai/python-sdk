from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_search_body_search_params_revenue_usd_type_0_max_type_0 import (
        CompanySearchBodySearchParamsRevenueUSDType0MaxType0,
    )
    from ..models.company_search_body_search_params_revenue_usd_type_0_min_type_0 import (
        CompanySearchBodySearchParamsRevenueUSDType0MinType0,
    )


T = TypeVar("T", bound="CompanySearchBodySearchParamsRevenueUSDType0")


@_attrs_define
class CompanySearchBodySearchParamsRevenueUSDType0:
    """
    Attributes:
        min_ (CompanySearchBodySearchParamsRevenueUSDType0MinType0 | None | Unset):
        max_ (CompanySearchBodySearchParamsRevenueUSDType0MaxType0 | None | Unset):
    """

    min_: CompanySearchBodySearchParamsRevenueUSDType0MinType0 | None | Unset = UNSET
    max_: CompanySearchBodySearchParamsRevenueUSDType0MaxType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_body_search_params_revenue_usd_type_0_max_type_0 import (
            CompanySearchBodySearchParamsRevenueUSDType0MaxType0,
        )
        from ..models.company_search_body_search_params_revenue_usd_type_0_min_type_0 import (
            CompanySearchBodySearchParamsRevenueUSDType0MinType0,
        )

        min_: dict[str, Any] | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        elif isinstance(self.min_, CompanySearchBodySearchParamsRevenueUSDType0MinType0):
            min_ = self.min_.to_dict()
        else:
            min_ = self.min_

        max_: dict[str, Any] | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        elif isinstance(self.max_, CompanySearchBodySearchParamsRevenueUSDType0MaxType0):
            max_ = self.max_.to_dict()
        else:
            max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params_revenue_usd_type_0_max_type_0 import (
            CompanySearchBodySearchParamsRevenueUSDType0MaxType0,
        )
        from ..models.company_search_body_search_params_revenue_usd_type_0_min_type_0 import (
            CompanySearchBodySearchParamsRevenueUSDType0MinType0,
        )

        d = dict(src_dict)

        def _parse_min_(data: object) -> CompanySearchBodySearchParamsRevenueUSDType0MinType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                min_type_0 = CompanySearchBodySearchParamsRevenueUSDType0MinType0.from_dict(data)

                return min_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanySearchBodySearchParamsRevenueUSDType0MinType0 | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        def _parse_max_(data: object) -> CompanySearchBodySearchParamsRevenueUSDType0MaxType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                max_type_0 = CompanySearchBodySearchParamsRevenueUSDType0MaxType0.from_dict(data)

                return max_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanySearchBodySearchParamsRevenueUSDType0MaxType0 | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        company_search_body_search_params_revenue_usd_type_0 = cls(
            min_=min_,
            max_=max_,
        )

        company_search_body_search_params_revenue_usd_type_0.additional_properties = d
        return company_search_body_search_params_revenue_usd_type_0

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
