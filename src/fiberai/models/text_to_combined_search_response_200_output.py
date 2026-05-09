from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_output_company_search_params_type_0 import (
        TextToCombinedSearchResponse200OutputCompanySearchParamsType0,
    )
    from ..models.text_to_combined_search_response_200_output_data import TextToCombinedSearchResponse200OutputData
    from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0 import (
        TextToCombinedSearchResponse200OutputProfileSearchParamsType0,
    )


T = TypeVar("T", bound="TextToCombinedSearchResponse200Output")


@_attrs_define
class TextToCombinedSearchResponse200Output:
    """
    Attributes:
        company_search_params (None | TextToCombinedSearchResponse200OutputCompanySearchParamsType0):
        profile_search_params (None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0):
        data (TextToCombinedSearchResponse200OutputData):
        company_cursor (None | str | Unset):
        profile_cursor (None | str | Unset):
    """

    company_search_params: None | TextToCombinedSearchResponse200OutputCompanySearchParamsType0
    profile_search_params: None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0
    data: TextToCombinedSearchResponse200OutputData
    company_cursor: None | str | Unset = UNSET
    profile_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0 import (
            TextToCombinedSearchResponse200OutputCompanySearchParamsType0,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0,
        )

        company_search_params: dict[str, Any] | None
        if isinstance(self.company_search_params, TextToCombinedSearchResponse200OutputCompanySearchParamsType0):
            company_search_params = self.company_search_params.to_dict()
        else:
            company_search_params = self.company_search_params

        profile_search_params: dict[str, Any] | None
        if isinstance(self.profile_search_params, TextToCombinedSearchResponse200OutputProfileSearchParamsType0):
            profile_search_params = self.profile_search_params.to_dict()
        else:
            profile_search_params = self.profile_search_params

        data = self.data.to_dict()

        company_cursor: None | str | Unset
        if isinstance(self.company_cursor, Unset):
            company_cursor = UNSET
        else:
            company_cursor = self.company_cursor

        profile_cursor: None | str | Unset
        if isinstance(self.profile_cursor, Unset):
            profile_cursor = UNSET
        else:
            profile_cursor = self.profile_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companySearchParams": company_search_params,
                "profileSearchParams": profile_search_params,
                "data": data,
            }
        )
        if company_cursor is not UNSET:
            field_dict["companyCursor"] = company_cursor
        if profile_cursor is not UNSET:
            field_dict["profileCursor"] = profile_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0 import (
            TextToCombinedSearchResponse200OutputCompanySearchParamsType0,
        )
        from ..models.text_to_combined_search_response_200_output_data import TextToCombinedSearchResponse200OutputData
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0,
        )

        d = dict(src_dict)

        def _parse_company_search_params(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputCompanySearchParamsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_search_params_type_0 = TextToCombinedSearchResponse200OutputCompanySearchParamsType0.from_dict(
                    data
                )

                return company_search_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCombinedSearchResponse200OutputCompanySearchParamsType0, data)

        company_search_params = _parse_company_search_params(d.pop("companySearchParams"))

        def _parse_profile_search_params(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_search_params_type_0 = TextToCombinedSearchResponse200OutputProfileSearchParamsType0.from_dict(
                    data
                )

                return profile_search_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0, data)

        profile_search_params = _parse_profile_search_params(d.pop("profileSearchParams"))

        data = TextToCombinedSearchResponse200OutputData.from_dict(d.pop("data"))

        def _parse_company_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_cursor = _parse_company_cursor(d.pop("companyCursor", UNSET))

        def _parse_profile_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_cursor = _parse_profile_cursor(d.pop("profileCursor", UNSET))

        text_to_combined_search_response_200_output = cls(
            company_search_params=company_search_params,
            profile_search_params=profile_search_params,
            data=data,
            company_cursor=company_cursor,
            profile_cursor=profile_cursor,
        )

        text_to_combined_search_response_200_output.additional_properties = d
        return text_to_combined_search_response_200_output

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
