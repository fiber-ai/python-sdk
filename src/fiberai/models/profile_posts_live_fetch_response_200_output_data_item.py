from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_posts_live_fetch_response_200_output_data_item_author_type_0 import (
        ProfilePostsLiveFetchResponse200OutputDataItemAuthorType0,
    )
    from ..models.profile_posts_live_fetch_response_200_output_data_item_engagement_type_0 import (
        ProfilePostsLiveFetchResponse200OutputDataItemEngagementType0,
    )
    from ..models.profile_posts_live_fetch_response_200_output_data_item_posted_at_type_0 import (
        ProfilePostsLiveFetchResponse200OutputDataItemPostedAtType0,
    )
    from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0 import (
        ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0,
    )
    from ..models.profile_posts_live_fetch_response_200_output_data_item_video_type_0 import (
        ProfilePostsLiveFetchResponse200OutputDataItemVideoType0,
    )


T = TypeVar("T", bound="ProfilePostsLiveFetchResponse200OutputDataItem")


@_attrs_define
class ProfilePostsLiveFetchResponse200OutputDataItem:
    """
    Attributes:
        post_id (str):
        author (None | ProfilePostsLiveFetchResponse200OutputDataItemAuthorType0 | Unset):
        posted_at (None | ProfilePostsLiveFetchResponse200OutputDataItemPostedAtType0 | Unset):
        engagement (None | ProfilePostsLiveFetchResponse200OutputDataItemEngagementType0 | Unset):
        image_urls (list[str] | None | Unset):
        post_url (None | str | Unset):
        video (None | ProfilePostsLiveFetchResponse200OutputDataItemVideoType0 | Unset):
        caption (None | str | Unset):
        sub_text (None | str | Unset):
        reshared_post (None | ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0 | Unset):
    """

    post_id: str
    author: None | ProfilePostsLiveFetchResponse200OutputDataItemAuthorType0 | Unset = UNSET
    posted_at: None | ProfilePostsLiveFetchResponse200OutputDataItemPostedAtType0 | Unset = UNSET
    engagement: None | ProfilePostsLiveFetchResponse200OutputDataItemEngagementType0 | Unset = UNSET
    image_urls: list[str] | None | Unset = UNSET
    post_url: None | str | Unset = UNSET
    video: None | ProfilePostsLiveFetchResponse200OutputDataItemVideoType0 | Unset = UNSET
    caption: None | str | Unset = UNSET
    sub_text: None | str | Unset = UNSET
    reshared_post: None | ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_posts_live_fetch_response_200_output_data_item_author_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemAuthorType0,
        )
        from ..models.profile_posts_live_fetch_response_200_output_data_item_engagement_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemEngagementType0,
        )
        from ..models.profile_posts_live_fetch_response_200_output_data_item_posted_at_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemPostedAtType0,
        )
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0,
        )
        from ..models.profile_posts_live_fetch_response_200_output_data_item_video_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemVideoType0,
        )

        post_id = self.post_id

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, ProfilePostsLiveFetchResponse200OutputDataItemAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        posted_at: dict[str, Any] | None | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        elif isinstance(self.posted_at, ProfilePostsLiveFetchResponse200OutputDataItemPostedAtType0):
            posted_at = self.posted_at.to_dict()
        else:
            posted_at = self.posted_at

        engagement: dict[str, Any] | None | Unset
        if isinstance(self.engagement, Unset):
            engagement = UNSET
        elif isinstance(self.engagement, ProfilePostsLiveFetchResponse200OutputDataItemEngagementType0):
            engagement = self.engagement.to_dict()
        else:
            engagement = self.engagement

        image_urls: list[str] | None | Unset
        if isinstance(self.image_urls, Unset):
            image_urls = UNSET
        elif isinstance(self.image_urls, list):
            image_urls = self.image_urls

        else:
            image_urls = self.image_urls

        post_url: None | str | Unset
        if isinstance(self.post_url, Unset):
            post_url = UNSET
        else:
            post_url = self.post_url

        video: dict[str, Any] | None | Unset
        if isinstance(self.video, Unset):
            video = UNSET
        elif isinstance(self.video, ProfilePostsLiveFetchResponse200OutputDataItemVideoType0):
            video = self.video.to_dict()
        else:
            video = self.video

        caption: None | str | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        sub_text: None | str | Unset
        if isinstance(self.sub_text, Unset):
            sub_text = UNSET
        else:
            sub_text = self.sub_text

        reshared_post: dict[str, Any] | None | Unset
        if isinstance(self.reshared_post, Unset):
            reshared_post = UNSET
        elif isinstance(self.reshared_post, ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0):
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
        if author is not UNSET:
            field_dict["author"] = author
        if posted_at is not UNSET:
            field_dict["postedAt"] = posted_at
        if engagement is not UNSET:
            field_dict["engagement"] = engagement
        if image_urls is not UNSET:
            field_dict["imageUrls"] = image_urls
        if post_url is not UNSET:
            field_dict["postUrl"] = post_url
        if video is not UNSET:
            field_dict["video"] = video
        if caption is not UNSET:
            field_dict["caption"] = caption
        if sub_text is not UNSET:
            field_dict["subText"] = sub_text
        if reshared_post is not UNSET:
            field_dict["resharedPost"] = reshared_post

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_posts_live_fetch_response_200_output_data_item_author_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemAuthorType0,
        )
        from ..models.profile_posts_live_fetch_response_200_output_data_item_engagement_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemEngagementType0,
        )
        from ..models.profile_posts_live_fetch_response_200_output_data_item_posted_at_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemPostedAtType0,
        )
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0,
        )
        from ..models.profile_posts_live_fetch_response_200_output_data_item_video_type_0 import (
            ProfilePostsLiveFetchResponse200OutputDataItemVideoType0,
        )

        d = dict(src_dict)
        post_id = d.pop("postId")

        def _parse_author(data: object) -> None | ProfilePostsLiveFetchResponse200OutputDataItemAuthorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = ProfilePostsLiveFetchResponse200OutputDataItemAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfilePostsLiveFetchResponse200OutputDataItemAuthorType0 | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_posted_at(
            data: object,
        ) -> None | ProfilePostsLiveFetchResponse200OutputDataItemPostedAtType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                posted_at_type_0 = ProfilePostsLiveFetchResponse200OutputDataItemPostedAtType0.from_dict(data)

                return posted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfilePostsLiveFetchResponse200OutputDataItemPostedAtType0 | Unset, data)

        posted_at = _parse_posted_at(d.pop("postedAt", UNSET))

        def _parse_engagement(
            data: object,
        ) -> None | ProfilePostsLiveFetchResponse200OutputDataItemEngagementType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                engagement_type_0 = ProfilePostsLiveFetchResponse200OutputDataItemEngagementType0.from_dict(data)

                return engagement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfilePostsLiveFetchResponse200OutputDataItemEngagementType0 | Unset, data)

        engagement = _parse_engagement(d.pop("engagement", UNSET))

        def _parse_image_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_urls_type_0 = cast(list[str], data)

                return image_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_urls = _parse_image_urls(d.pop("imageUrls", UNSET))

        def _parse_post_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_url = _parse_post_url(d.pop("postUrl", UNSET))

        def _parse_video(data: object) -> None | ProfilePostsLiveFetchResponse200OutputDataItemVideoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_type_0 = ProfilePostsLiveFetchResponse200OutputDataItemVideoType0.from_dict(data)

                return video_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfilePostsLiveFetchResponse200OutputDataItemVideoType0 | Unset, data)

        video = _parse_video(d.pop("video", UNSET))

        def _parse_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))

        def _parse_sub_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_text = _parse_sub_text(d.pop("subText", UNSET))

        def _parse_reshared_post(
            data: object,
        ) -> None | ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reshared_post_type_0 = ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0.from_dict(data)

                return reshared_post_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0 | Unset, data)

        reshared_post = _parse_reshared_post(d.pop("resharedPost", UNSET))

        profile_posts_live_fetch_response_200_output_data_item = cls(
            post_id=post_id,
            author=author,
            posted_at=posted_at,
            engagement=engagement,
            image_urls=image_urls,
            post_url=post_url,
            video=video,
            caption=caption,
            sub_text=sub_text,
            reshared_post=reshared_post,
        )

        profile_posts_live_fetch_response_200_output_data_item.additional_properties = d
        return profile_posts_live_fetch_response_200_output_data_item

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
