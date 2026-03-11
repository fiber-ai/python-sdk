from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StartLocalBusinessSearchResponse200Output")


@_attrs_define
class StartLocalBusinessSearchResponse200Output:
    """
    Attributes:
        research_run_id (str): Run ID for the local business agent run. Use this ID to poll the result of the run.
    """

    research_run_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        research_run_id = self.research_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "researchRunId": research_run_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        research_run_id = d.pop("researchRunId")

        start_local_business_search_response_200_output = cls(
            research_run_id=research_run_id,
        )

        start_local_business_search_response_200_output.additional_properties = d
        return start_local_business_search_response_200_output

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
