from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.quick_person_resolve_body_people_item_type_0 import QuickPersonResolveBodyPeopleItemType0
    from ..models.quick_person_resolve_body_people_item_type_1 import QuickPersonResolveBodyPeopleItemType1
    from ..models.quick_person_resolve_body_people_item_type_2 import QuickPersonResolveBodyPeopleItemType2
    from ..models.quick_person_resolve_body_people_item_type_3 import QuickPersonResolveBodyPeopleItemType3


T = TypeVar("T", bound="QuickPersonResolveBody")


@_attrs_define
class QuickPersonResolveBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        people (list[QuickPersonResolveBodyPeopleItemType0 | QuickPersonResolveBodyPeopleItemType1 |
            QuickPersonResolveBodyPeopleItemType2 | QuickPersonResolveBodyPeopleItemType3]): People to resolve. Each entry
            is an { identifier, value } pair where identifier is "linkedinSlug", "linkedinUserId", "linkedinUrl", or
            "entityUrn". Max 100 per request. You are charged only for the ones that resolve.
    """

    api_key: str
    people: list[
        QuickPersonResolveBodyPeopleItemType0
        | QuickPersonResolveBodyPeopleItemType1
        | QuickPersonResolveBodyPeopleItemType2
        | QuickPersonResolveBodyPeopleItemType3
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_person_resolve_body_people_item_type_0 import (
            QuickPersonResolveBodyPeopleItemType0,  # noqa: PLC0415
        )
        from ..models.quick_person_resolve_body_people_item_type_1 import (
            QuickPersonResolveBodyPeopleItemType1,  # noqa: PLC0415
        )
        from ..models.quick_person_resolve_body_people_item_type_2 import (
            QuickPersonResolveBodyPeopleItemType2,  # noqa: PLC0415
        )

        api_key = self.api_key

        people = []
        for people_item_data in self.people:
            people_item: dict[str, Any]
            if isinstance(people_item_data, QuickPersonResolveBodyPeopleItemType0):
                people_item = people_item_data.to_dict()
            elif isinstance(people_item_data, QuickPersonResolveBodyPeopleItemType1):
                people_item = people_item_data.to_dict()
            elif isinstance(people_item_data, QuickPersonResolveBodyPeopleItemType2):
                people_item = people_item_data.to_dict()
            else:
                people_item = people_item_data.to_dict()

            people.append(people_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "people": people,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_person_resolve_body_people_item_type_0 import (
            QuickPersonResolveBodyPeopleItemType0,  # noqa: PLC0415
        )
        from ..models.quick_person_resolve_body_people_item_type_1 import (
            QuickPersonResolveBodyPeopleItemType1,  # noqa: PLC0415
        )
        from ..models.quick_person_resolve_body_people_item_type_2 import (
            QuickPersonResolveBodyPeopleItemType2,  # noqa: PLC0415
        )
        from ..models.quick_person_resolve_body_people_item_type_3 import (
            QuickPersonResolveBodyPeopleItemType3,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        people = []
        _people = d.pop("people")
        for people_item_data in _people:

            def _parse_people_item(
                data: object,
            ) -> (
                QuickPersonResolveBodyPeopleItemType0
                | QuickPersonResolveBodyPeopleItemType1
                | QuickPersonResolveBodyPeopleItemType2
                | QuickPersonResolveBodyPeopleItemType3
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    people_item_type_0 = QuickPersonResolveBodyPeopleItemType0.from_dict(data)

                    return people_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    people_item_type_1 = QuickPersonResolveBodyPeopleItemType1.from_dict(data)

                    return people_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    people_item_type_2 = QuickPersonResolveBodyPeopleItemType2.from_dict(data)

                    return people_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                people_item_type_3 = QuickPersonResolveBodyPeopleItemType3.from_dict(data)

                return people_item_type_3

            people_item = _parse_people_item(people_item_data)

            people.append(people_item)

        quick_person_resolve_body = cls(
            api_key=api_key,
            people=people,
        )

        quick_person_resolve_body.additional_properties = d
        return quick_person_resolve_body

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
