from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        data (TextToCombinedSearchResponse200OutputData):
        company_search_params (None | TextToCombinedSearchResponse200OutputCompanySearchParamsType0):
        profile_search_params (None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0):
    """

    data: TextToCombinedSearchResponse200OutputData
    company_search_params: None | TextToCombinedSearchResponse200OutputCompanySearchParamsType0
    profile_search_params: None | TextToCombinedSearchResponse200OutputProfileSearchParamsType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_company_search_params_type_0 import (
            TextToCombinedSearchResponse200OutputCompanySearchParamsType0,
        )
        from ..models.text_to_combined_search_response_200_output_profile_search_params_type_0 import (
            TextToCombinedSearchResponse200OutputProfileSearchParamsType0,
        )

        data = self.data.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "companySearchParams": company_search_params,
                "profileSearchParams": profile_search_params,
            }
        )

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
        data = TextToCombinedSearchResponse200OutputData.from_dict(d.pop("data"))

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

        text_to_combined_search_response_200_output = cls(
            data=data,
            company_search_params=company_search_params,
            profile_search_params=profile_search_params,
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
