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
  from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0_author_type_0 import ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0





T = TypeVar("T", bound="ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0")



@_attrs_define
class ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0:
    """ 
        Attributes:
            post_urn (Union[None, Unset, str]):
            post_url (Union[None, Unset, str]):
            author (Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0', None, Unset]):
     """

    post_urn: Union[None, Unset, str] = UNSET
    post_url: Union[None, Unset, str] = UNSET
    author: Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0_author_type_0 import ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0
        post_urn: Union[None, Unset, str]
        if isinstance(self.post_urn, Unset):
            post_urn = UNSET
        else:
            post_urn = self.post_urn

        post_url: Union[None, Unset, str]
        if isinstance(self.post_url, Unset):
            post_url = UNSET
        else:
            post_url = self.post_url

        author: Union[None, Unset, dict[str, Any]]
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if post_urn is not UNSET:
            field_dict["postUrn"] = post_urn
        if post_url is not UNSET:
            field_dict["postUrl"] = post_url
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0_author_type_0 import ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0
        d = dict(src_dict)
        def _parse_post_urn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post_urn = _parse_post_urn(d.pop("postUrn", UNSET))


        def _parse_post_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post_url = _parse_post_url(d.pop("postUrl", UNSET))


        def _parse_author(data: object) -> Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0.from_dict(data)



                return author_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfileCommentsLiveFetchResponse200OutputCommentsType0ItemPostType0AuthorType0', None, Unset], data)

        author = _parse_author(d.pop("author", UNSET))


        profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0 = cls(
            post_urn=post_urn,
            post_url=post_url,
            author=author,
        )


        profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0.additional_properties = d
        return profile_comments_live_fetch_response_200_output_comments_type_0_item_post_type_0

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
