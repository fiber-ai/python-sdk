from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.investment_search_body_search_params_type_0_investor_type_type_1 import (
    InvestmentSearchBodySearchParamsType0InvestorTypeType1,
)
from ..models.investment_search_body_search_params_type_0_investor_type_type_2_type_1 import (
    InvestmentSearchBodySearchParamsType0InvestorTypeType2Type1,
)
from ..models.investment_search_body_search_params_type_0_investor_type_type_3_type_1 import (
    InvestmentSearchBodySearchParamsType0InvestorTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investment_search_body_search_params_type_0_country_code_type_0 import (
        InvestmentSearchBodySearchParamsType0CountryCodeType0,
    )
    from ..models.investment_search_body_search_params_type_0_investor_country_code_type_0 import (
        InvestmentSearchBodySearchParamsType0InvestorCountryCodeType0,
    )
    from ..models.investment_search_body_search_params_type_0_post_money_valuation_usd_type_0 import (
        InvestmentSearchBodySearchParamsType0PostMoneyValuationUSDType0,
    )
    from ..models.investment_search_body_search_params_type_0_raised_amount_usd_type_0 import (
        InvestmentSearchBodySearchParamsType0RaisedAmountUSDType0,
    )
    from ..models.investment_search_body_search_params_type_0_round_date_type_0 import (
        InvestmentSearchBodySearchParamsType0RoundDateType0,
    )
    from ..models.investment_search_body_search_params_type_0_round_type_type_0 import (
        InvestmentSearchBodySearchParamsType0RoundTypeType0,
    )
    from ..models.investment_search_body_search_params_type_0_sorting_type_0 import (
        InvestmentSearchBodySearchParamsType0SortingType0,
    )
    from ..models.investment_search_body_search_params_type_0_state_name_type_0 import (
        InvestmentSearchBodySearchParamsType0StateNameType0,
    )


T = TypeVar("T", bound="InvestmentSearchBodySearchParamsType0")


@_attrs_define
class InvestmentSearchBodySearchParamsType0:
    """Investment search filter parameters. If not provided, returns all investments (subject to pagination)

    Attributes:
        investor_name (None | str | Unset): Filter by investor name (partial match, case-insensitive). Use ILIKE pattern
            matching.
        investor_type (InvestmentSearchBodySearchParamsType0InvestorTypeType1 |
            InvestmentSearchBodySearchParamsType0InvestorTypeType2Type1 |
            InvestmentSearchBodySearchParamsType0InvestorTypeType3Type1 | None | Unset): Filter by investor type: 'person'
            for individuals, 'organization' for firms, 'either' to include both types. Pass null/undefined to include both
            types (same as 'either')
        investor_country_code (InvestmentSearchBodySearchParamsType0InvestorCountryCodeType0 | None | Unset): Investor
            country or region filter with include/exclude pattern. Region codes like X-ANGLOSPHERE expand to multiple
            countries (USA, GBR, AUS, etc.)
        investor_domain (None | str | Unset): Filter by investor domain (exact match). For example, 'techstars.com' to
            find all investments made by Techstars
        investor_crunchbase_slug (None | str | Unset): Filter by investor Crunchbase slug (exact match). For example,
            'sequoia-capital' to find all investments made by Sequoia Capital
        company_name (None | str | Unset): Filter by company name (partial match, case-insensitive). Use ILIKE pattern
            matching.
        company_domain (None | str | Unset): Filter by company domain (exact match)
        company_linkedin_url (None | str | Unset): Filter by company LinkedIn URL. Accepts either full URL (e.g.,
            'https://www.linkedin.com/company/fiber-ai/') or slug (e.g., 'fiber-ai'). You can also use LinkedIn organization
            ID in the slug (e.g., 'https://www.linkedin.com/company/123456789/' or just '123456789')
        round_type (InvestmentSearchBodySearchParamsType0RoundTypeType0 | None | Unset): Round type filter with
            include/exclude pattern. Examples: include: ['series_a', 'seed']
        round_date (InvestmentSearchBodySearchParamsType0RoundDateType0 | None | Unset): Filter by funding round
            announcement date (date range)
        raised_amount_usd (InvestmentSearchBodySearchParamsType0RaisedAmountUSDType0 | None | Unset): Filter by amount
            raised in USD (range). For example, min: 5000000 to find rounds with at least $5M raised
        post_money_valuation_usd (InvestmentSearchBodySearchParamsType0PostMoneyValuationUSDType0 | None | Unset):
            Filter by post-money valuation in USD (range)
        country_code (InvestmentSearchBodySearchParamsType0CountryCodeType0 | None | Unset): Round location country or
            region filter with include/exclude pattern. Region codes like X-ANGLOSPHERE expand to multiple countries (USA,
            GBR, AUS, etc.)
        state_name (InvestmentSearchBodySearchParamsType0StateNameType0 | None | Unset): Round location state name
            filter with include/exclude pattern. Use full state names (e.g., 'California', 'England', 'New York'). State
            codes like 'CA' or 'NY' are not accepted.
        city (None | str | Unset): Filter by round location city (partial match, case-insensitive). Use ILIKE pattern
            matching.
        was_lead_investor (bool | None | Unset): Filter by whether the investor was a lead investor in the round
        min_investor_count (int | None | Unset): Filter by minimum number of investors in the funding round
        sorting (InvestmentSearchBodySearchParamsType0SortingType0 | None | Unset): Sorting configuration. If provided,
            field is required. Defaults to round_date DESC if not provided.
    """

    investor_name: None | str | Unset = UNSET
    investor_type: (
        InvestmentSearchBodySearchParamsType0InvestorTypeType1
        | InvestmentSearchBodySearchParamsType0InvestorTypeType2Type1
        | InvestmentSearchBodySearchParamsType0InvestorTypeType3Type1
        | None
        | Unset
    ) = UNSET
    investor_country_code: InvestmentSearchBodySearchParamsType0InvestorCountryCodeType0 | None | Unset = UNSET
    investor_domain: None | str | Unset = UNSET
    investor_crunchbase_slug: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    company_domain: None | str | Unset = UNSET
    company_linkedin_url: None | str | Unset = UNSET
    round_type: InvestmentSearchBodySearchParamsType0RoundTypeType0 | None | Unset = UNSET
    round_date: InvestmentSearchBodySearchParamsType0RoundDateType0 | None | Unset = UNSET
    raised_amount_usd: InvestmentSearchBodySearchParamsType0RaisedAmountUSDType0 | None | Unset = UNSET
    post_money_valuation_usd: InvestmentSearchBodySearchParamsType0PostMoneyValuationUSDType0 | None | Unset = UNSET
    country_code: InvestmentSearchBodySearchParamsType0CountryCodeType0 | None | Unset = UNSET
    state_name: InvestmentSearchBodySearchParamsType0StateNameType0 | None | Unset = UNSET
    city: None | str | Unset = UNSET
    was_lead_investor: bool | None | Unset = UNSET
    min_investor_count: int | None | Unset = UNSET
    sorting: InvestmentSearchBodySearchParamsType0SortingType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.investment_search_body_search_params_type_0_country_code_type_0 import (
            InvestmentSearchBodySearchParamsType0CountryCodeType0,
        )
        from ..models.investment_search_body_search_params_type_0_investor_country_code_type_0 import (
            InvestmentSearchBodySearchParamsType0InvestorCountryCodeType0,
        )
        from ..models.investment_search_body_search_params_type_0_post_money_valuation_usd_type_0 import (
            InvestmentSearchBodySearchParamsType0PostMoneyValuationUSDType0,
        )
        from ..models.investment_search_body_search_params_type_0_raised_amount_usd_type_0 import (
            InvestmentSearchBodySearchParamsType0RaisedAmountUSDType0,
        )
        from ..models.investment_search_body_search_params_type_0_round_date_type_0 import (
            InvestmentSearchBodySearchParamsType0RoundDateType0,
        )
        from ..models.investment_search_body_search_params_type_0_round_type_type_0 import (
            InvestmentSearchBodySearchParamsType0RoundTypeType0,
        )
        from ..models.investment_search_body_search_params_type_0_sorting_type_0 import (
            InvestmentSearchBodySearchParamsType0SortingType0,
        )
        from ..models.investment_search_body_search_params_type_0_state_name_type_0 import (
            InvestmentSearchBodySearchParamsType0StateNameType0,
        )

        investor_name: None | str | Unset
        if isinstance(self.investor_name, Unset):
            investor_name = UNSET
        else:
            investor_name = self.investor_name

        investor_type: None | str | Unset
        if isinstance(self.investor_type, Unset):
            investor_type = UNSET
        elif isinstance(self.investor_type, InvestmentSearchBodySearchParamsType0InvestorTypeType1):
            investor_type = self.investor_type.value
        elif isinstance(self.investor_type, InvestmentSearchBodySearchParamsType0InvestorTypeType2Type1):
            investor_type = self.investor_type.value
        elif isinstance(self.investor_type, InvestmentSearchBodySearchParamsType0InvestorTypeType3Type1):
            investor_type = self.investor_type.value
        else:
            investor_type = self.investor_type

        investor_country_code: dict[str, Any] | None | Unset
        if isinstance(self.investor_country_code, Unset):
            investor_country_code = UNSET
        elif isinstance(self.investor_country_code, InvestmentSearchBodySearchParamsType0InvestorCountryCodeType0):
            investor_country_code = self.investor_country_code.to_dict()
        else:
            investor_country_code = self.investor_country_code

        investor_domain: None | str | Unset
        if isinstance(self.investor_domain, Unset):
            investor_domain = UNSET
        else:
            investor_domain = self.investor_domain

        investor_crunchbase_slug: None | str | Unset
        if isinstance(self.investor_crunchbase_slug, Unset):
            investor_crunchbase_slug = UNSET
        else:
            investor_crunchbase_slug = self.investor_crunchbase_slug

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_domain: None | str | Unset
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        else:
            company_domain = self.company_domain

        company_linkedin_url: None | str | Unset
        if isinstance(self.company_linkedin_url, Unset):
            company_linkedin_url = UNSET
        else:
            company_linkedin_url = self.company_linkedin_url

        round_type: dict[str, Any] | None | Unset
        if isinstance(self.round_type, Unset):
            round_type = UNSET
        elif isinstance(self.round_type, InvestmentSearchBodySearchParamsType0RoundTypeType0):
            round_type = self.round_type.to_dict()
        else:
            round_type = self.round_type

        round_date: dict[str, Any] | None | Unset
        if isinstance(self.round_date, Unset):
            round_date = UNSET
        elif isinstance(self.round_date, InvestmentSearchBodySearchParamsType0RoundDateType0):
            round_date = self.round_date.to_dict()
        else:
            round_date = self.round_date

        raised_amount_usd: dict[str, Any] | None | Unset
        if isinstance(self.raised_amount_usd, Unset):
            raised_amount_usd = UNSET
        elif isinstance(self.raised_amount_usd, InvestmentSearchBodySearchParamsType0RaisedAmountUSDType0):
            raised_amount_usd = self.raised_amount_usd.to_dict()
        else:
            raised_amount_usd = self.raised_amount_usd

        post_money_valuation_usd: dict[str, Any] | None | Unset
        if isinstance(self.post_money_valuation_usd, Unset):
            post_money_valuation_usd = UNSET
        elif isinstance(self.post_money_valuation_usd, InvestmentSearchBodySearchParamsType0PostMoneyValuationUSDType0):
            post_money_valuation_usd = self.post_money_valuation_usd.to_dict()
        else:
            post_money_valuation_usd = self.post_money_valuation_usd

        country_code: dict[str, Any] | None | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        elif isinstance(self.country_code, InvestmentSearchBodySearchParamsType0CountryCodeType0):
            country_code = self.country_code.to_dict()
        else:
            country_code = self.country_code

        state_name: dict[str, Any] | None | Unset
        if isinstance(self.state_name, Unset):
            state_name = UNSET
        elif isinstance(self.state_name, InvestmentSearchBodySearchParamsType0StateNameType0):
            state_name = self.state_name.to_dict()
        else:
            state_name = self.state_name

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        was_lead_investor: bool | None | Unset
        if isinstance(self.was_lead_investor, Unset):
            was_lead_investor = UNSET
        else:
            was_lead_investor = self.was_lead_investor

        min_investor_count: int | None | Unset
        if isinstance(self.min_investor_count, Unset):
            min_investor_count = UNSET
        else:
            min_investor_count = self.min_investor_count

        sorting: dict[str, Any] | None | Unset
        if isinstance(self.sorting, Unset):
            sorting = UNSET
        elif isinstance(self.sorting, InvestmentSearchBodySearchParamsType0SortingType0):
            sorting = self.sorting.to_dict()
        else:
            sorting = self.sorting

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if investor_name is not UNSET:
            field_dict["investorName"] = investor_name
        if investor_type is not UNSET:
            field_dict["investorType"] = investor_type
        if investor_country_code is not UNSET:
            field_dict["investorCountryCode"] = investor_country_code
        if investor_domain is not UNSET:
            field_dict["investorDomain"] = investor_domain
        if investor_crunchbase_slug is not UNSET:
            field_dict["investorCrunchbaseSlug"] = investor_crunchbase_slug
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_domain is not UNSET:
            field_dict["companyDomain"] = company_domain
        if company_linkedin_url is not UNSET:
            field_dict["companyLinkedinUrl"] = company_linkedin_url
        if round_type is not UNSET:
            field_dict["roundType"] = round_type
        if round_date is not UNSET:
            field_dict["roundDate"] = round_date
        if raised_amount_usd is not UNSET:
            field_dict["raisedAmountUSD"] = raised_amount_usd
        if post_money_valuation_usd is not UNSET:
            field_dict["postMoneyValuationUSD"] = post_money_valuation_usd
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if state_name is not UNSET:
            field_dict["stateName"] = state_name
        if city is not UNSET:
            field_dict["city"] = city
        if was_lead_investor is not UNSET:
            field_dict["wasLeadInvestor"] = was_lead_investor
        if min_investor_count is not UNSET:
            field_dict["minInvestorCount"] = min_investor_count
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_search_body_search_params_type_0_country_code_type_0 import (
            InvestmentSearchBodySearchParamsType0CountryCodeType0,
        )
        from ..models.investment_search_body_search_params_type_0_investor_country_code_type_0 import (
            InvestmentSearchBodySearchParamsType0InvestorCountryCodeType0,
        )
        from ..models.investment_search_body_search_params_type_0_post_money_valuation_usd_type_0 import (
            InvestmentSearchBodySearchParamsType0PostMoneyValuationUSDType0,
        )
        from ..models.investment_search_body_search_params_type_0_raised_amount_usd_type_0 import (
            InvestmentSearchBodySearchParamsType0RaisedAmountUSDType0,
        )
        from ..models.investment_search_body_search_params_type_0_round_date_type_0 import (
            InvestmentSearchBodySearchParamsType0RoundDateType0,
        )
        from ..models.investment_search_body_search_params_type_0_round_type_type_0 import (
            InvestmentSearchBodySearchParamsType0RoundTypeType0,
        )
        from ..models.investment_search_body_search_params_type_0_sorting_type_0 import (
            InvestmentSearchBodySearchParamsType0SortingType0,
        )
        from ..models.investment_search_body_search_params_type_0_state_name_type_0 import (
            InvestmentSearchBodySearchParamsType0StateNameType0,
        )

        d = dict(src_dict)

        def _parse_investor_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_name = _parse_investor_name(d.pop("investorName", UNSET))

        def _parse_investor_type(
            data: object,
        ) -> (
            InvestmentSearchBodySearchParamsType0InvestorTypeType1
            | InvestmentSearchBodySearchParamsType0InvestorTypeType2Type1
            | InvestmentSearchBodySearchParamsType0InvestorTypeType3Type1
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
                investor_type_type_1 = InvestmentSearchBodySearchParamsType0InvestorTypeType1(data)

                return investor_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                investor_type_type_2_type_1 = InvestmentSearchBodySearchParamsType0InvestorTypeType2Type1(data)

                return investor_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                investor_type_type_3_type_1 = InvestmentSearchBodySearchParamsType0InvestorTypeType3Type1(data)

                return investor_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InvestmentSearchBodySearchParamsType0InvestorTypeType1
                | InvestmentSearchBodySearchParamsType0InvestorTypeType2Type1
                | InvestmentSearchBodySearchParamsType0InvestorTypeType3Type1
                | None
                | Unset,
                data,
            )

        investor_type = _parse_investor_type(d.pop("investorType", UNSET))

        def _parse_investor_country_code(
            data: object,
        ) -> InvestmentSearchBodySearchParamsType0InvestorCountryCodeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investor_country_code_type_0 = InvestmentSearchBodySearchParamsType0InvestorCountryCodeType0.from_dict(
                    data
                )

                return investor_country_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSearchBodySearchParamsType0InvestorCountryCodeType0 | None | Unset, data)

        investor_country_code = _parse_investor_country_code(d.pop("investorCountryCode", UNSET))

        def _parse_investor_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_domain = _parse_investor_domain(d.pop("investorDomain", UNSET))

        def _parse_investor_crunchbase_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_crunchbase_slug = _parse_investor_crunchbase_slug(d.pop("investorCrunchbaseSlug", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_company_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_domain = _parse_company_domain(d.pop("companyDomain", UNSET))

        def _parse_company_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_linkedin_url = _parse_company_linkedin_url(d.pop("companyLinkedinUrl", UNSET))

        def _parse_round_type(data: object) -> InvestmentSearchBodySearchParamsType0RoundTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_type_type_0 = InvestmentSearchBodySearchParamsType0RoundTypeType0.from_dict(data)

                return round_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSearchBodySearchParamsType0RoundTypeType0 | None | Unset, data)

        round_type = _parse_round_type(d.pop("roundType", UNSET))

        def _parse_round_date(data: object) -> InvestmentSearchBodySearchParamsType0RoundDateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_date_type_0 = InvestmentSearchBodySearchParamsType0RoundDateType0.from_dict(data)

                return round_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSearchBodySearchParamsType0RoundDateType0 | None | Unset, data)

        round_date = _parse_round_date(d.pop("roundDate", UNSET))

        def _parse_raised_amount_usd(
            data: object,
        ) -> InvestmentSearchBodySearchParamsType0RaisedAmountUSDType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raised_amount_usd_type_0 = InvestmentSearchBodySearchParamsType0RaisedAmountUSDType0.from_dict(data)

                return raised_amount_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSearchBodySearchParamsType0RaisedAmountUSDType0 | None | Unset, data)

        raised_amount_usd = _parse_raised_amount_usd(d.pop("raisedAmountUSD", UNSET))

        def _parse_post_money_valuation_usd(
            data: object,
        ) -> InvestmentSearchBodySearchParamsType0PostMoneyValuationUSDType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                post_money_valuation_usd_type_0 = (
                    InvestmentSearchBodySearchParamsType0PostMoneyValuationUSDType0.from_dict(data)
                )

                return post_money_valuation_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSearchBodySearchParamsType0PostMoneyValuationUSDType0 | None | Unset, data)

        post_money_valuation_usd = _parse_post_money_valuation_usd(d.pop("postMoneyValuationUSD", UNSET))

        def _parse_country_code(data: object) -> InvestmentSearchBodySearchParamsType0CountryCodeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_code_type_0 = InvestmentSearchBodySearchParamsType0CountryCodeType0.from_dict(data)

                return country_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSearchBodySearchParamsType0CountryCodeType0 | None | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_state_name(data: object) -> InvestmentSearchBodySearchParamsType0StateNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_name_type_0 = InvestmentSearchBodySearchParamsType0StateNameType0.from_dict(data)

                return state_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSearchBodySearchParamsType0StateNameType0 | None | Unset, data)

        state_name = _parse_state_name(d.pop("stateName", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_was_lead_investor(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        was_lead_investor = _parse_was_lead_investor(d.pop("wasLeadInvestor", UNSET))

        def _parse_min_investor_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_investor_count = _parse_min_investor_count(d.pop("minInvestorCount", UNSET))

        def _parse_sorting(data: object) -> InvestmentSearchBodySearchParamsType0SortingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sorting_type_0 = InvestmentSearchBodySearchParamsType0SortingType0.from_dict(data)

                return sorting_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSearchBodySearchParamsType0SortingType0 | None | Unset, data)

        sorting = _parse_sorting(d.pop("sorting", UNSET))

        investment_search_body_search_params_type_0 = cls(
            investor_name=investor_name,
            investor_type=investor_type,
            investor_country_code=investor_country_code,
            investor_domain=investor_domain,
            investor_crunchbase_slug=investor_crunchbase_slug,
            company_name=company_name,
            company_domain=company_domain,
            company_linkedin_url=company_linkedin_url,
            round_type=round_type,
            round_date=round_date,
            raised_amount_usd=raised_amount_usd,
            post_money_valuation_usd=post_money_valuation_usd,
            country_code=country_code,
            state_name=state_name,
            city=city,
            was_lead_investor=was_lead_investor,
            min_investor_count=min_investor_count,
            sorting=sorting,
        )

        return investment_search_body_search_params_type_0
