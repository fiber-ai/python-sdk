from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_accelerators_response_200_output_item_batches_type_0_item import (
        GetAcceleratorsResponse200OutputItemBatchesType0Item,
    )
    from ..models.get_accelerators_response_200_output_item_years_type_0_item import (
        GetAcceleratorsResponse200OutputItemYearsType0Item,
    )


T = TypeVar("T", bound="GetAcceleratorsResponse200OutputItem")


@_attrs_define
class GetAcceleratorsResponse200OutputItem:
    """
    Attributes:
        accelerator_slug (str): The accelerator identifier (e.g., 'y_combinator')
        accelerator_name (str): The human-readable accelerator name (e.g., 'Y Combinator')
        num_companies (int): Total number of companies in this accelerator
        batches (list[GetAcceleratorsResponse200OutputItemBatchesType0Item] | None | Unset): List of batches with
            company counts for this accelerator. Null if the accelerator doesn't use batches.
        years (list[GetAcceleratorsResponse200OutputItemYearsType0Item] | None | Unset): List of years with company
            counts for this accelerator. Null if the accelerator doesn't track years.
        logo_url (None | str | Unset): URL to the accelerator's logo image
        website (None | str | Unset): The accelerator's website URL (includes https:// and www. if applicable)
        other_names (list[str] | None | Unset): Alternate names for the accelerator (e.g., 'YC' for 'Y Combinator')
    """

    accelerator_slug: str
    accelerator_name: str
    num_companies: int
    batches: list[GetAcceleratorsResponse200OutputItemBatchesType0Item] | None | Unset = UNSET
    years: list[GetAcceleratorsResponse200OutputItemYearsType0Item] | None | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    other_names: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accelerator_slug = self.accelerator_slug

        accelerator_name = self.accelerator_name

        num_companies = self.num_companies

        batches: list[dict[str, Any]] | None | Unset
        if isinstance(self.batches, Unset):
            batches = UNSET
        elif isinstance(self.batches, list):
            batches = []
            for batches_type_0_item_data in self.batches:
                batches_type_0_item = batches_type_0_item_data.to_dict()
                batches.append(batches_type_0_item)

        else:
            batches = self.batches

        years: list[dict[str, Any]] | None | Unset
        if isinstance(self.years, Unset):
            years = UNSET
        elif isinstance(self.years, list):
            years = []
            for years_type_0_item_data in self.years:
                years_type_0_item = years_type_0_item_data.to_dict()
                years.append(years_type_0_item)

        else:
            years = self.years

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        other_names: list[str] | None | Unset
        if isinstance(self.other_names, Unset):
            other_names = UNSET
        elif isinstance(self.other_names, list):
            other_names = self.other_names

        else:
            other_names = self.other_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acceleratorSlug": accelerator_slug,
                "acceleratorName": accelerator_name,
                "numCompanies": num_companies,
            }
        )
        if batches is not UNSET:
            field_dict["batches"] = batches
        if years is not UNSET:
            field_dict["years"] = years
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if website is not UNSET:
            field_dict["website"] = website
        if other_names is not UNSET:
            field_dict["otherNames"] = other_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_accelerators_response_200_output_item_batches_type_0_item import (
            GetAcceleratorsResponse200OutputItemBatchesType0Item,
        )
        from ..models.get_accelerators_response_200_output_item_years_type_0_item import (
            GetAcceleratorsResponse200OutputItemYearsType0Item,
        )

        d = dict(src_dict)
        accelerator_slug = d.pop("acceleratorSlug")

        accelerator_name = d.pop("acceleratorName")

        num_companies = d.pop("numCompanies")

        def _parse_batches(data: object) -> list[GetAcceleratorsResponse200OutputItemBatchesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                batches_type_0 = []
                _batches_type_0 = data
                for batches_type_0_item_data in _batches_type_0:
                    batches_type_0_item = GetAcceleratorsResponse200OutputItemBatchesType0Item.from_dict(
                        batches_type_0_item_data
                    )

                    batches_type_0.append(batches_type_0_item)

                return batches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetAcceleratorsResponse200OutputItemBatchesType0Item] | None | Unset, data)

        batches = _parse_batches(d.pop("batches", UNSET))

        def _parse_years(data: object) -> list[GetAcceleratorsResponse200OutputItemYearsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                years_type_0 = []
                _years_type_0 = data
                for years_type_0_item_data in _years_type_0:
                    years_type_0_item = GetAcceleratorsResponse200OutputItemYearsType0Item.from_dict(
                        years_type_0_item_data
                    )

                    years_type_0.append(years_type_0_item)

                return years_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetAcceleratorsResponse200OutputItemYearsType0Item] | None | Unset, data)

        years = _parse_years(d.pop("years", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_other_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                other_names_type_0 = cast(list[str], data)

                return other_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        other_names = _parse_other_names(d.pop("otherNames", UNSET))

        get_accelerators_response_200_output_item = cls(
            accelerator_slug=accelerator_slug,
            accelerator_name=accelerator_name,
            num_companies=num_companies,
            batches=batches,
            years=years,
            logo_url=logo_url,
            website=website,
            other_names=other_names,
        )

        get_accelerators_response_200_output_item.additional_properties = d
        return get_accelerators_response_200_output_item

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
