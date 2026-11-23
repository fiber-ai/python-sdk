from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_investors_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemInvestorsType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_round_date_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType0,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_round_date_type_1 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1,
    )
    from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_round_types_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundTypesType0,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0Item")


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0Item:
    """
    Attributes:
        round_types (None |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundTypesType0 |
            Unset):
        round_date (None |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType0 |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1 |
            Unset):
        investors (None |
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemInvestorsType0 |
            Unset):
    """

    round_types: (
        None
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundTypesType0
        | Unset
    ) = UNSET
    round_date: (
        None
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType0
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1
        | Unset
    ) = UNSET
    investors: (
        None
        | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemInvestorsType0
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_investors_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemInvestorsType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_round_date_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_round_date_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_round_types_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundTypesType0,  # noqa: PLC0415
        )

        round_types: dict[str, Any] | None | Unset
        if isinstance(self.round_types, Unset):
            round_types = UNSET
        elif isinstance(
            self.round_types,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundTypesType0,
        ):
            round_types = self.round_types.to_dict()
        else:
            round_types = self.round_types

        round_date: dict[str, Any] | None | Unset
        if isinstance(self.round_date, Unset):
            round_date = UNSET
        elif isinstance(
            self.round_date,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType0,
        ):
            round_date = self.round_date.to_dict()
        elif isinstance(
            self.round_date,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1,
        ):
            round_date = self.round_date.to_dict()
        else:
            round_date = self.round_date

        investors: dict[str, Any] | None | Unset
        if isinstance(self.investors, Unset):
            investors = UNSET
        elif isinstance(
            self.investors,
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemInvestorsType0,
        ):
            investors = self.investors.to_dict()
        else:
            investors = self.investors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if round_types is not UNSET:
            field_dict["roundTypes"] = round_types
        if round_date is not UNSET:
            field_dict["roundDate"] = round_date
        if investors is not UNSET:
            field_dict["investors"] = investors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_investors_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemInvestorsType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_round_date_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_round_date_type_1 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item_round_types_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundTypesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_round_types(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundTypesType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_types_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundTypesType0.from_dict(
                    data
                )

                return round_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundTypesType0
                | Unset,
                data,
            )

        round_types = _parse_round_types(d.pop("roundTypes", UNSET))

        def _parse_round_date(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType0
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_date_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType0.from_dict(
                    data
                )

                return round_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_date_type_1 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1.from_dict(
                    data
                )

                return round_date_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType0
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemRoundDateType1
                | Unset,
                data,
            )

        round_date = _parse_round_date(d.pop("roundDate", UNSET))

        def _parse_investors(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemInvestorsType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investors_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemInvestorsType0.from_dict(
                    data
                )

                return investors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AnyOfType0ItemInvestorsType0
                | Unset,
                data,
            )

        investors = _parse_investors(d.pop("investors", UNSET))

        paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item = cls(
            round_types=round_types,
            round_date=round_date,
            investors=investors,
        )

        paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item.additional_properties = d
        return paginated_combined_search_body_company_config_type_0_search_params_funding_rounds_v2_type_0_any_of_type_0_item

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
