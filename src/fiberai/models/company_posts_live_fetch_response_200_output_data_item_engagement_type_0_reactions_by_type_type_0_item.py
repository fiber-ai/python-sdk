from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_posts_live_fetch_response_200_output_data_item_engagement_type_0_reactions_by_type_type_0_item_reaction_type_type_1 import (
    CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType1,
)
from ..models.company_posts_live_fetch_response_200_output_data_item_engagement_type_0_reactions_by_type_type_0_item_reaction_type_type_2_type_1 import (
    CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType2Type1,
)
from ..models.company_posts_live_fetch_response_200_output_data_item_engagement_type_0_reactions_by_type_type_0_item_reaction_type_type_3_type_1 import (
    CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0Item")


@_attrs_define
class CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0Item:
    """
    Attributes:
        num_reactions (float | None | Unset):
        reaction_type
            (CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType1 |
            CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType2Type1 |
            CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType3Type1 |
            None | Unset): One of LinkedIn's reaction types. These match the tooltips on each of LinkedIn's six reaction
            buttons; for instance, 'Like' is the blue thumbs-up.
    """

    num_reactions: float | None | Unset = UNSET
    reaction_type: (
        CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType1
        | CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType2Type1
        | CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_reactions: float | None | Unset
        if isinstance(self.num_reactions, Unset):
            num_reactions = UNSET
        else:
            num_reactions = self.num_reactions

        reaction_type: None | str | Unset
        if isinstance(self.reaction_type, Unset):
            reaction_type = UNSET
        elif isinstance(
            self.reaction_type,
            CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType1,
        ):
            reaction_type = self.reaction_type.value
        elif isinstance(
            self.reaction_type,
            CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType2Type1,
        ):
            reaction_type = self.reaction_type.value
        elif isinstance(
            self.reaction_type,
            CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType3Type1,
        ):
            reaction_type = self.reaction_type.value
        else:
            reaction_type = self.reaction_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_reactions is not UNSET:
            field_dict["numReactions"] = num_reactions
        if reaction_type is not UNSET:
            field_dict["reactionType"] = reaction_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_num_reactions(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        num_reactions = _parse_num_reactions(d.pop("numReactions", UNSET))

        def _parse_reaction_type(
            data: object,
        ) -> (
            CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType1
            | CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType2Type1
            | CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reaction_type_type_1 = CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType1(
                    data
                )

                return reaction_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reaction_type_type_2_type_1 = CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType2Type1(
                    data
                )

                return reaction_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reaction_type_type_3_type_1 = CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType3Type1(
                    data
                )

                return reaction_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType1
                | CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType2Type1
                | CompanyPostsLiveFetchResponse200OutputDataItemEngagementType0ReactionsByTypeType0ItemReactionTypeType3Type1
                | None
                | Unset,
                data,
            )

        reaction_type = _parse_reaction_type(d.pop("reactionType", UNSET))

        company_posts_live_fetch_response_200_output_data_item_engagement_type_0_reactions_by_type_type_0_item = cls(
            num_reactions=num_reactions,
            reaction_type=reaction_type,
        )

        company_posts_live_fetch_response_200_output_data_item_engagement_type_0_reactions_by_type_type_0_item.additional_properties = d
        return company_posts_live_fetch_response_200_output_data_item_engagement_type_0_reactions_by_type_type_0_item

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
