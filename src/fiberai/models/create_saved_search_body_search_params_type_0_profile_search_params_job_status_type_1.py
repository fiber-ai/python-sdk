from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1_status import (
    CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1_left_at_type_0 import (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType0,
    )
    from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1_left_at_type_1 import (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1")


@_attrs_define
class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1:
    """
    Attributes:
        status (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1Status):
        left_at (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType0 |
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1 | None | Unset):
    """

    status: CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1Status
    left_at: (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType0
        | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1_left_at_type_0 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType0,
        )
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1_left_at_type_1 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1,
        )

        status = self.status.value

        left_at: dict[str, Any] | None | Unset
        if isinstance(self.left_at, Unset):
            left_at = UNSET
        elif isinstance(
            self.left_at, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType0
        ):
            left_at = self.left_at.to_dict()
        elif isinstance(
            self.left_at, CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1
        ):
            left_at = self.left_at.to_dict()
        else:
            left_at = self.left_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if left_at is not UNSET:
            field_dict["leftAt"] = left_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1_left_at_type_0 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType0,
        )
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1_left_at_type_1 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1,
        )

        d = dict(src_dict)
        status = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1Status(d.pop("status"))

        def _parse_left_at(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType0
            | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1
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
                left_at_type_0 = (
                    CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType0.from_dict(data)
                )

                return left_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_at_type_1 = (
                    CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1.from_dict(data)
                )

                return left_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType0
                | CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1
                | None
                | Unset,
                data,
            )

        left_at = _parse_left_at(d.pop("leftAt", UNSET))

        create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1 = cls(
            status=status,
            left_at=left_at,
        )

        create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1.additional_properties = d
        return create_saved_search_body_search_params_type_0_profile_search_params_job_status_type_1

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
