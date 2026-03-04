from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_education_type_0_item_school_details_type_0 import KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0ItemSchoolDetailsType0





T = TypeVar("T", bound="KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0Item")



@_attrs_define
class KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0Item:
    """ 
        Attributes:
            school_details (Union['KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0ItemSchoolDetailsType0',
                None, Unset]):
            school_id (Union[None, Unset, str]):
            school_name (Union[None, Unset, str]):
            field_of_study_id (Union[None, Unset, str]):
            field_of_study_name (Union[None, Unset, str]):
            degree (Union[None, Unset, str]):
            grade (Union[None, Unset, str]):
            start_date (Union[None, Unset, str]):
            end_date (Union[None, Unset, str]):
            activities (Union[None, Unset, str]):
            notes (Union[None, Unset, str]):
     """

    school_details: Union['KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0ItemSchoolDetailsType0', None, Unset] = UNSET
    school_id: Union[None, Unset, str] = UNSET
    school_name: Union[None, Unset, str] = UNSET
    field_of_study_id: Union[None, Unset, str] = UNSET
    field_of_study_name: Union[None, Unset, str] = UNSET
    degree: Union[None, Unset, str] = UNSET
    grade: Union[None, Unset, str] = UNSET
    start_date: Union[None, Unset, str] = UNSET
    end_date: Union[None, Unset, str] = UNSET
    activities: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_education_type_0_item_school_details_type_0 import KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0ItemSchoolDetailsType0
        school_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.school_details, Unset):
            school_details = UNSET
        elif isinstance(self.school_details, KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0ItemSchoolDetailsType0):
            school_details = self.school_details.to_dict()
        else:
            school_details = self.school_details

        school_id: Union[None, Unset, str]
        if isinstance(self.school_id, Unset):
            school_id = UNSET
        else:
            school_id = self.school_id

        school_name: Union[None, Unset, str]
        if isinstance(self.school_name, Unset):
            school_name = UNSET
        else:
            school_name = self.school_name

        field_of_study_id: Union[None, Unset, str]
        if isinstance(self.field_of_study_id, Unset):
            field_of_study_id = UNSET
        else:
            field_of_study_id = self.field_of_study_id

        field_of_study_name: Union[None, Unset, str]
        if isinstance(self.field_of_study_name, Unset):
            field_of_study_name = UNSET
        else:
            field_of_study_name = self.field_of_study_name

        degree: Union[None, Unset, str]
        if isinstance(self.degree, Unset):
            degree = UNSET
        else:
            degree = self.degree

        grade: Union[None, Unset, str]
        if isinstance(self.grade, Unset):
            grade = UNSET
        else:
            grade = self.grade

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        activities: Union[None, Unset, str]
        if isinstance(self.activities, Unset):
            activities = UNSET
        else:
            activities = self.activities

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if school_details is not UNSET:
            field_dict["school_details"] = school_details
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
        from ..models.kitchen_sink_profile_response_200_output_data_item_detailed_education_type_0_item_school_details_type_0 import KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0ItemSchoolDetailsType0
        d = dict(src_dict)
        def _parse_school_details(data: object) -> Union['KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0ItemSchoolDetailsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_details_type_0 = KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0ItemSchoolDetailsType0.from_dict(data)



                return school_details_type_0
            except: # noqa: E722
                pass
            return cast(Union['KitchenSinkProfileResponse200OutputDataItemDetailedEducationType0ItemSchoolDetailsType0', None, Unset], data)

        school_details = _parse_school_details(d.pop("school_details", UNSET))


        def _parse_school_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        school_id = _parse_school_id(d.pop("school_id", UNSET))


        def _parse_school_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        school_name = _parse_school_name(d.pop("school_name", UNSET))


        def _parse_field_of_study_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        field_of_study_id = _parse_field_of_study_id(d.pop("field_of_study_id", UNSET))


        def _parse_field_of_study_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        field_of_study_name = _parse_field_of_study_name(d.pop("field_of_study_name", UNSET))


        def _parse_degree(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        degree = _parse_degree(d.pop("degree", UNSET))


        def _parse_grade(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        grade = _parse_grade(d.pop("grade", UNSET))


        def _parse_start_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))


        def _parse_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))


        def _parse_activities(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        activities = _parse_activities(d.pop("activities", UNSET))


        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))


        kitchen_sink_profile_response_200_output_data_item_detailed_education_type_0_item = cls(
            school_details=school_details,
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


        kitchen_sink_profile_response_200_output_data_item_detailed_education_type_0_item.additional_properties = d
        return kitchen_sink_profile_response_200_output_data_item_detailed_education_type_0_item

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
