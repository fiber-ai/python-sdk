from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_strategy import (
    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1Strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_window_type_0 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType0,
    )
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_window_type_1 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType1,
    )
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_window_type_2 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType2,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1")


@_attrs_define
class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1:
    """
    Attributes:
        strategy (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1Strategy):
        window (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType0
            | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType1 |
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType2 | None |
            Unset):
    """

    strategy: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1Strategy
    window: (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType0
        | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType1
        | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType2
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_window_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType0,
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_window_type_1 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType1,
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_window_type_2 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType2,
        )

        strategy = self.strategy.value

        window: dict[str, Any] | None | Unset
        if isinstance(self.window, Unset):
            window = UNSET
        elif isinstance(
            self.window,
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType0,
        ):
            window = self.window.to_dict()
        elif isinstance(
            self.window,
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType1,
        ):
            window = self.window.to_dict()
        elif isinstance(
            self.window,
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType2,
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
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_window_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType0,
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_window_type_1 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType1,
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1_window_type_2 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType2,
        )

        d = dict(src_dict)
        strategy = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1Strategy(
            d.pop("strategy")
        )

        def _parse_window(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType0
            | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType1
            | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType2
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
                window_type_0 = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType0.from_dict(
                    data
                )

                return window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_1 = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType1.from_dict(
                    data
                )

                return window_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_2 = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType2.from_dict(
                    data
                )

                return window_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType0
                | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType1
                | CreateSavedSearchBodySearchParamsType2ProfileSearchParamsStealthV2Type1EnteredStealthAtType1WindowType2
                | None
                | Unset,
                data,
            )

        window = _parse_window(d.pop("window", UNSET))

        create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1 = cls(
            strategy=strategy,
            window=window,
        )

        create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1.additional_properties = d
        return create_saved_search_body_search_params_type_2_profile_search_params_stealth_v2_type_1_entered_stealth_at_type_1

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
