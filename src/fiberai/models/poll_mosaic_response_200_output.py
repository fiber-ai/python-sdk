from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.poll_mosaic_response_200_output_run import PollMosaicResponse200OutputRun


T = TypeVar("T", bound="PollMosaicResponse200Output")


@_attrs_define
class PollMosaicResponse200Output:
    """
    Attributes:
        run (PollMosaicResponse200OutputRun): Current Mosaic run state. When status is done, outputCsvUrl and reportUrl
            are temporary download links.
    """

    run: PollMosaicResponse200OutputRun
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run = self.run.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run": run,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_mosaic_response_200_output_run import PollMosaicResponse200OutputRun  # noqa: PLC0415

        d = dict(src_dict)
        run = PollMosaicResponse200OutputRun.from_dict(d.pop("run"))

        poll_mosaic_response_200_output = cls(
            run=run,
        )

        poll_mosaic_response_200_output.additional_properties = d
        return poll_mosaic_response_200_output

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
