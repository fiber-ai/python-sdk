from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0")


@_attrs_define
class GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0:
    """
    Attributes:
        name (None | str):
        company (None | str):
        location (None | str):
        bio (None | str):
        blog (None | str):
        avatar_url (None | str):
        followers (int | None):
        public_repos (int | None):
    """

    name: None | str
    company: None | str
    location: None | str
    bio: None | str
    blog: None | str
    avatar_url: None | str
    followers: int | None
    public_repos: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        company: None | str
        company = self.company

        location: None | str
        location = self.location

        bio: None | str
        bio = self.bio

        blog: None | str
        blog = self.blog

        avatar_url: None | str
        avatar_url = self.avatar_url

        followers: int | None
        followers = self.followers

        public_repos: int | None
        public_repos = self.public_repos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "company": company,
                "location": location,
                "bio": bio,
                "blog": blog,
                "avatarUrl": avatar_url,
                "followers": followers,
                "publicRepos": public_repos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_company(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company = _parse_company(d.pop("company"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_bio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio = _parse_bio(d.pop("bio"))

        def _parse_blog(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        blog = _parse_blog(d.pop("blog"))

        def _parse_avatar_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl"))

        def _parse_followers(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        followers = _parse_followers(d.pop("followers"))

        def _parse_public_repos(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        public_repos = _parse_public_repos(d.pop("publicRepos"))

        github_to_linked_in_polling_response_200_output_data_item_github_profile_type_0 = cls(
            name=name,
            company=company,
            location=location,
            bio=bio,
            blog=blog,
            avatar_url=avatar_url,
            followers=followers,
            public_repos=public_repos,
        )

        github_to_linked_in_polling_response_200_output_data_item_github_profile_type_0.additional_properties = d
        return github_to_linked_in_polling_response_200_output_data_item_github_profile_type_0

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
