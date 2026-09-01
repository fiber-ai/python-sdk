from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instant_contact_reveal_body_enrichment_type import InstantContactRevealBodyEnrichmentType
    from ..models.instant_contact_reveal_body_input_type_0 import InstantContactRevealBodyInputType0
    from ..models.instant_contact_reveal_body_input_type_1 import InstantContactRevealBodyInputType1


T = TypeVar("T", bound="InstantContactRevealBody")


@_attrs_define
class InstantContactRevealBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        input_ (InstantContactRevealBodyInputType0 | InstantContactRevealBodyInputType1): Person lookup parameters. Use
            mode 'linkedin' or 'name-domain'.
        enrichment_type (InstantContactRevealBodyEnrichmentType | Unset): Which email and phone types to look for.
    """

    api_key: str
    input_: InstantContactRevealBodyInputType0 | InstantContactRevealBodyInputType1
    enrichment_type: InstantContactRevealBodyEnrichmentType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.instant_contact_reveal_body_input_type_0 import (
            InstantContactRevealBodyInputType0,  # noqa: PLC0415
        )

        api_key = self.api_key

        input_: dict[str, Any]
        if isinstance(self.input_, InstantContactRevealBodyInputType0):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_.to_dict()

        enrichment_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enrichment_type, Unset):
            enrichment_type = self.enrichment_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "input": input_,
            }
        )
        if enrichment_type is not UNSET:
            field_dict["enrichmentType"] = enrichment_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instant_contact_reveal_body_enrichment_type import (
            InstantContactRevealBodyEnrichmentType,  # noqa: PLC0415
        )
        from ..models.instant_contact_reveal_body_input_type_0 import (
            InstantContactRevealBodyInputType0,  # noqa: PLC0415
        )
        from ..models.instant_contact_reveal_body_input_type_1 import (
            InstantContactRevealBodyInputType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_input_(data: object) -> InstantContactRevealBodyInputType0 | InstantContactRevealBodyInputType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0 = InstantContactRevealBodyInputType0.from_dict(data)

                return input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            input_type_1 = InstantContactRevealBodyInputType1.from_dict(data)

            return input_type_1

        input_ = _parse_input_(d.pop("input"))

        _enrichment_type = d.pop("enrichmentType", UNSET)
        enrichment_type: InstantContactRevealBodyEnrichmentType | Unset
        if isinstance(_enrichment_type, Unset):
            enrichment_type = UNSET
        else:
            enrichment_type = InstantContactRevealBodyEnrichmentType.from_dict(_enrichment_type)

        instant_contact_reveal_body = cls(
            api_key=api_key,
            input_=input_,
            enrichment_type=enrichment_type,
        )

        instant_contact_reveal_body.additional_properties = d
        return instant_contact_reveal_body

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
