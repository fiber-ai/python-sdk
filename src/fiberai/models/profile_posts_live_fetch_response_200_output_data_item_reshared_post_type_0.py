from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_posted_at_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0PostedAtType0
  from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_video_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0
  from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_engagement_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0
  from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_author_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0AuthorType0





T = TypeVar("T", bound="ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0")



@_attrs_define
class ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0:
    """ 
        Attributes:
            post_id (str):
            author (Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0AuthorType0', None, Unset]):
            posted_at (Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0PostedAtType0', None, Unset]):
            engagement (Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0', None,
                Unset]):
            image_urls (Union[None, Unset, list[str]]):
            post_url (Union[None, Unset, str]):
            video (Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0', None, Unset]):
            caption (Union[None, Unset, str]):
            sub_text (Union[None, Unset, str]):
     """

    post_id: str
    author: Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0AuthorType0', None, Unset] = UNSET
    posted_at: Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0PostedAtType0', None, Unset] = UNSET
    engagement: Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0', None, Unset] = UNSET
    image_urls: Union[None, Unset, list[str]] = UNSET
    post_url: Union[None, Unset, str] = UNSET
    video: Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0', None, Unset] = UNSET
    caption: Union[None, Unset, str] = UNSET
    sub_text: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_posted_at_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0PostedAtType0
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_video_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_engagement_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_author_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0AuthorType0
        post_id = self.post_id

        author: Union[None, Unset, dict[str, Any]]
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0AuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        posted_at: Union[None, Unset, dict[str, Any]]
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        elif isinstance(self.posted_at, ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0PostedAtType0):
            posted_at = self.posted_at.to_dict()
        else:
            posted_at = self.posted_at

        engagement: Union[None, Unset, dict[str, Any]]
        if isinstance(self.engagement, Unset):
            engagement = UNSET
        elif isinstance(self.engagement, ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0):
            engagement = self.engagement.to_dict()
        else:
            engagement = self.engagement

        image_urls: Union[None, Unset, list[str]]
        if isinstance(self.image_urls, Unset):
            image_urls = UNSET
        elif isinstance(self.image_urls, list):
            image_urls = self.image_urls


        else:
            image_urls = self.image_urls

        post_url: Union[None, Unset, str]
        if isinstance(self.post_url, Unset):
            post_url = UNSET
        else:
            post_url = self.post_url

        video: Union[None, Unset, dict[str, Any]]
        if isinstance(self.video, Unset):
            video = UNSET
        elif isinstance(self.video, ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0):
            video = self.video.to_dict()
        else:
            video = self.video

        caption: Union[None, Unset, str]
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        sub_text: Union[None, Unset, str]
        if isinstance(self.sub_text, Unset):
            sub_text = UNSET
        else:
            sub_text = self.sub_text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "postId": post_id,
        })
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_posted_at_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0PostedAtType0
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_video_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_engagement_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0
        from ..models.profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0_author_type_0 import ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0AuthorType0
        d = dict(src_dict)
        post_id = d.pop("postId")

        def _parse_author(data: object) -> Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0AuthorType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0AuthorType0.from_dict(data)



                return author_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0AuthorType0', None, Unset], data)

        author = _parse_author(d.pop("author", UNSET))


        def _parse_posted_at(data: object) -> Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0PostedAtType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                posted_at_type_0 = ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0PostedAtType0.from_dict(data)



                return posted_at_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0PostedAtType0', None, Unset], data)

        posted_at = _parse_posted_at(d.pop("postedAt", UNSET))


        def _parse_engagement(data: object) -> Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                engagement_type_0 = ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0.from_dict(data)



                return engagement_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0', None, Unset], data)

        engagement = _parse_engagement(d.pop("engagement", UNSET))


        def _parse_image_urls(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_urls_type_0 = cast(list[str], data)

                return image_urls_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        image_urls = _parse_image_urls(d.pop("imageUrls", UNSET))


        def _parse_post_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post_url = _parse_post_url(d.pop("postUrl", UNSET))


        def _parse_video(data: object) -> Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_type_0 = ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0.from_dict(data)



                return video_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfilePostsLiveFetchResponse200OutputDataItemResharedPostType0VideoType0', None, Unset], data)

        video = _parse_video(d.pop("video", UNSET))


        def _parse_caption(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        caption = _parse_caption(d.pop("caption", UNSET))


        def _parse_sub_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sub_text = _parse_sub_text(d.pop("subText", UNSET))


        profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0 = cls(
            post_id=post_id,
            author=author,
            posted_at=posted_at,
            engagement=engagement,
            image_urls=image_urls,
            post_url=post_url,
            video=video,
            caption=caption,
            sub_text=sub_text,
        )


        profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0.additional_properties = d
        return profile_posts_live_fetch_response_200_output_data_item_reshared_post_type_0

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
