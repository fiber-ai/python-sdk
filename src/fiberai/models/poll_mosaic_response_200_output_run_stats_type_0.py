from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollMosaicResponse200OutputRunStatsType0")


@_attrs_define
class PollMosaicResponse200OutputRunStatsType0:
    """
    Attributes:
        input_rows (int):
        output_rows (int):
        rows_where_profile_found (int):
        rows_with_contact_details (int):
        rows_with_errors (int):
    """

    input_rows: int
    output_rows: int
    rows_where_profile_found: int
    rows_with_contact_details: int
    rows_with_errors: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_rows = self.input_rows

        output_rows = self.output_rows

        rows_where_profile_found = self.rows_where_profile_found

        rows_with_contact_details = self.rows_with_contact_details

        rows_with_errors = self.rows_with_errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputRows": input_rows,
                "outputRows": output_rows,
                "rowsWhereProfileFound": rows_where_profile_found,
                "rowsWithContactDetails": rows_with_contact_details,
                "rowsWithErrors": rows_with_errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_rows = d.pop("inputRows")

        output_rows = d.pop("outputRows")

        rows_where_profile_found = d.pop("rowsWhereProfileFound")

        rows_with_contact_details = d.pop("rowsWithContactDetails")

        rows_with_errors = d.pop("rowsWithErrors")

        poll_mosaic_response_200_output_run_stats_type_0 = cls(
            input_rows=input_rows,
            output_rows=output_rows,
            rows_where_profile_found=rows_where_profile_found,
            rows_with_contact_details=rows_with_contact_details,
            rows_with_errors=rows_with_errors,
        )

        poll_mosaic_response_200_output_run_stats_type_0.additional_properties = d
        return poll_mosaic_response_200_output_run_stats_type_0

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
