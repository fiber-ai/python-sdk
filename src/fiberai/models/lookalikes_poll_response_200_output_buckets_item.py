from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookalikes_poll_response_200_output_buckets_item_findings_item import (
        LookalikesPollResponse200OutputBucketsItemFindingsItem,
    )


T = TypeVar("T", bound="LookalikesPollResponse200OutputBucketsItem")


@_attrs_define
class LookalikesPollResponse200OutputBucketsItem:
    """
    Attributes:
        name (str): Short name of this company grouping.
        member_company_names (list[str]): Names of your input companies that define this grouping.
        findings (list[LookalikesPollResponse200OutputBucketsItemFindingsItem]): Graded lookalike companies for this
            grouping, best first.
        description (None | str | Unset): What the companies in this grouping have in common. Omitted when the
            grouping's name says it all.
    """

    name: str
    member_company_names: list[str]
    findings: list[LookalikesPollResponse200OutputBucketsItemFindingsItem]
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        member_company_names = self.member_company_names

        findings = []
        for findings_item_data in self.findings:
            findings_item = findings_item_data.to_dict()
            findings.append(findings_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "memberCompanyNames": member_company_names,
                "findings": findings,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookalikes_poll_response_200_output_buckets_item_findings_item import (
            LookalikesPollResponse200OutputBucketsItemFindingsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        member_company_names = cast(list[str], d.pop("memberCompanyNames"))

        findings = []
        _findings = d.pop("findings")
        for findings_item_data in _findings:
            findings_item = LookalikesPollResponse200OutputBucketsItemFindingsItem.from_dict(findings_item_data)

            findings.append(findings_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        lookalikes_poll_response_200_output_buckets_item = cls(
            name=name,
            member_company_names=member_company_names,
            findings=findings,
            description=description,
        )

        lookalikes_poll_response_200_output_buckets_item.additional_properties = d
        return lookalikes_poll_response_200_output_buckets_item

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
