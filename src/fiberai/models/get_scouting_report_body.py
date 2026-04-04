from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_scouting_report_body_company_type_0 import GetScoutingReportBodyCompanyType0
    from ..models.get_scouting_report_body_company_type_1 import GetScoutingReportBodyCompanyType1
    from ..models.get_scouting_report_body_company_type_2 import GetScoutingReportBodyCompanyType2
    from ..models.get_scouting_report_body_company_type_3 import GetScoutingReportBodyCompanyType3


T = TypeVar("T", bound="GetScoutingReportBody")


@_attrs_define
class GetScoutingReportBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company (GetScoutingReportBodyCompanyType0 | GetScoutingReportBodyCompanyType1 |
            GetScoutingReportBodyCompanyType2 | GetScoutingReportBodyCompanyType3): Company identifier. Set identifier to
            'linkedinUrl', 'linkedinSlug', 'linkedinOrgId', or 'domain' and provide the corresponding value.
    """

    api_key: str
    company: (
        GetScoutingReportBodyCompanyType0
        | GetScoutingReportBodyCompanyType1
        | GetScoutingReportBodyCompanyType2
        | GetScoutingReportBodyCompanyType3
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_scouting_report_body_company_type_0 import GetScoutingReportBodyCompanyType0
        from ..models.get_scouting_report_body_company_type_1 import GetScoutingReportBodyCompanyType1
        from ..models.get_scouting_report_body_company_type_2 import GetScoutingReportBodyCompanyType2

        api_key = self.api_key

        company: dict[str, Any]
        if isinstance(self.company, GetScoutingReportBodyCompanyType0):
            company = self.company.to_dict()
        elif isinstance(self.company, GetScoutingReportBodyCompanyType1):
            company = self.company.to_dict()
        elif isinstance(self.company, GetScoutingReportBodyCompanyType2):
            company = self.company.to_dict()
        else:
            company = self.company.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "company": company,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_scouting_report_body_company_type_0 import GetScoutingReportBodyCompanyType0
        from ..models.get_scouting_report_body_company_type_1 import GetScoutingReportBodyCompanyType1
        from ..models.get_scouting_report_body_company_type_2 import GetScoutingReportBodyCompanyType2
        from ..models.get_scouting_report_body_company_type_3 import GetScoutingReportBodyCompanyType3

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_company(
            data: object,
        ) -> (
            GetScoutingReportBodyCompanyType0
            | GetScoutingReportBodyCompanyType1
            | GetScoutingReportBodyCompanyType2
            | GetScoutingReportBodyCompanyType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = GetScoutingReportBodyCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_1 = GetScoutingReportBodyCompanyType1.from_dict(data)

                return company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_2 = GetScoutingReportBodyCompanyType2.from_dict(data)

                return company_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            company_type_3 = GetScoutingReportBodyCompanyType3.from_dict(data)

            return company_type_3

        company = _parse_company(d.pop("company"))

        get_scouting_report_body = cls(
            api_key=api_key,
            company=company,
        )

        get_scouting_report_body.additional_properties = d
        return get_scouting_report_body

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
