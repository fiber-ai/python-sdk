from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LookalikesBulkPollResponse200OutputRedirectedDomainsItem")


@_attrs_define
class LookalikesBulkPollResponse200OutputRedirectedDomainsItem:
    """
    Attributes:
        submitted_input (str): The input exactly as you submitted it (it may be a URL rather than a bare domain), so you
            can match it against your own list.
        matched_domain (str): The domain the company was matched on.
    """

    submitted_input: str
    matched_domain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submitted_input = self.submitted_input

        matched_domain = self.matched_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submittedInput": submitted_input,
                "matchedDomain": matched_domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        submitted_input = d.pop("submittedInput")

        matched_domain = d.pop("matchedDomain")

        lookalikes_bulk_poll_response_200_output_redirected_domains_item = cls(
            submitted_input=submitted_input,
            matched_domain=matched_domain,
        )

        lookalikes_bulk_poll_response_200_output_redirected_domains_item.additional_properties = d
        return lookalikes_bulk_poll_response_200_output_redirected_domains_item

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
