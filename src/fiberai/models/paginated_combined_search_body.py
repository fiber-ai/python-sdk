from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_company_config_type_0 import (
        PaginatedCombinedSearchBodyCompanyConfigType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBody")


@_attrs_define
class PaginatedCombinedSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company_config (None | PaginatedCombinedSearchBodyCompanyConfigType0 | Unset):
        profile_config (None | PaginatedCombinedSearchBodyProfileConfigType0 | Unset):
    """

    api_key: str
    company_config: None | PaginatedCombinedSearchBodyCompanyConfigType0 | Unset = UNSET
    profile_config: None | PaginatedCombinedSearchBodyProfileConfigType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_company_config_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0,
        )

        api_key = self.api_key

        company_config: dict[str, Any] | None | Unset
        if isinstance(self.company_config, Unset):
            company_config = UNSET
        elif isinstance(self.company_config, PaginatedCombinedSearchBodyCompanyConfigType0):
            company_config = self.company_config.to_dict()
        else:
            company_config = self.company_config

        profile_config: dict[str, Any] | None | Unset
        if isinstance(self.profile_config, Unset):
            profile_config = UNSET
        elif isinstance(self.profile_config, PaginatedCombinedSearchBodyProfileConfigType0):
            profile_config = self.profile_config.to_dict()
        else:
            profile_config = self.profile_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if company_config is not UNSET:
            field_dict["companyConfig"] = company_config
        if profile_config is not UNSET:
            field_dict["profileConfig"] = profile_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_combined_search_body_company_config_type_0 import (
            PaginatedCombinedSearchBodyCompanyConfigType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0,
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_company_config(data: object) -> None | PaginatedCombinedSearchBodyCompanyConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_config_type_0 = PaginatedCombinedSearchBodyCompanyConfigType0.from_dict(data)

                return company_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyCompanyConfigType0 | Unset, data)

        company_config = _parse_company_config(d.pop("companyConfig", UNSET))

        def _parse_profile_config(data: object) -> None | PaginatedCombinedSearchBodyProfileConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_config_type_0 = PaginatedCombinedSearchBodyProfileConfigType0.from_dict(data)

                return profile_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginatedCombinedSearchBodyProfileConfigType0 | Unset, data)

        profile_config = _parse_profile_config(d.pop("profileConfig", UNSET))

        paginated_combined_search_body = cls(
            api_key=api_key,
            company_config=company_config,
            profile_config=profile_config,
        )

        paginated_combined_search_body.additional_properties = d
        return paginated_combined_search_body

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
