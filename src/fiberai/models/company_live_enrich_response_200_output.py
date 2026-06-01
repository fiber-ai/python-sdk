from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_live_enrich_response_200_output_company import CompanyLiveEnrichResponse200OutputCompany


T = TypeVar("T", bound="CompanyLiveEnrichResponse200Output")


@_attrs_define
class CompanyLiveEnrichResponse200Output:
    """
    Attributes:
        company (CompanyLiveEnrichResponse200OutputCompany): The enriched company data. A 404 status is returned if the
            company was not found.
        is_cached_404 (bool | None | Unset): True when the company is not found on LinkedIn but we have cached data in
            our database.
    """

    company: CompanyLiveEnrichResponse200OutputCompany
    is_cached_404: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company.to_dict()

        is_cached_404: bool | None | Unset
        if isinstance(self.is_cached_404, Unset):
            is_cached_404 = UNSET
        else:
            is_cached_404 = self.is_cached_404

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
            }
        )
        if is_cached_404 is not UNSET:
            field_dict["isCached404"] = is_cached_404

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_live_enrich_response_200_output_company import CompanyLiveEnrichResponse200OutputCompany

        d = dict(src_dict)
        company = CompanyLiveEnrichResponse200OutputCompany.from_dict(d.pop("company"))

        def _parse_is_cached_404(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_cached_404 = _parse_is_cached_404(d.pop("isCached404", UNSET))

        company_live_enrich_response_200_output = cls(
            company=company,
            is_cached_404=is_cached_404,
        )

        company_live_enrich_response_200_output.additional_properties = d
        return company_live_enrich_response_200_output

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
