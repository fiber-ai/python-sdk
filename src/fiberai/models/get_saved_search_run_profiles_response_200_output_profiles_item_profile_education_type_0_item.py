from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSavedSearchRunProfilesResponse200OutputProfilesItemProfileEducationType0Item")


@_attrs_define
class GetSavedSearchRunProfilesResponse200OutputProfilesItemProfileEducationType0Item:
    """
    Attributes:
        school_id (None | str | Unset):
        school_name (None | str | Unset):
        field_of_study_id (None | str | Unset):
        field_of_study_name (None | str | Unset):
        degree (None | str | Unset):
        grade (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        activities (None | str | Unset):
        notes (None | str | Unset):
    """

    school_id: None | str | Unset = UNSET
    school_name: None | str | Unset = UNSET
    field_of_study_id: None | str | Unset = UNSET
    field_of_study_name: None | str | Unset = UNSET
    degree: None | str | Unset = UNSET
    grade: None | str | Unset = UNSET
    start_date: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    activities: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        school_id: None | str | Unset
        if isinstance(self.school_id, Unset):
            school_id = UNSET
        else:
            school_id = self.school_id

        school_name: None | str | Unset
        if isinstance(self.school_name, Unset):
            school_name = UNSET
        else:
            school_name = self.school_name

        field_of_study_id: None | str | Unset
        if isinstance(self.field_of_study_id, Unset):
            field_of_study_id = UNSET
        else:
            field_of_study_id = self.field_of_study_id

        field_of_study_name: None | str | Unset
        if isinstance(self.field_of_study_name, Unset):
            field_of_study_name = UNSET
        else:
            field_of_study_name = self.field_of_study_name

        degree: None | str | Unset
        if isinstance(self.degree, Unset):
            degree = UNSET
        else:
            degree = self.degree

        grade: None | str | Unset
        if isinstance(self.grade, Unset):
            grade = UNSET
        else:
            grade = self.grade

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        activities: None | str | Unset
        if isinstance(self.activities, Unset):
            activities = UNSET
        else:
            activities = self.activities

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if school_id is not UNSET:
            field_dict["school_id"] = school_id
        if school_name is not UNSET:
            field_dict["school_name"] = school_name
        if field_of_study_id is not UNSET:
            field_dict["field_of_study_id"] = field_of_study_id
        if field_of_study_name is not UNSET:
            field_dict["field_of_study_name"] = field_of_study_name
        if degree is not UNSET:
            field_dict["degree"] = degree
        if grade is not UNSET:
            field_dict["grade"] = grade
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if activities is not UNSET:
            field_dict["activities"] = activities
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_school_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_id = _parse_school_id(d.pop("school_id", UNSET))

        def _parse_school_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name = _parse_school_name(d.pop("school_name", UNSET))

        def _parse_field_of_study_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_of_study_id = _parse_field_of_study_id(d.pop("field_of_study_id", UNSET))

        def _parse_field_of_study_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_of_study_name = _parse_field_of_study_name(d.pop("field_of_study_name", UNSET))

        def _parse_degree(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        degree = _parse_degree(d.pop("degree", UNSET))

        def _parse_grade(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grade = _parse_grade(d.pop("grade", UNSET))

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_activities(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activities = _parse_activities(d.pop("activities", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        get_saved_search_run_profiles_response_200_output_profiles_item_profile_education_type_0_item = cls(
            school_id=school_id,
            school_name=school_name,
            field_of_study_id=field_of_study_id,
            field_of_study_name=field_of_study_name,
            degree=degree,
            grade=grade,
            start_date=start_date,
            end_date=end_date,
            activities=activities,
            notes=notes,
        )

        get_saved_search_run_profiles_response_200_output_profiles_item_profile_education_type_0_item.additional_properties = d
        return get_saved_search_run_profiles_response_200_output_profiles_item_profile_education_type_0_item

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
