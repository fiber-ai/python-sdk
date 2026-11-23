from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.facebook_post_comments_body_sort_type_1 import FacebookPostCommentsBodySortType1
from ..models.facebook_post_comments_body_sort_type_2_type_1 import FacebookPostCommentsBodySortType2Type1
from ..models.facebook_post_comments_body_sort_type_3_type_1 import FacebookPostCommentsBodySortType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="FacebookPostCommentsBody")


@_attrs_define
class FacebookPostCommentsBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        url (str): Facebook post, video, or Reel URL.
        feedback_id (None | str | Unset): Feedback ID of the post, from the post details response. Optional; makes the
            request much faster.
        sort (FacebookPostCommentsBodySortType1 | FacebookPostCommentsBodySortType2Type1 |
            FacebookPostCommentsBodySortType3Type1 | None | Unset): Which comments to return. `top` is Facebook's ranked
            view, which can hide some comments; `all` returns every comment, and reply tokens from an `all` page return
            unfiltered replies. Keep the same value across pages.
        next_page_token (None | str | Unset): Pagination token from a previous response's `nextPageToken`. Omit for the
            first page.
    """

    api_key: str
    url: str
    feedback_id: None | str | Unset = UNSET
    sort: (
        FacebookPostCommentsBodySortType1
        | FacebookPostCommentsBodySortType2Type1
        | FacebookPostCommentsBodySortType3Type1
        | None
        | Unset
    ) = UNSET
    next_page_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        url = self.url

        feedback_id: None | str | Unset
        if isinstance(self.feedback_id, Unset):
            feedback_id = UNSET
        else:
            feedback_id = self.feedback_id

        sort: None | str | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, FacebookPostCommentsBodySortType1):
            sort = self.sort.value
        elif isinstance(self.sort, FacebookPostCommentsBodySortType2Type1):
            sort = self.sort.value
        elif isinstance(self.sort, FacebookPostCommentsBodySortType3Type1):
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
        if feedback_id is not UNSET:
            field_dict["feedbackId"] = feedback_id
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

        def _parse_feedback_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feedback_id = _parse_feedback_id(d.pop("feedbackId", UNSET))

        def _parse_sort(
            data: object,
        ) -> (
            FacebookPostCommentsBodySortType1
            | FacebookPostCommentsBodySortType2Type1
            | FacebookPostCommentsBodySortType3Type1
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
                sort_type_1 = FacebookPostCommentsBodySortType1(data)

                return sort_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_type_2_type_1 = FacebookPostCommentsBodySortType2Type1(data)

                return sort_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sort_type_3_type_1 = FacebookPostCommentsBodySortType3Type1(data)

                return sort_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FacebookPostCommentsBodySortType1
                | FacebookPostCommentsBodySortType2Type1
                | FacebookPostCommentsBodySortType3Type1
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

        facebook_post_comments_body = cls(
            api_key=api_key,
            url=url,
            feedback_id=feedback_id,
            sort=sort,
            next_page_token=next_page_token,
        )

        facebook_post_comments_body.additional_properties = d
        return facebook_post_comments_body

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
