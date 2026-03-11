from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_inputs import (
        PollBatchContactEnrichmentResponse200OutputPageResultsItemInputs,
    )
    from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0 import (
        PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0,
    )


T = TypeVar("T", bound="PollBatchContactEnrichmentResponse200OutputPageResultsItem")


@_attrs_define
class PollBatchContactEnrichmentResponse200OutputPageResultsItem:
    """
    Attributes:
        inputs (PollBatchContactEnrichmentResponse200OutputPageResultsItemInputs): The input details provided for this
            person
        outputs (None | PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0 | Unset): The reveal
            result for this person
    """

    inputs: PollBatchContactEnrichmentResponse200OutputPageResultsItemInputs
    outputs: None | PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0 import (
            PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0,
        )

        inputs = self.inputs.to_dict()

        outputs: dict[str, Any] | None | Unset
        if isinstance(self.outputs, Unset):
            outputs = UNSET
        elif isinstance(self.outputs, PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0):
            outputs = self.outputs.to_dict()
        else:
            outputs = self.outputs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputs": inputs,
            }
        )
        if outputs is not UNSET:
            field_dict["outputs"] = outputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_inputs import (
            PollBatchContactEnrichmentResponse200OutputPageResultsItemInputs,
        )
        from ..models.poll_batch_contact_enrichment_response_200_output_page_results_item_outputs_type_0 import (
            PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0,
        )

        d = dict(src_dict)
        inputs = PollBatchContactEnrichmentResponse200OutputPageResultsItemInputs.from_dict(d.pop("inputs"))

        def _parse_outputs(
            data: object,
        ) -> None | PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outputs_type_0 = PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0.from_dict(data)

                return outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0 | Unset, data)

        outputs = _parse_outputs(d.pop("outputs", UNSET))

        poll_batch_contact_enrichment_response_200_output_page_results_item = cls(
            inputs=inputs,
            outputs=outputs,
        )

        poll_batch_contact_enrichment_response_200_output_page_results_item.additional_properties = d
        return poll_batch_contact_enrichment_response_200_output_page_results_item

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
