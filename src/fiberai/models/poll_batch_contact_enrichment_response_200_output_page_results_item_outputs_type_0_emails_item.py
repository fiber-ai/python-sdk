from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_emails_item_status import PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemStatus
from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_emails_item_type import PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemType
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItem")



@_attrs_define
class PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItem:
    """ 
        Attributes:
            email (str):
            type_ (PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemType):
            status (Union[Unset, PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemStatus]):
     """

    email: str
    type_: PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemType
    status: Union[Unset, PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        type_ = self.type_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "email": email,
            "type": type_,
        })
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        type_ = PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemType(d.pop("type"))




        _status = d.pop("status", UNSET)
        status: Union[Unset, PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemStatus(_status)




        poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_emails_item = cls(
            email=email,
            type_=type_,
            status=status,
        )


        poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_emails_item.additional_properties = d
        return poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_emails_item

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
