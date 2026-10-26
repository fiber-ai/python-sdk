from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookalikesExportCsvResponse200Output")


@_attrs_define
class LookalikesExportCsvResponse200Output:
    """
    Attributes:
        filename (str): Suggested filename for saving the exported file.
        csv (str): The graded target list as CSV text with a header row. Columns: bucket, rank_in_bucket, domain, name,
            similarity_score, opportunity_score, match_confidence, why_this_target.
    """

    filename: str
    csv: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        csv = self.csv

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "csv": csv,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        csv = d.pop("csv")

        lookalikes_export_csv_response_200_output = cls(
            filename=filename,
            csv=csv,
        )

        lookalikes_export_csv_response_200_output.additional_properties = d
        return lookalikes_export_csv_response_200_output

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
