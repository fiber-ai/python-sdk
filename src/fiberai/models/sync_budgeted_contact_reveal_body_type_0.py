from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_budgeted_contact_reveal_body_type_0_depth import SyncBudgetedContactRevealBodyType0Depth
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_0 import (
        SyncBudgetedContactRevealBodyType0CompanyType0,
    )
    from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_1 import (
        SyncBudgetedContactRevealBodyType0CompanyType1,
    )
    from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_2 import (
        SyncBudgetedContactRevealBodyType0CompanyType2,
    )
    from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_3 import (
        SyncBudgetedContactRevealBodyType0CompanyType3,
    )
    from ..models.sync_budgeted_contact_reveal_body_type_0_enrichment_type import (
        SyncBudgetedContactRevealBodyType0EnrichmentType,
    )


T = TypeVar("T", bound="SyncBudgetedContactRevealBodyType0")


@_attrs_define
class SyncBudgetedContactRevealBodyType0:
    """
    Attributes:
        api_key (str): Your Fiber API key
        linkedin_url (str): The person's LinkedIn identifier. Accepts a full LinkedIn profile URL (e.g.
            'https://www.linkedin.com/in/williamhgates/'), a bare slug (e.g. 'williamhgates'), a Sales Navigator URN (e.g.
            'ACwAAA-001MBbIvJon'), or a numeric LinkedIn user ID (e.g. '443105112').
        depth (SyncBudgetedContactRevealBodyType0Depth): Stored contact details only — no deliverability check. Waits 10
            seconds when timeBudgetMs is omitted. Priced by this choice and what is delivered, not by how long the lookup
            takes.
        enrichment_type (SyncBudgetedContactRevealBodyType0EnrichmentType | Unset): Which email and phone types to look
            for.
        time_budget_ms (int | None | Unset): How long this call may run, in milliseconds. Omit to use the default for
            the chosen depth.
        company (None | SyncBudgetedContactRevealBodyType0CompanyType0 | SyncBudgetedContactRevealBodyType0CompanyType1
            | SyncBudgetedContactRevealBodyType0CompanyType2 | SyncBudgetedContactRevealBodyType0CompanyType3 | Unset):
            Optional current company of the person. When provided, work emails whose domain does not match this company are
            returned in unmatchedWorkEmails instead of emails. Set identifier to 'linkedinUrl', 'linkedinSlug',
            'linkedinOrgId', or 'domain' and provide the corresponding value.
    """

    api_key: str
    linkedin_url: str
    depth: SyncBudgetedContactRevealBodyType0Depth
    enrichment_type: SyncBudgetedContactRevealBodyType0EnrichmentType | Unset = UNSET
    time_budget_ms: int | None | Unset = UNSET
    company: (
        None
        | SyncBudgetedContactRevealBodyType0CompanyType0
        | SyncBudgetedContactRevealBodyType0CompanyType1
        | SyncBudgetedContactRevealBodyType0CompanyType2
        | SyncBudgetedContactRevealBodyType0CompanyType3
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_0 import (
            SyncBudgetedContactRevealBodyType0CompanyType0,  # noqa: PLC0415
        )
        from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_1 import (
            SyncBudgetedContactRevealBodyType0CompanyType1,  # noqa: PLC0415
        )
        from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_2 import (
            SyncBudgetedContactRevealBodyType0CompanyType2,  # noqa: PLC0415
        )
        from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_3 import (
            SyncBudgetedContactRevealBodyType0CompanyType3,  # noqa: PLC0415
        )

        api_key = self.api_key

        linkedin_url = self.linkedin_url

        depth = self.depth.value

        enrichment_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enrichment_type, Unset):
            enrichment_type = self.enrichment_type.to_dict()

        time_budget_ms: int | None | Unset
        if isinstance(self.time_budget_ms, Unset):
            time_budget_ms = UNSET
        else:
            time_budget_ms = self.time_budget_ms

        company: dict[str, Any] | None | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        elif isinstance(self.company, SyncBudgetedContactRevealBodyType0CompanyType0):
            company = self.company.to_dict()
        elif isinstance(self.company, SyncBudgetedContactRevealBodyType0CompanyType1):
            company = self.company.to_dict()
        elif isinstance(self.company, SyncBudgetedContactRevealBodyType0CompanyType2):
            company = self.company.to_dict()
        elif isinstance(self.company, SyncBudgetedContactRevealBodyType0CompanyType3):
            company = self.company.to_dict()
        else:
            company = self.company

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "linkedinUrl": linkedin_url,
                "depth": depth,
            }
        )
        if enrichment_type is not UNSET:
            field_dict["enrichmentType"] = enrichment_type
        if time_budget_ms is not UNSET:
            field_dict["timeBudgetMs"] = time_budget_ms
        if company is not UNSET:
            field_dict["company"] = company

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_0 import (
            SyncBudgetedContactRevealBodyType0CompanyType0,  # noqa: PLC0415
        )
        from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_1 import (
            SyncBudgetedContactRevealBodyType0CompanyType1,  # noqa: PLC0415
        )
        from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_2 import (
            SyncBudgetedContactRevealBodyType0CompanyType2,  # noqa: PLC0415
        )
        from ..models.sync_budgeted_contact_reveal_body_type_0_company_type_3 import (
            SyncBudgetedContactRevealBodyType0CompanyType3,  # noqa: PLC0415
        )
        from ..models.sync_budgeted_contact_reveal_body_type_0_enrichment_type import (
            SyncBudgetedContactRevealBodyType0EnrichmentType,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        linkedin_url = d.pop("linkedinUrl")

        depth = SyncBudgetedContactRevealBodyType0Depth(d.pop("depth"))

        _enrichment_type = d.pop("enrichmentType", UNSET)
        enrichment_type: SyncBudgetedContactRevealBodyType0EnrichmentType | Unset
        if isinstance(_enrichment_type, Unset):
            enrichment_type = UNSET
        else:
            enrichment_type = SyncBudgetedContactRevealBodyType0EnrichmentType.from_dict(_enrichment_type)

        def _parse_time_budget_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_budget_ms = _parse_time_budget_ms(d.pop("timeBudgetMs", UNSET))

        def _parse_company(
            data: object,
        ) -> (
            None
            | SyncBudgetedContactRevealBodyType0CompanyType0
            | SyncBudgetedContactRevealBodyType0CompanyType1
            | SyncBudgetedContactRevealBodyType0CompanyType2
            | SyncBudgetedContactRevealBodyType0CompanyType3
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = SyncBudgetedContactRevealBodyType0CompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_1 = SyncBudgetedContactRevealBodyType0CompanyType1.from_dict(data)

                return company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_2 = SyncBudgetedContactRevealBodyType0CompanyType2.from_dict(data)

                return company_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_3 = SyncBudgetedContactRevealBodyType0CompanyType3.from_dict(data)

                return company_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SyncBudgetedContactRevealBodyType0CompanyType0
                | SyncBudgetedContactRevealBodyType0CompanyType1
                | SyncBudgetedContactRevealBodyType0CompanyType2
                | SyncBudgetedContactRevealBodyType0CompanyType3
                | Unset,
                data,
            )

        company = _parse_company(d.pop("company", UNSET))

        sync_budgeted_contact_reveal_body_type_0 = cls(
            api_key=api_key,
            linkedin_url=linkedin_url,
            depth=depth,
            enrichment_type=enrichment_type,
            time_budget_ms=time_budget_ms,
            company=company,
        )

        sync_budgeted_contact_reveal_body_type_0.additional_properties = d
        return sync_budgeted_contact_reveal_body_type_0

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
