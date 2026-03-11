from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kitchen_sink_company_response_200_output_data_item_accelerators_type_0_item_founders_type_0_item import (
        KitchenSinkCompanyResponse200OutputDataItemAcceleratorsType0ItemFoundersType0Item,
    )


T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemAcceleratorsType0Item")


@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemAcceleratorsType0Item:
    """
    Attributes:
        id (None | str | Unset):
        slug (None | str | Unset):
        tags (list[str] | None | Unset):
        year (float | None | Unset):
        batch (None | str | Unset):
        founders (list[KitchenSinkCompanyResponse200OutputDataItemAcceleratorsType0ItemFoundersType0Item] | None |
            Unset):
        description (None | str | Unset):
        one_liner (None | str | Unset):
        company_name (None | str | Unset):
        company_domain (None | str | Unset):
        accelerator_name (None | str | Unset):
        accelerator_domain (None | str | Unset):
    """

    id: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    year: float | None | Unset = UNSET
    batch: None | str | Unset = UNSET
    founders: list[KitchenSinkCompanyResponse200OutputDataItemAcceleratorsType0ItemFoundersType0Item] | None | Unset = (
        UNSET
    )
    description: None | str | Unset = UNSET
    one_liner: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    company_domain: None | str | Unset = UNSET
    accelerator_name: None | str | Unset = UNSET
    accelerator_domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        year: float | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        batch: None | str | Unset
        if isinstance(self.batch, Unset):
            batch = UNSET
        else:
            batch = self.batch

        founders: list[dict[str, Any]] | None | Unset
        if isinstance(self.founders, Unset):
            founders = UNSET
        elif isinstance(self.founders, list):
            founders = []
            for founders_type_0_item_data in self.founders:
                founders_type_0_item = founders_type_0_item_data.to_dict()
                founders.append(founders_type_0_item)

        else:
            founders = self.founders

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        one_liner: None | str | Unset
        if isinstance(self.one_liner, Unset):
            one_liner = UNSET
        else:
            one_liner = self.one_liner

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_domain: None | str | Unset
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        else:
            company_domain = self.company_domain

        accelerator_name: None | str | Unset
        if isinstance(self.accelerator_name, Unset):
            accelerator_name = UNSET
        else:
            accelerator_name = self.accelerator_name

        accelerator_domain: None | str | Unset
        if isinstance(self.accelerator_domain, Unset):
            accelerator_domain = UNSET
        else:
            accelerator_domain = self.accelerator_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if tags is not UNSET:
            field_dict["tags"] = tags
        if year is not UNSET:
            field_dict["year"] = year
        if batch is not UNSET:
            field_dict["batch"] = batch
        if founders is not UNSET:
            field_dict["founders"] = founders
        if description is not UNSET:
            field_dict["description"] = description
        if one_liner is not UNSET:
            field_dict["one_liner"] = one_liner
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_domain is not UNSET:
            field_dict["company_domain"] = company_domain
        if accelerator_name is not UNSET:
            field_dict["accelerator_name"] = accelerator_name
        if accelerator_domain is not UNSET:
            field_dict["accelerator_domain"] = accelerator_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_company_response_200_output_data_item_accelerators_type_0_item_founders_type_0_item import (
            KitchenSinkCompanyResponse200OutputDataItemAcceleratorsType0ItemFoundersType0Item,
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))

        def _parse_batch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch = _parse_batch(d.pop("batch", UNSET))

        def _parse_founders(
            data: object,
        ) -> list[KitchenSinkCompanyResponse200OutputDataItemAcceleratorsType0ItemFoundersType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                founders_type_0 = []
                _founders_type_0 = data
                for founders_type_0_item_data in _founders_type_0:
                    founders_type_0_item = (
                        KitchenSinkCompanyResponse200OutputDataItemAcceleratorsType0ItemFoundersType0Item.from_dict(
                            founders_type_0_item_data
                        )
                    )

                    founders_type_0.append(founders_type_0_item)

                return founders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[KitchenSinkCompanyResponse200OutputDataItemAcceleratorsType0ItemFoundersType0Item] | None | Unset,
                data,
            )

        founders = _parse_founders(d.pop("founders", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_one_liner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        one_liner = _parse_one_liner(d.pop("one_liner", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_company_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_domain = _parse_company_domain(d.pop("company_domain", UNSET))

        def _parse_accelerator_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accelerator_name = _parse_accelerator_name(d.pop("accelerator_name", UNSET))

        def _parse_accelerator_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accelerator_domain = _parse_accelerator_domain(d.pop("accelerator_domain", UNSET))

        kitchen_sink_company_response_200_output_data_item_accelerators_type_0_item = cls(
            id=id,
            slug=slug,
            tags=tags,
            year=year,
            batch=batch,
            founders=founders,
            description=description,
            one_liner=one_liner,
            company_name=company_name,
            company_domain=company_domain,
            accelerator_name=accelerator_name,
            accelerator_domain=accelerator_domain,
        )

        kitchen_sink_company_response_200_output_data_item_accelerators_type_0_item.additional_properties = d
        return kitchen_sink_company_response_200_output_data_item_accelerators_type_0_item

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
