from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.company_count_body_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0 import CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0
  from ..models.company_count_body_search_params_headquarters_location_type_0_union_all_type_0_item_type_0 import CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0





T = TypeVar("T", bound="CompanyCountBodySearchParamsHeadquartersLocationType0")



@_attrs_define
class CompanyCountBodySearchParamsHeadquartersLocationType0:
    """ 
        Attributes:
            union_all (Union[None, Unset,
                list['CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0']]):
            subtract_all (Union[None, Unset,
                list['CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0']]):
     """

    union_all: Union[None, Unset, list['CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0']] = UNSET
    subtract_all: Union[None, Unset, list['CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_count_body_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0 import CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0
        from ..models.company_count_body_search_params_headquarters_location_type_0_union_all_type_0_item_type_0 import CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0
        union_all: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.union_all, Unset):
            union_all = UNSET
        elif isinstance(self.union_all, list):
            union_all = []
            for union_all_type_0_item_data in self.union_all:
                union_all_type_0_item: dict[str, Any]
                if isinstance(union_all_type_0_item_data, CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0):
                    union_all_type_0_item = union_all_type_0_item_data.to_dict()

                union_all.append(union_all_type_0_item)


        else:
            union_all = self.union_all

        subtract_all: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.subtract_all, Unset):
            subtract_all = UNSET
        elif isinstance(self.subtract_all, list):
            subtract_all = []
            for subtract_all_type_0_item_data in self.subtract_all:
                subtract_all_type_0_item: dict[str, Any]
                if isinstance(subtract_all_type_0_item_data, CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0):
                    subtract_all_type_0_item = subtract_all_type_0_item_data.to_dict()

                subtract_all.append(subtract_all_type_0_item)


        else:
            subtract_all = self.subtract_all


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if union_all is not UNSET:
            field_dict["unionAll"] = union_all
        if subtract_all is not UNSET:
            field_dict["subtractAll"] = subtract_all

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_count_body_search_params_headquarters_location_type_0_subtract_all_type_0_item_type_0 import CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0
        from ..models.company_count_body_search_params_headquarters_location_type_0_union_all_type_0_item_type_0 import CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0
        d = dict(src_dict)
        def _parse_union_all(data: object) -> Union[None, Unset, list['CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                union_all_type_0 = []
                _union_all_type_0 = data
                for union_all_type_0_item_data in (_union_all_type_0):
                    def _parse_union_all_type_0_item(data: object) -> 'CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0':
                        if not isinstance(data, dict):
                            raise TypeError()
                        union_all_type_0_item_type_0 = CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0.from_dict(data)



                        return union_all_type_0_item_type_0

                    union_all_type_0_item = _parse_union_all_type_0_item(union_all_type_0_item_data)

                    union_all_type_0.append(union_all_type_0_item)

                return union_all_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['CompanyCountBodySearchParamsHeadquartersLocationType0UnionAllType0ItemType0']], data)

        union_all = _parse_union_all(d.pop("unionAll", UNSET))


        def _parse_subtract_all(data: object) -> Union[None, Unset, list['CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subtract_all_type_0 = []
                _subtract_all_type_0 = data
                for subtract_all_type_0_item_data in (_subtract_all_type_0):
                    def _parse_subtract_all_type_0_item(data: object) -> 'CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0':
                        if not isinstance(data, dict):
                            raise TypeError()
                        subtract_all_type_0_item_type_0 = CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0.from_dict(data)



                        return subtract_all_type_0_item_type_0

                    subtract_all_type_0_item = _parse_subtract_all_type_0_item(subtract_all_type_0_item_data)

                    subtract_all_type_0.append(subtract_all_type_0_item)

                return subtract_all_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['CompanyCountBodySearchParamsHeadquartersLocationType0SubtractAllType0ItemType0']], data)

        subtract_all = _parse_subtract_all(d.pop("subtractAll", UNSET))


        company_count_body_search_params_headquarters_location_type_0 = cls(
            union_all=union_all,
            subtract_all=subtract_all,
        )


        company_count_body_search_params_headquarters_location_type_0.additional_properties = d
        return company_count_body_search_params_headquarters_location_type_0

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
