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
  from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0 import ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0
  from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_commenter_type_0 import ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0





T = TypeVar("T", bound="ProfileCommentsLiveFetchResponse200OutputCommentsType0Item")



@_attrs_define
class ProfileCommentsLiveFetchResponse200OutputCommentsType0Item:
    """ 
        Attributes:
            comment_id (Union[None, Unset, str]):
            content (Union[None, Unset, str]):
            commented_ago (Union[None, Unset, str]):
            commenter (Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0', None, Unset]):
            post (Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0', None, Unset]):
     """

    comment_id: Union[None, Unset, str] = UNSET
    content: Union[None, Unset, str] = UNSET
    commented_ago: Union[None, Unset, str] = UNSET
    commenter: Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0', None, Unset] = UNSET
    post: Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0 import ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_commenter_type_0 import ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0
        comment_id: Union[None, Unset, str]
        if isinstance(self.comment_id, Unset):
            comment_id = UNSET
        else:
            comment_id = self.comment_id

        content: Union[None, Unset, str]
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        commented_ago: Union[None, Unset, str]
        if isinstance(self.commented_ago, Unset):
            commented_ago = UNSET
        else:
            commented_ago = self.commented_ago

        commenter: Union[None, Unset, dict[str, Any]]
        if isinstance(self.commenter, Unset):
            commenter = UNSET
        elif isinstance(self.commenter, ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0):
            commenter = self.commenter.to_dict()
        else:
            commenter = self.commenter

        post: Union[None, Unset, dict[str, Any]]
        if isinstance(self.post, Unset):
            post = UNSET
        elif isinstance(self.post, ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0):
            post = self.post.to_dict()
        else:
            post = self.post


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comment_id is not UNSET:
            field_dict["commentId"] = comment_id
        if content is not UNSET:
            field_dict["content"] = content
        if commented_ago is not UNSET:
            field_dict["commentedAgo"] = commented_ago
        if commenter is not UNSET:
            field_dict["commenter"] = commenter
        if post is not UNSET:
            field_dict["post"] = post

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0 import ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_commenter_type_0 import ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0
        d = dict(src_dict)
        def _parse_comment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment_id = _parse_comment_id(d.pop("commentId", UNSET))


        def _parse_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content = _parse_content(d.pop("content", UNSET))


        def _parse_commented_ago(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        commented_ago = _parse_commented_ago(d.pop("commentedAgo", UNSET))


        def _parse_commenter(data: object) -> Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                commenter_type_0 = ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0.from_dict(data)



                return commenter_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemCommenterType0', None, Unset], data)

        commenter = _parse_commenter(d.pop("commenter", UNSET))


        def _parse_post(data: object) -> Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                post_type_0 = ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0.from_dict(data)



                return post_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0', None, Unset], data)

        post = _parse_post(d.pop("post", UNSET))


        profile_comments_live_fetch_response_200_output_comments_type_0_item = cls(
            comment_id=comment_id,
            content=content,
            commented_ago=commented_ago,
            commenter=commenter,
            post=post,
        )


        profile_comments_live_fetch_response_200_output_comments_type_0_item.additional_properties = d
        return profile_comments_live_fetch_response_200_output_comments_type_0_item

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
