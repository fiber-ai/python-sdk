from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.quick_company_resolve_body_companies_item_type_0 import QuickCompanyResolveBodyCompaniesItemType0
    from ..models.quick_company_resolve_body_companies_item_type_1 import QuickCompanyResolveBodyCompaniesItemType1
    from ..models.quick_company_resolve_body_companies_item_type_2 import QuickCompanyResolveBodyCompaniesItemType2
    from ..models.quick_company_resolve_body_companies_item_type_3 import QuickCompanyResolveBodyCompaniesItemType3


T = TypeVar("T", bound="QuickCompanyResolveBody")


@_attrs_define
class QuickCompanyResolveBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        companies (list[QuickCompanyResolveBodyCompaniesItemType0 | QuickCompanyResolveBodyCompaniesItemType1 |
            QuickCompanyResolveBodyCompaniesItemType2 | QuickCompanyResolveBodyCompaniesItemType3]): Companies to resolve.
            Each entry is an { identifier, value } pair where identifier is "linkedinSlug", "linkedinOrgId", "linkedinUrl",
            or "domain". Max 100 per request. You are charged only for the ones that resolve.
    """

    api_key: str
    companies: list[
        QuickCompanyResolveBodyCompaniesItemType0
        | QuickCompanyResolveBodyCompaniesItemType1
        | QuickCompanyResolveBodyCompaniesItemType2
        | QuickCompanyResolveBodyCompaniesItemType3
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_company_resolve_body_companies_item_type_0 import (
            QuickCompanyResolveBodyCompaniesItemType0,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_body_companies_item_type_1 import (
            QuickCompanyResolveBodyCompaniesItemType1,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_body_companies_item_type_2 import (
            QuickCompanyResolveBodyCompaniesItemType2,  # noqa: PLC0415
        )

        api_key = self.api_key

        companies = []
        for companies_item_data in self.companies:
            companies_item: dict[str, Any]
            if isinstance(companies_item_data, QuickCompanyResolveBodyCompaniesItemType0):
                companies_item = companies_item_data.to_dict()
            elif isinstance(companies_item_data, QuickCompanyResolveBodyCompaniesItemType1):
                companies_item = companies_item_data.to_dict()
            elif isinstance(companies_item_data, QuickCompanyResolveBodyCompaniesItemType2):
                companies_item = companies_item_data.to_dict()
            else:
                companies_item = companies_item_data.to_dict()

            companies.append(companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "companies": companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_company_resolve_body_companies_item_type_0 import (
            QuickCompanyResolveBodyCompaniesItemType0,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_body_companies_item_type_1 import (
            QuickCompanyResolveBodyCompaniesItemType1,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_body_companies_item_type_2 import (
            QuickCompanyResolveBodyCompaniesItemType2,  # noqa: PLC0415
        )
        from ..models.quick_company_resolve_body_companies_item_type_3 import (
            QuickCompanyResolveBodyCompaniesItemType3,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:

            def _parse_companies_item(
                data: object,
            ) -> (
                QuickCompanyResolveBodyCompaniesItemType0
                | QuickCompanyResolveBodyCompaniesItemType1
                | QuickCompanyResolveBodyCompaniesItemType2
                | QuickCompanyResolveBodyCompaniesItemType3
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    companies_item_type_0 = QuickCompanyResolveBodyCompaniesItemType0.from_dict(data)

                    return companies_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    companies_item_type_1 = QuickCompanyResolveBodyCompaniesItemType1.from_dict(data)

                    return companies_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    companies_item_type_2 = QuickCompanyResolveBodyCompaniesItemType2.from_dict(data)

                    return companies_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                companies_item_type_3 = QuickCompanyResolveBodyCompaniesItemType3.from_dict(data)

                return companies_item_type_3

            companies_item = _parse_companies_item(companies_item_data)

            companies.append(companies_item)

        quick_company_resolve_body = cls(
            api_key=api_key,
            companies=companies,
        )

        quick_company_resolve_body.additional_properties = d
        return quick_company_resolve_body

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
