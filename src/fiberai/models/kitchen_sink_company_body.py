from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kitchen_sink_company_body_company_domain_type_0 import KitchenSinkCompanyBodyCompanyDomainType0
    from ..models.kitchen_sink_company_body_company_identifier_type_0 import (
        KitchenSinkCompanyBodyCompanyIdentifierType0,
    )
    from ..models.kitchen_sink_company_body_company_identifier_type_1 import (
        KitchenSinkCompanyBodyCompanyIdentifierType1,
    )
    from ..models.kitchen_sink_company_body_company_identifier_type_2 import (
        KitchenSinkCompanyBodyCompanyIdentifierType2,
    )
    from ..models.kitchen_sink_company_body_company_name_type_0 import KitchenSinkCompanyBodyCompanyNameType0


T = TypeVar("T", bound="KitchenSinkCompanyBody")


@_attrs_define
class KitchenSinkCompanyBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company_identifier (KitchenSinkCompanyBodyCompanyIdentifierType0 | KitchenSinkCompanyBodyCompanyIdentifierType1
            | KitchenSinkCompanyBodyCompanyIdentifierType2 | None | Unset):
        company_name (KitchenSinkCompanyBodyCompanyNameType0 | None | Unset):
        company_domain (KitchenSinkCompanyBodyCompanyDomainType0 | None | Unset):
        num_companies (int | Unset):  Default: 1.
    """

    api_key: str
    company_identifier: (
        KitchenSinkCompanyBodyCompanyIdentifierType0
        | KitchenSinkCompanyBodyCompanyIdentifierType1
        | KitchenSinkCompanyBodyCompanyIdentifierType2
        | None
        | Unset
    ) = UNSET
    company_name: KitchenSinkCompanyBodyCompanyNameType0 | None | Unset = UNSET
    company_domain: KitchenSinkCompanyBodyCompanyDomainType0 | None | Unset = UNSET
    num_companies: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.kitchen_sink_company_body_company_domain_type_0 import KitchenSinkCompanyBodyCompanyDomainType0
        from ..models.kitchen_sink_company_body_company_identifier_type_0 import (
            KitchenSinkCompanyBodyCompanyIdentifierType0,
        )
        from ..models.kitchen_sink_company_body_company_identifier_type_1 import (
            KitchenSinkCompanyBodyCompanyIdentifierType1,
        )
        from ..models.kitchen_sink_company_body_company_identifier_type_2 import (
            KitchenSinkCompanyBodyCompanyIdentifierType2,
        )
        from ..models.kitchen_sink_company_body_company_name_type_0 import KitchenSinkCompanyBodyCompanyNameType0

        api_key = self.api_key

        company_identifier: dict[str, Any] | None | Unset
        if isinstance(self.company_identifier, Unset):
            company_identifier = UNSET
        elif isinstance(self.company_identifier, KitchenSinkCompanyBodyCompanyIdentifierType0):
            company_identifier = self.company_identifier.to_dict()
        elif isinstance(self.company_identifier, KitchenSinkCompanyBodyCompanyIdentifierType1):
            company_identifier = self.company_identifier.to_dict()
        elif isinstance(self.company_identifier, KitchenSinkCompanyBodyCompanyIdentifierType2):
            company_identifier = self.company_identifier.to_dict()
        else:
            company_identifier = self.company_identifier

        company_name: dict[str, Any] | None | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        elif isinstance(self.company_name, KitchenSinkCompanyBodyCompanyNameType0):
            company_name = self.company_name.to_dict()
        else:
            company_name = self.company_name

        company_domain: dict[str, Any] | None | Unset
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        elif isinstance(self.company_domain, KitchenSinkCompanyBodyCompanyDomainType0):
            company_domain = self.company_domain.to_dict()
        else:
            company_domain = self.company_domain

        num_companies = self.num_companies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if company_identifier is not UNSET:
            field_dict["companyIdentifier"] = company_identifier
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_domain is not UNSET:
            field_dict["companyDomain"] = company_domain
        if num_companies is not UNSET:
            field_dict["numCompanies"] = num_companies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_company_body_company_domain_type_0 import KitchenSinkCompanyBodyCompanyDomainType0
        from ..models.kitchen_sink_company_body_company_identifier_type_0 import (
            KitchenSinkCompanyBodyCompanyIdentifierType0,
        )
        from ..models.kitchen_sink_company_body_company_identifier_type_1 import (
            KitchenSinkCompanyBodyCompanyIdentifierType1,
        )
        from ..models.kitchen_sink_company_body_company_identifier_type_2 import (
            KitchenSinkCompanyBodyCompanyIdentifierType2,
        )
        from ..models.kitchen_sink_company_body_company_name_type_0 import KitchenSinkCompanyBodyCompanyNameType0

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_company_identifier(
            data: object,
        ) -> (
            KitchenSinkCompanyBodyCompanyIdentifierType0
            | KitchenSinkCompanyBodyCompanyIdentifierType1
            | KitchenSinkCompanyBodyCompanyIdentifierType2
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
                company_identifier_type_0 = KitchenSinkCompanyBodyCompanyIdentifierType0.from_dict(data)

                return company_identifier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_1 = KitchenSinkCompanyBodyCompanyIdentifierType1.from_dict(data)

                return company_identifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_2 = KitchenSinkCompanyBodyCompanyIdentifierType2.from_dict(data)

                return company_identifier_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KitchenSinkCompanyBodyCompanyIdentifierType0
                | KitchenSinkCompanyBodyCompanyIdentifierType1
                | KitchenSinkCompanyBodyCompanyIdentifierType2
                | None
                | Unset,
                data,
            )

        company_identifier = _parse_company_identifier(d.pop("companyIdentifier", UNSET))

        def _parse_company_name(data: object) -> KitchenSinkCompanyBodyCompanyNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_name_type_0 = KitchenSinkCompanyBodyCompanyNameType0.from_dict(data)

                return company_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkCompanyBodyCompanyNameType0 | None | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_company_domain(data: object) -> KitchenSinkCompanyBodyCompanyDomainType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_domain_type_0 = KitchenSinkCompanyBodyCompanyDomainType0.from_dict(data)

                return company_domain_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkCompanyBodyCompanyDomainType0 | None | Unset, data)

        company_domain = _parse_company_domain(d.pop("companyDomain", UNSET))

        num_companies = d.pop("numCompanies", UNSET)

        kitchen_sink_company_body = cls(
            api_key=api_key,
            company_identifier=company_identifier,
            company_name=company_name,
            company_domain=company_domain,
            num_companies=num_companies,
        )

        kitchen_sink_company_body.additional_properties = d
        return kitchen_sink_company_body

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
