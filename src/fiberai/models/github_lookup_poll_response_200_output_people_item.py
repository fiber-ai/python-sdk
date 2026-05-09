from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_0 import (
        GithubLookupPollResponse200OutputPeopleItemGithubProfileType0,
    )
    from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_1 import (
        GithubLookupPollResponse200OutputPeopleItemGithubProfileType1,
    )
    from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_2 import (
        GithubLookupPollResponse200OutputPeopleItemGithubProfileType2,
    )
    from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_3 import (
        GithubLookupPollResponse200OutputPeopleItemGithubProfileType3,
    )
    from ..models.github_lookup_poll_response_200_output_people_item_person import (
        GithubLookupPollResponse200OutputPeopleItemPerson,
    )


T = TypeVar("T", bound="GithubLookupPollResponse200OutputPeopleItem")


@_attrs_define
class GithubLookupPollResponse200OutputPeopleItem:
    """
    Attributes:
        person (GithubLookupPollResponse200OutputPeopleItemPerson): The original input person.
        github_profile (GithubLookupPollResponse200OutputPeopleItemGithubProfileType0 |
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType1 |
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType2 |
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType3): The GitHub lookup result for this person.
    """

    person: GithubLookupPollResponse200OutputPeopleItemPerson
    github_profile: (
        GithubLookupPollResponse200OutputPeopleItemGithubProfileType0
        | GithubLookupPollResponse200OutputPeopleItemGithubProfileType1
        | GithubLookupPollResponse200OutputPeopleItemGithubProfileType2
        | GithubLookupPollResponse200OutputPeopleItemGithubProfileType3
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_0 import (
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType0,
        )
        from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_1 import (
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType1,
        )
        from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_2 import (
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType2,
        )

        person = self.person.to_dict()

        github_profile: dict[str, Any]
        if isinstance(self.github_profile, GithubLookupPollResponse200OutputPeopleItemGithubProfileType0):
            github_profile = self.github_profile.to_dict()
        elif isinstance(self.github_profile, GithubLookupPollResponse200OutputPeopleItemGithubProfileType1):
            github_profile = self.github_profile.to_dict()
        elif isinstance(self.github_profile, GithubLookupPollResponse200OutputPeopleItemGithubProfileType2):
            github_profile = self.github_profile.to_dict()
        else:
            github_profile = self.github_profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "person": person,
                "githubProfile": github_profile,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_0 import (
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType0,
        )
        from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_1 import (
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType1,
        )
        from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_2 import (
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType2,
        )
        from ..models.github_lookup_poll_response_200_output_people_item_github_profile_type_3 import (
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType3,
        )
        from ..models.github_lookup_poll_response_200_output_people_item_person import (
            GithubLookupPollResponse200OutputPeopleItemPerson,
        )

        d = dict(src_dict)
        person = GithubLookupPollResponse200OutputPeopleItemPerson.from_dict(d.pop("person"))

        def _parse_github_profile(
            data: object,
        ) -> (
            GithubLookupPollResponse200OutputPeopleItemGithubProfileType0
            | GithubLookupPollResponse200OutputPeopleItemGithubProfileType1
            | GithubLookupPollResponse200OutputPeopleItemGithubProfileType2
            | GithubLookupPollResponse200OutputPeopleItemGithubProfileType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                github_profile_type_0 = GithubLookupPollResponse200OutputPeopleItemGithubProfileType0.from_dict(data)

                return github_profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                github_profile_type_1 = GithubLookupPollResponse200OutputPeopleItemGithubProfileType1.from_dict(data)

                return github_profile_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                github_profile_type_2 = GithubLookupPollResponse200OutputPeopleItemGithubProfileType2.from_dict(data)

                return github_profile_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            github_profile_type_3 = GithubLookupPollResponse200OutputPeopleItemGithubProfileType3.from_dict(data)

            return github_profile_type_3

        github_profile = _parse_github_profile(d.pop("githubProfile"))

        github_lookup_poll_response_200_output_people_item = cls(
            person=person,
            github_profile=github_profile,
        )

        github_lookup_poll_response_200_output_people_item.additional_properties = d
        return github_lookup_poll_response_200_output_people_item

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
