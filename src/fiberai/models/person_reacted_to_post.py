from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_reacted_to_post_reaction_types_type_0_item import PersonReactedToPostReactionTypesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonReactedToPost")


@_attrs_define
class PersonReactedToPost:
    """
    Attributes:
        type_ (Literal['person_reacted_to_post']):
        entity_type (Literal['person']):
        lookback_days (int | None | Unset): Compare against a snapshot from approximately N days ago instead of the most
            recent prior snapshot. Omit for the default previous-snapshot comparison. Maximum 90 days.
        is_dummy (bool | Unset): When true, this rule only fires via the fire-dummy endpoint and is skipped during
            normal pipeline runs.
        keywords (list[str] | None | Unset): Only alert for reactions on posts whose content or author name matches
            these keywords. Omit for any reaction.
        reaction_types (list[PersonReactedToPostReactionTypesType0Item] | None | Unset): Only alert for these reaction
            types. Omit for any type.
    """

    type_: Literal["person_reacted_to_post"]
    entity_type: Literal["person"]
    lookback_days: int | None | Unset = UNSET
    is_dummy: bool | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    reaction_types: list[PersonReactedToPostReactionTypesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        entity_type = self.entity_type

        lookback_days: int | None | Unset
        if isinstance(self.lookback_days, Unset):
            lookback_days = UNSET
        else:
            lookback_days = self.lookback_days

        is_dummy = self.is_dummy

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        reaction_types: list[str] | None | Unset
        if isinstance(self.reaction_types, Unset):
            reaction_types = UNSET
        elif isinstance(self.reaction_types, list):
            reaction_types = []
            for reaction_types_type_0_item_data in self.reaction_types:
                reaction_types_type_0_item = reaction_types_type_0_item_data.value
                reaction_types.append(reaction_types_type_0_item)

        else:
            reaction_types = self.reaction_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "entityType": entity_type,
            }
        )
        if lookback_days is not UNSET:
            field_dict["lookbackDays"] = lookback_days
        if is_dummy is not UNSET:
            field_dict["isDummy"] = is_dummy
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if reaction_types is not UNSET:
            field_dict["reactionTypes"] = reaction_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["person_reacted_to_post"], d.pop("type"))
        if type_ != "person_reacted_to_post":
            raise ValueError(f"type must match const 'person_reacted_to_post', got '{type_}'")

        entity_type = cast(Literal["person"], d.pop("entityType"))
        if entity_type != "person":
            raise ValueError(f"entityType must match const 'person', got '{entity_type}'")

        def _parse_lookback_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lookback_days = _parse_lookback_days(d.pop("lookbackDays", UNSET))

        is_dummy = d.pop("isDummy", UNSET)

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_reaction_types(data: object) -> list[PersonReactedToPostReactionTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reaction_types_type_0 = []
                _reaction_types_type_0 = data
                for reaction_types_type_0_item_data in _reaction_types_type_0:
                    reaction_types_type_0_item = PersonReactedToPostReactionTypesType0Item(
                        reaction_types_type_0_item_data
                    )

                    reaction_types_type_0.append(reaction_types_type_0_item)

                return reaction_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PersonReactedToPostReactionTypesType0Item] | None | Unset, data)

        reaction_types = _parse_reaction_types(d.pop("reactionTypes", UNSET))

        person_reacted_to_post = cls(
            type_=type_,
            entity_type=entity_type,
            lookback_days=lookback_days,
            is_dummy=is_dummy,
            keywords=keywords,
            reaction_types=reaction_types,
        )

        person_reacted_to_post.additional_properties = d
        return person_reacted_to_post

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
