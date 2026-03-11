from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_strategy import (
    SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1Strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_window_type_0 import (
        SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0,
    )
    from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_window_type_1 import (
        SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType1,
    )
    from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_window_type_2 import (
        SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType2,
    )


T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1")


@_attrs_define
class SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1:
    """
    Attributes:
        strategy (SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1Strategy):
        window (None | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0 |
            SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType1 |
            SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType2 | Unset):
    """

    strategy: SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1Strategy
    window: (
        None
        | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0
        | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType1
        | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType2
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_window_type_0 import (
            SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0,
        )
        from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_window_type_1 import (
            SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType1,
        )
        from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_window_type_2 import (
            SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType2,
        )

        strategy = self.strategy.value

        window: dict[str, Any] | None | Unset
        if isinstance(self.window, Unset):
            window = UNSET
        elif isinstance(
            self.window, SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0
        ):
            window = self.window.to_dict()
        elif isinstance(
            self.window, SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType1
        ):
            window = self.window.to_dict()
        elif isinstance(
            self.window, SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType2
        ):
            window = self.window.to_dict()
        else:
            window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
            }
        )
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_window_type_0 import (
            SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0,
        )
        from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_window_type_1 import (
            SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType1,
        )
        from ..models.sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1_window_type_2 import (
            SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType2,
        )

        d = dict(src_dict)
        strategy = SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1Strategy(
            d.pop("strategy")
        )

        def _parse_window(
            data: object,
        ) -> (
            None
            | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0
            | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType1
            | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType2
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_0 = SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0.from_dict(
                    data
                )

                return window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_1 = SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType1.from_dict(
                    data
                )

                return window_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_2 = SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType2.from_dict(
                    data
                )

                return window_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0
                | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType1
                | SyncCombinedSearchBodyProfileParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType2
                | Unset,
                data,
            )

        window = _parse_window(d.pop("window", UNSET))

        sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1 = cls(
            strategy=strategy,
            window=window,
        )

        sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1.additional_properties = d
        return sync_combined_search_body_profile_params_education_type_0_any_of_type_0_item_started_school_at_type_1

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
