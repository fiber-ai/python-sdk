from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.investor_search_body_search_params_investor_type_type_1 import InvestorSearchBodySearchParamsInvestorTypeType1
from ..models.investor_search_body_search_params_investor_type_type_2_type_1 import InvestorSearchBodySearchParamsInvestorTypeType2Type1
from ..models.investor_search_body_search_params_investor_type_type_3_type_1 import InvestorSearchBodySearchParamsInvestorTypeType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.investor_search_body_search_params_num_investments_type_0 import InvestorSearchBodySearchParamsNumInvestmentsType0
  from ..models.investor_search_body_search_params_founded_on_type_0 import InvestorSearchBodySearchParamsFoundedOnType0
  from ..models.investor_search_body_search_params_lead_rate_type_0 import InvestorSearchBodySearchParamsLeadRateType0
  from ..models.investor_search_body_search_params_state_name_type_0 import InvestorSearchBodySearchParamsStateNameType0
  from ..models.investor_search_body_search_params_sorting_type_0 import InvestorSearchBodySearchParamsSortingType0
  from ..models.investor_search_body_search_params_country_code_type_0 import InvestorSearchBodySearchParamsCountryCodeType0
  from ..models.investor_search_body_search_params_num_lead_investments_type_0 import InvestorSearchBodySearchParamsNumLeadInvestmentsType0
  from ..models.investor_search_body_search_params_types_type_0 import InvestorSearchBodySearchParamsTypesType0
  from ..models.investor_search_body_search_params_last_investment_date_type_0 import InvestorSearchBodySearchParamsLastInvestmentDateType0





T = TypeVar("T", bound="InvestorSearchBodySearchParams")



