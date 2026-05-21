from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RedditSubredditDetailsResponse200OutputSubreddit")


@_attrs_define
class RedditSubredditDetailsResponse200OutputSubreddit:
    """Subreddit metadata.

    Attributes:
        name (str): Subreddit display name (e.g. `AskReddit`). Use this as the primary key when storing subreddits in a
            database — it is unique on Reddit and stable across time.
        id (None | str | Unset): Subreddit identifier (e.g. `2qh1i` for r/AskReddit). May be null when not available;
            use `name` as the stable identifier.
        title (None | str | Unset): Subreddit title.
        description (None | str | Unset): Subreddit description.
        subscriber_count (float | None | Unset): Subscriber count.
        weekly_active_user_count (float | None | Unset): Weekly active user count when available.
        weekly_contribution_count (float | None | Unset): Total number of posts and comments in the subreddit over the
            past 7 days.
        icon_url (None | str | Unset): Subreddit icon URL.
        header_image_url (None | str | Unset): Subreddit header image URL.
        rules (None | str | Unset): Subreddit rules text.
        created_at (None | str | Unset): Subreddit creation timestamp in ISO 8601 format.
    """

    name: str
    id: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    subscriber_count: float | None | Unset = UNSET
    weekly_active_user_count: float | None | Unset = UNSET
    weekly_contribution_count: float | None | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    header_image_url: None | str | Unset = UNSET
    rules: None | str | Unset = UNSET
    created_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        subscriber_count: float | None | Unset
        if isinstance(self.subscriber_count, Unset):
            subscriber_count = UNSET
        else:
            subscriber_count = self.subscriber_count

        weekly_active_user_count: float | None | Unset
        if isinstance(self.weekly_active_user_count, Unset):
            weekly_active_user_count = UNSET
        else:
            weekly_active_user_count = self.weekly_active_user_count

        weekly_contribution_count: float | None | Unset
        if isinstance(self.weekly_contribution_count, Unset):
            weekly_contribution_count = UNSET
        else:
            weekly_contribution_count = self.weekly_contribution_count

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        header_image_url: None | str | Unset
        if isinstance(self.header_image_url, Unset):
            header_image_url = UNSET
        else:
            header_image_url = self.header_image_url

        rules: None | str | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        else:
            rules = self.rules

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if subscriber_count is not UNSET:
            field_dict["subscriberCount"] = subscriber_count
        if weekly_active_user_count is not UNSET:
            field_dict["weeklyActiveUserCount"] = weekly_active_user_count
        if weekly_contribution_count is not UNSET:
            field_dict["weeklyContributionCount"] = weekly_contribution_count
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if header_image_url is not UNSET:
            field_dict["headerImageUrl"] = header_image_url
        if rules is not UNSET:
            field_dict["rules"] = rules
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_subscriber_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        subscriber_count = _parse_subscriber_count(d.pop("subscriberCount", UNSET))

        def _parse_weekly_active_user_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weekly_active_user_count = _parse_weekly_active_user_count(d.pop("weeklyActiveUserCount", UNSET))

        def _parse_weekly_contribution_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weekly_contribution_count = _parse_weekly_contribution_count(d.pop("weeklyContributionCount", UNSET))

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("iconUrl", UNSET))

        def _parse_header_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_image_url = _parse_header_image_url(d.pop("headerImageUrl", UNSET))

        def _parse_rules(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        reddit_subreddit_details_response_200_output_subreddit = cls(
            name=name,
            id=id,
            title=title,
            description=description,
            subscriber_count=subscriber_count,
            weekly_active_user_count=weekly_active_user_count,
            weekly_contribution_count=weekly_contribution_count,
            icon_url=icon_url,
            header_image_url=header_image_url,
            rules=rules,
            created_at=created_at,
        )

        reddit_subreddit_details_response_200_output_subreddit.additional_properties = d
        return reddit_subreddit_details_response_200_output_subreddit

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
