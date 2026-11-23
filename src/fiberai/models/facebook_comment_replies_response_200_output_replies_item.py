from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.facebook_comment_replies_response_200_output_replies_item_author_type_0 import (
        FacebookCommentRepliesResponse200OutputRepliesItemAuthorType0,
    )


T = TypeVar("T", bound="FacebookCommentRepliesResponse200OutputRepliesItem")


@_attrs_define
class FacebookCommentRepliesResponse200OutputRepliesItem:
    """
    Attributes:
        id (str): Unique comment ID.
        text (None | str | Unset): Comment text.
        author (FacebookCommentRepliesResponse200OutputRepliesItemAuthorType0 | None | Unset): Author of the comment.
        reaction_count (float | None | Unset): Number of reactions on the comment.
        reply_count (float | None | Unset): Number of replies to the comment.
        feedback_id (None | str | Unset): Feedback ID of the comment. Pass as `feedbackId` (with `expansionToken`) when
            fetching this comment's replies.
        expansion_token (None | str | Unset): Expansion token of the comment. Pass as `expansionToken` (with
            `feedbackId`) when fetching this comment's replies.
    """

    id: str
    text: None | str | Unset = UNSET
    author: FacebookCommentRepliesResponse200OutputRepliesItemAuthorType0 | None | Unset = UNSET
    reaction_count: float | None | Unset = UNSET
    reply_count: float | None | Unset = UNSET
    feedback_id: None | str | Unset = UNSET
    expansion_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.facebook_comment_replies_response_200_output_replies_item_author_type_0 import (
            FacebookCommentRepliesResponse200OutputRepliesItemAuthorType0,  # noqa: PLC0415
        )

        id = self.id

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, FacebookCommentRepliesResponse200OutputRepliesItemAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        reaction_count: float | None | Unset
        if isinstance(self.reaction_count, Unset):
            reaction_count = UNSET
        else:
            reaction_count = self.reaction_count

        reply_count: float | None | Unset
        if isinstance(self.reply_count, Unset):
            reply_count = UNSET
        else:
            reply_count = self.reply_count

        feedback_id: None | str | Unset
        if isinstance(self.feedback_id, Unset):
            feedback_id = UNSET
        else:
            feedback_id = self.feedback_id

        expansion_token: None | str | Unset
        if isinstance(self.expansion_token, Unset):
            expansion_token = UNSET
        else:
            expansion_token = self.expansion_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if author is not UNSET:
            field_dict["author"] = author
        if reaction_count is not UNSET:
            field_dict["reactionCount"] = reaction_count
        if reply_count is not UNSET:
            field_dict["replyCount"] = reply_count
        if feedback_id is not UNSET:
            field_dict["feedbackId"] = feedback_id
        if expansion_token is not UNSET:
            field_dict["expansionToken"] = expansion_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.facebook_comment_replies_response_200_output_replies_item_author_type_0 import (
            FacebookCommentRepliesResponse200OutputRepliesItemAuthorType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_author(data: object) -> FacebookCommentRepliesResponse200OutputRepliesItemAuthorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = FacebookCommentRepliesResponse200OutputRepliesItemAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FacebookCommentRepliesResponse200OutputRepliesItemAuthorType0 | None | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_reaction_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        reaction_count = _parse_reaction_count(d.pop("reactionCount", UNSET))

        def _parse_reply_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        reply_count = _parse_reply_count(d.pop("replyCount", UNSET))

        def _parse_feedback_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feedback_id = _parse_feedback_id(d.pop("feedbackId", UNSET))

        def _parse_expansion_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expansion_token = _parse_expansion_token(d.pop("expansionToken", UNSET))

        facebook_comment_replies_response_200_output_replies_item = cls(
            id=id,
            text=text,
            author=author,
            reaction_count=reaction_count,
            reply_count=reply_count,
            feedback_id=feedback_id,
            expansion_token=expansion_token,
        )

        facebook_comment_replies_response_200_output_replies_item.additional_properties = d
        return facebook_comment_replies_response_200_output_replies_item

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
