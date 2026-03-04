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
  from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_2 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2
  from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_1 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1
  from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_0 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0
  from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_3 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType3
  from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_1 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1
  from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_2 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2
  from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_0 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0
  from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_3 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType3





T = TypeVar("T", bound="TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0")



@_attrs_define
class TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0:
    """ 
        Attributes:
            any_of (Union[None, Unset,
                list[Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0',
                'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1',
                'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2',
                'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType3']]]):
            none_of (Union[None, Unset,
                list[Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0',
                'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1',
                'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2',
                'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType3']]]):
     """

    any_of: Union[None, Unset, list[Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType3']]] = UNSET
    none_of: Union[None, Unset, list[Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType3']]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_2 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_1 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_0 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_3 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType3
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_1 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_2 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_0 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_3 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType3
        any_of: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.any_of, Unset):
            any_of = UNSET
        elif isinstance(self.any_of, list):
            any_of = []
            for any_of_type_0_item_data in self.any_of:
                any_of_type_0_item: dict[str, Any]
                if isinstance(any_of_type_0_item_data, TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0):
                    any_of_type_0_item = any_of_type_0_item_data.to_dict()
                elif isinstance(any_of_type_0_item_data, TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1):
                    any_of_type_0_item = any_of_type_0_item_data.to_dict()
                elif isinstance(any_of_type_0_item_data, TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2):
                    any_of_type_0_item = any_of_type_0_item_data.to_dict()
                else:
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
                none_of_type_0_item: dict[str, Any]
                if isinstance(none_of_type_0_item_data, TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0):
                    none_of_type_0_item = none_of_type_0_item_data.to_dict()
                elif isinstance(none_of_type_0_item_data, TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1):
                    none_of_type_0_item = none_of_type_0_item_data.to_dict()
                elif isinstance(none_of_type_0_item_data, TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2):
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
        if none_of is not UNSET:
            field_dict["noneOf"] = none_of

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_2 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_1 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_0 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_3 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType3
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_1 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_2 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_any_of_type_0_item_type_0 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0
        from ..models.text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0_none_of_type_0_item_type_3 import TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType3
        d = dict(src_dict)
        def _parse_any_of(data: object) -> Union[None, Unset, list[Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType3']]]:
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
                    def _parse_any_of_type_0_item(data: object) -> Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType3']:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            any_of_type_0_item_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0.from_dict(data)



                            return any_of_type_0_item_type_0
                        except: # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            any_of_type_0_item_type_1 = TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1.from_dict(data)



                            return any_of_type_0_item_type_1
                        except: # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            any_of_type_0_item_type_2 = TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2.from_dict(data)



                            return any_of_type_0_item_type_2
                        except: # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        any_of_type_0_item_type_3 = TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType3.from_dict(data)



                        return any_of_type_0_item_type_3

                    any_of_type_0_item = _parse_any_of_type_0_item(any_of_type_0_item_data)

                    any_of_type_0.append(any_of_type_0_item)

                return any_of_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType0', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType1', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType2', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0AnyOfType0ItemType3']]], data)

        any_of = _parse_any_of(d.pop("anyOf", UNSET))


        def _parse_none_of(data: object) -> Union[None, Unset, list[Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType3']]]:
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
                    def _parse_none_of_type_0_item(data: object) -> Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType3']:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            none_of_type_0_item_type_0 = TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0.from_dict(data)



                            return none_of_type_0_item_type_0
                        except: # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            none_of_type_0_item_type_1 = TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1.from_dict(data)



                            return none_of_type_0_item_type_1
                        except: # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            none_of_type_0_item_type_2 = TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2.from_dict(data)



                            return none_of_type_0_item_type_2
                        except: # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        none_of_type_0_item_type_3 = TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType3.from_dict(data)



                        return none_of_type_0_item_type_3

                    none_of_type_0_item = _parse_none_of_type_0_item(none_of_type_0_item_data)

                    none_of_type_0.append(none_of_type_0_item)

                return none_of_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[Union['TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType0', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType1', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType2', 'TextToCompanySearchParamsResponse200OutputSearchParamsExactCompanyV2Type0NoneOfType0ItemType3']]], data)

        none_of = _parse_none_of(d.pop("noneOf", UNSET))


        text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0 = cls(
            any_of=any_of,
            none_of=none_of,
        )


        text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0.additional_properties = d
        return text_to_company_search_params_response_200_output_search_params_exact_company_v2_type_0

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
