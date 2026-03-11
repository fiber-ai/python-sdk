from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_search_body_search_params_employee_trends_type_0_obeys_all_type_0_item import (
        CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAllType0Item,
    )
    from ..models.company_search_body_search_params_employee_trends_type_0_obeys_any_type_0_item import (
        CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0Item,
    )
    from ..models.company_search_body_search_params_employee_trends_type_0_obeys_none_type_0_item import (
        CompanySearchBodySearchParamsEmployeeTrendsType0ObeysNoneType0Item,
    )


T = TypeVar("T", bound="CompanySearchBodySearchParamsEmployeeTrendsType0")


@_attrs_define
class CompanySearchBodySearchParamsEmployeeTrendsType0:
    """
    Attributes:
        obeys_all (list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAllType0Item] | None | Unset):
        obeys_any (list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0Item] | None | Unset):
        obeys_none (list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysNoneType0Item] | None | Unset):
    """

    obeys_all: list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAllType0Item] | None | Unset = UNSET
    obeys_any: list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0Item] | None | Unset = UNSET
    obeys_none: list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysNoneType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        obeys_all: list[dict[str, Any]] | None | Unset
        if isinstance(self.obeys_all, Unset):
            obeys_all = UNSET
        elif isinstance(self.obeys_all, list):
            obeys_all = []
            for obeys_all_type_0_item_data in self.obeys_all:
                obeys_all_type_0_item = obeys_all_type_0_item_data.to_dict()
                obeys_all.append(obeys_all_type_0_item)

        else:
            obeys_all = self.obeys_all

        obeys_any: list[dict[str, Any]] | None | Unset
        if isinstance(self.obeys_any, Unset):
            obeys_any = UNSET
        elif isinstance(self.obeys_any, list):
            obeys_any = []
            for obeys_any_type_0_item_data in self.obeys_any:
                obeys_any_type_0_item = obeys_any_type_0_item_data.to_dict()
                obeys_any.append(obeys_any_type_0_item)

        else:
            obeys_any = self.obeys_any

        obeys_none: list[dict[str, Any]] | None | Unset
        if isinstance(self.obeys_none, Unset):
            obeys_none = UNSET
        elif isinstance(self.obeys_none, list):
            obeys_none = []
            for obeys_none_type_0_item_data in self.obeys_none:
                obeys_none_type_0_item = obeys_none_type_0_item_data.to_dict()
                obeys_none.append(obeys_none_type_0_item)

        else:
            obeys_none = self.obeys_none

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obeys_all is not UNSET:
            field_dict["obeysAll"] = obeys_all
        if obeys_any is not UNSET:
            field_dict["obeysAny"] = obeys_any
        if obeys_none is not UNSET:
            field_dict["obeysNone"] = obeys_none

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_search_body_search_params_employee_trends_type_0_obeys_all_type_0_item import (
            CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAllType0Item,
        )
        from ..models.company_search_body_search_params_employee_trends_type_0_obeys_any_type_0_item import (
            CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0Item,
        )
        from ..models.company_search_body_search_params_employee_trends_type_0_obeys_none_type_0_item import (
            CompanySearchBodySearchParamsEmployeeTrendsType0ObeysNoneType0Item,
        )

        d = dict(src_dict)

        def _parse_obeys_all(
            data: object,
        ) -> list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAllType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                obeys_all_type_0 = []
                _obeys_all_type_0 = data
                for obeys_all_type_0_item_data in _obeys_all_type_0:
                    obeys_all_type_0_item = CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAllType0Item.from_dict(
                        obeys_all_type_0_item_data
                    )

                    obeys_all_type_0.append(obeys_all_type_0_item)

                return obeys_all_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAllType0Item] | None | Unset, data)

        obeys_all = _parse_obeys_all(d.pop("obeysAll", UNSET))

        def _parse_obeys_any(
            data: object,
        ) -> list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                obeys_any_type_0 = []
                _obeys_any_type_0 = data
                for obeys_any_type_0_item_data in _obeys_any_type_0:
                    obeys_any_type_0_item = CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0Item.from_dict(
                        obeys_any_type_0_item_data
                    )

                    obeys_any_type_0.append(obeys_any_type_0_item)

                return obeys_any_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysAnyType0Item] | None | Unset, data)

        obeys_any = _parse_obeys_any(d.pop("obeysAny", UNSET))

        def _parse_obeys_none(
            data: object,
        ) -> list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysNoneType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                obeys_none_type_0 = []
                _obeys_none_type_0 = data
                for obeys_none_type_0_item_data in _obeys_none_type_0:
                    obeys_none_type_0_item = (
                        CompanySearchBodySearchParamsEmployeeTrendsType0ObeysNoneType0Item.from_dict(
                            obeys_none_type_0_item_data
                        )
                    )

                    obeys_none_type_0.append(obeys_none_type_0_item)

                return obeys_none_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanySearchBodySearchParamsEmployeeTrendsType0ObeysNoneType0Item] | None | Unset, data)

        obeys_none = _parse_obeys_none(d.pop("obeysNone", UNSET))

        company_search_body_search_params_employee_trends_type_0 = cls(
            obeys_all=obeys_all,
            obeys_any=obeys_any,
            obeys_none=obeys_none,
        )

        company_search_body_search_params_employee_trends_type_0.additional_properties = d
        return company_search_body_search_params_employee_trends_type_0

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
