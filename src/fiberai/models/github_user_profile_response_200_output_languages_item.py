from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GithubUserProfileResponse200OutputLanguagesItem")


@_attrs_define
class GithubUserProfileResponse200OutputLanguagesItem:
    """
    Attributes:
        language (str): Programming language name.
        repo_count (float): How many of the user's own repositories use this language.
        share (float): Fraction of the counted repositories that use this language, from 0 to 1.
    """

    language: str
    repo_count: float
    share: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        repo_count = self.repo_count

        share = self.share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "repoCount": repo_count,
                "share": share,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("language")

        repo_count = d.pop("repoCount")

        share = d.pop("share")

        github_user_profile_response_200_output_languages_item = cls(
            language=language,
            repo_count=repo_count,
            share=share,
        )

        github_user_profile_response_200_output_languages_item.additional_properties = d
        return github_user_profile_response_200_output_languages_item

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
