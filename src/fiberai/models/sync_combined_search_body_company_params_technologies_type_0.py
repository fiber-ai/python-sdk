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
  from ..models.sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0
  from ..models.sync_combined_search_body_company_params_technologies_type_0_any_of_type_0_item_type_1 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType1
  from ..models.sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_1 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType1
  from ..models.sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0
  from ..models.sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_1 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1
  from ..models.sync_combined_search_body_company_params_technologies_type_0_any_of_type_0_item_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0





T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsTechnologiesType0")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsTechnologiesType0:
    """ 
        Attributes:
            any_of (Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0',
                'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType1']]]):
            all_of (Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0',
                'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1']]]):
            none_of (Union[None, Unset,
                list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0',
                'SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType1']]]):
     """

    any_of: Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType1']]] = UNSET
    all_of: Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1']]] = UNSET
    none_of: Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType1']]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0
        from ..models.sync_combined_search_body_company_params_technologies_type_0_any_of_type_0_item_type_1 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType1
        from ..models.sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_1 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType1
        from ..models.sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0
        from ..models.sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_1 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1
        from ..models.sync_combined_search_body_company_params_technologies_type_0_any_of_type_0_item_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0
        any_of: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.any_of, Unset):
            any_of = UNSET
        elif isinstance(self.any_of, list):
            any_of = []
            for any_of_type_0_item_data in self.any_of:
                any_of_type_0_item: dict[str, Any]
                if isinstance(any_of_type_0_item_data, SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0):
                    any_of_type_0_item = any_of_type_0_item_data.to_dict()
                else:
                    any_of_type_0_item = any_of_type_0_item_data.to_dict()

                any_of.append(any_of_type_0_item)


        else:
            any_of = self.any_of

        all_of: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.all_of, Unset):
            all_of = UNSET
        elif isinstance(self.all_of, list):
            all_of = []
            for all_of_type_0_item_data in self.all_of:
                all_of_type_0_item: dict[str, Any]
                if isinstance(all_of_type_0_item_data, SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0):
                    all_of_type_0_item = all_of_type_0_item_data.to_dict()
                else:
                    all_of_type_0_item = all_of_type_0_item_data.to_dict()

                all_of.append(all_of_type_0_item)


        else:
            all_of = self.all_of

        none_of: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.none_of, Unset):
            none_of = UNSET
        elif isinstance(self.none_of, list):
            none_of = []
            for none_of_type_0_item_data in self.none_of:
                none_of_type_0_item: dict[str, Any]
                if isinstance(none_of_type_0_item_data, SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0):
                    none_of_type_0_item = none_of_type_0_item_data.to_dict()
                else:
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
        if all_of is not UNSET:
            field_dict["allOf"] = all_of
        if none_of is not UNSET:
            field_dict["noneOf"] = none_of

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0
        from ..models.sync_combined_search_body_company_params_technologies_type_0_any_of_type_0_item_type_1 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType1
        from ..models.sync_combined_search_body_company_params_technologies_type_0_none_of_type_0_item_type_1 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType1
        from ..models.sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0
        from ..models.sync_combined_search_body_company_params_technologies_type_0_all_of_type_0_item_type_1 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1
        from ..models.sync_combined_search_body_company_params_technologies_type_0_any_of_type_0_item_type_0 import SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0
        d = dict(src_dict)
        def _parse_any_of(data: object) -> Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType1']]]:
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
                    def _parse_any_of_type_0_item(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType1']:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            any_of_type_0_item_type_0 = SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0.from_dict(data)



                            return any_of_type_0_item_type_0
                        except: # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        any_of_type_0_item_type_1 = SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType1.from_dict(data)



                        return any_of_type_0_item_type_1

                    any_of_type_0_item = _parse_any_of_type_0_item(any_of_type_0_item_data)

                    any_of_type_0.append(any_of_type_0_item)

                return any_of_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AnyOfType0ItemType1']]], data)

        any_of = _parse_any_of(d.pop("anyOf", UNSET))


        def _parse_all_of(data: object) -> Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1']]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                all_of_type_0 = []
                _all_of_type_0 = data
                for all_of_type_0_item_data in (_all_of_type_0):
                    def _parse_all_of_type_0_item(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1']:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            all_of_type_0_item_type_0 = SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0.from_dict(data)



                            return all_of_type_0_item_type_0
                        except: # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        all_of_type_0_item_type_1 = SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1.from_dict(data)



                        return all_of_type_0_item_type_1

                    all_of_type_0_item = _parse_all_of_type_0_item(all_of_type_0_item_data)

                    all_of_type_0.append(all_of_type_0_item)

                return all_of_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0AllOfType0ItemType1']]], data)

        all_of = _parse_all_of(d.pop("allOf", UNSET))


        def _parse_none_of(data: object) -> Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType1']]]:
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
                    def _parse_none_of_type_0_item(data: object) -> Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType1']:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            none_of_type_0_item_type_0 = SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0.from_dict(data)



                            return none_of_type_0_item_type_0
                        except: # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        none_of_type_0_item_type_1 = SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType1.from_dict(data)



                        return none_of_type_0_item_type_1

                    none_of_type_0_item = _parse_none_of_type_0_item(none_of_type_0_item_data)

                    none_of_type_0.append(none_of_type_0_item)

                return none_of_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[Union['SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType0', 'SyncCombinedSearchBodyCompanyParamsTechnologiesType0NoneOfType0ItemType1']]], data)

        none_of = _parse_none_of(d.pop("noneOf", UNSET))


        sync_combined_search_body_company_params_technologies_type_0 = cls(
            any_of=any_of,
            all_of=all_of,
            none_of=none_of,
        )


        sync_combined_search_body_company_params_technologies_type_0.additional_properties = d
        return sync_combined_search_body_company_params_technologies_type_0

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
