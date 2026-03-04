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
  from ..models.sync_combined_search_body_company_params_accelerators_v2_type_0_any_of_type_0_item import SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0AnyOfType0Item
  from ..models.sync_combined_search_body_company_params_accelerators_v2_type_0_none_of_type_0_item import SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0NoneOfType0Item





T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0:
    """ 
        Attributes:
            any_of (Union[None, Unset, list['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0AnyOfType0Item']]):
            none_of (Union[None, Unset, list['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0NoneOfType0Item']]):
     """

    any_of: Union[None, Unset, list['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0AnyOfType0Item']] = UNSET
    none_of: Union[None, Unset, list['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0NoneOfType0Item']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_accelerators_v2_type_0_any_of_type_0_item import SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0AnyOfType0Item
        from ..models.sync_combined_search_body_company_params_accelerators_v2_type_0_none_of_type_0_item import SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0NoneOfType0Item
        any_of: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.any_of, Unset):
            any_of = UNSET
        elif isinstance(self.any_of, list):
            any_of = []
            for any_of_type_0_item_data in self.any_of:
                any_of_type_0_item = any_of_type_0_item_data.to_dict()
                any_of.append(any_of_type_0_item)


        else:
            any_of = self.any_of

        none_of: Union[None, Unset, list[dict[str, Any]]]
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
        field_dict.update({
        })
        if any_of is not UNSET:
            field_dict["anyOf"] = any_of
        if none_of is not UNSET:
            field_dict["noneOf"] = none_of

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_accelerators_v2_type_0_any_of_type_0_item import SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0AnyOfType0Item
        from ..models.sync_combined_search_body_company_params_accelerators_v2_type_0_none_of_type_0_item import SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0NoneOfType0Item
        d = dict(src_dict)
        def _parse_any_of(data: object) -> Union[None, Unset, list['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0AnyOfType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                any_of_type_0 = []
                _any_of_type_0 = data
                for any_of_type_0_item_data in (_any_of_type_0):
                    any_of_type_0_item = SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0AnyOfType0Item.from_dict(any_of_type_0_item_data)



                    any_of_type_0.append(any_of_type_0_item)

                return any_of_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0AnyOfType0Item']], data)

        any_of = _parse_any_of(d.pop("anyOf", UNSET))


        def _parse_none_of(data: object) -> Union[None, Unset, list['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0NoneOfType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                none_of_type_0 = []
                _none_of_type_0 = data
                for none_of_type_0_item_data in (_none_of_type_0):
                    none_of_type_0_item = SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0NoneOfType0Item.from_dict(none_of_type_0_item_data)



                    none_of_type_0.append(none_of_type_0_item)

                return none_of_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['SyncCombinedSearchBodyCompanyParamsAcceleratorsV2Type0NoneOfType0Item']], data)

        none_of = _parse_none_of(d.pop("noneOf", UNSET))


        sync_combined_search_body_company_params_accelerators_v2_type_0 = cls(
            any_of=any_of,
            none_of=none_of,
        )


        sync_combined_search_body_company_params_accelerators_v2_type_0.additional_properties = d
        return sync_combined_search_body_company_params_accelerators_v2_type_0

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
