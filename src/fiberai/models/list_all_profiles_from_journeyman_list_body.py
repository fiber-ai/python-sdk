from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_all_profiles_from_journeyman_list_body_movements_type_0_item import (
    ListAllProfilesFromJourneymanListBodyMovementsType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAllProfilesFromJourneymanListBody")


@_attrs_define
class ListAllProfilesFromJourneymanListBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        job_change_list_id (str): The job change list id.
        movements (list[ListAllProfilesFromJourneymanListBodyMovementsType0Item] | None | Unset):
        cursor (None | str | Unset): The pagination cursor to continue from a previous response.
        page_size (int | Unset): The number of profiles to return per page. Default: 100.
    """

    api_key: str
    job_change_list_id: str
    movements: list[ListAllProfilesFromJourneymanListBodyMovementsType0Item] | None | Unset = UNSET
    cursor: None | str | Unset = UNSET
    page_size: int | Unset = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        job_change_list_id = self.job_change_list_id

        movements: list[str] | None | Unset
        if isinstance(self.movements, Unset):
            movements = UNSET
        elif isinstance(self.movements, list):
            movements = []
            for movements_type_0_item_data in self.movements:
                movements_type_0_item = movements_type_0_item_data.value
                movements.append(movements_type_0_item)

        else:
            movements = self.movements

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "jobChangeListId": job_change_list_id,
            }
        )
        if movements is not UNSET:
            field_dict["movements"] = movements
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        job_change_list_id = d.pop("jobChangeListId")

        def _parse_movements(
            data: object,
        ) -> list[ListAllProfilesFromJourneymanListBodyMovementsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                movements_type_0 = []
                _movements_type_0 = data
                for movements_type_0_item_data in _movements_type_0:
                    movements_type_0_item = ListAllProfilesFromJourneymanListBodyMovementsType0Item(
                        movements_type_0_item_data
                    )

                    movements_type_0.append(movements_type_0_item)

                return movements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ListAllProfilesFromJourneymanListBodyMovementsType0Item] | None | Unset, data)

        movements = _parse_movements(d.pop("movements", UNSET))

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        page_size = d.pop("pageSize", UNSET)

        list_all_profiles_from_journeyman_list_body = cls(
            api_key=api_key,
            job_change_list_id=job_change_list_id,
            movements=movements,
            cursor=cursor,
            page_size=page_size,
        )

        list_all_profiles_from_journeyman_list_body.additional_properties = d
        return list_all_profiles_from_journeyman_list_body

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
