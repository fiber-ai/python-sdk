from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_media_lookup_batch_polling_response_200_output_results_item_outcome_type_1 import (
    SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType1,
)
from ..models.social_media_lookup_batch_polling_response_200_output_results_item_outcome_type_2_type_1 import (
    SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType2Type1,
)
from ..models.social_media_lookup_batch_polling_response_200_output_results_item_outcome_type_3_type_1 import (
    SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_media_lookup_batch_polling_response_200_output_results_item_candidates_item import (
        SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItem,
    )


T = TypeVar("T", bound="SocialMediaLookupBatchPollingResponse200OutputResultsItem")


@_attrs_define
class SocialMediaLookupBatchPollingResponse200OutputResultsItem:
    """
    Attributes:
        full_name (str): The full name of the person this result corresponds to.
        candidates (list[SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItem]): The best-match
            profiles found, one per platform. Empty if no confident matches were found.
        customer_provided_id (None | str | Unset): The external ID echoed back from the input for joining results to
            your original dataset.
        outcome (None | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType1 |
            SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType2Type1 |
            SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType3Type1 | Unset): Overall outcome:
            FOUND_CANDIDATES if at least one profile was found, NO_CANDIDATES_FOUND if the search returned nothing,
            INSUFFICIENT_INFORMATION if there was not enough input to search.
        error_message (None | str | Unset): Error message if the lookup failed for this person. Null on success.
    """

    full_name: str
    candidates: list[SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItem]
    customer_provided_id: None | str | Unset = UNSET
    outcome: (
        None
        | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType1
        | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType2Type1
        | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType3Type1
        | Unset
    ) = UNSET
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

        candidates = []
        for candidates_item_data in self.candidates:
            candidates_item = candidates_item_data.to_dict()
            candidates.append(candidates_item)

        customer_provided_id: None | str | Unset
        if isinstance(self.customer_provided_id, Unset):
            customer_provided_id = UNSET
        else:
            customer_provided_id = self.customer_provided_id

        outcome: None | str | Unset
        if isinstance(self.outcome, Unset):
            outcome = UNSET
        elif isinstance(self.outcome, SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType1):
            outcome = self.outcome.value
        elif isinstance(self.outcome, SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType2Type1):
            outcome = self.outcome.value
        elif isinstance(self.outcome, SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType3Type1):
            outcome = self.outcome.value
        else:
            outcome = self.outcome

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fullName": full_name,
                "candidates": candidates,
            }
        )
        if customer_provided_id is not UNSET:
            field_dict["customerProvidedId"] = customer_provided_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_media_lookup_batch_polling_response_200_output_results_item_candidates_item import (
            SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItem,
        )

        d = dict(src_dict)
        full_name = d.pop("fullName")

        candidates = []
        _candidates = d.pop("candidates")
        for candidates_item_data in _candidates:
            candidates_item = SocialMediaLookupBatchPollingResponse200OutputResultsItemCandidatesItem.from_dict(
                candidates_item_data
            )

            candidates.append(candidates_item)

        def _parse_customer_provided_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId", UNSET))

        def _parse_outcome(
            data: object,
        ) -> (
            None
            | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType1
            | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType2Type1
            | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_1 = SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType1(data)

                return outcome_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_2_type_1 = SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType2Type1(data)

                return outcome_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_3_type_1 = SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType3Type1(data)

                return outcome_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType1
                | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType2Type1
                | SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType3Type1
                | Unset,
                data,
            )

        outcome = _parse_outcome(d.pop("outcome", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        social_media_lookup_batch_polling_response_200_output_results_item = cls(
            full_name=full_name,
            candidates=candidates,
            customer_provided_id=customer_provided_id,
            outcome=outcome,
            error_message=error_message,
        )

        social_media_lookup_batch_polling_response_200_output_results_item.additional_properties = d
        return social_media_lookup_batch_polling_response_200_output_results_item

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