@_attrs_define
class InvestorSearchBodySearchParams:
    """ Investor search filter parameters

        Attributes:
            country_code (Union['InvestorSearchBodySearchParamsCountryCodeType0', None, Unset]): Country or region filter
                with include/exclude pattern. Region codes like X-ANGLOSPHERE expand to multiple countries (USA, GBR, AUS, etc.)
            state_name (Union['InvestorSearchBodySearchParamsStateNameType0', None, Unset]): State name filter with
                include/exclude pattern. Use full state names (e.g., 'California', 'England', 'New York'). State codes like 'CA'
                or 'NY' are not accepted.
            investor_type (Union[InvestorSearchBodySearchParamsInvestorTypeType1,
                InvestorSearchBodySearchParamsInvestorTypeType2Type1, InvestorSearchBodySearchParamsInvestorTypeType3Type1,
                None, Unset]): Filter by investor type: 'person' for individuals, 'organization' for firms, 'either' to include
                both types. Pass null/undefined to include both types (same as 'either')
            types (Union['InvestorSearchBodySearchParamsTypesType0', None, Unset]): Investor types filter with
                include/exclude pattern. Examples: include: ['venture_capital', 'angel']
            num_investments (Union['InvestorSearchBodySearchParamsNumInvestmentsType0', None, Unset]): Filter by total
                investment count (range)
            num_lead_investments (Union['InvestorSearchBodySearchParamsNumLeadInvestmentsType0', None, Unset]): Filter by
                number of lead investments (range)
            lead_rate (Union['InvestorSearchBodySearchParamsLeadRateType0', None, Unset]): Filter by lead investment rate
                (0.0 - 1.0). Values outside [0,1] will be clamped to this range
            last_investment_date (Union['InvestorSearchBodySearchParamsLastInvestmentDateType0', None, Unset]): Filter by
                last investment date (date range)
            founded_on (Union['InvestorSearchBodySearchParamsFoundedOnType0', None, Unset]): Filter by founded date (date
                range). Note: many investors have null founded_on, so this filter may exclude many rows
            sorting (Union['InvestorSearchBodySearchParamsSortingType0', None, Unset]): Sorting configuration. If provided,
                field is required. Defaults to total_investment_count DESC if not provided.
            is_top_vc (Union[None, Unset, bool]): Filter by whether investor is a top VC. Note: only a few dozen companies
                qualify as 'top'
            domains (Union[None, Unset, list[str]]): Array of investor domains to filter by
            name_patterns (Union[None, Unset, list[str]]): An array of name patterns used for partial, case-insensitive
                matching against investor names
            crunchbase_slugs (Union[None, Unset, list[str]]): Array of Crunchbase slugs to filter by (exact match). Slugs
                are the last part of the Crunchbase URL (for example, 'sequoia-capital' from
                crunchbase.com/organization/sequoia-capital)
     """

    country_code: Union['InvestorSearchBodySearchParamsCountryCodeType0', None, Unset] = UNSET
    state_name: Union['InvestorSearchBodySearchParamsStateNameType0', None, Unset] = UNSET
    investor_type: Union[InvestorSearchBodySearchParamsInvestorTypeType1, InvestorSearchBodySearchParamsInvestorTypeType2Type1, InvestorSearchBodySearchParamsInvestorTypeType3Type1, None, Unset] = UNSET
    types: Union['InvestorSearchBodySearchParamsTypesType0', None, Unset] = UNSET
    num_investments: Union['InvestorSearchBodySearchParamsNumInvestmentsType0', None, Unset] = UNSET
    num_lead_investments: Union['InvestorSearchBodySearchParamsNumLeadInvestmentsType0', None, Unset] = UNSET
    lead_rate: Union['InvestorSearchBodySearchParamsLeadRateType0', None, Unset] = UNSET
    last_investment_date: Union['InvestorSearchBodySearchParamsLastInvestmentDateType0', None, Unset] = UNSET
    founded_on: Union['InvestorSearchBodySearchParamsFoundedOnType0', None, Unset] = UNSET
    sorting: Union['InvestorSearchBodySearchParamsSortingType0', None, Unset] = UNSET
    is_top_vc: Union[None, Unset, bool] = UNSET
    domains: Union[None, Unset, list[str]] = UNSET
    name_patterns: Union[None, Unset, list[str]] = UNSET
    crunchbase_slugs: Union[None, Unset, list[str]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.investor_search_body_search_params_num_investments_type_0 import InvestorSearchBodySearchParamsNumInvestmentsType0
        from ..models.investor_search_body_search_params_founded_on_type_0 import InvestorSearchBodySearchParamsFoundedOnType0
        from ..models.investor_search_body_search_params_lead_rate_type_0 import InvestorSearchBodySearchParamsLeadRateType0
        from ..models.investor_search_body_search_params_state_name_type_0 import InvestorSearchBodySearchParamsStateNameType0
        from ..models.investor_search_body_search_params_sorting_type_0 import InvestorSearchBodySearchParamsSortingType0
        from ..models.investor_search_body_search_params_country_code_type_0 import InvestorSearchBodySearchParamsCountryCodeType0
        from ..models.investor_search_body_search_params_num_lead_investments_type_0 import InvestorSearchBodySearchParamsNumLeadInvestmentsType0
        from ..models.investor_search_body_search_params_types_type_0 import InvestorSearchBodySearchParamsTypesType0
        from ..models.investor_search_body_search_params_last_investment_date_type_0 import InvestorSearchBodySearchParamsLastInvestmentDateType0
        country_code: Union[None, Unset, dict[str, Any]]
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        elif isinstance(self.country_code, InvestorSearchBodySearchParamsCountryCodeType0):
            country_code = self.country_code.to_dict()
        else:
            country_code = self.country_code

        state_name: Union[None, Unset, dict[str, Any]]
        if isinstance(self.state_name, Unset):
            state_name = UNSET
        elif isinstance(self.state_name, InvestorSearchBodySearchParamsStateNameType0):
            state_name = self.state_name.to_dict()
        else:
            state_name = self.state_name

        investor_type: Union[None, Unset, str]
        if isinstance(self.investor_type, Unset):
            investor_type = UNSET
        elif isinstance(self.investor_type, InvestorSearchBodySearchParamsInvestorTypeType1):
            investor_type = self.investor_type.value
        elif isinstance(self.investor_type, InvestorSearchBodySearchParamsInvestorTypeType2Type1):
            investor_type = self.investor_type.value
        elif isinstance(self.investor_type, InvestorSearchBodySearchParamsInvestorTypeType3Type1):
            investor_type = self.investor_type.value
        else:
            investor_type = self.investor_type

        types: Union[None, Unset, dict[str, Any]]
        if isinstance(self.types, Unset):
            types = UNSET
        elif isinstance(self.types, InvestorSearchBodySearchParamsTypesType0):
            types = self.types.to_dict()
        else:
            types = self.types

        num_investments: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_investments, Unset):
            num_investments = UNSET
        elif isinstance(self.num_investments, InvestorSearchBodySearchParamsNumInvestmentsType0):
            num_investments = self.num_investments.to_dict()
        else:
            num_investments = self.num_investments

        num_lead_investments: Union[None, Unset, dict[str, Any]]
        if isinstance(self.num_lead_investments, Unset):
            num_lead_investments = UNSET
        elif isinstance(self.num_lead_investments, InvestorSearchBodySearchParamsNumLeadInvestmentsType0):
            num_lead_investments = self.num_lead_investments.to_dict()
        else:
            num_lead_investments = self.num_lead_investments

        lead_rate: Union[None, Unset, dict[str, Any]]
        if isinstance(self.lead_rate, Unset):
            lead_rate = UNSET
        elif isinstance(self.lead_rate, InvestorSearchBodySearchParamsLeadRateType0):
            lead_rate = self.lead_rate.to_dict()
        else:
            lead_rate = self.lead_rate

        last_investment_date: Union[None, Unset, dict[str, Any]]
        if isinstance(self.last_investment_date, Unset):
            last_investment_date = UNSET
        elif isinstance(self.last_investment_date, InvestorSearchBodySearchParamsLastInvestmentDateType0):
            last_investment_date = self.last_investment_date.to_dict()
        else:
            last_investment_date = self.last_investment_date

        founded_on: Union[None, Unset, dict[str, Any]]
        if isinstance(self.founded_on, Unset):
            founded_on = UNSET
        elif isinstance(self.founded_on, InvestorSearchBodySearchParamsFoundedOnType0):
            founded_on = self.founded_on.to_dict()
        else:
            founded_on = self.founded_on

        sorting: Union[None, Unset, dict[str, Any]]
        if isinstance(self.sorting, Unset):
            sorting = UNSET
        elif isinstance(self.sorting, InvestorSearchBodySearchParamsSortingType0):
            sorting = self.sorting.to_dict()
        else:
            sorting = self.sorting

        is_top_vc: Union[None, Unset, bool]
        if isinstance(self.is_top_vc, Unset):
            is_top_vc = UNSET
        else:
            is_top_vc = self.is_top_vc

        domains: Union[None, Unset, list[str]]
        if isinstance(self.domains, Unset):
            domains = UNSET
        elif isinstance(self.domains, list):
            domains = self.domains


        else:
            domains = self.domains

        name_patterns: Union[None, Unset, list[str]]
        if isinstance(self.name_patterns, Unset):
            name_patterns = UNSET
        elif isinstance(self.name_patterns, list):
            name_patterns = self.name_patterns


        else:
            name_patterns = self.name_patterns

        crunchbase_slugs: Union[None, Unset, list[str]]
        if isinstance(self.crunchbase_slugs, Unset):
            crunchbase_slugs = UNSET
        elif isinstance(self.crunchbase_slugs, list):
            crunchbase_slugs = self.crunchbase_slugs


        else:
            crunchbase_slugs = self.crunchbase_slugs


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if state_name is not UNSET:
            field_dict["stateName"] = state_name
        if investor_type is not UNSET:
            field_dict["investorType"] = investor_type
        if types is not UNSET:
            field_dict["types"] = types
        if num_investments is not UNSET:
            field_dict["numInvestments"] = num_investments
        if num_lead_investments is not UNSET:
            field_dict["numLeadInvestments"] = num_lead_investments
        if lead_rate is not UNSET:
            field_dict["leadRate"] = lead_rate
        if last_investment_date is not UNSET:
            field_dict["lastInvestmentDate"] = last_investment_date
        if founded_on is not UNSET:
            field_dict["foundedOn"] = founded_on
        if sorting is not UNSET:
            field_dict["sorting"] = sorting
        if is_top_vc is not UNSET:
            field_dict["isTopVc"] = is_top_vc
        if domains is not UNSET:
            field_dict["domains"] = domains
        if name_patterns is not UNSET:
            field_dict["namePatterns"] = name_patterns
        if crunchbase_slugs is not UNSET:
            field_dict["crunchbaseSlugs"] = crunchbase_slugs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investor_search_body_search_params_num_investments_type_0 import InvestorSearchBodySearchParamsNumInvestmentsType0
        from ..models.investor_search_body_search_params_founded_on_type_0 import InvestorSearchBodySearchParamsFoundedOnType0
        from ..models.investor_search_body_search_params_lead_rate_type_0 import InvestorSearchBodySearchParamsLeadRateType0
        from ..models.investor_search_body_search_params_state_name_type_0 import InvestorSearchBodySearchParamsStateNameType0
        from ..models.investor_search_body_search_params_sorting_type_0 import InvestorSearchBodySearchParamsSortingType0
        from ..models.investor_search_body_search_params_country_code_type_0 import InvestorSearchBodySearchParamsCountryCodeType0
        from ..models.investor_search_body_search_params_num_lead_investments_type_0 import InvestorSearchBodySearchParamsNumLeadInvestmentsType0
        from ..models.investor_search_body_search_params_types_type_0 import InvestorSearchBodySearchParamsTypesType0
        from ..models.investor_search_body_search_params_last_investment_date_type_0 import InvestorSearchBodySearchParamsLastInvestmentDateType0
        d = dict(src_dict)
        def _parse_country_code(data: object) -> Union['InvestorSearchBodySearchParamsCountryCodeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                country_code_type_0 = InvestorSearchBodySearchParamsCountryCodeType0.from_dict(data)



                return country_code_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvestorSearchBodySearchParamsCountryCodeType0', None, Unset], data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))


        def _parse_state_name(data: object) -> Union['InvestorSearchBodySearchParamsStateNameType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_name_type_0 = InvestorSearchBodySearchParamsStateNameType0.from_dict(data)



                return state_name_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvestorSearchBodySearchParamsStateNameType0', None, Unset], data)

        state_name = _parse_state_name(d.pop("stateName", UNSET))


        def _parse_investor_type(data: object) -> Union[InvestorSearchBodySearchParamsInvestorTypeType1, InvestorSearchBodySearchParamsInvestorTypeType2Type1, InvestorSearchBodySearchParamsInvestorTypeType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                investor_type_type_1 = InvestorSearchBodySearchParamsInvestorTypeType1(data)



                return investor_type_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                investor_type_type_2_type_1 = InvestorSearchBodySearchParamsInvestorTypeType2Type1(data)



                return investor_type_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                investor_type_type_3_type_1 = InvestorSearchBodySearchParamsInvestorTypeType3Type1(data)



                return investor_type_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[InvestorSearchBodySearchParamsInvestorTypeType1, InvestorSearchBodySearchParamsInvestorTypeType2Type1, InvestorSearchBodySearchParamsInvestorTypeType3Type1, None, Unset], data)

        investor_type = _parse_investor_type(d.pop("investorType", UNSET))


        def _parse_types(data: object) -> Union['InvestorSearchBodySearchParamsTypesType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                types_type_0 = InvestorSearchBodySearchParamsTypesType0.from_dict(data)



                return types_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvestorSearchBodySearchParamsTypesType0', None, Unset], data)

        types = _parse_types(d.pop("types", UNSET))


        def _parse_num_investments(data: object) -> Union['InvestorSearchBodySearchParamsNumInvestmentsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_investments_type_0 = InvestorSearchBodySearchParamsNumInvestmentsType0.from_dict(data)



                return num_investments_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvestorSearchBodySearchParamsNumInvestmentsType0', None, Unset], data)

        num_investments = _parse_num_investments(d.pop("numInvestments", UNSET))


        def _parse_num_lead_investments(data: object) -> Union['InvestorSearchBodySearchParamsNumLeadInvestmentsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_lead_investments_type_0 = InvestorSearchBodySearchParamsNumLeadInvestmentsType0.from_dict(data)



                return num_lead_investments_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvestorSearchBodySearchParamsNumLeadInvestmentsType0', None, Unset], data)

        num_lead_investments = _parse_num_lead_investments(d.pop("numLeadInvestments", UNSET))


        def _parse_lead_rate(data: object) -> Union['InvestorSearchBodySearchParamsLeadRateType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lead_rate_type_0 = InvestorSearchBodySearchParamsLeadRateType0.from_dict(data)



                return lead_rate_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvestorSearchBodySearchParamsLeadRateType0', None, Unset], data)

        lead_rate = _parse_lead_rate(d.pop("leadRate", UNSET))


        def _parse_last_investment_date(data: object) -> Union['InvestorSearchBodySearchParamsLastInvestmentDateType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_investment_date_type_0 = InvestorSearchBodySearchParamsLastInvestmentDateType0.from_dict(data)



                return last_investment_date_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvestorSearchBodySearchParamsLastInvestmentDateType0', None, Unset], data)

        last_investment_date = _parse_last_investment_date(d.pop("lastInvestmentDate", UNSET))


        def _parse_founded_on(data: object) -> Union['InvestorSearchBodySearchParamsFoundedOnType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                founded_on_type_0 = InvestorSearchBodySearchParamsFoundedOnType0.from_dict(data)



                return founded_on_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvestorSearchBodySearchParamsFoundedOnType0', None, Unset], data)

        founded_on = _parse_founded_on(d.pop("foundedOn", UNSET))


        def _parse_sorting(data: object) -> Union['InvestorSearchBodySearchParamsSortingType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sorting_type_0 = InvestorSearchBodySearchParamsSortingType0.from_dict(data)



                return sorting_type_0
            except: # noqa: E722
                pass
            return cast(Union['InvestorSearchBodySearchParamsSortingType0', None, Unset], data)

        sorting = _parse_sorting(d.pop("sorting", UNSET))


        def _parse_is_top_vc(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_top_vc = _parse_is_top_vc(d.pop("isTopVc", UNSET))


        def _parse_domains(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                domains_type_0 = cast(list[str], data)

                return domains_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        domains = _parse_domains(d.pop("domains", UNSET))


        def _parse_name_patterns(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                name_patterns_type_0 = cast(list[str], data)

                return name_patterns_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        name_patterns = _parse_name_patterns(d.pop("namePatterns", UNSET))


        def _parse_crunchbase_slugs(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                crunchbase_slugs_type_0 = cast(list[str], data)

                return crunchbase_slugs_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        crunchbase_slugs = _parse_crunchbase_slugs(d.pop("crunchbaseSlugs", UNSET))


        investor_search_body_search_params = cls(
            country_code=country_code,
            state_name=state_name,
            investor_type=investor_type,
            types=types,
            num_investments=num_investments,
            num_lead_investments=num_lead_investments,
            lead_rate=lead_rate,
            last_investment_date=last_investment_date,
            founded_on=founded_on,
            sorting=sorting,
            is_top_vc=is_top_vc,
            domains=domains,
            name_patterns=name_patterns,
            crunchbase_slugs=crunchbase_slugs,
        )

        return investor_search_body_search_params

