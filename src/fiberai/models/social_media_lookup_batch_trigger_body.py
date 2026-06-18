from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_media_lookup_batch_trigger_body_platforms_item import (
    SocialMediaLookupBatchTriggerBodyPlatformsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_media_lookup_batch_trigger_body_people_item_type_0 import (
        SocialMediaLookupBatchTriggerBodyPeopleItemType0,
    )
    from ..models.social_media_lookup_batch_trigger_body_people_item_type_1 import (
        SocialMediaLookupBatchTriggerBodyPeopleItemType1,
    )
    from ..models.social_media_lookup_batch_trigger_body_people_item_type_2 import (
        SocialMediaLookupBatchTriggerBodyPeopleItemType2,
    )


T = TypeVar("T", bound="SocialMediaLookupBatchTriggerBody")


@_attrs_define
class SocialMediaLookupBatchTriggerBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        people (list[SocialMediaLookupBatchTriggerBodyPeopleItemType0 | SocialMediaLookupBatchTriggerBodyPeopleItemType1
            | SocialMediaLookupBatchTriggerBodyPeopleItemType2]): Array of people to look up (1-100). Each person can be
            identified by LinkedIn URL, LinkedIn user ID, or manual name+context.
        overall_context (None | str | Unset): Optional context about this batch to help disambiguation (e.g. 'AI startup
            founders'). Applied to all people in the batch.
        platforms (list[SocialMediaLookupBatchTriggerBodyPlatformsItem] | Unset): Which social media platforms to
            search. Defaults to Twitter/X.
    """

    api_key: str
    people: list[
        SocialMediaLookupBatchTriggerBodyPeopleItemType0
        | SocialMediaLookupBatchTriggerBodyPeopleItemType1
        | SocialMediaLookupBatchTriggerBodyPeopleItemType2
    ]
    overall_context: None | str | Unset = UNSET
    platforms: list[SocialMediaLookupBatchTriggerBodyPlatformsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.social_media_lookup_batch_trigger_body_people_item_type_0 import (
            SocialMediaLookupBatchTriggerBodyPeopleItemType0,
        )
        from ..models.social_media_lookup_batch_trigger_body_people_item_type_1 import (
            SocialMediaLookupBatchTriggerBodyPeopleItemType1,
        )

        api_key = self.api_key

        people = []
        for people_item_data in self.people:
            people_item: dict[str, Any]
            if isinstance(people_item_data, SocialMediaLookupBatchTriggerBodyPeopleItemType0):
                people_item = people_item_data.to_dict()
            elif isinstance(people_item_data, SocialMediaLookupBatchTriggerBodyPeopleItemType1):
                people_item = people_item_data.to_dict()
            else:
                people_item = people_item_data.to_dict()

            people.append(people_item)

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
                "people": people,
            }
        )
        if overall_context is not UNSET:
            field_dict["overallContext"] = overall_context
        if platforms is not UNSET:
            field_dict["platforms"] = platforms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_media_lookup_batch_trigger_body_people_item_type_0 import (
            SocialMediaLookupBatchTriggerBodyPeopleItemType0,
        )
        from ..models.social_media_lookup_batch_trigger_body_people_item_type_1 import (
            SocialMediaLookupBatchTriggerBodyPeopleItemType1,
        )
        from ..models.social_media_lookup_batch_trigger_body_people_item_type_2 import (
            SocialMediaLookupBatchTriggerBodyPeopleItemType2,
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        people = []
        _people = d.pop("people")
        for people_item_data in _people:

            def _parse_people_item(
                data: object,
            ) -> (
                SocialMediaLookupBatchTriggerBodyPeopleItemType0
                | SocialMediaLookupBatchTriggerBodyPeopleItemType1
                | SocialMediaLookupBatchTriggerBodyPeopleItemType2
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    people_item_type_0 = SocialMediaLookupBatchTriggerBodyPeopleItemType0.from_dict(data)

                    return people_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    people_item_type_1 = SocialMediaLookupBatchTriggerBodyPeopleItemType1.from_dict(data)

                    return people_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                people_item_type_2 = SocialMediaLookupBatchTriggerBodyPeopleItemType2.from_dict(data)

                return people_item_type_2

            people_item = _parse_people_item(people_item_data)

            people.append(people_item)

        def _parse_overall_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overall_context = _parse_overall_context(d.pop("overallContext", UNSET))

        _platforms = d.pop("platforms", UNSET)
        platforms: list[SocialMediaLookupBatchTriggerBodyPlatformsItem] | Unset = UNSET
        if _platforms is not UNSET:
            platforms = []
            for platforms_item_data in _platforms:
                platforms_item = SocialMediaLookupBatchTriggerBodyPlatformsItem(platforms_item_data)

                platforms.append(platforms_item)

        social_media_lookup_batch_trigger_body = cls(
            api_key=api_key,
            people=people,
            overall_context=overall_context,
            platforms=platforms,
        )

        social_media_lookup_batch_trigger_body.additional_properties = d
        return social_media_lookup_batch_trigger_body

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
