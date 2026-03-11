from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_0 import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType0,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_1 import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType1,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_2 import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType2,
    )
    from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_3 import (
        PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType3,
    )


T = TypeVar("T", bound="PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0Item")


@_attrs_define
class PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0Item:
    """
    Attributes:
        num_matching_employees
            (PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType0 |
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType1 |
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType2 |
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType3):
    """

    num_matching_employees: (
        PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType0
        | PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType1
        | PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType2
        | PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType3
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_0 import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType0,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_1 import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType1,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_2 import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType2,
        )

        num_matching_employees: dict[str, Any]
        if isinstance(
            self.num_matching_employees,
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType0,
        ):
            num_matching_employees = self.num_matching_employees.to_dict()
        elif isinstance(
            self.num_matching_employees,
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType1,
        ):
            num_matching_employees = self.num_matching_employees.to_dict()
        elif isinstance(
            self.num_matching_employees,
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType2,
        ):
            num_matching_employees = self.num_matching_employees.to_dict()
        else:
            num_matching_employees = self.num_matching_employees.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numMatchingEmployees": num_matching_employees,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_0 import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType0,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_1 import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType1,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_2 import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType2,
        )
        from ..models.poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item_num_matching_employees_type_3 import (
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType3,
        )

        d = dict(src_dict)

        def _parse_num_matching_employees(
            data: object,
        ) -> (
            PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType0
            | PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType1
            | PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType2
            | PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_employees_type_0 = PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType0.from_dict(
                    data
                )

                return num_matching_employees_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_employees_type_1 = PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType1.from_dict(
                    data
                )

                return num_matching_employees_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_employees_type_2 = PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType2.from_dict(
                    data
                )

                return num_matching_employees_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            num_matching_employees_type_3 = PollCombinedSearchResponse200OutputDataType0ItemsItemRoleCountMatchesType0ItemNumMatchingEmployeesType3.from_dict(
                data
            )

            return num_matching_employees_type_3

        num_matching_employees = _parse_num_matching_employees(d.pop("numMatchingEmployees"))

        poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item = cls(
            num_matching_employees=num_matching_employees,
        )

        poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item.additional_properties = d
        return poll_combined_search_response_200_output_data_type_0_items_item_role_count_matches_type_0_item

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
