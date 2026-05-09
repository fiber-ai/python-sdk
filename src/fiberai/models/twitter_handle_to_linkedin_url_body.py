from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TwitterHandleToLinkedinUrlBody")


@_attrs_define
class TwitterHandleToLinkedinUrlBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        handle (str): Twitter/X handle to look up. Accepts a bare handle with or without a leading '@' (e.g. 'elonmusk',
            '@elonmusk'), or a full X/Twitter profile URL (e.g. 'https://x.com/elonmusk', 'twitter.com/@elonmusk').
        context (None | str | Unset): Optional hint about the person, used to disambiguate common-name handles (e.g. "VC
            at a16z" or "YC W23 founder"). Improves accuracy on ambiguous handles. Max 1000 characters.
    """

    api_key: str
    handle: str
    context: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        handle = self.handle

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "handle": handle,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        handle = d.pop("handle")

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        twitter_handle_to_linkedin_url_body = cls(
            api_key=api_key,
            handle=handle,
            context=context,
        )

        twitter_handle_to_linkedin_url_body.additional_properties = d
        return twitter_handle_to_linkedin_url_body

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
