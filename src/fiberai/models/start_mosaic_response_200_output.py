from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StartMosaicResponse200Output")


@_attrs_define
class StartMosaicResponse200Output:
    """
    Attributes:
        run_id (str): Unique Mosaic run ID. Poll /mosaic/poll with this ID to check status and retrieve results.
        is_free_trial_run (bool): True when this run used the organization's one-time free Mosaic trial. The first 1,000
            processed rows are free; rows beyond that are billed against normal credits.
    """

    run_id: str
    is_free_trial_run: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        is_free_trial_run = self.is_free_trial_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "isFreeTrialRun": is_free_trial_run,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        is_free_trial_run = d.pop("isFreeTrialRun")

        start_mosaic_response_200_output = cls(
            run_id=run_id,
            is_free_trial_run=is_free_trial_run,
        )

        start_mosaic_response_200_output.additional_properties = d
        return start_mosaic_response_200_output

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
