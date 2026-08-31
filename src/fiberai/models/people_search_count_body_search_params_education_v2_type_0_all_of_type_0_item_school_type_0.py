from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0_exact_type_0 import (
        PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0ExactType0,
    )
    from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0_name_keywords_type_0 import (
        PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0NameKeywordsType0,
    )
    from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0_properties_type_0 import (
        PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0PropertiesType0,
    )


T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0")


@_attrs_define
class PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0:
    """
    Attributes:
        exact (None | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0ExactType0 | Unset):
        name_keywords (None |
            PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0NameKeywordsType0 | Unset):
        properties (None | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0PropertiesType0 |
            Unset):
    """

    exact: None | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0ExactType0 | Unset = UNSET
    name_keywords: (
        None | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0NameKeywordsType0 | Unset
    ) = UNSET
    properties: (
        None | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0PropertiesType0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0_exact_type_0 import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0ExactType0,  # noqa: PLC0415
        )
        from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0_name_keywords_type_0 import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0NameKeywordsType0,  # noqa: PLC0415
        )
        from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0_properties_type_0 import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0PropertiesType0,  # noqa: PLC0415
        )

        exact: dict[str, Any] | None | Unset
        if isinstance(self.exact, Unset):
            exact = UNSET
        elif isinstance(
            self.exact, PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0ExactType0
        ):
            exact = self.exact.to_dict()
        else:
            exact = self.exact

        name_keywords: dict[str, Any] | None | Unset
        if isinstance(self.name_keywords, Unset):
            name_keywords = UNSET
        elif isinstance(
            self.name_keywords,
            PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0NameKeywordsType0,
        ):
            name_keywords = self.name_keywords.to_dict()
        else:
            name_keywords = self.name_keywords

        properties: dict[str, Any] | None | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(
            self.properties, PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0PropertiesType0
        ):
            properties = self.properties.to_dict()
        else:
            properties = self.properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exact is not UNSET:
            field_dict["exact"] = exact
        if name_keywords is not UNSET:
            field_dict["nameKeywords"] = name_keywords
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0_exact_type_0 import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0ExactType0,  # noqa: PLC0415
        )
        from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0_name_keywords_type_0 import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0NameKeywordsType0,  # noqa: PLC0415
        )
        from ..models.people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0_properties_type_0 import (
            PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0PropertiesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_exact(
            data: object,
        ) -> None | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0ExactType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exact_type_0 = (
                    PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0ExactType0.from_dict(data)
                )

                return exact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0ExactType0 | Unset,
                data,
            )

        exact = _parse_exact(d.pop("exact", UNSET))

        def _parse_name_keywords(
            data: object,
        ) -> None | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0NameKeywordsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_keywords_type_0 = PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0NameKeywordsType0.from_dict(
                    data
                )

                return name_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0NameKeywordsType0
                | Unset,
                data,
            )

        name_keywords = _parse_name_keywords(d.pop("nameKeywords", UNSET))

        def _parse_properties(
            data: object,
        ) -> None | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0PropertiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = (
                    PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0PropertiesType0.from_dict(
                        data
                    )
                )

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemSchoolType0PropertiesType0
                | Unset,
                data,
            )

        properties = _parse_properties(d.pop("properties", UNSET))

        people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0 = cls(
            exact=exact,
            name_keywords=name_keywords,
            properties=properties,
        )

        people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0.additional_properties = d
        return people_search_count_body_search_params_education_v2_type_0_all_of_type_0_item_school_type_0

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
