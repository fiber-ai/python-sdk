from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_to_linkedin_single_response_200_output_github_profile_type_0 import (
        GithubToLinkedinSingleResponse200OutputGithubProfileType0,
    )


T = TypeVar("T", bound="GithubToLinkedinSingleResponse200Output")


@_attrs_define
class GithubToLinkedinSingleResponse200Output:
    """
    Attributes:
        github_username (str): The GitHub username that was resolved.
        confidence_out_of_10 (int): Confidence score (0-10) for this resolution.
        extracted_emails (list[str]): Extracted work email addresses from GitHub commits/cache.
        customer_provided_id (None | str | Unset): Echoes the optional customer-provided ID from the request.
        linked_in_url (None | str | Unset): Resolved LinkedIn profile URL when available.
        linked_in_slug (None | str | Unset): Resolved LinkedIn profile slug when available.
        rationale (None | str | Unset): Optional explanation for the selected match.
        github_profile (GithubToLinkedinSingleResponse200OutputGithubProfileType0 | None | Unset): Basic GitHub profile
            fields used by the resolver.
    """

    github_username: str
    confidence_out_of_10: int
    extracted_emails: list[str]
    customer_provided_id: None | str | Unset = UNSET
    linked_in_url: None | str | Unset = UNSET
    linked_in_slug: None | str | Unset = UNSET
    rationale: None | str | Unset = UNSET
    github_profile: GithubToLinkedinSingleResponse200OutputGithubProfileType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.github_to_linkedin_single_response_200_output_github_profile_type_0 import (
            GithubToLinkedinSingleResponse200OutputGithubProfileType0,
        )

        github_username = self.github_username

        confidence_out_of_10 = self.confidence_out_of_10

        extracted_emails = self.extracted_emails

        customer_provided_id: None | str | Unset
        if isinstance(self.customer_provided_id, Unset):
            customer_provided_id = UNSET
        else:
            customer_provided_id = self.customer_provided_id

        linked_in_url: None | str | Unset
        if isinstance(self.linked_in_url, Unset):
            linked_in_url = UNSET
        else:
            linked_in_url = self.linked_in_url

        linked_in_slug: None | str | Unset
        if isinstance(self.linked_in_slug, Unset):
            linked_in_slug = UNSET
        else:
            linked_in_slug = self.linked_in_slug

        rationale: None | str | Unset
        if isinstance(self.rationale, Unset):
            rationale = UNSET
        else:
            rationale = self.rationale

        github_profile: dict[str, Any] | None | Unset
        if isinstance(self.github_profile, Unset):
            github_profile = UNSET
        elif isinstance(self.github_profile, GithubToLinkedinSingleResponse200OutputGithubProfileType0):
            github_profile = self.github_profile.to_dict()
        else:
            github_profile = self.github_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "githubUsername": github_username,
                "confidenceOutOf10": confidence_out_of_10,
                "extractedEmails": extracted_emails,
            }
        )
        if customer_provided_id is not UNSET:
            field_dict["customerProvidedId"] = customer_provided_id
        if linked_in_url is not UNSET:
            field_dict["linkedInUrl"] = linked_in_url
        if linked_in_slug is not UNSET:
            field_dict["linkedInSlug"] = linked_in_slug
        if rationale is not UNSET:
            field_dict["rationale"] = rationale
        if github_profile is not UNSET:
            field_dict["githubProfile"] = github_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_to_linkedin_single_response_200_output_github_profile_type_0 import (
            GithubToLinkedinSingleResponse200OutputGithubProfileType0,
        )

        d = dict(src_dict)
        github_username = d.pop("githubUsername")

        confidence_out_of_10 = d.pop("confidenceOutOf10")

        extracted_emails = cast(list[str], d.pop("extractedEmails"))

        def _parse_customer_provided_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId", UNSET))

        def _parse_linked_in_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linked_in_url = _parse_linked_in_url(d.pop("linkedInUrl", UNSET))

        def _parse_linked_in_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linked_in_slug = _parse_linked_in_slug(d.pop("linkedInSlug", UNSET))

        def _parse_rationale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rationale = _parse_rationale(d.pop("rationale", UNSET))

        def _parse_github_profile(
            data: object,
        ) -> GithubToLinkedinSingleResponse200OutputGithubProfileType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                github_profile_type_0 = GithubToLinkedinSingleResponse200OutputGithubProfileType0.from_dict(data)

                return github_profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GithubToLinkedinSingleResponse200OutputGithubProfileType0 | None | Unset, data)

        github_profile = _parse_github_profile(d.pop("githubProfile", UNSET))

        github_to_linkedin_single_response_200_output = cls(
            github_username=github_username,
            confidence_out_of_10=confidence_out_of_10,
            extracted_emails=extracted_emails,
            customer_provided_id=customer_provided_id,
            linked_in_url=linked_in_url,
            linked_in_slug=linked_in_slug,
            rationale=rationale,
            github_profile=github_profile,
        )

        github_to_linkedin_single_response_200_output.additional_properties = d
        return github_to_linkedin_single_response_200_output

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
