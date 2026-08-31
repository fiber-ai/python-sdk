from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_0 import (
        PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0,
    )
    from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_1 import (
        PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType1,
    )
    from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_field_of_study_type_0 import (
        PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemFieldOfStudyType0,
    )
    from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_keywords_type_0 import (
        PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemKeywordsType0,
    )
    from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0 import (
        PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0,
    )
    from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_years_type_0 import (
        PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0,
    )


T = TypeVar("T", bound="PeopleSearchBodySearchParamsEducationV2Type0AllOfType0Item")


@_attrs_define
class PeopleSearchBodySearchParamsEducationV2Type0AllOfType0Item:
    """
    Attributes:
        keywords (None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemKeywordsType0 | Unset):
        degree (None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0 |
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType1 | Unset):
        field_of_study (None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemFieldOfStudyType0 | Unset):
        school (None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0 | Unset):
        years (None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0 | Unset):
    """

    keywords: None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemKeywordsType0 | Unset = UNSET
    degree: (
        None
        | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0
        | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType1
        | Unset
    ) = UNSET
    field_of_study: None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemFieldOfStudyType0 | Unset = UNSET
    school: None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0 | Unset = UNSET
    years: None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_1 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType1,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_field_of_study_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemFieldOfStudyType0,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_keywords_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemKeywordsType0,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_years_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0,  # noqa: PLC0415
        )

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemKeywordsType0):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        degree: dict[str, Any] | None | Unset
        if isinstance(self.degree, Unset):
            degree = UNSET
        elif isinstance(self.degree, PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0):
            degree = self.degree.to_dict()
        elif isinstance(self.degree, PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType1):
            degree = self.degree.to_dict()
        else:
            degree = self.degree

        field_of_study: dict[str, Any] | None | Unset
        if isinstance(self.field_of_study, Unset):
            field_of_study = UNSET
        elif isinstance(
            self.field_of_study, PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemFieldOfStudyType0
        ):
            field_of_study = self.field_of_study.to_dict()
        else:
            field_of_study = self.field_of_study

        school: dict[str, Any] | None | Unset
        if isinstance(self.school, Unset):
            school = UNSET
        elif isinstance(self.school, PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0):
            school = self.school.to_dict()
        else:
            school = self.school

        years: dict[str, Any] | None | Unset
        if isinstance(self.years, Unset):
            years = UNSET
        elif isinstance(self.years, PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0):
            years = self.years.to_dict()
        else:
            years = self.years

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if degree is not UNSET:
            field_dict["degree"] = degree
        if field_of_study is not UNSET:
            field_dict["fieldOfStudy"] = field_of_study
        if school is not UNSET:
            field_dict["school"] = school
        if years is not UNSET:
            field_dict["years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_degree_type_1 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType1,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_field_of_study_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemFieldOfStudyType0,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_keywords_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemKeywordsType0,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0,  # noqa: PLC0415
        )
        from ..models.people_search_body_search_params_education_v2_type_0_all_of_type_0_item_years_type_0 import (
            PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_keywords(
            data: object,
        ) -> None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemKeywordsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemKeywordsType0.from_dict(
                    data
                )

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemKeywordsType0 | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_degree(
            data: object,
        ) -> (
            None
            | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0
            | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                degree_type_0 = PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0.from_dict(data)

                return degree_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                degree_type_1 = PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType1.from_dict(data)

                return degree_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType0
                | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemDegreeType1
                | Unset,
                data,
            )

        degree = _parse_degree(d.pop("degree", UNSET))

        def _parse_field_of_study(
            data: object,
        ) -> None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemFieldOfStudyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_of_study_type_0 = (
                    PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemFieldOfStudyType0.from_dict(data)
                )

                return field_of_study_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemFieldOfStudyType0 | Unset, data
            )

        field_of_study = _parse_field_of_study(d.pop("fieldOfStudy", UNSET))

        def _parse_school(
            data: object,
        ) -> None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_type_0 = PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0.from_dict(data)

                return school_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0 | Unset, data)

        school = _parse_school(d.pop("school", UNSET))

        def _parse_years(
            data: object,
        ) -> None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_type_0 = PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0.from_dict(data)

                return years_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleSearchBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0 | Unset, data)

        years = _parse_years(d.pop("years", UNSET))

        people_search_body_search_params_education_v2_type_0_all_of_type_0_item = cls(
            keywords=keywords,
            degree=degree,
            field_of_study=field_of_study,
            school=school,
            years=years,
        )

        people_search_body_search_params_education_v2_type_0_all_of_type_0_item.additional_properties = d
        return people_search_body_search_params_education_v2_type_0_all_of_type_0_item

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
