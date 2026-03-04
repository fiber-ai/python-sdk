from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_profile_params_past_job_text_type_0_joiner import SyncCombinedSearchBodyProfileParamsPastJobTextType0Joiner
from typing import cast

if TYPE_CHECKING:
  from ..models.sync_combined_search_body_profile_params_past_job_text_type_0_criteria_item import SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItem





T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsPastJobTextType0")



@_attrs_define
class SyncCombinedSearchBodyProfileParamsPastJobTextType0:
    """ 
        Attributes:
            joiner (SyncCombinedSearchBodyProfileParamsPastJobTextType0Joiner):
            criteria (list['SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItem']):
     """

    joiner: SyncCombinedSearchBodyProfileParamsPastJobTextType0Joiner
    criteria: list['SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItem']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_profile_params_past_job_text_type_0_criteria_item import SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItem
        joiner = self.joiner.value

        criteria = []
        for criteria_item_data in self.criteria:
            criteria_item = criteria_item_data.to_dict()
            criteria.append(criteria_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "joiner": joiner,
            "criteria": criteria,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_profile_params_past_job_text_type_0_criteria_item import SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItem
        d = dict(src_dict)
        joiner = SyncCombinedSearchBodyProfileParamsPastJobTextType0Joiner(d.pop("joiner"))




        criteria = []
        _criteria = d.pop("criteria")
        for criteria_item_data in (_criteria):
            criteria_item = SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItem.from_dict(criteria_item_data)



            criteria.append(criteria_item)


        sync_combined_search_body_profile_params_past_job_text_type_0 = cls(
            joiner=joiner,
            criteria=criteria,
        )


        sync_combined_search_body_profile_params_past_job_text_type_0.additional_properties = d
        return sync_combined_search_body_profile_params_past_job_text_type_0

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
