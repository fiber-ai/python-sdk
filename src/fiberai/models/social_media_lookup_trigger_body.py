from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_media_lookup_trigger_body_platforms_item import SocialMediaLookupTriggerBodyPlatformsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_media_lookup_trigger_body_person_type_0 import SocialMediaLookupTriggerBodyPersonType0
    from ..models.social_media_lookup_trigger_body_person_type_1 import SocialMediaLookupTriggerBodyPersonType1
    from ..models.social_media_lookup_trigger_body_person_type_2 import SocialMediaLookupTriggerBodyPersonType2


T = TypeVar("T", bound="SocialMediaLookupTriggerBody")


@_attrs_define
class SocialMediaLookupTriggerBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        person (SocialMediaLookupTriggerBodyPersonType0 | SocialMediaLookupTriggerBodyPersonType1 |
            SocialMediaLookupTriggerBodyPersonType2): The person to look up.
        overall_context (None | str | Unset): Optional context about the person to help disambiguation (e.g. "AI
            researcher at OpenAI"). Useful for common names. Max 1000 characters.
        platforms (list[SocialMediaLookupTriggerBodyPlatformsItem] | Unset): Which social media platforms to search.
            Defaults to Twitter. Supported: TWITTER, INSTAGRAM.
    """

    api_key: str
    person: (
        SocialMediaLookupTriggerBodyPersonType0
        | SocialMediaLookupTriggerBodyPersonType1
        | SocialMediaLookupTriggerBodyPersonType2
    )
    overall_context: None | str | Unset = UNSET
    platforms: list[SocialMediaLookupTriggerBodyPlatformsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.social_media_lookup_trigger_body_person_type_0 import (
            SocialMediaLookupTriggerBodyPersonType0,  # noqa: PLC0415
        )
        from ..models.social_media_lookup_trigger_body_person_type_1 import (
            SocialMediaLookupTriggerBodyPersonType1,  # noqa: PLC0415
        )

        api_key = self.api_key

        person: dict[str, Any]
        if isinstance(self.person, SocialMediaLookupTriggerBodyPersonType0):
            person = self.person.to_dict()
        elif isinstance(self.person, SocialMediaLookupTriggerBodyPersonType1):
            person = self.person.to_dict()
        else:
            person = self.person.to_dict()

        overall_context: None | str | Unset
        if isinstance(self.overall_context, Unset):
            overall_context = UNSET
        else:
            overall_context = self.overall_context

        platforms: list[str] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.value
                platforms.append(platforms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "person": person,
            }
        )
        if overall_context is not UNSET:
            field_dict["overallContext"] = overall_context
        if platforms is not UNSET:
            field_dict["platforms"] = platforms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_media_lookup_trigger_body_person_type_0 import (
            SocialMediaLookupTriggerBodyPersonType0,  # noqa: PLC0415
        )
        from ..models.social_media_lookup_trigger_body_person_type_1 import (
            SocialMediaLookupTriggerBodyPersonType1,  # noqa: PLC0415
        )
        from ..models.social_media_lookup_trigger_body_person_type_2 import (
            SocialMediaLookupTriggerBodyPersonType2,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_person(
            data: object,
        ) -> (
            SocialMediaLookupTriggerBodyPersonType0
            | SocialMediaLookupTriggerBodyPersonType1
            | SocialMediaLookupTriggerBodyPersonType2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_type_0 = SocialMediaLookupTriggerBodyPersonType0.from_dict(data)

                return person_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_type_1 = SocialMediaLookupTriggerBodyPersonType1.from_dict(data)

                return person_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            person_type_2 = SocialMediaLookupTriggerBodyPersonType2.from_dict(data)

            return person_type_2

        person = _parse_person(d.pop("person"))

        def _parse_overall_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overall_context = _parse_overall_context(d.pop("overallContext", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[SocialMediaLookupTriggerBodyPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = SocialMediaLookupTriggerBodyPlatformsItem(platforms_item_data)

                platforms.append(platforms_item)

        social_media_lookup_trigger_body = cls(
            api_key=api_key,
            person=person,
            overall_context=overall_context,
            platforms=platforms,
        )

        social_media_lookup_trigger_body.additional_properties = d
        return social_media_lookup_trigger_body

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
