from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_audiences_response_200_output_audiences_item_creation_method import (
    ListAudiencesResponse200OutputAudiencesItemCreationMethod,
)
from ..models.list_audiences_response_200_output_audiences_item_status import (
    ListAudiencesResponse200OutputAudiencesItemStatus,
)

T = TypeVar("T", bound="ListAudiencesResponse200OutputAudiencesItem")


@_attrs_define
class ListAudiencesResponse200OutputAudiencesItem:
    """
    Attributes:
        audience_id (str): Unique ID of the audience
        name (str): Name of the audience
        status (ListAudiencesResponse200OutputAudiencesItemStatus): Current status of the audience
        creation_method (ListAudiencesResponse200OutputAudiencesItemCreationMethod): How the audience was created
        created_at (str): When the audience was created
        companies_count (float): Number of companies
        prospects_count (float): Number of prospects
    """

    audience_id: str
    name: str
    status: ListAudiencesResponse200OutputAudiencesItemStatus
    creation_method: ListAudiencesResponse200OutputAudiencesItemCreationMethod
    created_at: str
    companies_count: float
    prospects_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience_id = self.audience_id

        name = self.name

        status = self.status.value

        creation_method = self.creation_method.value

        created_at = self.created_at

        companies_count = self.companies_count

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
                "companiesCount": companies_count,
                "prospectsCount": prospects_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audience_id = d.pop("audienceId")

        name = d.pop("name")

        status = ListAudiencesResponse200OutputAudiencesItemStatus(d.pop("status"))

        creation_method = ListAudiencesResponse200OutputAudiencesItemCreationMethod(d.pop("creationMethod"))

        created_at = d.pop("createdAt")

        companies_count = d.pop("companiesCount")

        prospects_count = d.pop("prospectsCount")

        list_audiences_response_200_output_audiences_item = cls(
            audience_id=audience_id,
            name=name,
            status=status,
            creation_method=creation_method,
            created_at=created_at,
            companies_count=companies_count,
            prospects_count=prospects_count,
        )

        list_audiences_response_200_output_audiences_item.additional_properties = d
        return list_audiences_response_200_output_audiences_item

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
