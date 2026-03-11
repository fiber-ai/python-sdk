from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_lookup_polling_response_200_output_data_item_outcome_type_1 import (
    GithubLookupPollingResponse200OutputDataItemOutcomeType1,
)
from ..models.github_lookup_polling_response_200_output_data_item_outcome_type_2_type_1 import (
    GithubLookupPollingResponse200OutputDataItemOutcomeType2Type1,
)
from ..models.github_lookup_polling_response_200_output_data_item_outcome_type_3_type_1 import (
    GithubLookupPollingResponse200OutputDataItemOutcomeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubLookupPollingResponse200OutputDataItem")


@_attrs_define
class GithubLookupPollingResponse200OutputDataItem:
    """
    Attributes:
        full_name (str): The full name of the person this result corresponds to. This generally matches the input full
            name.
        confidence_out_of_10 (int): Confidence score between 1 and 10 denoting the match quality. Higher scores mean a
            stronger match.
        github_url (None | str | Unset): The GitHub profile URL that best matches this person. Null if we could not
            confidently find a profile.
        username (None | str | Unset): The GitHub username (login) for the matched profile. Null when no confident match
            was found.
        display_name (None | str | Unset): The user's display name on GitHub.
        profile_picture_url (None | str | Unset): URL to the user's GitHub profile picture.
        bio (None | str | Unset): One-line summary below the person's name on GitHub.
        location (None | str | Unset): Location as displayed on the GitHub profile.
        num_repositories (int | None | Unset): Number of public repositories.
        num_followers (int | None | Unset): Number of followers on GitHub.
        rationale (None | str | Unset): The reasoning for why the agent chose (or did not choose) the given GitHub
            profile.
        error_message (None | str | Unset): Error message if the lookup failed for this person.
        customer_provided_id (None | str | Unset): The customerProvidedId echoed back from the input so you can easily
            join results to your original dataset.
        outcome (GithubLookupPollingResponse200OutputDataItemOutcomeType1 |
            GithubLookupPollingResponse200OutputDataItemOutcomeType2Type1 |
            GithubLookupPollingResponse200OutputDataItemOutcomeType3Type1 | None | Unset):
    """

    full_name: str
    confidence_out_of_10: int
    github_url: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    profile_picture_url: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    num_repositories: int | None | Unset = UNSET
    num_followers: int | None | Unset = UNSET
    rationale: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    customer_provided_id: None | str | Unset = UNSET
    outcome: (
        GithubLookupPollingResponse200OutputDataItemOutcomeType1
        | GithubLookupPollingResponse200OutputDataItemOutcomeType2Type1
        | GithubLookupPollingResponse200OutputDataItemOutcomeType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

        confidence_out_of_10 = self.confidence_out_of_10

        github_url: None | str | Unset
        if isinstance(self.github_url, Unset):
            github_url = UNSET
        else:
            github_url = self.github_url

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

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

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        customer_provided_id: None | str | Unset
        if isinstance(self.customer_provided_id, Unset):
            customer_provided_id = UNSET
        else:
            customer_provided_id = self.customer_provided_id

        outcome: None | str | Unset
        if isinstance(self.outcome, Unset):
            outcome = UNSET
        elif isinstance(self.outcome, GithubLookupPollingResponse200OutputDataItemOutcomeType1):
            outcome = self.outcome.value
        elif isinstance(self.outcome, GithubLookupPollingResponse200OutputDataItemOutcomeType2Type1):
            outcome = self.outcome.value
        elif isinstance(self.outcome, GithubLookupPollingResponse200OutputDataItemOutcomeType3Type1):
            outcome = self.outcome.value
        else:
            outcome = self.outcome

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fullName": full_name,
                "confidenceOutOf10": confidence_out_of_10,
            }
        )
        if github_url is not UNSET:
            field_dict["githubUrl"] = github_url
        if username is not UNSET:
            field_dict["username"] = username
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
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if customer_provided_id is not UNSET:
            field_dict["customerProvidedId"] = customer_provided_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_name = d.pop("fullName")

        confidence_out_of_10 = d.pop("confidenceOutOf10")

        def _parse_github_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        github_url = _parse_github_url(d.pop("githubUrl", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

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

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_customer_provided_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId", UNSET))

        def _parse_outcome(
            data: object,
        ) -> (
            GithubLookupPollingResponse200OutputDataItemOutcomeType1
            | GithubLookupPollingResponse200OutputDataItemOutcomeType2Type1
            | GithubLookupPollingResponse200OutputDataItemOutcomeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_1 = GithubLookupPollingResponse200OutputDataItemOutcomeType1(data)

                return outcome_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_2_type_1 = GithubLookupPollingResponse200OutputDataItemOutcomeType2Type1(data)

                return outcome_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outcome_type_3_type_1 = GithubLookupPollingResponse200OutputDataItemOutcomeType3Type1(data)

                return outcome_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GithubLookupPollingResponse200OutputDataItemOutcomeType1
                | GithubLookupPollingResponse200OutputDataItemOutcomeType2Type1
                | GithubLookupPollingResponse200OutputDataItemOutcomeType3Type1
                | None
                | Unset,
                data,
            )

        outcome = _parse_outcome(d.pop("outcome", UNSET))

        github_lookup_polling_response_200_output_data_item = cls(
            full_name=full_name,
            confidence_out_of_10=confidence_out_of_10,
            github_url=github_url,
            username=username,
            display_name=display_name,
            profile_picture_url=profile_picture_url,
            bio=bio,
            location=location,
            num_repositories=num_repositories,
            num_followers=num_followers,
            rationale=rationale,
            error_message=error_message,
            customer_provided_id=customer_provided_id,
            outcome=outcome,
        )

        github_lookup_polling_response_200_output_data_item.additional_properties = d
        return github_lookup_polling_response_200_output_data_item

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
