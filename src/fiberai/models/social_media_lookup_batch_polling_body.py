from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialMediaLookupBatchPollingBody")


@_attrs_define
class SocialMediaLookupBatchPollingBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        run_id (str): The ID of the batch run returned by the batch trigger endpoint.
        next_page_token (None | str | Unset): Token from the previous response to fetch the next page. Omit for the
            first page.
        page_size (float | Unset): Number of results to return per page (default 50, max 100). Default: 50.0.
    """

    api_key: str
    run_id: str
    next_page_token: None | str | Unset = UNSET
    page_size: float | Unset = 50.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        run_id = self.run_id

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "runId": run_id,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        run_id = d.pop("runId")

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        page_size = d.pop("pageSize", UNSET)

        social_media_lookup_batch_polling_body = cls(
            api_key=api_key,
            run_id=run_id,
            next_page_token=next_page_token,
            page_size=page_size,
        )

        social_media_lookup_batch_polling_body.additional_properties = d
        return social_media_lookup_batch_polling_body

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
