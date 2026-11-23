from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FacebookProfileResponse200Output")


@_attrs_define
class FacebookProfileResponse200Output:
    """
    Attributes:
        id (str): Unique profile ID.
        name (str): Display name of the page or profile.
        page_id (None | str | Unset): Numeric page ID. Pass as `pageId` when fetching this page's posts to make that
            request faster.
        url (None | str | Unset): URL of the Facebook page or profile.
        category (None | str | Unset): Category the page lists itself under (e.g. 'Coffee shop').
        follower_count (float | None | Unset): Number of followers.
        like_count (float | None | Unset): Number of page likes.
        intro (None | str | Unset): Short intro text from the page.
        email (None | str | Unset): Public contact email listed on the page.
        phone (None | str | Unset): Public contact phone number listed on the page.
        website (None | str | Unset): Website URL listed on the page.
        address (None | str | Unset): Physical address listed on the page.
    """

    id: str
    name: str
    page_id: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    follower_count: float | None | Unset = UNSET
    like_count: float | None | Unset = UNSET
    intro: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        page_id: None | str | Unset
        if isinstance(self.page_id, Unset):
            page_id = UNSET
        else:
            page_id = self.page_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        follower_count: float | None | Unset
        if isinstance(self.follower_count, Unset):
            follower_count = UNSET
        else:
            follower_count = self.follower_count

        like_count: float | None | Unset
        if isinstance(self.like_count, Unset):
            like_count = UNSET
        else:
            like_count = self.like_count

        intro: None | str | Unset
        if isinstance(self.intro, Unset):
            intro = UNSET
        else:
            intro = self.intro

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if page_id is not UNSET:
            field_dict["pageId"] = page_id
        if url is not UNSET:
            field_dict["url"] = url
        if category is not UNSET:
            field_dict["category"] = category
        if follower_count is not UNSET:
            field_dict["followerCount"] = follower_count
        if like_count is not UNSET:
            field_dict["likeCount"] = like_count
        if intro is not UNSET:
            field_dict["intro"] = intro
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if website is not UNSET:
            field_dict["website"] = website
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_page_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_id = _parse_page_id(d.pop("pageId", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_follower_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        follower_count = _parse_follower_count(d.pop("followerCount", UNSET))

        def _parse_like_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        like_count = _parse_like_count(d.pop("likeCount", UNSET))

        def _parse_intro(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intro = _parse_intro(d.pop("intro", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        facebook_profile_response_200_output = cls(
            id=id,
            name=name,
            page_id=page_id,
            url=url,
            category=category,
            follower_count=follower_count,
            like_count=like_count,
            intro=intro,
            email=email,
            phone=phone,
            website=website,
            address=address,
        )

        facebook_profile_response_200_output.additional_properties = d
        return facebook_profile_response_200_output

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
