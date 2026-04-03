from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_1m_type_0 import (
        TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth1MType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_2m_type_0 import (
        TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth2MType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_3m_type_0 import (
        TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth3MType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_6m_type_0 import (
        TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth6MType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_12m_type_0 import (
        TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth12MType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_18m_type_0 import (
        TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth18MType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_24m_type_0 import (
        TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth24MType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_36m_type_0 import (
        TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth36MType0,
    )


T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth")


@_attrs_define
class TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth:
    """
    Attributes:
        field_1m (None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth1MType0 |
            Unset):
        field_2m (None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth2MType0 |
            Unset):
        field_3m (None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth3MType0 |
            Unset):
        field_6m (None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth6MType0 |
            Unset):
        field_12m (None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth12MType0 |
            Unset):
        field_18m (None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth18MType0 |
            Unset):
        field_24m (None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth24MType0 |
            Unset):
        field_36m (None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth36MType0 |
            Unset):
    """

    field_1m: (
        None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth1MType0 | Unset
    ) = UNSET
    field_2m: (
        None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth2MType0 | Unset
    ) = UNSET
    field_3m: (
        None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth3MType0 | Unset
    ) = UNSET
    field_6m: (
        None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth6MType0 | Unset
    ) = UNSET
    field_12m: (
        None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth12MType0 | Unset
    ) = UNSET
    field_18m: (
        None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth18MType0 | Unset
    ) = UNSET
    field_24m: (
        None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth24MType0 | Unset
    ) = UNSET
    field_36m: (
        None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth36MType0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_1m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth1MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_2m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth2MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_3m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth3MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_6m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth6MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_12m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth12MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_18m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth18MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_24m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth24MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_36m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth36MType0,
        )

        field_1m: dict[str, Any] | None | Unset
        if isinstance(self.field_1m, Unset):
            field_1m = UNSET
        elif isinstance(
            self.field_1m, TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth1MType0
        ):
            field_1m = self.field_1m.to_dict()
        else:
            field_1m = self.field_1m

        field_2m: dict[str, Any] | None | Unset
        if isinstance(self.field_2m, Unset):
            field_2m = UNSET
        elif isinstance(
            self.field_2m, TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth2MType0
        ):
            field_2m = self.field_2m.to_dict()
        else:
            field_2m = self.field_2m

        field_3m: dict[str, Any] | None | Unset
        if isinstance(self.field_3m, Unset):
            field_3m = UNSET
        elif isinstance(
            self.field_3m, TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth3MType0
        ):
            field_3m = self.field_3m.to_dict()
        else:
            field_3m = self.field_3m

        field_6m: dict[str, Any] | None | Unset
        if isinstance(self.field_6m, Unset):
            field_6m = UNSET
        elif isinstance(
            self.field_6m, TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth6MType0
        ):
            field_6m = self.field_6m.to_dict()
        else:
            field_6m = self.field_6m

        field_12m: dict[str, Any] | None | Unset
        if isinstance(self.field_12m, Unset):
            field_12m = UNSET
        elif isinstance(
            self.field_12m, TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth12MType0
        ):
            field_12m = self.field_12m.to_dict()
        else:
            field_12m = self.field_12m

        field_18m: dict[str, Any] | None | Unset
        if isinstance(self.field_18m, Unset):
            field_18m = UNSET
        elif isinstance(
            self.field_18m, TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth18MType0
        ):
            field_18m = self.field_18m.to_dict()
        else:
            field_18m = self.field_18m

        field_24m: dict[str, Any] | None | Unset
        if isinstance(self.field_24m, Unset):
            field_24m = UNSET
        elif isinstance(
            self.field_24m, TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth24MType0
        ):
            field_24m = self.field_24m.to_dict()
        else:
            field_24m = self.field_24m

        field_36m: dict[str, Any] | None | Unset
        if isinstance(self.field_36m, Unset):
            field_36m = UNSET
        elif isinstance(
            self.field_36m, TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth36MType0
        ):
            field_36m = self.field_36m.to_dict()
        else:
            field_36m = self.field_36m

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_1m is not UNSET:
            field_dict["1m"] = field_1m
        if field_2m is not UNSET:
            field_dict["2m"] = field_2m
        if field_3m is not UNSET:
            field_dict["3m"] = field_3m
        if field_6m is not UNSET:
            field_dict["6m"] = field_6m
        if field_12m is not UNSET:
            field_dict["12m"] = field_12m
        if field_18m is not UNSET:
            field_dict["18m"] = field_18m
        if field_24m is not UNSET:
            field_dict["24m"] = field_24m
        if field_36m is not UNSET:
            field_dict["36m"] = field_36m

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_1m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth1MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_2m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth2MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_3m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth3MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_6m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth6MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_12m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth12MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_18m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth18MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_24m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth24MType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth_36m_type_0 import (
            TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth36MType0,
        )

        d = dict(src_dict)

        def _parse_field_1m(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth1MType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_1m_type_0 = TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth1MType0.from_dict(
                    data
                )

                return field_1m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth1MType0
                | Unset,
                data,
            )

        field_1m = _parse_field_1m(d.pop("1m", UNSET))

        def _parse_field_2m(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth2MType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_2m_type_0 = TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth2MType0.from_dict(
                    data
                )

                return field_2m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth2MType0
                | Unset,
                data,
            )

        field_2m = _parse_field_2m(d.pop("2m", UNSET))

        def _parse_field_3m(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth3MType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_3m_type_0 = TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth3MType0.from_dict(
                    data
                )

                return field_3m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth3MType0
                | Unset,
                data,
            )

        field_3m = _parse_field_3m(d.pop("3m", UNSET))

        def _parse_field_6m(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth6MType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_6m_type_0 = TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth6MType0.from_dict(
                    data
                )

                return field_6m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth6MType0
                | Unset,
                data,
            )

        field_6m = _parse_field_6m(d.pop("6m", UNSET))

        def _parse_field_12m(
            data: object,
        ) -> (
            None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth12MType0 | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_12m_type_0 = TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth12MType0.from_dict(
                    data
                )

                return field_12m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth12MType0
                | Unset,
                data,
            )

        field_12m = _parse_field_12m(d.pop("12m", UNSET))

        def _parse_field_18m(
            data: object,
        ) -> (
            None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth18MType0 | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_18m_type_0 = TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth18MType0.from_dict(
                    data
                )

                return field_18m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth18MType0
                | Unset,
                data,
            )

        field_18m = _parse_field_18m(d.pop("18m", UNSET))

        def _parse_field_24m(
            data: object,
        ) -> (
            None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth24MType0 | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_24m_type_0 = TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth24MType0.from_dict(
                    data
                )

                return field_24m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth24MType0
                | Unset,
                data,
            )

        field_24m = _parse_field_24m(d.pop("24m", UNSET))

        def _parse_field_36m(
            data: object,
        ) -> (
            None | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth36MType0 | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_36m_type_0 = TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth36MType0.from_dict(
                    data
                )

                return field_36m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCombinedSearchResponse200OutputDataCompaniesItemHistoricalHeadcountType0Growth36MType0
                | Unset,
                data,
            )

        field_36m = _parse_field_36m(d.pop("36m", UNSET))

        text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth = cls(
            field_1m=field_1m,
            field_2m=field_2m,
            field_3m=field_3m,
            field_6m=field_6m,
            field_12m=field_12m,
            field_18m=field_18m,
            field_24m=field_24m,
            field_36m=field_36m,
        )

        text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth.additional_properties = d
        return text_to_combined_search_response_200_output_data_companies_item_historical_headcount_type_0_growth

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
