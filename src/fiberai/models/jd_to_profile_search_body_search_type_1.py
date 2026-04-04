from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jd_to_profile_search_body_search_type_1_request import JdToProfileSearchBodySearchType1Request

T = TypeVar("T", bound="JdToProfileSearchBodySearchType1")


@_attrs_define
class JdToProfileSearchBodySearchType1:
    """
    Attributes:
        request (JdToProfileSearchBodySearchType1Request): Use "subsequent" for page 2 and beyond. Only the cursor from
            the previous response is required; all other parameters are stored server-side.
        cursor (str): The `nextCursor` value returned by the previous response. Valid for 3 days.
    """

    request: JdToProfileSearchBodySearchType1Request
    cursor: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request = self.request.value

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request": request,
                "cursor": cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request = JdToProfileSearchBodySearchType1Request(d.pop("request"))

        cursor = d.pop("cursor")

        jd_to_profile_search_body_search_type_1 = cls(
            request=request,
            cursor=cursor,
        )

        jd_to_profile_search_body_search_type_1.additional_properties = d
        return jd_to_profile_search_body_search_type_1

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
