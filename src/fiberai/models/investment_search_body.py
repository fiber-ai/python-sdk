from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investment_search_body_search_params_type_0 import InvestmentSearchBodySearchParamsType0


T = TypeVar("T", bound="InvestmentSearchBody")


@_attrs_define
class InvestmentSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        search_params (InvestmentSearchBodySearchParamsType0 | None | Unset): Investment search filter parameters. If
            not provided, returns all investments (subject to pagination)
        page_size (int | Unset): Number of investments to return per page (max 100) Default: 25.
        cursor (None | str | Unset): Pagination cursor returned from a previous search response. Use this to fetch the
            next page of results. Null for the first page.
    """

    api_key: str
    search_params: InvestmentSearchBodySearchParamsType0 | None | Unset = UNSET
    page_size: int | Unset = 25
    cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.investment_search_body_search_params_type_0 import InvestmentSearchBodySearchParamsType0

        api_key = self.api_key

        search_params: dict[str, Any] | None | Unset
        if isinstance(self.search_params, Unset):
            search_params = UNSET
        elif isinstance(self.search_params, InvestmentSearchBodySearchParamsType0):
            search_params = self.search_params.to_dict()
        else:
            search_params = self.search_params

        page_size = self.page_size

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if search_params is not UNSET:
            field_dict["searchParams"] = search_params
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_search_body_search_params_type_0 import InvestmentSearchBodySearchParamsType0

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_search_params(data: object) -> InvestmentSearchBodySearchParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_params_type_0 = InvestmentSearchBodySearchParamsType0.from_dict(data)

                return search_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSearchBodySearchParamsType0 | None | Unset, data)

        search_params = _parse_search_params(d.pop("searchParams", UNSET))

        page_size = d.pop("pageSize", UNSET)

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        investment_search_body = cls(
            api_key=api_key,
            search_params=search_params,
            page_size=page_size,
            cursor=cursor,
        )

        investment_search_body.additional_properties = d
        return investment_search_body

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
