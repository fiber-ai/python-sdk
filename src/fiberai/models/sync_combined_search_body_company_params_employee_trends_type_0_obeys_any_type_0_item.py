from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_job_function import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemJobFunction
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1
  from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_2 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2
  from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0





T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0Item")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0Item:
    """ 
        Attributes:
            job_function (SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemJobFunction):
            count_criteria
                (Union['SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0',
                'SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1',
                'SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2']):
     """

    job_function: SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemJobFunction
    count_criteria: Union['SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0', 'SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1', 'SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_2 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0
        job_function = self.job_function.value

        count_criteria: dict[str, Any]
        if isinstance(self.count_criteria, SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0):
            count_criteria = self.count_criteria.to_dict()
        elif isinstance(self.count_criteria, SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1):
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
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_1 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_2 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2
        from ..models.sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item_count_criteria_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0
        d = dict(src_dict)
        job_function = SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemJobFunction(d.pop("jobFunction"))




        def _parse_count_criteria(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0', 'SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1', 'SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                count_criteria_type_0 = SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType0.from_dict(data)



                return count_criteria_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                count_criteria_type_1 = SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType1.from_dict(data)



                return count_criteria_type_1
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            count_criteria_type_2 = SyncCombinedSearchBodyCompanyParamsEmployeeTrendsType0ObeysAnyType0ItemCountCriteriaType2.from_dict(data)



            return count_criteria_type_2

        count_criteria = _parse_count_criteria(d.pop("countCriteria"))


        sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item = cls(
            job_function=job_function,
            count_criteria=count_criteria,
        )


        sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item.additional_properties = d
        return sync_combined_search_body_company_params_employee_trends_type_0_obeys_any_type_0_item

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
