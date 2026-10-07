from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0_standard_industries_type_0_item import (
    KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0StandardIndustriesType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0_employee_count_consensus_type_0 import (
        KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0EmployeeCountConsensusType0,
    )
    from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0_revenue_estimate_type_0 import (
        KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0RevenueEstimateType0,
    )


T = TypeVar("T", bound="KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0")


@_attrs_define
class KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0:
    """
    Attributes:
        linkedin_ids (list[str] | None | Unset):
        li_org_id (None | str | Unset):
        linkedin_primary_slug (None | str | Unset):
        domains (list[str] | None | Unset):
        preferred_name (None | str | Unset):
        crunchbase_slug (None | str | Unset):
        logo_url (None | str | Unset):
        standard_industries (list[KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDeta
            ilsType0StandardIndustriesType0Item] | None | Unset):
        li_industries (list[str] | None | Unset):
        employee_count_consensus (KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDeta
            ilsType0EmployeeCountConsensusType0 | None | Unset):
        revenue_estimate (KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0
            RevenueEstimateType0 | None | Unset):
    """

    linkedin_ids: list[str] | None | Unset = UNSET
    li_org_id: None | str | Unset = UNSET
    linkedin_primary_slug: None | str | Unset = UNSET
    domains: list[str] | None | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    crunchbase_slug: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    standard_industries: (
        list[
            KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0StandardIndustriesType0Item
        ]
        | None
        | Unset
    ) = UNSET
    li_industries: list[str] | None | Unset = UNSET
    employee_count_consensus: (
        KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0EmployeeCountConsensusType0
        | None
        | Unset
    ) = UNSET
    revenue_estimate: (
        KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0RevenueEstimateType0
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0_employee_count_consensus_type_0 import (
            KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0EmployeeCountConsensusType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0_revenue_estimate_type_0 import (
            KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0RevenueEstimateType0,  # noqa: PLC0415
        )

        linkedin_ids: list[str] | None | Unset
        if isinstance(self.linkedin_ids, Unset):
            linkedin_ids = UNSET
        elif isinstance(self.linkedin_ids, list):
            linkedin_ids = self.linkedin_ids

        else:
            linkedin_ids = self.linkedin_ids

        li_org_id: None | str | Unset
        if isinstance(self.li_org_id, Unset):
            li_org_id = UNSET
        else:
            li_org_id = self.li_org_id

        linkedin_primary_slug: None | str | Unset
        if isinstance(self.linkedin_primary_slug, Unset):
            linkedin_primary_slug = UNSET
        else:
            linkedin_primary_slug = self.linkedin_primary_slug

        domains: list[str] | None | Unset
        if isinstance(self.domains, Unset):
            domains = UNSET
        elif isinstance(self.domains, list):
            domains = self.domains

        else:
            domains = self.domains

        preferred_name: None | str | Unset
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        crunchbase_slug: None | str | Unset
        if isinstance(self.crunchbase_slug, Unset):
            crunchbase_slug = UNSET
        else:
            crunchbase_slug = self.crunchbase_slug

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        standard_industries: list[str] | None | Unset
        if isinstance(self.standard_industries, Unset):
            standard_industries = UNSET
        elif isinstance(self.standard_industries, list):
            standard_industries = []
            for standard_industries_type_0_item_data in self.standard_industries:
                standard_industries_type_0_item = standard_industries_type_0_item_data.value
                standard_industries.append(standard_industries_type_0_item)

        else:
            standard_industries = self.standard_industries

        li_industries: list[str] | None | Unset
        if isinstance(self.li_industries, Unset):
            li_industries = UNSET
        elif isinstance(self.li_industries, list):
            li_industries = self.li_industries

        else:
            li_industries = self.li_industries

        employee_count_consensus: dict[str, Any] | None | Unset
        if isinstance(self.employee_count_consensus, Unset):
            employee_count_consensus = UNSET
        elif isinstance(
            self.employee_count_consensus,
            KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0EmployeeCountConsensusType0,
        ):
            employee_count_consensus = self.employee_count_consensus.to_dict()
        else:
            employee_count_consensus = self.employee_count_consensus

        revenue_estimate: dict[str, Any] | None | Unset
        if isinstance(self.revenue_estimate, Unset):
            revenue_estimate = UNSET
        elif isinstance(
            self.revenue_estimate,
            KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0RevenueEstimateType0,
        ):
            revenue_estimate = self.revenue_estimate.to_dict()
        else:
            revenue_estimate = self.revenue_estimate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkedin_ids is not UNSET:
            field_dict["linkedin_ids"] = linkedin_ids
        if li_org_id is not UNSET:
            field_dict["li_org_id"] = li_org_id
        if linkedin_primary_slug is not UNSET:
            field_dict["linkedin_primary_slug"] = linkedin_primary_slug
        if domains is not UNSET:
            field_dict["domains"] = domains
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if crunchbase_slug is not UNSET:
            field_dict["crunchbase_slug"] = crunchbase_slug
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if standard_industries is not UNSET:
            field_dict["standard_industries"] = standard_industries
        if li_industries is not UNSET:
            field_dict["li_industries"] = li_industries
        if employee_count_consensus is not UNSET:
            field_dict["employee_count_consensus"] = employee_count_consensus
        if revenue_estimate is not UNSET:
            field_dict["revenue_estimate"] = revenue_estimate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0_employee_count_consensus_type_0 import (
            KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0EmployeeCountConsensusType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0_revenue_estimate_type_0 import (
            KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0RevenueEstimateType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_linkedin_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                linkedin_ids_type_0 = cast(list[str], data)

                return linkedin_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        linkedin_ids = _parse_linkedin_ids(d.pop("linkedin_ids", UNSET))

        def _parse_li_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        li_org_id = _parse_li_org_id(d.pop("li_org_id", UNSET))

        def _parse_linkedin_primary_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_primary_slug = _parse_linkedin_primary_slug(d.pop("linkedin_primary_slug", UNSET))

        def _parse_domains(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                domains_type_0 = cast(list[str], data)

                return domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        domains = _parse_domains(d.pop("domains", UNSET))

        def _parse_preferred_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        def _parse_crunchbase_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crunchbase_slug = _parse_crunchbase_slug(d.pop("crunchbase_slug", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_standard_industries(
            data: object,
        ) -> (
            list[
                KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0StandardIndustriesType0Item
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                standard_industries_type_0 = []
                _standard_industries_type_0 = data
                for standard_industries_type_0_item_data in _standard_industries_type_0:
                    standard_industries_type_0_item = KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0StandardIndustriesType0Item(
                        standard_industries_type_0_item_data
                    )

                    standard_industries_type_0.append(standard_industries_type_0_item)

                return standard_industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0StandardIndustriesType0Item
                ]
                | None
                | Unset,
                data,
            )

        standard_industries = _parse_standard_industries(d.pop("standard_industries", UNSET))

        def _parse_li_industries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                li_industries_type_0 = cast(list[str], data)

                return li_industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        li_industries = _parse_li_industries(d.pop("li_industries", UNSET))

        def _parse_employee_count_consensus(
            data: object,
        ) -> (
            KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0EmployeeCountConsensusType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_consensus_type_0 = KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0EmployeeCountConsensusType0.from_dict(
                    data
                )

                return employee_count_consensus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0EmployeeCountConsensusType0
                | None
                | Unset,
                data,
            )

        employee_count_consensus = _parse_employee_count_consensus(d.pop("employee_count_consensus", UNSET))

        def _parse_revenue_estimate(
            data: object,
        ) -> (
            KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0RevenueEstimateType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                revenue_estimate_type_0 = KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0RevenueEstimateType0.from_dict(
                    data
                )

                return revenue_estimate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KitchenSinkProfileResponse200OutputDataItemDetailedWorkExperiencesType0ItemCompanyDetailsType0RevenueEstimateType0
                | None
                | Unset,
                data,
            )

        revenue_estimate = _parse_revenue_estimate(d.pop("revenue_estimate", UNSET))

        kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0 = cls(
            linkedin_ids=linkedin_ids,
            li_org_id=li_org_id,
            linkedin_primary_slug=linkedin_primary_slug,
            domains=domains,
            preferred_name=preferred_name,
            crunchbase_slug=crunchbase_slug,
            logo_url=logo_url,
            standard_industries=standard_industries,
            li_industries=li_industries,
            employee_count_consensus=employee_count_consensus,
            revenue_estimate=revenue_estimate,
        )

        kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0.additional_properties = d
        return kitchen_sink_profile_response_200_output_data_item_detailed_work_experiences_type_0_item_company_details_type_0

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
