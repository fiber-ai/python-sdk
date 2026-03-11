from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_audience_search_params_response_200_output_company_search_params_type_0 import (
        UpdateAudienceSearchParamsResponse200OutputCompanySearchParamsType0,
    )
    from ..models.update_audience_search_params_response_200_output_prospect_search_params_type_0 import (
        UpdateAudienceSearchParamsResponse200OutputProspectSearchParamsType0,
    )


T = TypeVar("T", bound="UpdateAudienceSearchParamsResponse200Output")


@_attrs_define
class UpdateAudienceSearchParamsResponse200Output:
    """
    Attributes:
        audience_id (str): Unique ID of the audience
        company_search_params (None | Unset | UpdateAudienceSearchParamsResponse200OutputCompanySearchParamsType0): The
            updated company search parameters
        prospect_search_params (None | Unset | UpdateAudienceSearchParamsResponse200OutputProspectSearchParamsType0):
            The updated prospect search parameters
    """

    audience_id: str
    company_search_params: None | Unset | UpdateAudienceSearchParamsResponse200OutputCompanySearchParamsType0 = UNSET
    prospect_search_params: None | Unset | UpdateAudienceSearchParamsResponse200OutputProspectSearchParamsType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_audience_search_params_response_200_output_company_search_params_type_0 import (
            UpdateAudienceSearchParamsResponse200OutputCompanySearchParamsType0,
        )
        from ..models.update_audience_search_params_response_200_output_prospect_search_params_type_0 import (
            UpdateAudienceSearchParamsResponse200OutputProspectSearchParamsType0,
        )

        audience_id = self.audience_id

        company_search_params: dict[str, Any] | None | Unset
        if isinstance(self.company_search_params, Unset):
            company_search_params = UNSET
        elif isinstance(
            self.company_search_params, UpdateAudienceSearchParamsResponse200OutputCompanySearchParamsType0
        ):
            company_search_params = self.company_search_params.to_dict()
        else:
            company_search_params = self.company_search_params

        prospect_search_params: dict[str, Any] | None | Unset
        if isinstance(self.prospect_search_params, Unset):
            prospect_search_params = UNSET
        elif isinstance(
            self.prospect_search_params, UpdateAudienceSearchParamsResponse200OutputProspectSearchParamsType0
        ):
            prospect_search_params = self.prospect_search_params.to_dict()
        else:
            prospect_search_params = self.prospect_search_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audienceId": audience_id,
            }
        )
        if company_search_params is not UNSET:
            field_dict["companySearchParams"] = company_search_params
        if prospect_search_params is not UNSET:
            field_dict["prospectSearchParams"] = prospect_search_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_audience_search_params_response_200_output_company_search_params_type_0 import (
            UpdateAudienceSearchParamsResponse200OutputCompanySearchParamsType0,
        )
        from ..models.update_audience_search_params_response_200_output_prospect_search_params_type_0 import (
            UpdateAudienceSearchParamsResponse200OutputProspectSearchParamsType0,
        )

        d = dict(src_dict)
        audience_id = d.pop("audienceId")

        def _parse_company_search_params(
            data: object,
        ) -> None | Unset | UpdateAudienceSearchParamsResponse200OutputCompanySearchParamsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_search_params_type_0 = (
                    UpdateAudienceSearchParamsResponse200OutputCompanySearchParamsType0.from_dict(data)
                )

                return company_search_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAudienceSearchParamsResponse200OutputCompanySearchParamsType0, data)

        company_search_params = _parse_company_search_params(d.pop("companySearchParams", UNSET))

        def _parse_prospect_search_params(
            data: object,
        ) -> None | Unset | UpdateAudienceSearchParamsResponse200OutputProspectSearchParamsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prospect_search_params_type_0 = (
                    UpdateAudienceSearchParamsResponse200OutputProspectSearchParamsType0.from_dict(data)
                )

                return prospect_search_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAudienceSearchParamsResponse200OutputProspectSearchParamsType0, data)

        prospect_search_params = _parse_prospect_search_params(d.pop("prospectSearchParams", UNSET))

        update_audience_search_params_response_200_output = cls(
            audience_id=audience_id,
            company_search_params=company_search_params,
            prospect_search_params=prospect_search_params,
        )

        update_audience_search_params_response_200_output.additional_properties = d
        return update_audience_search_params_response_200_output

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
