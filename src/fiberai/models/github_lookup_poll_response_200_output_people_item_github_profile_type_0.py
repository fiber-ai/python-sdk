from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_0_outcome import (
    GithubLookupPollResponse200OutputPeopleItemGithubProfileType0Outcome,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubLookupPollResponse200OutputPeopleItemGithubProfileType0")


@_attrs_define
class GithubLookupPollResponse200OutputPeopleItemGithubProfileType0:
    """
    Attributes:
        outcome (GithubLookupPollResponse200OutputPeopleItemGithubProfileType0Outcome):
        username (str): The GitHub username (login) for the matched profile.
        github_url (str): The GitHub profile URL.
        confidence_out_of_10 (int): Confidence score between 1 and 10 denoting the match quality.
        display_name (None | str | Unset): The user's display name on GitHub.
        profile_picture_url (None | str | Unset): URL to the user's GitHub profile picture.
        bio (None | str | Unset): One-line summary below the person's name on GitHub.
        location (None | str | Unset): Location as displayed on the GitHub profile.
        num_repositories (int | None | Unset): Number of public repositories.
        num_followers (int | None | Unset): Number of followers on GitHub.
        rationale (None | str | Unset): Short explanation of why this GitHub profile was matched to the person,
            referencing details like name, company, or location.
    """

    outcome: GithubLookupPollResponse200OutputPeopleItemGithubProfileType0Outcome
    username: str
    github_url: str
    confidence_out_of_10: int
    display_name: None | str | Unset = UNSET
    profile_picture_url: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    num_repositories: int | None | Unset = UNSET
    num_followers: int | None | Unset = UNSET
    rationale: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outcome = self.outcome.value

        username = self.username

        github_url = self.github_url

        confidence_out_of_10 = self.confidence_out_of_10

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        profile_picture_url: None | str | Unset
        if isinstance(self.profile_picture_url, Unset):
            profile_picture_url = UNSET
        else:
            profile_picture_url = self.profile_picture_url

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        num_repositories: int | None | Unset
        if isinstance(self.num_repositories, Unset):
            num_repositories = UNSET
        else:
            num_repositories = self.num_repositories

        num_followers: int | None | Unset
        if isinstance(self.num_followers, Unset):
            num_followers = UNSET
        else:
            num_followers = self.num_followers

        rationale: None | str | Unset
        if isinstance(self.rationale, Unset):
            rationale = UNSET
        else:
            rationale = self.rationale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outcome": outcome,
                "username": username,
                "githubUrl": github_url,
                "confidenceOutOf10": confidence_out_of_10,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if profile_picture_url is not UNSET:
            field_dict["profilePictureUrl"] = profile_picture_url
        if bio is not UNSET:
            field_dict["bio"] = bio
        if location is not UNSET:
            field_dict["location"] = location
        if num_repositories is not UNSET:
            field_dict["numRepositories"] = num_repositories
        if num_followers is not UNSET:
            field_dict["numFollowers"] = num_followers
        if rationale is not UNSET:
            field_dict["rationale"] = rationale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        outcome = GithubLookupPollResponse200OutputPeopleItemGithubProfileType0Outcome(d.pop("outcome"))

        username = d.pop("username")

        github_url = d.pop("githubUrl")

        confidence_out_of_10 = d.pop("confidenceOutOf10")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profilePictureUrl", UNSET))

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_num_repositories(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_repositories = _parse_num_repositories(d.pop("numRepositories", UNSET))

        def _parse_num_followers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_followers = _parse_num_followers(d.pop("numFollowers", UNSET))

        def _parse_rationale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rationale = _parse_rationale(d.pop("rationale", UNSET))

        github_lookup_poll_response_200_output_people_item_github_profile_type_0 = cls(
            outcome=outcome,
            username=username,
            github_url=github_url,
            confidence_out_of_10=confidence_out_of_10,
            display_name=display_name,
            profile_picture_url=profile_picture_url,
            bio=bio,
            location=location,
            num_repositories=num_repositories,
            num_followers=num_followers,
            rationale=rationale,
        )

        github_lookup_poll_response_200_output_people_item_github_profile_type_0.additional_properties = d
        return github_lookup_poll_response_200_output_people_item_github_profile_type_0

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
