from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_prospects_body_exclude_fields_item import ExportProspectsBodyExcludeFieldsItem
from ..models.export_prospects_body_format import ExportProspectsBodyFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportProspectsBody")


@_attrs_define
class ExportProspectsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        format_ (ExportProspectsBodyFormat): Format of the exported CSV
        max_rows_to_export (int | None | Unset): Maximum number of rows to export. Defaults to remaining export quota.
        exclude_fields (list[ExportProspectsBodyExcludeFieldsItem] | Unset): Fields to exclude from the export
        only_with_contacts (bool | Unset): If true, only export prospects with verified emails or phones Default: False.
        user_email (None | str | Unset): Optional email address to receive CSV export links. If not provided, no email
            will be sent.
    """

    api_key: str
    format_: ExportProspectsBodyFormat
    max_rows_to_export: int | None | Unset = UNSET
    exclude_fields: list[ExportProspectsBodyExcludeFieldsItem] | Unset = UNSET
    only_with_contacts: bool | Unset = False
    user_email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        format_ = self.format_.value

        max_rows_to_export: int | None | Unset
        if isinstance(self.max_rows_to_export, Unset):
            max_rows_to_export = UNSET
        else:
            max_rows_to_export = self.max_rows_to_export

        exclude_fields: list[str] | Unset = UNSET
        if not isinstance(self.exclude_fields, Unset):
            exclude_fields = []
            for exclude_fields_item_data in self.exclude_fields:
                exclude_fields_item = exclude_fields_item_data.value
                exclude_fields.append(exclude_fields_item)

        only_with_contacts = self.only_with_contacts

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "format": format_,
            }
        )
        if max_rows_to_export is not UNSET:
            field_dict["maxRowsToExport"] = max_rows_to_export
        if exclude_fields is not UNSET:
            field_dict["excludeFields"] = exclude_fields
        if only_with_contacts is not UNSET:
            field_dict["onlyWithContacts"] = only_with_contacts
        if user_email is not UNSET:
            field_dict["userEmail"] = user_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        format_ = ExportProspectsBodyFormat(d.pop("format"))

        def _parse_max_rows_to_export(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_rows_to_export = _parse_max_rows_to_export(d.pop("maxRowsToExport", UNSET))

        _exclude_fields = d.pop("excludeFields", UNSET)
        exclude_fields: list[ExportProspectsBodyExcludeFieldsItem] | Unset = UNSET
        if _exclude_fields is not UNSET:
            exclude_fields = []
            for exclude_fields_item_data in _exclude_fields:
                exclude_fields_item = ExportProspectsBodyExcludeFieldsItem(exclude_fields_item_data)

                exclude_fields.append(exclude_fields_item)

        only_with_contacts = d.pop("onlyWithContacts", UNSET)

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("userEmail", UNSET))

        export_prospects_body = cls(
            api_key=api_key,
            format_=format_,
            max_rows_to_export=max_rows_to_export,
            exclude_fields=exclude_fields,
            only_with_contacts=only_with_contacts,
            user_email=user_email,
        )

        export_prospects_body.additional_properties = d
        return export_prospects_body

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
