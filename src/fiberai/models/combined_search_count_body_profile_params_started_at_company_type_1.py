from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_search_count_body_profile_params_started_at_company_type_1_strategy import (
    CombinedSearchCountBodyProfileParamsStartedAtCompanyType1Strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_search_count_body_profile_params_started_at_company_type_1_window_type_0 import (
        CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType0,
    )
    from ..models.combined_search_count_body_profile_params_started_at_company_type_1_window_type_1 import (
        CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType1,
    )
    from ..models.combined_search_count_body_profile_params_started_at_company_type_1_window_type_2 import (
        CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType2,
    )


T = TypeVar("T", bound="CombinedSearchCountBodyProfileParamsStartedAtCompanyType1")


@_attrs_define
class CombinedSearchCountBodyProfileParamsStartedAtCompanyType1:
    """
    Attributes:
        strategy (CombinedSearchCountBodyProfileParamsStartedAtCompanyType1Strategy):
        window (CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType0 |
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType1 |
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType2 | None | Unset):
    """

    strategy: CombinedSearchCountBodyProfileParamsStartedAtCompanyType1Strategy
    window: (
        CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType0
        | CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType1
        | CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType2
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.combined_search_count_body_profile_params_started_at_company_type_1_window_type_0 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType0,  # noqa: PLC0415
        )
        from ..models.combined_search_count_body_profile_params_started_at_company_type_1_window_type_1 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType1,  # noqa: PLC0415
        )
        from ..models.combined_search_count_body_profile_params_started_at_company_type_1_window_type_2 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType2,  # noqa: PLC0415
        )

        strategy = self.strategy.value

        window: dict[str, Any] | None | Unset
        if isinstance(self.window, Unset):
            window = UNSET
        elif isinstance(self.window, CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType0):
            window = self.window.to_dict()
        elif isinstance(self.window, CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType1):
            window = self.window.to_dict()
        elif isinstance(self.window, CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType2):
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
        from ..models.combined_search_count_body_profile_params_started_at_company_type_1_window_type_0 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType0,  # noqa: PLC0415
        )
        from ..models.combined_search_count_body_profile_params_started_at_company_type_1_window_type_1 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType1,  # noqa: PLC0415
        )
        from ..models.combined_search_count_body_profile_params_started_at_company_type_1_window_type_2 import (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType2,  # noqa: PLC0415
        )

        d = dict(src_dict)
        strategy = CombinedSearchCountBodyProfileParamsStartedAtCompanyType1Strategy(d.pop("strategy"))

        def _parse_window(
            data: object,
        ) -> (
            CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType0
            | CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType1
            | CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType2
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
                window_type_0 = CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType0.from_dict(data)

                return window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_1 = CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType1.from_dict(data)

                return window_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                window_type_2 = CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType2.from_dict(data)

                return window_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType0
                | CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType1
                | CombinedSearchCountBodyProfileParamsStartedAtCompanyType1WindowType2
                | None
                | Unset,
                data,
            )

        window = _parse_window(d.pop("window", UNSET))

        combined_search_count_body_profile_params_started_at_company_type_1 = cls(
            strategy=strategy,
            window=window,
        )

        combined_search_count_body_profile_params_started_at_company_type_1.additional_properties = d
        return combined_search_count_body_profile_params_started_at_company_type_1

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
