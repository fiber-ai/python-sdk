from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CertificationChange")


@_attrs_define
class CertificationChange:
    """
    Attributes:
        title (str): Certification title
        company (None | str): Issuing organization
        credential_id (None | str): Credential ID
        issue_date (None | str): ISO issue date
    """

    title: str
    company: None | str
    credential_id: None | str
    issue_date: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        company: None | str
        company = self.company

        credential_id: None | str
        credential_id = self.credential_id

        issue_date: None | str
        issue_date = self.issue_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "company": company,
                "credentialId": credential_id,
                "issueDate": issue_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        def _parse_company(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company = _parse_company(d.pop("company"))

        def _parse_credential_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        credential_id = _parse_credential_id(d.pop("credentialId"))

        def _parse_issue_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issue_date = _parse_issue_date(d.pop("issueDate"))

        certification_change = cls(
            title=title,
            company=company,
            credential_id=credential_id,
            issue_date=issue_date,
        )

        certification_change.additional_properties = d
        return certification_change

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
