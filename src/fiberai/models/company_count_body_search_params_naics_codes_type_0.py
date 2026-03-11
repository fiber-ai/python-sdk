from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_count_body_search_params_naics_codes_type_0_all_of_type_0_item import (
        CompanyCountBodySearchParamsNaicsCodesType0AllOfType0Item,
    )
    from ..models.company_count_body_search_params_naics_codes_type_0_any_of_type_0_item import (
        CompanyCountBodySearchParamsNaicsCodesType0AnyOfType0Item,
    )
    from ..models.company_count_body_search_params_naics_codes_type_0_none_of_type_0_item import (
        CompanyCountBodySearchParamsNaicsCodesType0NoneOfType0Item,
    )


T = TypeVar("T", bound="CompanyCountBodySearchParamsNaicsCodesType0")


@_attrs_define
class CompanyCountBodySearchParamsNaicsCodesType0:
    """
    Attributes:
        any_of (list[CompanyCountBodySearchParamsNaicsCodesType0AnyOfType0Item] | None | Unset):
        all_of (list[CompanyCountBodySearchParamsNaicsCodesType0AllOfType0Item] | None | Unset):
        none_of (list[CompanyCountBodySearchParamsNaicsCodesType0NoneOfType0Item] | None | Unset):
    """

    any_of: list[CompanyCountBodySearchParamsNaicsCodesType0AnyOfType0Item] | None | Unset = UNSET
    all_of: list[CompanyCountBodySearchParamsNaicsCodesType0AllOfType0Item] | None | Unset = UNSET
    none_of: list[CompanyCountBodySearchParamsNaicsCodesType0NoneOfType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        any_of: list[dict[str, Any]] | None | Unset
        if isinstance(self.any_of, Unset):
            any_of = UNSET
        elif isinstance(self.any_of, list):
            any_of = []
            for any_of_type_0_item_data in self.any_of:
                any_of_type_0_item = any_of_type_0_item_data.to_dict()
                any_of.append(any_of_type_0_item)

        else:
            any_of = self.any_of

        all_of: list[dict[str, Any]] | None | Unset
        if isinstance(self.all_of, Unset):
            all_of = UNSET
        elif isinstance(self.all_of, list):
            all_of = []
            for all_of_type_0_item_data in self.all_of:
                all_of_type_0_item = all_of_type_0_item_data.to_dict()
                all_of.append(all_of_type_0_item)

        else:
            all_of = self.all_of

        none_of: list[dict[str, Any]] | None | Unset
        if isinstance(self.none_of, Unset):
            none_of = UNSET
        elif isinstance(self.none_of, list):
            none_of = []
            for none_of_type_0_item_data in self.none_of:
                none_of_type_0_item = none_of_type_0_item_data.to_dict()
                none_of.append(none_of_type_0_item)

        else:
            none_of = self.none_of

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if any_of is not UNSET:
            field_dict["anyOf"] = any_of
        if all_of is not UNSET:
            field_dict["allOf"] = all_of
        if none_of is not UNSET:
            field_dict["noneOf"] = none_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_count_body_search_params_naics_codes_type_0_all_of_type_0_item import (
            CompanyCountBodySearchParamsNaicsCodesType0AllOfType0Item,
        )
        from ..models.company_count_body_search_params_naics_codes_type_0_any_of_type_0_item import (
            CompanyCountBodySearchParamsNaicsCodesType0AnyOfType0Item,
        )
        from ..models.company_count_body_search_params_naics_codes_type_0_none_of_type_0_item import (
            CompanyCountBodySearchParamsNaicsCodesType0NoneOfType0Item,
        )

        d = dict(src_dict)

        def _parse_any_of(
            data: object,
        ) -> list[CompanyCountBodySearchParamsNaicsCodesType0AnyOfType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                any_of_type_0 = []
                _any_of_type_0 = data
                for any_of_type_0_item_data in _any_of_type_0:
                    any_of_type_0_item = CompanyCountBodySearchParamsNaicsCodesType0AnyOfType0Item.from_dict(
                        any_of_type_0_item_data
                    )

                    any_of_type_0.append(any_of_type_0_item)

                return any_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyCountBodySearchParamsNaicsCodesType0AnyOfType0Item] | None | Unset, data)

        any_of = _parse_any_of(d.pop("anyOf", UNSET))

        def _parse_all_of(
            data: object,
        ) -> list[CompanyCountBodySearchParamsNaicsCodesType0AllOfType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                all_of_type_0 = []
                _all_of_type_0 = data
                for all_of_type_0_item_data in _all_of_type_0:
                    all_of_type_0_item = CompanyCountBodySearchParamsNaicsCodesType0AllOfType0Item.from_dict(
                        all_of_type_0_item_data
                    )

                    all_of_type_0.append(all_of_type_0_item)

                return all_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyCountBodySearchParamsNaicsCodesType0AllOfType0Item] | None | Unset, data)

        all_of = _parse_all_of(d.pop("allOf", UNSET))

        def _parse_none_of(
            data: object,
        ) -> list[CompanyCountBodySearchParamsNaicsCodesType0NoneOfType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                none_of_type_0 = []
                _none_of_type_0 = data
                for none_of_type_0_item_data in _none_of_type_0:
                    none_of_type_0_item = CompanyCountBodySearchParamsNaicsCodesType0NoneOfType0Item.from_dict(
                        none_of_type_0_item_data
                    )

                    none_of_type_0.append(none_of_type_0_item)

                return none_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyCountBodySearchParamsNaicsCodesType0NoneOfType0Item] | None | Unset, data)

        none_of = _parse_none_of(d.pop("noneOf", UNSET))

        company_count_body_search_params_naics_codes_type_0 = cls(
            any_of=any_of,
            all_of=all_of,
            none_of=none_of,
        )

        company_count_body_search_params_naics_codes_type_0.additional_properties = d
        return company_count_body_search_params_naics_codes_type_0

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
