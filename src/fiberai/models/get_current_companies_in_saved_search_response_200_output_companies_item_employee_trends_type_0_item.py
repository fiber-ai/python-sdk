from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item_functions_type_1 import (
    GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType1,
)
from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item_functions_type_2_type_1 import (
    GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1,
)
from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item_functions_type_3_type_1 import (
    GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item_changes_type_0_item import (
        GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemChangesType0Item,
    )


T = TypeVar("T", bound="GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item")


@_attrs_define
class GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0Item:
    """
    Attributes:
        functions (GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType1 |
            GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1 |
            GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1 | None
            | Unset):
        current_count (float | None | Unset):
        changes
            (list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemChangesType0Item] |
            None | Unset):
    """

    functions: (
        GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType1
        | GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1
        | GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1
        | None
        | Unset
    ) = UNSET
    current_count: float | None | Unset = UNSET
    changes: (
        list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemChangesType0Item]
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        functions: None | str | Unset
        if isinstance(self.functions, Unset):
            functions = UNSET
        elif isinstance(
            self.functions,
            GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType1,
        ):
            functions = self.functions.value
        elif isinstance(
            self.functions,
            GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1,
        ):
            functions = self.functions.value
        elif isinstance(
            self.functions,
            GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1,
        ):
            functions = self.functions.value
        else:
            functions = self.functions

        current_count: float | None | Unset
        if isinstance(self.current_count, Unset):
            current_count = UNSET
        else:
            current_count = self.current_count

        changes: list[dict[str, Any]] | None | Unset
        if isinstance(self.changes, Unset):
            changes = UNSET
        elif isinstance(self.changes, list):
            changes = []
            for changes_type_0_item_data in self.changes:
                changes_type_0_item = changes_type_0_item_data.to_dict()
                changes.append(changes_type_0_item)

        else:
            changes = self.changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if functions is not UNSET:
            field_dict["functions"] = functions
        if current_count is not UNSET:
            field_dict["current_count"] = current_count
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item_changes_type_0_item import (
            GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemChangesType0Item,
        )

        d = dict(src_dict)

        def _parse_functions(
            data: object,
        ) -> (
            GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType1
            | GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1
            | GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1
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
                functions_type_1 = (
                    GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType1(
                        data
                    )
                )

                return functions_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                functions_type_2_type_1 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1(
                    data
                )

                return functions_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                functions_type_3_type_1 = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1(
                    data
                )

                return functions_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType1
                | GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1
                | GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1
                | None
                | Unset,
                data,
            )

        functions = _parse_functions(d.pop("functions", UNSET))

        def _parse_current_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_count = _parse_current_count(d.pop("current_count", UNSET))

        def _parse_changes(
            data: object,
        ) -> (
            list[GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemChangesType0Item]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changes_type_0 = []
                _changes_type_0 = data
                for changes_type_0_item_data in _changes_type_0:
                    changes_type_0_item = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemChangesType0Item.from_dict(
                        changes_type_0_item_data
                    )

                    changes_type_0.append(changes_type_0_item)

                return changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemEmployeeTrendsType0ItemChangesType0Item
                ]
                | None
                | Unset,
                data,
            )

        changes = _parse_changes(d.pop("changes", UNSET))

        get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item = cls(
            functions=functions,
            current_count=current_count,
            changes=changes,
        )

        get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item.additional_properties = d
        return get_current_companies_in_saved_search_response_200_output_companies_item_employee_trends_type_0_item

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
