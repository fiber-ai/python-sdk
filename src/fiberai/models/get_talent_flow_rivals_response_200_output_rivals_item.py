from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTalentFlowRivalsResponse200OutputRivalsItem")


@_attrs_define
class GetTalentFlowRivalsResponse200OutputRivalsItem:
    """
    Attributes:
        company_name (str): Rival company name.
        gained_count (int): People who left this company to join the analyzed company within the window.
        lost_count (int): People who left the analyzed company to join this company within the window.
        net_count (int): gainedCount minus lostCount. Positive means the analyzed company gained more talent from this
            company than it lost to it.
        total_moves_count (int): Total two-way moves with this company (gainedCount plus lostCount).
        domain (None | str | Unset): Rival company website domain (e.g. 'stripe.com').
        linkedin_url (None | str | Unset): Rival company LinkedIn URL.
        linkedin_org_id (None | str | Unset): Rival company LinkedIn organization ID.
        stage (None | str | Unset): Rival company funding stage (e.g. 'Series A', 'IPO').
        total_funding_usd (float | None | Unset): Rival company total funding raised in USD, if available.
        valuation_usd (float | None | Unset): Rival company latest known valuation in USD, if available.
    """

    company_name: str
    gained_count: int
    lost_count: int
    net_count: int
    total_moves_count: int
    domain: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    linkedin_org_id: None | str | Unset = UNSET
    stage: None | str | Unset = UNSET
    total_funding_usd: float | None | Unset = UNSET
    valuation_usd: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        gained_count = self.gained_count

        lost_count = self.lost_count

        net_count = self.net_count

        total_moves_count = self.total_moves_count

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        linkedin_org_id: None | str | Unset
        if isinstance(self.linkedin_org_id, Unset):
            linkedin_org_id = UNSET
        else:
            linkedin_org_id = self.linkedin_org_id

        stage: None | str | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        else:
            stage = self.stage

        total_funding_usd: float | None | Unset
        if isinstance(self.total_funding_usd, Unset):
            total_funding_usd = UNSET
        else:
            total_funding_usd = self.total_funding_usd

        valuation_usd: float | None | Unset
        if isinstance(self.valuation_usd, Unset):
            valuation_usd = UNSET
        else:
            valuation_usd = self.valuation_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyName": company_name,
                "gainedCount": gained_count,
                "lostCount": lost_count,
                "netCount": net_count,
                "totalMovesCount": total_moves_count,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url
        if linkedin_org_id is not UNSET:
            field_dict["linkedinOrgId"] = linkedin_org_id
        if stage is not UNSET:
            field_dict["stage"] = stage
        if total_funding_usd is not UNSET:
            field_dict["totalFundingUsd"] = total_funding_usd
        if valuation_usd is not UNSET:
            field_dict["valuationUsd"] = valuation_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_name = d.pop("companyName")

        gained_count = d.pop("gainedCount")

        lost_count = d.pop("lostCount")

        net_count = d.pop("netCount")

        total_moves_count = d.pop("totalMovesCount")

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        def _parse_linkedin_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_org_id = _parse_linkedin_org_id(d.pop("linkedinOrgId", UNSET))

        def _parse_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_total_funding_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_funding_usd = _parse_total_funding_usd(d.pop("totalFundingUsd", UNSET))

        def _parse_valuation_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        valuation_usd = _parse_valuation_usd(d.pop("valuationUsd", UNSET))

        get_talent_flow_rivals_response_200_output_rivals_item = cls(
            company_name=company_name,
            gained_count=gained_count,
            lost_count=lost_count,
            net_count=net_count,
            total_moves_count=total_moves_count,
            domain=domain,
            linkedin_url=linkedin_url,
            linkedin_org_id=linkedin_org_id,
            stage=stage,
            total_funding_usd=total_funding_usd,
            valuation_usd=valuation_usd,
        )

        get_talent_flow_rivals_response_200_output_rivals_item.additional_properties = d
        return get_talent_flow_rivals_response_200_output_rivals_item

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
