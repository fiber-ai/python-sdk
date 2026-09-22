from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_turbo_contact_enrichment_body_patience_type_1 import SyncTurboContactEnrichmentBodyPatienceType1
from ..models.sync_turbo_contact_enrichment_body_patience_type_2_type_1 import (
    SyncTurboContactEnrichmentBodyPatienceType2Type1,
)
from ..models.sync_turbo_contact_enrichment_body_patience_type_3_type_1 import (
    SyncTurboContactEnrichmentBodyPatienceType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_turbo_contact_enrichment_body_company_type_0 import SyncTurboContactEnrichmentBodyCompanyType0
    from ..models.sync_turbo_contact_enrichment_body_company_type_1 import SyncTurboContactEnrichmentBodyCompanyType1
    from ..models.sync_turbo_contact_enrichment_body_company_type_2 import SyncTurboContactEnrichmentBodyCompanyType2
    from ..models.sync_turbo_contact_enrichment_body_company_type_3 import SyncTurboContactEnrichmentBodyCompanyType3
    from ..models.sync_turbo_contact_enrichment_body_enrichment_type import SyncTurboContactEnrichmentBodyEnrichmentType


T = TypeVar("T", bound="SyncTurboContactEnrichmentBody")


@_attrs_define
class SyncTurboContactEnrichmentBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        linkedin_url (str): The person's LinkedIn identifier. Accepts a full LinkedIn profile URL (e.g.
            'https://www.linkedin.com/in/williamhgates/'), a bare slug (e.g. 'williamhgates'), a Sales Navigator URN (e.g.
            'ACwAAA-001MBbIvJon'), or a numeric LinkedIn user ID (e.g. '443105112').
        enrichment_type (SyncTurboContactEnrichmentBodyEnrichmentType | Unset): The enrichment types to request. Credits
            are charged per selected type.
        patience (None | SyncTurboContactEnrichmentBodyPatienceType1 | SyncTurboContactEnrichmentBodyPatienceType2Type1
            | SyncTurboContactEnrichmentBodyPatienceType3Type1 | Unset): How long to wait for email deliverability
            validation after a contact is found. Higher patience increases average response time but improves deliverability
            accuracy. MINIMUM is the least thorough bounce-detection option.
        company (None | SyncTurboContactEnrichmentBodyCompanyType0 | SyncTurboContactEnrichmentBodyCompanyType1 |
            SyncTurboContactEnrichmentBodyCompanyType2 | SyncTurboContactEnrichmentBodyCompanyType3 | Unset): Optional
            current company of the person. When provided, work emails whose domain does not match this company are returned
            in unmatchedWorkEmails instead of emails. Set identifier to 'linkedinUrl', 'linkedinSlug', 'linkedinOrgId', or
            'domain' and provide the corresponding value.
    """

    api_key: str
    linkedin_url: str
    enrichment_type: SyncTurboContactEnrichmentBodyEnrichmentType | Unset = UNSET
    patience: (
        None
        | SyncTurboContactEnrichmentBodyPatienceType1
        | SyncTurboContactEnrichmentBodyPatienceType2Type1
        | SyncTurboContactEnrichmentBodyPatienceType3Type1
        | Unset
    ) = UNSET
    company: (
        None
        | SyncTurboContactEnrichmentBodyCompanyType0
        | SyncTurboContactEnrichmentBodyCompanyType1
        | SyncTurboContactEnrichmentBodyCompanyType2
        | SyncTurboContactEnrichmentBodyCompanyType3
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_turbo_contact_enrichment_body_company_type_0 import (
            SyncTurboContactEnrichmentBodyCompanyType0,  # noqa: PLC0415
        )
        from ..models.sync_turbo_contact_enrichment_body_company_type_1 import (
            SyncTurboContactEnrichmentBodyCompanyType1,  # noqa: PLC0415
        )
        from ..models.sync_turbo_contact_enrichment_body_company_type_2 import (
            SyncTurboContactEnrichmentBodyCompanyType2,  # noqa: PLC0415
        )
        from ..models.sync_turbo_contact_enrichment_body_company_type_3 import (
            SyncTurboContactEnrichmentBodyCompanyType3,  # noqa: PLC0415
        )

        api_key = self.api_key

        linkedin_url = self.linkedin_url

        enrichment_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enrichment_type, Unset):
            enrichment_type = self.enrichment_type.to_dict()

        patience: None | str | Unset
        if isinstance(self.patience, Unset):
            patience = UNSET
        elif isinstance(self.patience, SyncTurboContactEnrichmentBodyPatienceType1):
            patience = self.patience.value
        elif isinstance(self.patience, SyncTurboContactEnrichmentBodyPatienceType2Type1):
            patience = self.patience.value
        elif isinstance(self.patience, SyncTurboContactEnrichmentBodyPatienceType3Type1):
            patience = self.patience.value
        else:
            patience = self.patience

        company: dict[str, Any] | None | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        elif isinstance(self.company, SyncTurboContactEnrichmentBodyCompanyType0):
            company = self.company.to_dict()
        elif isinstance(self.company, SyncTurboContactEnrichmentBodyCompanyType1):
            company = self.company.to_dict()
        elif isinstance(self.company, SyncTurboContactEnrichmentBodyCompanyType2):
            company = self.company.to_dict()
        elif isinstance(self.company, SyncTurboContactEnrichmentBodyCompanyType3):
            company = self.company.to_dict()
        else:
            company = self.company

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "linkedinUrl": linkedin_url,
            }
        )
        if enrichment_type is not UNSET:
            field_dict["enrichmentType"] = enrichment_type
        if patience is not UNSET:
            field_dict["patience"] = patience
        if company is not UNSET:
            field_dict["company"] = company

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_turbo_contact_enrichment_body_company_type_0 import (
            SyncTurboContactEnrichmentBodyCompanyType0,  # noqa: PLC0415
        )
        from ..models.sync_turbo_contact_enrichment_body_company_type_1 import (
            SyncTurboContactEnrichmentBodyCompanyType1,  # noqa: PLC0415
        )
        from ..models.sync_turbo_contact_enrichment_body_company_type_2 import (
            SyncTurboContactEnrichmentBodyCompanyType2,  # noqa: PLC0415
        )
        from ..models.sync_turbo_contact_enrichment_body_company_type_3 import (
            SyncTurboContactEnrichmentBodyCompanyType3,  # noqa: PLC0415
        )
        from ..models.sync_turbo_contact_enrichment_body_enrichment_type import (
            SyncTurboContactEnrichmentBodyEnrichmentType,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        linkedin_url = d.pop("linkedinUrl")

        _enrichment_type = d.pop("enrichmentType", UNSET)
        enrichment_type: SyncTurboContactEnrichmentBodyEnrichmentType | Unset
        if isinstance(_enrichment_type, Unset):
            enrichment_type = UNSET
        else:
            enrichment_type = SyncTurboContactEnrichmentBodyEnrichmentType.from_dict(_enrichment_type)

        def _parse_patience(
            data: object,
        ) -> (
            None
            | SyncTurboContactEnrichmentBodyPatienceType1
            | SyncTurboContactEnrichmentBodyPatienceType2Type1
            | SyncTurboContactEnrichmentBodyPatienceType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_1 = SyncTurboContactEnrichmentBodyPatienceType1(data)

                return patience_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_2_type_1 = SyncTurboContactEnrichmentBodyPatienceType2Type1(data)

                return patience_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_3_type_1 = SyncTurboContactEnrichmentBodyPatienceType3Type1(data)

                return patience_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SyncTurboContactEnrichmentBodyPatienceType1
                | SyncTurboContactEnrichmentBodyPatienceType2Type1
                | SyncTurboContactEnrichmentBodyPatienceType3Type1
                | Unset,
                data,
            )

        patience = _parse_patience(d.pop("patience", UNSET))

        def _parse_company(
            data: object,
        ) -> (
            None
            | SyncTurboContactEnrichmentBodyCompanyType0
            | SyncTurboContactEnrichmentBodyCompanyType1
            | SyncTurboContactEnrichmentBodyCompanyType2
            | SyncTurboContactEnrichmentBodyCompanyType3
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = SyncTurboContactEnrichmentBodyCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_1 = SyncTurboContactEnrichmentBodyCompanyType1.from_dict(data)

                return company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_2 = SyncTurboContactEnrichmentBodyCompanyType2.from_dict(data)

                return company_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_3 = SyncTurboContactEnrichmentBodyCompanyType3.from_dict(data)

                return company_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SyncTurboContactEnrichmentBodyCompanyType0
                | SyncTurboContactEnrichmentBodyCompanyType1
                | SyncTurboContactEnrichmentBodyCompanyType2
                | SyncTurboContactEnrichmentBodyCompanyType3
                | Unset,
                data,
            )

        company = _parse_company(d.pop("company", UNSET))

        sync_turbo_contact_enrichment_body = cls(
            api_key=api_key,
            linkedin_url=linkedin_url,
            enrichment_type=enrichment_type,
            patience=patience,
            company=company,
        )

        sync_turbo_contact_enrichment_body.additional_properties = d
        return sync_turbo_contact_enrichment_body

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
