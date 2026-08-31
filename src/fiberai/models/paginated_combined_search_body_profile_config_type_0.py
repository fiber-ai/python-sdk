from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParams,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyProfileConfigType0")


@_attrs_define
class PaginatedCombinedSearchBodyProfileConfigType0:
    """
    Attributes:
        page_size (float): The number of profiles to return per page.
        search_params (PaginatedCombinedSearchBodyProfileConfigType0SearchParams | Unset): The profile search
            parameters. Returns profiles matching these filters who work at companies satisfying companyParams.
        exclusion_list_i_ds (list[str] | None | Unset): The IDs of prospect exclusion lists to filter out matching
            people.
        profile_cursor (None | str | Unset):
    """

    page_size: float
    search_params: PaginatedCombinedSearchBodyProfileConfigType0SearchParams | Unset = UNSET
    exclusion_list_i_ds: list[str] | None | Unset = UNSET
    profile_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        search_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_params, Unset):
            search_params = self.search_params.to_dict()

        exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.exclusion_list_i_ds, Unset):
            exclusion_list_i_ds = UNSET
        elif isinstance(self.exclusion_list_i_ds, list):
            exclusion_list_i_ds = self.exclusion_list_i_ds

        else:
            exclusion_list_i_ds = self.exclusion_list_i_ds

        profile_cursor: None | str | Unset
        if isinstance(self.profile_cursor, Unset):
            profile_cursor = UNSET
        else:
            profile_cursor = self.profile_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageSize": page_size,
            }
        )
        if search_params is not UNSET:
            field_dict["searchParams"] = search_params
        if exclusion_list_i_ds is not UNSET:
            field_dict["exclusionListIDs"] = exclusion_list_i_ds
        if profile_cursor is not UNSET:
            field_dict["profileCursor"] = profile_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParams,  # noqa: PLC0415
        )

        d = dict(src_dict)
        page_size = d.pop("pageSize")

        _search_params = d.pop("searchParams", UNSET)
        search_params: PaginatedCombinedSearchBodyProfileConfigType0SearchParams | Unset
        if isinstance(_search_params, Unset):
            search_params = UNSET
        else:
            search_params = PaginatedCombinedSearchBodyProfileConfigType0SearchParams.from_dict(_search_params)

        def _parse_exclusion_list_i_ds(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusion_list_i_ds_type_0 = cast(list[str], data)

                return exclusion_list_i_ds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclusion_list_i_ds = _parse_exclusion_list_i_ds(d.pop("exclusionListIDs", UNSET))

        def _parse_profile_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_cursor = _parse_profile_cursor(d.pop("profileCursor", UNSET))

        paginated_combined_search_body_profile_config_type_0 = cls(
            page_size=page_size,
            search_params=search_params,
            exclusion_list_i_ds=exclusion_list_i_ds,
            profile_cursor=profile_cursor,
        )

        paginated_combined_search_body_profile_config_type_0.additional_properties = d
        return paginated_combined_search_body_profile_config_type_0

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
