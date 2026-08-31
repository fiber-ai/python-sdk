from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_talent_flow_response_200_output_breakdowns_by_metro_item_centroid_type_0 import (
        GetTalentFlowResponse200OutputBreakdownsByMetroItemCentroidType0,
    )


T = TypeVar("T", bound="GetTalentFlowResponse200OutputBreakdownsByMetroItem")


@_attrs_define
class GetTalentFlowResponse200OutputBreakdownsByMetroItem:
    """
    Attributes:
        slug (str): Region identifier. Preset metros use slugs like 'sf-bay-area'; non-preset metros are clustered and
            use 'unknown-metro' with centroid coordinates; profiles with no location use 'no-location'.
        name (str): Metro area display name.
        count (int): Number of people in this metro area.
        percent (float): Percentage of total people (0-100).
        centroid (GetTalentFlowResponse200OutputBreakdownsByMetroItemCentroidType0 | None | Unset): Centroid coordinates
            for clustered metros. Null for preset regions and no-location.
    """

    slug: str
    name: str
    count: int
    percent: float
    centroid: GetTalentFlowResponse200OutputBreakdownsByMetroItemCentroidType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_talent_flow_response_200_output_breakdowns_by_metro_item_centroid_type_0 import (
            GetTalentFlowResponse200OutputBreakdownsByMetroItemCentroidType0,  # noqa: PLC0415
        )

        slug = self.slug

        name = self.name

        count = self.count

        percent = self.percent

        centroid: dict[str, Any] | None | Unset
        if isinstance(self.centroid, Unset):
            centroid = UNSET
        elif isinstance(self.centroid, GetTalentFlowResponse200OutputBreakdownsByMetroItemCentroidType0):
            centroid = self.centroid.to_dict()
        else:
            centroid = self.centroid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "count": count,
                "percent": percent,
            }
        )
        if centroid is not UNSET:
            field_dict["centroid"] = centroid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_talent_flow_response_200_output_breakdowns_by_metro_item_centroid_type_0 import (
            GetTalentFlowResponse200OutputBreakdownsByMetroItemCentroidType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        count = d.pop("count")

        percent = d.pop("percent")

        def _parse_centroid(
            data: object,
        ) -> GetTalentFlowResponse200OutputBreakdownsByMetroItemCentroidType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                centroid_type_0 = GetTalentFlowResponse200OutputBreakdownsByMetroItemCentroidType0.from_dict(data)

                return centroid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTalentFlowResponse200OutputBreakdownsByMetroItemCentroidType0 | None | Unset, data)

        centroid = _parse_centroid(d.pop("centroid", UNSET))

        get_talent_flow_response_200_output_breakdowns_by_metro_item = cls(
            slug=slug,
            name=name,
            count=count,
            percent=percent,
            centroid=centroid,
        )

        get_talent_flow_response_200_output_breakdowns_by_metro_item.additional_properties = d
        return get_talent_flow_response_200_output_breakdowns_by_metro_item

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
