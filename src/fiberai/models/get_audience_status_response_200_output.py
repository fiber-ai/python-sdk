from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_audience_status_response_200_output_creation_method import (
    GetAudienceStatusResponse200OutputCreationMethod,
)
from ..models.get_audience_status_response_200_output_status import GetAudienceStatusResponse200OutputStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAudienceStatusResponse200Output")


@_attrs_define
class GetAudienceStatusResponse200Output:
    """
    Attributes:
        audience_id (str): Unique ID of the audience
        name (str): Name of the audience
        status (GetAudienceStatusResponse200OutputStatus): Current status of the audience
        creation_method (GetAudienceStatusResponse200OutputCreationMethod): How the audience was created
        created_at (str): When the audience was created
        building_started_at (None | str | Unset): When the audience build started
        building_finished_at (None | str | Unset): When the audience build finished
        companies_count (float | None | Unset): Number of companies in the audience
        prospects_count (float | None | Unset): Number of prospects in the audience
    """

    audience_id: str
    name: str
    status: GetAudienceStatusResponse200OutputStatus
    creation_method: GetAudienceStatusResponse200OutputCreationMethod
    created_at: str
    building_started_at: None | str | Unset = UNSET
    building_finished_at: None | str | Unset = UNSET
    companies_count: float | None | Unset = UNSET
    prospects_count: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience_id = self.audience_id

        name = self.name

        status = self.status.value

        creation_method = self.creation_method.value

        created_at = self.created_at

        building_started_at: None | str | Unset
        if isinstance(self.building_started_at, Unset):
            building_started_at = UNSET
        else:
            building_started_at = self.building_started_at

        building_finished_at: None | str | Unset
        if isinstance(self.building_finished_at, Unset):
            building_finished_at = UNSET
        else:
            building_finished_at = self.building_finished_at

        companies_count: float | None | Unset
        if isinstance(self.companies_count, Unset):
            companies_count = UNSET
        else:
            companies_count = self.companies_count

        prospects_count: float | None | Unset
        if isinstance(self.prospects_count, Unset):
            prospects_count = UNSET
        else:
            prospects_count = self.prospects_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audienceId": audience_id,
                "name": name,
                "status": status,
                "creationMethod": creation_method,
                "createdAt": created_at,
            }
        )
        if building_started_at is not UNSET:
            field_dict["buildingStartedAt"] = building_started_at
        if building_finished_at is not UNSET:
            field_dict["buildingFinishedAt"] = building_finished_at
        if companies_count is not UNSET:
            field_dict["companiesCount"] = companies_count
        if prospects_count is not UNSET:
            field_dict["prospectsCount"] = prospects_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audience_id = d.pop("audienceId")

        name = d.pop("name")

        status = GetAudienceStatusResponse200OutputStatus(d.pop("status"))

        creation_method = GetAudienceStatusResponse200OutputCreationMethod(d.pop("creationMethod"))

        created_at = d.pop("createdAt")

        def _parse_building_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_started_at = _parse_building_started_at(d.pop("buildingStartedAt", UNSET))

        def _parse_building_finished_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_finished_at = _parse_building_finished_at(d.pop("buildingFinishedAt", UNSET))

        def _parse_companies_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        companies_count = _parse_companies_count(d.pop("companiesCount", UNSET))

        def _parse_prospects_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        prospects_count = _parse_prospects_count(d.pop("prospectsCount", UNSET))

        get_audience_status_response_200_output = cls(
            audience_id=audience_id,
            name=name,
            status=status,
            creation_method=creation_method,
            created_at=created_at,
            building_started_at=building_started_at,
            building_finished_at=building_finished_at,
            companies_count=companies_count,
            prospects_count=prospects_count,
        )

        get_audience_status_response_200_output.additional_properties = d
        return get_audience_status_response_200_output

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
