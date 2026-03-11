from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_company_logos_body_companies_identifier_type_0 import (
        BulkCompanyLogosBodyCompaniesIdentifierType0,
    )
    from ..models.bulk_company_logos_body_companies_identifier_type_1 import (
        BulkCompanyLogosBodyCompaniesIdentifierType1,
    )
    from ..models.bulk_company_logos_body_companies_identifier_type_2 import (
        BulkCompanyLogosBodyCompaniesIdentifierType2,
    )


T = TypeVar("T", bound="BulkCompanyLogosBody")


@_attrs_define
class BulkCompanyLogosBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        companies_identifier (BulkCompanyLogosBodyCompaniesIdentifierType0 |
            BulkCompanyLogosBodyCompaniesIdentifierType1 | BulkCompanyLogosBodyCompaniesIdentifierType2): The list of
            companies to get the logo for. Include any of domain, linkedinUrl, or liOrgId. Max 10000 companies can be added
            at a time.
    """

    api_key: str
    companies_identifier: (
        BulkCompanyLogosBodyCompaniesIdentifierType0
        | BulkCompanyLogosBodyCompaniesIdentifierType1
        | BulkCompanyLogosBodyCompaniesIdentifierType2
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_company_logos_body_companies_identifier_type_0 import (
            BulkCompanyLogosBodyCompaniesIdentifierType0,
        )
        from ..models.bulk_company_logos_body_companies_identifier_type_1 import (
            BulkCompanyLogosBodyCompaniesIdentifierType1,
        )

        api_key = self.api_key

        companies_identifier: dict[str, Any]
        if isinstance(self.companies_identifier, BulkCompanyLogosBodyCompaniesIdentifierType0):
            companies_identifier = self.companies_identifier.to_dict()
        elif isinstance(self.companies_identifier, BulkCompanyLogosBodyCompaniesIdentifierType1):
            companies_identifier = self.companies_identifier.to_dict()
        else:
            companies_identifier = self.companies_identifier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "companiesIdentifier": companies_identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_company_logos_body_companies_identifier_type_0 import (
            BulkCompanyLogosBodyCompaniesIdentifierType0,
        )
        from ..models.bulk_company_logos_body_companies_identifier_type_1 import (
            BulkCompanyLogosBodyCompaniesIdentifierType1,
        )
        from ..models.bulk_company_logos_body_companies_identifier_type_2 import (
            BulkCompanyLogosBodyCompaniesIdentifierType2,
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_companies_identifier(
            data: object,
        ) -> (
            BulkCompanyLogosBodyCompaniesIdentifierType0
            | BulkCompanyLogosBodyCompaniesIdentifierType1
            | BulkCompanyLogosBodyCompaniesIdentifierType2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                companies_identifier_type_0 = BulkCompanyLogosBodyCompaniesIdentifierType0.from_dict(data)

                return companies_identifier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                companies_identifier_type_1 = BulkCompanyLogosBodyCompaniesIdentifierType1.from_dict(data)

                return companies_identifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            companies_identifier_type_2 = BulkCompanyLogosBodyCompaniesIdentifierType2.from_dict(data)

            return companies_identifier_type_2

        companies_identifier = _parse_companies_identifier(d.pop("companiesIdentifier"))

        bulk_company_logos_body = cls(
            api_key=api_key,
            companies_identifier=companies_identifier,
        )

        bulk_company_logos_body.additional_properties = d
        return bulk_company_logos_body

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
