from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompanyRevenueResponse200OutputRevenueInfoType0")


@_attrs_define
class GetCompanyRevenueResponse200OutputRevenueInfoType0:
    """Revenue information. Null means the company was found but no public revenue data is available.

    Attributes:
        lower_bound (float): Lower bound of the annual revenue estimate in USD
        upper_bound (float): Upper bound of the annual revenue estimate in USD
        fiscal_year (float): Fiscal year the revenue figure corresponds to. Often (but not always) the most recent
            completed calendar year (e.g. 2025 as of 2026).
        citations (list[str]): Source URLs used to derive the revenue estimate. May be empty when the revenue figure is
            common knowledge to the AI model and no web sources were needed.
        comments (None | str | Unset): Additional context about the revenue data
    """

    lower_bound: float
    upper_bound: float
    fiscal_year: float
    citations: list[str]
    comments: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lower_bound = self.lower_bound

        upper_bound = self.upper_bound

        fiscal_year = self.fiscal_year

        citations = self.citations

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lowerBound": lower_bound,
                "upperBound": upper_bound,
                "fiscalYear": fiscal_year,
                "citations": citations,
            }
        )
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lower_bound = d.pop("lowerBound")

        upper_bound = d.pop("upperBound")

        fiscal_year = d.pop("fiscalYear")

        citations = cast(list[str], d.pop("citations"))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        get_company_revenue_response_200_output_revenue_info_type_0 = cls(
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            fiscal_year=fiscal_year,
            citations=citations,
            comments=comments,
        )

        get_company_revenue_response_200_output_revenue_info_type_0.additional_properties = d
        return get_company_revenue_response_200_output_revenue_info_type_0

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
