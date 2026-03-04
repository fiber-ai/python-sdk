from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_profile_params_past_job_text_type_0_criteria_item_field import SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemField
from ..models.sync_combined_search_body_profile_params_past_job_text_type_0_criteria_item_rule import SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemRule
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItem")



@_attrs_define
class SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItem:
    """ 
        Attributes:
            field (SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemField):
            rule (SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemRule):
            text (Union[None, Unset, str]):
     """

    field: SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemField
    rule: SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemRule
    text: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field = self.field.value

        rule = self.rule.value

        text: Union[None, Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "rule": rule,
        })
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemField(d.pop("field"))




        rule = SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemRule(d.pop("rule"))




        def _parse_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text = _parse_text(d.pop("text", UNSET))


        sync_combined_search_body_profile_params_past_job_text_type_0_criteria_item = cls(
            field=field,
            rule=rule,
            text=text,
        )


        sync_combined_search_body_profile_params_past_job_text_type_0_criteria_item.additional_properties = d
        return sync_combined_search_body_profile_params_past_job_text_type_0_criteria_item

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
