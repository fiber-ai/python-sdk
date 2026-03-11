from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExportCompaniesResponse200Output")


@_attrs_define
class ExportCompaniesResponse200Output:
    """
    Attributes:
        message (str): Human-readable message about the export status
        estimated_rows (float): Estimated number of rows that will be exported
        max_rows_allowed (float): Maximum rows allowed based on export quota
    """

    message: str
    estimated_rows: float
    max_rows_allowed: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        estimated_rows = self.estimated_rows

        max_rows_allowed = self.max_rows_allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "estimatedRows": estimated_rows,
                "maxRowsAllowed": max_rows_allowed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        estimated_rows = d.pop("estimatedRows")

        max_rows_allowed = d.pop("maxRowsAllowed")

        export_companies_response_200_output = cls(
            message=message,
            estimated_rows=estimated_rows,
            max_rows_allowed=max_rows_allowed,
        )

        export_companies_response_200_output.additional_properties = d
        return export_companies_response_200_output

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
