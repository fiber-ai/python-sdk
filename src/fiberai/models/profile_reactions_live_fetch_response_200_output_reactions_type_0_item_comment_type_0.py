from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0_author_type_0 import (
        ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0AuthorType0,
    )


T = TypeVar("T", bound="ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0")


@_attrs_define
class ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0:
    """
    Attributes:
        content (None | str | Unset):
        author (None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0AuthorType0 | Unset):
    """

    content: None | str | Unset = UNSET
    author: None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0AuthorType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0_author_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0AuthorType0,
        )

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(
            self.author, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0AuthorType0
        ):
            author = self.author.to_dict()
        else:
            author = self.author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0_author_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0AuthorType0,
        )

        d = dict(src_dict)

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_author(
            data: object,
        ) -> None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0AuthorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = (
                    ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0AuthorType0.from_dict(data)
                )

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemCommentType0AuthorType0 | Unset, data
            )

        author = _parse_author(d.pop("author", UNSET))

        profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0 = cls(
            content=content,
            author=author,
        )

        profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0.additional_properties = d
        return profile_reactions_live_fetch_response_200_output_reactions_type_0_item_comment_type_0

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
