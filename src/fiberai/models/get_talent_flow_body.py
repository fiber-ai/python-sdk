from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_talent_flow_body_direction import GetTalentFlowBodyDirection

if TYPE_CHECKING:
    from ..models.get_talent_flow_body_company_type_0 import GetTalentFlowBodyCompanyType0
    from ..models.get_talent_flow_body_company_type_1 import GetTalentFlowBodyCompanyType1
    from ..models.get_talent_flow_body_company_type_2 import GetTalentFlowBodyCompanyType2
    from ..models.get_talent_flow_body_company_type_3 import GetTalentFlowBodyCompanyType3
    from ..models.get_talent_flow_body_date_range import GetTalentFlowBodyDateRange


T = TypeVar("T", bound="GetTalentFlowBody")


@_attrs_define
class GetTalentFlowBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company (GetTalentFlowBodyCompanyType0 | GetTalentFlowBodyCompanyType1 | GetTalentFlowBodyCompanyType2 |
            GetTalentFlowBodyCompanyType3): Company to analyze. Set identifier to 'linkedinUrl', 'linkedinSlug',
            'linkedinOrgId', or 'domain' and provide the corresponding value.
        direction (GetTalentFlowBodyDirection): Direction of talent flow. 'joiners' finds people who started at the
            company within the window and reports where they came from. 'leavers' finds people who left the company within
            the window and reports where they went.
        date_range (GetTalentFlowBodyDateRange):
    """

    api_key: str
    company: (
        GetTalentFlowBodyCompanyType0
        | GetTalentFlowBodyCompanyType1
        | GetTalentFlowBodyCompanyType2
        | GetTalentFlowBodyCompanyType3
    )
    direction: GetTalentFlowBodyDirection
    date_range: GetTalentFlowBodyDateRange
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_talent_flow_body_company_type_0 import GetTalentFlowBodyCompanyType0
        from ..models.get_talent_flow_body_company_type_1 import GetTalentFlowBodyCompanyType1
        from ..models.get_talent_flow_body_company_type_2 import GetTalentFlowBodyCompanyType2

        api_key = self.api_key

        company: dict[str, Any]
        if isinstance(self.company, GetTalentFlowBodyCompanyType0):
            company = self.company.to_dict()
        elif isinstance(self.company, GetTalentFlowBodyCompanyType1):
            company = self.company.to_dict()
        elif isinstance(self.company, GetTalentFlowBodyCompanyType2):
            company = self.company.to_dict()
        else:
            company = self.company.to_dict()

        direction = self.direction.value

        date_range = self.date_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "company": company,
                "direction": direction,
                "dateRange": date_range,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_talent_flow_body_company_type_0 import GetTalentFlowBodyCompanyType0
        from ..models.get_talent_flow_body_company_type_1 import GetTalentFlowBodyCompanyType1
        from ..models.get_talent_flow_body_company_type_2 import GetTalentFlowBodyCompanyType2
        from ..models.get_talent_flow_body_company_type_3 import GetTalentFlowBodyCompanyType3
        from ..models.get_talent_flow_body_date_range import GetTalentFlowBodyDateRange

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_company(
            data: object,
        ) -> (
            GetTalentFlowBodyCompanyType0
            | GetTalentFlowBodyCompanyType1
            | GetTalentFlowBodyCompanyType2
            | GetTalentFlowBodyCompanyType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = GetTalentFlowBodyCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_1 = GetTalentFlowBodyCompanyType1.from_dict(data)

                return company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_2 = GetTalentFlowBodyCompanyType2.from_dict(data)

                return company_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            company_type_3 = GetTalentFlowBodyCompanyType3.from_dict(data)

            return company_type_3

        company = _parse_company(d.pop("company"))

        direction = GetTalentFlowBodyDirection(d.pop("direction"))

        date_range = GetTalentFlowBodyDateRange.from_dict(d.pop("dateRange"))

        get_talent_flow_body = cls(
            api_key=api_key,
            company=company,
            direction=direction,
            date_range=date_range,
        )

        get_talent_flow_body.additional_properties = d
        return get_talent_flow_body

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
