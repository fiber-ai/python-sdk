from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_degree_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType1,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_field_of_study_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_keywords_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_school_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemSchoolType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_years_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0Item")


@_attrs_define
class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0Item:
    """
    Attributes:
        keywords (None |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0 | Unset):
        degree (None |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType0 |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType1 | Unset):
        field_of_study (None |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0 |
            Unset):
        school (None |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemSchoolType0 | Unset):
        years (None | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0
            | Unset):
    """

    keywords: (
        None
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0
        | Unset
    ) = UNSET
    degree: (
        None
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType0
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType1
        | Unset
    ) = UNSET
    field_of_study: (
        None
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0
        | Unset
    ) = UNSET
    school: (
        None
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemSchoolType0
        | Unset
    ) = UNSET
    years: (
        None | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_degree_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType1,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_field_of_study_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_keywords_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_school_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemSchoolType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_years_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0,
        )

        keywords: dict[str, Any] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(
            self.keywords,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0,
        ):
            keywords = self.keywords.to_dict()
        else:
            keywords = self.keywords

        degree: dict[str, Any] | None | Unset
        if isinstance(self.degree, Unset):
            degree = UNSET
        elif isinstance(
            self.degree,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType0,
        ):
            degree = self.degree.to_dict()
        elif isinstance(
            self.degree,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType1,
        ):
            degree = self.degree.to_dict()
        else:
            degree = self.degree

        field_of_study: dict[str, Any] | None | Unset
        if isinstance(self.field_of_study, Unset):
            field_of_study = UNSET
        elif isinstance(
            self.field_of_study,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0,
        ):
            field_of_study = self.field_of_study.to_dict()
        else:
            field_of_study = self.field_of_study

        school: dict[str, Any] | None | Unset
        if isinstance(self.school, Unset):
            school = UNSET
        elif isinstance(
            self.school,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemSchoolType0,
        ):
            school = self.school.to_dict()
        else:
            school = self.school

        years: dict[str, Any] | None | Unset
        if isinstance(self.years, Unset):
            years = UNSET
        elif isinstance(
            self.years,
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0,
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
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_degree_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_degree_type_1 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType1,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_field_of_study_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_keywords_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_school_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemSchoolType0,
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item_years_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0,
        )

        d = dict(src_dict)

        def _parse_keywords(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                keywords_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0.from_dict(
                    data
                )

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemKeywordsType0
                | Unset,
                data,
            )

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_degree(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType0
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                degree_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType0.from_dict(
                    data
                )

                return degree_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                degree_type_1 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType1.from_dict(
                    data
                )

                return degree_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType0
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemDegreeType1
                | Unset,
                data,
            )

        degree = _parse_degree(d.pop("degree", UNSET))

        def _parse_field_of_study(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_of_study_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0.from_dict(
                    data
                )

                return field_of_study_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemFieldOfStudyType0
                | Unset,
                data,
            )

        field_of_study = _parse_field_of_study(d.pop("fieldOfStudy", UNSET))

        def _parse_school(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemSchoolType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemSchoolType0.from_dict(
                    data
                )

                return school_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemSchoolType0
                | Unset,
                data,
            )

        school = _parse_school(d.pop("school", UNSET))

        def _parse_years(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_type_0 = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0.from_dict(
                    data
                )

                return years_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0
                | Unset,
                data,
            )

        years = _parse_years(d.pop("years", UNSET))

        paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item = cls(
            keywords=keywords,
            degree=degree,
            field_of_study=field_of_study,
            school=school,
            years=years,
        )

        paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item.additional_properties = d
        return paginated_combined_search_body_profile_config_type_0_search_params_education_v2_type_0_any_of_type_0_item

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
