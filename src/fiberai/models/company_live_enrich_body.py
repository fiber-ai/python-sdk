from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_live_enrich_body_type import CompanyLiveEnrichBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyLiveEnrichBody")


@_attrs_define
class CompanyLiveEnrichBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        type_ (CompanyLiveEnrichBodyType):
        value (str): The company's LinkedIn slug (e.g., 'microsoft'), LinkedIn URL (e.g.,
            'https://www.linkedin.com/company/microsoft' or 'https://www.linkedin.com/company/1441'), LinkedIn organization
            ID (e.g., '1441' for Google), or Fiber company ID (e.g., 'comp_1441')
        get_historical_headcount (bool | Unset): If true, we will attempt to compute the company's historical employee
            count and recent growth trends. No extra cost, but may take longer. Default: False.
    """

    api_key: str
    type_: CompanyLiveEnrichBodyType
    value: str
    get_historical_headcount: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        type_ = self.type_.value

        value = self.value

        get_historical_headcount = self.get_historical_headcount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "type": type_,
                "value": value,
            }
        )
        if get_historical_headcount is not UNSET:
            field_dict["getHistoricalHeadcount"] = get_historical_headcount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        type_ = CompanyLiveEnrichBodyType(d.pop("type"))

        value = d.pop("value")

        get_historical_headcount = d.pop("getHistoricalHeadcount", UNSET)

        company_live_enrich_body = cls(
            api_key=api_key,
            type_=type_,
            value=value,
            get_historical_headcount=get_historical_headcount,
        )

        company_live_enrich_body.additional_properties = d
        return company_live_enrich_body

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
