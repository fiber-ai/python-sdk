from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_job_function import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemJobFunction
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_count_criteria_type_0 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType0
  from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_count_criteria_type_2 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType2
  from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_count_criteria_type_1 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType1





T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0Item")



@_attrs_define
class CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0Item:
    """ 
        Attributes:
            job_function
                (CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemJobFunction):
            count_criteria (Union['CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0
                ItemCountCriteriaType0', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllTy
                pe0ItemCountCriteriaType1', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAl
                lType0ItemCountCriteriaType2']):
     """

    job_function: CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemJobFunction
    count_criteria: Union['CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType0', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType1', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType2']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_count_criteria_type_0 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType0
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_count_criteria_type_2 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType2
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_count_criteria_type_1 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType1
        job_function = self.job_function.value

        count_criteria: dict[str, Any]
        if isinstance(self.count_criteria, CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType0):
            count_criteria = self.count_criteria.to_dict()
        elif isinstance(self.count_criteria, CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType1):
            count_criteria = self.count_criteria.to_dict()
        else:
            count_criteria = self.count_criteria.to_dict()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "jobFunction": job_function,
            "countCriteria": count_criteria,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_count_criteria_type_0 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType0
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_count_criteria_type_2 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType2
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item_count_criteria_type_1 import CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType1
        d = dict(src_dict)
        job_function = CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemJobFunction(d.pop("jobFunction"))




        def _parse_count_criteria(data: object) -> Union['CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType0', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType1', 'CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType2']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                count_criteria_type_0 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType0.from_dict(data)



                return count_criteria_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                count_criteria_type_1 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType1.from_dict(data)



                return count_criteria_type_1
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            count_criteria_type_2 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsEmployeeTrendsType0ObeysAllType0ItemCountCriteriaType2.from_dict(data)



            return count_criteria_type_2

        count_criteria = _parse_count_criteria(d.pop("countCriteria"))


        create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item = cls(
            job_function=job_function,
            count_criteria=count_criteria,
        )


        create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item.additional_properties = d
        return create_saved_search_body_search_params_type_1_company_search_params_employee_trends_type_0_obeys_all_type_0_item

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
