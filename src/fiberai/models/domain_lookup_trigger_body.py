from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domain_lookup_trigger_body_company_info_item import DomainLookupTriggerBodyCompanyInfoItem


T = TypeVar("T", bound="DomainLookupTriggerBody")


@_attrs_define
class DomainLookupTriggerBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        over_all_context (str): Descriptor of what your companies have in common and what they are. Like "British
            freight brokers" or "YC startups." Helps our agent disambiguate companies with similar names.
        company_info (list[DomainLookupTriggerBodyCompanyInfoItem]): List of companies to look up. Max 400 companies can
            be provided at a time.
    """

    api_key: str
    over_all_context: str
    company_info: list[DomainLookupTriggerBodyCompanyInfoItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        over_all_context = self.over_all_context

        company_info = []
        for company_info_item_data in self.company_info:
            company_info_item = company_info_item_data.to_dict()
            company_info.append(company_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "overAllContext": over_all_context,
                "companyInfo": company_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_lookup_trigger_body_company_info_item import DomainLookupTriggerBodyCompanyInfoItem

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        over_all_context = d.pop("overAllContext")

        company_info = []
        _company_info = d.pop("companyInfo")
        for company_info_item_data in _company_info:
            company_info_item = DomainLookupTriggerBodyCompanyInfoItem.from_dict(company_info_item_data)

            company_info.append(company_info_item)

        domain_lookup_trigger_body = cls(
            api_key=api_key,
            over_all_context=over_all_context,
            company_info=company_info,
        )

        domain_lookup_trigger_body.additional_properties = d
        return domain_lookup_trigger_body

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
