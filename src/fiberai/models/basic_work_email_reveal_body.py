from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.basic_work_email_reveal_body_company_type_0 import BasicWorkEmailRevealBodyCompanyType0
    from ..models.basic_work_email_reveal_body_company_type_1 import BasicWorkEmailRevealBodyCompanyType1
    from ..models.basic_work_email_reveal_body_name_type_0 import BasicWorkEmailRevealBodyNameType0
    from ..models.basic_work_email_reveal_body_name_type_1 import BasicWorkEmailRevealBodyNameType1


T = TypeVar("T", bound="BasicWorkEmailRevealBody")


@_attrs_define
class BasicWorkEmailRevealBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        name (BasicWorkEmailRevealBodyNameType0 | BasicWorkEmailRevealBodyNameType1): Person name. Provide a full name,
            or first and last name separately.
        company (BasicWorkEmailRevealBodyCompanyType0 | BasicWorkEmailRevealBodyCompanyType1): Company to search.
            Provide a domain, or a company identifier.
    """

    api_key: str
    name: BasicWorkEmailRevealBodyNameType0 | BasicWorkEmailRevealBodyNameType1
    company: BasicWorkEmailRevealBodyCompanyType0 | BasicWorkEmailRevealBodyCompanyType1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.basic_work_email_reveal_body_company_type_0 import (
            BasicWorkEmailRevealBodyCompanyType0,  # noqa: PLC0415
        )
        from ..models.basic_work_email_reveal_body_name_type_0 import BasicWorkEmailRevealBodyNameType0  # noqa: PLC0415

        api_key = self.api_key

        name: dict[str, Any]
        if isinstance(self.name, BasicWorkEmailRevealBodyNameType0):
            name = self.name.to_dict()
        else:
            name = self.name.to_dict()

        company: dict[str, Any]
        if isinstance(self.company, BasicWorkEmailRevealBodyCompanyType0):
            company = self.company.to_dict()
        else:
            company = self.company.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "name": name,
                "company": company,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_work_email_reveal_body_company_type_0 import (
            BasicWorkEmailRevealBodyCompanyType0,  # noqa: PLC0415
        )
        from ..models.basic_work_email_reveal_body_company_type_1 import (
            BasicWorkEmailRevealBodyCompanyType1,  # noqa: PLC0415
        )
        from ..models.basic_work_email_reveal_body_name_type_0 import BasicWorkEmailRevealBodyNameType0  # noqa: PLC0415
        from ..models.basic_work_email_reveal_body_name_type_1 import BasicWorkEmailRevealBodyNameType1  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_name(data: object) -> BasicWorkEmailRevealBodyNameType0 | BasicWorkEmailRevealBodyNameType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_0 = BasicWorkEmailRevealBodyNameType0.from_dict(data)

                return name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            name_type_1 = BasicWorkEmailRevealBodyNameType1.from_dict(data)

            return name_type_1

        name = _parse_name(d.pop("name"))

        def _parse_company(data: object) -> BasicWorkEmailRevealBodyCompanyType0 | BasicWorkEmailRevealBodyCompanyType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = BasicWorkEmailRevealBodyCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            company_type_1 = BasicWorkEmailRevealBodyCompanyType1.from_dict(data)

            return company_type_1

        company = _parse_company(d.pop("company"))

        basic_work_email_reveal_body = cls(
            api_key=api_key,
            name=name,
            company=company,
        )

        basic_work_email_reveal_body.additional_properties = d
        return basic_work_email_reveal_body

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
