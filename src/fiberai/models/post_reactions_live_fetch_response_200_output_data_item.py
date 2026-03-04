from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_reactions_live_fetch_response_200_output_data_item_reaction_type_type_1 import PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType1
from ..models.post_reactions_live_fetch_response_200_output_data_item_reaction_type_type_2_type_1 import PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType2Type1
from ..models.post_reactions_live_fetch_response_200_output_data_item_reaction_type_type_3_type_1 import PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.post_reactions_live_fetch_response_200_output_data_item_reactor_type_0 import PostReactionsLiveFetchResponse200OutputDataItemReactorType0





T = TypeVar("T", bound="PostReactionsLiveFetchResponse200OutputDataItem")



@_attrs_define
class PostReactionsLiveFetchResponse200OutputDataItem:
    """ 
        Attributes:
            reaction_type (Union[None, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType1,
                PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType2Type1,
                PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType3Type1, Unset]): One of LinkedIn's reaction
                types. These match the tooltips on each of LinkedIn's six reaction buttons; for instance, 'Like' is the blue
                thumbs-up.
            reactor (Union['PostReactionsLiveFetchResponse200OutputDataItemReactorType0', None, Unset]):
     """

    reaction_type: Union[None, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType1, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType2Type1, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType3Type1, Unset] = UNSET
    reactor: Union['PostReactionsLiveFetchResponse200OutputDataItemReactorType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_reactions_live_fetch_response_200_output_data_item_reactor_type_0 import PostReactionsLiveFetchResponse200OutputDataItemReactorType0
        reaction_type: Union[None, Unset, str]
        if isinstance(self.reaction_type, Unset):
            reaction_type = UNSET
        elif isinstance(self.reaction_type, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType1):
            reaction_type = self.reaction_type.value
        elif isinstance(self.reaction_type, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType2Type1):
            reaction_type = self.reaction_type.value
        elif isinstance(self.reaction_type, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType3Type1):
            reaction_type = self.reaction_type.value
        else:
            reaction_type = self.reaction_type

        reactor: Union[None, Unset, dict[str, Any]]
        if isinstance(self.reactor, Unset):
            reactor = UNSET
        elif isinstance(self.reactor, PostReactionsLiveFetchResponse200OutputDataItemReactorType0):
            reactor = self.reactor.to_dict()
        else:
            reactor = self.reactor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reaction_type is not UNSET:
            field_dict["reactionType"] = reaction_type
        if reactor is not UNSET:
            field_dict["reactor"] = reactor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_reactions_live_fetch_response_200_output_data_item_reactor_type_0 import PostReactionsLiveFetchResponse200OutputDataItemReactorType0
        d = dict(src_dict)
        def _parse_reaction_type(data: object) -> Union[None, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType1, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType2Type1, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reaction_type_type_1 = PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType1(data)



                return reaction_type_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reaction_type_type_2_type_1 = PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType2Type1(data)



                return reaction_type_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reaction_type_type_3_type_1 = PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType3Type1(data)



                return reaction_type_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[None, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType1, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType2Type1, PostReactionsLiveFetchResponse200OutputDataItemReactionTypeType3Type1, Unset], data)

        reaction_type = _parse_reaction_type(d.pop("reactionType", UNSET))


        def _parse_reactor(data: object) -> Union['PostReactionsLiveFetchResponse200OutputDataItemReactorType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reactor_type_0 = PostReactionsLiveFetchResponse200OutputDataItemReactorType0.from_dict(data)



                return reactor_type_0
            except: # noqa: E722
                pass
            return cast(Union['PostReactionsLiveFetchResponse200OutputDataItemReactorType0', None, Unset], data)

        reactor = _parse_reactor(d.pop("reactor", UNSET))


        post_reactions_live_fetch_response_200_output_data_item = cls(
            reaction_type=reaction_type,
            reactor=reactor,
        )


        post_reactions_live_fetch_response_200_output_data_item.additional_properties = d
        return post_reactions_live_fetch_response_200_output_data_item

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
