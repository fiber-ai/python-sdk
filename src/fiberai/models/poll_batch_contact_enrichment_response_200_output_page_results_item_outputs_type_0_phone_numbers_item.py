from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_phone_numbers_item_type import PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItemType






T = TypeVar("T", bound="PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItem")



@_attrs_define
class PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItem:
    """ 
        Attributes:
            number (str):
            type_ (PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItemType):
     """

    number: str
    type_: PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItemType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        number = self.number

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "number": number,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")

        type_ = PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItemType(d.pop("type"))




        poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_phone_numbers_item = cls(
            number=number,
            type_=type_,
        )


        poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_phone_numbers_item.additional_properties = d
        return poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0_phone_numbers_item

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
