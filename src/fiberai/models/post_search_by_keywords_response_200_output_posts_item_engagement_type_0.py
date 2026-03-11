from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_search_by_keywords_response_200_output_posts_item_engagement_type_0_reactions_by_type_type_0_item import (
        PostSearchByKeywordsResponse200OutputPostsItemEngagementType0ReactionsByTypeType0Item,
    )


T = TypeVar("T", bound="PostSearchByKeywordsResponse200OutputPostsItemEngagementType0")


@_attrs_define
class PostSearchByKeywordsResponse200OutputPostsItemEngagementType0:
    """
    Attributes:
        num_comments (float | None | Unset):
        num_shares (float | None | Unset):
        num_likes (float | None | Unset):
        reactions_by_type (list[PostSearchByKeywordsResponse200OutputPostsItemEngagementType0ReactionsByTypeType0Item] |
            None | Unset):
    """

    num_comments: float | None | Unset = UNSET
    num_shares: float | None | Unset = UNSET
    num_likes: float | None | Unset = UNSET
    reactions_by_type: (
        list[PostSearchByKeywordsResponse200OutputPostsItemEngagementType0ReactionsByTypeType0Item] | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_comments: float | None | Unset
        if isinstance(self.num_comments, Unset):
            num_comments = UNSET
        else:
            num_comments = self.num_comments

        num_shares: float | None | Unset
        if isinstance(self.num_shares, Unset):
            num_shares = UNSET
        else:
            num_shares = self.num_shares

        num_likes: float | None | Unset
        if isinstance(self.num_likes, Unset):
            num_likes = UNSET
        else:
            num_likes = self.num_likes

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_comments is not UNSET:
            field_dict["numComments"] = num_comments
        if num_shares is not UNSET:
            field_dict["numShares"] = num_shares
        if num_likes is not UNSET:
            field_dict["numLikes"] = num_likes
        if reactions_by_type is not UNSET:
            field_dict["reactionsByType"] = reactions_by_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_search_by_keywords_response_200_output_posts_item_engagement_type_0_reactions_by_type_type_0_item import (
            PostSearchByKeywordsResponse200OutputPostsItemEngagementType0ReactionsByTypeType0Item,
        )

        d = dict(src_dict)

        def _parse_num_comments(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_comments = _parse_num_comments(d.pop("numComments", UNSET))

        def _parse_num_shares(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_shares = _parse_num_shares(d.pop("numShares", UNSET))

        def _parse_num_likes(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_likes = _parse_num_likes(d.pop("numLikes", UNSET))

        def _parse_reactions_by_type(
            data: object,
        ) -> list[PostSearchByKeywordsResponse200OutputPostsItemEngagementType0ReactionsByTypeType0Item] | None | Unset:
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
                        PostSearchByKeywordsResponse200OutputPostsItemEngagementType0ReactionsByTypeType0Item.from_dict(
                            reactions_by_type_type_0_item_data
                        )
                    )

                    reactions_by_type_type_0.append(reactions_by_type_type_0_item)

                return reactions_by_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[PostSearchByKeywordsResponse200OutputPostsItemEngagementType0ReactionsByTypeType0Item]
                | None
                | Unset,
                data,
            )

        reactions_by_type = _parse_reactions_by_type(d.pop("reactionsByType", UNSET))

        post_search_by_keywords_response_200_output_posts_item_engagement_type_0 = cls(
            num_comments=num_comments,
            num_shares=num_shares,
            num_likes=num_likes,
            reactions_by_type=reactions_by_type,
        )

        post_search_by_keywords_response_200_output_posts_item_engagement_type_0.additional_properties = d
        return post_search_by_keywords_response_200_output_posts_item_engagement_type_0

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
