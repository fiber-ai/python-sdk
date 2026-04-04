from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScoutingReportResponse200OutputReportFundingInfoType0")


@_attrs_define
class GetScoutingReportResponse200OutputReportFundingInfoType0:
    """
    Attributes:
        investors (list[str]):
        stage (None | str | Unset):
        total_funding_usd (float | None | Unset):
        last_round_usd (float | None | Unset):
        last_round_date (None | str | Unset):
        description (None | str | Unset):
    """

    investors: list[str]
    stage: None | str | Unset = UNSET
    total_funding_usd: float | None | Unset = UNSET
    last_round_usd: float | None | Unset = UNSET
    last_round_date: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investors = self.investors

        stage: None | str | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        else:
            stage = self.stage

        total_funding_usd: float | None | Unset
        if isinstance(self.total_funding_usd, Unset):
            total_funding_usd = UNSET
        else:
            total_funding_usd = self.total_funding_usd

        last_round_usd: float | None | Unset
        if isinstance(self.last_round_usd, Unset):
            last_round_usd = UNSET
        else:
            last_round_usd = self.last_round_usd

        last_round_date: None | str | Unset
        if isinstance(self.last_round_date, Unset):
            last_round_date = UNSET
        else:
            last_round_date = self.last_round_date

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "investors": investors,
            }
        )
        if stage is not UNSET:
            field_dict["stage"] = stage
        if total_funding_usd is not UNSET:
            field_dict["totalFundingUsd"] = total_funding_usd
        if last_round_usd is not UNSET:
            field_dict["lastRoundUsd"] = last_round_usd
        if last_round_date is not UNSET:
            field_dict["lastRoundDate"] = last_round_date
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        investors = cast(list[str], d.pop("investors"))

        def _parse_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_total_funding_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_funding_usd = _parse_total_funding_usd(d.pop("totalFundingUsd", UNSET))

        def _parse_last_round_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last_round_usd = _parse_last_round_usd(d.pop("lastRoundUsd", UNSET))

        def _parse_last_round_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_round_date = _parse_last_round_date(d.pop("lastRoundDate", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        get_scouting_report_response_200_output_report_funding_info_type_0 = cls(
            investors=investors,
            stage=stage,
            total_funding_usd=total_funding_usd,
            last_round_usd=last_round_usd,
            last_round_date=last_round_date,
            description=description,
        )

        get_scouting_report_response_200_output_report_funding_info_type_0.additional_properties = d
        return get_scouting_report_response_200_output_report_funding_info_type_0

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
