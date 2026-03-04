from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_type_type_1 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1
from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_type_type_2_type_1 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1
from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_type_type_3_type_1 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_reactor_type_0 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0
  from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0
  from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0





T = TypeVar("T", bound="ProfileReactionsLiveFetchResponse200OutputReactionsType0Item")



@_attrs_define
class ProfileReactionsLiveFetchResponse200OutputReactionsType0Item:
    """ 
        Attributes:
            reaction_id (Union[None, Unset, str]):
            type_ (Union[None, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1,
                ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1,
                ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1, Unset]): One of LinkedIn's reaction
                types. These match the tooltips on each of LinkedIn's six reaction buttons; for instance, 'Like' is the blue
                thumbs-up.
            target (Union[None, Unset, str]):
            reacted_ago (Union[None, Unset, str]):
            reactor (Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0', None, Unset]):
            post (Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0', None, Unset]):
            comment (Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0', None, Unset]):
     """

    reaction_id: Union[None, Unset, str] = UNSET
    type_: Union[None, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1, Unset] = UNSET
    target: Union[None, Unset, str] = UNSET
    reacted_ago: Union[None, Unset, str] = UNSET
    reactor: Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0', None, Unset] = UNSET
    post: Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0', None, Unset] = UNSET
    comment: Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_reactor_type_0 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0
        reaction_id: Union[None, Unset, str]
        if isinstance(self.reaction_id, Unset):
            reaction_id = UNSET
        else:
            reaction_id = self.reaction_id

        type_: Union[None, Unset, str]
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

        target: Union[None, Unset, str]
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target

        reacted_ago: Union[None, Unset, str]
        if isinstance(self.reacted_ago, Unset):
            reacted_ago = UNSET
        else:
            reacted_ago = self.reacted_ago

        reactor: Union[None, Unset, dict[str, Any]]
        if isinstance(self.reactor, Unset):
            reactor = UNSET
        elif isinstance(self.reactor, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0):
            reactor = self.reactor.to_dict()
        else:
            reactor = self.reactor

        post: Union[None, Unset, dict[str, Any]]
        if isinstance(self.post, Unset):
            post = UNSET
        elif isinstance(self.post, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0):
            post = self.post.to_dict()
        else:
            post = self.post

        comment: Union[None, Unset, dict[str, Any]]
        if isinstance(self.comment, Unset):
            comment = UNSET
        elif isinstance(self.comment, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0):
            comment = self.comment.to_dict()
        else:
            comment = self.comment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_reactor_type_0 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0 import ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0
        d = dict(src_dict)
        def _parse_reaction_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reaction_id = _parse_reaction_id(d.pop("reactionId", UNSET))


        def _parse_type_(data: object) -> Union[None, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1(data)



                return type_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1(data)



                return type_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1(data)



                return type_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[None, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType1, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType3Type1, Unset], data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_target(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        target = _parse_target(d.pop("target", UNSET))


        def _parse_reacted_ago(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reacted_ago = _parse_reacted_ago(d.pop("reactedAgo", UNSET))


        def _parse_reactor(data: object) -> Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reactor_type_0 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0.from_dict(data)



                return reactor_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemReactorType0', None, Unset], data)

        reactor = _parse_reactor(d.pop("reactor", UNSET))


        def _parse_post(data: object) -> Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                post_type_0 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0.from_dict(data)



                return post_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0', None, Unset], data)

        post = _parse_post(d.pop("post", UNSET))


        def _parse_comment(data: object) -> Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                comment_type_0 = ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0.from_dict(data)



                return comment_type_0
            except: # noqa: E722
                pass
            return cast(Union['ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0', None, Unset], data)

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
