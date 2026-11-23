from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.facebook_group_posts_body_sort_type_1 import FacebookGroupPostsBodySortType1
from ..models.facebook_group_posts_body_sort_type_2_type_1 import FacebookGroupPostsBodySortType2Type1
from ..models.facebook_group_posts_body_sort_type_3_type_1 import FacebookGroupPostsBodySortType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="FacebookGroupPostsBody")


@_attrs_define
class FacebookGroupPostsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        url (str): Public Facebook group URL.
        group_id (None | str | Unset): Numeric group ID from the group details response. Optional; makes the request
            faster.
        sort (FacebookGroupPostsBodySortType1 | FacebookGroupPostsBodySortType2Type1 |
            FacebookGroupPostsBodySortType3Type1 | None | Unset): How to order the group's posts. Omit for Facebook's
            default order.
        next_page_token (None | str | Unset): Pagination token from a previous response's `nextPageToken`. Omit for the
            first page.
    """

    api_key: str
    url: str
    group_id: None | str | Unset = UNSET
    sort: (
        FacebookGroupPostsBodySortType1
        | FacebookGroupPostsBodySortType2Type1
        | FacebookGroupPostsBodySortType3Type1
        | None
        | Unset
    ) = UNSET
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        url = self.url

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        sort: None | str | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, FacebookGroupPostsBodySortType1):
            sort = self.sort.value
        elif isinstance(self.sort, FacebookGroupPostsBodySortType2Type1):
            sort = self.sort.value
        elif isinstance(self.sort, FacebookGroupPostsBodySortType3Type1):
            sort = self.sort.value
        else:
            sort = self.sort

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "url": url,
            }
        )
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if sort is not UNSET:
            field_dict["sort"] = sort
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        url = d.pop("url")

        def _parse_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))

        def _parse_sort(
            data: object,
        ) -> (
            FacebookGroupPostsBodySortType1
            | FacebookGroupPostsBodySortType2Type1
            | FacebookGroupPostsBodySortType3Type1
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
                sort_type_1 = FacebookGroupPostsBodySortType1(data)

                return sort_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_type_2_type_1 = FacebookGroupPostsBodySortType2Type1(data)

                return sort_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_type_3_type_1 = FacebookGroupPostsBodySortType3Type1(data)

                return sort_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FacebookGroupPostsBodySortType1
                | FacebookGroupPostsBodySortType2Type1
                | FacebookGroupPostsBodySortType3Type1
                | None
                | Unset,
                data,
            )

        sort = _parse_sort(d.pop("sort", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        facebook_group_posts_body = cls(
            api_key=api_key,
            url=url,
            group_id=group_id,
            sort=sort,
            next_page_token=next_page_token,
        )

        facebook_group_posts_body.additional_properties = d
        return facebook_group_posts_body

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
