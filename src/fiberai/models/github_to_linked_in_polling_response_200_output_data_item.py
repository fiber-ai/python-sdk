from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.github_to_linked_in_polling_response_200_output_data_item_match_source import (
    GithubToLinkedInPollingResponse200OutputDataItemMatchSource,
)
from ..models.github_to_linked_in_polling_response_200_output_data_item_status import (
    GithubToLinkedInPollingResponse200OutputDataItemStatus,
)

if TYPE_CHECKING:
    from ..models.github_to_linked_in_polling_response_200_output_data_item_github_profile_type_0 import (
        GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0,
    )


T = TypeVar("T", bound="GithubToLinkedInPollingResponse200OutputDataItem")


@_attrs_define
class GithubToLinkedInPollingResponse200OutputDataItem:
    """
    Attributes:
        github_username (str):
        customer_provided_id (None | str):
        status (GithubToLinkedInPollingResponse200OutputDataItemStatus):
        linked_in_url (None | str):
        linked_in_slug (None | str):
        confidence_out_of_10 (int):
        match_source (GithubToLinkedInPollingResponse200OutputDataItemMatchSource):
        rationale (None | str):
        extracted_emails (list[str]):
        github_profile (GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0 | None):
        error_message (None | str):
    """

    github_username: str
    customer_provided_id: None | str
    status: GithubToLinkedInPollingResponse200OutputDataItemStatus
    linked_in_url: None | str
    linked_in_slug: None | str
    confidence_out_of_10: int
    match_source: GithubToLinkedInPollingResponse200OutputDataItemMatchSource
    rationale: None | str
    extracted_emails: list[str]
    github_profile: GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0 | None
    error_message: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.github_to_linked_in_polling_response_200_output_data_item_github_profile_type_0 import (
            GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0,
        )

        github_username = self.github_username

        customer_provided_id: None | str
        customer_provided_id = self.customer_provided_id

        status = self.status.value

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
        if isinstance(self.github_profile, GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0):
            github_profile = self.github_profile.to_dict()
        else:
            github_profile = self.github_profile

        error_message: None | str
        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "githubUsername": github_username,
                "customerProvidedId": customer_provided_id,
                "status": status,
                "linkedInUrl": linked_in_url,
                "linkedInSlug": linked_in_slug,
                "confidenceOutOf10": confidence_out_of_10,
                "matchSource": match_source,
                "rationale": rationale,
                "extractedEmails": extracted_emails,
                "githubProfile": github_profile,
                "errorMessage": error_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_to_linked_in_polling_response_200_output_data_item_github_profile_type_0 import (
            GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0,
        )

        d = dict(src_dict)
        github_username = d.pop("githubUsername")

        def _parse_customer_provided_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId"))

        status = GithubToLinkedInPollingResponse200OutputDataItemStatus(d.pop("status"))

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

        match_source = GithubToLinkedInPollingResponse200OutputDataItemMatchSource(d.pop("matchSource"))

        def _parse_rationale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rationale = _parse_rationale(d.pop("rationale"))

        extracted_emails = cast(list[str], d.pop("extractedEmails"))

        def _parse_github_profile(
            data: object,
        ) -> GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                github_profile_type_0 = GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0.from_dict(
                    data
                )

                return github_profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GithubToLinkedInPollingResponse200OutputDataItemGithubProfileType0 | None, data)

        github_profile = _parse_github_profile(d.pop("githubProfile"))

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("errorMessage"))

        github_to_linked_in_polling_response_200_output_data_item = cls(
            github_username=github_username,
            customer_provided_id=customer_provided_id,
            status=status,
            linked_in_url=linked_in_url,
            linked_in_slug=linked_in_slug,
            confidence_out_of_10=confidence_out_of_10,
            match_source=match_source,
            rationale=rationale,
            extracted_emails=extracted_emails,
            github_profile=github_profile,
            error_message=error_message,
        )

        github_to_linked_in_polling_response_200_output_data_item.additional_properties = d
        return github_to_linked_in_polling_response_200_output_data_item

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
