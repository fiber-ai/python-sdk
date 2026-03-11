from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_reactions_live_fetch_body_reaction_type_type_1 import PostReactionsLiveFetchBodyReactionTypeType1
from ..models.post_reactions_live_fetch_body_reaction_type_type_2_type_1 import (
    PostReactionsLiveFetchBodyReactionTypeType2Type1,
)
from ..models.post_reactions_live_fetch_body_reaction_type_type_3_type_1 import (
    PostReactionsLiveFetchBodyReactionTypeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostReactionsLiveFetchBody")


@_attrs_define
class PostReactionsLiveFetchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        content_id (str): You can get LinkedIn posts from the Profile or Company Posts endpoints. (e.g.,
            'urn:li:activity:7123456789012345678' or 'urn:li:ugcPost:7391650829398675456')
        reaction_type (None | PostReactionsLiveFetchBodyReactionTypeType1 |
            PostReactionsLiveFetchBodyReactionTypeType2Type1 | PostReactionsLiveFetchBodyReactionTypeType3Type1 | Unset):
            Type of reaction to fetch. If null, all reactions will be fetched.
        cursor (None | str | Unset): Pagination cursor for fetching additional pages of posts
    """

    api_key: str
    content_id: str
    reaction_type: (
        None
        | PostReactionsLiveFetchBodyReactionTypeType1
        | PostReactionsLiveFetchBodyReactionTypeType2Type1
        | PostReactionsLiveFetchBodyReactionTypeType3Type1
        | Unset
    ) = UNSET
    cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        content_id = self.content_id

        reaction_type: None | str | Unset
        if isinstance(self.reaction_type, Unset):
            reaction_type = UNSET
        elif isinstance(self.reaction_type, PostReactionsLiveFetchBodyReactionTypeType1):
            reaction_type = self.reaction_type.value
        elif isinstance(self.reaction_type, PostReactionsLiveFetchBodyReactionTypeType2Type1):
            reaction_type = self.reaction_type.value
        elif isinstance(self.reaction_type, PostReactionsLiveFetchBodyReactionTypeType3Type1):
            reaction_type = self.reaction_type.value
        else:
            reaction_type = self.reaction_type

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "contentId": content_id,
            }
        )
        if reaction_type is not UNSET:
            field_dict["reactionType"] = reaction_type
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        content_id = d.pop("contentId")

        def _parse_reaction_type(
            data: object,
        ) -> (
            None
            | PostReactionsLiveFetchBodyReactionTypeType1
            | PostReactionsLiveFetchBodyReactionTypeType2Type1
            | PostReactionsLiveFetchBodyReactionTypeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reaction_type_type_1 = PostReactionsLiveFetchBodyReactionTypeType1(data)

                return reaction_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reaction_type_type_2_type_1 = PostReactionsLiveFetchBodyReactionTypeType2Type1(data)

                return reaction_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reaction_type_type_3_type_1 = PostReactionsLiveFetchBodyReactionTypeType3Type1(data)

                return reaction_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PostReactionsLiveFetchBodyReactionTypeType1
                | PostReactionsLiveFetchBodyReactionTypeType2Type1
                | PostReactionsLiveFetchBodyReactionTypeType3Type1
                | Unset,
                data,
            )

        reaction_type = _parse_reaction_type(d.pop("reactionType", UNSET))

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        post_reactions_live_fetch_body = cls(
            api_key=api_key,
            content_id=content_id,
            reaction_type=reaction_type,
            cursor=cursor,
        )

        post_reactions_live_fetch_body.additional_properties = d
        return post_reactions_live_fetch_body

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
