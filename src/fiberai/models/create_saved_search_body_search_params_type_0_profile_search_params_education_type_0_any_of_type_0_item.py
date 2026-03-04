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
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_started_school_at_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType0
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_school_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_school_name_keywords_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolNameKeywordsType0
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_started_school_at_type_1 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_degree_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemDegreeType0
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_keywords_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemKeywordsType0





T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0Item")



@_attrs_define
class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0Item:
    """ 
        Attributes:
            school
                (Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0', None,
                Unset]):
            keywords
                (Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemKeywordsType0',
                None, Unset]):
            degree
                (Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemDegreeType0', None,
                Unset]):
            school_name_keywords (Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0It
                emSchoolNameKeywordsType0', None, Unset]):
            finished_school_at (Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0Item
                FinishedSchoolAtType0',
                'CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1',
                None, Unset]):
            started_school_at (Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemS
                tartedSchoolAtType0',
                'CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1',
                None, Unset]):
            is_currently_student (Union[None, Unset, bool]):
     """

    school: Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0', None, Unset] = UNSET
    keywords: Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemKeywordsType0', None, Unset] = UNSET
    degree: Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemDegreeType0', None, Unset] = UNSET
    school_name_keywords: Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolNameKeywordsType0', None, Unset] = UNSET
    finished_school_at: Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0', 'CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1', None, Unset] = UNSET
    started_school_at: Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType0', 'CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1', None, Unset] = UNSET
    is_currently_student: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_started_school_at_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_school_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_school_name_keywords_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolNameKeywordsType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_started_school_at_type_1 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_degree_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemDegreeType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_keywords_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemKeywordsType0
        school: Union[None, Unset, dict[str, Any]]
        if isinstance(self.school, Unset):
            school = UNSET
        elif isinstance(self.school, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0):
            school = self.school.to_dict()
        else:
            school = self.school

        keywords: Union[None, Unset, dict[str, Any]]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        degree: Union[None, Unset, dict[str, Any]]
        if isinstance(self.degree, Unset):
            degree = UNSET
        elif isinstance(self.degree, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemDegreeType0):
            degree = self.degree.to_dict()
        else:
            degree = self.degree

        school_name_keywords: Union[None, Unset, dict[str, Any]]
        if isinstance(self.school_name_keywords, Unset):
            school_name_keywords = UNSET
        elif isinstance(self.school_name_keywords, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolNameKeywordsType0):
            school_name_keywords = self.school_name_keywords.to_dict()
        else:
            school_name_keywords = self.school_name_keywords

        finished_school_at: Union[None, Unset, dict[str, Any]]
        if isinstance(self.finished_school_at, Unset):
            finished_school_at = UNSET
        elif isinstance(self.finished_school_at, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0):
            finished_school_at = self.finished_school_at.to_dict()
        elif isinstance(self.finished_school_at, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1):
            finished_school_at = self.finished_school_at.to_dict()
        else:
            finished_school_at = self.finished_school_at

        started_school_at: Union[None, Unset, dict[str, Any]]
        if isinstance(self.started_school_at, Unset):
            started_school_at = UNSET
        elif isinstance(self.started_school_at, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType0):
            started_school_at = self.started_school_at.to_dict()
        elif isinstance(self.started_school_at, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1):
            started_school_at = self.started_school_at.to_dict()
        else:
            started_school_at = self.started_school_at

        is_currently_student: Union[None, Unset, bool]
        if isinstance(self.is_currently_student, Unset):
            is_currently_student = UNSET
        else:
            is_currently_student = self.is_currently_student


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if school is not UNSET:
            field_dict["school"] = school
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if degree is not UNSET:
            field_dict["degree"] = degree
        if school_name_keywords is not UNSET:
            field_dict["schoolNameKeywords"] = school_name_keywords
        if finished_school_at is not UNSET:
            field_dict["finishedSchoolAt"] = finished_school_at
        if started_school_at is not UNSET:
            field_dict["startedSchoolAt"] = started_school_at
        if is_currently_student is not UNSET:
            field_dict["isCurrentlyStudent"] = is_currently_student

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_started_school_at_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_school_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_school_name_keywords_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolNameKeywordsType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_started_school_at_type_1 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_finished_school_at_type_1 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_degree_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemDegreeType0
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item_keywords_type_0 import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemKeywordsType0
        d = dict(src_dict)
        def _parse_school(data: object) -> Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0.from_dict(data)



                return school_type_0
            except: # noqa: E722
                pass
            return cast(Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolType0', None, Unset], data)

        school = _parse_school(d.pop("school", UNSET))


        def _parse_keywords(data: object) -> Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemKeywordsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemKeywordsType0.from_dict(data)



                return keywords_type_0
            except: # noqa: E722
                pass
            return cast(Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemKeywordsType0', None, Unset], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        def _parse_degree(data: object) -> Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemDegreeType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                degree_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemDegreeType0.from_dict(data)



                return degree_type_0
            except: # noqa: E722
                pass
            return cast(Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemDegreeType0', None, Unset], data)

        degree = _parse_degree(d.pop("degree", UNSET))


        def _parse_school_name_keywords(data: object) -> Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolNameKeywordsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_name_keywords_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolNameKeywordsType0.from_dict(data)



                return school_name_keywords_type_0
            except: # noqa: E722
                pass
            return cast(Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemSchoolNameKeywordsType0', None, Unset], data)

        school_name_keywords = _parse_school_name_keywords(d.pop("schoolNameKeywords", UNSET))


        def _parse_finished_school_at(data: object) -> Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0', 'CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                finished_school_at_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0.from_dict(data)



                return finished_school_at_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                finished_school_at_type_1 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1.from_dict(data)



                return finished_school_at_type_1
            except: # noqa: E722
                pass
            return cast(Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType0', 'CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemFinishedSchoolAtType1', None, Unset], data)

        finished_school_at = _parse_finished_school_at(d.pop("finishedSchoolAt", UNSET))


        def _parse_started_school_at(data: object) -> Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType0', 'CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_school_at_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType0.from_dict(data)



                return started_school_at_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_school_at_type_1 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1.from_dict(data)



                return started_school_at_type_1
            except: # noqa: E722
                pass
            return cast(Union['CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType0', 'CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1', None, Unset], data)

        started_school_at = _parse_started_school_at(d.pop("startedSchoolAt", UNSET))


        def _parse_is_currently_student(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_currently_student = _parse_is_currently_student(d.pop("isCurrentlyStudent", UNSET))


        create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item = cls(
            school=school,
            keywords=keywords,
            degree=degree,
            school_name_keywords=school_name_keywords,
            finished_school_at=finished_school_at,
            started_school_at=started_school_at,
            is_currently_student=is_currently_student,
        )


        create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item.additional_properties = d
        return create_saved_search_body_search_params_type_0_profile_search_params_education_type_0_any_of_type_0_item

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
