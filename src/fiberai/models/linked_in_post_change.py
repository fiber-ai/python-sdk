from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linked_in_post_change_post_type_type_1 import LinkedInPostChangePostTypeType1
from ..models.linked_in_post_change_post_type_type_2_type_1 import LinkedInPostChangePostTypeType2Type1
from ..models.linked_in_post_change_post_type_type_3_type_1 import LinkedInPostChangePostTypeType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linked_in_post_reshared_by import LinkedInPostResharedBy
    from ..models.linked_in_reshared_post import LinkedInResharedPost


T = TypeVar("T", bound="LinkedInPostChange")


@_attrs_define
class LinkedInPostChange:
    """
    Attributes:
        post_id (str): LinkedIn post ID
        post_url (None | str | Unset): URL to the post
        caption (None | str | Unset): Post content
        posted_at (None | str | Unset): ISO date when posted
        num_reactions (float | None | Unset): Number of reactions
        num_comments (float | None | Unset): Number of comments
        num_shares (float | None | Unset): Number of shares
        poster_name (None | str | Unset): Display name of the author of the post. When the tracked person or company
            reposted someone else's post, this is the original author.
        poster_slug (None | str | Unset): LinkedIn slug of the author of the post (e.g. 'williamhgates'). For a company
            author this can be the company's numeric LinkedIn id.
        poster_url (None | str | Unset): Full LinkedIn URL of the author of the post. A company page URL when the author
            is a company.
        poster_profile_picture (None | str | Unset): Profile picture URL of the author of the post
        matched_keywords (list[str] | None | Unset): Keywords from your tracking rule that this post matched. Omitted
            for rules without keywords.
        post_type (LinkedInPostChangePostTypeType1 | LinkedInPostChangePostTypeType2Type1 |
            LinkedInPostChangePostTypeType3Type1 | None | Unset): How the tracked person or company relates to this post.
            Null on signals created before repost detection was available.
        reshared_by (LinkedInPostResharedBy | None | Unset): The tracked person or company that reposted this post.
            Present only when the post was reposted without added commentary; the poster fields then describe the original
            author.
        reshared_post (LinkedInResharedPost | None | Unset): The post being quoted. Present only when the tracked person
            or company reposted with their own commentary; the poster fields and caption then describe that commentary.
    """

    post_id: str
    post_url: None | str | Unset = UNSET
    caption: None | str | Unset = UNSET
    posted_at: None | str | Unset = UNSET
    num_reactions: float | None | Unset = UNSET
    num_comments: float | None | Unset = UNSET
    num_shares: float | None | Unset = UNSET
    poster_name: None | str | Unset = UNSET
    poster_slug: None | str | Unset = UNSET
    poster_url: None | str | Unset = UNSET
    poster_profile_picture: None | str | Unset = UNSET
    matched_keywords: list[str] | None | Unset = UNSET
    post_type: (
        LinkedInPostChangePostTypeType1
        | LinkedInPostChangePostTypeType2Type1
        | LinkedInPostChangePostTypeType3Type1
        | None
        | Unset
    ) = UNSET
    reshared_by: LinkedInPostResharedBy | None | Unset = UNSET
    reshared_post: LinkedInResharedPost | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.linked_in_post_reshared_by import LinkedInPostResharedBy  # noqa: PLC0415
        from ..models.linked_in_reshared_post import LinkedInResharedPost  # noqa: PLC0415

        post_id = self.post_id

        post_url: None | str | Unset
        if isinstance(self.post_url, Unset):
            post_url = UNSET
        else:
            post_url = self.post_url

        caption: None | str | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        posted_at: None | str | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        else:
            posted_at = self.posted_at

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

        num_shares: float | None | Unset
        if isinstance(self.num_shares, Unset):
            num_shares = UNSET
        else:
            num_shares = self.num_shares

        poster_name: None | str | Unset
        if isinstance(self.poster_name, Unset):
            poster_name = UNSET
        else:
            poster_name = self.poster_name

        poster_slug: None | str | Unset
        if isinstance(self.poster_slug, Unset):
            poster_slug = UNSET
        else:
            poster_slug = self.poster_slug

        poster_url: None | str | Unset
        if isinstance(self.poster_url, Unset):
            poster_url = UNSET
        else:
            poster_url = self.poster_url

        poster_profile_picture: None | str | Unset
        if isinstance(self.poster_profile_picture, Unset):
            poster_profile_picture = UNSET
        else:
            poster_profile_picture = self.poster_profile_picture

        matched_keywords: list[str] | None | Unset
        if isinstance(self.matched_keywords, Unset):
            matched_keywords = UNSET
        elif isinstance(self.matched_keywords, list):
            matched_keywords = self.matched_keywords

        else:
            matched_keywords = self.matched_keywords

        post_type: None | str | Unset
        if isinstance(self.post_type, Unset):
            post_type = UNSET
        elif isinstance(self.post_type, LinkedInPostChangePostTypeType1):
            post_type = self.post_type.value
        elif isinstance(self.post_type, LinkedInPostChangePostTypeType2Type1):
            post_type = self.post_type.value
        elif isinstance(self.post_type, LinkedInPostChangePostTypeType3Type1):
            post_type = self.post_type.value
        else:
            post_type = self.post_type

        reshared_by: dict[str, Any] | None | Unset
        if isinstance(self.reshared_by, Unset):
            reshared_by = UNSET
        elif isinstance(self.reshared_by, LinkedInPostResharedBy):
            reshared_by = self.reshared_by.to_dict()
        else:
            reshared_by = self.reshared_by

        reshared_post: dict[str, Any] | None | Unset
        if isinstance(self.reshared_post, Unset):
            reshared_post = UNSET
        elif isinstance(self.reshared_post, LinkedInResharedPost):
            reshared_post = self.reshared_post.to_dict()
        else:
            reshared_post = self.reshared_post

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "postId": post_id,
            }
        )
        if post_url is not UNSET:
            field_dict["postUrl"] = post_url
        if caption is not UNSET:
            field_dict["caption"] = caption
        if posted_at is not UNSET:
            field_dict["postedAt"] = posted_at
        if num_reactions is not UNSET:
            field_dict["numReactions"] = num_reactions
        if num_comments is not UNSET:
            field_dict["numComments"] = num_comments
        if num_shares is not UNSET:
            field_dict["numShares"] = num_shares
        if poster_name is not UNSET:
            field_dict["posterName"] = poster_name
        if poster_slug is not UNSET:
            field_dict["posterSlug"] = poster_slug
        if poster_url is not UNSET:
            field_dict["posterUrl"] = poster_url
        if poster_profile_picture is not UNSET:
            field_dict["posterProfilePicture"] = poster_profile_picture
        if matched_keywords is not UNSET:
            field_dict["matchedKeywords"] = matched_keywords
        if post_type is not UNSET:
            field_dict["postType"] = post_type
        if reshared_by is not UNSET:
            field_dict["resharedBy"] = reshared_by
        if reshared_post is not UNSET:
            field_dict["resharedPost"] = reshared_post

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_in_post_reshared_by import LinkedInPostResharedBy  # noqa: PLC0415
        from ..models.linked_in_reshared_post import LinkedInResharedPost  # noqa: PLC0415

        d = dict(src_dict)
        post_id = d.pop("postId")

        def _parse_post_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_url = _parse_post_url(d.pop("postUrl", UNSET))

        def _parse_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))

        def _parse_posted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        posted_at = _parse_posted_at(d.pop("postedAt", UNSET))

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

        def _parse_num_shares(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_shares = _parse_num_shares(d.pop("numShares", UNSET))

        def _parse_poster_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_name = _parse_poster_name(d.pop("posterName", UNSET))

        def _parse_poster_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_slug = _parse_poster_slug(d.pop("posterSlug", UNSET))

        def _parse_poster_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_url = _parse_poster_url(d.pop("posterUrl", UNSET))

        def _parse_poster_profile_picture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poster_profile_picture = _parse_poster_profile_picture(d.pop("posterProfilePicture", UNSET))

        def _parse_matched_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                matched_keywords_type_0 = cast(list[str], data)

                return matched_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        matched_keywords = _parse_matched_keywords(d.pop("matchedKeywords", UNSET))

        def _parse_post_type(
            data: object,
        ) -> (
            LinkedInPostChangePostTypeType1
            | LinkedInPostChangePostTypeType2Type1
            | LinkedInPostChangePostTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                post_type_type_1 = LinkedInPostChangePostTypeType1(data)

                return post_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                post_type_type_2_type_1 = LinkedInPostChangePostTypeType2Type1(data)

                return post_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                post_type_type_3_type_1 = LinkedInPostChangePostTypeType3Type1(data)

                return post_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LinkedInPostChangePostTypeType1
                | LinkedInPostChangePostTypeType2Type1
                | LinkedInPostChangePostTypeType3Type1
                | None
                | Unset,
                data,
            )

        post_type = _parse_post_type(d.pop("postType", UNSET))

        def _parse_reshared_by(data: object) -> LinkedInPostResharedBy | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reshared_by_type_0 = LinkedInPostResharedBy.from_dict(data)

                return reshared_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinkedInPostResharedBy | None | Unset, data)

        reshared_by = _parse_reshared_by(d.pop("resharedBy", UNSET))

        def _parse_reshared_post(data: object) -> LinkedInResharedPost | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reshared_post_type_0 = LinkedInResharedPost.from_dict(data)

                return reshared_post_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LinkedInResharedPost | None | Unset, data)

        reshared_post = _parse_reshared_post(d.pop("resharedPost", UNSET))

        linked_in_post_change = cls(
            post_id=post_id,
            post_url=post_url,
            caption=caption,
            posted_at=posted_at,
            num_reactions=num_reactions,
            num_comments=num_comments,
            num_shares=num_shares,
            poster_name=poster_name,
            poster_slug=poster_slug,
            poster_url=poster_url,
            poster_profile_picture=poster_profile_picture,
            matched_keywords=matched_keywords,
            post_type=post_type,
            reshared_by=reshared_by,
            reshared_post=reshared_post,
        )

        linked_in_post_change.additional_properties = d
        return linked_in_post_change

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
