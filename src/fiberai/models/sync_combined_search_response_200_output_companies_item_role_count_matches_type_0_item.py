from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_2 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType2
  from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_0 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType0
  from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_1 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType1
  from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_3 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType3





T = TypeVar("T", bound="SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item")



@_attrs_define
class SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0Item:
    """ 
        Attributes:
            num_matching_employees
                (Union['SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType0',
                'SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType1',
                'SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType2',
                'SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType3']):
     """

    num_matching_employees: Union['SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType0', 'SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType1', 'SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType2', 'SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType3']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_2 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType2
        from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_0 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType0
        from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_1 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType1
        from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_3 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType3
        num_matching_employees: dict[str, Any]
        if isinstance(self.num_matching_employees, SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType0):
            num_matching_employees = self.num_matching_employees.to_dict()
        elif isinstance(self.num_matching_employees, SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType1):
            num_matching_employees = self.num_matching_employees.to_dict()
        elif isinstance(self.num_matching_employees, SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType2):
            num_matching_employees = self.num_matching_employees.to_dict()
        else:
            num_matching_employees = self.num_matching_employees.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "numMatchingEmployees": num_matching_employees,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_2 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType2
        from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_0 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType0
        from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_1 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType1
        from ..models.sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item_num_matching_employees_type_3 import SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType3
        d = dict(src_dict)
        def _parse_num_matching_employees(data: object) -> Union['SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType0', 'SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType1', 'SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType2', 'SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType3']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_employees_type_0 = SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType0.from_dict(data)



                return num_matching_employees_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_employees_type_1 = SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType1.from_dict(data)



                return num_matching_employees_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_employees_type_2 = SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType2.from_dict(data)



                return num_matching_employees_type_2
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            num_matching_employees_type_3 = SyncCombinedSearchResponse200OutputCompaniesItemRoleCountMatchesType0ItemNumMatchingEmployeesType3.from_dict(data)



            return num_matching_employees_type_3

        num_matching_employees = _parse_num_matching_employees(d.pop("numMatchingEmployees"))


        sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item = cls(
            num_matching_employees=num_matching_employees,
        )


        sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item.additional_properties = d
        return sync_combined_search_response_200_output_companies_item_role_count_matches_type_0_item

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
