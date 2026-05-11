from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_to_linkedin_single_body_output_type import GithubToLinkedinSingleBodyOutputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubToLinkedinSingleBody")


@_attrs_define
class GithubToLinkedinSingleBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        github_username (str): The GitHub username to look up.
        output_type (GithubToLinkedinSingleBodyOutputType | Unset): What to extract from GitHub profile. 'linkedin'
            finds LinkedIn profile, 'email' extracts work emails from commits, 'both' returns both. Default:
            GithubToLinkedinSingleBodyOutputType.BOTH.
        customer_provided_id (None | str | Unset): Optional customer-provided ID to tie results back to original input.
        include_debug_timings (bool | Unset): When true, include resolver timing details in the response for
            diagnostics. Default: False.
    """

    api_key: str
    github_username: str
    output_type: GithubToLinkedinSingleBodyOutputType | Unset = GithubToLinkedinSingleBodyOutputType.BOTH
    customer_provided_id: None | str | Unset = UNSET
    include_debug_timings: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        github_username = self.github_username

        output_type: str | Unset = UNSET
        if not isinstance(self.output_type, Unset):
            output_type = self.output_type.value

        customer_provided_id: None | str | Unset
        if isinstance(self.customer_provided_id, Unset):
            customer_provided_id = UNSET
        else:
            customer_provided_id = self.customer_provided_id

        include_debug_timings = self.include_debug_timings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "githubUsername": github_username,
            }
        )
        if output_type is not UNSET:
            field_dict["outputType"] = output_type
        if customer_provided_id is not UNSET:
            field_dict["customerProvidedId"] = customer_provided_id
        if include_debug_timings is not UNSET:
            field_dict["includeDebugTimings"] = include_debug_timings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        github_username = d.pop("githubUsername")

        _output_type = d.pop("outputType", UNSET)
        output_type: GithubToLinkedinSingleBodyOutputType | Unset
        if isinstance(_output_type, Unset):
            output_type = UNSET
        else:
            output_type = GithubToLinkedinSingleBodyOutputType(_output_type)

        def _parse_customer_provided_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId", UNSET))

        include_debug_timings = d.pop("includeDebugTimings", UNSET)

        github_to_linkedin_single_body = cls(
            api_key=api_key,
            github_username=github_username,
            output_type=output_type,
            customer_provided_id=customer_provided_id,
            include_debug_timings=include_debug_timings,
        )

        github_to_linkedin_single_body.additional_properties = d
        return github_to_linkedin_single_body

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
