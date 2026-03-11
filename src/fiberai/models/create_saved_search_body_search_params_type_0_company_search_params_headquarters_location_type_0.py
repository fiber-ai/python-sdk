from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0,
    )
    from ..models.create_saved_search_body_search_params_type_0_company_search_params_headquarters_location_type_0_union_all_type_0_item_type_0 import (
        CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0")


@_attrs_define
class CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0:
    """
    Attributes:
        union_all
            (list[CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0]
            | None | Unset):
        subtract_all (list[CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAll
            Type0ItemType0] | None | Unset):
    """

    union_all: (
        list[CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0]
        | None
        | Unset
    ) = UNSET
    subtract_all: (
        list[
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0
        ]
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0,
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_headquarters_location_type_0_union_all_type_0_item_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0,
        )

        union_all: list[dict[str, Any]] | None | Unset
        if isinstance(self.union_all, Unset):
            union_all = UNSET
        elif isinstance(self.union_all, list):
            union_all = []
            for union_all_type_0_item_data in self.union_all:
                union_all_type_0_item: dict[str, Any]
                if isinstance(
                    union_all_type_0_item_data,
                    CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0,
                ):
                    union_all_type_0_item = union_all_type_0_item_data.to_dict()

                union_all.append(union_all_type_0_item)

        else:
            union_all = self.union_all

        subtract_all: list[dict[str, Any]] | None | Unset
        if isinstance(self.subtract_all, Unset):
            subtract_all = UNSET
        elif isinstance(self.subtract_all, list):
            subtract_all = []
            for subtract_all_type_0_item_data in self.subtract_all:
                subtract_all_type_0_item: dict[str, Any]
                if isinstance(
                    subtract_all_type_0_item_data,
                    CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0,
                ):
                    subtract_all_type_0_item = subtract_all_type_0_item_data.to_dict()

                subtract_all.append(subtract_all_type_0_item)

        else:
            subtract_all = self.subtract_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if union_all is not UNSET:
            field_dict["unionAll"] = union_all
        if subtract_all is not UNSET:
            field_dict["subtractAll"] = subtract_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0,
        )
        from ..models.create_saved_search_body_search_params_type_0_company_search_params_headquarters_location_type_0_union_all_type_0_item_type_0 import (
            CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0,
        )

        d = dict(src_dict)

        def _parse_union_all(
            data: object,
        ) -> (
            list[
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                union_all_type_0 = []
                _union_all_type_0 = data
                for union_all_type_0_item_data in _union_all_type_0:

                    def _parse_union_all_type_0_item(
                        data: object,
                    ) -> CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0:
                        if not isinstance(data, dict):
                            raise TypeError()
                        union_all_type_0_item_type_0 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0.from_dict(
                            data
                        )

                        return union_all_type_0_item_type_0

                    union_all_type_0_item = _parse_union_all_type_0_item(union_all_type_0_item_data)

                    union_all_type_0.append(union_all_type_0_item)

                return union_all_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0UnionAllType0ItemType0
                ]
                | None
                | Unset,
                data,
            )

        union_all = _parse_union_all(d.pop("unionAll", UNSET))

        def _parse_subtract_all(
            data: object,
        ) -> (
            list[
                CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subtract_all_type_0 = []
                _subtract_all_type_0 = data
                for subtract_all_type_0_item_data in _subtract_all_type_0:

                    def _parse_subtract_all_type_0_item(
                        data: object,
                    ) -> CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0:
                        if not isinstance(data, dict):
                            raise TypeError()
                        subtract_all_type_0_item_type_0 = CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0.from_dict(
                            data
                        )

                        return subtract_all_type_0_item_type_0

                    subtract_all_type_0_item = _parse_subtract_all_type_0_item(subtract_all_type_0_item_data)

                    subtract_all_type_0.append(subtract_all_type_0_item)

                return subtract_all_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    CreateSavedSearchBodySearchParamsType0CompanySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0
                ]
                | None
                | Unset,
                data,
            )

        subtract_all = _parse_subtract_all(d.pop("subtractAll", UNSET))

        create_saved_search_body_search_params_type_0_company_search_params_headquarters_location_type_0 = cls(
            union_all=union_all,
            subtract_all=subtract_all,
        )

        create_saved_search_body_search_params_type_0_company_search_params_headquarters_location_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_0_company_search_params_headquarters_location_type_0

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
