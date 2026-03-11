from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.poll_local_business_search_response_200_output_data_observations_item import (
        PollLocalBusinessSearchResponse200OutputDataObservationsItem,
    )


T = TypeVar("T", bound="PollLocalBusinessSearchResponse200OutputData")


@_attrs_define
class PollLocalBusinessSearchResponse200OutputData:
    """The Local business agent search result

    Attributes:
        observations (list[PollLocalBusinessSearchResponse200OutputDataObservationsItem]):
    """

    observations: list[PollLocalBusinessSearchResponse200OutputDataObservationsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observations = []
        for observations_item_data in self.observations:
            observations_item = observations_item_data.to_dict()
            observations.append(observations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "observations": observations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_local_business_search_response_200_output_data_observations_item import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItem,
        )

        d = dict(src_dict)
        observations = []
        _observations = d.pop("observations")
        for observations_item_data in _observations:
            observations_item = PollLocalBusinessSearchResponse200OutputDataObservationsItem.from_dict(
                observations_item_data
            )

            observations.append(observations_item)

        poll_local_business_search_response_200_output_data = cls(
            observations=observations,
        )

        poll_local_business_search_response_200_output_data.additional_properties = d
        return poll_local_business_search_response_200_output_data

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
