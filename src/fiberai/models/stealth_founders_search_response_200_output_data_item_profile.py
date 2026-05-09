from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stealth_founders_search_response_200_output_data_item_profile_current_job_type_0 import (
        StealthFoundersSearchResponse200OutputDataItemProfileCurrentJobType0,
    )
    from ..models.stealth_founders_search_response_200_output_data_item_profile_education_type_0_item import (
        StealthFoundersSearchResponse200OutputDataItemProfileEducationType0Item,
    )
    from ..models.stealth_founders_search_response_200_output_data_item_profile_experiences_type_0_item import (
        StealthFoundersSearchResponse200OutputDataItemProfileExperiencesType0Item,
    )
    from ..models.stealth_founders_search_response_200_output_data_item_profile_inferred_location_type_0 import (
        StealthFoundersSearchResponse200OutputDataItemProfileInferredLocationType0,
    )


T = TypeVar("T", bound="StealthFoundersSearchResponse200OutputDataItemProfile")


@_attrs_define
class StealthFoundersSearchResponse200OutputDataItemProfile:
    """
    Attributes:
        primary_slug (str):
        user_id (None | str | Unset):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
        name (None | str | Unset):
        headline (None | str | Unset):
        profile_pic (None | str | Unset):
        locality (None | str | Unset):
        inferred_location (None | StealthFoundersSearchResponse200OutputDataItemProfileInferredLocationType0 | Unset):
        experiences (list[StealthFoundersSearchResponse200OutputDataItemProfileExperiencesType0Item] | None | Unset):
        education (list[StealthFoundersSearchResponse200OutputDataItemProfileEducationType0Item] | None | Unset):
        current_job (None | StealthFoundersSearchResponse200OutputDataItemProfileCurrentJobType0 | Unset):
        relevance_score (float | None | Unset):
        last_sort_key (None | str | Unset):
        entity_urn (None | str | Unset):
        detailed_education (list[Any] | None | Unset):
        detailed_work_experiences (list[Any] | None | Unset):
    """

    primary_slug: str
    user_id: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    headline: None | str | Unset = UNSET
    profile_pic: None | str | Unset = UNSET
    locality: None | str | Unset = UNSET
    inferred_location: None | StealthFoundersSearchResponse200OutputDataItemProfileInferredLocationType0 | Unset = UNSET
    experiences: list[StealthFoundersSearchResponse200OutputDataItemProfileExperiencesType0Item] | None | Unset = UNSET
    education: list[StealthFoundersSearchResponse200OutputDataItemProfileEducationType0Item] | None | Unset = UNSET
    current_job: None | StealthFoundersSearchResponse200OutputDataItemProfileCurrentJobType0 | Unset = UNSET
    relevance_score: float | None | Unset = UNSET
    last_sort_key: None | str | Unset = UNSET
    entity_urn: None | str | Unset = UNSET
    detailed_education: list[Any] | None | Unset = UNSET
    detailed_work_experiences: list[Any] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.stealth_founders_search_response_200_output_data_item_profile_current_job_type_0 import (
            StealthFoundersSearchResponse200OutputDataItemProfileCurrentJobType0,
        )
        from ..models.stealth_founders_search_response_200_output_data_item_profile_inferred_location_type_0 import (
            StealthFoundersSearchResponse200OutputDataItemProfileInferredLocationType0,
        )

        primary_slug = self.primary_slug

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        headline: None | str | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        profile_pic: None | str | Unset
        if isinstance(self.profile_pic, Unset):
            profile_pic = UNSET
        else:
            profile_pic = self.profile_pic

        locality: None | str | Unset
        if isinstance(self.locality, Unset):
            locality = UNSET
        else:
            locality = self.locality

        inferred_location: dict[str, Any] | None | Unset
        if isinstance(self.inferred_location, Unset):
            inferred_location = UNSET
        elif isinstance(
            self.inferred_location, StealthFoundersSearchResponse200OutputDataItemProfileInferredLocationType0
        ):
            inferred_location = self.inferred_location.to_dict()
        else:
            inferred_location = self.inferred_location

        experiences: list[dict[str, Any]] | None | Unset
        if isinstance(self.experiences, Unset):
            experiences = UNSET
        elif isinstance(self.experiences, list):
            experiences = []
            for experiences_type_0_item_data in self.experiences:
                experiences_type_0_item = experiences_type_0_item_data.to_dict()
                experiences.append(experiences_type_0_item)

        else:
            experiences = self.experiences

        education: list[dict[str, Any]] | None | Unset
        if isinstance(self.education, Unset):
            education = UNSET
        elif isinstance(self.education, list):
            education = []
            for education_type_0_item_data in self.education:
                education_type_0_item = education_type_0_item_data.to_dict()
                education.append(education_type_0_item)

        else:
            education = self.education

        current_job: dict[str, Any] | None | Unset
        if isinstance(self.current_job, Unset):
            current_job = UNSET
        elif isinstance(self.current_job, StealthFoundersSearchResponse200OutputDataItemProfileCurrentJobType0):
            current_job = self.current_job.to_dict()
        else:
            current_job = self.current_job

        relevance_score: float | None | Unset
        if isinstance(self.relevance_score, Unset):
            relevance_score = UNSET
        else:
            relevance_score = self.relevance_score

        last_sort_key: None | str | Unset
        if isinstance(self.last_sort_key, Unset):
            last_sort_key = UNSET
        else:
            last_sort_key = self.last_sort_key

        entity_urn: None | str | Unset
        if isinstance(self.entity_urn, Unset):
            entity_urn = UNSET
        else:
            entity_urn = self.entity_urn

        detailed_education: list[Any] | None | Unset
        if isinstance(self.detailed_education, Unset):
            detailed_education = UNSET
        elif isinstance(self.detailed_education, list):
            detailed_education = self.detailed_education

        else:
            detailed_education = self.detailed_education

        detailed_work_experiences: list[Any] | None | Unset
        if isinstance(self.detailed_work_experiences, Unset):
            detailed_work_experiences = UNSET
        elif isinstance(self.detailed_work_experiences, list):
            detailed_work_experiences = self.detailed_work_experiences

        else:
            detailed_work_experiences = self.detailed_work_experiences

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "primary_slug": primary_slug,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if name is not UNSET:
            field_dict["name"] = name
        if headline is not UNSET:
            field_dict["headline"] = headline
        if profile_pic is not UNSET:
            field_dict["profile_pic"] = profile_pic
        if locality is not UNSET:
            field_dict["locality"] = locality
        if inferred_location is not UNSET:
            field_dict["inferred_location"] = inferred_location
        if experiences is not UNSET:
            field_dict["experiences"] = experiences
        if education is not UNSET:
            field_dict["education"] = education
        if current_job is not UNSET:
            field_dict["current_job"] = current_job
        if relevance_score is not UNSET:
            field_dict["relevance_score"] = relevance_score
        if last_sort_key is not UNSET:
            field_dict["last_sort_key"] = last_sort_key
        if entity_urn is not UNSET:
            field_dict["entity_urn"] = entity_urn
        if detailed_education is not UNSET:
            field_dict["detailed_education"] = detailed_education
        if detailed_work_experiences is not UNSET:
            field_dict["detailed_work_experiences"] = detailed_work_experiences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stealth_founders_search_response_200_output_data_item_profile_current_job_type_0 import (
            StealthFoundersSearchResponse200OutputDataItemProfileCurrentJobType0,
        )
        from ..models.stealth_founders_search_response_200_output_data_item_profile_education_type_0_item import (
            StealthFoundersSearchResponse200OutputDataItemProfileEducationType0Item,
        )
        from ..models.stealth_founders_search_response_200_output_data_item_profile_experiences_type_0_item import (
            StealthFoundersSearchResponse200OutputDataItemProfileExperiencesType0Item,
        )
        from ..models.stealth_founders_search_response_200_output_data_item_profile_inferred_location_type_0 import (
            StealthFoundersSearchResponse200OutputDataItemProfileInferredLocationType0,
        )

        d = dict(src_dict)
        primary_slug = d.pop("primary_slug")

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_headline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))

        def _parse_profile_pic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_pic = _parse_profile_pic(d.pop("profile_pic", UNSET))

        def _parse_locality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locality = _parse_locality(d.pop("locality", UNSET))

        def _parse_inferred_location(
            data: object,
        ) -> None | StealthFoundersSearchResponse200OutputDataItemProfileInferredLocationType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inferred_location_type_0 = (
                    StealthFoundersSearchResponse200OutputDataItemProfileInferredLocationType0.from_dict(data)
                )

                return inferred_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StealthFoundersSearchResponse200OutputDataItemProfileInferredLocationType0 | Unset, data)

        inferred_location = _parse_inferred_location(d.pop("inferred_location", UNSET))

        def _parse_experiences(
            data: object,
        ) -> list[StealthFoundersSearchResponse200OutputDataItemProfileExperiencesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                experiences_type_0 = []
                _experiences_type_0 = data
                for experiences_type_0_item_data in _experiences_type_0:
                    experiences_type_0_item = (
                        StealthFoundersSearchResponse200OutputDataItemProfileExperiencesType0Item.from_dict(
                            experiences_type_0_item_data
                        )
                    )

                    experiences_type_0.append(experiences_type_0_item)

                return experiences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[StealthFoundersSearchResponse200OutputDataItemProfileExperiencesType0Item] | None | Unset, data
            )

        experiences = _parse_experiences(d.pop("experiences", UNSET))

        def _parse_education(
            data: object,
        ) -> list[StealthFoundersSearchResponse200OutputDataItemProfileEducationType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                education_type_0 = []
                _education_type_0 = data
                for education_type_0_item_data in _education_type_0:
                    education_type_0_item = (
                        StealthFoundersSearchResponse200OutputDataItemProfileEducationType0Item.from_dict(
                            education_type_0_item_data
                        )
                    )

                    education_type_0.append(education_type_0_item)

                return education_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[StealthFoundersSearchResponse200OutputDataItemProfileEducationType0Item] | None | Unset, data
            )

        education = _parse_education(d.pop("education", UNSET))

        def _parse_current_job(
            data: object,
        ) -> None | StealthFoundersSearchResponse200OutputDataItemProfileCurrentJobType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_job_type_0 = StealthFoundersSearchResponse200OutputDataItemProfileCurrentJobType0.from_dict(
                    data
                )

                return current_job_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StealthFoundersSearchResponse200OutputDataItemProfileCurrentJobType0 | Unset, data)

        current_job = _parse_current_job(d.pop("current_job", UNSET))

        def _parse_relevance_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        relevance_score = _parse_relevance_score(d.pop("relevance_score", UNSET))

        def _parse_last_sort_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_sort_key = _parse_last_sort_key(d.pop("last_sort_key", UNSET))

        def _parse_entity_urn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_urn = _parse_entity_urn(d.pop("entity_urn", UNSET))

        def _parse_detailed_education(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                detailed_education_type_0 = cast(list[Any], data)

                return detailed_education_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        detailed_education = _parse_detailed_education(d.pop("detailed_education", UNSET))

        def _parse_detailed_work_experiences(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                detailed_work_experiences_type_0 = cast(list[Any], data)

                return detailed_work_experiences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        detailed_work_experiences = _parse_detailed_work_experiences(d.pop("detailed_work_experiences", UNSET))

        stealth_founders_search_response_200_output_data_item_profile = cls(
            primary_slug=primary_slug,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            name=name,
            headline=headline,
            profile_pic=profile_pic,
            locality=locality,
            inferred_location=inferred_location,
            experiences=experiences,
            education=education,
            current_job=current_job,
            relevance_score=relevance_score,
            last_sort_key=last_sort_key,
            entity_urn=entity_urn,
            detailed_education=detailed_education,
            detailed_work_experiences=detailed_work_experiences,
        )

        stealth_founders_search_response_200_output_data_item_profile.additional_properties = d
        return stealth_founders_search_response_200_output_data_item_profile

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
