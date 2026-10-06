from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.flight_deals_body_discovery_type_0_mode import FlightDealsBodyDiscoveryType0Mode

T = TypeVar("T", bound="FlightDealsBodyDiscoveryType0")


@_attrs_define
class FlightDealsBodyDiscoveryType0:
    """
    Attributes:
        mode (FlightDealsBodyDiscoveryType0Mode):
        free_text (str): Free-text description of the destinations to surface (e.g. 'beaches and islands', 'ski towns in
            the Alps').
    """

    mode: FlightDealsBodyDiscoveryType0Mode
    free_text: str

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        free_text = self.free_text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
                "freeText": free_text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = FlightDealsBodyDiscoveryType0Mode(d.pop("mode"))

        free_text = d.pop("freeText")

        flight_deals_body_discovery_type_0 = cls(
            mode=mode,
            free_text=free_text,
        )

        return flight_deals_body_discovery_type_0
