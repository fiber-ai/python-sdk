from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.people_search_body_search_params_unemployment_type_0_became_unemployed_at_type_0 import (
        PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType0,
    )
    from ..models.people_search_body_search_params_unemployment_type_0_became_unemployed_at_type_1 import (
        PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1,
    )


T = TypeVar("T", bound="PeopleSearchBodySearchParamsUnemploymentType0")


@_attrs_define
class PeopleSearchBodySearchParamsUnemploymentType0:
    """
    Attributes:
        is_unemployed (bool):
        became_unemployed_at (None | PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType0 |
            PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1 | Unset):
    """

    is_unemployed: bool
    became_unemployed_at: (
        None
        | PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType0
        | PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_body_search_params_unemployment_type_0_became_unemployed_at_type_0 import (
            PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType0,
        )
        from ..models.people_search_body_search_params_unemployment_type_0_became_unemployed_at_type_1 import (
            PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1,
        )

        is_unemployed = self.is_unemployed

        became_unemployed_at: dict[str, Any] | None | Unset
        if isinstance(self.became_unemployed_at, Unset):
            became_unemployed_at = UNSET
        elif isinstance(
            self.became_unemployed_at, PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType0
        ):
            became_unemployed_at = self.became_unemployed_at.to_dict()
        elif isinstance(
            self.became_unemployed_at, PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1
        ):
            became_unemployed_at = self.became_unemployed_at.to_dict()
        else:
            became_unemployed_at = self.became_unemployed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isUnemployed": is_unemployed,
            }
        )
        if became_unemployed_at is not UNSET:
            field_dict["becameUnemployedAt"] = became_unemployed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_body_search_params_unemployment_type_0_became_unemployed_at_type_0 import (
            PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType0,
        )
        from ..models.people_search_body_search_params_unemployment_type_0_became_unemployed_at_type_1 import (
            PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1,
        )

        d = dict(src_dict)
        is_unemployed = d.pop("isUnemployed")

        def _parse_became_unemployed_at(
            data: object,
        ) -> (
            None
            | PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType0
            | PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                became_unemployed_at_type_0 = (
                    PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType0.from_dict(data)
                )

                return became_unemployed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                became_unemployed_at_type_1 = (
                    PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1.from_dict(data)
                )

                return became_unemployed_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType0
                | PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1
                | Unset,
                data,
            )

        became_unemployed_at = _parse_became_unemployed_at(d.pop("becameUnemployedAt", UNSET))

        people_search_body_search_params_unemployment_type_0 = cls(
            is_unemployed=is_unemployed,
            became_unemployed_at=became_unemployed_at,
        )

        people_search_body_search_params_unemployment_type_0.additional_properties = d
        return people_search_body_search_params_unemployment_type_0

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
