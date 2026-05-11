from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lite_contact_reveal_body_enrichment_type import LiteContactRevealBodyEnrichmentType
    from ..models.lite_contact_reveal_body_input_type_0 import LiteContactRevealBodyInputType0
    from ..models.lite_contact_reveal_body_input_type_1 import LiteContactRevealBodyInputType1


T = TypeVar("T", bound="LiteContactRevealBody")


@_attrs_define
class LiteContactRevealBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        input_ (LiteContactRevealBodyInputType0 | LiteContactRevealBodyInputType1): Person lookup parameters. Use mode
            'linkedin' or 'name-domain'.
        enrichment_type (LiteContactRevealBodyEnrichmentType | Unset): Which email types to look for.
    """

    api_key: str
    input_: LiteContactRevealBodyInputType0 | LiteContactRevealBodyInputType1
    enrichment_type: LiteContactRevealBodyEnrichmentType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_contact_reveal_body_input_type_0 import LiteContactRevealBodyInputType0

        api_key = self.api_key

        input_: dict[str, Any]
        if isinstance(self.input_, LiteContactRevealBodyInputType0):
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
        from ..models.lite_contact_reveal_body_enrichment_type import LiteContactRevealBodyEnrichmentType
        from ..models.lite_contact_reveal_body_input_type_0 import LiteContactRevealBodyInputType0
        from ..models.lite_contact_reveal_body_input_type_1 import LiteContactRevealBodyInputType1

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_input_(data: object) -> LiteContactRevealBodyInputType0 | LiteContactRevealBodyInputType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0 = LiteContactRevealBodyInputType0.from_dict(data)

                return input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            input_type_1 = LiteContactRevealBodyInputType1.from_dict(data)

            return input_type_1

        input_ = _parse_input_(d.pop("input"))

        _enrichment_type = d.pop("enrichmentType", UNSET)
        enrichment_type: LiteContactRevealBodyEnrichmentType | Unset
        if isinstance(_enrichment_type, Unset):
            enrichment_type = UNSET
        else:
            enrichment_type = LiteContactRevealBodyEnrichmentType.from_dict(_enrichment_type)

        lite_contact_reveal_body = cls(
            api_key=api_key,
            input_=input_,
            enrichment_type=enrichment_type,
        )

        lite_contact_reveal_body.additional_properties = d
        return lite_contact_reveal_body

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
