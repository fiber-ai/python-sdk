from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_company_revenue_body_company_metadata import GetCompanyRevenueBodyCompanyMetadata


T = TypeVar("T", bound="GetCompanyRevenueBody")


@_attrs_define
class GetCompanyRevenueBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company_metadata (GetCompanyRevenueBodyCompanyMetadata):
    """

    api_key: str
    company_metadata: GetCompanyRevenueBodyCompanyMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        company_metadata = self.company_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "companyMetadata": company_metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_company_revenue_body_company_metadata import (
            GetCompanyRevenueBodyCompanyMetadata,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        company_metadata = GetCompanyRevenueBodyCompanyMetadata.from_dict(d.pop("companyMetadata"))

        get_company_revenue_body = cls(
            api_key=api_key,
            company_metadata=company_metadata,
        )

        get_company_revenue_body.additional_properties = d
        return get_company_revenue_body

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
