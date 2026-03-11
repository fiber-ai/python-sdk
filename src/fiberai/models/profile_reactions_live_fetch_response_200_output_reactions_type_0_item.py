from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_type_type_1 import (
    ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1,
)
from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_type_type_2_type_1 import (
    ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1,
)
from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_type_type_3_type_1 import (
    ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0 import (
        ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0,
    )
    from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0 import (
        ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0,
    )
    from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_reactor_type_0 import (
        ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0,
    )


T = TypeVar("T", bound="ProfileReactionsLiveFetchResponse200OutputReactionsType0Item")


@_attrs_define
class ProfileReactionsLiveFetchResponse200OutputReactionsType0Item:
    """
    Attributes:
        reaction_id (None | str | Unset):
        type_ (None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1 |
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1 |
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1 | Unset): One of LinkedIn's reaction
            types. These match the tooltips on each of LinkedIn's six reaction buttons; for instance, 'Like' is the blue
            thumbs-up.
        target (None | str | Unset):
        reacted_ago (None | str | Unset):
        reactor (None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0 | Unset):
        post (None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0 | Unset):
        comment (None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0 | Unset):
    """

    reaction_id: None | str | Unset = UNSET
    type_: (
        None
        | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1
        | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1
        | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1
        | Unset
    ) = UNSET
    target: None | str | Unset = UNSET
    reacted_ago: None | str | Unset = UNSET
    reactor: None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0 | Unset = UNSET
    post: None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0 | Unset = UNSET
    comment: None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0,
        )
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0,
        )
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_reactor_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0,
        )

        reaction_id: None | str | Unset
        if isinstance(self.reaction_id, Unset):
            reaction_id = UNSET
        else:
            reaction_id = self.reaction_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        target: None | str | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target

        reacted_ago: None | str | Unset
        if isinstance(self.reacted_ago, Unset):
            reacted_ago = UNSET
        else:
            reacted_ago = self.reacted_ago

        reactor: dict[str, Any] | None | Unset
        if isinstance(self.reactor, Unset):
            reactor = UNSET
        elif isinstance(self.reactor, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0):
            reactor = self.reactor.to_dict()
        else:
            reactor = self.reactor

        post: dict[str, Any] | None | Unset
        if isinstance(self.post, Unset):
            post = UNSET
        elif isinstance(self.post, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0):
            post = self.post.to_dict()
        else:
            post = self.post

        comment: dict[str, Any] | None | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        elif isinstance(self.comment, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0):
            comment = self.comment.to_dict()
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reaction_id is not UNSET:
            field_dict["reactionId"] = reaction_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if target is not UNSET:
            field_dict["target"] = target
        if reacted_ago is not UNSET:
            field_dict["reactedAgo"] = reacted_ago
        if reactor is not UNSET:
            field_dict["reactor"] = reactor
        if post is not UNSET:
            field_dict["post"] = post
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0,
        )
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0,
        )
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_reactor_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0,
        )

        d = dict(src_dict)

        def _parse_reaction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reaction_id = _parse_reaction_id(d.pop("reactionId", UNSET))

        def _parse_type_(
            data: object,
        ) -> (
            None
            | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1
            | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1
            | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1(data)

                return type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1(data)

                return type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1
                | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1
                | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1
                | Unset,
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target = _parse_target(d.pop("target", UNSET))

        def _parse_reacted_ago(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reacted_ago = _parse_reacted_ago(d.pop("reactedAgo", UNSET))

        def _parse_reactor(
            data: object,
        ) -> None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reactor_type_0 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0.from_dict(
                    data
                )

                return reactor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0 | Unset, data)

        reactor = _parse_reactor(d.pop("reactor", UNSET))

        def _parse_post(
            data: object,
        ) -> None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                post_type_0 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0.from_dict(data)

                return post_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0 | Unset, data)

        post = _parse_post(d.pop("post", UNSET))

        def _parse_comment(
            data: object,
        ) -> None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                comment_type_0 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0.from_dict(
                    data
                )

                return comment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0 | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        profile_reactions_live_fetch_response_200_output_reactions_type_0_item = cls(
            reaction_id=reaction_id,
            type_=type_,
            target=target,
            reacted_ago=reacted_ago,
            reactor=reactor,
            post=post,
            comment=comment,
        )

        profile_reactions_live_fetch_response_200_output_reactions_type_0_item.additional_properties = d
        return profile_reactions_live_fetch_response_200_output_reactions_type_0_item

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
