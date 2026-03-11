from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_tags_response_200_output_company_tags_item import GetTagsResponse200OutputCompanyTagsItem
    from ..models.get_tags_response_200_output_profile_tags_item import GetTagsResponse200OutputProfileTagsItem


T = TypeVar("T", bound="GetTagsResponse200Output")


@_attrs_define
class GetTagsResponse200Output:
    """
    Attributes:
        profile_tags (list[GetTagsResponse200OutputProfileTagsItem]): List of all available profile tags
        company_tags (list[GetTagsResponse200OutputCompanyTagsItem]): List of all available company tags
    """

    profile_tags: list[GetTagsResponse200OutputProfileTagsItem]
    company_tags: list[GetTagsResponse200OutputCompanyTagsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_tags = []
        for profile_tags_item_data in self.profile_tags:
            profile_tags_item = profile_tags_item_data.to_dict()
            profile_tags.append(profile_tags_item)

        company_tags = []
        for company_tags_item_data in self.company_tags:
            company_tags_item = company_tags_item_data.to_dict()
            company_tags.append(company_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileTags": profile_tags,
                "companyTags": company_tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tags_response_200_output_company_tags_item import GetTagsResponse200OutputCompanyTagsItem
        from ..models.get_tags_response_200_output_profile_tags_item import GetTagsResponse200OutputProfileTagsItem

        d = dict(src_dict)
        profile_tags = []
        _profile_tags = d.pop("profileTags")
        for profile_tags_item_data in _profile_tags:
            profile_tags_item = GetTagsResponse200OutputProfileTagsItem.from_dict(profile_tags_item_data)

            profile_tags.append(profile_tags_item)

        company_tags = []
        _company_tags = d.pop("companyTags")
        for company_tags_item_data in _company_tags:
            company_tags_item = GetTagsResponse200OutputCompanyTagsItem.from_dict(company_tags_item_data)

            company_tags.append(company_tags_item)

        get_tags_response_200_output = cls(
            profile_tags=profile_tags,
            company_tags=company_tags,
        )

        get_tags_response_200_output.additional_properties = d
        return get_tags_response_200_output

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
