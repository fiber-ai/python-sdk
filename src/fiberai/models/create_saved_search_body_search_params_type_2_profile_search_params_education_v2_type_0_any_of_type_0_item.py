from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_degree_type_0 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType0,
    )
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType1,
    )
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_field_of_study_type_0 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0,
    )
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_keywords_type_0 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0,
    )
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_school_type_0 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemSchoolType0,
    )
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0Item")


@_attrs_define
class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0Item:
    """
    Attributes:
        keywords (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0 |
            None | Unset):
        degree (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType0 |
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType1 | None |
            Unset):
        field_of_study
            (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0 | None
            | Unset):
        school (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemSchoolType0 |
            None | Unset):
        years (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0 | None
            | Unset):
    """

    keywords: (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0
        | None
        | Unset
    ) = UNSET
    degree: (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType0
        | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType1
        | None
        | Unset
    ) = UNSET
    field_of_study: (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0
        | None
        | Unset
    ) = UNSET
    school: (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemSchoolType0
        | None
        | Unset
    ) = UNSET
    years: (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_degree_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType1,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_field_of_study_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_keywords_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_school_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemSchoolType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0,  # noqa: PLC0415
        )

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(
            self.keywords,
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0,
        ):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        degree: dict[str, Any] | None | Unset
        if isinstance(self.degree, Unset):
            degree = UNSET
        elif isinstance(
            self.degree,
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType0,
        ):
            degree = self.degree.to_dict()
        elif isinstance(
            self.degree,
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType1,
        ):
            degree = self.degree.to_dict()
        else:
            degree = self.degree

        field_of_study: dict[str, Any] | None | Unset
        if isinstance(self.field_of_study, Unset):
            field_of_study = UNSET
        elif isinstance(
            self.field_of_study,
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0,
        ):
            field_of_study = self.field_of_study.to_dict()
        else:
            field_of_study = self.field_of_study

        school: dict[str, Any] | None | Unset
        if isinstance(self.school, Unset):
            school = UNSET
        elif isinstance(
            self.school,
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemSchoolType0,
        ):
            school = self.school.to_dict()
        else:
            school = self.school

        years: dict[str, Any] | None | Unset
        if isinstance(self.years, Unset):
            years = UNSET
        elif isinstance(
            self.years,
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0,
        ):
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
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_degree_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType1,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_field_of_study_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_keywords_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_school_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemSchoolType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_keywords(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0.from_dict(
                    data
                )

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0
                | None
                | Unset,
                data,
            )

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_degree(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType0
            | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                degree_type_0 = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType0.from_dict(
                    data
                )

                return degree_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                degree_type_1 = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType1.from_dict(
                    data
                )

                return degree_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType0
                | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemDegreeType1
                | None
                | Unset,
                data,
            )

        degree = _parse_degree(d.pop("degree", UNSET))

        def _parse_field_of_study(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_of_study_type_0 = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0.from_dict(
                    data
                )

                return field_of_study_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0
                | None
                | Unset,
                data,
            )

        field_of_study = _parse_field_of_study(d.pop("fieldOfStudy", UNSET))

        def _parse_school(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemSchoolType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_type_0 = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemSchoolType0.from_dict(
                    data
                )

                return school_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemSchoolType0
                | None
                | Unset,
                data,
            )

        school = _parse_school(d.pop("school", UNSET))

        def _parse_years(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_type_0 = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0.from_dict(
                    data
                )

                return years_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType2ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0
                | None
                | Unset,
                data,
            )

        years = _parse_years(d.pop("years", UNSET))

        create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item = (
            cls(
                keywords=keywords,
                degree=degree,
                field_of_study=field_of_study,
                school=school,
                years=years,
            )
        )

        create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item.additional_properties = d
        return (
            create_saved_search_body_search_params_type_2_profile_search_params_education_v2_type_0_any_of_type_0_item
        )

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
