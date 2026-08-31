from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1_status import (
    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1_left_at_type_0 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType0,
    )
    from ..models.paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1_left_at_type_1 import (
        PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1,
    )


T = TypeVar("T", bound="PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1")


@_attrs_define
class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1:
    """
    Attributes:
        status (PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1Status):
        left_at (None | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType0 |
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1 | Unset):
    """

    status: PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1Status
    left_at: (
        None
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType0
        | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1_left_at_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1_left_at_type_1 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1,  # noqa: PLC0415
        )

        status = self.status.value

        left_at: dict[str, Any] | None | Unset
        if isinstance(self.left_at, Unset):
            left_at = UNSET
        elif isinstance(
            self.left_at, PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType0
        ):
            left_at = self.left_at.to_dict()
        elif isinstance(
            self.left_at, PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1
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
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1_left_at_type_0 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType0,  # noqa: PLC0415
        )
        from ..models.paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1_left_at_type_1 import (
            PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1Status(d.pop("status"))

        def _parse_left_at(
            data: object,
        ) -> (
            None
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType0
            | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1
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
                    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType0.from_dict(data)
                )

                return left_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_at_type_1 = (
                    PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1.from_dict(data)
                )

                return left_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType0
                | PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1
                | Unset,
                data,
            )

        left_at = _parse_left_at(d.pop("leftAt", UNSET))

        paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1 = cls(
            status=status,
            left_at=left_at,
        )

        paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1.additional_properties = d
        return paginated_combined_search_body_profile_config_type_0_search_params_job_status_type_1

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
