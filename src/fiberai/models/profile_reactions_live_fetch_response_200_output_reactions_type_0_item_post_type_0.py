from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0_author_type_0 import (
        ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0AuthorType0,
    )


T = TypeVar("T", bound="ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0")


@_attrs_define
class ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0:
    """
    Attributes:
        post_urn (None | str | Unset):
        post_url (None | str | Unset):
        author (None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0AuthorType0 | Unset):
        content (None | str | Unset):
    """

    post_urn: None | str | Unset = UNSET
    post_url: None | str | Unset = UNSET
    author: None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0AuthorType0 | Unset = UNSET
    content: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0_author_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0AuthorType0,
        )

        post_urn: None | str | Unset
        if isinstance(self.post_urn, Unset):
            post_urn = UNSET
        else:
            post_urn = self.post_urn

        post_url: None | str | Unset
        if isinstance(self.post_url, Unset):
            post_url = UNSET
        else:
            post_url = self.post_url

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0AuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_urn is not UNSET:
            field_dict["postUrn"] = post_urn
        if post_url is not UNSET:
            field_dict["postUrl"] = post_url
        if author is not UNSET:
            field_dict["author"] = author
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0_author_type_0 import (
            ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0AuthorType0,
        )

        d = dict(src_dict)

        def _parse_post_urn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_urn = _parse_post_urn(d.pop("postUrn", UNSET))

        def _parse_post_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_url = _parse_post_url(d.pop("postUrl", UNSET))

        def _parse_author(
            data: object,
        ) -> None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0AuthorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = (
                    ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0AuthorType0.from_dict(data)
                )

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemPostType0AuthorType0 | Unset, data
            )

        author = _parse_author(d.pop("author", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0 = cls(
            post_urn=post_urn,
            post_url=post_url,
            author=author,
            content=content,
        )

        profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0.additional_properties = d
        return profile_reactions_live_fetch_response_200_output_reactions_type_0_item_post_type_0

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
