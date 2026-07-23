from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.funding_round_change import FundingRoundChange


T = TypeVar("T", bound="FundingStageChange")


@_attrs_define
class FundingStageChange:
    """
    Attributes:
        kind (Literal['scalar']):
        previous (bool | None | str): Previous funding stage
        current (bool | None | str): Current funding stage
        current_round_details (FundingRoundChange | None | Unset): Details of the funding round that drove the new
            stage, when available
    """

    kind: Literal["scalar"]
    previous: bool | None | str
    current: bool | None | str
    current_round_details: FundingRoundChange | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.funding_round_change import FundingRoundChange

        kind = self.kind

        previous: bool | None | str
        previous = self.previous

        current: bool | None | str
        current = self.current

        current_round_details: dict[str, Any] | None | Unset
        if isinstance(self.current_round_details, Unset):
            current_round_details = UNSET
        elif isinstance(self.current_round_details, FundingRoundChange):
            current_round_details = self.current_round_details.to_dict()
        else:
            current_round_details = self.current_round_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "previous": previous,
                "current": current,
            }
        )
        if current_round_details is not UNSET:
            field_dict["currentRoundDetails"] = current_round_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.funding_round_change import FundingRoundChange

        d = dict(src_dict)
        kind = cast(Literal["scalar"], d.pop("kind"))
        if kind != "scalar":
            raise ValueError(f"kind must match const 'scalar', got '{kind}'")

        def _parse_previous(data: object) -> bool | None | str:
            if data is None:
                return data
            return cast(bool | None | str, data)

        previous = _parse_previous(d.pop("previous"))

        def _parse_current(data: object) -> bool | None | str:
            if data is None:
                return data
            return cast(bool | None | str, data)

        current = _parse_current(d.pop("current"))

        def _parse_current_round_details(data: object) -> FundingRoundChange | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_round_details_type_0 = FundingRoundChange.from_dict(data)

                return current_round_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FundingRoundChange | None | Unset, data)

        current_round_details = _parse_current_round_details(d.pop("currentRoundDetails", UNSET))

        funding_stage_change = cls(
            kind=kind,
            previous=previous,
            current=current,
            current_round_details=current_round_details,
        )

        funding_stage_change.additional_properties = d
        return funding_stage_change

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
