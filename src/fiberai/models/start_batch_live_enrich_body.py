from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_batch_live_enrich_body_type import StartBatchLiveEnrichBodyType

T = TypeVar("T", bound="StartBatchLiveEnrichBody")


@_attrs_define
class StartBatchLiveEnrichBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        type_ (StartBatchLiveEnrichBodyType): Whether to enrich people or companies
        identifiers (list[str]): List of LinkedIn identifiers. For profiles: LinkedIn URL (e.g.
            'https://www.linkedin.com/in/williamhgates'), profile slug (e.g. 'williamhgates'), or Sales Navigator URN (e.g.
            'ACwAAAjNR6wBsr_od4UG9Y-HRxg21mwhv5xO0FE') or numeric user ID (e.g. '4532776'). For companies: LinkedIn URL
            (e.g. 'https://www.linkedin.com/company/microsoft'), company slug (e.g. 'microsoft'), or numeric org ID (e.g.
            '1035').
    """

    api_key: str
    type_: StartBatchLiveEnrichBodyType
    identifiers: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        type_ = self.type_.value

        identifiers = self.identifiers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "type": type_,
                "identifiers": identifiers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        type_ = StartBatchLiveEnrichBodyType(d.pop("type"))

        identifiers = cast(list[str], d.pop("identifiers"))

        start_batch_live_enrich_body = cls(
            api_key=api_key,
            type_=type_,
            identifiers=identifiers,
        )

        start_batch_live_enrich_body.additional_properties = d
        return start_batch_live_enrich_body

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
