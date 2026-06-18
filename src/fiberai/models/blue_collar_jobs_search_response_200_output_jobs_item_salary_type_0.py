from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0_period_type_1 import (
    BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType1,
)
from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0_period_type_2_type_1 import (
    BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType2Type1,
)
from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0_period_type_3_type_1 import (
    BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0_local_type_0 import (
        BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0LocalType0,
    )
    from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0_usd_type_0 import (
        BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0UsdType0,
    )


T = TypeVar("T", bound="BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0")


@_attrs_define
class BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0:
    """Compensation information. Covers various forms of pay (hourly, daily, monthly, yearly). Null when not listed.

    Attributes:
        text (str): Human-readable salary string as shown on the listing (e.g. '$18 - $22 an hour', 'From $45,000 a
            year').
        local (BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0LocalType0 | None | Unset): Parsed compensation
            in the listed currency. Null when the salary text uses an unrecognized format that could not be parsed into
            structured numbers.
        usd (BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0UsdType0 | None | Unset): Compensation in USD. Null
            when the listing currency is not USD or could not be determined.
        period (BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType1 |
            BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType2Type1 |
            BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType3Type1 | None | Unset): Pay period. Null when
            the listing does not specify a recognizable pay frequency.
    """

    text: str
    local: BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0LocalType0 | None | Unset = UNSET
    usd: BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0UsdType0 | None | Unset = UNSET
    period: (
        BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType1
        | BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType2Type1
        | BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0_local_type_0 import (
            BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0LocalType0,
        )
        from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0_usd_type_0 import (
            BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0UsdType0,
        )

        text = self.text

        local: dict[str, Any] | None | Unset
        if isinstance(self.local, Unset):
            local = UNSET
        elif isinstance(self.local, BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0LocalType0):
            local = self.local.to_dict()
        else:
            local = self.local

        usd: dict[str, Any] | None | Unset
        if isinstance(self.usd, Unset):
            usd = UNSET
        elif isinstance(self.usd, BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0UsdType0):
            usd = self.usd.to_dict()
        else:
            usd = self.usd

        period: None | str | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        elif isinstance(self.period, BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType1):
            period = self.period.value
        elif isinstance(self.period, BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType2Type1):
            period = self.period.value
        elif isinstance(self.period, BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType3Type1):
            period = self.period.value
        else:
            period = self.period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if local is not UNSET:
            field_dict["local"] = local
        if usd is not UNSET:
            field_dict["usd"] = usd
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0_local_type_0 import (
            BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0LocalType0,
        )
        from ..models.blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0_usd_type_0 import (
            BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0UsdType0,
        )

        d = dict(src_dict)
        text = d.pop("text")

        def _parse_local(
            data: object,
        ) -> BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0LocalType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                local_type_0 = BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0LocalType0.from_dict(data)

                return local_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0LocalType0 | None | Unset, data)

        local = _parse_local(d.pop("local", UNSET))

        def _parse_usd(data: object) -> BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0UsdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usd_type_0 = BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0UsdType0.from_dict(data)

                return usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0UsdType0 | None | Unset, data)

        usd = _parse_usd(d.pop("usd", UNSET))

        def _parse_period(
            data: object,
        ) -> (
            BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType1
            | BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType2Type1
            | BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_type_1 = BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType1(data)

                return period_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_type_2_type_1 = BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType2Type1(data)

                return period_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_type_3_type_1 = BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType3Type1(data)

                return period_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType1
                | BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType2Type1
                | BlueCollarJobsSearchResponse200OutputJobsItemSalaryType0PeriodType3Type1
                | None
                | Unset,
                data,
            )

        period = _parse_period(d.pop("period", UNSET))

        blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0 = cls(
            text=text,
            local=local,
            usd=usd,
            period=period,
        )

        blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0.additional_properties = d
        return blue_collar_jobs_search_response_200_output_jobs_item_salary_type_0

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
