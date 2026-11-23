from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_investors_type_0 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemInvestorsType0,
    )
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_round_date_type_0 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType0,
    )
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_round_date_type_1 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1,
    )
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_round_types_type_0 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundTypesType0,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0Item")


@_attrs_define
class CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0Item:
    """
    Attributes:
        round_types
            (CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundTypesType0 |
            None | Unset):
        round_date
            (CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType0 |
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1 | None
            | Unset):
        investors
            (CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemInvestorsType0 |
            None | Unset):
    """

    round_types: (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundTypesType0
        | None
        | Unset
    ) = UNSET
    round_date: (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType0
        | CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1
        | None
        | Unset
    ) = UNSET
    investors: (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemInvestorsType0
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_investors_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemInvestorsType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_round_date_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_round_date_type_1 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_round_types_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundTypesType0,  # noqa: PLC0415
        )

        round_types: dict[str, Any] | None | Unset
        if isinstance(self.round_types, Unset):
            round_types = UNSET
        elif isinstance(
            self.round_types,
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundTypesType0,
        ):
            round_types = self.round_types.to_dict()
        else:
            round_types = self.round_types

        round_date: dict[str, Any] | None | Unset
        if isinstance(self.round_date, Unset):
            round_date = UNSET
        elif isinstance(
            self.round_date,
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType0,
        ):
            round_date = self.round_date.to_dict()
        elif isinstance(
            self.round_date,
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1,
        ):
            round_date = self.round_date.to_dict()
        else:
            round_date = self.round_date

        investors: dict[str, Any] | None | Unset
        if isinstance(self.investors, Unset):
            investors = UNSET
        elif isinstance(
            self.investors,
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemInvestorsType0,
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
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_investors_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemInvestorsType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_round_date_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_round_date_type_1 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item_round_types_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundTypesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_round_types(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundTypesType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_types_type_0 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundTypesType0.from_dict(
                    data
                )

                return round_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundTypesType0
                | None
                | Unset,
                data,
            )

        round_types = _parse_round_types(d.pop("roundTypes", UNSET))

        def _parse_round_date(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType0
            | CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_date_type_0 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType0.from_dict(
                    data
                )

                return round_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_date_type_1 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1.from_dict(
                    data
                )

                return round_date_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType0
                | CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1
                | None
                | Unset,
                data,
            )

        round_date = _parse_round_date(d.pop("roundDate", UNSET))

        def _parse_investors(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemInvestorsType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                investors_type_0 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemInvestorsType0.from_dict(
                    data
                )

                return investors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsFundingRoundsV2Type0AllOfType0ItemInvestorsType0
                | None
                | Unset,
                data,
            )

        investors = _parse_investors(d.pop("investors", UNSET))

        create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item = cls(
            round_types=round_types,
            round_date=round_date,
            investors=investors,
        )

        create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item.additional_properties = d
        return create_saved_search_body_search_params_type_0_company_search_params_funding_rounds_v2_type_0_all_of_type_0_item

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
