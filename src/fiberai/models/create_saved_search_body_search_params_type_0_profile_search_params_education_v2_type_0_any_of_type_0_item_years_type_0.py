from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_finished_school_at_type_0 import (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType0,
    )
    from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_finished_school_at_type_1 import (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1,
    )
    from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_started_school_at_type_0 import (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType0,
    )
    from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_started_school_at_type_1 import (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType1,
    )


T = TypeVar(
    "T", bound="CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0"
)


@_attrs_define
class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0:
    """
    Attributes:
        started_school_at (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsT
            ype0StartedSchoolAtType0 | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0It
            emYearsType0StartedSchoolAtType1 | None | Unset):
        finished_school_at (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYears
            Type0FinishedSchoolAtType0 | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0
            ItemYearsType0FinishedSchoolAtType1 | None | Unset):
        is_currently_student (bool | None | Unset):
    """

    started_school_at: (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType0
        | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType1
        | None
        | Unset
    ) = UNSET
    finished_school_at: (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType0
        | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1
        | None
        | Unset
    ) = UNSET
    is_currently_student: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_finished_school_at_type_0 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_finished_school_at_type_1 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_started_school_at_type_0 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_started_school_at_type_1 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType1,  # noqa: PLC0415
        )

        started_school_at: dict[str, Any] | None | Unset
        if isinstance(self.started_school_at, Unset):
            started_school_at = UNSET
        elif isinstance(
            self.started_school_at,
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType0,
        ):
            started_school_at = self.started_school_at.to_dict()
        elif isinstance(
            self.started_school_at,
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType1,
        ):
            started_school_at = self.started_school_at.to_dict()
        else:
            started_school_at = self.started_school_at

        finished_school_at: dict[str, Any] | None | Unset
        if isinstance(self.finished_school_at, Unset):
            finished_school_at = UNSET
        elif isinstance(
            self.finished_school_at,
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType0,
        ):
            finished_school_at = self.finished_school_at.to_dict()
        elif isinstance(
            self.finished_school_at,
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1,
        ):
            finished_school_at = self.finished_school_at.to_dict()
        else:
            finished_school_at = self.finished_school_at

        is_currently_student: bool | None | Unset
        if isinstance(self.is_currently_student, Unset):
            is_currently_student = UNSET
        else:
            is_currently_student = self.is_currently_student

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if started_school_at is not UNSET:
            field_dict["startedSchoolAt"] = started_school_at
        if finished_school_at is not UNSET:
            field_dict["finishedSchoolAt"] = finished_school_at
        if is_currently_student is not UNSET:
            field_dict["isCurrentlyStudent"] = is_currently_student

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_finished_school_at_type_0 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_finished_school_at_type_1 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_started_school_at_type_0 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0_started_school_at_type_1 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType1,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_started_school_at(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType0
            | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType1
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
                started_school_at_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType0.from_dict(
                    data
                )

                return started_school_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_school_at_type_1 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType1.from_dict(
                    data
                )

                return started_school_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType0
                | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType1
                | None
                | Unset,
                data,
            )

        started_school_at = _parse_started_school_at(d.pop("startedSchoolAt", UNSET))

        def _parse_finished_school_at(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType0
            | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1
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
                finished_school_at_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType0.from_dict(
                    data
                )

                return finished_school_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                finished_school_at_type_1 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1.from_dict(
                    data
                )

                return finished_school_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType0
                | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1
                | None
                | Unset,
                data,
            )

        finished_school_at = _parse_finished_school_at(d.pop("finishedSchoolAt", UNSET))

        def _parse_is_currently_student(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_currently_student = _parse_is_currently_student(d.pop("isCurrentlyStudent", UNSET))

        create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0 = cls(
            started_school_at=started_school_at,
            finished_school_at=finished_school_at,
            is_currently_student=is_currently_student,
        )

        create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_0_profile_search_params_education_v2_type_0_any_of_type_0_item_years_type_0

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
