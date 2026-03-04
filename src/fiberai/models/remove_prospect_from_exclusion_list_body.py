from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.remove_prospect_from_exclusion_list_body_excluded_prospect_details import RemoveProspectFromExclusionListBodyExcludedProspectDetails





T = TypeVar("T", bound="RemoveProspectFromExclusionListBody")



@_attrs_define
class RemoveProspectFromExclusionListBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            list_id (str): Id of the prospect exclusion lists to remove the prospect from
            excluded_prospect_details (RemoveProspectFromExclusionListBodyExcludedProspectDetails): Details of the prospects
                to remove from the exclusion list
     """

    api_key: str
    list_id: str
    excluded_prospect_details: 'RemoveProspectFromExclusionListBodyExcludedProspectDetails'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.remove_prospect_from_exclusion_list_body_excluded_prospect_details import RemoveProspectFromExclusionListBodyExcludedProspectDetails
        api_key = self.api_key

        list_id = self.list_id

        excluded_prospect_details = self.excluded_prospect_details.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "listId": list_id,
            "excludedProspectDetails": excluded_prospect_details,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remove_prospect_from_exclusion_list_body_excluded_prospect_details import RemoveProspectFromExclusionListBodyExcludedProspectDetails
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        list_id = d.pop("listId")

        excluded_prospect_details = RemoveProspectFromExclusionListBodyExcludedProspectDetails.from_dict(d.pop("excludedProspectDetails"))




        remove_prospect_from_exclusion_list_body = cls(
            api_key=api_key,
            list_id=list_id,
            excluded_prospect_details=excluded_prospect_details,
        )


        remove_prospect_from_exclusion_list_body.additional_properties = d
        return remove_prospect_from_exclusion_list_body

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
