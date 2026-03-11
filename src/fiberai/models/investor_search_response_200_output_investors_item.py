from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investor_search_response_200_output_investors_item_country_code_type_1 import (
    InvestorSearchResponse200OutputInvestorsItemCountryCodeType1,
)
from ..models.investor_search_response_200_output_investors_item_country_code_type_2_type_1 import (
    InvestorSearchResponse200OutputInvestorsItemCountryCodeType2Type1,
)
from ..models.investor_search_response_200_output_investors_item_country_code_type_3_type_1 import (
    InvestorSearchResponse200OutputInvestorsItemCountryCodeType3Type1,
)
from ..models.investor_search_response_200_output_investors_item_type_type_1 import (
    InvestorSearchResponse200OutputInvestorsItemTypeType1,
)
from ..models.investor_search_response_200_output_investors_item_type_type_2_type_1 import (
    InvestorSearchResponse200OutputInvestorsItemTypeType2Type1,
)
from ..models.investor_search_response_200_output_investors_item_type_type_3_type_1 import (
    InvestorSearchResponse200OutputInvestorsItemTypeType3Type1,
)
from ..models.investor_search_response_200_output_investors_item_types_type_0_item import (
    InvestorSearchResponse200OutputInvestorsItemTypesType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investor_search_response_200_output_investors_item_investments_by_stage_type_0_item import (
        InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0Item,
    )
    from ..models.investor_search_response_200_output_investors_item_recent_investments_type_0_item import (
        InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0Item,
    )


T = TypeVar("T", bound="InvestorSearchResponse200OutputInvestorsItem")


@_attrs_define
class InvestorSearchResponse200OutputInvestorsItem:
    """
    Attributes:
        total_investment_count (int): Total number of investments made
        lead_investment_count (int): Number of lead investments
        lead_investment_rate (float): Lead investment rate (0.0 - 1.0)
        name (None | str | Unset): Investor name
        crunchbase_slug (None | str | Unset): Crunchbase slug
        last_investment_date (None | str | Unset): Date of most recent investment
        type_ (InvestorSearchResponse200OutputInvestorsItemTypeType1 |
            InvestorSearchResponse200OutputInvestorsItemTypeType2Type1 |
            InvestorSearchResponse200OutputInvestorsItemTypeType3Type1 | None | Unset): Investor type: 'person' for
            individuals, 'organization' for firms
        types (list[InvestorSearchResponse200OutputInvestorsItemTypesType0Item] | None | Unset): Investor categories
        is_top_vc (bool | None | Unset): Whether investor is a top VC
        domain (None | str | Unset): Investor domain
        country_code (InvestorSearchResponse200OutputInvestorsItemCountryCodeType1 |
            InvestorSearchResponse200OutputInvestorsItemCountryCodeType2Type1 |
            InvestorSearchResponse200OutputInvestorsItemCountryCodeType3Type1 | None | Unset): Country code
        state_code (None | str | Unset): State code
        state (None | str | Unset): State name
        city (None | str | Unset): City name
        founded_on (None | str | Unset): Founded on date
        closed_on (None | str | Unset): Closed on date
        investments_by_stage (list[InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0Item] | None |
            Unset): Breakdown of investments by stage
        recent_investments (list[InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0Item] | None |
            Unset): Preview of 5 most recent investments
        linkedin_url (None | str | Unset): LinkedIn company URL
        logo_url (None | str | Unset): Logo URL (proxied through api.fiber.ai)
        facebook_url (None | str | Unset): Facebook URL
        x_url (None | str | Unset): X (Twitter) URL
    """

    total_investment_count: int
    lead_investment_count: int
    lead_investment_rate: float
    name: None | str | Unset = UNSET
    crunchbase_slug: None | str | Unset = UNSET
    last_investment_date: None | str | Unset = UNSET
    type_: (
        InvestorSearchResponse200OutputInvestorsItemTypeType1
        | InvestorSearchResponse200OutputInvestorsItemTypeType2Type1
        | InvestorSearchResponse200OutputInvestorsItemTypeType3Type1
        | None
        | Unset
    ) = UNSET
    types: list[InvestorSearchResponse200OutputInvestorsItemTypesType0Item] | None | Unset = UNSET
    is_top_vc: bool | None | Unset = UNSET
    domain: None | str | Unset = UNSET
    country_code: (
        InvestorSearchResponse200OutputInvestorsItemCountryCodeType1
        | InvestorSearchResponse200OutputInvestorsItemCountryCodeType2Type1
        | InvestorSearchResponse200OutputInvestorsItemCountryCodeType3Type1
        | None
        | Unset
    ) = UNSET
    state_code: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    founded_on: None | str | Unset = UNSET
    closed_on: None | str | Unset = UNSET
    investments_by_stage: (
        list[InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0Item] | None | Unset
    ) = UNSET
    recent_investments: list[InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0Item] | None | Unset = (
        UNSET
    )
    linkedin_url: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    facebook_url: None | str | Unset = UNSET
    x_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_investment_count = self.total_investment_count

        lead_investment_count = self.lead_investment_count

        lead_investment_rate = self.lead_investment_rate

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        crunchbase_slug: None | str | Unset
        if isinstance(self.crunchbase_slug, Unset):
            crunchbase_slug = UNSET
        else:
            crunchbase_slug = self.crunchbase_slug

        last_investment_date: None | str | Unset
        if isinstance(self.last_investment_date, Unset):
            last_investment_date = UNSET
        else:
            last_investment_date = self.last_investment_date

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, InvestorSearchResponse200OutputInvestorsItemTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, InvestorSearchResponse200OutputInvestorsItemTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, InvestorSearchResponse200OutputInvestorsItemTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        types: list[str] | None | Unset
        if isinstance(self.types, Unset):
            types = UNSET
        elif isinstance(self.types, list):
            types = []
            for types_type_0_item_data in self.types:
                types_type_0_item = types_type_0_item_data.value
                types.append(types_type_0_item)

        else:
            types = self.types

        is_top_vc: bool | None | Unset
        if isinstance(self.is_top_vc, Unset):
            is_top_vc = UNSET
        else:
            is_top_vc = self.is_top_vc

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        elif isinstance(self.country_code, InvestorSearchResponse200OutputInvestorsItemCountryCodeType1):
            country_code = self.country_code.value
        elif isinstance(self.country_code, InvestorSearchResponse200OutputInvestorsItemCountryCodeType2Type1):
            country_code = self.country_code.value
        elif isinstance(self.country_code, InvestorSearchResponse200OutputInvestorsItemCountryCodeType3Type1):
            country_code = self.country_code.value
        else:
            country_code = self.country_code

        state_code: None | str | Unset
        if isinstance(self.state_code, Unset):
            state_code = UNSET
        else:
            state_code = self.state_code

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        founded_on: None | str | Unset
        if isinstance(self.founded_on, Unset):
            founded_on = UNSET
        else:
            founded_on = self.founded_on

        closed_on: None | str | Unset
        if isinstance(self.closed_on, Unset):
            closed_on = UNSET
        else:
            closed_on = self.closed_on

        investments_by_stage: list[dict[str, Any]] | None | Unset
        if isinstance(self.investments_by_stage, Unset):
            investments_by_stage = UNSET
        elif isinstance(self.investments_by_stage, list):
            investments_by_stage = []
            for investments_by_stage_type_0_item_data in self.investments_by_stage:
                investments_by_stage_type_0_item = investments_by_stage_type_0_item_data.to_dict()
                investments_by_stage.append(investments_by_stage_type_0_item)

        else:
            investments_by_stage = self.investments_by_stage

        recent_investments: list[dict[str, Any]] | None | Unset
        if isinstance(self.recent_investments, Unset):
            recent_investments = UNSET
        elif isinstance(self.recent_investments, list):
            recent_investments = []
            for recent_investments_type_0_item_data in self.recent_investments:
                recent_investments_type_0_item = recent_investments_type_0_item_data.to_dict()
                recent_investments.append(recent_investments_type_0_item)

        else:
            recent_investments = self.recent_investments

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        facebook_url: None | str | Unset
        if isinstance(self.facebook_url, Unset):
            facebook_url = UNSET
        else:
            facebook_url = self.facebook_url

        x_url: None | str | Unset
        if isinstance(self.x_url, Unset):
            x_url = UNSET
        else:
            x_url = self.x_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalInvestmentCount": total_investment_count,
                "leadInvestmentCount": lead_investment_count,
                "leadInvestmentRate": lead_investment_rate,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if crunchbase_slug is not UNSET:
            field_dict["crunchbaseSlug"] = crunchbase_slug
        if last_investment_date is not UNSET:
            field_dict["lastInvestmentDate"] = last_investment_date
        if type_ is not UNSET:
            field_dict["type"] = type_
        if types is not UNSET:
            field_dict["types"] = types
        if is_top_vc is not UNSET:
            field_dict["isTopVc"] = is_top_vc
        if domain is not UNSET:
            field_dict["domain"] = domain
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if founded_on is not UNSET:
            field_dict["foundedOn"] = founded_on
        if closed_on is not UNSET:
            field_dict["closedOn"] = closed_on
        if investments_by_stage is not UNSET:
            field_dict["investmentsByStage"] = investments_by_stage
        if recent_investments is not UNSET:
            field_dict["recentInvestments"] = recent_investments
        if linkedin_url is not UNSET:
            field_dict["linkedinURL"] = linkedin_url
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if facebook_url is not UNSET:
            field_dict["facebookUrl"] = facebook_url
        if x_url is not UNSET:
            field_dict["xUrl"] = x_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investor_search_response_200_output_investors_item_investments_by_stage_type_0_item import (
            InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0Item,
        )
        from ..models.investor_search_response_200_output_investors_item_recent_investments_type_0_item import (
            InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0Item,
        )

        d = dict(src_dict)
        total_investment_count = d.pop("totalInvestmentCount")

        lead_investment_count = d.pop("leadInvestmentCount")

        lead_investment_rate = d.pop("leadInvestmentRate")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_crunchbase_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crunchbase_slug = _parse_crunchbase_slug(d.pop("crunchbaseSlug", UNSET))

        def _parse_last_investment_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_investment_date = _parse_last_investment_date(d.pop("lastInvestmentDate", UNSET))

        def _parse_type_(
            data: object,
        ) -> (
            InvestorSearchResponse200OutputInvestorsItemTypeType1
            | InvestorSearchResponse200OutputInvestorsItemTypeType2Type1
            | InvestorSearchResponse200OutputInvestorsItemTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = InvestorSearchResponse200OutputInvestorsItemTypeType1(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = InvestorSearchResponse200OutputInvestorsItemTypeType2Type1(data)

                return type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = InvestorSearchResponse200OutputInvestorsItemTypeType3Type1(data)

                return type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InvestorSearchResponse200OutputInvestorsItemTypeType1
                | InvestorSearchResponse200OutputInvestorsItemTypeType2Type1
                | InvestorSearchResponse200OutputInvestorsItemTypeType3Type1
                | None
                | Unset,
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_types(
            data: object,
        ) -> list[InvestorSearchResponse200OutputInvestorsItemTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                types_type_0 = []
                _types_type_0 = data
                for types_type_0_item_data in _types_type_0:
                    types_type_0_item = InvestorSearchResponse200OutputInvestorsItemTypesType0Item(
                        types_type_0_item_data
                    )

                    types_type_0.append(types_type_0_item)

                return types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InvestorSearchResponse200OutputInvestorsItemTypesType0Item] | None | Unset, data)

        types = _parse_types(d.pop("types", UNSET))

        def _parse_is_top_vc(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_top_vc = _parse_is_top_vc(d.pop("isTopVc", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_country_code(
            data: object,
        ) -> (
            InvestorSearchResponse200OutputInvestorsItemCountryCodeType1
            | InvestorSearchResponse200OutputInvestorsItemCountryCodeType2Type1
            | InvestorSearchResponse200OutputInvestorsItemCountryCodeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_code_type_1 = InvestorSearchResponse200OutputInvestorsItemCountryCodeType1(data)

                return country_code_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_code_type_2_type_1 = InvestorSearchResponse200OutputInvestorsItemCountryCodeType2Type1(data)

                return country_code_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                country_code_type_3_type_1 = InvestorSearchResponse200OutputInvestorsItemCountryCodeType3Type1(data)

                return country_code_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InvestorSearchResponse200OutputInvestorsItemCountryCodeType1
                | InvestorSearchResponse200OutputInvestorsItemCountryCodeType2Type1
                | InvestorSearchResponse200OutputInvestorsItemCountryCodeType3Type1
                | None
                | Unset,
                data,
            )

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_state_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_code = _parse_state_code(d.pop("stateCode", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_founded_on(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        founded_on = _parse_founded_on(d.pop("foundedOn", UNSET))

        def _parse_closed_on(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closed_on = _parse_closed_on(d.pop("closedOn", UNSET))

        def _parse_investments_by_stage(
            data: object,
        ) -> list[InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investments_by_stage_type_0 = []
                _investments_by_stage_type_0 = data
                for investments_by_stage_type_0_item_data in _investments_by_stage_type_0:
                    investments_by_stage_type_0_item = (
                        InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0Item.from_dict(
                            investments_by_stage_type_0_item_data
                        )
                    )

                    investments_by_stage_type_0.append(investments_by_stage_type_0_item)

                return investments_by_stage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[InvestorSearchResponse200OutputInvestorsItemInvestmentsByStageType0Item] | None | Unset, data
            )

        investments_by_stage = _parse_investments_by_stage(d.pop("investmentsByStage", UNSET))

        def _parse_recent_investments(
            data: object,
        ) -> list[InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recent_investments_type_0 = []
                _recent_investments_type_0 = data
                for recent_investments_type_0_item_data in _recent_investments_type_0:
                    recent_investments_type_0_item = (
                        InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0Item.from_dict(
                            recent_investments_type_0_item_data
                        )
                    )

                    recent_investments_type_0.append(recent_investments_type_0_item)

                return recent_investments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[InvestorSearchResponse200OutputInvestorsItemRecentInvestmentsType0Item] | None | Unset, data
            )

        recent_investments = _parse_recent_investments(d.pop("recentInvestments", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinURL", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        def _parse_facebook_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facebook_url = _parse_facebook_url(d.pop("facebookUrl", UNSET))

        def _parse_x_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        x_url = _parse_x_url(d.pop("xUrl", UNSET))

        investor_search_response_200_output_investors_item = cls(
            total_investment_count=total_investment_count,
            lead_investment_count=lead_investment_count,
            lead_investment_rate=lead_investment_rate,
            name=name,
            crunchbase_slug=crunchbase_slug,
            last_investment_date=last_investment_date,
            type_=type_,
            types=types,
            is_top_vc=is_top_vc,
            domain=domain,
            country_code=country_code,
            state_code=state_code,
            state=state,
            city=city,
            founded_on=founded_on,
            closed_on=closed_on,
            investments_by_stage=investments_by_stage,
            recent_investments=recent_investments,
            linkedin_url=linkedin_url,
            logo_url=logo_url,
            facebook_url=facebook_url,
            x_url=x_url,
        )

        investor_search_response_200_output_investors_item.additional_properties = d
        return investor_search_response_200_output_investors_item

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
