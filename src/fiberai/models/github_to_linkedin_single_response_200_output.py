from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_to_linkedin_single_response_200_output_match_source import (
    GithubToLinkedinSingleResponse200OutputMatchSource,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_to_linkedin_single_response_200_output_debug_timings_type_0 import (
        GithubToLinkedinSingleResponse200OutputDebugTimingsType0,
    )
    from ..models.github_to_linkedin_single_response_200_output_github_profile_type_0 import (
        GithubToLinkedinSingleResponse200OutputGithubProfileType0,
    )


T = TypeVar("T", bound="GithubToLinkedinSingleResponse200Output")


@_attrs_define
class GithubToLinkedinSingleResponse200Output:
    """
    Attributes:
        github_username (str): The GitHub username that was resolved.
        customer_provided_id (None | str): Echoes the optional customer-provided ID from the request.
        linked_in_url (None | str): Resolved LinkedIn profile URL when available.
        linked_in_slug (None | str): Resolved LinkedIn profile slug when available.
        confidence_out_of_10 (int): Confidence score (0-10) for this resolution.
        match_source (GithubToLinkedinSingleResponse200OutputMatchSource): Method used to resolve the result. See the
            enum values on the PublicMatchSource schema for the full list.
        rationale (None | str): Optional explanation for the selected match.
        extracted_emails (list[str]): Extracted work email addresses from GitHub commits/cache.
        github_profile (GithubToLinkedinSingleResponse200OutputGithubProfileType0 | None): Basic GitHub profile fields
            used by the resolver.
        debug_timings (GithubToLinkedinSingleResponse200OutputDebugTimingsType0 | None | Unset): Optional resolver
            timing metadata. Present only when requested for diagnostics.
    """

    github_username: str
    customer_provided_id: None | str
    linked_in_url: None | str
    linked_in_slug: None | str
    confidence_out_of_10: int
    match_source: GithubToLinkedinSingleResponse200OutputMatchSource
    rationale: None | str
    extracted_emails: list[str]
    github_profile: GithubToLinkedinSingleResponse200OutputGithubProfileType0 | None
    debug_timings: GithubToLinkedinSingleResponse200OutputDebugTimingsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.github_to_linkedin_single_response_200_output_debug_timings_type_0 import (
            GithubToLinkedinSingleResponse200OutputDebugTimingsType0,
        )
        from ..models.github_to_linkedin_single_response_200_output_github_profile_type_0 import (
            GithubToLinkedinSingleResponse200OutputGithubProfileType0,
        )

        github_username = self.github_username

        customer_provided_id: None | str
        customer_provided_id = self.customer_provided_id

        linked_in_url: None | str
        linked_in_url = self.linked_in_url

        linked_in_slug: None | str
        linked_in_slug = self.linked_in_slug

        confidence_out_of_10 = self.confidence_out_of_10

        match_source = self.match_source.value

        rationale: None | str
        rationale = self.rationale

        extracted_emails = self.extracted_emails

        github_profile: dict[str, Any] | None
        if isinstance(self.github_profile, GithubToLinkedinSingleResponse200OutputGithubProfileType0):
            github_profile = self.github_profile.to_dict()
        else:
            github_profile = self.github_profile

        debug_timings: dict[str, Any] | None | Unset
        if isinstance(self.debug_timings, Unset):
            debug_timings = UNSET
        elif isinstance(self.debug_timings, GithubToLinkedinSingleResponse200OutputDebugTimingsType0):
            debug_timings = self.debug_timings.to_dict()
        else:
            debug_timings = self.debug_timings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "githubUsername": github_username,
                "customerProvidedId": customer_provided_id,
                "linkedInUrl": linked_in_url,
                "linkedInSlug": linked_in_slug,
                "confidenceOutOf10": confidence_out_of_10,
                "matchSource": match_source,
                "rationale": rationale,
                "extractedEmails": extracted_emails,
                "githubProfile": github_profile,
            }
        )
        if debug_timings is not UNSET:
            field_dict["debugTimings"] = debug_timings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_to_linkedin_single_response_200_output_debug_timings_type_0 import (
            GithubToLinkedinSingleResponse200OutputDebugTimingsType0,
        )
        from ..models.github_to_linkedin_single_response_200_output_github_profile_type_0 import (
            GithubToLinkedinSingleResponse200OutputGithubProfileType0,
        )

        d = dict(src_dict)
        github_username = d.pop("githubUsername")

        def _parse_customer_provided_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId"))

        def _parse_linked_in_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linked_in_url = _parse_linked_in_url(d.pop("linkedInUrl"))

        def _parse_linked_in_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linked_in_slug = _parse_linked_in_slug(d.pop("linkedInSlug"))

        confidence_out_of_10 = d.pop("confidenceOutOf10")

        match_source = GithubToLinkedinSingleResponse200OutputMatchSource(d.pop("matchSource"))

        def _parse_rationale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rationale = _parse_rationale(d.pop("rationale"))

        extracted_emails = cast(list[str], d.pop("extractedEmails"))

        def _parse_github_profile(data: object) -> GithubToLinkedinSingleResponse200OutputGithubProfileType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                github_profile_type_0 = GithubToLinkedinSingleResponse200OutputGithubProfileType0.from_dict(data)

                return github_profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GithubToLinkedinSingleResponse200OutputGithubProfileType0 | None, data)

        github_profile = _parse_github_profile(d.pop("githubProfile"))

        def _parse_debug_timings(
            data: object,
        ) -> GithubToLinkedinSingleResponse200OutputDebugTimingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                debug_timings_type_0 = GithubToLinkedinSingleResponse200OutputDebugTimingsType0.from_dict(data)

                return debug_timings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GithubToLinkedinSingleResponse200OutputDebugTimingsType0 | None | Unset, data)

        debug_timings = _parse_debug_timings(d.pop("debugTimings", UNSET))

        github_to_linkedin_single_response_200_output = cls(
            github_username=github_username,
            customer_provided_id=customer_provided_id,
            linked_in_url=linked_in_url,
            linked_in_slug=linked_in_slug,
            confidence_out_of_10=confidence_out_of_10,
            match_source=match_source,
            rationale=rationale,
            extracted_emails=extracted_emails,
            github_profile=github_profile,
            debug_timings=debug_timings,
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
