from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_comments_live_fetch_response_200_output_data_item_commenter_type_0 import (
        PostCommentsLiveFetchResponse200OutputDataItemCommenterType0,
    )
    from ..models.post_comments_live_fetch_response_200_output_data_item_comments_type_0_item import (
        PostCommentsLiveFetchResponse200OutputDataItemCommentsType0Item,
    )
    from ..models.post_comments_live_fetch_response_200_output_data_item_reactions_by_type_type_0_item import (
        PostCommentsLiveFetchResponse200OutputDataItemReactionsByTypeType0Item,
    )


T = TypeVar("T", bound="PostCommentsLiveFetchResponse200OutputDataItem")


@_attrs_define
class PostCommentsLiveFetchResponse200OutputDataItem:
    """
    Attributes:
        commentary (None | str | Unset):
        commenter (None | PostCommentsLiveFetchResponse200OutputDataItemCommenterType0 | Unset):
        num_reactions (float | None | Unset):
        num_comments (float | None | Unset):
        reactions_by_type (list[PostCommentsLiveFetchResponse200OutputDataItemReactionsByTypeType0Item] | None | Unset):
        created_at (None | str | Unset):
        comments (list[PostCommentsLiveFetchResponse200OutputDataItemCommentsType0Item] | None | Unset):
    """

    commentary: None | str | Unset = UNSET
    commenter: None | PostCommentsLiveFetchResponse200OutputDataItemCommenterType0 | Unset = UNSET
    num_reactions: float | None | Unset = UNSET
    num_comments: float | None | Unset = UNSET
    reactions_by_type: list[PostCommentsLiveFetchResponse200OutputDataItemReactionsByTypeType0Item] | None | Unset = (
        UNSET
    )
    created_at: None | str | Unset = UNSET
    comments: list[PostCommentsLiveFetchResponse200OutputDataItemCommentsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_comments_live_fetch_response_200_output_data_item_commenter_type_0 import (
            PostCommentsLiveFetchResponse200OutputDataItemCommenterType0,
        )

        commentary: None | str | Unset
        if isinstance(self.commentary, Unset):
            commentary = UNSET
        else:
            commentary = self.commentary

        commenter: dict[str, Any] | None | Unset
        if isinstance(self.commenter, Unset):
            commenter = UNSET
        elif isinstance(self.commenter, PostCommentsLiveFetchResponse200OutputDataItemCommenterType0):
            commenter = self.commenter.to_dict()
        else:
            commenter = self.commenter

        num_reactions: float | None | Unset
        if isinstance(self.num_reactions, Unset):
            num_reactions = UNSET
        else:
            num_reactions = self.num_reactions

        num_comments: float | None | Unset
        if isinstance(self.num_comments, Unset):
            num_comments = UNSET
        else:
            num_comments = self.num_comments

        reactions_by_type: list[dict[str, Any]] | None | Unset
        if isinstance(self.reactions_by_type, Unset):
            reactions_by_type = UNSET
        elif isinstance(self.reactions_by_type, list):
            reactions_by_type = []
            for reactions_by_type_type_0_item_data in self.reactions_by_type:
                reactions_by_type_type_0_item = reactions_by_type_type_0_item_data.to_dict()
                reactions_by_type.append(reactions_by_type_type_0_item)

        else:
            reactions_by_type = self.reactions_by_type

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        comments: list[dict[str, Any]] | None | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        elif isinstance(self.comments, list):
            comments = []
            for comments_type_0_item_data in self.comments:
                comments_type_0_item = comments_type_0_item_data.to_dict()
                comments.append(comments_type_0_item)

        else:
            comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commentary is not UNSET:
            field_dict["commentary"] = commentary
        if commenter is not UNSET:
            field_dict["commenter"] = commenter
        if num_reactions is not UNSET:
            field_dict["numReactions"] = num_reactions
        if num_comments is not UNSET:
            field_dict["numComments"] = num_comments
        if reactions_by_type is not UNSET:
            field_dict["reactionsByType"] = reactions_by_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_comments_live_fetch_response_200_output_data_item_commenter_type_0 import (
            PostCommentsLiveFetchResponse200OutputDataItemCommenterType0,
        )
        from ..models.post_comments_live_fetch_response_200_output_data_item_comments_type_0_item import (
            PostCommentsLiveFetchResponse200OutputDataItemCommentsType0Item,
        )
        from ..models.post_comments_live_fetch_response_200_output_data_item_reactions_by_type_type_0_item import (
            PostCommentsLiveFetchResponse200OutputDataItemReactionsByTypeType0Item,
        )

        d = dict(src_dict)

        def _parse_commentary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commentary = _parse_commentary(d.pop("commentary", UNSET))

        def _parse_commenter(
            data: object,
        ) -> None | PostCommentsLiveFetchResponse200OutputDataItemCommenterType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                commenter_type_0 = PostCommentsLiveFetchResponse200OutputDataItemCommenterType0.from_dict(data)

                return commenter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostCommentsLiveFetchResponse200OutputDataItemCommenterType0 | Unset, data)

        commenter = _parse_commenter(d.pop("commenter", UNSET))

        def _parse_num_reactions(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_reactions = _parse_num_reactions(d.pop("numReactions", UNSET))

        def _parse_num_comments(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_comments = _parse_num_comments(d.pop("numComments", UNSET))

        def _parse_reactions_by_type(
            data: object,
        ) -> list[PostCommentsLiveFetchResponse200OutputDataItemReactionsByTypeType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reactions_by_type_type_0 = []
                _reactions_by_type_type_0 = data
                for reactions_by_type_type_0_item_data in _reactions_by_type_type_0:
                    reactions_by_type_type_0_item = (
                        PostCommentsLiveFetchResponse200OutputDataItemReactionsByTypeType0Item.from_dict(
                            reactions_by_type_type_0_item_data
                        )
                    )

                    reactions_by_type_type_0.append(reactions_by_type_type_0_item)

                return reactions_by_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[PostCommentsLiveFetchResponse200OutputDataItemReactionsByTypeType0Item] | None | Unset, data
            )

        reactions_by_type = _parse_reactions_by_type(d.pop("reactionsByType", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_comments(
            data: object,
        ) -> list[PostCommentsLiveFetchResponse200OutputDataItemCommentsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                comments_type_0 = []
                _comments_type_0 = data
                for comments_type_0_item_data in _comments_type_0:
                    comments_type_0_item = PostCommentsLiveFetchResponse200OutputDataItemCommentsType0Item.from_dict(
                        comments_type_0_item_data
                    )

                    comments_type_0.append(comments_type_0_item)

                return comments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PostCommentsLiveFetchResponse200OutputDataItemCommentsType0Item] | None | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        post_comments_live_fetch_response_200_output_data_item = cls(
            commentary=commentary,
            commenter=commenter,
            num_reactions=num_reactions,
            num_comments=num_comments,
            reactions_by_type=reactions_by_type,
            created_at=created_at,
            comments=comments,
        )

        post_comments_live_fetch_response_200_output_data_item.additional_properties = d
        return post_comments_live_fetch_response_200_output_data_item

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
