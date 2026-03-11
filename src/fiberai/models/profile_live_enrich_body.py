from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileLiveEnrichBody")


@_attrs_define
class ProfileLiveEnrichBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        identifier (str): Identifier can be a profile's LinkedIn slug (e.g. 'williamhgates' from
            <linkedin.com/in/williamhgates>), a Sales Navigator URN (e.g. 'ACwAAA.....'), a full LinkedIn URL (e.g.
            'https://www.linkedin.com/in/williamhgates/'), or a LinkedIn user ID (e.g. '443105112')
        get_detailed_education (bool | None | Unset): Whether to include deep details about each educational item, like
            the school's LinkedIn URL, website, location, etc. That'll be put in the detailedEducation array. This slows
            down the API call, so only enable this if you need it. Default: False.
        get_detailed_work_experience (bool | None | Unset): Whether to include deep details about each work experience
            item, like the company's LinkedIn URL, website, location, etc. That'll be put in the detailedWorkExperience
            array. This slows down the API call, so only enable this if you need it. Default: False.
    """

    api_key: str
    identifier: str
    get_detailed_education: bool | None | Unset = False
    get_detailed_work_experience: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        identifier = self.identifier

        get_detailed_education: bool | None | Unset
        if isinstance(self.get_detailed_education, Unset):
            get_detailed_education = UNSET
        else:
            get_detailed_education = self.get_detailed_education

        get_detailed_work_experience: bool | None | Unset
        if isinstance(self.get_detailed_work_experience, Unset):
            get_detailed_work_experience = UNSET
        else:
            get_detailed_work_experience = self.get_detailed_work_experience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "identifier": identifier,
            }
        )
        if get_detailed_education is not UNSET:
            field_dict["getDetailedEducation"] = get_detailed_education
        if get_detailed_work_experience is not UNSET:
            field_dict["getDetailedWorkExperience"] = get_detailed_work_experience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        identifier = d.pop("identifier")

        def _parse_get_detailed_education(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_education = _parse_get_detailed_education(d.pop("getDetailedEducation", UNSET))

        def _parse_get_detailed_work_experience(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_work_experience = _parse_get_detailed_work_experience(d.pop("getDetailedWorkExperience", UNSET))

        profile_live_enrich_body = cls(
            api_key=api_key,
            identifier=identifier,
            get_detailed_education=get_detailed_education,
            get_detailed_work_experience=get_detailed_work_experience,
        )

        profile_live_enrich_body.additional_properties = d
        return profile_live_enrich_body

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
