from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_job_function import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemJobFunction
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_0 import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0
  from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_2 import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2
  from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1 import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1





T = TypeVar("T", bound="CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0Item")



@_attrs_define
class CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0Item:
    """ 
        Attributes:
            job_function (CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemJobFunction):
            count_criteria (Union['CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0',
                'CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1',
                'CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2']):
     """

    job_function: CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemJobFunction
    count_criteria: Union['CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0', 'CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1', 'CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_0 import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0
        from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_2 import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2
        from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1 import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1
        job_function = self.job_function.value

        count_criteria: dict[str, Any]
        if isinstance(self.count_criteria, CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0):
            count_criteria = self.count_criteria.to_dict()
        elif isinstance(self.count_criteria, CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1):
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
        from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_0 import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0
        from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_2 import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2
        from ..models.combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1 import CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1
        d = dict(src_dict)
        job_function = CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemJobFunction(d.pop("jobFunction"))




        def _parse_count_criteria(data: object) -> Union['CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0', 'CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1', 'CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                count_criteria_type_0 = CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0.from_dict(data)



                return count_criteria_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                count_criteria_type_1 = CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1.from_dict(data)



                return count_criteria_type_1
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            count_criteria_type_2 = CombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2.from_dict(data)



            return count_criteria_type_2

        count_criteria = _parse_count_criteria(d.pop("countCriteria"))


        combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item = cls(
            job_function=job_function,
            count_criteria=count_criteria,
        )


        combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item.additional_properties = d
        return combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item

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
