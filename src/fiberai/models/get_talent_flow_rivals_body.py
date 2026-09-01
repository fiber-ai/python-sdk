from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_talent_flow_rivals_body_company_type_0 import GetTalentFlowRivalsBodyCompanyType0
    from ..models.get_talent_flow_rivals_body_company_type_1 import GetTalentFlowRivalsBodyCompanyType1
    from ..models.get_talent_flow_rivals_body_company_type_2 import GetTalentFlowRivalsBodyCompanyType2
    from ..models.get_talent_flow_rivals_body_company_type_3 import GetTalentFlowRivalsBodyCompanyType3
    from ..models.get_talent_flow_rivals_body_date_range import GetTalentFlowRivalsBodyDateRange


T = TypeVar("T", bound="GetTalentFlowRivalsBody")


@_attrs_define
class GetTalentFlowRivalsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company (GetTalentFlowRivalsBodyCompanyType0 | GetTalentFlowRivalsBodyCompanyType1 |
            GetTalentFlowRivalsBodyCompanyType2 | GetTalentFlowRivalsBodyCompanyType3): Company to analyze. Set identifier
            to 'linkedinUrl', 'linkedinSlug', 'linkedinOrgId', or 'domain' and provide the corresponding value.
        date_range (GetTalentFlowRivalsBodyDateRange):
        num_companies_per_side (int | Unset): Number of top donor and acceptor companies to include. Donors are
            companies the analyzed company gained the most people from; acceptors are companies it lost the most people to.
            Overlapping companies are combined, so the rival list may hold fewer than twice this number. Default: 10.
    """

    api_key: str
    company: (
        GetTalentFlowRivalsBodyCompanyType0
        | GetTalentFlowRivalsBodyCompanyType1
        | GetTalentFlowRivalsBodyCompanyType2
        | GetTalentFlowRivalsBodyCompanyType3
    )
    date_range: GetTalentFlowRivalsBodyDateRange
    num_companies_per_side: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_talent_flow_rivals_body_company_type_0 import (
            GetTalentFlowRivalsBodyCompanyType0,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_rivals_body_company_type_1 import (
            GetTalentFlowRivalsBodyCompanyType1,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_rivals_body_company_type_2 import (
            GetTalentFlowRivalsBodyCompanyType2,  # noqa: PLC0415
        )

        api_key = self.api_key

        company: dict[str, Any]
        if isinstance(self.company, GetTalentFlowRivalsBodyCompanyType0):
            company = self.company.to_dict()
        elif isinstance(self.company, GetTalentFlowRivalsBodyCompanyType1):
            company = self.company.to_dict()
        elif isinstance(self.company, GetTalentFlowRivalsBodyCompanyType2):
            company = self.company.to_dict()
        else:
            company = self.company.to_dict()

        date_range = self.date_range.to_dict()

        num_companies_per_side = self.num_companies_per_side

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "company": company,
                "dateRange": date_range,
            }
        )
        if num_companies_per_side is not UNSET:
            field_dict["numCompaniesPerSide"] = num_companies_per_side

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_talent_flow_rivals_body_company_type_0 import (
            GetTalentFlowRivalsBodyCompanyType0,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_rivals_body_company_type_1 import (
            GetTalentFlowRivalsBodyCompanyType1,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_rivals_body_company_type_2 import (
            GetTalentFlowRivalsBodyCompanyType2,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_rivals_body_company_type_3 import (
            GetTalentFlowRivalsBodyCompanyType3,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_rivals_body_date_range import GetTalentFlowRivalsBodyDateRange  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_company(
            data: object,
        ) -> (
            GetTalentFlowRivalsBodyCompanyType0
            | GetTalentFlowRivalsBodyCompanyType1
            | GetTalentFlowRivalsBodyCompanyType2
            | GetTalentFlowRivalsBodyCompanyType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = GetTalentFlowRivalsBodyCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_1 = GetTalentFlowRivalsBodyCompanyType1.from_dict(data)

                return company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_2 = GetTalentFlowRivalsBodyCompanyType2.from_dict(data)

                return company_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            company_type_3 = GetTalentFlowRivalsBodyCompanyType3.from_dict(data)

            return company_type_3

        company = _parse_company(d.pop("company"))

        date_range = GetTalentFlowRivalsBodyDateRange.from_dict(d.pop("dateRange"))

        num_companies_per_side = d.pop("numCompaniesPerSide", UNSET)

        get_talent_flow_rivals_body = cls(
            api_key=api_key,
            company=company,
            date_range=date_range,
            num_companies_per_side=num_companies_per_side,
        )

        get_talent_flow_rivals_body.additional_properties = d
        return get_talent_flow_rivals_body

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
