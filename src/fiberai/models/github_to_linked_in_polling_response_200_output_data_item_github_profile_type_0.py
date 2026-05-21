from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0")


@_attrs_define
class GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0:
    """
    Attributes:
        name (None | str | Unset):
        company (None | str | Unset):
        location (None | str | Unset):
        bio (None | str | Unset):
        blog (None | str | Unset):
        avatar_url (None | str | Unset):
        followers (int | None | Unset):
        public_repos (int | None | Unset):
    """

    name: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    blog: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    followers: int | None | Unset = UNSET
    public_repos: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        blog: None | str | Unset
        if isinstance(self.blog, Unset):
            blog = UNSET
        else:
            blog = self.blog

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        followers: int | None | Unset
        if isinstance(self.followers, Unset):
            followers = UNSET
        else:
            followers = self.followers

        public_repos: int | None | Unset
        if isinstance(self.public_repos, Unset):
            public_repos = UNSET
        else:
            public_repos = self.public_repos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if company is not UNSET:
            field_dict["company"] = company
        if location is not UNSET:
            field_dict["location"] = location
        if bio is not UNSET:
            field_dict["bio"] = bio
        if blog is not UNSET:
            field_dict["blog"] = blog
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if followers is not UNSET:
            field_dict["followers"] = followers
        if public_repos is not UNSET:
            field_dict["publicRepos"] = public_repos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_blog(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blog = _parse_blog(d.pop("blog", UNSET))

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl", UNSET))

        def _parse_followers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        followers = _parse_followers(d.pop("followers", UNSET))

        def _parse_public_repos(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        public_repos = _parse_public_repos(d.pop("publicRepos", UNSET))

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
