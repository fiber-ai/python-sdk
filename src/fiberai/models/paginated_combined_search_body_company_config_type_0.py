from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0_search_params import (
        PaginatedCombinedSearchBodyCompanyConfigType0SearchParams,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyCompanyConfigType0")


@_attrs_define
class PaginatedCombinedSearchBodyCompanyConfigType0:
    """
    Attributes:
        search_params (PaginatedCombinedSearchBodyCompanyConfigType0SearchParams): The company search parameters.
            Prospects are found from companies matching these filters.
        page_size (float | None | Unset): The number of companies to return per page. Pass null if you only want
            profiles. NOTE: your companies search params will still get honored to find the profiles.
        exclusion_list_i_ds (list[str] | None | Unset): The IDs of company exclusion lists to filter out matching
            companies.
        company_cursor (None | str | Unset):
    """

    search_params: PaginatedCombinedSearchBodyCompanyConfigType0SearchParams
    page_size: float | None | Unset = UNSET
    exclusion_list_i_ds: list[str] | None | Unset = UNSET
    company_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_params = self.search_params.to_dict()

        page_size: float | None | Unset
        if isinstance(self.page_size, Unset):
            page_size = UNSET
        else:
            page_size = self.page_size

        exclusion_list_i_ds: list[str] | None | Unset
        if isinstance(self.exclusion_list_i_ds, Unset):
            exclusion_list_i_ds = UNSET
        elif isinstance(self.exclusion_list_i_ds, list):
            exclusion_list_i_ds = self.exclusion_list_i_ds

        else:
            exclusion_list_i_ds = self.exclusion_list_i_ds

        company_cursor: None | str | Unset
        if isinstance(self.company_cursor, Unset):
            company_cursor = UNSET
        else:
            company_cursor = self.company_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "searchParams": search_params,
            }
        )
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if exclusion_list_i_ds is not UNSET:
            field_dict["exclusionListIDs"] = exclusion_list_i_ds
        if company_cursor is not UNSET:
            field_dict["companyCursor"] = company_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_company_config_type_0_search_params import (
            PaginatedCombinedSearchBodyCompanyConfigType0SearchParams,
        )

        d = dict(src_dict)
        search_params = PaginatedCombinedSearchBodyCompanyConfigType0SearchParams.from_dict(d.pop("searchParams"))

        def _parse_page_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        page_size = _parse_page_size(d.pop("pageSize", UNSET))

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

        def _parse_company_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_cursor = _parse_company_cursor(d.pop("companyCursor", UNSET))

        paginated_combined_search_body_company_config_type_0 = cls(
            search_params=search_params,
            page_size=page_size,
            exclusion_list_i_ds=exclusion_list_i_ds,
            company_cursor=company_cursor,
        )

        paginated_combined_search_body_company_config_type_0.additional_properties = d
        return paginated_combined_search_body_company_config_type_0

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
