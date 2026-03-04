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
  from ..models.post_comments_live_fetch_response_200_output_data_item_comments_type_0_item_reactions_by_type_type_0_item import PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemReactionsByTypeType0Item
  from ..models.post_comments_live_fetch_response_200_output_data_item_comments_type_0_item_commenter_type_0 import PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemCommenterType0





T = TypeVar("T", bound="PostCommentsLiveFetchResponse200OutputDataItemCommentsType0Item")



@_attrs_define
class PostCommentsLiveFetchResponse200OutputDataItemCommentsType0Item:
    """ 
        Attributes:
            commentary (Union[None, Unset, str]):
            commenter (Union['PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemCommenterType0', None, Unset]):
            num_reactions (Union[None, Unset, float]):
            num_comments (Union[None, Unset, float]):
            reactions_by_type (Union[None, Unset,
                list['PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemReactionsByTypeType0Item']]):
            created_at (Union[None, Unset, str]):
     """

    commentary: Union[None, Unset, str] = UNSET
    commenter: Union['PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemCommenterType0', None, Unset] = UNSET
    num_reactions: Union[None, Unset, float] = UNSET
    num_comments: Union[None, Unset, float] = UNSET
    reactions_by_type: Union[None, Unset, list['PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemReactionsByTypeType0Item']] = UNSET
    created_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_comments_live_fetch_response_200_output_data_item_comments_type_0_item_reactions_by_type_type_0_item import PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemReactionsByTypeType0Item
        from ..models.post_comments_live_fetch_response_200_output_data_item_comments_type_0_item_commenter_type_0 import PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemCommenterType0
        commentary: Union[None, Unset, str]
        if isinstance(self.commentary, Unset):
            commentary = UNSET
        else:
            commentary = self.commentary

        commenter: Union[None, Unset, dict[str, Any]]
        if isinstance(self.commenter, Unset):
            commenter = UNSET
        elif isinstance(self.commenter, PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemCommenterType0):
            commenter = self.commenter.to_dict()
        else:
            commenter = self.commenter

        num_reactions: Union[None, Unset, float]
        if isinstance(self.num_reactions, Unset):
            num_reactions = UNSET
        else:
            num_reactions = self.num_reactions

        num_comments: Union[None, Unset, float]
        if isinstance(self.num_comments, Unset):
            num_comments = UNSET
        else:
            num_comments = self.num_comments

        reactions_by_type: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.reactions_by_type, Unset):
            reactions_by_type = UNSET
        elif isinstance(self.reactions_by_type, list):
            reactions_by_type = []
            for reactions_by_type_type_0_item_data in self.reactions_by_type:
                reactions_by_type_type_0_item = reactions_by_type_type_0_item_data.to_dict()
                reactions_by_type.append(reactions_by_type_type_0_item)


        else:
            reactions_by_type = self.reactions_by_type

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_comments_live_fetch_response_200_output_data_item_comments_type_0_item_reactions_by_type_type_0_item import PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemReactionsByTypeType0Item
        from ..models.post_comments_live_fetch_response_200_output_data_item_comments_type_0_item_commenter_type_0 import PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemCommenterType0
        d = dict(src_dict)
        def _parse_commentary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        commentary = _parse_commentary(d.pop("commentary", UNSET))


        def _parse_commenter(data: object) -> Union['PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemCommenterType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                commenter_type_0 = PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemCommenterType0.from_dict(data)



                return commenter_type_0
            except: # noqa: E722
                pass
            return cast(Union['PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemCommenterType0', None, Unset], data)

        commenter = _parse_commenter(d.pop("commenter", UNSET))


        def _parse_num_reactions(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        num_reactions = _parse_num_reactions(d.pop("numReactions", UNSET))


        def _parse_num_comments(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        num_comments = _parse_num_comments(d.pop("numComments", UNSET))


        def _parse_reactions_by_type(data: object) -> Union[None, Unset, list['PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemReactionsByTypeType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reactions_by_type_type_0 = []
                _reactions_by_type_type_0 = data
                for reactions_by_type_type_0_item_data in (_reactions_by_type_type_0):
                    reactions_by_type_type_0_item = PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemReactionsByTypeType0Item.from_dict(reactions_by_type_type_0_item_data)



                    reactions_by_type_type_0.append(reactions_by_type_type_0_item)

                return reactions_by_type_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemReactionsByTypeType0Item']], data)

        reactions_by_type = _parse_reactions_by_type(d.pop("reactionsByType", UNSET))


        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        post_comments_live_fetch_response_200_output_data_item_comments_type_0_item = cls(
            commentary=commentary,
            commenter=commenter,
            num_reactions=num_reactions,
            num_comments=num_comments,
            reactions_by_type=reactions_by_type,
            created_at=created_at,
        )


        post_comments_live_fetch_response_200_output_data_item_comments_type_0_item.additional_properties = d
        return post_comments_live_fetch_response_200_output_data_item_comments_type_0_item

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
