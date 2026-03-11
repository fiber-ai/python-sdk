from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_search_by_keywords_response_200_output_posts_item_article_type_0 import (
        PostSearchByKeywordsResponse200OutputPostsItemArticleType0,
    )
    from ..models.post_search_by_keywords_response_200_output_posts_item_author_type_0 import (
        PostSearchByKeywordsResponse200OutputPostsItemAuthorType0,
    )
    from ..models.post_search_by_keywords_response_200_output_posts_item_engagement_type_0 import (
        PostSearchByKeywordsResponse200OutputPostsItemEngagementType0,
    )
    from ..models.post_search_by_keywords_response_200_output_posts_item_original_post_type_0 import (
        PostSearchByKeywordsResponse200OutputPostsItemOriginalPostType0,
    )
    from ..models.post_search_by_keywords_response_200_output_posts_item_reshared_by_type_0 import (
        PostSearchByKeywordsResponse200OutputPostsItemResharedByType0,
    )
    from ..models.post_search_by_keywords_response_200_output_posts_item_video_type_0 import (
        PostSearchByKeywordsResponse200OutputPostsItemVideoType0,
    )


T = TypeVar("T", bound="PostSearchByKeywordsResponse200OutputPostsItem")


@_attrs_define
class PostSearchByKeywordsResponse200OutputPostsItem:
    """
    Attributes:
        post_id (str):
        content (None | str | Unset):
        post_url (None | str | Unset):
        author (None | PostSearchByKeywordsResponse200OutputPostsItemAuthorType0 | Unset):
        published_at (None | str | Unset):
        image_urls (list[str] | None | Unset):
        video (None | PostSearchByKeywordsResponse200OutputPostsItemVideoType0 | Unset):
        article (None | PostSearchByKeywordsResponse200OutputPostsItemArticleType0 | Unset):
        original_post_id (None | str | Unset):
        original_post (None | PostSearchByKeywordsResponse200OutputPostsItemOriginalPostType0 | Unset):
        reshared_by (None | PostSearchByKeywordsResponse200OutputPostsItemResharedByType0 | Unset):
        newsletter_url (None | str | Unset):
        newsletter_title (None | str | Unset):
        engagement (None | PostSearchByKeywordsResponse200OutputPostsItemEngagementType0 | Unset):
    """

    post_id: str
    content: None | str | Unset = UNSET
    post_url: None | str | Unset = UNSET
    author: None | PostSearchByKeywordsResponse200OutputPostsItemAuthorType0 | Unset = UNSET
    published_at: None | str | Unset = UNSET
    image_urls: list[str] | None | Unset = UNSET
    video: None | PostSearchByKeywordsResponse200OutputPostsItemVideoType0 | Unset = UNSET
    article: None | PostSearchByKeywordsResponse200OutputPostsItemArticleType0 | Unset = UNSET
    original_post_id: None | str | Unset = UNSET
    original_post: None | PostSearchByKeywordsResponse200OutputPostsItemOriginalPostType0 | Unset = UNSET
    reshared_by: None | PostSearchByKeywordsResponse200OutputPostsItemResharedByType0 | Unset = UNSET
    newsletter_url: None | str | Unset = UNSET
    newsletter_title: None | str | Unset = UNSET
    engagement: None | PostSearchByKeywordsResponse200OutputPostsItemEngagementType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_search_by_keywords_response_200_output_posts_item_article_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemArticleType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_author_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemAuthorType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_engagement_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemEngagementType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_original_post_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemOriginalPostType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_reshared_by_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemResharedByType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_video_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemVideoType0,
        )

        post_id = self.post_id

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        post_url: None | str | Unset
        if isinstance(self.post_url, Unset):
            post_url = UNSET
        else:
            post_url = self.post_url

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, PostSearchByKeywordsResponse200OutputPostsItemAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        else:
            published_at = self.published_at

        image_urls: list[str] | None | Unset
        if isinstance(self.image_urls, Unset):
            image_urls = UNSET
        elif isinstance(self.image_urls, list):
            image_urls = self.image_urls

        else:
            image_urls = self.image_urls

        video: dict[str, Any] | None | Unset
        if isinstance(self.video, Unset):
            video = UNSET
        elif isinstance(self.video, PostSearchByKeywordsResponse200OutputPostsItemVideoType0):
            video = self.video.to_dict()
        else:
            video = self.video

        article: dict[str, Any] | None | Unset
        if isinstance(self.article, Unset):
            article = UNSET
        elif isinstance(self.article, PostSearchByKeywordsResponse200OutputPostsItemArticleType0):
            article = self.article.to_dict()
        else:
            article = self.article

        original_post_id: None | str | Unset
        if isinstance(self.original_post_id, Unset):
            original_post_id = UNSET
        else:
            original_post_id = self.original_post_id

        original_post: dict[str, Any] | None | Unset
        if isinstance(self.original_post, Unset):
            original_post = UNSET
        elif isinstance(self.original_post, PostSearchByKeywordsResponse200OutputPostsItemOriginalPostType0):
            original_post = self.original_post.to_dict()
        else:
            original_post = self.original_post

        reshared_by: dict[str, Any] | None | Unset
        if isinstance(self.reshared_by, Unset):
            reshared_by = UNSET
        elif isinstance(self.reshared_by, PostSearchByKeywordsResponse200OutputPostsItemResharedByType0):
            reshared_by = self.reshared_by.to_dict()
        else:
            reshared_by = self.reshared_by

        newsletter_url: None | str | Unset
        if isinstance(self.newsletter_url, Unset):
            newsletter_url = UNSET
        else:
            newsletter_url = self.newsletter_url

        newsletter_title: None | str | Unset
        if isinstance(self.newsletter_title, Unset):
            newsletter_title = UNSET
        else:
            newsletter_title = self.newsletter_title

        engagement: dict[str, Any] | None | Unset
        if isinstance(self.engagement, Unset):
            engagement = UNSET
        elif isinstance(self.engagement, PostSearchByKeywordsResponse200OutputPostsItemEngagementType0):
            engagement = self.engagement.to_dict()
        else:
            engagement = self.engagement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "postId": post_id,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if post_url is not UNSET:
            field_dict["postUrl"] = post_url
        if author is not UNSET:
            field_dict["author"] = author
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if image_urls is not UNSET:
            field_dict["imageUrls"] = image_urls
        if video is not UNSET:
            field_dict["video"] = video
        if article is not UNSET:
            field_dict["article"] = article
        if original_post_id is not UNSET:
            field_dict["originalPostId"] = original_post_id
        if original_post is not UNSET:
            field_dict["originalPost"] = original_post
        if reshared_by is not UNSET:
            field_dict["resharedBy"] = reshared_by
        if newsletter_url is not UNSET:
            field_dict["newsletterUrl"] = newsletter_url
        if newsletter_title is not UNSET:
            field_dict["newsletterTitle"] = newsletter_title
        if engagement is not UNSET:
            field_dict["engagement"] = engagement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_search_by_keywords_response_200_output_posts_item_article_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemArticleType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_author_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemAuthorType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_engagement_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemEngagementType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_original_post_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemOriginalPostType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_reshared_by_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemResharedByType0,
        )
        from ..models.post_search_by_keywords_response_200_output_posts_item_video_type_0 import (
            PostSearchByKeywordsResponse200OutputPostsItemVideoType0,
        )

        d = dict(src_dict)
        post_id = d.pop("postId")

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_post_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_url = _parse_post_url(d.pop("postUrl", UNSET))

        def _parse_author(data: object) -> None | PostSearchByKeywordsResponse200OutputPostsItemAuthorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = PostSearchByKeywordsResponse200OutputPostsItemAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostSearchByKeywordsResponse200OutputPostsItemAuthorType0 | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_published_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))

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

        def _parse_video(data: object) -> None | PostSearchByKeywordsResponse200OutputPostsItemVideoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_type_0 = PostSearchByKeywordsResponse200OutputPostsItemVideoType0.from_dict(data)

                return video_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostSearchByKeywordsResponse200OutputPostsItemVideoType0 | Unset, data)

        video = _parse_video(d.pop("video", UNSET))

        def _parse_article(data: object) -> None | PostSearchByKeywordsResponse200OutputPostsItemArticleType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                article_type_0 = PostSearchByKeywordsResponse200OutputPostsItemArticleType0.from_dict(data)

                return article_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostSearchByKeywordsResponse200OutputPostsItemArticleType0 | Unset, data)

        article = _parse_article(d.pop("article", UNSET))

        def _parse_original_post_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_post_id = _parse_original_post_id(d.pop("originalPostId", UNSET))

        def _parse_original_post(
            data: object,
        ) -> None | PostSearchByKeywordsResponse200OutputPostsItemOriginalPostType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                original_post_type_0 = PostSearchByKeywordsResponse200OutputPostsItemOriginalPostType0.from_dict(data)

                return original_post_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostSearchByKeywordsResponse200OutputPostsItemOriginalPostType0 | Unset, data)

        original_post = _parse_original_post(d.pop("originalPost", UNSET))

        def _parse_reshared_by(
            data: object,
        ) -> None | PostSearchByKeywordsResponse200OutputPostsItemResharedByType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reshared_by_type_0 = PostSearchByKeywordsResponse200OutputPostsItemResharedByType0.from_dict(data)

                return reshared_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostSearchByKeywordsResponse200OutputPostsItemResharedByType0 | Unset, data)

        reshared_by = _parse_reshared_by(d.pop("resharedBy", UNSET))

        def _parse_newsletter_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        newsletter_url = _parse_newsletter_url(d.pop("newsletterUrl", UNSET))

        def _parse_newsletter_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        newsletter_title = _parse_newsletter_title(d.pop("newsletterTitle", UNSET))

        def _parse_engagement(
            data: object,
        ) -> None | PostSearchByKeywordsResponse200OutputPostsItemEngagementType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                engagement_type_0 = PostSearchByKeywordsResponse200OutputPostsItemEngagementType0.from_dict(data)

                return engagement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostSearchByKeywordsResponse200OutputPostsItemEngagementType0 | Unset, data)

        engagement = _parse_engagement(d.pop("engagement", UNSET))

        post_search_by_keywords_response_200_output_posts_item = cls(
            post_id=post_id,
            content=content,
            post_url=post_url,
            author=author,
            published_at=published_at,
            image_urls=image_urls,
            video=video,
            article=article,
            original_post_id=original_post_id,
            original_post=original_post,
            reshared_by=reshared_by,
            newsletter_url=newsletter_url,
            newsletter_title=newsletter_title,
            engagement=engagement,
        )

        post_search_by_keywords_response_200_output_posts_item.additional_properties = d
        return post_search_by_keywords_response_200_output_posts_item

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
