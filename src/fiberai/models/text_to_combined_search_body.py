from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.text_to_combined_search_body_company_config import TextToCombinedSearchBodyCompanyConfig
    from ..models.text_to_combined_search_body_profile_config import TextToCombinedSearchBodyProfileConfig


T = TypeVar("T", bound="TextToCombinedSearchBody")


@_attrs_define
class TextToCombinedSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        query (str): Describe what you’re looking for — for example: I want Senior Product Managers from Series A to C
            FinTech startups located in New York.
        company_config (TextToCombinedSearchBodyCompanyConfig):
        profile_config (TextToCombinedSearchBodyProfileConfig):
    """

    api_key: str
    query: str
    company_config: TextToCombinedSearchBodyCompanyConfig
    profile_config: TextToCombinedSearchBodyProfileConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        query = self.query

        company_config = self.company_config.to_dict()

        profile_config = self.profile_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "query": query,
                "companyConfig": company_config,
                "profileConfig": profile_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_body_company_config import TextToCombinedSearchBodyCompanyConfig
        from ..models.text_to_combined_search_body_profile_config import TextToCombinedSearchBodyProfileConfig

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        query = d.pop("query")

        company_config = TextToCombinedSearchBodyCompanyConfig.from_dict(d.pop("companyConfig"))

        profile_config = TextToCombinedSearchBodyProfileConfig.from_dict(d.pop("profileConfig"))

        text_to_combined_search_body = cls(
            api_key=api_key,
            query=query,
            company_config=company_config,
            profile_config=profile_config,
        )

        text_to_combined_search_body.additional_properties = d
        return text_to_combined_search_body

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
