from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_1 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType1
  from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_2 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType2
  from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_3 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3
  from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_0 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0





T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0Item")



@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0Item:
    """ 
        Attributes:
            num_matching_employees
                (Union['KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0',
                'KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType1',
                'KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType2',
                'KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3']):
     """

    num_matching_employees: Union['KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0', 'KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType1', 'KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType2', 'KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_1 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType1
        from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_2 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType2
        from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_3 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3
        from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_0 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0
        num_matching_employees: dict[str, Any]
        if isinstance(self.num_matching_employees, KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0):
            num_matching_employees = self.num_matching_employees.to_dict()
        elif isinstance(self.num_matching_employees, KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType1):
            num_matching_employees = self.num_matching_employees.to_dict()
        elif isinstance(self.num_matching_employees, KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType2):
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
        from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_1 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType1
        from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_2 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType2
        from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_3 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3
        from ..models.kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item_num_matching_employees_type_0 import KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0
        d = dict(src_dict)
        def _parse_num_matching_employees(data: object) -> Union['KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0', 'KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType1', 'KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType2', 'KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_employees_type_0 = KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType0.from_dict(data)



                return num_matching_employees_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_employees_type_1 = KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType1.from_dict(data)



                return num_matching_employees_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                num_matching_employees_type_2 = KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType2.from_dict(data)



                return num_matching_employees_type_2
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            num_matching_employees_type_3 = KitchenSinkCompanyResponse200OutputDataItemRoleCountMatchesType0ItemNumMatchingEmployeesType3.from_dict(data)



            return num_matching_employees_type_3

        num_matching_employees = _parse_num_matching_employees(d.pop("numMatchingEmployees"))


        kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item = cls(
            num_matching_employees=num_matching_employees,
        )


        kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item.additional_properties = d
        return kitchen_sink_company_response_200_output_data_item_role_count_matches_type_0_item

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
