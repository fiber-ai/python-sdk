from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_search_body_search_params_vesting_schedule_type_0_cadences_type_0_item import (
    CompanySearchBodySearchParamsVestingScheduleType0CadencesType0Item,
)
from ..models.company_search_body_search_params_vesting_schedule_type_0_scope_type_1 import (
    CompanySearchBodySearchParamsVestingScheduleType0ScopeType1,
)
from ..models.company_search_body_search_params_vesting_schedule_type_0_scope_type_2_type_1 import (
    CompanySearchBodySearchParamsVestingScheduleType0ScopeType2Type1,
)
from ..models.company_search_body_search_params_vesting_schedule_type_0_scope_type_3_type_1 import (
    CompanySearchBodySearchParamsVestingScheduleType0ScopeType3Type1,
)
from ..models.company_search_body_search_params_vesting_schedule_type_0_shapes_type_0_item import (
    CompanySearchBodySearchParamsVestingScheduleType0ShapesType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_search_body_search_params_vesting_schedule_type_0_total_years_type_0 import (
        CompanySearchBodySearchParamsVestingScheduleType0TotalYearsType0,
    )


T = TypeVar("T", bound="CompanySearchBodySearchParamsVestingScheduleType0")


@_attrs_define
class CompanySearchBodySearchParamsVestingScheduleType0:
    """
    Attributes:
        scope (CompanySearchBodySearchParamsVestingScheduleType0ScopeType1 |
            CompanySearchBodySearchParamsVestingScheduleType0ScopeType2Type1 |
            CompanySearchBodySearchParamsVestingScheduleType0ScopeType3Type1 | None | Unset):
        shapes (list[CompanySearchBodySearchParamsVestingScheduleType0ShapesType0Item] | None | Unset):
        total_years (CompanySearchBodySearchParamsVestingScheduleType0TotalYearsType0 | None | Unset):
        cadences (list[CompanySearchBodySearchParamsVestingScheduleType0CadencesType0Item] | None | Unset):
        has_one_year_cliff (bool | None | Unset):
    """

    scope: (
        CompanySearchBodySearchParamsVestingScheduleType0ScopeType1
        | CompanySearchBodySearchParamsVestingScheduleType0ScopeType2Type1
        | CompanySearchBodySearchParamsVestingScheduleType0ScopeType3Type1
        | None
        | Unset
    ) = UNSET
    shapes: list[CompanySearchBodySearchParamsVestingScheduleType0ShapesType0Item] | None | Unset = UNSET
    total_years: CompanySearchBodySearchParamsVestingScheduleType0TotalYearsType0 | None | Unset = UNSET
    cadences: list[CompanySearchBodySearchParamsVestingScheduleType0CadencesType0Item] | None | Unset = UNSET
    has_one_year_cliff: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_body_search_params_vesting_schedule_type_0_total_years_type_0 import (
            CompanySearchBodySearchParamsVestingScheduleType0TotalYearsType0,  # noqa: PLC0415
        )

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        elif isinstance(self.scope, CompanySearchBodySearchParamsVestingScheduleType0ScopeType1):
            scope = self.scope.value
        elif isinstance(self.scope, CompanySearchBodySearchParamsVestingScheduleType0ScopeType2Type1):
            scope = self.scope.value
        elif isinstance(self.scope, CompanySearchBodySearchParamsVestingScheduleType0ScopeType3Type1):
            scope = self.scope.value
        else:
            scope = self.scope

        shapes: list[str] | None | Unset
        if isinstance(self.shapes, Unset):
            shapes = UNSET
        elif isinstance(self.shapes, list):
            shapes = []
            for shapes_type_0_item_data in self.shapes:
                shapes_type_0_item = shapes_type_0_item_data.value
                shapes.append(shapes_type_0_item)

        else:
            shapes = self.shapes

        total_years: dict[str, Any] | None | Unset
        if isinstance(self.total_years, Unset):
            total_years = UNSET
        elif isinstance(self.total_years, CompanySearchBodySearchParamsVestingScheduleType0TotalYearsType0):
            total_years = self.total_years.to_dict()
        else:
            total_years = self.total_years

        cadences: list[str] | None | Unset
        if isinstance(self.cadences, Unset):
            cadences = UNSET
        elif isinstance(self.cadences, list):
            cadences = []
            for cadences_type_0_item_data in self.cadences:
                cadences_type_0_item = cadences_type_0_item_data.value
                cadences.append(cadences_type_0_item)

        else:
            cadences = self.cadences

        has_one_year_cliff: bool | None | Unset
        if isinstance(self.has_one_year_cliff, Unset):
            has_one_year_cliff = UNSET
        else:
            has_one_year_cliff = self.has_one_year_cliff

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if shapes is not UNSET:
            field_dict["shapes"] = shapes
        if total_years is not UNSET:
            field_dict["totalYears"] = total_years
        if cadences is not UNSET:
            field_dict["cadences"] = cadences
        if has_one_year_cliff is not UNSET:
            field_dict["hasOneYearCliff"] = has_one_year_cliff

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params_vesting_schedule_type_0_total_years_type_0 import (
            CompanySearchBodySearchParamsVestingScheduleType0TotalYearsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_scope(
            data: object,
        ) -> (
            CompanySearchBodySearchParamsVestingScheduleType0ScopeType1
            | CompanySearchBodySearchParamsVestingScheduleType0ScopeType2Type1
            | CompanySearchBodySearchParamsVestingScheduleType0ScopeType3Type1
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
                scope_type_1 = CompanySearchBodySearchParamsVestingScheduleType0ScopeType1(data)

                return scope_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scope_type_2_type_1 = CompanySearchBodySearchParamsVestingScheduleType0ScopeType2Type1(data)

                return scope_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scope_type_3_type_1 = CompanySearchBodySearchParamsVestingScheduleType0ScopeType3Type1(data)

                return scope_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanySearchBodySearchParamsVestingScheduleType0ScopeType1
                | CompanySearchBodySearchParamsVestingScheduleType0ScopeType2Type1
                | CompanySearchBodySearchParamsVestingScheduleType0ScopeType3Type1
                | None
                | Unset,
                data,
            )

        scope = _parse_scope(d.pop("scope", UNSET))

        def _parse_shapes(
            data: object,
        ) -> list[CompanySearchBodySearchParamsVestingScheduleType0ShapesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                shapes_type_0 = []
                _shapes_type_0 = data
                for shapes_type_0_item_data in _shapes_type_0:
                    shapes_type_0_item = CompanySearchBodySearchParamsVestingScheduleType0ShapesType0Item(
                        shapes_type_0_item_data
                    )

                    shapes_type_0.append(shapes_type_0_item)

                return shapes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanySearchBodySearchParamsVestingScheduleType0ShapesType0Item] | None | Unset, data)

        shapes = _parse_shapes(d.pop("shapes", UNSET))

        def _parse_total_years(
            data: object,
        ) -> CompanySearchBodySearchParamsVestingScheduleType0TotalYearsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_years_type_0 = CompanySearchBodySearchParamsVestingScheduleType0TotalYearsType0.from_dict(data)

                return total_years_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanySearchBodySearchParamsVestingScheduleType0TotalYearsType0 | None | Unset, data)

        total_years = _parse_total_years(d.pop("totalYears", UNSET))

        def _parse_cadences(
            data: object,
        ) -> list[CompanySearchBodySearchParamsVestingScheduleType0CadencesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cadences_type_0 = []
                _cadences_type_0 = data
                for cadences_type_0_item_data in _cadences_type_0:
                    cadences_type_0_item = CompanySearchBodySearchParamsVestingScheduleType0CadencesType0Item(
                        cadences_type_0_item_data
                    )

                    cadences_type_0.append(cadences_type_0_item)

                return cadences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanySearchBodySearchParamsVestingScheduleType0CadencesType0Item] | None | Unset, data)

        cadences = _parse_cadences(d.pop("cadences", UNSET))

        def _parse_has_one_year_cliff(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_one_year_cliff = _parse_has_one_year_cliff(d.pop("hasOneYearCliff", UNSET))

        company_search_body_search_params_vesting_schedule_type_0 = cls(
            scope=scope,
            shapes=shapes,
            total_years=total_years,
            cadences=cadences,
            has_one_year_cliff=has_one_year_cliff,
        )

        company_search_body_search_params_vesting_schedule_type_0.additional_properties = d
        return company_search_body_search_params_vesting_schedule_type_0

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
