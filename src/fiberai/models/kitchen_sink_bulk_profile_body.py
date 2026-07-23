from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kitchen_sink_bulk_profile_body_thoroughness_type_1 import KitchenSinkBulkProfileBodyThoroughnessType1
from ..models.kitchen_sink_bulk_profile_body_thoroughness_type_2_type_1 import (
    KitchenSinkBulkProfileBodyThoroughnessType2Type1,
)
from ..models.kitchen_sink_bulk_profile_body_thoroughness_type_3_type_1 import (
    KitchenSinkBulkProfileBodyThoroughnessType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kitchen_sink_bulk_profile_body_profiles_item import KitchenSinkBulkProfileBodyProfilesItem


T = TypeVar("T", bound="KitchenSinkBulkProfileBody")


@_attrs_define
class KitchenSinkBulkProfileBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        profiles (list[KitchenSinkBulkProfileBodyProfilesItem]):
        live_fetch (bool | None | Unset): When true, triggers a real-time LinkedIn profile fetch. Costs additional
            credits. Useful for profiles not yet in the database or to get the freshest data. Default: False.
        force_company_match (bool | None | Unset): When true, requires that the matched profile works at the specified
            company. Without this, the API may return profiles that match by name but work elsewhere. Default: False.
        fuzzy_search (bool | None | Unset): When true, enables fuzzy name matching. Useful when exact name spelling is
            uncertain. Default: False.
        thoroughness (KitchenSinkBulkProfileBodyThoroughnessType1 | KitchenSinkBulkProfileBodyThoroughnessType2Type1 |
            KitchenSinkBulkProfileBodyThoroughnessType3Type1 | None | Unset): Controls how thoroughly to search across all
            profiles in the batch. Higher values recover more matches at the cost of additional per-row latency; lower
            values return faster. Omit to use the recommended default. Default:
            KitchenSinkBulkProfileBodyThoroughnessType1.LOW.
        get_detailed_education (bool | None | Unset): When true, returns detailed_education[] with school_details for
            each education entry. Default: False.
        get_detailed_work_experience (bool | None | Unset): When true, returns detailed_work_experiences[] with
            company_details (domains, preferred_name, linkedin_primary_slug, li_org_id) for each work experience. Use this
            to get company domains for a person. Default: False.
    """

    api_key: str
    profiles: list[KitchenSinkBulkProfileBodyProfilesItem]
    live_fetch: bool | None | Unset = False
    force_company_match: bool | None | Unset = False
    fuzzy_search: bool | None | Unset = False
    thoroughness: (
        KitchenSinkBulkProfileBodyThoroughnessType1
        | KitchenSinkBulkProfileBodyThoroughnessType2Type1
        | KitchenSinkBulkProfileBodyThoroughnessType3Type1
        | None
        | Unset
    ) = KitchenSinkBulkProfileBodyThoroughnessType1.LOW
    get_detailed_education: bool | None | Unset = False
    get_detailed_work_experience: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        profiles = []
        for profiles_item_data in self.profiles:
            profiles_item = profiles_item_data.to_dict()
            profiles.append(profiles_item)

        live_fetch: bool | None | Unset
        if isinstance(self.live_fetch, Unset):
            live_fetch = UNSET
        else:
            live_fetch = self.live_fetch

        force_company_match: bool | None | Unset
        if isinstance(self.force_company_match, Unset):
            force_company_match = UNSET
        else:
            force_company_match = self.force_company_match

        fuzzy_search: bool | None | Unset
        if isinstance(self.fuzzy_search, Unset):
            fuzzy_search = UNSET
        else:
            fuzzy_search = self.fuzzy_search

        thoroughness: None | str | Unset
        if isinstance(self.thoroughness, Unset):
            thoroughness = UNSET
        elif isinstance(self.thoroughness, KitchenSinkBulkProfileBodyThoroughnessType1):
            thoroughness = self.thoroughness.value
        elif isinstance(self.thoroughness, KitchenSinkBulkProfileBodyThoroughnessType2Type1):
            thoroughness = self.thoroughness.value
        elif isinstance(self.thoroughness, KitchenSinkBulkProfileBodyThoroughnessType3Type1):
            thoroughness = self.thoroughness.value
        else:
            thoroughness = self.thoroughness

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
                "profiles": profiles,
            }
        )
        if live_fetch is not UNSET:
            field_dict["liveFetch"] = live_fetch
        if force_company_match is not UNSET:
            field_dict["forceCompanyMatch"] = force_company_match
        if fuzzy_search is not UNSET:
            field_dict["fuzzySearch"] = fuzzy_search
        if thoroughness is not UNSET:
            field_dict["thoroughness"] = thoroughness
        if get_detailed_education is not UNSET:
            field_dict["getDetailedEducation"] = get_detailed_education
        if get_detailed_work_experience is not UNSET:
            field_dict["getDetailedWorkExperience"] = get_detailed_work_experience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_bulk_profile_body_profiles_item import KitchenSinkBulkProfileBodyProfilesItem

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in _profiles:
            profiles_item = KitchenSinkBulkProfileBodyProfilesItem.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        def _parse_live_fetch(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        live_fetch = _parse_live_fetch(d.pop("liveFetch", UNSET))

        def _parse_force_company_match(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force_company_match = _parse_force_company_match(d.pop("forceCompanyMatch", UNSET))

        def _parse_fuzzy_search(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        fuzzy_search = _parse_fuzzy_search(d.pop("fuzzySearch", UNSET))

        def _parse_thoroughness(
            data: object,
        ) -> (
            KitchenSinkBulkProfileBodyThoroughnessType1
            | KitchenSinkBulkProfileBodyThoroughnessType2Type1
            | KitchenSinkBulkProfileBodyThoroughnessType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                thoroughness_type_1 = KitchenSinkBulkProfileBodyThoroughnessType1(data)

                return thoroughness_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                thoroughness_type_2_type_1 = KitchenSinkBulkProfileBodyThoroughnessType2Type1(data)

                return thoroughness_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                thoroughness_type_3_type_1 = KitchenSinkBulkProfileBodyThoroughnessType3Type1(data)

                return thoroughness_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KitchenSinkBulkProfileBodyThoroughnessType1
                | KitchenSinkBulkProfileBodyThoroughnessType2Type1
                | KitchenSinkBulkProfileBodyThoroughnessType3Type1
                | None
                | Unset,
                data,
            )

        thoroughness = _parse_thoroughness(d.pop("thoroughness", UNSET))

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

        kitchen_sink_bulk_profile_body = cls(
            api_key=api_key,
            profiles=profiles,
            live_fetch=live_fetch,
            force_company_match=force_company_match,
            fuzzy_search=fuzzy_search,
            thoroughness=thoroughness,
            get_detailed_education=get_detailed_education,
            get_detailed_work_experience=get_detailed_work_experience,
        )

        kitchen_sink_bulk_profile_body.additional_properties = d
        return kitchen_sink_bulk_profile_body

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
