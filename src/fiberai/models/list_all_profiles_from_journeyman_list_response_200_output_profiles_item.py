from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_all_profiles_from_journeyman_list_response_200_output_profiles_item_all_movements_item import (
        ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItem,
    )


T = TypeVar("T", bound="ListAllProfilesFromJourneymanListResponse200OutputProfilesItem")


@_attrs_define
class ListAllProfilesFromJourneymanListResponse200OutputProfilesItem:
    """
    Attributes:
        id (str): The ID of the profile.
        linkedin_url (str): The linkedin url of the profile.
        all_movements (list[ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItem]): Get all
            movement of the profile sorted latest
    """

    id: str
    linkedin_url: str
    all_movements: list[ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        linkedin_url = self.linkedin_url

        all_movements = []
        for all_movements_item_data in self.all_movements:
            all_movements_item = all_movements_item_data.to_dict()
            all_movements.append(all_movements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "linkedinUrl": linkedin_url,
                "allMovements": all_movements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_all_profiles_from_journeyman_list_response_200_output_profiles_item_all_movements_item import (
            ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        linkedin_url = d.pop("linkedinUrl")

        all_movements = []
        _all_movements = d.pop("allMovements")
        for all_movements_item_data in _all_movements:
            all_movements_item = (
                ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItem.from_dict(
                    all_movements_item_data
                )
            )

            all_movements.append(all_movements_item)

        list_all_profiles_from_journeyman_list_response_200_output_profiles_item = cls(
            id=id,
            linkedin_url=linkedin_url,
            all_movements=all_movements,
        )

        list_all_profiles_from_journeyman_list_response_200_output_profiles_item.additional_properties = d
        return list_all_profiles_from_journeyman_list_response_200_output_profiles_item

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
