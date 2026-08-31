from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lite_contact_reveal_body_patience_type_1 import LiteContactRevealBodyPatienceType1
from ..models.lite_contact_reveal_body_patience_type_2_type_1 import LiteContactRevealBodyPatienceType2Type1
from ..models.lite_contact_reveal_body_patience_type_3_type_1 import LiteContactRevealBodyPatienceType3Type1
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
        enrichment_type (LiteContactRevealBodyEnrichmentType | Unset): Which email and phone types to look for.
        patience (LiteContactRevealBodyPatienceType1 | LiteContactRevealBodyPatienceType2Type1 |
            LiteContactRevealBodyPatienceType3Type1 | None | Unset): How long to wait for email deliverability validation
            after a contact is found. Higher patience increases average response time but improves deliverability accuracy.
            MINIMUM is the least thorough bounce-detection option.
    """

    api_key: str
    input_: LiteContactRevealBodyInputType0 | LiteContactRevealBodyInputType1
    enrichment_type: LiteContactRevealBodyEnrichmentType | Unset = UNSET
    patience: (
        LiteContactRevealBodyPatienceType1
        | LiteContactRevealBodyPatienceType2Type1
        | LiteContactRevealBodyPatienceType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_contact_reveal_body_input_type_0 import LiteContactRevealBodyInputType0  # noqa: PLC0415

        api_key = self.api_key

        input_: dict[str, Any]
        if isinstance(self.input_, LiteContactRevealBodyInputType0):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_.to_dict()

        enrichment_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enrichment_type, Unset):
            enrichment_type = self.enrichment_type.to_dict()

        patience: None | str | Unset
        if isinstance(self.patience, Unset):
            patience = UNSET
        elif isinstance(self.patience, LiteContactRevealBodyPatienceType1):
            patience = self.patience.value
        elif isinstance(self.patience, LiteContactRevealBodyPatienceType2Type1):
            patience = self.patience.value
        elif isinstance(self.patience, LiteContactRevealBodyPatienceType3Type1):
            patience = self.patience.value
        else:
            patience = self.patience

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
        if patience is not UNSET:
            field_dict["patience"] = patience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_contact_reveal_body_enrichment_type import (
            LiteContactRevealBodyEnrichmentType,  # noqa: PLC0415
        )
        from ..models.lite_contact_reveal_body_input_type_0 import LiteContactRevealBodyInputType0  # noqa: PLC0415
        from ..models.lite_contact_reveal_body_input_type_1 import LiteContactRevealBodyInputType1  # noqa: PLC0415

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

        def _parse_patience(
            data: object,
        ) -> (
            LiteContactRevealBodyPatienceType1
            | LiteContactRevealBodyPatienceType2Type1
            | LiteContactRevealBodyPatienceType3Type1
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
                patience_type_1 = LiteContactRevealBodyPatienceType1(data)

                return patience_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_2_type_1 = LiteContactRevealBodyPatienceType2Type1(data)

                return patience_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                patience_type_3_type_1 = LiteContactRevealBodyPatienceType3Type1(data)

                return patience_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LiteContactRevealBodyPatienceType1
                | LiteContactRevealBodyPatienceType2Type1
                | LiteContactRevealBodyPatienceType3Type1
                | None
                | Unset,
                data,
            )

        patience = _parse_patience(d.pop("patience", UNSET))

        lite_contact_reveal_body = cls(
            api_key=api_key,
            input_=input_,
            enrichment_type=enrichment_type,
            patience=patience,
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
