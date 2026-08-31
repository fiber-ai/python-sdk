from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quick_company_resolve_response_200_output_data_item_identifier import (
    QuickCompanyResolveResponse200OutputDataItemIdentifier,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quick_company_resolve_response_200_output_data_item_company_type_0 import (
        QuickCompanyResolveResponse200OutputDataItemCompanyType0,
    )


T = TypeVar("T", bound="QuickCompanyResolveResponse200OutputDataItem")


@_attrs_define
class QuickCompanyResolveResponse200OutputDataItem:
    """
    Attributes:
        identifier (QuickCompanyResolveResponse200OutputDataItemIdentifier): The identifier type you supplied, echoed
            back.
        value (str): The identifier value you supplied, echoed back.
        found (bool):
        company (None | QuickCompanyResolveResponse200OutputDataItemCompanyType0 | Unset):
    """

    identifier: QuickCompanyResolveResponse200OutputDataItemIdentifier
    value: str
    found: bool
    company: None | QuickCompanyResolveResponse200OutputDataItemCompanyType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0 import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0,  # noqa: PLC0415
        )

        identifier = self.identifier.value

        value = self.value

        found = self.found

        company: dict[str, Any] | None | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        elif isinstance(self.company, QuickCompanyResolveResponse200OutputDataItemCompanyType0):
            company = self.company.to_dict()
        else:
            company = self.company

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "value": value,
                "found": found,
            }
        )
        if company is not UNSET:
            field_dict["company"] = company

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_company_resolve_response_200_output_data_item_company_type_0 import (
            QuickCompanyResolveResponse200OutputDataItemCompanyType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        identifier = QuickCompanyResolveResponse200OutputDataItemIdentifier(d.pop("identifier"))

        value = d.pop("value")

        found = d.pop("found")

        def _parse_company(data: object) -> None | QuickCompanyResolveResponse200OutputDataItemCompanyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = QuickCompanyResolveResponse200OutputDataItemCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QuickCompanyResolveResponse200OutputDataItemCompanyType0 | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        quick_company_resolve_response_200_output_data_item = cls(
            identifier=identifier,
            value=value,
            found=found,
            company=company,
        )

        quick_company_resolve_response_200_output_data_item.additional_properties = d
        return quick_company_resolve_response_200_output_data_item

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
