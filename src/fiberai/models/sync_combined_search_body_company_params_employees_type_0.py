from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_company_params_employees_type_0_joiner import SyncCombinedSearchBodyCompanyParamsEmployeesType0Joiner
from typing import cast

if TYPE_CHECKING:
  from ..models.sync_combined_search_body_company_params_employees_type_0_rules_item import SyncCombinedSearchBodyCompanyParamsEmployeesType0RulesItem





T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsEmployeesType0")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsEmployeesType0:
    """ 
        Attributes:
            rules (list['SyncCombinedSearchBodyCompanyParamsEmployeesType0RulesItem']):
            joiner (SyncCombinedSearchBodyCompanyParamsEmployeesType0Joiner):
     """

    rules: list['SyncCombinedSearchBodyCompanyParamsEmployeesType0RulesItem']
    joiner: SyncCombinedSearchBodyCompanyParamsEmployeesType0Joiner
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_employees_type_0_rules_item import SyncCombinedSearchBodyCompanyParamsEmployeesType0RulesItem
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)



        joiner = self.joiner.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rules": rules,
            "joiner": joiner,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_employees_type_0_rules_item import SyncCombinedSearchBodyCompanyParamsEmployeesType0RulesItem
        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in (_rules):
            rules_item = SyncCombinedSearchBodyCompanyParamsEmployeesType0RulesItem.from_dict(rules_item_data)



            rules.append(rules_item)


        joiner = SyncCombinedSearchBodyCompanyParamsEmployeesType0Joiner(d.pop("joiner"))




        sync_combined_search_body_company_params_employees_type_0 = cls(
            rules=rules,
            joiner=joiner,
        )


        sync_combined_search_body_company_params_employees_type_0.additional_properties = d
        return sync_combined_search_body_company_params_employees_type_0

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
