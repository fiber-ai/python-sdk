from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KitchenSinkBulkProfileResponse200OutputDataItemItemCertificationsType0Item")


@_attrs_define
class KitchenSinkBulkProfileResponse200OutputDataItemItemCertificationsType0Item:
    """
    Attributes:
        title (None | str | Unset):
        credential_id (None | str | Unset):
        verify_url (None | str | Unset):
        summary (None | str | Unset):
        linkedin_company_id (None | str | Unset):
        company_name (None | str | Unset):
        date (None | str | Unset):
    """

    title: None | str | Unset = UNSET
    credential_id: None | str | Unset = UNSET
    verify_url: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    linkedin_company_id: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        credential_id: None | str | Unset
        if isinstance(self.credential_id, Unset):
            credential_id = UNSET
        else:
            credential_id = self.credential_id

        verify_url: None | str | Unset
        if isinstance(self.verify_url, Unset):
            verify_url = UNSET
        else:
            verify_url = self.verify_url

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        linkedin_company_id: None | str | Unset
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if credential_id is not UNSET:
            field_dict["credential_id"] = credential_id
        if verify_url is not UNSET:
            field_dict["verify_url"] = verify_url
        if summary is not UNSET:
            field_dict["summary"] = summary
        if linkedin_company_id is not UNSET:
            field_dict["linkedin_company_id"] = linkedin_company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_credential_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credential_id = _parse_credential_id(d.pop("credential_id", UNSET))

        def _parse_verify_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verify_url = _parse_verify_url(d.pop("verify_url", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_linkedin_company_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedin_company_id", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        kitchen_sink_bulk_profile_response_200_output_data_item_item_certifications_type_0_item = cls(
            title=title,
            credential_id=credential_id,
            verify_url=verify_url,
            summary=summary,
            linkedin_company_id=linkedin_company_id,
            company_name=company_name,
            date=date,
        )

        kitchen_sink_bulk_profile_response_200_output_data_item_item_certifications_type_0_item.additional_properties = d
        return kitchen_sink_bulk_profile_response_200_output_data_item_item_certifications_type_0_item

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
