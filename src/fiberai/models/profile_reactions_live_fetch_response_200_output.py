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
  from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item import ProfileReactionsLiveFetchResponse200OutputReactionsType0Item





T = TypeVar("T", bound="ProfileReactionsLiveFetchResponse200Output")



@_attrs_define
class ProfileReactionsLiveFetchResponse200Output:
    """ 
        Attributes:
            reactions (Union[None, Unset, list['ProfileReactionsLiveFetchResponse200OutputReactionsType0Item']]):
            cursor (Union[None, Unset, str]):
     """

    reactions: Union[None, Unset, list['ProfileReactionsLiveFetchResponse200OutputReactionsType0Item']] = UNSET
    cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item import ProfileReactionsLiveFetchResponse200OutputReactionsType0Item
        reactions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.reactions, Unset):
            reactions = UNSET
        elif isinstance(self.reactions, list):
            reactions = []
            for reactions_type_0_item_data in self.reactions:
                reactions_type_0_item = reactions_type_0_item_data.to_dict()
                reactions.append(reactions_type_0_item)


        else:
            reactions = self.reactions

        cursor: Union[None, Unset, str]
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item import ProfileReactionsLiveFetchResponse200OutputReactionsType0Item
        d = dict(src_dict)
        def _parse_reactions(data: object) -> Union[None, Unset, list['ProfileReactionsLiveFetchResponse200OutputReactionsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reactions_type_0 = []
                _reactions_type_0 = data
                for reactions_type_0_item_data in (_reactions_type_0):
                    reactions_type_0_item = ProfileReactionsLiveFetchResponse200OutputReactionsType0Item.from_dict(reactions_type_0_item_data)



                    reactions_type_0.append(reactions_type_0_item)

                return reactions_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['ProfileReactionsLiveFetchResponse200OutputReactionsType0Item']], data)

        reactions = _parse_reactions(d.pop("reactions", UNSET))


        def _parse_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))


        profile_reactions_live_fetch_response_200_output = cls(
            reactions=reactions,
            cursor=cursor,
        )


        profile_reactions_live_fetch_response_200_output.additional_properties = d
        return profile_reactions_live_fetch_response_200_output

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
