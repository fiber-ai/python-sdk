from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_user_profile_response_200_output_languages_item import (
        GithubUserProfileResponse200OutputLanguagesItem,
    )


T = TypeVar("T", bound="GithubUserProfileResponse200Output")


@_attrs_define
class GithubUserProfileResponse200Output:
    """
    Attributes:
        username (str): GitHub username.
        profile_url (str): Profile URL.
        languages (list[GithubUserProfileResponse200OutputLanguagesItem]): Languages across the user's own non-fork
            repositories, using the 100 most recently pushed. Repositories with no detected language are excluded. Ordered
            by `repoCount`, highest first.
        languages_unavailable (bool): True when the language breakdown could not be loaded. The profile fields are still
            returned.
        name (None | str | Unset): Name on the profile.
        company (None | str | Unset): Company on the profile.
        location (None | str | Unset): Location on the profile.
        bio (None | str | Unset): Profile bio.
        website (None | str | Unset): Website linked from the profile.
        twitter_url (None | str | Unset): X profile URL linked from the GitHub profile.
        num_followers (float | None | Unset): Number of followers.
        num_repositories (float | None | Unset): Number of public repositories.
        account_created_at (None | str | Unset): When the account was created, as an ISO-8601 timestamp.
    """

    username: str
    profile_url: str
    languages: list[GithubUserProfileResponse200OutputLanguagesItem]
    languages_unavailable: bool
    name: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    twitter_url: None | str | Unset = UNSET
    num_followers: float | None | Unset = UNSET
    num_repositories: float | None | Unset = UNSET
    account_created_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        profile_url = self.profile_url

        languages = []
        for languages_item_data in self.languages:
            languages_item = languages_item_data.to_dict()
            languages.append(languages_item)

        languages_unavailable = self.languages_unavailable

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

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        twitter_url: None | str | Unset
        if isinstance(self.twitter_url, Unset):
            twitter_url = UNSET
        else:
            twitter_url = self.twitter_url

        num_followers: float | None | Unset
        if isinstance(self.num_followers, Unset):
            num_followers = UNSET
        else:
            num_followers = self.num_followers

        num_repositories: float | None | Unset
        if isinstance(self.num_repositories, Unset):
            num_repositories = UNSET
        else:
            num_repositories = self.num_repositories

        account_created_at: None | str | Unset
        if isinstance(self.account_created_at, Unset):
            account_created_at = UNSET
        else:
            account_created_at = self.account_created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "profileUrl": profile_url,
                "languages": languages,
                "languagesUnavailable": languages_unavailable,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if company is not UNSET:
            field_dict["company"] = company
        if location is not UNSET:
            field_dict["location"] = location
        if bio is not UNSET:
            field_dict["bio"] = bio
        if website is not UNSET:
            field_dict["website"] = website
        if twitter_url is not UNSET:
            field_dict["twitterUrl"] = twitter_url
        if num_followers is not UNSET:
            field_dict["numFollowers"] = num_followers
        if num_repositories is not UNSET:
            field_dict["numRepositories"] = num_repositories
        if account_created_at is not UNSET:
            field_dict["accountCreatedAt"] = account_created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_user_profile_response_200_output_languages_item import (
            GithubUserProfileResponse200OutputLanguagesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        username = d.pop("username")

        profile_url = d.pop("profileUrl")

        languages = []
        _languages = d.pop("languages")
        for languages_item_data in _languages:
            languages_item = GithubUserProfileResponse200OutputLanguagesItem.from_dict(languages_item_data)

            languages.append(languages_item)

        languages_unavailable = d.pop("languagesUnavailable")

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

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_twitter_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter_url = _parse_twitter_url(d.pop("twitterUrl", UNSET))

        def _parse_num_followers(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_followers = _parse_num_followers(d.pop("numFollowers", UNSET))

        def _parse_num_repositories(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_repositories = _parse_num_repositories(d.pop("numRepositories", UNSET))

        def _parse_account_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_created_at = _parse_account_created_at(d.pop("accountCreatedAt", UNSET))

        github_user_profile_response_200_output = cls(
            username=username,
            profile_url=profile_url,
            languages=languages,
            languages_unavailable=languages_unavailable,
            name=name,
            company=company,
            location=location,
            bio=bio,
            website=website,
            twitter_url=twitter_url,
            num_followers=num_followers,
            num_repositories=num_repositories,
            account_created_at=account_created_at,
        )

        github_user_profile_response_200_output.additional_properties = d
        return github_user_profile_response_200_output

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
