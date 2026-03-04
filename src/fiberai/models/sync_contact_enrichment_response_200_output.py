from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.sync_contact_enrichment_response_200_output_profile import SyncContactEnrichmentResponse200OutputProfile





T = TypeVar("T", bound="SyncContactEnrichmentResponse200Output")



@_attrs_define
class SyncContactEnrichmentResponse200Output:
    """ 
        Attributes:
            profile (SyncContactEnrichmentResponse200OutputProfile):
            done (bool): Whether the enrichment is completed or not.
     """

    profile: 'SyncContactEnrichmentResponse200OutputProfile'
    done: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_contact_enrichment_response_200_output_profile import SyncContactEnrichmentResponse200OutputProfile
        profile = self.profile.to_dict()

        done = self.done


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "profile": profile,
            "done": done,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_contact_enrichment_response_200_output_profile import SyncContactEnrichmentResponse200OutputProfile
        d = dict(src_dict)
        profile = SyncContactEnrichmentResponse200OutputProfile.from_dict(d.pop("profile"))




        done = d.pop("done")

        sync_contact_enrichment_response_200_output = cls(
            profile=profile,
            done=done,
        )


        sync_contact_enrichment_response_200_output.additional_properties = d
        return sync_contact_enrichment_response_200_output

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
