from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_0 import (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_1 import (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1,
    )
    from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investment_rounds_type_0 import (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestmentRoundsType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_0 import (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType0,
    )
    from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_1 import (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType1,
    )
    from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_2 import (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType2,
    )
    from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_3 import (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType3,
    )


T = TypeVar(
    "T", bound="TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0Item"
)


@_attrs_define
class TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0Item:
    """
    Attributes:
        investor_identifier (TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfTyp
            e0ItemInvestorIdentifierType0 | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Typ
            e0NoneOfType0ItemInvestorIdentifierType1 | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0Inv
            estorsV2Type0NoneOfType0ItemInvestorIdentifierType2 | TextToCombinedSearchParamResponse200OutputCompanySearchPar
            amsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType3):
        invested_at (None |
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType0
            |
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1
            | Unset):
        investment_rounds (None | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0None
            OfType0ItemInvestmentRoundsType0 | Unset):
    """

    investor_identifier: (
        TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType0
        | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType1
        | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType2
        | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType3
    )
    invested_at: (
        None
        | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType0
        | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1
        | Unset
    ) = UNSET
    investment_rounds: (
        None
        | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestmentRoundsType0
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_0 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_1 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investment_rounds_type_0 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestmentRoundsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_0 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_1 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_2 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType2,
        )

        investor_identifier: dict[str, Any]
        if isinstance(
            self.investor_identifier,
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType0,
        ):
            investor_identifier = self.investor_identifier.to_dict()
        elif isinstance(
            self.investor_identifier,
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType1,
        ):
            investor_identifier = self.investor_identifier.to_dict()
        elif isinstance(
            self.investor_identifier,
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType2,
        ):
            investor_identifier = self.investor_identifier.to_dict()
        else:
            investor_identifier = self.investor_identifier.to_dict()

        invested_at: dict[str, Any] | None | Unset
        if isinstance(self.invested_at, Unset):
            invested_at = UNSET
        elif isinstance(
            self.invested_at,
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType0,
        ):
            invested_at = self.invested_at.to_dict()
        elif isinstance(
            self.invested_at,
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1,
        ):
            invested_at = self.invested_at.to_dict()
        else:
            invested_at = self.invested_at

        investment_rounds: dict[str, Any] | None | Unset
        if isinstance(self.investment_rounds, Unset):
            investment_rounds = UNSET
        elif isinstance(
            self.investment_rounds,
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestmentRoundsType0,
        ):
            investment_rounds = self.investment_rounds.to_dict()
        else:
            investment_rounds = self.investment_rounds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "investorIdentifier": investor_identifier,
            }
        )
        if invested_at is not UNSET:
            field_dict["investedAt"] = invested_at
        if investment_rounds is not UNSET:
            field_dict["investmentRounds"] = investment_rounds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_0 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_invested_at_type_1 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investment_rounds_type_0 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestmentRoundsType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_0 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType0,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_1 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType1,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_2 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType2,
        )
        from ..models.text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item_investor_identifier_type_3 import (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType3,
        )

        d = dict(src_dict)

        def _parse_investor_identifier(
            data: object,
        ) -> (
            TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType0
            | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType1
            | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType2
            | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investor_identifier_type_0 = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType0.from_dict(
                    data
                )

                return investor_identifier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investor_identifier_type_1 = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType1.from_dict(
                    data
                )

                return investor_identifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investor_identifier_type_2 = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType2.from_dict(
                    data
                )

                return investor_identifier_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            investor_identifier_type_3 = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestorIdentifierType3.from_dict(
                data
            )

            return investor_identifier_type_3

        investor_identifier = _parse_investor_identifier(d.pop("investorIdentifier"))

        def _parse_invested_at(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType0
            | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invested_at_type_0 = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType0.from_dict(
                    data
                )

                return invested_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                invested_at_type_1 = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1.from_dict(
                    data
                )

                return invested_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType0
                | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestedAtType1
                | Unset,
                data,
            )

        invested_at = _parse_invested_at(d.pop("investedAt", UNSET))

        def _parse_investment_rounds(
            data: object,
        ) -> (
            None
            | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestmentRoundsType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investment_rounds_type_0 = TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestmentRoundsType0.from_dict(
                    data
                )

                return investment_rounds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchParamResponse200OutputCompanySearchParamsType0InvestorsV2Type0NoneOfType0ItemInvestmentRoundsType0
                | Unset,
                data,
            )

        investment_rounds = _parse_investment_rounds(d.pop("investmentRounds", UNSET))

        text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item = cls(
            investor_identifier=investor_identifier,
            invested_at=invested_at,
            investment_rounds=investment_rounds,
        )

        text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item.additional_properties = d
        return text_to_combined_search_param_response_200_output_company_search_params_type_0_investors_v2_type_0_none_of_type_0_item

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
