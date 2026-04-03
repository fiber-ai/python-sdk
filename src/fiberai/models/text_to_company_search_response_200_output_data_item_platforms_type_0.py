from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextToCompanySearchResponse200OutputDataItemPlatformsType0")


@_attrs_define
class TextToCompanySearchResponse200OutputDataItemPlatformsType0:
    """
    Attributes:
        ecommerce (list[str] | None | Unset):
        cms (list[str] | None | Unset):
        crm (list[str] | None | Unset):
        marketing (list[str] | None | Unset):
        payment (list[str] | None | Unset):
    """

    ecommerce: list[str] | None | Unset = UNSET
    cms: list[str] | None | Unset = UNSET
    crm: list[str] | None | Unset = UNSET
    marketing: list[str] | None | Unset = UNSET
    payment: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ecommerce: list[str] | None | Unset
        if isinstance(self.ecommerce, Unset):
            ecommerce = UNSET
        elif isinstance(self.ecommerce, list):
            ecommerce = self.ecommerce

        else:
            ecommerce = self.ecommerce

        cms: list[str] | None | Unset
        if isinstance(self.cms, Unset):
            cms = UNSET
        elif isinstance(self.cms, list):
            cms = self.cms

        else:
            cms = self.cms

        crm: list[str] | None | Unset
        if isinstance(self.crm, Unset):
            crm = UNSET
        elif isinstance(self.crm, list):
            crm = self.crm

        else:
            crm = self.crm

        marketing: list[str] | None | Unset
        if isinstance(self.marketing, Unset):
            marketing = UNSET
        elif isinstance(self.marketing, list):
            marketing = self.marketing

        else:
            marketing = self.marketing

        payment: list[str] | None | Unset
        if isinstance(self.payment, Unset):
            payment = UNSET
        elif isinstance(self.payment, list):
            payment = self.payment

        else:
            payment = self.payment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ecommerce is not UNSET:
            field_dict["ecommerce"] = ecommerce
        if cms is not UNSET:
            field_dict["cms"] = cms
        if crm is not UNSET:
            field_dict["crm"] = crm
        if marketing is not UNSET:
            field_dict["marketing"] = marketing
        if payment is not UNSET:
            field_dict["payment"] = payment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ecommerce(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ecommerce_type_0 = cast(list[str], data)

                return ecommerce_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ecommerce = _parse_ecommerce(d.pop("ecommerce", UNSET))

        def _parse_cms(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cms_type_0 = cast(list[str], data)

                return cms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cms = _parse_cms(d.pop("cms", UNSET))

        def _parse_crm(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                crm_type_0 = cast(list[str], data)

                return crm_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        crm = _parse_crm(d.pop("crm", UNSET))

        def _parse_marketing(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                marketing_type_0 = cast(list[str], data)

                return marketing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        marketing = _parse_marketing(d.pop("marketing", UNSET))

        def _parse_payment(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payment_type_0 = cast(list[str], data)

                return payment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        payment = _parse_payment(d.pop("payment", UNSET))

        text_to_company_search_response_200_output_data_item_platforms_type_0 = cls(
            ecommerce=ecommerce,
            cms=cms,
            crm=crm,
            marketing=marketing,
            payment=payment,
        )

        text_to_company_search_response_200_output_data_item_platforms_type_0.additional_properties = d
        return text_to_company_search_response_200_output_data_item_platforms_type_0

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
